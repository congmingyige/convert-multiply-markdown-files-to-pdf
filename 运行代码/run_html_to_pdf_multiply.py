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
                if (filename == 'readme.html'):
                    continue

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
                
                # chrome_options.add_argument('--headless')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument("--disable-extensions")


                driver = webdriver.Chrome(options=chrome_options)
                driver.get(f"file:///{html_path.replace('\\', '/')}")
                driver.maximize_window()
                time.sleep(10)  # 等待页面加载 # 设置大一点，确保页面加载完成
                driver.execute_script(f'document.title="{pdf_name}"; window.print();')
                time.sleep(10)  # 等待打印 # 设置大一点，确保打印完成
                driver.refresh()
                driver.close()



print_html_files(source_folder, output_folder)
