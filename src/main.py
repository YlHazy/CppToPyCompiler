import sys
import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from CPPLexer import CPPLexer
from CPPParser import CPPParser
from antlr4.Token import CommonToken
from CPPParserListener import CPPParserListener
import time
import subprocess
import tkinter.font as tkFont
from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD

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

# 更新后的转换函数，返回转换后的代码和符号表
def convert_cpp_to_python(cpp_code):
    # 假设实现了 C++ 转换为 Python 的逻辑
    # 这里只是简单返回示例代码和符号表
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
    
    # 返回转换后的代码和符号表
    return listener.output, listener.symbol_table

# GUI 应用程序类
class CPPParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("C++ 词法和语法分析器")
        self.root.geometry("1600x900")  # 调整窗口大小以适应新增的表格
        self.root.configure(bg="#f0f4f7")  # 更柔和的背景色

        # 当前打开的文件路径
        self.current_cpp_file = None
        self.current_py_file = None

        # 自定义样式
        self.style = ttk.Style()
        self.style.theme_use('clam')  # 使用clam主题，更加现代
        self.style.configure("TButton",
                             font=("Helvetica", 12, "bold"),
                             foreground="#ffffff",
                             background="#3498db",
                             padding=10)
        self.style.map("TButton",
                       background=[('active', '#2980b9')])

        self.style.configure("TLabelFrame.Label",
                             font=("Helvetica", 12, "bold"),
                             foreground="#2c3e50")

        self.style.configure("TNotebook.Tab",
                             font=("Helvetica", 12, "bold"),
                             padding=[10, 5],
                             foreground="#2c3e50")

        # 新增样式用于符号表，基于Treeview样式
        self.style.configure("SymbolTreeview.Treeview",
                             background="#ecf0f1",
                             foreground="#2c3e50",
                             font=("Consolas", 12),
                             rowheight=25,
                             borderwidth=1,
                             relief="solid")
        self.style.configure("SymbolTreeview.Treeview.Heading",
                             background="#34495e",
                             foreground="#ffffff",
                             font=("Helvetica", 12, "bold"),
                             borderwidth=1,
                             relief="solid")
        self.style.map("SymbolTreeview.Treeview",
                       background=[('selected', '#3498db')])

        # 定义交替行颜色的标签
        # 在 Treeview 的每行添加标签 'oddrow' 或 'evenrow'
        self.style.configure("OddRow.Treeview", background="#ecf0f1")
        self.style.configure("EvenRow.Treeview", background="#bdc3c7")

        # 调整菜单栏字体
        self.menu_font = tkFont.Font(family="Helvetica", size=12, weight="bold")

        # 创建菜单栏
        self.create_menu()

        # 创建按钮框架
        self.create_button_frame()

        # 创建分隔窗口（选项卡）
        self.create_layout()

        # 创建状态栏
        self.create_status_bar()

        # 添加拖放支持
        self.add_drag_and_drop()

        # 初始化符号表数据
        self.symbol_table = []

    def create_menu(self):
        menubar = tk.Menu(self.root, font=self.menu_font)
        self.root.config(menu=menubar)

        # 文件菜单
        file_menu = tk.Menu(menubar, tearoff=0, font=self.menu_font)
        menubar.add_cascade(label="文件", menu=file_menu)
        file_menu.add_command(label="打开文件\tCtrl+O", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.root.quit)

        # 保存菜单
        save_menu = tk.Menu(menubar, tearoff=0, font=self.menu_font)
        menubar.add_cascade(label="保存", menu=save_menu)
        save_menu.add_command(label="保存词法分析结果", command=self.save_lex_result, accelerator="")
        save_menu.add_command(label="保存语法分析结果", command=self.save_syntax_result, accelerator="")
        save_menu.add_command(label="保存符号表", command=self.save_symbol_table, accelerator="")  # 新增保存符号表

        # 帮助菜单
        help_menu = tk.Menu(menubar, tearoff=0, font=self.menu_font)
        menubar.add_cascade(label="帮助", menu=help_menu)
        help_menu.add_command(label="关于", command=self.show_about)

        # 绑定菜单快捷键
        self.root.bind_all("<Control-o>", self.open_file_event)
        self.root.bind_all("<Control-Shift-s>", self.save_lex_result_event)
        self.root.bind_all("<Control-Alt-s>", self.save_syntax_result_event)
        self.root.bind_all("<Control-Shift-t>", self.save_symbol_table_event)  # 绑定保存符号表快捷键

    def create_button_frame(self):
        # 按钮框架放置在菜单栏下方
        button_frame = ttk.Frame(self.root, padding=10)
        button_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

        # 按钮列表
        buttons = [
            ("打开文件", self.open_file, "#3498db"),
            ("词法分析", self.perform_lexical_analysis, "#2ecc71"),
            ("语法分析", self.perform_syntax_analysis, "#f1c40f"),
            ("转换为 Python", self.convert_code, "#e67e22"),
            ("运行代码", self.run_converted_code, "#e74c3c"),
            ("清除", self.clear_all_text, "#34495e"),
        ]

        for text, command, color in buttons:
            button = ttk.Button(
                button_frame,
                text=text,
                command=command,
                style="TButton"
            )
            # 修改按钮颜色
            button_style = f"{text}.TButton"
            self.style.configure(button_style,
                                 background=color)
            button.configure(style=button_style)
            button.pack(side=tk.LEFT, padx=10)

    def create_layout(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 选项卡1：代码与运行
        self.tab_code_run = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_code_run, text="代码与运行")
        self.create_code_run_section(self.tab_code_run)

        # 选项卡2：分析结果
        self.tab_analysis = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_analysis, text="分析结果")
        self.create_analysis_section(self.tab_analysis)

        # 新增选项卡3：符号表
        self.tab_symbol_table = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_symbol_table, text="符号表")
        self.create_symbol_table_section(self.tab_symbol_table)

    def create_code_run_section(self, parent):
        # 主框架
        main_frame = tk.Frame(parent, bg="#f0f4f7")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 左侧：C++ 代码
        cpp_frame = ttk.LabelFrame(main_frame, text="C++ 代码")
        cpp_frame.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=10, pady=10)

        self.text_input = scrolledtext.ScrolledText(cpp_frame, wrap=tk.WORD, font=("Consolas", 12), bg="#ffffff", fg="#2c3e50")
        self.text_input.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        # 绑定 Ctrl+S
        self.text_input.bind("<Control-s>", self.save_cpp_code_event)
        # 绑定焦点事件
        self.text_input.bind("<FocusIn>", lambda event: self.update_status_bar("按 Ctrl + S 保存 C++ 代码"))
        self.text_input.bind("<FocusOut>", lambda event: self.update_status_bar("准备就绪"))

        # 右上角：转换后的 Python 代码
        python_frame = ttk.LabelFrame(main_frame, text="转换后的 Python 代码")
        python_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.converted_code_display = scrolledtext.ScrolledText(python_frame, wrap=tk.WORD, font=("Consolas", 12), bg="#ffffff", fg="#2c3e50")
        self.converted_code_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        # 绑定 Ctrl+S
        self.converted_code_display.bind("<Control-s>", self.save_python_code_event)
        # 绑定焦点事件
        self.converted_code_display.bind("<FocusIn>", lambda event: self.update_status_bar("按 Ctrl + S 保存 Python 代码"))
        self.converted_code_display.bind("<FocusOut>", lambda event: self.update_status_bar("准备就绪"))

        # 右下角：输入参数和运行结果
        run_frame = tk.Frame(main_frame, bg="#f0f4f7")
        run_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        # 参数输入
        param_frame = ttk.LabelFrame(run_frame, text="输入参数（空格分隔）")
        param_frame.pack(fill=tk.X, expand=False, padx=5, pady=5)

        self.param_values = tk.Entry(param_frame, font=("Consolas", 12), bg="#ffffff", fg="#2c3e50")
        self.param_values.pack(fill=tk.X, padx=5, pady=5, ipady=5)

        # 运行结果
        execution_result_frame = ttk.LabelFrame(run_frame, text="运行结果")
        execution_result_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.execution_result_display = scrolledtext.ScrolledText(
            execution_result_frame, 
            wrap=tk.WORD, 
            font=("Consolas", 12), 
            height=8,
            bg="#ffffff",
            fg="#2c3e50"
        )
        self.execution_result_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        # 绑定 Ctrl+S
        self.execution_result_display.bind("<Control-s>", self.save_execution_result_event)
        # 绑定焦点事件
        self.execution_result_display.bind("<FocusIn>", lambda event: self.update_status_bar("按 Ctrl + S 保存运行结果"))
        self.execution_result_display.bind("<FocusOut>", lambda event: self.update_status_bar("准备就绪"))

        # 配置网格权重
        main_frame.grid_rowconfigure(0, weight=3)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=2)
        main_frame.grid_columnconfigure(1, weight=3)

    def create_analysis_section(self, parent):
        # 分析结果框架
        analysis_frame = tk.Frame(parent, bg="#f0f4f7")
        analysis_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 左侧：词法分析结果
        lex_frame = ttk.LabelFrame(analysis_frame, text="词法分析结果")
        lex_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.lex_result_display = scrolledtext.ScrolledText(lex_frame, wrap=tk.WORD, font=("Consolas", 12), bg="#ffffff", fg="#2c3e50")
        self.lex_result_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        # 绑定 Ctrl+S
        self.lex_result_display.bind("<Control-s>", self.save_lex_result_event)
        # 绑定焦点事件
        self.lex_result_display.bind("<FocusIn>", lambda event: self.update_status_bar("按 Ctrl + S 保存词法分析结果"))
        self.lex_result_display.bind("<FocusOut>", lambda event: self.update_status_bar("准备就绪"))

        # 右侧：语法分析结果
        syntax_frame = ttk.LabelFrame(analysis_frame, text="语法分析结果")
        syntax_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.syntax_result_display = scrolledtext.ScrolledText(syntax_frame, wrap=tk.WORD, font=("Consolas", 12), bg="#ffffff", fg="#2c3e50")
        self.syntax_result_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        # 绑定 Ctrl+S
        self.syntax_result_display.bind("<Control-s>", self.save_syntax_result_event)
        # 绑定焦点事件
        self.syntax_result_display.bind("<FocusIn>", lambda event: self.update_status_bar("按 Ctrl + S 保存语法分析结果"))
        self.syntax_result_display.bind("<FocusOut>", lambda event: self.update_status_bar("准备就绪"))

    def create_symbol_table_section(self, parent):
        # 符号表框架
        symbol_frame = ttk.Frame(parent, padding=10)
        symbol_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 搜索栏
        search_frame = ttk.Frame(symbol_frame)
        search_frame.pack(fill=tk.X, padx=5, pady=5)

        search_label = ttk.Label(search_frame, text="搜索符号:")
        search_label.pack(side=tk.LEFT, padx=(0, 5))

        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var, font=("Consolas", 12))
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.search_entry.bind("<KeyRelease>", self.search_symbol)

        clear_search_button = ttk.Button(search_frame, text="清除", command=self.clear_search)
        clear_search_button.pack(side=tk.LEFT)

        # 定义Treeview，应用正确的样式名称
        self.symbol_table_tree = ttk.Treeview(symbol_frame, columns=("Name", "Type", "Value", "Scope"), show="headings", style="SymbolTreeview.Treeview")
        self.symbol_table_tree.heading("Name", text="名称")
        self.symbol_table_tree.heading("Type", text="类型")
        self.symbol_table_tree.heading("Value", text="值")
        self.symbol_table_tree.heading("Scope", text="作用域")

        # 设置列宽和对齐方式
        self.symbol_table_tree.column("Name", width=200, anchor='center', stretch=True)
        self.symbol_table_tree.column("Type", width=150, anchor='center', stretch=True)
        self.symbol_table_tree.column("Value", width=200, anchor='center', stretch=True)
        self.symbol_table_tree.column("Scope", width=150, anchor='center', stretch=True)

        # 添加交替行颜色的标签
        self.symbol_table_tree.tag_configure('oddrow', background="#ecf0f1")
        self.symbol_table_tree.tag_configure('evenrow', background="#bdc3c7")

        # 配置网格线（模拟）
        self.style.configure("SymbolTreeview.Treeview", fieldbackground="#ecf0f1")
        self.style.layout("SymbolTreeview.Treeview",
                          [('Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        # 添加垂直滚动条
        symbol_scrollbar = ttk.Scrollbar(symbol_frame, orient="vertical", command=self.symbol_table_tree.yview)
        self.symbol_table_tree.configure(yscroll=symbol_scrollbar.set)
        symbol_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.symbol_table_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def create_status_bar(self):
        self.status_var = tk.StringVar()
        self.status_var.set("准备就绪")
        status_bar = ttk.Label(
            self.root, 
            textvariable=self.status_var, 
            relief=tk.SUNKEN, 
            anchor=tk.W, 
            font=("Helvetica", 10)
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def update_status_bar(self, message):
        self.status_var.set(message)

    # 功能实现部分与原代码保持一致

    def open_file_event(self, event):
        self.open_file()

    def open_file(self):
        # 清空现有内容
        self.clear_all_text()

        file_path = filedialog.askopenfilename(
            title="打开 C++ 文件", 
            filetypes=[("C++ 文件", "*.cpp *.h *.hpp"), ("所有文件", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    code = f.read()
                self.text_input.insert(tk.END, code)
                self.status_var.set(f"已打开文件: {os.path.basename(file_path)}")
                # 设置当前 C++ 文件路径
                self.current_cpp_file = file_path
            except Exception as e:
                messagebox.showerror("错误", f"无法打开文件：\n{e}")
                self.status_var.set("打开文件失败")

    def perform_lexical_analysis(self):
        code = self.text_input.get(1.0, tk.END)
        if not code.strip():
            messagebox.showwarning("提示", "请输入 C++ 代码或打开文件。")
            self.status_var.set("词法分析失败：无输入代码")
            return
        tokens, error = lexical_analysis(code)
        if error:
            messagebox.showerror("词法分析错误", error)
            self.status_var.set("词法分析失败")
        else:
            self.lex_result_display.delete(1.0, tk.END)
            self.lex_result_display.insert(tk.END, "词法分析结果（Token流）：\n")
            for token in tokens:
                self.lex_result_display.insert(tk.END, f"{token}\n")
            # 保存词法结果，供保存功能使用
            self.lex_result = tokens
            self.status_var.set("词法分析成功")
            # 跳转到“分析结果”选项卡并聚焦词法分析结果
            self.notebook.select(self.tab_analysis)
            self.lex_result_display.focus_set()

    def perform_syntax_analysis(self):
        code = self.text_input.get(1.0, tk.END)
        if not code.strip():
            messagebox.showwarning("提示", "请输入 C++ 代码或打开文件。")
            self.status_var.set("语法分析失败：无输入代码")
            return
        tree, error = syntax_analysis(code)
        if error:
            messagebox.showerror("语法分析错误", error)
            self.status_var.set("语法分析失败")
        else:
            parser = CPPParser(CommonTokenStream(CPPLexer(InputStream(code))))
            tree_dict = tree_to_dict(tree, parser)
            # 输出为 JSON 格式
            tree_json = json.dumps(tree_dict, indent=2, ensure_ascii=False)
            self.syntax_result_display.delete(1.0, tk.END)
            self.syntax_result_display.insert(tk.END, "语法分析结果（解析树）：\n")
            self.syntax_result_display.insert(tk.END, tree_json)
            # 保存语法结果，供保存功能使用
            self.syntax_result = tree_dict
            self.status_var.set("语法分析成功")
            # 跳转到“分析结果”选项卡并聚焦语法分析结果
            self.notebook.select(self.tab_analysis)
            self.syntax_result_display.focus_set()

    def save_lex_result(self):
        if not hasattr(self, 'lex_result'):
            messagebox.showwarning("提示", "没有可保存的词法分析结果，请先执行词法分析。")
            self.status_var.set("保存词法分析结果失败：无数据")
            return
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        default_filename = f"lexical_analysis_{timestamp}.json"
        file_path = filedialog.asksaveasfilename(
            title="保存词法分析结果",
            defaultextension=".json",
            initialfile=default_filename,
            filetypes=[("JSON 文件", "*.json"), ("所有文件", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(self.lex_result, f, indent=2, ensure_ascii=False)
                messagebox.showinfo("提示", "词法分析结果已成功保存。")
                self.status_var.set(f"词法分析结果已保存: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("错误", f"保存词法分析结果时发生错误：\n{e}")
                self.status_var.set("保存词法分析结果失败")

    def save_syntax_result(self):
        if not hasattr(self, 'syntax_result'):
            messagebox.showwarning("提示", "没有可保存的语法分析结果，请先执行语法分析。")
            self.status_var.set("保存语法分析结果失败：无数据")
            return
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        default_filename = f"syntax_analysis_{timestamp}.json"
        file_path = filedialog.asksaveasfilename(
            title="保存语法分析结果",
            defaultextension=".json",
            initialfile=default_filename,
            filetypes=[("JSON 文件", "*.json"), ("所有文件", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(self.syntax_result, f, indent=2, ensure_ascii=False)
                messagebox.showinfo("提示", "语法分析结果已成功保存。")
                self.status_var.set(f"语法分析结果已保存: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("错误", f"保存语法分析结果时发生错误：\n{e}")
                self.status_var.set("保存语法分析结果失败")

    def save_symbol_table(self):
        if not self.symbol_table:
            messagebox.showwarning("提示", "没有可保存的符号表，请先执行代码转换。")
            self.status_var.set("保存符号表失败：无数据")
            return
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        default_filename = f"symbol_table_{timestamp}.json"
        file_path = filedialog.asksaveasfilename(
            title="保存符号表",
            defaultextension=".json",
            initialfile=default_filename,
            filetypes=[("JSON 文件", "*.json"), ("所有文件", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(self.symbol_table, f, indent=2, ensure_ascii=False)
                messagebox.showinfo("提示", "符号表已成功保存。")
                self.status_var.set(f"符号表已保存: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("错误", f"保存符号表时发生错误：\n{e}")
                self.status_var.set("保存符号表失败")

    def save_symbol_table_event(self, event):
        self.save_symbol_table()

    def show_about(self):
        about_message = (
            "C++ 词法和语法分析器\n"
            "版本 1.0\n\n"
            "使用 Python 和 Tkinter 开发。\n"
            "支持词法分析、语法分析、代码转换和运行。\n\n"
            "开发者: cwx zmy mjh yyh"
        )
        messagebox.showinfo("关于", about_message)

    def clear_all_text(self):
        self.text_input.delete(1.0, tk.END)
        self.syntax_result_display.delete(1.0, tk.END)
        self.lex_result_display.delete(1.0, tk.END)
        self.converted_code_display.delete(1.0, tk.END)
        self.execution_result_display.delete(1.0, tk.END)
        self.param_values.delete(0, tk.END)
        # 清除保存的结果
        if hasattr(self, 'lex_result'):
            del self.lex_result
        if hasattr(self, 'syntax_result'):
            del self.syntax_result
        if self.symbol_table:
            self.symbol_table = []
            self.symbol_table_tree.delete(*self.symbol_table_tree.get_children())
        # 将属性设置为 None，而不是删除它们
        self.current_cpp_file = None
        self.current_py_file = None
        self.status_var.set("已清除所有内容")

    def convert_code(self):
        cpp_code = self.text_input.get(1.0, tk.END).strip()
        if not cpp_code:
            messagebox.showwarning("提示", "请输入 C++ 代码或打开文件。")
            self.status_var.set("转换失败：无输入代码")
            return

        # 转换代码
        python_code, symbol_table = convert_cpp_to_python(cpp_code)
        self.converted_code_display.delete(1.0, tk.END)
        self.converted_code_display.insert(tk.END, python_code)
        self.status_var.set("代码转换成功")
        # 保存符号表
        self.symbol_table = symbol_table
        self.display_symbol_table()
        # 跳转到“代码与运行”选项卡并聚焦转换后的 Python 代码
        self.notebook.select(self.tab_code_run)
        self.converted_code_display.focus_set()

    def display_symbol_table(self):
        # 清空现有符号表
        self.symbol_table_tree.delete(*self.symbol_table_tree.get_children())

        # 插入新的符号表数据，并应用交替行颜色
        for index, entry in enumerate(self.symbol_table):
            # 确保每项有四个元素
            if len(entry) == 4:
                tag = 'evenrow' if index % 2 == 0 else 'oddrow'
                self.symbol_table_tree.insert("", "end", values=entry, tags=(tag,))

    def run_converted_code(self):
        python_code = self.converted_code_display.get(1.0, tk.END).strip()
        if not python_code:
            messagebox.showwarning("提示", "请输入代码后再运行。")
            self.status_var.set("运行失败：无转换代码")
            return

        params = self.param_values.get().strip()
        if not params:
            messagebox.showwarning("提示", "请输入参数值后再运行。")
            self.status_var.set("运行失败：无输入参数")
            return

        inputs = params.split()

        # 将输入值拼接为换行分隔字符串
        simulated_input_str = "\n".join(inputs) + "\n"

        temp_script_path = "temp_script.py"
        try:
            with open(temp_script_path, "w", encoding="utf-8") as temp_file:
                temp_file.write(python_code)

            # 运行代码
            result = subprocess.run(
                ["python", temp_script_path],
                input=simulated_input_str,
                text=True,
                capture_output=True,
            )

            self.execution_result_display.delete(1.0, tk.END)
            if result.stdout.strip():
                self.execution_result_display.insert(tk.END, result.stdout)
            if result.stderr.strip():
                self.execution_result_display.insert(tk.END, "错误输出：\n" + result.stderr)

            if result.returncode == 0:
                self.status_var.set("代码运行成功")
            else:
                self.status_var.set("代码运行完成，但存在错误")

            # 跳转到“代码与运行”选项卡并聚焦运行结果
            self.notebook.select(self.tab_code_run)
            self.execution_result_display.focus_set()
        except Exception as e:
            messagebox.showerror("运行错误", f"运行代码时发生错误：\n{e}")
            self.status_var.set("运行失败")

    # 保存 C++ 代码事件
    def save_cpp_code_event(self, event):
        self.save_cpp_code()

    def save_cpp_code(self):
        if self.current_cpp_file:
            try:
                code = self.text_input.get(1.0, tk.END)
                with open(self.current_cpp_file, 'w', encoding='utf-8') as f:
                    f.write(code)
                messagebox.showinfo("提示", f"C++ 代码已保存到: {self.current_cpp_file}")
                self.status_var.set(f"C++ 代码已保存: {os.path.basename(self.current_cpp_file)}")
            except Exception as e:
                messagebox.showerror("错误", f"保存 C++ 代码时发生错误：\n{e}")
                self.status_var.set("保存 C++ 代码失败")
        else:
            # 如果没有打开的文件，弹出“另存为”对话框
            self.save_cpp_code_as()

    def save_cpp_code_as(self):
        file_path = filedialog.asksaveasfilename(
            title="保存 C++ 代码",
            defaultextension=".cpp",
            filetypes=[("C++ 文件", "*.cpp *.h *.hpp"), ("所有文件", "*.*")]
        )
        if file_path:
            try:
                code = self.text_input.get(1.0, tk.END)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(code)
                self.current_cpp_file = file_path
                messagebox.showinfo("提示", f"C++ 代码已保存到: {file_path}")
                self.status_var.set(f"C++ 代码已保存: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("错误", f"保存 C++ 代码时发生错误：\n{e}")
                self.status_var.set("保存 C++ 代码失败")

    # 保存 Python 代码事件
    def save_python_code_event(self, event):
        self.save_python_code()

    def save_python_code(self):
        if self.current_py_file:
            try:
                code = self.converted_code_display.get(1.0, tk.END)
                with open(self.current_py_file, 'w', encoding='utf-8') as f:
                    f.write(code)
                messagebox.showinfo("提示", f"Python 代码已保存到: {self.current_py_file}")
                self.status_var.set(f"Python 代码已保存: {os.path.basename(self.current_py_file)}")
            except Exception as e:
                messagebox.showerror("错误", f"保存 Python 代码时发生错误：\n{e}")
                self.status_var.set("保存 Python 代码失败")
        else:
            # 弹出“另存为”对话框
            self.save_python_code_as()

    def save_python_code_as(self):
        file_path = filedialog.asksaveasfilename(
            title="保存 Python 代码",
            defaultextension=".py",
            filetypes=[("Python 文件", "*.py"), ("所有文件", "*.*")]
        )
        if file_path:
            try:
                code = self.converted_code_display.get(1.0, tk.END)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(code)
                self.current_py_file = file_path
                messagebox.showinfo("提示", f"Python 代码已保存到: {file_path}")
                self.status_var.set(f"Python 代码已保存: {os.path.basename(self.current_py_file)}")
            except Exception as e:
                messagebox.showerror("错误", f"保存 Python 代码时发生错误：\n{e}")
                self.status_var.set("保存 Python 代码失败")

    # 保存运行结果事件
    def save_execution_result_event(self, event):
        self.save_execution_result()

    def save_execution_result(self):
        file_path = filedialog.asksaveasfilename(
            title="保存运行结果",
            defaultextension=".txt",
            filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
        )
        if file_path:
            try:
                result = self.execution_result_display.get(1.0, tk.END)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(result)
                messagebox.showinfo("提示", f"运行结果已保存到: {file_path}")
                self.status_var.set(f"运行结果已保存: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("错误", f"保存运行结果时发生错误：\n{e}")
                self.status_var.set("保存运行结果失败")

    # 保存词法分析结果事件
    def save_lex_result_event(self, event):
        self.save_lex_result()

    # 保存语法分析结果事件
    def save_syntax_result_event(self, event):
        self.save_syntax_result()

    # 保存符号表事件
    def save_symbol_table_event(self, event):
        self.save_symbol_table()

    def add_drag_and_drop(self):
        # 允许整个应用窗口接受文件拖放
        self.root.drop_target_register(DND_FILES)
        self.root.dnd_bind('<<Drop>>', self.handle_drop)

    def handle_drop(self, event):
        # 清空现有内容
        self.clear_all_text()

        # 获取拖放的文件路径
        files = self.root.tk.splitlist(event.data)
        if files:
            file_path = files[0]
            if os.path.isfile(file_path):
                # 检查文件扩展名是否为 C++ 文件
                if file_path.endswith(('.cpp', '.h', '.hpp')):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            code = f.read()
                        self.text_input.insert(tk.END, code)
                        self.status_var.set(f"已打开文件: {os.path.basename(file_path)} (通过拖放)")
                        # 设置当前 C++ 文件路径
                        self.current_cpp_file = file_path
                        # 可选：自动进行词法和语法分析
                        # self.perform_lexical_analysis()
                        # self.perform_syntax_analysis()
                    except Exception as e:
                        messagebox.showerror("错误", f"无法打开文件：\n{e}")
                        self.status_var.set("拖放文件失败")
                else:
                    messagebox.showwarning("警告", "仅支持拖放 C++ 文件（.cpp, .h, .hpp）。")
                    self.status_var.set("拖放文件失败：不支持的文件类型")
            else:
                messagebox.showwarning("警告", "拖放的内容不是文件。")
                self.status_var.set("拖放文件失败：无效的文件")
        else:
            self.status_var.set("拖放操作未检测到文件")

    def search_symbol(self, event):
        search_term = self.search_var.get().lower()
        # 清空现有显示
        self.symbol_table_tree.delete(*self.symbol_table_tree.get_children())
        # 插入符合搜索条件的条目
        for index, entry in enumerate(self.symbol_table):
            symbol_name = entry[0]  # 假设符号名称在每个条目的第一个位置（即entry[0]）
            
            # 只针对符号名称进行模糊匹配（向右模糊匹配）
            if symbol_name.lower().startswith(search_term.lower()):
                tag = 'evenrow' if index % 2 == 0 else 'oddrow'
                self.symbol_table_tree.insert("", "end", values=entry, tags=(tag,))

    def clear_search(self):
        self.search_var.set("")
        self.display_symbol_table()

# 主函数
def main():
    # 使用 TkinterDnD.Tk() 代替 tk.Tk()
    root = TkinterDnD.Tk()
    app = CPPParserGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
