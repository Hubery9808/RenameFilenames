import os

def insert_chars_in_position(filename, x, insertion):
    # 去掉扩展名
    base, ext = os.path.splitext(filename)
    
    # 检查索引的有效性
    if x < 1 or x > len(base):
        raise ValueError(f"Invalid position: x={x} for filename: {filename}")
    
    # 插入指定内容
    new_base = base[:x] + insertion + base[x:]
    # 构造新的文件名
    new_filename = f'{new_base}{ext}'
    return new_filename

# 获取当前目录
current_directory = os.getcwd()

# 定义要插入字符的位置和插入内容
x = 2  # 从第x个字符之后的位置插入（0-based index），示例2可自行修改
insertion = 'abc'  # 插入的字符串，示例abc可自行修改

# 遍历当前目录下的所有文件
for filename in os.listdir(current_directory):
    # 只处理以 .jpg 结尾的文件
    if filename.lower().endswith('.jpg'):
        try:
            new_filename = insert_chars_in_position(filename, x, insertion)
            # 获取旧文件路径和新文件路径
            old_file = os.path.join(current_directory, filename)
            new_file = os.path.join(current_directory, new_filename)
            # 重命名文件
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} -> {new_file}')
        except ValueError as e:
            print(f'Error processing file {filename}: {e}')

print('Renaming completed.')
