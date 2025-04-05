def c_enc_main():
    while True:
        choice = input(":")

        if choice == "1":
            folder_to_encrypt = input("请输入将要加密的文件夹路径: ")
            file_path = input("程序文件生成路径(文件夹路径!): ")
            file_name = input("程序文件名称(不需要后缀!): ")
            file_path_2 = f"{file_path}\{file_name}.py"
            with open(r"c_enc_RSA\c_enc_folder_1.py", "r", encoding="utf-8") as f:
                template = f.read()
            with open(file_path_2, "w", encoding="utf-8") as f:
                f.write(f'folder_to_encrypt = r"{folder_to_encrypt}"\n')
                f.write(template)

        elif choice == "2":
            target_path = input("请输入将要加密的文件路径: ")
            file_path = input("程序文件生成路径(文件夹路径!): ")
            file_name = input("程序文件名称(不需要后缀!): ")
            file_path_2 = f"{file_path}/{file_name}.py"
            with open(r"c_enc_RSA\c_enc_file_1.py", "r", encoding="utf-8") as f:
                c_enc_decrypt = f.read()
            with open(file_path_2, "w", encoding="utf-8") as f:
                f.write(f'target_path = r"{target_path}"\n')
                f.write(c_enc_decrypt)
            print(f"加密程序文件已保存到 {file_path_2}")

        elif choice == "3":
            target_path = input("请输入将要解密的文件路径: ")
            private_key_path = input("请输入私钥路径: ")
            file_path = input("程序文件生成路径(文件夹路径!): ")
            file_name = input("程序文件名称(不需要后缀!): ")
            file_path_2 = f"{file_path}/{file_name}.py"
            with open(r"c_enc_RSA\c_enc_decrypt.py", "r", encoding="utf-8") as f:
                c_enc_decrypt = f.read()
            with open(file_path_2, "w", encoding="utf-8") as f:
                f.write(f'target_path = r"{target_path}"\nprivate_key_path = r"{private_key_path}"\n')
                f.write(c_enc_decrypt)
            print(f"解密程序文件已保存到 {file_path_2}")

        elif choice == "4":
            break

if __name__ == "__main__":
    print(f"{'-' * 30}")
    print("       生成加密文件工具")
    print(f"{'-' * 30}")
    print("1. 生成加密文件夹程序 - 不可解密")
    print("2. 生成加密文件程序 - 可解密")
    print("3. 生成解密程序 - 仅解密单个文件")
    print("4. 退出")
    print(f"{'=' * 30}")
    c_enc_main()
    print("特殊退出 Error Code[001]")