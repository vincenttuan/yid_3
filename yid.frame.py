import tkinter
from tkinter import font, Frame, PhotoImage

'''
    +---------------------+
    | Station 1           |
    +---------------------+
    | 箱件狀態 | 有箱 | 無箱 |
    +--------+------+-----+
    | 按鈕觸發 |  有  | 無  |
    +--------+------+-----+
    | 滾筒動作 | 轉動 | 停止 |
    +--------+------+-----+
'''

def station1_box_status():
    print("station1_box_status")


def station4_box_status():
    print("station4_box_status")


if __name__ == '__main__':
    win = tkinter.Tk()
    win.title('YID Grid')
    win.geometry('771x600')

    myfont = font.Font(family='Helvetica', size=12, weight='normal')
    myfont36 = font.Font(family='Helvetica', size=18, weight='bold')

    img1 = PhotoImage(file='btn_bg1.png')
    img2 = PhotoImage(file='btn_bg2.png')

    # View 元件佈局
    win.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1)  # 列 0, 列 1 同步放大縮小
    win.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)  # 欄 0, 欄 1, 欄 2 同步放大縮小

    # View 元件
    # -----------------------------------------------------------------------------------------
    label_station1 = tkinter.Label(text='Station 1', font=myfont36)
    label_box = tkinter.Label(text='箱件狀態', font=myfont)
    label_trigger = tkinter.Label(text='按鈕觸發', font=myfont)
    label_roller = tkinter.Label(text='滾筒動作', font=myfont)

    btn_box_1 = tkinter.Label(text='有箱', font=myfont, image=img1, compound='center')
    btn_box_1.bind("<Button-1>", lambda e: station1_box_status())

    btn_box_0 = tkinter.Label(text='無箱', font=myfont, image=img2, compound='center')
    btn_trigger_1 = tkinter.Label(text='有', font=myfont, image=img1, compound='center')
    btn_trigger_0 = tkinter.Label(text='無', font=myfont, image=img2, compound='center')
    btn_roller_1 = tkinter.Label(text='轉動', font=myfont, image=img1, compound='center')
    btn_roller_0 = tkinter.Label(text='停止', font=myfont, image=img2, compound='center')

    label_station1.grid(row=0, column=0, columnspan=2, sticky='EWNS')  # sticky='EWNS' 無縫填滿

    label_box.grid(row=1, column=0, sticky='EWNS')
    btn_box_1.grid(row=1, column=1, sticky='EWNS')
    btn_box_0.grid(row=1, column=2, sticky='EWNS')

    label_trigger.grid(row=2, column=0, sticky='EWNS')
    btn_trigger_1.grid(row=2, column=1, sticky='EWNS')
    btn_trigger_0.grid(row=2, column=2, sticky='EWNS')

    label_roller.grid(row=3, column=0, sticky='EWNS')
    btn_roller_1.grid(row=3, column=1, sticky='EWNS')
    btn_roller_0.grid(row=3, column=2, sticky='EWNS')

    # -----------------------------------------------------------------------------------------

    label_station1 = tkinter.Label(text='Station 2', font=myfont36)
    label_box = tkinter.Label(text='箱件狀態', font=myfont)
    label_trigger = tkinter.Label(text='按鈕觸發', font=myfont)
    label_roller = tkinter.Label(text='滾筒動作', font=myfont)

    btn_box_1 = tkinter.Label(text='有箱', font=myfont, image=img1, compound='center')
    btn_box_0 = tkinter.Label(text='無箱', font=myfont, image=img2, compound='center')
    btn_trigger_1 = tkinter.Label(text='有', font=myfont, image=img1, compound='center')
    btn_trigger_0 = tkinter.Label(text='無', font=myfont, image=img2, compound='center')
    btn_roller_1 = tkinter.Label(text='轉動', font=myfont, image=img1, compound='center')
    btn_roller_0 = tkinter.Label(text='停止', font=myfont, image=img2, compound='center')

    label_station1.grid(row=4, column=0, columnspan=2, sticky='EWNS')  # sticky='EWNS' 無縫填滿

    label_box.grid(row=5, column=0, sticky='EWNS')
    btn_box_1.grid(row=5, column=1, sticky='EWNS')
    btn_box_0.grid(row=5, column=2, sticky='EWNS')

    label_trigger.grid(row=6, column=0, sticky='EWNS')
    btn_trigger_1.grid(row=6, column=1, sticky='EWNS')
    btn_trigger_0.grid(row=6, column=2, sticky='EWNS')

    label_roller.grid(row=7, column=0, sticky='EWNS')
    btn_roller_1.grid(row=7, column=1, sticky='EWNS')
    btn_roller_0.grid(row=7, column=2, sticky='EWNS')

    # -----------------------------------------------------------------------------------------

    label_station1 = tkinter.Label(text='Station 3', font=myfont36)
    label_box = tkinter.Label(text='箱件狀態', font=myfont)
    label_trigger = tkinter.Label(text='按鈕觸發', font=myfont)
    label_roller = tkinter.Label(text='滾筒動作', font=myfont)

    btn_box_1 = tkinter.Label(text='有箱', font=myfont, image=img1, compound='center')
    btn_box_0 = tkinter.Label(text='無箱', font=myfont, image=img2, compound='center')
    btn_trigger_1 = tkinter.Label(text='有', font=myfont, image=img1, compound='center')
    btn_trigger_0 = tkinter.Label(text='無', font=myfont, image=img2, compound='center')
    btn_roller_1 = tkinter.Label(text='轉動', font=myfont, image=img1, compound='center')
    btn_roller_0 = tkinter.Label(text='停止', font=myfont, image=img2, compound='center')

    label_station1.grid(row=8, column=0, columnspan=2, sticky='EWNS')  # sticky='EWNS' 無縫填滿

    label_box.grid(row=9, column=0, sticky='EWNS')
    btn_box_1.grid(row=9, column=1, sticky='EWNS')
    btn_box_0.grid(row=9, column=2, sticky='EWNS')

    label_trigger.grid(row=10, column=0, sticky='EWNS')
    btn_trigger_1.grid(row=10, column=1, sticky='EWNS')
    btn_trigger_0.grid(row=10, column=2, sticky='EWNS')

    label_roller.grid(row=11, column=0, sticky='EWNS')
    btn_roller_1.grid(row=11, column=1, sticky='EWNS')
    btn_roller_0.grid(row=11, column=2, sticky='EWNS')

    # -----------------------------------------------------------------------------------------

    label_station1 = tkinter.Label(text='Station 4', font=myfont36)
    label_box = tkinter.Label(text='箱件狀態', font=myfont)
    label_trigger = tkinter.Label(text='按鈕觸發', font=myfont)
    label_roller = tkinter.Label(text='滾筒動作', font=myfont)

    btn_box_1 = tkinter.Label(text='有箱', font=myfont, image=img1, compound='center')
    btn_box_1.bind("<Button-1>", lambda e: station1_box_status())

    btn_box_0 = tkinter.Label(text='無箱', font=myfont, image=img2, compound='center')
    btn_trigger_1 = tkinter.Label(text='有', font=myfont, image=img1, compound='center')
    btn_trigger_0 = tkinter.Label(text='無', font=myfont, image=img2, compound='center')
    btn_roller_1 = tkinter.Label(text='轉動', font=myfont, image=img1, compound='center')
    btn_roller_0 = tkinter.Label(text='停止', font=myfont, image=img2, compound='center')

    label_station1.grid(row=0, column=3, columnspan=2, sticky='EWNS')  # sticky='EWNS' 無縫填滿

    label_box.grid(row=1, column=3, sticky='EWNS')
    btn_box_1.grid(row=1, column=4, sticky='EWNS')
    btn_box_0.grid(row=1, column=5, sticky='EWNS')

    label_trigger.grid(row=2, column=3, sticky='EWNS')
    btn_trigger_1.grid(row=2, column=4, sticky='EWNS')
    btn_trigger_0.grid(row=2, column=5, sticky='EWNS')

    label_roller.grid(row=3, column=3, sticky='EWNS')
    btn_roller_1.grid(row=3, column=4, sticky='EWNS')
    btn_roller_0.grid(row=3, column=5, sticky='EWNS')

    # -----------------------------------------------------------------------------------------

    label_station1 = tkinter.Label(text='Station 5', font=myfont36)
    label_box = tkinter.Label(text='箱件狀態', font=myfont)
    label_trigger = tkinter.Label(text='按鈕觸發', font=myfont)
    label_roller = tkinter.Label(text='滾筒動作', font=myfont)

    btn_box_1 = tkinter.Label(text='有箱', font=myfont, image=img1, compound='center')
    btn_box_1.bind("<Button-1>", lambda e: station1_box_status())

    btn_box_0 = tkinter.Label(text='無箱', font=myfont, image=img2, compound='center')
    btn_trigger_1 = tkinter.Label(text='有', font=myfont, image=img1, compound='center')
    btn_trigger_0 = tkinter.Label(text='無', font=myfont, image=img2, compound='center')
    btn_roller_1 = tkinter.Label(text='轉動', font=myfont, image=img1, compound='center')
    btn_roller_0 = tkinter.Label(text='停止', font=myfont, image=img2, compound='center')

    label_station1.grid(row=4, column=3, columnspan=2, sticky='EWNS')  # sticky='EWNS' 無縫填滿

    label_box.grid(row=5, column=3, sticky='EWNS')
    btn_box_1.grid(row=5, column=4, sticky='EWNS')
    btn_box_0.grid(row=5, column=5, sticky='EWNS')

    label_trigger.grid(row=6, column=3, sticky='EWNS')
    btn_trigger_1.grid(row=6, column=4, sticky='EWNS')
    btn_trigger_0.grid(row=6, column=5, sticky='EWNS')

    label_roller.grid(row=7, column=3, sticky='EWNS')
    btn_roller_1.grid(row=7, column=4, sticky='EWNS')
    btn_roller_0.grid(row=7, column=5, sticky='EWNS')

    # -----------------------------------------------------------------------------------------

    label_station1 = tkinter.Label(text='Station 6', font=myfont36)
    label_box = tkinter.Label(text='箱件狀態', font=myfont)
    label_trigger = tkinter.Label(text='按鈕觸發', font=myfont)
    label_roller = tkinter.Label(text='滾筒動作', font=myfont)

    btn_box_1 = tkinter.Label(text='有箱', font=myfont, image=img1, compound='center')
    btn_box_1.bind("<Button-1>", lambda e: station1_box_status())

    btn_box_0 = tkinter.Label(text='無箱', font=myfont, image=img2, compound='center')
    btn_trigger_1 = tkinter.Label(text='有', font=myfont, image=img1, compound='center')
    btn_trigger_0 = tkinter.Label(text='無', font=myfont, image=img2, compound='center')
    btn_roller_1 = tkinter.Label(text='轉動', font=myfont, image=img1, compound='center')
    btn_roller_0 = tkinter.Label(text='停止', font=myfont, image=img2, compound='center')

    label_station1.grid(row=8, column=3, columnspan=2, sticky='EWNS')  # sticky='EWNS' 無縫填滿

    label_box.grid(row=9, column=3, sticky='EWNS')
    btn_box_1.grid(row=9, column=4, sticky='EWNS')
    btn_box_0.grid(row=9, column=5, sticky='EWNS')

    label_trigger.grid(row=10, column=3, sticky='EWNS')
    btn_trigger_1.grid(row=10, column=4, sticky='EWNS')
    btn_trigger_0.grid(row=10, column=5, sticky='EWNS')

    label_roller.grid(row=11, column=3, sticky='EWNS')
    btn_roller_1.grid(row=11, column=4, sticky='EWNS')
    btn_roller_0.grid(row=11, column=5, sticky='EWNS')

    win.mainloop()