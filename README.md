
# 文件重命名脚本

本项目包含了一系列用于处理和重命名当前目录下 `.jpg` 文件的 Python 脚本。每个脚本提供了不同的重命名操作，具体功能如下：

## 脚本列表

### `convert_to_utf8.py`
将当前目录下所有文件识别编码并将它们转换为 UTF-8 编码。

### `front_add_filename.py`
将前目录下所有以 `.jpg` 结尾的文件，文件名称前添加前缀 `xxx`。

### `front_delete_filename.py`
将当前目录下所有以 `.jpg` 结尾的文件，文件名的开头删除两个字符。

### `back_add_filename.py`
将前目录下所有以 `.jpg` 结尾的文件，文件名称后添加后缀 `xxx`。

### `back_delete_filename.py`
将当前目录下所有以 `.jpg` 结尾的文件，文件名的末尾删除两个字符。

### `remove_chars_in_range.py`
处理当前目录下所有 `.jpg` 文件，并删除文件名中第 `x` 到第 `y` 个字符（包括这两个位置的字符）。

### `replace_chars_in_range.py`
将当前目录下所有 .jpg 文件的名称中，从第 3 到第 7 个字符的部分替换为 'xyz'，包含第3和第7个字符。

### `replace_chars_in_directory.py`
将当前目录下所有以 `.jpg` 结尾的文件名中的 `xxx` 替换为 `yyy`。

### `insert_chars_in_position.py`
在当前目录下所有以 `.jpg` 结尾的文件名中，将字符 `abc` 插入到第 `x` 和第 `x+1` 之间的位置。

### `renew_all_filenames.py`
按顺序重命名当前目录下所有 `.jpg` 文件，将它们重命名为 `zzz1.jpg`、`zzz2.jpg`、`zzz3.jpg` 等等，其中 `index` 是文件的编号，从 1 开始。

## 使用说明

1. 将脚本文件放置于需要处理 `.jpg` 文件的目录中。
2. 确保你已经安装了 Python3 环境。
3. 确保需要处理的文件为UTF-8 编码格式，如果不是则用convert_to_utf8.py脚本转换为UTF-8 编码。
4. 运行对应的脚本文件来执行所需的文件重命名操作。

## 免责声明

请在运行这些脚本之前备份你的文件，以免不必要的数据丢失或错误操作。

