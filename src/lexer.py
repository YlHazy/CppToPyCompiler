import re

# 定义 Token 类型及其正则表达式
TOKEN_SPECIFICATION = [
    ('NUMBER',   r'\d+(\.\d*)?'),     # 整数或浮点数
    ('ID',       r'[A-Za-z_]\w*'),    # 标识符
    ('OP',       r'[+\-*/=<>!]+'),    # 操作符
    ('STRING',   r'"[^"]*"'),         # 字符串
    ('LPAREN',   r'\('),              # 左括号
    ('RPAREN',   r'\)'),              # 右括号
    ('LBRACE',   r'\{'),              # 左花括号
    ('RBRACE',   r'\}'),              # 右花括号
    ('SEMI',     r';'),               # 分号
    ('COMMA',    r','),               # 逗号
    ('WHITESPACE', r'[ \t\n]+'),      # 空白字符（包含换行）
    ('MISMATCH', r'.'),               # 其他未识别字符
]

# 编译为正则表达式模式
TOKEN_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)

class Token:
    def __init__(self, type, value, position):
        self.type = type
        self.value = value
        self.position = position

    def __repr__(self):
        return f"Token({self.type}, {self.value}, {self.position})"

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []

    def tokenize(self):
        line_number = 1
        line_start = 0

        # 使用正则表达式匹配
        for match in re.finditer(TOKEN_REGEX, self.code):
            kind = match.lastgroup
            value = match.group()
            column = match.start() - line_start  # 获取列位置

            if kind == 'NUMBER':
                value = float(value) if '.' in value else int(value)  # 将数字转换为整数或浮点数
            elif kind == 'WHITESPACE':
                # 计算行数和行起始位置
                if '\n' in value:
                    line_number += value.count('\n')
                    line_start = match.end()
                continue  # 跳过空白字符
            elif kind == 'MISMATCH':
                raise SyntaxError(f'Unexpected character {value!r} at line {line_number}, column {column}')

            # 记录 Token 的类型、值和位置
            self.tokens.append(Token(kind, value, (line_number, column)))

        return self.tokens

# 测试代码
if __name__ == "__main__":
    code = 'int main() { int x = 10 + 20; }'
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    for token in tokens:
        print(token)
