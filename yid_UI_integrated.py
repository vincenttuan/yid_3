import tkinter
from tkinter import font, PhotoImage  # 引用字型與圖片功能

'''
from yid_control import mod_switch, link_status, warehouse_status, \
     st1_box_status_1, st1_box_status_0, st1_trigger_status_1, st1_trigger_status_0, st1_roller_move_1, st1_roller_move_0
     # 從 yid_control 頁籤 引用function
'''

from yid_control_t import mod_switch, link_status, warehouse_status, click_station_service


from yid_util import get_ip_address   # 從 yid_util 頁籤 引用function(IP位址)

if __name__ == '__main__':
    win = tkinter.Tk()  # 定義 win 等於 tkinter.Tk() 功能函數表頭，簡化後續coding
    win.title('YID ' + get_ip_address())  # 設定 UI 標題，並加上本機 IP 位址
    win.geometry('1024x600')  # 設定 UI 畫素尺寸
    # win.configure(bg='white')  # 設定背景顏色

    myfont = font.Font(family='Helvetica', size=18, weight='normal')  # 定義一般字型，簡化後續coding
    myfont_st = font.Font(family='Helvetica', size=30, weight='bold')  # 定義小標字型，簡化後續coding

    img1 = PhotoImage(file='btn_bg1.png')  # 定義 第 1 類 按鈕引用圖片，簡化後續coding
    img2 = PhotoImage(file='btn_bg2.png')  # 定義 第 2 類 按鈕引用圖片，簡化後續coding
    img3 = PhotoImage(file='yid_logo2.png')  # 定義 LOGO + 系統名稱 引用圖片，簡化後續coding


    # View 元件佈局
    win.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1)  # 列 0  列 1 同步放大縮小
    win.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)  # 欄 0, 欄 1, 欄 2 同步放大縮小

    # View 元件
    # -----Logo、模式切換、連線狀態、倉庫狀態等UI架構-------------------------------------------------------
    label_logo = tkinter.Label(image=img3)  # 定義 logo 格式為 Label，並引用圖片
    label_mode = tkinter.Label(text='模式切換', font=myfont) # 定義 模式切換 格式為 Label，並設定顯示內容與字型
    label_linkage = tkinter.Label(text='連線狀態', font=myfont)
    label_warehouse = tkinter.Label(text='倉庫流道', font=myfont)

    btn_mode_str = tkinter.StringVar()  # 定義 btn_mode_str 為 TK 字串變數
    btn_mode_str.set("自動")  # 預設填入文字為 "自動"
    btn_mode = tkinter.Label(textvariable=btn_mode_str, font=myfont, image=img2, compound='center')
    # 設定 模式切換 按鈕的顯示方式，特別注意 文字變數 的引用
    btn_mode.bind("<Button-1>", lambda e: mod_switch(btn_mode_str))
    # 由於不希望出現框限，故前列將 顯示型態 設定為 Label，但因本質上還是按鈕，故引用 外加按鈕 定義攻勢，須注意 要 def 相對應的function

    btn_linkage_str = tkinter.StringVar()
    btn_linkage_str.set("離線")
    btn_linkage = tkinter.Label(textvariable=btn_linkage_str, font=myfont, image=img2, compound='center')
    btn_linkage.bind("<Button-1>", lambda e: link_status(btn_linkage_str))

    btn_warehouse_str = tkinter.StringVar()
    btn_warehouse_str.set("正常")
    btn_warehouse = tkinter.Label(textvariable=btn_warehouse_str, font=myfont, image=img2, compound='center')
    btn_warehouse.bind("<Button-1>", lambda e: warehouse_status(btn_warehouse_str))

    label_logo.grid(row=0, column=0, rowspan=8, columnspan=2, sticky='EWNS')  # sticky='EWNS' 無縫填滿
    # 設定 logo 顯示的 左上角起始位置、所佔列高(8)、所佔行寬(2)

    label_mode.grid(row=9, column=0, sticky='EWNS')  # 設定 模式切換 標籤 顯示的位置與配置原則 無縫填滿
    btn_mode.grid(row=9, column=1, sticky='EWNS')  # 設定 模式切換 按鈕 顯示的位置與配置原則 無縫填滿

    label_linkage.grid(row=10, column=0, sticky='EWNS')
    btn_linkage.grid(row=10, column=1, sticky='EWNS')

    label_warehouse.grid(row=11, column=0, sticky='EWNS')
    btn_warehouse.grid(row=11, column=1, sticky='EWNS')
    # -----第 1 站UI架構-------------------------------------------------------------------------------

    label_station = tkinter.Label(text='Station 1', font=myfont_st)
    label_box = tkinter.Label(text='箱件狀態', font=myfont)
    label_trigger = tkinter.Label(text='按鈕觸發', font=myfont)
    label_roller = tkinter.Label(text='滾筒動作', font=myfont)

    btn_box_1 = tkinter.Label(text='有箱', font=myfont, image=img1, compound='center')
    btn_box_0 = tkinter.Label(text='無箱', font=myfont, image=img2, compound='center')
    btn_trigger_1_1 = tkinter.Label(text='有', font=myfont, image=img1, compound='center')
    btn_trigger_1_0 = tkinter.Label(text='無', font=myfont, image=img2, compound='center')
    btn_roller_1_1 = tkinter.Label(text='轉動', font=myfont, image=img1, compound='center')
    btn_roller_1_0 = tkinter.Label(text='停止', font=myfont, image=img2, compound='center')

    btn_trigger_1_1.bind("<Button-1>", lambda e: click_station_service(1, 2, 1, btn_trigger_1_1, btn_trigger_1_0))
    btn_trigger_1_0.bind("<Button-1>", lambda e: click_station_service(1, 2, 0, btn_trigger_1_1, btn_trigger_1_0))
    btn_roller_1_1.bind("<Button-1>", lambda e: click_station_service(1, 3, 1, btn_roller_1_1, btn_roller_1_0))
    btn_roller_1_0.bind("<Button-1>", lambda e: click_station_service(1, 3, 0, btn_roller_1_1, btn_roller_1_0))

    label_station.grid(row=0, column=2, columnspan=2, sticky='EWNS')  # sticky='EWNS' 無縫填滿

    label_box.grid(row=1, column=2, sticky='EWNS')
    btn_box_1.grid(row=1, column=3, sticky='EWNS')
    btn_box_0.grid(row=1, column=4, sticky='EWNS')

    label_trigger.grid(row=2, column=2, sticky='EWNS')
    btn_trigger_1_1.grid(row=2, column=3, sticky='EWNS')
    btn_trigger_1_0.grid(row=2, column=4, sticky='EWNS')

    label_roller.grid(row=3, column=2, sticky='EWNS')
    btn_roller_1_1.grid(row=3, column=3, sticky='EWNS')
    btn_roller_1_0.grid(row=3, column=4, sticky='EWNS')

    # -----第 2 站UI架構-------------------------------------------------------------------

    label_station1 = tkinter.Label(text='Station 2', font=myfont_st)
    label_box = tkinter.Label(text='箱件狀態', font=myfont)
    label_trigger = tkinter.Label(text='按鈕觸發', font=myfont)
    label_roller = tkinter.Label(text='滾筒動作', font=myfont)

    btn_box_1 = tkinter.Label(text='有箱', font=myfont, image=img1, compound='center')
    btn_box_0 = tkinter.Label(text='無箱', font=myfont, image=img2, compound='center')
    btn_trigger_1 = tkinter.Label(text='有', font=myfont, image=img1, compound='center')
    btn_trigger_1.bind("<Button-1>", lambda e: click_station_service(2, 2, 1))
    btn_trigger_0 = tkinter.Label(text='無', font=myfont, image=img2, compound='center')
    btn_trigger_0.bind("<Button-1>", lambda e: click_station_service(2, 2, 0))
    btn_roller_1 = tkinter.Label(text='轉動', font=myfont, image=img1, compound='center')
    btn_roller_1.bind("<Button-1>", lambda e: click_station_service(2, 3, 1))
    btn_roller_0 = tkinter.Label(text='停止', font=myfont, image=img2, compound='center')
    btn_roller_0.bind("<Button-1>", lambda e: click_station_service(2, 3, 0))

    label_station1.grid(row=4, column=2, columnspan=2, sticky='EWNS')  # sticky='EWNS' 無縫填滿

    label_box.grid(row=5, column=2, sticky='EWNS')
    btn_box_1.grid(row=5, column=3, sticky='EWNS')
    btn_box_0.grid(row=5, column=4, sticky='EWNS')

    label_trigger.grid(row=6, column=2, sticky='EWNS')
    btn_trigger_1.grid(row=6, column=3, sticky='EWNS')
    btn_trigger_0.grid(row=6, column=4, sticky='EWNS')

    label_roller.grid(row=7, column=2, sticky='EWNS')
    btn_roller_1.grid(row=7, column=3, sticky='EWNS')
    btn_roller_0.grid(row=7, column=4, sticky='EWNS')

    # ------第 3 站UI架構--------------------------------------------------------------------

    label_station1 = tkinter.Label(text='Station 3', font=myfont_st)
    label_box = tkinter.Label(text='箱件狀態', font=myfont)
    label_trigger = tkinter.Label(text='按鈕觸發', font=myfont)
    label_roller = tkinter.Label(text='滾筒動作', font=myfont)

    btn_box_1 = tkinter.Label(text='有箱', font=myfont, image=img1, compound='center')
    btn_box_0 = tkinter.Label(text='無箱', font=myfont, image=img2, compound='center')
    btn_trigger_1 = tkinter.Label(text='有', font=myfont, image=img1, compound='center')
    btn_trigger_1.bind("<Button-1>", lambda e: click_station_service(3, 2, 1))
    btn_trigger_0 = tkinter.Label(text='無', font=myfont, image=img2, compound='center')
    btn_trigger_0.bind("<Button-1>", lambda e: click_station_service(3, 2, 0))
    btn_roller_1 = tkinter.Label(text='轉動', font=myfont, image=img1, compound='center')
    btn_roller_1.bind("<Button-1>", lambda e: click_station_service(3, 3, 1))
    btn_roller_0 = tkinter.Label(text='停止', font=myfont, image=img2, compound='center')
    btn_roller_0.bind("<Button-1>", lambda e: click_station_service(3, 3, 0))

    label_station1.grid(row=8, column=2, columnspan=2, sticky='EWNS')  # sticky='EWNS' 無縫填滿

    label_box.grid(row=9, column=2, sticky='EWNS')
    btn_box_1.grid(row=9, column=3, sticky='EWNS')
    btn_box_0.grid(row=9, column=4, sticky='EWNS')

    label_trigger.grid(row=10, column=2, sticky='EWNS')
    btn_trigger_1.grid(row=10, column=3, sticky='EWNS')
    btn_trigger_0.grid(row=10, column=4, sticky='EWNS')

    label_roller.grid(row=11, column=2, sticky='EWNS')
    btn_roller_1.grid(row=11, column=3, sticky='EWNS')
    btn_roller_0.grid(row=11, column=4, sticky='EWNS')

    # -----第 4 站UI架構----------------------------------------------------------------------

    label_station1 = tkinter.Label(text='Station 4', font=myfont_st)
    label_box = tkinter.Label(text='箱件狀態', font=myfont)
    label_trigger = tkinter.Label(text='按鈕觸發', font=myfont)
    label_roller = tkinter.Label(text='滾筒動作', font=myfont)

    btn_box_1 = tkinter.Label(text='有箱', font=myfont, image=img1, compound='center')
    btn_box_0 = tkinter.Label(text='無箱', font=myfont, image=img2, compound='center')
    btn_trigger_1 = tkinter.Label(text='有', font=myfont, image=img1, compound='center')
    btn_trigger_1.bind("<Button-1>", lambda e: click_station_service(4, 2, 1))
    btn_trigger_0 = tkinter.Label(text='無', font=myfont, image=img2, compound='center')
    btn_trigger_0.bind("<Button-1>", lambda e: click_station_service(4, 2, 0))
    btn_roller_1 = tkinter.Label(text='轉動', font=myfont, image=img1, compound='center')
    btn_roller_1.bind("<Button-1>", lambda e: click_station_service(4, 3, 1))
    btn_roller_0 = tkinter.Label(text='停止', font=myfont, image=img2, compound='center')
    btn_roller_0.bind("<Button-1>", lambda e: click_station_service(4, 3, 0))

    label_station1.grid(row=0, column=5, columnspan=2, sticky='EWNS')  # sticky='EWNS' 無縫填滿

    label_box.grid(row=1, column=5, sticky='EWNS')
    btn_box_1.grid(row=1, column=6, sticky='EWNS')
    btn_box_0.grid(row=1, column=7, sticky='EWNS')

    label_trigger.grid(row=2, column=5, sticky='EWNS')
    btn_trigger_1.grid(row=2, column=6, sticky='EWNS')
    btn_trigger_0.grid(row=2, column=7, sticky='EWNS')

    label_roller.grid(row=3, column=5, sticky='EWNS')
    btn_roller_1.grid(row=3, column=6, sticky='EWNS')
    btn_roller_0.grid(row=3, column=7, sticky='EWNS')

    # ------第 5 站UI架構------------------------------------------------------------------------

    label_station1 = tkinter.Label(text='Station 5', font=myfont_st)
    label_box = tkinter.Label(text='箱件狀態', font=myfont)
    label_trigger = tkinter.Label(text='按鈕觸發', font=myfont)
    label_roller = tkinter.Label(text='滾筒動作', font=myfont)

    btn_box_1 = tkinter.Label(text='有箱', font=myfont, image=img1, compound='center')
    btn_box_0 = tkinter.Label(text='無箱', font=myfont, image=img2, compound='center')
    btn_trigger_1 = tkinter.Label(text='有', font=myfont, image=img1, compound='center')
    btn_trigger_1.bind("<Button-1>", lambda e: click_station_service(5, 2, 1))
    btn_trigger_0 = tkinter.Label(text='無', font=myfont, image=img2, compound='center')
    btn_trigger_0.bind("<Button-1>", lambda e: click_station_service(5, 2, 0))
    btn_roller_1 = tkinter.Label(text='轉動', font=myfont, image=img1, compound='center')
    btn_roller_1.bind("<Button-1>", lambda e: click_station_service(5, 3, 1))
    btn_roller_0 = tkinter.Label(text='停止', font=myfont, image=img2, compound='center')
    btn_roller_0.bind("<Button-1>", lambda e: click_station_service(5, 3, 0))

    label_station1.grid(row=4, column=5, columnspan=2, sticky='EWNS')  # sticky='EWNS' 無縫填滿

    label_box.grid(row=5, column=5, sticky='EWNS')
    btn_box_1.grid(row=5, column=6, sticky='EWNS')
    btn_box_0.grid(row=5, column=7, sticky='EWNS')

    label_trigger.grid(row=6, column=5, sticky='EWNS')
    btn_trigger_1.grid(row=6, column=6, sticky='EWNS')
    btn_trigger_0.grid(row=6, column=7, sticky='EWNS')

    label_roller.grid(row=7, column=5, sticky='EWNS')
    btn_roller_1.grid(row=7, column=6, sticky='EWNS')
    btn_roller_0.grid(row=7, column=7, sticky='EWNS')

    # -----第 6 站UI架構------------------------------------------------------------------------

    label_station1 = tkinter.Label(text='Station 6', font=myfont_st)
    label_box = tkinter.Label(text='箱件狀態', font=myfont)
    label_trigger = tkinter.Label(text='按鈕觸發', font=myfont)
    label_roller = tkinter.Label(text='滾筒動作', font=myfont)

    btn_box_1 = tkinter.Label(text='有箱', font=myfont, image=img1, compound='center')
    btn_box_0 = tkinter.Label(text='無箱', font=myfont, image=img2, compound='center')
    btn_trigger_1 = tkinter.Label(text='有', font=myfont, image=img1, compound='center')
    btn_trigger_1.bind("<Button-1>", lambda e: click_station_service(6, 2, 1))
    btn_trigger_0 = tkinter.Label(text='無', font=myfont, image=img2, compound='center')
    btn_trigger_0.bind("<Button-1>", lambda e: click_station_service(6, 2, 0))
    btn_roller_1 = tkinter.Label(text='轉動', font=myfont, image=img1, compound='center')
    btn_roller_1.bind("<Button-1>", lambda e: click_station_service(6, 3, 1))
    btn_roller_0 = tkinter.Label(text='停止', font=myfont, image=img2, compound='center')
    btn_roller_0.bind("<Button-1>", lambda e: click_station_service(6, 3, 0))

    label_station1.grid(row=8, column=5, columnspan=2, sticky='EWNS')  # sticky='EWNS' 無縫填滿

    label_box.grid(row=9, column=5, sticky='EWNS')
    btn_box_1.grid(row=9, column=6, sticky='EWNS')
    btn_box_0.grid(row=9, column=7, sticky='EWNS')

    label_trigger.grid(row=10, column=5, sticky='EWNS')
    btn_trigger_1.grid(row=10, column=6, sticky='EWNS')
    btn_trigger_0.grid(row=10, column=7, sticky='EWNS')

    label_roller.grid(row=11, column=5, sticky='EWNS')
    btn_roller_1.grid(row=11, column=6, sticky='EWNS')
    btn_roller_0.grid(row=11, column=7, sticky='EWNS')

    win.mainloop()