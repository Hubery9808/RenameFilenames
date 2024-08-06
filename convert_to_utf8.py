import os
import chardet

def convert_to_utf8(file_path):
    """
    将文件内容从其当前编码转换为 UTF-8 编码。
    
    参数:
    - file_path: 文件路径
    """
    try:
        # 读取文件的二进制内容
        with open(file_path, 'rb') as file:
            raw_data = file.read()

        # 检测文件的原始编码
        result = chardet.detect(raw_data)
        encoding = result['encoding']

        if encoding is None:
            print(f'无法检测文件 {file_path} 的编码。跳过此文件。')
            return

        print(f'检测到文件 {file_path} 的编码为: {encoding}')

        # 解码为 Unicode
        try:
            text = raw_data.decode(encoding)
        except (UnicodeDecodeError, TypeError) as e:
            print(f'解码文件 {file_path} 时出现错误，编码为 {encoding}: {e}。跳过此文件。')
            return

        # 写入新的 UTF-8 编码文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)

        print(f'文件 {file_path} 已转换为 UTF-8 编码。')

    except Exception as e:
        print(f'处理文件 {file_path} 时出现错误: {e}')

def convert_directory_to_utf8(directory):
    """
    遍历目录中的所有文件，并将其编码转换为 UTF-8 编码。
    
    参数:
    - directory: 目录路径
    """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            convert_to_utf8(file_path)

if __name__ == '__main__':
    current_directory = os.getcwd()
    convert_directory_to_utf8(current_directory)
    print('所有文件编码转换为 UTF-8 编码完成。')
