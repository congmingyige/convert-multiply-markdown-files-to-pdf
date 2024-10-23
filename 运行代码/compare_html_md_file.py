import os

def get_corresponding_files(folder_a, folder_b):
    correspondences = {}

    # 获取文件夹A的文件
    for root, _, files in os.walk(folder_a):
        for file in files:
            if file.endswith('.html'):
                relative_path = os.path.relpath(root, folder_a)
                correspondences[os.path.join(relative_path, file[:-5])] = 'html'

    # 获取文件夹B的文件
    for root, _, files in os.walk(folder_b):
        for file in files:
            if file.endswith('.pdf'):
                relative_path = os.path.relpath(root, folder_b)
                correspondences[os.path.join(relative_path, file[:-4])] = 'pdf'

    return correspondences

def find_missing_pdfs(folder_a, folder_b):
    correspondences = get_corresponding_files(folder_a, folder_b)

    # 找出缺失的pdf文件
    missing_pdfs = [key + '.pdf' for key in correspondences.keys() if correspondences[key] == 'html' and key + '.pdf' not in correspondences]

    return missing_pdfs

folder_a = 'C:/Users/chenguanbin/OneDrive - hust.edu.cn/_工作/八股文/DL500-html'  # 替换为A文件夹路径
folder_b = 'C:/Users/chenguanbin/OneDrive - hust.edu.cn/_工作/八股文/DL500-html-to-microsoft-pdf'    # 替换为B文件夹路径
missing_pdf_files = find_missing_pdfs(folder_a, folder_b)

# print("Missing PDF files in folder B:", missing_pdf_files)
print("Missing PDF files in folder B:")
for data in missing_pdf_files:
    print(data)

# 'ch01_数学基础\\第一章_数学基础.pdf', 'ch06_循环神经网络(RNN)\\第六章_循环神经网络(RNN).pdf'