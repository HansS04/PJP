import sys
from antlr4 import *
from PLCLexer import PLCLexer
from PLCParser import PLCParser
from PLCVisitor import PLCVisitor

class MyCompiler(PLCVisitor):
    
    # 1. INICIALIZACE (Vytvoření naší paměti - tohle ti chybělo!)
    def __init__(self):
        self.instructions = [] # Sem ukládáme instrukce (push, add, atd.)
        self.variables = {}    # Sem ukládáme proměnné a jejich typy
        self.label_counter = 0 # Pro generování unikátních štítků (labelů) pro podmínky a smyčky

    # 2. DEKLARACE PROMĚNNÝCH (Např. int a, b;)
    def visitDeclarationStatement(self, ctx: PLCParser.DeclarationStatementContext):
        var_type = ctx.type_spec().getText()
        
        for var_node in ctx.ID():
            var_name = var_node.getText()
            
            if var_name in self.variables:
                print(f"Error: Proměnná '{var_name}' již byla deklarována!")
                sys.exit(1)
                
            self.variables[var_name] = var_type
            
            # Výchozí hodnoty podle zadání
            if var_type == 'int': self.instructions.append("push I 0")
            elif var_type == 'float': self.instructions.append("push F 0.0")
            elif var_type == 'bool': self.instructions.append("push B false")
            elif var_type == 'string': self.instructions.append('push S ""')
                
            self.instructions.append(f"save {var_name}")
        return None

    # 3. PŘIŘAZENÍ (Např. a = 5)
    def visitAssignmentExpression(self, ctx: PLCParser.AssignmentExpressionContext):
        var_name = ctx.expression(0).getText()

        # Zde musí být 'not in', ptáme se, jestli NEEXISTUJE
        if var_name not in self.variables:
            print(f"Error: Proměnná '{var_name}' neexistuje!")
            sys.exit(1)

        # Zpracujeme pravou stranu
        right_type = self.visit(ctx.expression(1))
        
        self.instructions.append(f"save {var_name}")
        return self.variables[var_name]
    
    def visitFloatExpression(self, ctx: PLCParser.FloatExpressionContext):
        hodnota = ctx.FLOAT_LITERAL().getText()
        self.instructions.append(f"push F {hodnota}")
        return 'float'
    
    def visitStringExpression(self, ctx: PLCParser.StringExpressionContext):
        hodnota = ctx.STRING_LITERAL().getText()
        self.instructions.append(f'push S {hodnota}')
        return 'string'
    
    def visitBoolExpression(self, ctx: PLCParser.BoolExpressionContext):
        hodnota = ctx.BOOL_LITERAL().getText()
        self.instructions.append(f'push B {hodnota}')
        return 'bool'

    # 5. ČTENÍ SAMOTNÉHO ČÍSLA (Tohle je nutné, aby mohl fungovat výpočet a = 5)
    def visitIntExpression(self, ctx: PLCParser.IntExpressionContext):
        hodnota = ctx.INT_LITERAL().getText()
        self.instructions.append(f"push I {hodnota}")
        return 'int'

    # 6. ČTENÍ HODNOTY Z PROMĚNNÉ (Nutné pro výpočet např. a + 5)
    def visitIdExpression(self, ctx: PLCParser.IdExpressionContext):
        var_name = ctx.ID().getText()
        if var_name not in self.variables:
            print(f"Error: Pokus o použití nedeklarované proměnné '{var_name}'!")
            sys.exit(1)
            
        self.instructions.append(f"load {var_name}")
        return self.variables[var_name]

    # 7. VÝPIS NA OBRAZOVKU (Např. write a + 5;)
    def visitWriteStatement(self, ctx: PLCParser.WriteStatementContext):
        expr_count = len(ctx.expression())
        for expr in ctx.expression():
            self.visit(expr)
        self.instructions.append(f"print {expr_count}")
        return None
    
    def visitAddSubConcatExpression(self, ctx: PLCParser.AddSubConcatExpressionContext):
        # 1. Zpracujeme levou stranu
        left_type = self.visit(ctx.expression(0))

        # TRIK: Zapamatujeme si, na kterém řádku v seznamu instrukcí právě jsme
        right_start_index = len(self.instructions)

        # 2. Zpracujeme pravou stranu
        right_type = self.visit(ctx.expression(1))
        
        operator = ctx.op.text

        # Pokud jde o spojování textu, nic nepřetypováváme
        if operator == '.':
            self.instructions.append("concat")
            return 'string'

        # 3. PŘETYPOVÁNÍ (Type Casting)
        result_type = left_type # Výchozí předpoklad (když jsou oba int, výsledek je int)
        
        #Nalevo int, napravo float (např. 5 + 3.5)
        if left_type == 'int' and right_type == 'float':
            # Vložíme 'itof' PŘESNĚ MEZI NĚ (na pozici right_start_index)!
            self.instructions.insert(right_start_index, "itof")
            result_type = 'float'
            
        # Nalevo float, napravo int (např. 3.5 + 5)
        elif left_type == 'float' and right_type == 'int':
            # Int je na vrcholu zásobníku, stačí 'itof' prostě přidat na konec
            self.instructions.append("itof")
            result_type = 'float'
            
        # (Pokud jsou oba int, nebo oba float, neděláme nic a result_type zůstane původní)

        # 4. Samotný výpočet
        type_code = result_type[0].upper() # Bude to 'I' pro int+int, a 'F' pokud tam byl aspoň jeden float
        
        if operator == '+':
            self.instructions.append(f"add {type_code}")
        elif operator == '-':
            self.instructions.append(f"sub {type_code}")
            
        return result_type
    

    def visitMulDivModExpression(self, ctx: PLCParser.MulDivModExpressionContext):
        left_type = self.visit(ctx.expression(0))
        right_start_index = len(self.instructions) # TRIK PRO ITOF
        right_type = self.visit(ctx.expression(1))
        operator = ctx.op.text

        if operator == '%':
            self.instructions.append("mod")
            return 'int'
        
        # PŘETYPOVÁNÍ (Type Casting)
        result_type = left_type
        if left_type == 'int' and right_type == 'float':
            self.instructions.insert(right_start_index, "itof")
            result_type = 'float'
        elif left_type == 'float' and right_type == 'int':
            self.instructions.append("itof")
            result_type = 'float'

        type_code = result_type[0].upper()
        if operator == '*':
            self.instructions.append(f"mul {type_code}")
        elif operator == '/':
            self.instructions.append(f"div {type_code}")
        
        return result_type

    # POROVNÁVÁNÍ (<, >) s itof
    def visitComparisonExpression(self, ctx: PLCParser.ComparisonExpressionContext):
        left_type = self.visit(ctx.expression(0))
        right_start_index = len(self.instructions)
        right_type = self.visit(ctx.expression(1))
        operator = ctx.op.text
        
        result_type = left_type
        if left_type == 'int' and right_type == 'float':
            self.instructions.insert(right_start_index, "itof")
            result_type = 'float'
        elif left_type == 'float' and right_type == 'int':
            self.instructions.append("itof")
            result_type = 'float'

        type_code = result_type[0].upper()

        if operator == '<':
            self.instructions.append(f"lt {type_code}")
        elif operator == '>':
            self.instructions.append(f"gt {type_code}")
            
        return 'bool' # Výsledek porovnávání je vždy bool

    # ROVNOST A NEROVNOST (==, !=) s itof
    def visitEqualityExpression(self, ctx: PLCParser.EqualityExpressionContext):
        left_type = self.visit(ctx.expression(0))
        right_start_index = len(self.instructions)
        right_type = self.visit(ctx.expression(1))
        operator = ctx.op.text
        
        result_type = left_type
        # Tady děláme itof jen pokud porovnáváme čísla (aby to nespadlo na stringu)
        if left_type in ['int', 'float'] and right_type in ['int', 'float']:
            if left_type == 'int' and right_type == 'float':
                self.instructions.insert(right_start_index, "itof")
                result_type = 'float'
            elif left_type == 'float' and right_type == 'int':
                self.instructions.append("itof")
                result_type = 'float'

        type_code = result_type[0].upper()

        self.instructions.append(f"eq {type_code}")
        
        if operator == '!=':
            self.instructions.append("not")
            
        return 'bool'

    # LOGICKÉ AND (&&) a OR (||)
    def visitAndExpression(self, ctx: PLCParser.AndExpressionContext):
        self.visit(ctx.expression(0))
        self.visit(ctx.expression(1))
        self.instructions.append("and")
        return 'bool'

    def visitOrExpression(self, ctx: PLCParser.OrExpressionContext):
        self.visit(ctx.expression(0))
        self.visit(ctx.expression(1))
        self.instructions.append("or")
        return 'bool'

    # UNÁRNÍ MÍNUS A NOT (např. -5, !true)
    def visitUnaryExpression(self, ctx: PLCParser.UnaryExpressionContext):
        operator = ctx.getChild(0).getText()
        expr_type = self.visit(ctx.expression())

        if operator == '-':
            type_code = expr_type[0].upper()
            self.instructions.append(f"uminus {type_code}")
            return expr_type
        elif operator == '!':
            self.instructions.append("not")
            return 'bool'

    def get_new_label(self):
        self.label_counter += 1
        return self.label_counter

    def visitBlockStatement(self, ctx: PLCParser.BlockStatementContext):
        for statement in ctx.statement():
            self.visit(statement)
        return None
    
    def visitIfStatement(self, ctx: PLCParser.IfStatementContext):
        condition_type = self.visit(ctx.expression())
        
        if condition_type != 'bool':
            print("Error: Podmínka v příkazu 'if' musí být typu bool")
            sys.exit(1)

        label_false = self.get_new_label()

        self.instructions.append(f"fjmp {label_false}")

        # 5. KROK: Tělo IFu (Co se má stát, když je to TRUE)
        self.visit(ctx.statement(0))

        # 6. KROK: Zjišťujeme, jestli programátor napsal i ELSE (Jinak)
        if ctx.statement(1): # Pokud existuje druhé 'statement', znamená to ELSE
            
            # 7. KROK: Máme ELSE, je to složitější!
            # Vytiskneme si druhý lepík pro úplný konec celé podmínky
            label_end = self.get_new_label() 
            
            # Úředník právě dodělal TRUE část. Nesmí jít dělat i FALSE část!
            # Dáme mu tvrdý příkaz přeskočit to celé až na konec.
            self.instructions.append(f"jmp {label_end}") 

            # Sem konečně NALEPÍME ten náš první lepík z kroku 3!
            # Sem přistane úředník, pokud na začátku uviděl FALSE.
            self.instructions.append(f"label {label_false}")
            
            # Pošleme panáčka zpracovat vnitřek ELSE části
            self.visit(ctx.statement(1))
            
            # Sem nalepíme lepík pro úplný konec.
            # Sem přistane úředník, pokud šel přes TRUE část a přeskočil ELSE.
            self.instructions.append(f"label {label_end}")


        else:
            # 8. KROK: Obyčejný IF bez ELSE
            # Nemáme žádné "Jinak". Takže prostě jen vezmeme ten lepík z kroku 3 
            # a nalepíme ho sem na konec, ať má úředník po 'fjmp' kam dopadnout.
            self.instructions.append(f"label {label_false}")

        return None
    
  
    def visitWhileStatement(self, ctx: PLCParser.WhileStatementContext):
            label_start = self.get_new_label()
            label_end = self.get_new_label()

            self.instructions.append(f"label {label_start}")

            condition_type = self.visit(ctx.expression())
            if condition_type != 'bool':
                print("Error: Podmínka v příkazu 'while' musí být bool!")
                sys.exit(1)

            self.instructions.append(f"fjmp {label_end}")
            self.visit(ctx.statement())
            self.instructions.append(f"jmp {label_start}")
            self.instructions.append(f"label {label_end}")

            return None

    # VÝRAZ POUŽITÝ JAKO PŘÍKAZ (musíme po něm uklidit zásobník)
    def visitExpressionStatement(self, ctx: PLCParser.ExpressionStatementContext):
        self.visit(ctx.expression())
        # Výraz zanechal na zásobníku hodnotu. Protože výsledek nikam neukládáme,
        # musíme vygenerovat instrukci 'pop', která tu hodnotu zahodí.
        self.instructions.append("pop")
        return None

    # ČTENÍ VSTUPU OD UŽIVATELE (read)
    def visitReadStatement(self, ctx: PLCParser.ReadStatementContext):
        for var_node in ctx.ID():
            var_name = var_node.getText()
            
            # Kontrola, jestli proměnná existuje
            if var_name not in self.variables:
                print(f"Error: Proměnná '{var_name}' v příkazu read neexistuje!")
                sys.exit(1)
                
            var_type = self.variables[var_name]
            type_code = var_type[0].upper() # Z 'int' udělá 'I', atd.
            
            # Vygenerujeme instrukci pro přečtení z klávesnice
            self.instructions.append(f"read {type_code}")
            # A hned to uložíme do dané proměnné
            self.instructions.append(f"save {var_name}")
            
        return None

def main():
    input_stream = FileStream("test.plc")
    lexer = PLCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PLCParser(stream)
    tree = parser.program()
    
    compiler = MyCompiler()
    compiler.visit(tree)
    
    # Zápis instrukcí do souboru
    with open("output.out", "w") as f:
        for instr in compiler.instructions:
            f.write(instr + "\n")
            
    print("Preklad uspesny! Instrukce jsou v souboru output.out")

if __name__ == '__main__':
    main()