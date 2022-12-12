import lexer
import RDA

class Compiler:
    f3 = open("test3.txt")
    f4 = open("test4.txt")
    # Change the file name below to test the different files
    text = f4.read()
    lex = lexer.Lexer(text)
    result = lexer.run(text)
    print(result)
    parser = RDA.Parser(result)
    print(parser.start())