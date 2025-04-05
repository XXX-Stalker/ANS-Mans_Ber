import ctypes
import os
import sys

def change_wallpaper(image_path):
    if not os.path.exists(image_path):
        print("指定的图片路径不存在！")
        return
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)  # 添加参数 3
    print("壁纸已成功更改！")

def change_wallpaper(wallpaper_jpg):
    current_folder = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_folder, rf"{wallpaper_jpg}")
    change_wallpaper(image_path)

if  __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print("需要被调用！")
    sys.exit()