import os
from time import sleep


# 点击方法
def click_screen(x, y):
    os.system('adb shell input tap {} {}'.format(x, y))


def repeat(zidong):
    print('开始挑战')
    # 闯关
    click_screen(1781, 895)
    sleep(58)

    # 跳过
    #rint('点击跳过')
    #click_screen(2175, 45)
    #sleep(1)

    # 自动
    #if zidong == 0:
    #    print('点击自动')
    #    click_screen(2117, 39)
    #    zidong = 1

    # 打完
    print('打完了')

    # 跳过
    click_screen(2175, 45)
    sleep(10)

    # 挑战完成
    print('挑战完成\n\n')
    #click_screen(1000, 500)
    #sleep(1)

    # 再次挑战
    print('再次挑战\n\n')
    click_screen(1963, 996)
    sleep(1)
    repeat(zidong)

if __name__ == '__main__':
    zidong = 0
    print('刷金币初始化....')
    click_screen(1645, 820)  # 万象天宫
    sleep(1)
    click_screen(210, 288)   # 冒险玩法
    sleep(1)
    click_screen(1164, 375)  # 挑战
    sleep(2)
    print('堕落的废墟\n')
    click_screen(705, 260)   #堕落的废墟
    sleep(1)
    click_screen(1318, 441)  # 魔女的回忆
    sleep(1)
    click_screen(2010, 294)  # 普通
    sleep(1)
    click_screen(1724, 954)  # 下一步
    print('刷金币重复阶段...')
    repeat(zidong)