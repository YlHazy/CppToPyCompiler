from antlr4 import *
from CppParser import CppParser
from CppLexer import CppLexer

class CppToPythonTranslator:
    def __init__(self):
        self.indent_level = 0

    def translate(self, ast):
        if ast.type == 'Program':
            return '\n'.join([self.translate(child) for child in ast.children])

        elif ast.type == 'FunctionDefinition':
            func_name = ast.children[1].value
            params = self.translate(ast.children[2])  # parameters
            body = self.translate(ast.children[3])   # body
            return f"def {func_name}({params}):\n{body}"

        elif ast.type == 'ParameterList':
            return ', '.join([param.value for param in ast.children])

        elif ast.type == 'CompoundStatement':
            return '\n'.join([self.translate(statement) for statement in ast.children])

        elif ast.type == 'ExpressionStatement':
            expr = self.translate(ast.children[0])  # expression
            return f"{expr}"

        elif ast.type == 'AssignmentExpression':
            lhs = self.translate(ast.children[0])  # left side
            rhs = self.translate(ast.children[1])  # right side
            return f"{lhs} = {rhs}"

        elif ast.type == 'Literal':
            return ast.value

        elif ast.type == 'Identifier':
            return ast.value

        # More cases as needed for control flow (if, for, while, etc.)
        return ""

    def increase_indent(self):
        self.indent_level += 1

    def decrease_indent(self):
        self.indent_level -= 1

# Helper function to parse the C++ code using ANTLR
def parse_cpp_code(input_code):
    # Create an input stream from the provided code
    input_stream = InputStream(input_code)

    # Create a lexer to process the input stream
    lexer = CppLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Create a parser to generate the abstract syntax tree (AST)
    parser = CppParser(token_stream)
    tree = parser.program()  # Start from the 'program' rule in the grammar

    # Return the parsed tree (AST)
    return tree

if __name__ == '__main__':
    # Example C++ code to convert
    cpp_code = """
    int add(int a, int b) {
        return a + b;
    }
    
    int main() {
        int result = add(3, 4);
        printf("Result: %d", result);
        return 0;
    }
    """
    
    # Parse the C++ code into an AST
    ast = parse_cpp_code(cpp_code)

    # Create an instance of the C++ to Python Translator
    translator = CppToPythonTranslator()

    # Translate the AST to Python code
    python_code = translator.translate(ast)

    # Print the generated Python code
    print(python_code)
