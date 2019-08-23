import tkinter as tk


def main():
    # 创建一个主窗口，用于容纳整个GUI程序
    root = tk.Tk()
    # 设置主窗口对象的标题栏
    root.title('NEW')
    # 添加Label组件
    theLabel = tk.Label(root, text="就是体验一下")
    theLabel.pack()
    # 显示主窗口
    root.mainloop()


if __name__ == "__main__":
    main()