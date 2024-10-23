import os

def find_string_in_file(file_path, search_string):
    """查找指定文件中某个字符串出现的位置和次数"""
    occurrences = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line_num, line in enumerate(lines, 1):
            # 查找当前行中字符串出现的位置
            index = line.find(search_string)
            while index != -1:
                occurrences.append((line_num, index))
                # 查找后续出现的位置
                index = line.find(search_string, index + 1)
    return occurrences

def find_string_in_directory(directory, search_string):
    """递归遍历文件夹，查找所有 Markdown 文件中指定字符串出现的位置和次数"""
    string_occurrences = {}
    
    # 遍历文件夹及子文件夹
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                occurrences = find_string_in_file(file_path, search_string)
                if occurrences:
                    string_occurrences[file_path] = occurrences
    
    return string_occurrences

def print_string_occurrences(occurrences, search_string):
    """输出指定字符串出现的位置和次数"""
    for file_path, positions in occurrences.items():
        print(f"\nFile: {file_path}")
        print(f"'{search_string}' found {len(positions)} time(s):")
        for line_num, col_num in positions:
            print(f"  Line {line_num}, Column {col_num}")

if __name__ == "__main__":
    directory = input("请输入要搜索的文件夹路径: ")
    search_string = input("请输入要查找的字符串: ")
    
    occurrences = find_string_in_directory(directory, search_string)
    if occurrences:
        print_string_occurrences(occurrences, search_string)
    else:
        print(f"No occurrences of '{search_string}' found.")
