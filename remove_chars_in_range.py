import os

def remove_chars_in_range(filename, x, y):
    # 去掉扩展名
    base, ext = os.path.splitext(filename)
    # 检查索引范围的有效性
    if x < 1 or y < x or x > len(base) or y >= len(base):
        raise ValueError(f"Invalid range: x={x}, y={y} for filename: {filename}")
    # 删除指定范围的字符
    new_base = base[:x-1] + base[y+1:]
    # 构造新的文件名
    new_filename = f'{new_base}{ext}'
    return new_filename

# 获取当前目录
current_directory = os.getcwd()

# 定义要删除字符的范围，从x到y（包含x和y）
x = 2  # 从第x个字符开始删除（1-based index）
y = 4  # 到第y个字符结束删除（1-based index）

# 遍历当前目录下的所有文件
for filename in os.listdir(current_directory):
    # 只处理以 .jpg 结尾的文件
    if filename.lower().endswith('.jpg'):
        try:
            new_filename = remove_chars_in_range(filename, x, y)
            # 获取旧文件路径和新文件路径
            old_file = os.path.join(current_directory, filename)
            new_file = os.path.join(current_directory, new_filename)
            # 重命名文件
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} -> {new_file}')
        except ValueError as e:
            print(f'Error processing file {filename}: {e}')

print('Renaming completed.')
