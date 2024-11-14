import re

# 定义 Token 类型及其正则表达式
TOKEN_SPECIFICATION = [
    ('KEYWORD', r'\b(if|else|for|while|return|int|float|double|char|bool|void)\b'),  # 关键字
    ('IDENTIFIER', r'[A-Za-z_]\w*'),               # 标识符
    ('HEX_LITERAL', r'0[xX][0-9a-fA-F]+'),         # 十六进制常量
    ('OCT_LITERAL', r'0[oO]?[0-7]+'),              # 八进制常量
    ('BIN_LITERAL', r'0[bB][01]+'),                # 二进制常量
    ('FLOAT_LITERAL', r'\d+\.\d+([eE][+-]?\d+)?'), # 浮点数常量
    ('INT_LITERAL', r'\d+'),                       # 整数常量
    ('STRING_LITERAL', r'"(\\.|[^"\\])*"'),        # 字符串常量，支持转义字符
    ('CHAR_LITERAL', r"'(\\.|[^'\\])'"),           # 字符常量，支持转义字符
    ('OPERATOR', r'(\+\+|--|\+=|-=|\*=|/=|==|!=|<=|>=|&&|\|\||[+\-*/=<>&|!])'),  # 运算符
    ('COMMENT', r'//.*|/\*[\s\S]*?\*/'),           # 单行和多行注释
    ('DELIMITER', r'[;,\(\)\{\}\[\]]'),            # 分隔符，包括方括号
    ('SKIP', r'[ \t]+'),                           # 空白字符
    ('NEWLINE', r'\n'),                            # 换行符
    ('MISMATCH', r'.'),                            # 不匹配字符
]

# 编译正则表达式模式
TOKEN_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)

class Token:
    def __init__(self, type, value, position, end_position=None):
        self.type = type
        self.value = value
        self.position = position
        self.end_position = end_position

    def __repr__(self):
        return f"Token(type={self.type}, value={self.value}, position={self.position}, end_position={self.end_position})"

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.errors = []

    def tokenize(self):
        line_number = 1
        line_start = 0

        for match in re.finditer(TOKEN_REGEX, self.code):
            kind = match.lastgroup
            value = match.group()
            column = match.start() - line_start
            end_column = match.end() - line_start

            if kind == 'KEYWORD':
                pass  # 保留为关键词
            elif kind == 'IDENTIFIER':
                pass  # 标识符
            elif kind == 'HEX_LITERAL':
                value = int(value, 16)  # 转换为十六进制整数
            elif kind == 'OCT_LITERAL':
                value = int(value, 8)   # 转换为八进制整数
            elif kind == 'BIN_LITERAL':
                value = int(value, 2)   # 转换为二进制整数
            elif kind == 'FLOAT_LITERAL':
                value = float(value)    # 转换为浮点数
            elif kind == 'INT_LITERAL':
                value = int(value)      # 转换为十进制整数
            elif kind == 'STRING_LITERAL' or kind == 'CHAR_LITERAL':
                if (kind == 'STRING_LITERAL' and not value.endswith('"')) or \
                   (kind == 'CHAR_LITERAL' and not value.endswith("'")):
                    self.errors.append(f"Unclosed string or char at line {line_number}, column {column}")
                    continue
                value = value[1:-1]  # 去除引号
            elif kind == 'COMMENT':
                continue  # 注释直接跳过
            elif kind == 'DELIMITER':
                pass  # 分隔符
            elif kind == 'SKIP':
                if '\n' in value:
                    line_number += value.count('\n')
                    line_start = match.end()
                continue
            elif kind == 'NEWLINE':
                line_number += 1
                line_start = match.end()
                continue
            elif kind == 'MISMATCH':
                self.errors.append(f"Unexpected character {value!r} at line {line_number}, column {column}")
                continue  # 跳过不匹配字符

            # 添加 Token
            self.tokens.append(Token(kind, value, (line_number, column), (line_number, end_column)))

        # 添加 EOF Token
        self.tokens.append(Token('EOF', None, (line_number, column)))

        # 检查 EOF 的有效性
        if not self.errors and len(self.tokens) > 0:
            last_token = self.tokens[-1]
            if last_token.type not in {'DELIMITER', 'OPERATOR', 'EOF'}:
                self.errors.append("Unexpected end of file without proper closing")

        return self.tokens, self.errors

# 测试代码
if __name__ == "__main__":
    code = '''
    int main() {
        float pi = 3.14159;
        char ch = '\\n';
        string s = "Hello, world!";
        int hex = 0xFF;
        int bin = 0b1010;
        int oct = 0o755;
    }
    '''
    lexer = Lexer(code)
    tokens, errors = lexer.tokenize()
    for token in tokens:
        print(token)
    if errors:
        print("Errors encountered:")
        for error in errors:
            print(error)
