from antlr4 import *
from FiveStarLexer import FiveStarLexer
from FiveStarParser import FiveStarParser
from FiveStarListener import FiveStarListener

# Read from sample.txt
input_stream = FileStream("sample.txt")
lexer = FiveStarLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = FiveStarParser(tokens)

# Parse
tree = parser.program()

# Print the parse tree
print(tree.toStringTree(recog=parser))