from lexer import Lexer
from parser import Parser
from codegen import CodeGen


fname = "input.toy"
with open(fname) as f:
    text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
codegen = CodeGen()

module = codegen.module
builder = codegen.builder
printf = codegen.printf

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

coedgen.create_ir()
codegen.save_ir("output.ll")
