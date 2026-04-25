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
        
    # 4. MATEMATIKA (Např. a + 5)
    def visitAddSubConcatExpression(self, ctx: PLCParser.AddSubConcatExpressionContext):
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        operator = ctx.op.text

        if operator == '.':
            self.instructions.append("concat")
            return 'string'
        elif operator == '+':
            type_code = left_type[0].upper()
            self.instructions.append(f"add {type_code}")
            return left_type
        elif operator == '-':
            type_code = left_type[0].upper()
            self.instructions.append(f"sub {type_code}")
            return left_type

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