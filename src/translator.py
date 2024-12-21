import json

def cpp_to_python(node):
    """转化C++ AST节点为Python代码"""
    
    # 变量声明
    if node['type'] == 'declaration':
        # C++中 int x = 10;  --> Python中 x = 10
        return f"{node['name']} = {node['value']}"
    
    # 赋值操作
    elif node['type'] == 'assignment':
        # C++中 x = x + 1; --> Python中 x = x + 1
        return f"{node['name']} = {cpp_to_python(node['value'])}"
    
    # 条件语句：if
    elif node['type'] == 'if':
        # C++中 if (x > 5) { x = x + 1; } --> Python中 if x > 5: x = x + 1
        condition = cpp_to_python(node['condition'])
        body = "\n    ".join(cpp_to_python(stmt) for stmt in node['body'])
        return f"if {condition}:\n    {body}"
    
    # 二元表达式：例如 x > 5, x + 1 等
    elif node['type'] == 'binary_expression':
        left = cpp_to_python(node['left'])
        operator = node['operator']
        right = cpp_to_python(node['right'])
        return f"({left} {operator} {right})"
    
    # 字面量（常量）处理：例如数字或字符串
    elif node['type'] == 'literal':
        return node['value']
    
    # 标识符：例如变量名（x）
    elif node['type'] == 'identifier':
        return node['name']
    
    # 如果节点类型不匹配，返回空字符串
    return ""

def traverse_ast(ast):
    """遍历C++语法树，将其转化为Python代码"""
    python_code = []
    for node in ast:
        python_code.append(cpp_to_python(node))
    return "\n".join(python_code)

# 假设我们从文件中加载C++编译器生成的AST（JSON格式）
with open('cpp_ast.json', 'r') as file:
    cpp_ast = json.load(file)

# 转化为Python代码
python_code = traverse_ast(cpp_ast)

# 输出转化后的Python代码
print(python_code)
