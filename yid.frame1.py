import tkinter
from tkinter import font, PhotoImage

from yid_control import mod_switch
from yid_util import get_ip_address

if __name__ == '__main__':
    win = tkinter.Tk()
    win.title('YID ' + get_ip_address())
    win.geometry('253x600')

    myfont = font.Font(family='Helvetica', size=12, weight='normal')
    myfont36 = font.Font(family='Helvetica', size=18, weight='bold')

    img1 = PhotoImage(file='btn_bg1.png')
    img2 = PhotoImage(file='btn_bg2.png')
    img3 = PhotoImage(file='yid_logo2.png')


    # View 元件佈局
    win.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1)  # 列 0, 列 1 同步放大縮小
    win.columnconfigure((0, 1), weight=1)  # 欄 0, 欄 1, 欄 2 同步放大縮小

    # View 元件
    # -----------------------------------------------------------------------------------------
    label_logo = tkinter.Label(font=myfont36, image=img3)
    label_mode = tkinter.Label(text='模式切換', font=myfont)
    label_linkage = tkinter.Label(text='連線狀態', font=myfont)
    label_warehouse = tkinter.Label(text='倉庫流道', font=myfont)

    btn_mode_str = tkinter.StringVar()
    btn_mode_str.set("自動")
    btn_mode = tkinter.Label(textvariable=btn_mode_str, font=myfont, image=img2, compound='center')
    btn_mode.bind("<Button-1>", lambda e: mod_switch(btn_mode_str))
    btn_linkage = tkinter.Label(text='連/斷線', font=myfont, image=img2, compound='center')
    btn_warehouse = tkinter.Label(text='正/異常', font=myfont, image=img2, compound='center')

    label_logo.grid(row=0, column=0, rowspan=8, columnspan=2, sticky='EWNS')  # sticky='EWNS' 無縫填滿

    label_mode.grid(row=8, column=0, sticky='EWNS')
    btn_mode.grid(row=8, column=1, sticky='EWNS')

    label_linkage.grid(row=9, column=0, sticky='EWNS')
    btn_linkage.grid(row=9, column=1, sticky='EWNS')

    label_warehouse.grid(row=10, column=0, sticky='EWNS')
    btn_warehouse.grid(row=10, column=1, sticky='EWNS')

    win.mainloop()