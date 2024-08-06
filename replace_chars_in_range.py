import os

def replace_chars_in_range(filename, x, y, replacement):
    """
    替换文件名中指定范围内的字符为给定的替换字符串。
    
    参数:
    - filename: 原文件名
    - x: 替换开始位置（1-based index）
    - y: 替换结束位置（1-based index）
    - replacement: 替换的字符串
    """
    # 分离文件名和扩展名
    base, ext = os.path.splitext(filename)
    
    # 检查索引范围的有效性
    if x < 1 or y < x or x > len(base) or y >= len(base):
        raise ValueError(f"Invalid range: x={x}, y={y} for filename: {filename}")
    
    # 替换指定范围的字符
    new_base = base[:x-1] + replacement + base[y+1:]
    
    # 构造新的文件名
    new_filename = f'{new_base}{ext}'
    return new_filename

def rename_files_in_directory(directory, x, y, replacement):
    """
    遍历目录中的所有 .jpg 文件，并将文件名中指定范围内的字符替换为给定字符串。
    
    参数:
    - directory: 目录路径
    - x: 替换开始位置（1-based index）
    - y: 替换结束位置（1-based index）
    - replacement: 替换的字符串
    """
    # 遍历目录下的所有文件
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg'):
            new_filename = replace_chars_in_range(filename, x, y, replacement)
            if new_filename != filename:  # 确保文件名已更改
                old_file = os.path.join(directory, filename)
                new_file = os.path.join(directory, new_filename)
                try:
                    if not os.path.exists(new_file):  # 检查新文件名是否已存在
                        os.rename(old_file, new_file)
                        print(f'Renamed: {old_file} -> {new_file}')
                    else:
                        print(f'File already exists: {new_file}')
                except OSError as e:
                    print(f'Error renaming file {filename}: {e}')
                except Exception as e:
                    print(f'Unexpected error for file {filename}: {e}')

if __name__ == '__main__':
    current_directory = os.getcwd()
    
    try:
        x = int(input('Enter the start position (1-based index) for replacement: '))
        y = int(input('Enter the end position (1-based index) for replacement: '))
        replacement = 'abc'  # 要替换的字符串
        rename_files_in_directory(current_directory, x, y, replacement)
    except ValueError:
        print('Invalid input. Please enter valid numbers.')
    except Exception as e:
        print(f'Unexpected error: {e}')

    print('Renaming completed.')
