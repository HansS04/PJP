# Proměnné, ať to můžeme snadno měnit
ANTLR = antlr-4.13.2-complete.jar
GRAMMAR = PLC.g4

# Výchozí pravidlo (spustí se, když napíšeš jen "make")
all: generate

# Pravidlo pro generování Python kódu
generate:
	java -jar $(ANTLR) -Dlanguage=Python3 -visitor $(GRAMMAR)

# Pravidlo pro úklid (smaže vygenerované soubory)
clean:
	rm -f PLC*.py *.interp *.tokens
	rm -rf __pycache__