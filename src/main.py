import sys
import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
# 如果需要输出 YAML 格式，取消以下注释
# import yaml
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees
from CPPLexer import CPPLexer
from CPPParser import CPPParser
from antlr4.Token import CommonToken
from CPPParserListener import CPPParserListener
# 确保当前目录在模块搜索路径中
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 自定义错误监听器，用于捕获解析错误
class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"语法错误: 行 {line}, 列 {column}: {msg}"
        self.errors.append(error_message)

    def has_errors(self):
        return len(self.errors) > 0

    def get_errors(self):
        return self.errors

# 词法分析器，提取Token流
def lexical_analysis(code):
    # 创建输入流
    input_stream = InputStream(code)

    # 词法分析器
    lexer = CPPLexer(input_stream)
    lexer.removeErrorListeners()
    lexer_error_listener = MyErrorListener()
    lexer.addErrorListener(lexer_error_listener)

    # 获取所有Token
    tokens = lexer.getAllTokens()

    # 检查是否有词法分析错误
    if lexer_error_listener.has_errors():
        error_msgs = "\n".join(lexer_error_listener.get_errors())
        return None, error_msgs

    # 重置词法分析器，以便语法分析器使用
    input_stream.reset()
    lexer.reset()

    # 构建Token列表
    token_list = []
    for token in tokens:
        token_info = {
            'type': lexer.symbolicNames[token.type],
            'text': token.text,
            'line': token.line,
            'column': token.column
        }
        token_list.append(token_info)

    return token_list, None

# 语法分析器，生成语法树
def syntax_analysis(code):
    # 创建输入流
    input_stream = InputStream(code)

    # 词法分析器
    lexer = CPPLexer(input_stream)
    lexer.removeErrorListeners()
    lexer_error_listener = MyErrorListener()
    lexer.addErrorListener(lexer_error_listener)

    # Token 流
    stream = CommonTokenStream(lexer)

    # 解析器
    parser = CPPParser(stream)
    parser.removeErrorListeners()
    parser_error_listener = MyErrorListener()
    parser.addErrorListener(parser_error_listener)

    # 开始解析
    tree = parser.program()

    # 检查是否有词法分析错误
    if lexer_error_listener.has_errors():
        error_msgs = "\n".join(lexer_error_listener.get_errors())
        return None, error_msgs

    # 检查是否有语法分析错误
    if parser_error_listener.has_errors():
        error_msgs = "\n".join(parser_error_listener.get_errors())
        return None, error_msgs

    return tree, None

# 将解析树转换为字典形式
def tree_to_dict(tree, parser):
    def create_node(node):
        if node.getChildCount() == 0:
            token = node.getSymbol()
            return {
                'type': parser.symbolicNames[token.type],
                'text': token.text,
                'line': token.line,
                'column': token.column
            }
        else:
            return {
                'rule': parser.ruleNames[node.getRuleIndex()],
                'children': [create_node(child) for child in node.children]
            }
    return create_node(tree)

