# 这是我的解决方法，详见，https://www.cnblogs.com/cmyg/p/18492942

DeepLearning-500-questions_pdf-html版本_20241023 
通过百度网盘分享的文件：DeepLearning-500-questions_pdf-html...
链接：https://pan.baidu.com/s/1D8pHj62pOyKYUjjM4KJN9w?pwd=to4e
提取码：to4e

几乎完美解决问题，除了有些图片放得比较大，图片质量低的时候看起来效果不太好之外，其它，公式、格式、粗体、换行，基本没什么问题
a. VScode插件Markdown All In One markdown转html，Ctrl+Shift+P，>Markdown All in One: 批量打印文档为HTML（选择文件夹）。批处理，支持多级文件夹的多个文件处理
　　a.1 用代码修改一下格式

````
import os

def replace_strings_in_file(file_path, replacements):
    """替换文件中指定字符串并记录替换的位置"""
    modified = False
    occurrences = []

    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 遍历每行进行替换
    new_lines = []
    for line_num, line in enumerate(lines, 1):
        new_line = line
        for search_string, replace_string in replacements.items():
            index = new_line.find(search_string)
            while index != -1:
                # 记录替换位置
                occurrences.append((line_num, index, search_string, replace_string))
                # 进行字符串替换
                new_line = new_line[:index] + replace_string + new_line[index + len(search_string):]
                # 查找后续出现的位置
                index = new_line.find(search_string, index + len(replace_string))
        # 保存修改后的行
        if new_line != line:
            modified = True
        new_lines.append(new_line)

    # 如果文件有修改，则重写文件
    if modified:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(new_lines)

    return occurrences

def replace_strings_in_directory(directory, replacements):
    """递归遍历文件夹，查找和替换所有 Markdown 文件中的指定字符串"""
    all_occurrences = {}

    # 遍历文件夹及子文件夹
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                occurrences = replace_strings_in_file(file_path, replacements)
                if occurrences:
                    all_occurrences[file_path] = occurrences

    return all_occurrences

def print_replacement_occurrences(occurrences):
    """输出所有修改的位置"""
    for file_path, positions in occurrences.items():
        print(f"\nFile: {file_path}")
        for line_num, col_num, old_string, new_string in positions:
            print(f"  Line {line_num}, Column {col_num}: '{old_string}' -> '{new_string}'")

if __name__ == "__main__":
    # 输入要搜索的文件夹路径
    directory = input("请输入要搜索的文件夹路径: ")

    # 替换规则
    replacements = {
        r'\begin{eqnarray}': r'\begin{equation}\begin{aligned}',
        r'\end{eqnarray}': r'\end{aligned}\end{equation}',
        '`$': '$',
        '$`': '$'
    }

    # 执行替换并记录修改位置
    occurrences = replace_strings_in_directory(directory, replacements)

    # 输出所有替换的地方
    if occurrences:
        print_replacement_occurrences(occurrences)
    else:
        print("No replacements made.")
````


b. 使用浏览器的Microsoft print to pdf，用代码，批处理，支持多级文件夹的多个文件处理
````
import os
import json
import time
from selenium import webdriver

source_folder = r'C:/Users/chenguanbin/OneDrive - hust.edu.cn/_工作/八股文/DL500-html'  # 修改为你的HTML文件路径
output_folder = r'C:/Users/chenguanbin/OneDrive - hust.edu.cn/_工作/八股文/DL500-html-to-microsoft-pdf'    # 修改为你的输出PDF路径

chrome_options = webdriver.ChromeOptions()

settings = {
    "recentDestinations": [{
        "id": "Save as PDF",
        "origin": "local",
        "account": ""
    }],
    "selectedDestinationId": "Save as PDF",
    "version": 2,
    "isHeaderFooterEnabled": False,
    "isLandscapeEnabled": True,
    "isCssBackgroundEnabled": True,
    "mediaSize": {
        "height_microns": 297000,
        "name": "ISO_A4",
        "width_microns": 210000,
        "custom_display_name": "A4 210 x 297 mm"
    },
}
chrome_options.add_argument('--enable-print-browser')
chrome_options.add_argument('--kiosk-printing')

def print_html_files(source_folder, output_folder):
    for dirpath, _, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.endswith('.html'):
                html_path = os.path.join(dirpath, filename)
                # 生成输出PDF路径，保持文件夹结构
                relative_path = os.path.relpath(dirpath, source_folder)
                pdf_output_dir = os.path.join(output_folder, relative_path)
                os.makedirs(pdf_output_dir, exist_ok=True)
                pdf_name = f"{os.path.splitext(filename)[0]}.pdf"
                pdf_output_path = os.path.join(pdf_output_dir, pdf_name)

                prefs = {
                    'printing.print_preview_sticky_settings.appState': json.dumps(settings),
                    'savefile.default_directory': pdf_output_dir  # 修改为你的输出路径
                }
                chrome_options.add_experimental_option('prefs', prefs)

                driver = webdriver.Chrome(options=chrome_options)
                driver.get(f"file:///{html_path.replace('\\', '/')}")
                driver.maximize_window()
                driver.execute_script(f'document.title="{pdf_name}"; window.print();')
                # time.sleep(2)  # 等待打印
                driver.close()



print_html_files(source_folder, output_folder)
````
