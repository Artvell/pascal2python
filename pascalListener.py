# Generated from pascal.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pascalParser import pascalParser
else:
    from pascalParser import pascalParser

# This class defines a complete listener for a parse tree produced by pascalParser.
class pascalListener(ParseTreeListener):

    # Enter a parse tree produced by pascalParser#program.
    def enterProgram(self, ctx:pascalParser.ProgramContext):
        pass

    # Exit a parse tree produced by pascalParser#program.
    def exitProgram(self, ctx:pascalParser.ProgramContext):
        pass


    # Enter a parse tree produced by pascalParser#variableDeclarationPart.
    def enterVariableDeclarationPart(self, ctx:pascalParser.VariableDeclarationPartContext):
        pass

    # Exit a parse tree produced by pascalParser#variableDeclarationPart.
    def exitVariableDeclarationPart(self, ctx:pascalParser.VariableDeclarationPartContext):
        pass


    # Enter a parse tree produced by pascalParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:pascalParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by pascalParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:pascalParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by pascalParser#identifierList.
    def enterIdentifierList(self, ctx:pascalParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by pascalParser#identifierList.
    def exitIdentifierList(self, ctx:pascalParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by pascalParser#varType.
    def enterVarType(self, ctx:pascalParser.VarTypeContext):
        pass

    # Exit a parse tree produced by pascalParser#varType.
    def exitVarType(self, ctx:pascalParser.VarTypeContext):
        pass


    # Enter a parse tree produced by pascalParser#block.
    def enterBlock(self, ctx:pascalParser.BlockContext):
        pass

    # Exit a parse tree produced by pascalParser#block.
    def exitBlock(self, ctx:pascalParser.BlockContext):
        pass


    # Enter a parse tree produced by pascalParser#statements.
    def enterStatements(self, ctx:pascalParser.StatementsContext):
        pass

    # Exit a parse tree produced by pascalParser#statements.
    def exitStatements(self, ctx:pascalParser.StatementsContext):
        pass


    # Enter a parse tree produced by pascalParser#statement.
    def enterStatement(self, ctx:pascalParser.StatementContext):
        pass

    # Exit a parse tree produced by pascalParser#statement.
    def exitStatement(self, ctx:pascalParser.StatementContext):
        pass


    # Enter a parse tree produced by pascalParser#writelnReadln.
    def enterWritelnReadln(self, ctx:pascalParser.WritelnReadlnContext):
        pass

    # Exit a parse tree produced by pascalParser#writelnReadln.
    def exitWritelnReadln(self, ctx:pascalParser.WritelnReadlnContext):
        pass


    # Enter a parse tree produced by pascalParser#readln.
    def enterReadln(self, ctx:pascalParser.ReadlnContext):
        pass

    # Exit a parse tree produced by pascalParser#readln.
    def exitReadln(self, ctx:pascalParser.ReadlnContext):
        pass


    # Enter a parse tree produced by pascalParser#writeln.
    def enterWriteln(self, ctx:pascalParser.WritelnContext):
        pass

    # Exit a parse tree produced by pascalParser#writeln.
    def exitWriteln(self, ctx:pascalParser.WritelnContext):
        pass


    # Enter a parse tree produced by pascalParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:pascalParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:pascalParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#expressions.
    def enterExpressions(self, ctx:pascalParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by pascalParser#expressions.
    def exitExpressions(self, ctx:pascalParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by pascalParser#expression.
    def enterExpression(self, ctx:pascalParser.ExpressionContext):
        pass

    # Exit a parse tree produced by pascalParser#expression.
    def exitExpression(self, ctx:pascalParser.ExpressionContext):
        pass


    # Enter a parse tree produced by pascalParser#operators.
    def enterOperators(self, ctx:pascalParser.OperatorsContext):
        pass

    # Exit a parse tree produced by pascalParser#operators.
    def exitOperators(self, ctx:pascalParser.OperatorsContext):
        pass


    # Enter a parse tree produced by pascalParser#ifStatement.
    def enterIfStatement(self, ctx:pascalParser.IfStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#ifStatement.
    def exitIfStatement(self, ctx:pascalParser.IfStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#elseStatement.
    def enterElseStatement(self, ctx:pascalParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#elseStatement.
    def exitElseStatement(self, ctx:pascalParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#whileStatement.
    def enterWhileStatement(self, ctx:pascalParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by pascalParser#whileStatement.
    def exitWhileStatement(self, ctx:pascalParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by pascalParser#blockBody.
    def enterBlockBody(self, ctx:pascalParser.BlockBodyContext):
        pass

    # Exit a parse tree produced by pascalParser#blockBody.
    def exitBlockBody(self, ctx:pascalParser.BlockBodyContext):
        pass