# GUI 应用程序类
class CPPParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("C++ 词法和语法分析器")

        # 创建文本输入框
        self.create_text_input()

        # 创建按钮
        self.create_buttons()

        # 创建结果显示框
        self.create_result_display()

    def create_text_input(self):
        label = tk.Label(self.root, text="输入 C++ 代码：")
        label.pack(anchor='nw')

        self.text_input = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=15)
        self.text_input.pack(fill=tk.BOTH, expand=True)

    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.X)

        self.open_button = tk.Button(frame, text="打开文件", command=self.open_file)
        self.open_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.lex_button = tk.Button(frame, text="词法分析", command=self.perform_lexical_analysis)
        self.lex_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.parse_button = tk.Button(frame, text="语法分析", command=self.perform_syntax_analysis)
        self.parse_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.save_button = tk.Button(frame, text="保存结果", command=self.save_result)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.clear_button = tk.Button(frame, text="清除", command=self.clear_text)
        self.clear_button.pack(side=tk.RIGHT, padx=5, pady=5)

    def create_result_display(self):
        label = tk.Label(self.root, text="结果：")
        label.pack(anchor='nw')

        self.result_display = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=15)
        self.result_display.pack(fill=tk.BOTH, expand=True)

    def open_file(self):
        file_path = filedialog.askopenfilename(title="打开 C++ 文件", filetypes=[("C++ 文件", "*.cpp *.h *.hpp"), ("所有文件", "*.*")]
)
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
            self.text_input.delete(1.0, tk.END)
            self.text_input.insert(tk.END, code)

    def perform_lexical_analysis(self):
        code = self.text_input.get(1.0, tk.END)
        if not code.strip():
            messagebox.showwarning("提示", "请输入 C++ 代码或打开文件。")
            return
        tokens, error = lexical_analysis(code)
        if error:
            messagebox.showerror("词法分析错误", error)
        else:
            self.result_display.delete(1.0, tk.END)
            self.result_display.insert(tk.END, "词法分析结果（Token流）：\n")
            for token in tokens:
                self.result_display.insert(tk.END, f"{token}\n")
            # 保存结果，供保存功能使用
            self.analysis_result = tokens
            self.result_type = 'lexical'

    def perform_syntax_analysis(self):
        code = self.text_input.get(1.0, tk.END)
        if not code.strip():
            messagebox.showwarning("提示", "请输入 C++ 代码或打开文件。")
            return
        tree, error = syntax_analysis(code)
        if error:
            messagebox.showerror("语法分析错误", error)
        else:
            parser = CPPParser(CommonTokenStream(CPPLexer(InputStream(code))))
            tree_dict = tree_to_dict(tree, parser)
            # 输出为 JSON 格式
            tree_json = json.dumps(tree_dict, indent=2, ensure_ascii=False)
            # 如果需要输出 YAML 格式，取消以下注释
            # tree_yaml = yaml.dump(tree_dict, sort_keys=False, allow_unicode=True)
            self.result_display.delete(1.0, tk.END)
            self.result_display.insert(tk.END, "语法分析结果（解析树）：\n")
            self.result_display.insert(tk.END, tree_json)
            # 如果需要输出 YAML 格式
            # self.result_display.insert(tk.END, tree_yaml)
            # 保存结果，供保存功能使用
            self.analysis_result = tree_dict
            self.result_type = 'syntax'

    def save_result(self):
        if not hasattr(self, 'analysis_result'):
            messagebox.showwarning("提示", "没有可保存的结果，请先执行词法分析或语法分析。")
            return
        filetypes = [("JSON 文件", "*.json"), ("所有文件", "*.*")]
        file_path = filedialog.asksaveasfilename(title="保存结果", defaultextension=".json", filetypes=filetypes)
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    if self.result_type == 'lexical':
                        json.dump(self.analysis_result, f, indent=2, ensure_ascii=False)
                    elif self.result_type == 'syntax':
                        json.dump(self.analysis_result, f, indent=2, ensure_ascii=False)
                messagebox.showinfo("提示", "结果已成功保存。")
            except Exception as e:
                messagebox.showerror("错误", f"保存结果时发生错误：\n{e}")

    def clear_text(self):
        self.text_input.delete(1.0, tk.END)
        self.result_display.delete(1.0, tk.END)
        if hasattr(self, 'analysis_result'):
            del self.analysis_result
        if hasattr(self, 'result_type'):
            del self.result_type

def main():
    cpp_code = """
    #include <iostream>
    using namespace std;

    int main() {
        int x = 10;
        cout << x << endl;
        return 0;
    }
    """
    input_stream = InputStream(cpp_code)
    lexer = CPPLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CPPParser(stream)
    
    # 获取语法树
    tree = parser.program()

    # 创建并应用监听器
    listener = CPPParserListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    print(listener.python_code)
    root = tk.Tk()
    app = CPPParserGUI(root)
    root.mainloop()
   
if __name__ == '__main__':
    main()
