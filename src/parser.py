from lexer import Token  # 导入 Token 类

class ASTNode:
    def __init__(self, type, value=None, children=None):
        self.type = type
        self.value = value
        self.children = children or []

    def __repr__(self, level=0):
        indent = '  ' * level
        result = f"{indent}{self.type}({self.value})\n"
        for child in self.children:
            result += child.__repr__(level + 1)
        return result

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        return self.parse_program()

    def parse_program(self):
        statements = []
        while self.pos < len(self.tokens):
            statements.append(self.parse_statement())
        return ASTNode('Program', children=statements)

    def parse_statement(self):
        current_token = self.tokens[self.pos]
        if current_token.type == 'ID' and current_token.value == 'int':  # 支持 int 类型变量声明
            return self.parse_variable_declaration()
        else:
            raise SyntaxError(f'Invalid statement at position {self.pos}')

    def parse_variable_declaration(self):
        self.expect('ID', 'int')  # 期望 'int' 关键字
        var_name = self.expect('ID').value  # 获取变量名
        self.expect('OP', '=')  # 期望 '=' 符号
        expr = self.parse_expression()  # 解析表达式
        self.expect('SEMI')  # 期望 ';' 结束符号
        return ASTNode('VariableDeclaration', var_name, [expr])

    def parse_expression(self):
        # 支持二元操作符 '+' 和 '-'，更复杂的可以进一步扩展
        left = self.parse_term()
        while self.peek('OP', '+') or self.peek('OP', '-'):
            op = self.tokens[self.pos]
            self.pos += 1
            right = self.parse_term()
            left = ASTNode('BinaryOperation', op.value, [left, right])
        return left

    def parse_term(self):
        token = self.tokens[self.pos]
        if token.type == 'NUMBER':
            self.pos += 1
            return ASTNode('Number', token.value)
        elif token.type == 'ID':
            self.pos += 1
            return ASTNode('Identifier', token.value)
        else:
            raise SyntaxError(f'Unexpected token: {token}')

    def expect(self, type, value=None):
        token = self.tokens[self.pos]
        if token.type != type or (value is not None and token.value != value):
            raise SyntaxError(f"Expected {type} {value or ''} at position {self.pos}, found {token}")
        self.pos += 1
        return token

    def peek(self, type, value=None):
        if self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            return token.type == type and (value is None or token.value == value)
        return False

# 测试代码
if __name__ == "__main__":
    tokens = [
        Token('ID', 'int', (1, 0)), Token('ID', 'x', (1, 4)), Token('OP', '=', (1, 6)), 
        Token('NUMBER', 10, (1, 8)), Token('OP', '+', (1, 11)), Token('NUMBER', 20, (1, 13)), 
        Token('SEMI', ';', (1, 15))
    ]
    parser = Parser(tokens)
    ast = parser.parse()
    print(ast)
