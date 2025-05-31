import time
import pyautogui
from yc_autopilot.screen_shot_manager import ScreenShotManager
from datetime import datetime
import os

class AutoSummon:
    def auto_summon(self):

        ss_path = ScreenShotManager.get_screen_shot_path_by_image_name("1001_actived_summon_button.PNG")
        ce = os.path.exists(ss_path)
        print(ss_path)
        print(ce)

        summon_button_location = pyautogui.locateOnScreen(
                ss_path
            )
        if summon_button_location:
            print("{} ボタンがあるので自動召喚処理開始".format(datetime.now()))
            summon_button_center = pyautogui.center(summon_button_location)
        else:
                print("{} ボタン非存在 or 非活性により実行せずに停止".format(datetime.now()))
        
        while True:
            print("{} 召喚を実行".format(datetime.now()))
            pyautogui.click(summon_button_center)
            
            time.sleep(10)

if __name__ == "__main__":
    auto_summon = AutoSummon()
    auto_summon.auto_summon()
