import  tkinter
from tkinter import font


'''
    +------+-----------------+
    |Station 1               |
    +------+-----------------+
    | 箱件狀態 | 有箱 | 無箱  |
    +------+------+----------+
    | 按鈕觸發 |  有  |  無   |
    +-------------+----------+
    | 滾筒動作 | 轉動 | 停止  |
    +-------------+----------+
'''

if __name__ == '__main__':
    win = tkinter.Tk()
    win.title('YID Grid')
    win.geometry('800x600')

    myfont = font.Font(family='Helvetica', size=36, weight='bold')
    label_station1 = tkinter.Label(text='Station 1', font=myfont)
    label_box = tkinter.Label(text='箱件狀態', font=myfont)
    label_trigger = tkinter.Label(text='按鈕觸發', font=myfont)
    label_roller = tkinter.Label(text='滾筒動作', font=myfont)

    btn_box_1 = tkinter.Button(text='有箱', font=myfont)
    btn_box_0 = tkinter.Button(text='無箱', font=myfont)
    btn_trigger_1 = tkinter.Button(text='有', font=myfont)
    btn_trigger_0 = tkinter.Button(text='無', font=myfont)
    btn_roller_1 = tkinter.Button(text='轉動', font=myfont)
    btn_roller_0 = tkinter.Button(text='停止', font=myfont)

    # View 元件佈局
    win.rowconfigure((0, 1, 2, 3), weight=1) # 列 0, 列 1 同步放大縮小
    win.columnconfigure((0, 1, 2), weight=1) # 欄 0, 欄 1 同步放大縮小

    label_station1.grid(row=0, column=0, columnspan=3, sticky='EWNS')  # sticky='EWNS' 無縫填滿

    label_box.grid(row=1, column=0, sticky='EWNS')
    btn_box_0.grid(row=1, column=1, sticky='EWNS')
    btn_box_1.grid(row=1, column=2, sticky='EWNS')

    label_trigger.grid(row=2, column=0, sticky='EWNS')
    btn_trigger_0.grid(row=2, column=1, sticky='EWNS')
    btn_trigger_1.grid(row=2, column=2, sticky='EWNS')

    label_roller.grid(row=3, column=0, sticky='EWNS')
    btn_roller_0.grid(row=3, column=1, sticky='EWNS')
    btn_roller_1.grid(row=3, column=2, sticky='EWNS')


    win.mainloop()