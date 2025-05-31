from yc_autopilot.initializer import Initializer

def adjust_window():
    Initializer.adjust_window_position(200, 100)
    Initializer.resize_window(1400, 1025)

def main():
    print("test")

    # 画面の調整
    Initializer.adjust_window_position(200, 100)
    Initializer.resize_window(1400, 1025)

    # メインタブ選択
    # if Initializer.is_main_tab_active():
    #     print("選択済み")
    # else:
    #     Initializer.activate_main_tab()
    #     print("mainタブを選択しました")

def execute_auto_summon():
    auto_summon = AutoSummon()
    auto_summon.auto_summon()

from yc_autopilot.auto_summon import AutoSummon

if __name__ == "__main__":
    # 画面の調整は必須
    adjust_window()

    execute_auto_summon()
