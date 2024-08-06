import os

# 获取当前目录
current_directory = os.getcwd()

# 遍历当前目录下的所有文件
for filename in os.listdir(current_directory):
    # 只处理以 .jpg 结尾的文件
    if filename.lower().endswith('.jpg'):
        # 构造新文件名，在旧文件基础上前面添加“xxx”（xxx可自定义，直接修改代码）
        base, ext = os.path.splitext(filename)
        new_filename = f'{base}xxx{ext}'
        # 获取旧文件路径和新文件路径
        old_file = os.path.join(current_directory, filename)
        new_file = os.path.join(current_directory, new_filename)
        # 重命名文件
        os.rename(old_file, new_file)
        print(f'Renamed: {old_file} -> {new_file}')

print('Renaming completed.')
