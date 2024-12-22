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
import re
from tkinter import simpledialog
import sys
from tkinter import scrolledtext, filedialog, messagebox, simpledialog, ttk

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

# 模拟转换函数（需要根据实际转换逻辑替换）
def convert_cpp_to_python(cpp_code):
    # 假设实现了 C++ 转换为 Python 的逻辑
    # 这里只是简单返回示例代码
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
    return  listener.output

# GUI 应用程序类
class CPPParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("C++ 词法和语法分析器")
        self.root.geometry("1400x900")  # 初始窗口大小
        self.root.configure(bg="#f0f8ff")  # 浅蓝背景

        # 创建分隔窗口
        self.create_layout()

    def create_layout(self):
        # 创建主布局
        main_pane = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        main_pane.pack(fill=tk.BOTH, expand=True)

        # 侧边栏
        self.create_sidebar(main_pane)

        # 主界面分隔
        content_pane = ttk.PanedWindow(main_pane, orient=tk.VERTICAL)
        main_pane.add(content_pane, weight=3)

        # 添加顶部输入框
        self.create_input_section(content_pane)

        # 添加中部分析结果
        analysis_pane = ttk.PanedWindow(content_pane, orient=tk.HORIZONTAL)
        content_pane.add(analysis_pane, weight=2)

        self.create_analysis_section(analysis_pane)

        # 添加底部转换和运行结果
        self.create_result_section(content_pane)

    def create_sidebar(self, parent):
        sidebar = tk.Frame(parent, bg="#2c3e50", width=250, relief=tk.GROOVE)
        parent.add(sidebar, weight=1)

        # 按钮列表
        buttons = [
            ("打开文件", self.open_file, "#2980b9"),
            ("词法分析", self.perform_lexical_analysis, "#2980b9"),
            ("语法分析", self.perform_syntax_analysis, "#2980b9"),
            ("转换为 Python", self.convert_code, "#27ae60"),
            ("运行代码", self.run_converted_code, "#27ae60"),
            ("保存结果", self.save_result, "#8e44ad"),
            ("清除", self.clear_text, "#c0392b"),
        ]

        for text, command, color in buttons:
            button = tk.Button(
                sidebar,
                text=text,
                command=command,
                bg=color,
                fg="white",
                font=("Arial", 12, "bold"),
                relief=tk.RAISED,
                width=18,
                height=2
            )
            button.pack(padx=10, pady=10, anchor="n")

    def create_input_section(self, parent):
        input_frame = tk.Frame(parent, bg="#f9f9f9", bd=2, relief=tk.GROOVE)
        parent.add(input_frame, weight=1)

        label = tk.Label(input_frame, text="输入 C++ 代码：", bg="#f9f9f9", font=("Arial", 12, "bold"))
        label.pack(anchor='nw', padx=5, pady=5)

        self.text_input = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD, height=10, font=("Consolas", 11))
        self.text_input.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def create_analysis_section(self, parent):
        # 词法分析
        lex_frame = tk.Frame(parent, bg="#f9f9f9", bd=2, relief=tk.GROOVE)
        parent.add(lex_frame, weight=1)

        lex_label = tk.Label(lex_frame, text="词法分析结果：", bg="#f9f9f9", font=("Arial", 12, "bold"))
        lex_label.pack(anchor="nw", padx=5, pady=5)

        self.lex_result_display = scrolledtext.ScrolledText(lex_frame, wrap=tk.WORD, font=("Consolas", 10))
        self.lex_result_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # 语法分析
        syntax_frame = tk.Frame(parent, bg="#f9f9f9", bd=2, relief=tk.GROOVE)
        parent.add(syntax_frame, weight=1)

        syntax_label = tk.Label(syntax_frame, text="语法分析结果：", bg="#f9f9f9", font=("Arial", 12, "bold"))
        syntax_label.pack(anchor="nw", padx=5, pady=5)

        self.syntax_result_display = scrolledtext.ScrolledText(syntax_frame, wrap=tk.WORD, font=("Consolas", 10))
        self.syntax_result_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def create_result_section(self, parent):
        result_pane = ttk.PanedWindow(parent, orient=tk.HORIZONTAL)
        parent.add(result_pane, weight=1)

        # 转换代码区域
        converted_code_frame = tk.Frame(result_pane, bg="#f9f9f9", bd=2, relief=tk.GROOVE)
        result_pane.add(converted_code_frame, weight=1)

        converted_code_label = tk.Label(converted_code_frame, text="转换后的 Python 代码：", bg="#f9f9f9", font=("Arial", 12, "bold"))
        converted_code_label.pack(anchor="nw", padx=5, pady=5)

        self.converted_code_display = scrolledtext.ScrolledText(converted_code_frame, wrap=tk.WORD, font=("Consolas", 10))
        self.converted_code_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # 运行结果区域
        execution_result_frame = tk.Frame(result_pane, bg="#f9f9f9", bd=2, relief=tk.GROOVE)
        result_pane.add(execution_result_frame, weight=1)

        execution_result_label = tk.Label(execution_result_frame, text="运行结果：", bg="#f9f9f9", font=("Arial", 12, "bold"))
        execution_result_label.pack(anchor="nw", padx=5, pady=5)

        self.execution_result_display = scrolledtext.ScrolledText(execution_result_frame, wrap=tk.WORD, font=("Consolas", 10))
        self.execution_result_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

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
            self.lex_result_display.delete(1.0, tk.END)
            self.lex_result_display.insert(tk.END, "词法分析结果（Token流）：\n")
            for token in tokens:
                self.lex_result_display.insert(tk.END, f"{token}\n")
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
            self.syntax_result_display.delete(1.0, tk.END)
            self.syntax_result_display.insert(tk.END, "语法分析结果（解析树）：\n")
            self.syntax_result_display.insert(tk.END, tree_json)
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
        self.syntax_result_display.delete(1.0, tk.END)
        self.lex_result_display.delete(1.0, tk.END)
        self.converted_code_display.delete(1.0, tk.END)
        self.execution_result_display.delete(1.0, tk.END)
        # 清除保存的结果
        if hasattr(self, 'analysis_result'):
            del self.analysis_result
        if hasattr(self, 'result_type'):
            del self.result_type

    def convert_code(self):
        cpp_code = self.text_input.get(1.0, tk.END).strip()
        if not cpp_code:
            messagebox.showwarning("提示", "请输入 C++ 代码或打开文件。")
            return

        # 转换代码
        python_code = convert_cpp_to_python(cpp_code)
        # print(python_code)
        self.converted_code_display.delete(1.0, tk.END)
        self.converted_code_display.insert(tk.END, python_code)

    def run_converted_code(self):
        python_code = self.converted_code_display.get(1.0, tk.END).strip()
        if not python_code:
            messagebox.showwarning("提示", "请先转换代码后再运行。")
            return

        try:
            import subprocess
            # 更精确地匹配赋值语句中的 `input()` 调用
            input_match = re.search(r'(\w+)\s*=\s*input\((.*?)\)', python_code)

            simulated_input = None
            if input_match:
                # 提取变量名和提示文字
                variable_name = input_match.group(1)
                prompt_text = input_match.group(2).strip("'\" ") if input_match.group(2) else " "
                simulated_input = simpledialog.askstring(
                    "模拟输入",
                    f"检测到变量 `{variable_name}` 的输入提示：{prompt_text}",
                    initialvalue="模拟值"
                )
                if simulated_input is None:
                    messagebox.showinfo("提示", "取消运行代码。")
                    return

            # 写入临时脚本
            temp_script_path = "temp_script.py"
            with open(temp_script_path, "w", encoding="utf-8") as temp_file:
                temp_file.write(python_code)

            # 运行 Python 脚本
            result = subprocess.run(
                ["python", temp_script_path],
                input=simulated_input,
                text=True,
                capture_output=True
            )

            # 显示运行结果
            self.execution_result_display.delete(1.0, tk.END)
            if result.stdout.strip():
                self.execution_result_display.insert(tk.END, "标准输出：\n" + result.stdout)
            if result.stderr.strip():
                self.execution_result_display.insert(tk.END, "错误输出：\n" + result.stderr)

        except Exception as e:
            messagebox.showerror("运行错误", f"运行代码时发生错误：\n{e}")
        finally:
            # 清理临时脚本
            if os.path.exists(temp_script_path):
                os.remove(temp_script_path)

def main():
    root = tk.Tk()
    app = CPPParserGUI(root)
    root.mainloop()
   
if __name__ == '__main__':
    main()
