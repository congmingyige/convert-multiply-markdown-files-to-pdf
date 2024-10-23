import os
import re

# 中文数字与阿拉伯数字的映射
chinese_to_arabic = {
    '零': '0', '一': '1', '二': '2', '三': '3', '四': '4',
    '五': '5', '六': '6', '七': '7', '八': '8', '九': '9',
    '十': '10', '百': '100', '千': '1000', '万': '10000'
}

# 将中文数字转换为阿拉伯数字
def convert_chinese_to_arabic(chinese_number):
    total = 0
    current = 0
    for char in chinese_number:
        if char in chinese_to_arabic:
            current += int(chinese_to_arabic[char])
        elif char == '十':
            current = current if current > 0 else 1  # 处理"十"开头的情况
            current *= 10
        elif char in ['百', '千', '万']:
            if char == '百':
                current *= 100
            elif char == '千':
                current *= 1000
            elif char == '万':
                total += current * 10000
                current = 0
    total += current
    return total

def rename_pdfs(folder):
    for filename in os.listdir(folder):
        if filename.endswith('.pdf'):
            match = re.match(r'第([零一二三四五六七八九十]+)章(.+)\.pdf', filename)
            if match:
                chinese_number = match.group(1)
                arabic_number = convert_chinese_to_arabic(chinese_number)
                new_filename = f'第{arabic_number}章{match.group(2)}.pdf'
                os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))
                print(f'Renamed: {filename} to {new_filename}')

folder_path = r'C:/Users/chenguanbin/OneDrive - hust.edu.cn/_工作/八股文/DL500-html-to-microsoft-pdf'  # 替换为你的文件夹路径
rename_pdfs(folder_path)
