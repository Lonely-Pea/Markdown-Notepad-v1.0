# 关于Markdown Notepad v1.0
作者：Lonely-Pea  
版本：v1.0

# Markdown Notepad v1.0 实现方式

使用tkinter模块和tkinter的相关子模块来实现软件的图形化界面  
下面是该软件所需要的所有模块和主要功能：  

| 模块 | 用途 |
|:----:|:----:|
|tkinter|创建图形化界面|
|tkinter.filedialog|创建文件选择框|
|tkinter.messagebox|创建弹窗|
|tkinter.ttk|美化窗口|
|os|处理文件

下面是软件的主要思路：  

1. 界面
: 使用tkinter相关模块创建窗口，并在窗口内添加各种内容。
2. 文件
: 使用os模块实现对文件的处理。
3. 编辑
: 使用tkinter的Text组件实现对文件的编辑。

# Markdown Notepad v1.0 主要功能

编辑md(Markdown)文件。

# 语法细则

with
：with 可以用来打开和对文件进行相关处理。
: 使用`with open(__file__, "w") as f:`
: 编辑__file__。
os.system
: os.system 可以用来执行Windows系统上的终端指令。
: `os.system(f'start "" "msedge.exe" "{os.path.dirname(os.path.abspath("test.md"))}\\test.md"')`可以用来在edge浏览器中打开md文件。前提是你必须已经安装好了edge浏览器并且已经安装好了Markdown Viewer插件。

# 代码解析
(1)生成窗口  
```[Python]
{
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


}
```

创建了Win对象，调用tkinter.Tk对象。  
(2)保存文件  
```[Python]
{
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

}
```

`all_text = text_write.get(1.0, tk.END)`获取了文本框内全部的内容。
其余的则是调用了`tkinter.filedialog`模块和`with open() as f:`代码来实现保存。

# 结尾
制作软件不易，如果对你有帮助的话可以给一个star吗？ :)






