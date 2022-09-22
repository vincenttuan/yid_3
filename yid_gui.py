import tkinter
from tkinter import messagebox

def show_msg():
    # messagebox.showinfo('my title', 'Hello YID')
    choice = messagebox.askyesnocancel('my title', 'Hello YID 請選擇?')
    # 按下 cancel -> None
    # 按下 yes -> True
    # 按下 no -> False
    print(choice, type(choice))

def close_win():
    win.quit()

def add():
    print(mytext.get(), type(mytext.get()))
    value = int(mytext.get()) + 1
    print(value, type(value))
    mytext.set(str(value))
    pass

if __name__ == '__main__':
    win = tkinter.Tk()
    win.title('YID')
    win.geometry("600x400")
    myfont = ("Courier", 44)
    btfont = ("Courier", 36)

    mytext = tkinter.StringVar()
    mytext.set("0")
    # 放置元件
    label =tkinter.Label(win, textvariable=mytext)
    label.pack()

    button1 = tkinter.Button(win, text="OK", font=btfont, command=show_msg)
    label.config(font=("Courier", 44))
    button1.pack(side=tkinter.LEFT)

    button2 = tkinter.Button(win, text="Exit", font=btfont, command=close_win)
    button2.pack(side=tkinter.RIGHT)

    button3 = tkinter.Button(win, text="Add", font=btfont, command=add)
    button3.pack()

    win.mainloop()