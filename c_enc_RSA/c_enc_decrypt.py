import os
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def decrypt_file(encrypted_path, private_key_path):
    try:
        with open(private_key_path, 'rb') as f:
            private_key = RSA.import_key(f.read())
        cipher = PKCS1_OAEP.new(private_key)
        max_block_size = private_key.size_in_bytes()
        with open(encrypted_path, 'rb') as f:
            encrypted_data = f.read()
        decrypted_chunks = []
        for i in range(0, len(encrypted_data), max_block_size):
            chunk = encrypted_data[i:i + max_block_size]
            decrypted_chunk = cipher.decrypt(chunk)
            decrypted_chunks.append(decrypted_chunk)
        original_path = os.path.splitext(encrypted_path)[0]
        with open(original_path, 'wb') as f:
            f.write(b''.join(decrypted_chunks))
        os.remove(encrypted_path)
        print(f"文件 '{encrypted_path}' 已解密为 '{original_path}'")
    except Exception as e:
        print(f"解密失败: {e}")

def decrypt_folder(folder_path, private_key_path=None):
    if private_key_path is None:
        private_key_path = os.path.join(folder_path, "private_key.pem")
    if not os.path.exists(private_key_path):
        print(f"私钥文件不存在: {private_key_path}")
        return
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file == "private_key.pem":
                continue  # 跳过私钥文件
            file_path = os.path.join(root, file)
            if len(file.split('.')) > 1:  # 检查是否有随机后缀
                decrypt_file(file_path, private_key_path)

def decrypt_target(target_path, private_key_path=None):
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{'-' * 50}\n\t\t文件/文件夹解密工具\n{'-' * 50}")
    if not os.path.exists(target_path):
        print(f"路径不存在: {target_path}")
        sys.exit(1)
    if os.path.isfile(target_path):
        if private_key_path is None:
            private_key_path = os.path.join(os.path.dirname(target_path), "private_key.pem")
        decrypt_file(target_path, private_key_path)
    elif os.path.isdir(target_path):
        decrypt_folder(target_path, private_key_path)
    else:
        print("无效的路径类型！")
        sys.exit(1)
    print(f"{'-' * 50}\n\t\t解密完成！\n{'-' * 50}")

if __name__ == "__main__":
    target_path = target_path if 'target_path' in globals() else ""
    private_key_path = private_key_path if 'private_key_path' in globals() else None
    if not target_path:
        print("错误: 未指定目标路径!")
        sys.exit(1)
    decrypt_target(target_path, private_key_path)
