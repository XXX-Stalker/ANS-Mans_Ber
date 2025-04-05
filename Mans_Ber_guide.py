def RUN():
    print("插件 Mans_Ber 正在启动...")
    print("正在检查插件的引导文件...")
    
    with open("plugins/plugins_list.txt", "r", encoding="utf-8") as f:
        plu_list = f.readlines()
        if len(plu_list) == "Mans_Ber":
            if "Mans_Ber" in plu_list:
                print("插件 Mans_Ber 的插件表存在")
            else:
                print("插件 Mans_Ber 的插件表不存在")
                choose = input("是否创建插件 Mans_Ber 的插件表?(y/n)")
                if choose in ["y", "Y"]:
                    with open("plugins/plugins_list.txt", "a", encoding="utf-8") as f:
                        f.write("Mans_Ber\n")
                    print("插件 Mans_Ber 的插件表已成功创建")
                else:
                    print("插件 Mans_Ber 的插件表已取消创建")
    print("尝试打开插件的引导文件...")
    try:
        import importlib
        module = importlib.import_module("plugins.Mans_Ber.Mans_Ber_main")
        Mans_Ber_run = getattr(module, "Mans_Ber_run")
        Mans_Ber_run()
    except Exception as e:
        print(f"插件启动失败: {str(e)}")

if __name__ == "__main__":
    RUN()