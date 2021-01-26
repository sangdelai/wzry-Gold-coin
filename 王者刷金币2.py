import os
from time import sleep


# 点击方法
def click_screen(x, y):
    os.system('adb shell input tap {} {}'.format(x, y))


def repeat(zidong):
    print('开始挑战')
    # 闯关
    click_screen(1781, 895)
    sleep(10)

    # 跳过
    print('点击跳过')
    click_screen(2175, 45)
    sleep(1)

    # 自动
    if zidong == 0:
        print('点击自动')
        click_screen(2117, 39)
        zidong = 1

    # 打完
    sleep(60)
    print('打完了')

    # 跳过
    click_screen(2175, 45)
    sleep(10)

    # 挑战完成
    print('挑战完成\n\n')
    click_screen(1000, 500)
    sleep(1)

    # 再次挑战
    print('再次挑战\n\n')
    click_screen(2001, 1011)
    sleep(1)
    repeat(zidong)

if __name__ == '__main__':
    zidong = 0
    print('刷金币初始化....')
    click_screen(1755, 793)  # 万象天宫
    sleep(1)
    click_screen(211, 275)   # 冒险玩法
    sleep(1)
    click_screen(1231, 557)  # 挑战
    sleep(2)
    print('通天塔\n')
    click_screen(1393, 475)  # 通天塔
    sleep(1)
    click_screen(1677, 675)  # 大师级别
    sleep(1)
    click_screen(1791, 939)  # 下一步
    print('刷金币重复阶段...')
    repeat(zidong)

    #3144