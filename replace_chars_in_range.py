import os

def replace_chars_in_range(filename, x, y, replacement):
    """
    替换文件名中指定范围内的字符为给定的替换字符串。
    
    参数:
    - filename: 原文件名（包括扩展名）
    - x: 替换开始位置（1-based index），例如 1 表示文件名的第一个字符
    - y: 替换结束位置（1-based index），例如 5 表示文件名的第5个字符
    - replacement: 替换的字符串，替换范围内的字符将被这个字符串取代
    
    返回:
    - 返回替换后的新文件名（包括扩展名）
    """
    # 分离文件名的主体部分和扩展名
    base, ext = os.path.splitext(filename)
    
    # 检查索引范围的有效性
    if x < 1 or y < x or x > len(base):
        raise ValueError(f"Invalid range: x={x}, y={y} for filename: {filename}")

    # 修正 y 的值，确保不超过文件名的实际长度
    y = min(y, len(base))

    # 生成新的文件名
    # base[:x-1]：保留原文件名中替换开始位置之前的部分
    # replacement：插入替换的字符串
    # base[y:]：保留原文件名中替换结束位置之后的部分
    new_base = base[:x-1] + replacement + base[y:]
    
    # 组合新的文件名（包括扩展名）
    new_filename = f'{new_base}{ext}'
    return new_filename

def rename_files_in_directory(directory, x, y, replacement):
    """
    遍历目录中的所有 .jpg 文件，并将文件名中指定范围内的字符替换为给定字符串。
    
    参数:
    - directory: 目录路径，包含要重命名的文件
    - x: 替换开始位置（1-based index）
    - y: 替换结束位置（1-based index）
    - replacement: 替换的字符串
    
    过程:
    - 遍历目录中的所有文件
    - 仅处理扩展名为 .jpg 的文件
    - 调用 replace_chars_in_range 函数进行重命名
    - 确保新文件名不冲突（检查是否已存在）
    - 重命名文件，并处理可能的异常
    """
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg'):
            try:
                # 获取新文件名
                new_filename = replace_chars_in_range(filename, x, y, replacement)
                
                # 仅当新文件名与原文件名不同才进行重命名
                if new_filename != filename:
                    old_file = os.path.join(directory, filename)
                    new_file = os.path.join(directory, new_filename)
                    
                    # 检查新文件名是否已存在
                    if not os.path.exists(new_file):
                        os.rename(old_file, new_file)
                        print(f'文件重命名成功: {old_file} -> {new_file}')
                    else:
                        print(f'文件已存在: {new_file}')
            except ValueError as e:
                # 捕捉并报告文件名范围无效的错误
                print(f'处理文件 {filename} 时发生错误: {e}')
            except OSError as e:
                # 捕捉并报告操作系统错误，例如权限问题
                print(f'重命名文件 {filename} 时发生错误: {e}')
            except Exception as e:
                # 捕捉并报告其他未知错误
                print(f'处理文件 {filename} 时发生意外错误: {e}')

if __name__ == '__main__':
    # 设置当前目录路径
    current_directory = os.getcwd()
    
    # 设置要替换的字符范围和替换字符串
    start_position = 3  # 替换开始位置（1-based index），示例是3，可自行修改
    end_position = 7    # 替换结束位置（1-based index），示例是7，可自行修改
    replacement_string = 'XYZ'  # 替换的字符串，示例是xyz，可自行修改
    
    # 调用重命名函数进行处理
    rename_files_in_directory(current_directory, start_position, end_position, replacement_string)

    # 完成后打印提示
    print('重命名操作完成。')
