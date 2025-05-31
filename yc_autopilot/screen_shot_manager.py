import os
from yc_autopilot.config import SCREEN_SHOT_DIR

class ScreenShotManager:
    def get_screen_shot_path_by_image_name(image_name: str) -> str:
        """
        指定された画像名に基づいてスクリーンショットのパスを取得します。

        Args:
            image_name (str): 画像名

        Returns:
            str: スクリーンショットのフルパス
        """
        return os.path.join(SCREEN_SHOT_DIR, image_name)
