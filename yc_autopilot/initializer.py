import pyautogui
import os

MAIN_TAB_SELECTED_IMAGE = os.path.join(os.path.dirname(__file__), "screen_shot", "0001_main_tab_selected.PNG")
MAIN_TAB_NOT_SELECTED_IMAGE = os.path.join(os.path.dirname(__file__), "screen_shot", "0002_main_tab_not_selected.PNG")


class Initializer:
    def is_main_tab_active():
        try:
            print(MAIN_TAB_SELECTED_IMAGE)
            print(os.path.exists(MAIN_TAB_SELECTED_IMAGE))
            main_tab_location = pyautogui.locateOnScreen(MAIN_TAB_SELECTED_IMAGE)
            print("maintab location: {}".format(main_tab_location))
            if main_tab_location:
                return True
            else:
                return False
        except pyautogui.ImageNotFoundException as e:
            print("メインタブ画像を検出できませんでした")
            print(e)
            return False

    def activate_main_tab():
        try:
            main_tab_location = pyautogui.locateOnScreen(MAIN_TAB_NOT_SELECTED_IMAGE)
            if main_tab_location:
                main_tab_x, main_tab_y, main_tab_width, main_tab_height = main_tab_location
                main_tab_center_x = main_tab_x + main_tab_width // 2
                main_tab_center_y = main_tab_y + main_tab_height // 2
                pyautogui.click(main_tab_center_x, main_tab_center_y)
        except pyautogui.ImageNotFoundException:
            print("「メイン」タブの画像が見つかりませんでした。")

    def adjust_window_position(x, y):
        try:
            window = pyautogui.getWindowsWithTitle("YourChronicle")[0]  # ウィンドウタイトルで検索
            window.moveTo(x, y)
            print(f"ウィンドウの位置を X={x}, Y={y} に調整しました。")
        except IndexError:
            print("「Your Chronicle」というタイトルのウィンドウが見つかりませんでした。")

    def resize_window(width, height):
        try:
            window = pyautogui.getWindowsWithTitle("YourChronicle")[0]  # ウィンドウタイトルで検索
            window.resizeTo(width, height)
            print(f"ウィンドウのサイズを 幅={width}, 高さ={height} に調整しました。")
        except IndexError:
            print("「Your Chronicle」というタイトルのウィンドウが見つかりませんでした。")
