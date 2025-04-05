import os

# 所有初始化
Version_file_name = os.path.basename(__file__)
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
Mans_Ber_Version_file = current_dir + "\Mans_Ber_Version.txt"
with open(Mans_Ber_Version_file, "r", encoding="utf-8") as f:
    VERSION = f.read()

TITLE = f"""
___  ___             _        ______
|  \/  |            | |       | ___ \ 
| .  . | __ _ _ __ / __)______| |_/ / ___ _ __ 
| |\/| |/ _` | '_ \\__ \______| ___ \/ _ \ '__|
| |  | | (_| | | | (   /      | |_/ /  __/ |   
\_|  |_/\__,_|_| |_||_|       \____/ \___|_|   
输入 'help' 查看帮助信息
{VERSION}"""
HELP = f"""
           _   _ _____ _     ____  
          | | | | ____| |   |  _ \ 
          | |_| |  _| | |   | |_) |
          |  _  | |___| |___|  __/ 
          |_| |_|_____|_____|_|    
--------------------------------------------
帮助:
    h, help                          显示帮助信息
    v, version                       显示版本信息
    exit, quit                       退出程序
    cls, clear                       清屏
代码:
    c -enc                           生成加密程序
--------------------------------------------
"""

def Mans_Ber_run():
    print(f"{TITLE}\n{'=' * 46}")
    print("当前工作目录:", current_dir, "\n")
    while True:
        arg = input("M$-Ber <<")
        if arg in ['help']:
            print(HELP)
        elif arg in ['exit', 'quit']:
            break
        elif arg in ['cls', 'clear']:
            os.system("cls" if os.name == "nt" else "clear")
        elif arg in ['v', 'version']:
            print(VERSION)
        elif arg in ['c -enc']:
            from Code.c_enc import c_enc_main
            c_enc_main()

if __name__ == "__main__":
    print(f"{'-' * 48}\n\t\tANSportion 插件\n{'-' * 48}")