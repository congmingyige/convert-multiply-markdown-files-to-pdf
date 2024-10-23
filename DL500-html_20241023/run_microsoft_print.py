import subprocess
import sys
import os
import win32api
import win32print
# 模块各取所需

def start_printer(cprinter,pdf):
    # """
    # # 调用本地打印机，打印PDF文件，要求：Python3.5+，仅支持win32平台，只支持PDF文件的打印
    # # 方法1：
    # # gswin64c.exe为Ghostscript打印程序安装后bin目录中的一个组件,下载地址：https://www.ghostscript.com/
    # # 方法2：
    # # windows自带打印cmd命令，可以打印安装了相关阅读软件的文件，如打印word文件，需要安装office，环境依赖很严重
    # # 方法3：
    # # SumatraPDF-3.3.3-64.exe（一个mini pdf阅图神器，支持打印）下载地址：https://www.sumatrapdfreader.org/free-pdf-reader
    # # 方法4：
    # # PDFtoPrinter.exe下载地址：http://www.columbia.edu/~em36/pdftoprinter.html,调用cmd，语法简单，小巧好用，但是不支持格式设置，
    # # 听说该软件是PDF-XChange某个封装的组件
    # # 方法5：
    # # PDF-XChange Editor 9.2.359.0.exe,有300多M，下载安装，默认路径
    # # 下载地址：https://www.tracker-software.com/product/pdf-xchange-lite
    # # 安装好了之后会在C:\Users\zhangchunguang\AppData\Local\Temp\PDFPrinterTmp 目录下找到以下文件：
    # # PDFXCview.exe,qpdf28.dll,resource.dat,settings.dat 一共4个文件，可以拷贝走，但需放在一起，使用的时候只需要调用PDFXCview.exe即可
    # :param cprinter: 调用的打印机名称
    # :param pdf: pdf文件的绝对路径
    # :return:
    # """
    # 第一种方法，我用可以，别人用的时候又不行-----
    # if sys.platform == 'win32':
    #     args = [f"{os.path.dirname(__file__)}\plug\gswin64c.exe",
    #             '-sDEVICE=mswinpr2',
    #             '-dBATCH',
    #             '-dNOPAUSE',
    #             '-dFitPage',
    #             f'-sOutputFile="%printer%{cprinter}"',
    #             f'"{pdf}"']
    #     subprocess.run(args, encoding="utf-8", shell=True)

    # 第二种方法，常规通用方法，可以用，但是控制不了颜色，我用的彩色打印机，打出来是彩色和黑白叠加的的，懒得研究了-----
    # win32api.ShellExecute(
    #     0,
    #     "print",
    #     pdf,
    #     '/d:"%s"' % cprinter,
    #     ".",
    #     0
    # )

    # 第三种方法，没搞成功，程序也无法自动关闭-----
    # if sys.platform == 'win32':
    #     args = [f"{os.path.dirname(__file__)}\plug\SumatraPDF-3.3.3-64.exe",
    #             '-silent',
    #             '-print-to',
    #             f'{cprinter}',
    #             '-print-settings',
    #             'shrink,monochrome',
    #             '-print-dialog',
    #             "-exit-when-done",
    #             f'{pdf}'
    #             ]
    #     subprocess.run(args, encoding="utf-8", shell=True)

    # 第四种方法，此方法调用独立插件，减少了对系统的环境的依赖-----
    if sys.platform == 'win32':
        args = [f"{os.path.dirname(__file__)}/plug/PDFtoPrinter.exe",
                f"{pdf}",
                f"{cprinter}",
                ]
        subprocess.run(args, encoding="utf-8", shell=True)
    print(f"\t|已发送至打印机：{cprinter}")

    # 第五种方法，也可以，但是这个插件包含多个依赖文件，比方法4麻烦----
    # if sys.platform == 'win32':
    #     args = [f"{os.path.dirname(__file__)}\plug\PDFXCview.exe",
    #             f"{pdf}",
    #             f"{cprinter}",
    #             ]
    #     subprocess.run(args, encoding="utf-8", shell=True)
    # print(f"\t|已发送至打印机：{cprinter}")

start_printer()