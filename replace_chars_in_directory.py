import os

def rename_files_in_directory(directory, old_str, new_str):
    """遍历目录并重命名文件"""
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg'):
            new_filename = filename.replace(old_str, new_str)
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
    
    old_str = 'xxx'  # 要替换的字符串，示例“xxx”可自行修改
    new_str = 'yyy'  # 新的字符串，示例“yyy”可自行修改
    
    rename_files_in_directory(current_directory, old_str, new_str)
    print('Renaming completed.')
