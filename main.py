import tkinter as tk
from tkinter import filedialog as fdg
from tkinter import messagebox as msg
from tkinter import ttk

import os

width, height = 960, 540  # 窗口的长和宽
now_file = ""  # 当前文件
total_line = 1  # 文本行数


class Win(tk.Tk):  # 主窗口
    def __init__(self):
        super().__init__()

        # 设置标题
        self.title("Markdown Notepad v1.0")

        # 设置窗口大小
        self.screenwidth, self.screenheight = self.winfo_screenwidth(), self.winfo_screenheight()
        self.size = "%dx%d+%d+%d" % (width, height, (self.screenwidth - width) / 2, (self.screenheight - height) / 2)
        self.geometry(self.size)
        self.resizable(False, False)  # 设置窗口大小不可更改

        # 设置标题栏点击事件
        self.protocol("WM_DELETE_WINDOW", self.close_win)

    def close_win(self):  # 关闭窗口的回调函数
        # 询问是否退出
        if msg.askyesno(title="提示", message="是否退出？将不会保存你的文件！"):  # 确定退出
            self.destroy()
        else:  # 取消退出
            pass


class Desktop(tk.Frame):  # 主要界面
    def __init__(self, master=None):
        super().__init__(master)

        # 放置主要界面
        self.pack(fill=tk.BOTH, expand=True)

        # 菜单
        self.menu()

        # 工作区域
        self.working_area()

    def menu(self, ):  # 菜单
        global button_how_to_use, button_about
        # 创建一个框架存放菜单
        frame_menu = tk.Frame(self)
        frame_menu.place(x=0, y=0, width=width, height=50)  # 放置框架

        # 文件部分
        frame_menu_file = ttk.LabelFrame(frame_menu, text="文件")
        frame_menu_file.place(x=0, y=0, width=210, height=50)
        ttk.Button(frame_menu_file, text="导入(Ctrl+I)", cursor="hand2", command=self.import_file).place(x=0, y=0, width=100, height=30)
        ttk.Button(frame_menu_file, text="保存(Ctrl+S)", cursor="hand2", command=self.save_file).place(x=100, y=0, width=100, height=30)

        # 帮助部分
        frame_menu_help = ttk.LabelFrame(frame_menu, text="帮助")
        frame_menu_help.place(x=220, y=0, width=220, height=50)
        button_how_to_use = ttk.Button(frame_menu_help, text="使用说明(Ctrl+U)", cursor="hand2", command=self.how_to_use)
        button_how_to_use.place(x=0, y=0, width=110, height=30)
        button_about = ttk.Button(frame_menu_help, text="关于(Ctrl+A)", cursor="hand2", command=self.about_software)
        button_about.place(x=110, y=0, width=100, height=30)

    def import_file(self, ):  # 导入文件
        global now_file
        # 选择文件
        file_path = fdg.askopenfilename(title="导入文件", filetypes=[("Markdown 文件", "*.md")])  # 选择文件框
        if file_path == "":  # 取消选择文件
            msg.showinfo(title="提示", message="用户已取消选择文件！")
        else:
            now_file = file_path
            now_file_ = open(now_file, "r", encoding="utf-8")
            text_write.delete(1.0, tk.END)
            text_write.insert(tk.END, now_file_.read())
            now_file_.close()

    def save_file(self, ):  # 保存文件
        all_text = text_write.get(1.0, tk.END)
        if now_file == "":
            save_path = fdg.askdirectory(title="选择文件夹保存文件")
            if save_path == "":
                msg.showinfo(title="提示", message="用户已经取消了保存文件！请注意文件安全！")
            else:
                with open(f"{save_path}\\Markdown-Notepad-v1.0-make.md", "w", encoding="utf-8") as f:
                    f.write(all_text)
                msg.showinfo(title="提示", message="文件已保存！保存在 %s\\Markdown-Notepad-v1.0-make.md 中！" % save_path)
        else:
            with open(now_file, "w", encoding="utf-8") as f:
                f.write(all_text)
            msg.showinfo(title="提示", message="文件已保存！保存在 %s 中！" % now_file)

    def how_to_use(self, ):  # 使用说明
        # 读取文本
        with open("Data\\How_To_Use.txt", "r", encoding="utf-8") as f:
            text_words = f.read()

        # 创建窗口显示使用说明
        how_to_use_win = AboutToplevel(callback_option=button_how_to_use, master=self.master, text=text_words, title="使用说明")

    def about_software(self, ):  # 关于软件
        # 读取文本
        with open("Data\\about.txt", "r", encoding="utf-8") as f:
            text_words = f.read()
        
        # 创建窗口显示关于软件
        about_win = AboutToplevel(callback_option=button_about, master=self.master, text=text_words, title="关于")

    def working_area(self, ):  # 工作区域
        global text_write, label_line
        # 创建标签框架容纳所有的工作区域内容
        frame_working_area = ttk.LabelFrame(self, text="工作区域")
        frame_working_area.place(x=0, y=50, width=width, height=height-50)

        # 最上方快捷栏
        # 快捷栏框架
        frame_ink_buttons = tk.Frame(frame_working_area)
        frame_ink_buttons.place(x=0, y=0, width=width - 10, height=60)
        # 菜单按钮
        # 标题按钮
        title_menu_button = ttk.Menubutton(frame_ink_buttons, text="标题", cursor="hand2")
        title_menu_button.place(x=0, y=0, width=100, height=30)
        title_menu = tk.Menu(title_menu_button, tearoff=False)  # 创建按钮的二级菜单
        title_menu.add_command(label="# 一级标题", command=self.title_first)
        title_menu.add_command(label="## 二级标题", command=self.title_second)
        title_menu.add_command(label="### 三级标题", command=self.title_third)
        title_menu.add_command(label="#### 四级标题", command=self.title_fourth)
        title_menu.add_command(label="##### 五级标题", command=self.title_fifth)
        title_menu.add_command(label="###### 六级标题", command=self.title_sixth)
        title_menu_button.config(menu=title_menu)
        # 粗体/斜体
        strong_tilt_word_menu_button = ttk.Menubutton(frame_ink_buttons, text="粗体/斜体", cursor="hand2")
        strong_tilt_word_menu_button.place(x=100, y=0, width=100, height=30)
        strong_tilt_word_menu = tk.Menu(strong_tilt_word_menu_button, tearoff=False)
        strong_tilt_word_menu.add_command(label="粗体", command=self.strong_word)
        strong_tilt_word_menu.add_command(label="斜体", command=self.tilt_word)
        strong_tilt_word_menu.add_command(label="粗体+斜体", command=self.strong_and_tilt)
        strong_tilt_word_menu_button.config(menu=strong_tilt_word_menu)
        # 列表
        list_menu_button = ttk.Menubutton(frame_ink_buttons, text="列表", cursor="hand2")
        list_menu_button.place(x=200, y=0, width=100, height=30)
        list_menu = tk.Menu(list_menu_button, tearoff=False)
        list_menu.add_command(label="有序列表", command=self.list_with_number)
        list_menu.add_command(label="无序列表", command=self.list_without_number)
        list_menu_button.config(menu=list_menu)
        # 代码
        code_menu_button = ttk.Menubutton(frame_ink_buttons, text="代码", cursor="hand2")
        code_menu_button.place(x=300, y=0, width=100, height=30)
        code_menu = tk.Menu(code_menu_button, tearoff=False)
        code_menu.add_command(label="一行代码", command=self.code_line)
        code_menu.add_command(label="代码块(写完后请回车并打上4个空格)", command=self.code_lines)
        code_menu_button.config(menu=code_menu)
        # 任务列表
        task_list_menu_button = ttk.Menubutton(frame_ink_buttons, text="任务列表", cursor="hand2")
        task_list_menu_button.place(x=400, y=0, width=100, height=30)
        task_list_menu = tk.Menu(frame_ink_buttons, tearoff=False)
        task_list_menu.add_command(label="基本框", command=self.basic_list)
        task_list_menu.add_command(label="复选框", command=self.check_list)
        task_list_menu_button.config(menu=task_list_menu)
        # 单选按钮
        # 段落
        part_button = ttk.Button(frame_ink_buttons, text="段落(完后留空)", cursor="hand2", command=self.part_)
        part_button.place(x=500, y=0, width=100, height=30)
        # 换行
        next_line_button = ttk.Button(frame_ink_buttons, text="换行", cursor="hand2", command=self.next_line)
        next_line_button.place(x=600, y=0, width=100, height=30)    
        # 引用
        appoint_button = ttk.Button(frame_ink_buttons, text="引用", cursor="hand2", command=self.appoint_)
        appoint_button.place(x=700, y=0, width=100, height=30)
        # 分隔线
        separate_button = ttk.Button(frame_ink_buttons, text="分割线", cursor="hand2", command=self.separate_)
        separate_button.place(x=0, y=30, width=100, height=30)
        # 链接
        link_button = ttk.Button(frame_ink_buttons, text="链接", cursor="hand2", command=self.link_)
        link_button.place(x=100, y=30, width=100, height=30)
        # 图片
        picture_button = ttk.Button(frame_ink_buttons, text="图片", cursor="hand2", command=self.picture_)
        picture_button.place(x=200, y=30, width=100, height=30)
        # 转义
        change_mean_button = ttk.Button(frame_ink_buttons, text="转义", cursor="hand2", command=self.change_mean_)
        change_mean_button.place(x=300, y=30, width=100, height=30)
        # 表格
        form_button = ttk.Button(frame_ink_buttons, text="表格", cursor="hand2", command=self.form_)
        form_button.place(x=400, y=30, width=100, height=30)
        # 围栏代码块
        form_code_button = ttk.Button(frame_ink_buttons, text="围栏代码块", cursor="hand2", command=self.form_code_)
        form_code_button.place(x=500, y=30, width=100, height=30)
        # 定义列表
        mean_list_button = ttk.Button(frame_ink_buttons, text="定义列表", cursor="hand2", command=self.mean_list_)
        mean_list_button.place(x=600, y=30, width=100, height=30)
        # 删除线
        delete_line_button = ttk.Button(frame_ink_buttons, text="删除线", cursor="hand2", command=self.delete_line_)
        delete_line_button.place(x=700, y=30, width=100, height=30)
        # 预览按钮
        preview_button = ttk.Button(frame_ink_buttons, text="预览(条件：edge浏览器(\n默认浏览器)、在edge浏览\n器上成功安装了Markdown\n Viewer插件)", cursor="hand2", command=self.preview_)
        preview_button.place(x=800, y=0, width=width-810, height=60)

        # 编辑区域
        text_write = Text(x=0, y=60, width=width-10, height=height-160, text="", master=frame_working_area, state="normal")
        # 绑定编辑区域
        text_write.bind("<KeyRelease>", self.get_text_line)

        # 底部区域
        frame_count_area = tk.Frame(frame_working_area)
        frame_count_area.place(x=0, y=height-100, width=width-10, height=30)
        label_line = tk.Label(frame_count_area, text="总行数：%d" % total_line, anchor="w")
        label_line.place(x=0, y=0, width=100, height=30)

        quit_button = ttk.Button(frame_count_area, text="退出Markdown Notepad v1.0", cursor="hand2", command=lambda: win.close_win())
        quit_button.place(x=width-210, y=0, width=200, height=30)

    # 标题事件
    def title_first(self, ):  # 一级标题
        text_write.insert(tk.INSERT, "# ")
        text_write.focus_set()  # 自动聚焦到输入框内
    
    def title_second(self, ):
        text_write.insert(tk.INSERT, "## ")
        text_write.focus_set()  # 自动聚焦到输入框内

    def title_third(self, ):
        text_write.insert(tk.INSERT, "### ")
        text_write.focus_set()  # 自动聚焦到输入框内

    def title_fourth(self, ):
        text_write.insert(tk.INSERT, "#### ")
        text_write.focus_set()  # 自动聚焦到输入框内

    def title_fifth(self, ):
        text_write.insert(tk.INSERT, "##### ")
        text_write.focus_set()  # 自动聚焦到输入框内

    def title_sixth(self, ):
        text_write.insert(tk.INSERT, "###### ")
        text_write.focus_set()  # 自动聚焦到输入框内
        
    # 粗体斜体事件
    def strong_word(self, ):
        text_write.insert(tk.INSERT, "****")
        text_write.mark_set(tk.INSERT, "insert-2c")
        text_write.focus_set()  # 自动聚焦到输入框内

    def tilt_word(self, ):
        text_write.insert(tk.INSERT, "**")
        text_write.mark_set(tk.INSERT, "insert-1c")
        text_write.focus_set()

    def strong_and_tilt(self, ):
        text_write.insert(tk.INSERT, "******")
        text_write.mark_set(tk.INSERT, "insert-3c")
        text_write.focus_set()

    # 列表事件
    def list_with_number(self, ):  # 有序列表
        text_write.insert(tk.INSERT, "1. ")
        text_write.focus_set()  # 自动聚焦到输入框内

    def list_without_number(self, ):  # 无序列表
        text_write.insert(tk.INSERT, "- ")
        text_write.focus_set()  # 自动聚焦到输入框内

    # 代码事件
    def code_line(self, ):  # 一行代码
        text_write.insert(tk.INSERT, "``")
        text_write.mark_set(tk.INSERT, "insert-1c")
        text_write.focus_set()  # 自动聚焦到输入框内

    def code_lines(self, ):  # 多行代码
        text_write.insert(tk.INSERT, "    \n")
        text_write.focus_set()  # 自动聚焦到输入框内

    # 任务列表时间
    def basic_list(self, ):
        text_write.insert(tk.INSERT, "- [ ] ")
        text_write.focus_set()  # 自动聚焦到输入框内

    def check_list(self, ):
        text_write.insert(tk.INSERT, "- [x] ")
        text_write.focus_set()  # 自动聚焦到输入框内

    # 段落事件
    def part_(self, ):
        text_write.insert(tk.INSERT, "\n")
        text_write.focus_set()  # 自动聚焦到输入框内

    # 换行事件
    def next_line(self, ):
        text_write.insert(tk.INSERT, "  \n")
        text_write.focus_set()  # 自动聚焦到输入框内

    # 引用事件
    def appoint_(self, ):
        text_write.insert(tk.INSERT, "> ")
        text_write.focus_set()  # 自动聚焦到输入框内

    # 分隔线
    def separate_(self, ):
        text_write.insert(tk.INSERT, "\n---\n\n")
        text_write.focus_set()  # 自动聚焦到输入框内

    # 链接
    def link_(self, ):
        def delete_toplevel_():
            toplevel.attributes("-topmost", False)
            yes_no =  msg.askyesno(title="提示", message="确定退出？退出将不会保存你的更改！")
            if yes_no:
                toplevel.destroy()
            else:
                toplevel.attributes("-topmost", True)

        def certain_make():
            name = name_of_link.get()
            link_ = link_of_link.get()
            alt_ = alt_of_link.get()
            text_ = f"[{name}]({link_} [{alt_}])\n"
            text_write.insert(tk.INSERT, text_)
            text_write.focus_set()  # 自动聚焦到输入框内
            toplevel.destroy()

        name_of_link = tk.StringVar()
        link_of_link = tk.StringVar()
        alt_of_link = tk.StringVar()

        toplevel = tk.Toplevel(self.master)
        toplevel.title("链接输入")
        toplevel.geometry("%dx%d+%d+%d" % (200, 150, (self.master.winfo_screenwidth() - 200) / 2, (self.master.winfo_screenheight() - 150) / 2))
        toplevel.resizable(False, False)
        toplevel.protocol("WM_DELETE_WINDOW", delete_toplevel_)
        toplevel.attributes("-topmost", True)
        tk.Label(toplevel, text="链接名称：").place(x=0, y=0, width=100, height=30)
        ttk.Entry(toplevel, textvariable=name_of_link).place(x=100, y=0, width=100)
        tk.Label(toplevel, text="链接地址：").place(x=0, y=30, width=100, height=30)
        ttk.Entry(toplevel, textvariable=link_of_link).place(x=100, y=30, width=100)
        tk.Label(toplevel, text="鼠标悬浮时显示的值：", anchor="w").place(x=0, y=60, width=200, height=30)
        ttk.Entry(toplevel, textvariable=alt_of_link).place(x=100, y=90, width=100)
        ttk.Button(toplevel, text="确定", command=certain_make).place(x=150, y=120, width=50, height=30)
    
    # 图片
    def picture_(self, ):
        def delete_toplevel_():
            toplevel.attributes("-topmost", False)
            yes_no =  msg.askyesno(title="提示", message="确定退出？退出将不会保存你的更改！")
            if yes_no:
                toplevel.destroy()
            else:
                toplevel.attributes("-topmost", True)

        def certain_make():
            alt = alt_of_picture.get()
            address = address_of_picture.get()
            title_ = title_of_picture.get()
            _link_ = link_of_picture.get()
            text_ = f"[![{alt}]({address} {title_})]({_link_})\n"
            text_write.insert(tk.INSERT, text_)
            text_write.focus_set()
            toplevel.destroy()

        alt_of_picture = tk.StringVar()
        address_of_picture = tk.StringVar()
        title_of_picture = tk.StringVar()
        link_of_picture = tk.StringVar()

        toplevel = tk.Toplevel(self.master)
        toplevel.title("图片输入")
        toplevel.geometry("%dx%d+%d+%d" % (200, 150, (self.master.winfo_screenwidth() - 200) / 2, (self.master.winfo_screenheight() - 150) / 2))
        toplevel.resizable(False, False)
        toplevel.protocol("WM_DELETE_WINDOW", delete_toplevel_)
        toplevel.attributes("-topmost", True)
        tk.Label(toplevel, text="图片alt：").place(x=0, y=0, width=100, height=30)
        ttk.Entry(toplevel, textvariable=alt_of_picture).place(x=100, y=0, width=100)
        tk.Label(toplevel, text="图片地址：").place(x=0, y=30, width=100, height=30)
        ttk.Entry(toplevel, textvariable=address_of_picture).place(x=100, y=30, width=100)
        tk.Label(toplevel, text="图片标题：").place(x=0, y=60, width=100, height=30)
        ttk.Entry(toplevel, textvariable=title_of_picture).place(x=100, y=60, width=100)
        tk.Label(toplevel, text="图片链接：").place(x=0, y=90, width=100, height=30)
        ttk.Entry(toplevel, textvariable=link_of_picture).place(x=100, y=90, width=100)
        ttk.Button(toplevel, text="确定", command=certain_make).place(x=150, y=120, width=50, height=30)

    # 转义
    def change_mean_(self, ):
        text_write.insert(tk.INSERT, "\ ")
        text_write.focus_set()

    # 表格
    def form_(self, ):
        msg.showinfo(title="提示", message="表格暂不支持快捷创建！请移步使用说明查看表格的相关语法！")

    def get_text_line(self, event=None):  # 获取文本总行数
        global total_line
        line, c = map(int, event.widget.index("end-1c").split("."))
        total_line = line
        label_line.config(text="总行数：%d" % total_line)

    # 围栏代码块
    def form_code_(self, ):
        def delete_toplevel_():
            toplevel.attributes("-topmost", False)
            yes_no =  msg.askyesno(title="提示", message="确定退出？退出将不会保存你的更改！")
            if yes_no:
                toplevel.destroy()
            else:
                toplevel.attributes("-topmost", True)

        def certain_make():
            lauguage_ = lauguage.get()
            code_text = text_code_write.get(1.0, tk.END)
            text_ = "```[%s]\n{\n    %s\n}\n```\n" % (lauguage_, code_text)
            text_write.insert(tk.INSERT, text_)
            text_write.focus_set()
            toplevel.destroy()

        lauguage = tk.StringVar()

        toplevel = tk.Toplevel(self.master)
        toplevel.title("围栏代码块")
        toplevel.geometry("%dx%d+%d+%d" % (200, 150, (self.master.winfo_screenwidth() - 200) / 2, (self.master.winfo_screenheight() - 150) / 2))
        toplevel.resizable(False, False)
        toplevel.protocol("WM_DELETE_WINDOW", delete_toplevel_)
        toplevel.attributes("-topmost", True)
        tk.Label(toplevel, text="语言：").place(x=0, y=0, width=100, height=30)
        ttk.Entry(toplevel, textvariable=lauguage).place(x=100, y=0, width=100)
        tk.Label(toplevel, text="代码内容：", anchor="w").place(x=0, y=30, width=200, height=30)
        text_code_write = Text(x=0, y=60, width=200, height=60, text="", master=toplevel, state="normal")
        ttk.Button(toplevel, text="确定", command=certain_make).place(x=150, y=120, width=50, height=30)

    # 定义列表
    def mean_list_(self, ):
        text_write.insert(tk.INSERT, ": ")
        text_write.focus_set()

    # 删除线
    def delete_line_(self, ):
        text_write.insert(tk.INSERT, "~~~~")
        text_write.mark_set(tk.INSERT, "insert-2c")
        text_write.focus_set()

    # 预览
    def preview_(self, ):
        text_preview = text_write.get(1.0, tk.END)  # 获取值
        with open("test.md", "w", encoding="utf-8") as f:
            f.write(text_preview)
        os.system(f'start "" "msedge.exe" "{os.path.dirname(os.path.abspath("test.md"))}\\test.md"')

    
