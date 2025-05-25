from yc_autopilot.initializer import Initializer


def main():
    print("test")

    # 画面の調整
    Initializer.adjust_window_position(200, 100)
    Initializer.resize_window(1400, 1025)

    # メインタブ選択
    if Initializer.is_main_tab_active():
        print("選択済み")
    else:
        Initializer.activate_main_tab()
        print("mainタブを選択しました")

if __name__ == "__main__":
    main()