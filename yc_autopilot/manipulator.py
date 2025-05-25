import pyautogui
from pyautogui import Point
import os

from yc_autopilot.config import SCREEN_SHOT_DIR

class Manipulator:
    def mouse_click_by_image(image_name: str) -> bool:
        """
        指定した名前の画像をscreen_shotディレクトリから探し、
        画像があったら、その画像に相当する位置をクリックし、Trueを返す。
        画像がなかったら、ないことをコンソールに出力し、Falseを返す。
        """
        image_path = os.path.join(SCREEN_SHOT_DIR, image_name)
        location = Manipulator.get_image_location_on_window(image_name)
        if location:
            pyautogui.click(location)
            return True
        else:
            return False

        
    def get_image_location_on_window(image_name: str) -> Point | None:
        image_path = os.path.join(SCREEN_SHOT_DIR, image_name)
        try:
            location = pyautogui.locateCenterOnScreen(image_path)
            return location
        except Exception as e:
            print(f"Error while locating image {image_name}: {e}")
            return None


    def enter_key_board(key_name: str, x: int, y: int):
        """
        x, yの位置にマウスポインターを移動する
        移動した場所でkey_nameに相当するキーボード操作を行う
        """
        pyautogui.moveTo(x, y)
        pyautogui.typewrite(key_name)