class AboutToplevel(tk.Toplevel):  # 查看信息窗口
    def __init__(self, callback_option=None, master=None, text="", title=""):
        super().__init__(master)

        self.callback_option = callback_option
        self.master = master
        self.text = text
        self.title_ = title

        # 设置触发此对象的按钮失效
        self.callback_option.config(state="disabled")

        # 设置标题
        self.title(self.title_)

        # 设置窗口大小
        self.width, self.height = 400, 300
        self.screenwidth, self.screenheight = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        self.size = "%dx%d+%d+%d" % (self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.geometry(self.size)
        self.resizable(False, False)  # 设置窗口大小不可更改

        # 设置窗口位于顶部
        self.attributes("-topmost", "True")

        # 设置点击标题栏退出按钮的执行韩式
        self.protocol("WM_DELETE_WINDOW", self.quit_win)

        # 文本显示
        self.text_area()

    def text_area(self, ):  # 文本显示区域
        # 文本框
        text_option = Text(x=0, y=0, width=self.width, height=self.height-30, text=self.text, master=self, state="disabled")

        # 确定(退出)按钮
        ttk.Button(self, text="确定", command=self.quit_win, cursor="hand2").place(x=self.width-50, y=self.height-30, width=50, height=30)

    def quit_win(self, ):  # 退出窗口
        self.destroy()
        self.callback_option.config(state="normal")


class Text(tk.Text):  # 文本框对象
    def __init__(self, x, y, width, height, text="", master=None, state="normal"):
        super().__init__(master)

        self.master = master
        self.text = text
        self.state = state

        # 放置文本框
        self.place(x=x, y=y, width=width-20, height=height-20)

        # 滚动条
        self.scrollbarx = ttk.Scrollbar(self.master, command=self.xview, orient=tk.HORIZONTAL, cursor="hand2")
        self.scrollbarx.place(x=x, y=y+height-20, width=width-20, height=20)
        self.scrollbary = ttk.Scrollbar(self.master, command=self.yview, cursor="hand2")
        self.scrollbary.place(x=x+width-20, y=y, width=20, height=height-20)

        # 文本框属性设置
        self.config(xscrollcommand=self.scrollbarx.set)
        self.config(yscrollcommand=self.scrollbary.set)
        self.config(wrap="none")  # 设置文本不换行
        self.insert("end", self.text)
        self.config(state=self.state)


if __name__ == "__main__":  # 运行入口
    win = Win()  # 生成窗口
    desktop = Desktop(win)

    win.mainloop()  # 显示窗口
