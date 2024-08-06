import os

# 获取当前工作目录的路径
current_directory = os.getcwd()

# 列出当前目录下所有以 .jpg 结尾的文件
# 使用列表推导式过滤出文件列表，并将所有文件名转为小写以进行不区分大小写的匹配
files = [f for f in os.listdir(current_directory) if f.lower().endswith('.jpg')]

# 遍历所有找到的 .jpg 文件，并按顺序进行重命名
for index, filename in enumerate(files, start=1):
    # 使用枚举函数提供的索引值（从1开始）构造新的文件名
    # 新文件名格式为 'zzz' 加上当前文件的顺序编号，再加上 '.jpg' 扩展名
    new_filename = f'zzz{index}.jpg'
    
    # 构造旧文件的完整路径
    old_file = os.path.join(current_directory, filename)
    # 构造新文件的完整路径
    new_file = os.path.join(current_directory, new_filename)
    
    # 使用 os.rename() 函数将文件重命名
    os.rename(old_file, new_file)
    
    # 打印重命名操作的结果
    print(f'Renamed: {old_file} -> {new_file}')

# 打印完成重命名操作的消息
print('Renaming completed.')
