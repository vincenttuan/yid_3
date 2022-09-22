# YID 控制功能

# 模式切換 功能邏輯區------------------------------------------------
def mod_switch(btn_mode_str):
    print("mod_switch")
    if btn_mode_str.get() == '自動':
        btn_mode_str.set('手動')
    else:
        btn_mode_str.set('自動')
# 連線狀態 功能邏輯區------------------------------------------------
def link_status(btn_linkage_str):
    print("linkage status")
    if btn_linkage_str.get() == '離線':
        btn_linkage_str.set('連線')
    else:
        btn_linkage_str.set('離線')
# 倉庫流道 功能邏輯區------------------------------------------------
def warehouse_status(warehouse_status):
    print("warehouse status")
    if warehouse_status.get() == '異常':
        warehouse_status.set('正常')
    else:
        warehouse_status.set('異常')

# 第 1 站 功能邏輯區------------------------------------------------
def st1_box_status_1():
    print("Box exists")

def st1_box_status_0():
    print("No Box")

def st1_trigger_status_1():
    print("Button Light ON")

def st1_trigger_status_0():
    print("Button Light OFF")

def st1_roller_move_1():
    print("Roller Start Running")

def st1_roller_move_0():
    print("Roller Stop Running")

# 第 2 站 功能邏輯區------------------------------------------------
def st2_box_status():
    print("st2_box_status")

def st2_trigger_status():
    print("st2_trigger_status")

def st2_roller_movement():
    print("st2_roller_movement")

# 第 3 站 功能邏輯區------------------------------------------------
def st3_box_status():
    print("st3_box_status")

def st3_trigger_status():
    print("st3_trigger_status")

def st3_roller_movement():
    print("st3_roller_movement")

# 第 4 站 功能邏輯區------------------------------------------------
def st4_box_status():
    print("st4_box_status")

def st4_trigger_status():
    print("st4_trigger_status")

def st4_roller_movement():
    print("st4_roller_movement")

# 第 5 站 功能邏輯區------------------------------------------------
def st5_box_status():
    print("st5_box_status")

def st5_trigger_status():
    print("st5_trigger_status")

def st5_roller_movement():
    print("st5_roller_movement")

# 第 6 站 功能邏輯區------------------------------------------------
def st6_box_status():
    print("st6_box_status")

def st6_trigger_status():
    print("st6_trigger_status")

def st1_roller_movement():
    print("st6_roller_movement")