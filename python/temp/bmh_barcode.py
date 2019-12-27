import os
import barcode
from barcode.writer import ImageWriter

def barcode128(filepath, name):
    """
    功能：在指定目录生成 code128 条码
    参数：filepath = 条码生成目录
         name = 条码内容，同时也是生成的条码文件名
    """
    # 查看 python-barcode 支持的条形码格式
    # print(barcode.PROVIDED_BARCODES)
    # 获取编码类
    Code = barcode.get_barcode_class('code128')
    # 获取条形码对象
    bar = Code(name, writer=ImageWriter())
    fullname = os.path.join(filepath, name)
    # 保存条形码文件，条码高度5毫米，不显示文本
    bar.save(fullname, {'module_height':5, 'write_text':False})


def main():
    """
    功能： 生成研考考生报名号条形码
    """
    print("正在生成条形码，请稍候...")
    source_filepath = '/home/jackchen/2020年硕士研究生编排管理系统-修正版/zp/print'
    targer_filepath = '/home/jackchen/2020年硕士研究生编排管理系统-修正版/barcode'
    g = os.walk(source_filepath)
    for path, d, filelist in g:
        filelist.sort()
        for filename in filelist:
            if filename.endswith('jpg'):
                # 分离文件名与扩展名
                (fn, extension) = os.path.splitext(filename)
                barcode128(targer_filepath, fn)
    print("条形码生成完毕！")


if __name__ == "__main__":
    main()