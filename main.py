import re
import sys

from antlr4.InputStream import InputStream
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.tree.Tree import ParseTreeWalker

from pascalLexer import pascalLexer
from pascalListener import pascalListener
from pascalParser import pascalParser

KEYWORDS = (
    'var', 'integer', 'int64',
    'begin', 'end',
    'readln', 'writeln',
    'mod', 'div', 'or', 'and',
    'if', 'then', 'else', 'while', 'do',
)


class Listener(pascalListener):
    def __init__(self):
        self.var_ls = {}
        self.spaces = -4

    def exitVariableDeclaration(self, ctx: pascalParser.VariableDeclarationContext):
        var_type = ctx.varType().getText()
        for i in ctx.identifierList().getText().split(','):
            self.var_ls[i] = var_type

    def exitWritelnReadln(self, ctx: pascalParser.WritelnReadlnContext):
        var = ctx.ID().getText()
        const = ctx.CONST_STR().getText()
        self._print_input(var, const)

    def enterReadln(self, ctx: pascalParser.ReadlnContext):
        for i in ctx.identifierList().getText().split(','):
            self._print_input(i)

    def exitWriteln(self, ctx: pascalParser.WritelnContext):
        self._print('print({})'.format(ctx.expressions().getText()))

    def exitAssignmentStatement(self, ctx: pascalParser.AssignmentStatementContext):
        var = ctx.ID().getText()
        expr = ctx.expression().getText()
        self._print(f'{var} = {expr}')

    def enterWhileStatement(self, ctx: pascalParser.WhileStatementContext):
        self._print(f'while {ctx.expression().getText()}:')

    def enterIfStatement(self, ctx: pascalParser.IfStatementContext):
        self._print(f'if {ctx.expression().getText()}:')

    def enterElseStatement(self, ctx: pascalParser.ElseStatementContext):
        self._print('else:')

    def enterBlock(self, ctx: pascalParser.BlockContext):
        self.spaces += 4

    def exitBlock(self, ctx: pascalParser.BlockContext):
        self.spaces -= 4

    def enterBlockBody(self, ctx: pascalParser.BlockBodyContext):
        self.spaces += 4

    def exitBlockBody(self, ctx: pascalParser.BlockBodyContext):
        self.spaces -= 4

    def _print_input(self, var, const=None):
        const = const or ''
        var_type = self._get_var_type(var)
        if var_type:
            self._print(f'{var} = {var_type}(input({const}))')
        else:
            raise NotImplementedError

    def _get_var_type(self, var):
        try:
            var_type = self.var_ls[var]
        except KeyError:
            raise ValueError(f'variable {var} not defined')
        if var_type in ('integer', 'int64'):
            return 'int'
        else:
            raise NotImplementedError(var_type)

    def _print(self, line):
        with open("result.py","a") as f:
            code = ' ' * self.spaces + line + "\n"
            f.write(code)
        #print(' ' * self.spaces, line, sep='')


def main(filename):
    with open(filename) as f:
        text = f.read()
    text = re.sub(r'\b({})\b'.format(r'|'.join(KEYWORDS)), lambda m: m.group().lower(), text, flags=re.IGNORECASE)
    #print(text)
    text = text.replace('div', '//').replace('mod', '%')

    lexer = pascalLexer(InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = pascalParser(stream)
    tree = parser.program()
    listener = Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        # main('test1.pas')
        # main('test2.pas')
        # main('test3.pas')
        main('test4.pas')
