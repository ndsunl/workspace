import os
import barcode
from barcode.writer import ImageWriter
from dbfread import DBF

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
    bar.save(fullname, {'module_height':5, 'write_text':True})


def main():
    """
    功能：生成研考考生报名号条形码
    说明：条形码内容为考试科目单元顺序号+报名号后5位
    """
    print("正在生成条形码，请稍候...")
 
    dbf_filepath = '/media/sun/Data/数据备份/研招/_2021yz/考场编排软件/userdb/sbm.dbf'
    targer_filepath = '/media/sun/Data/数据备份/研招/_2021yz/考场编排软件/zp/barcode'
    
    table = DBF(dbf_filepath, encoding='gb18030', char_decode_errors='ignore')
    rec = 0
    for record in table:
        bar_num = 0
        bmh = record['BMH']
        if record['SCH11'] != '':
            barcode128(targer_filepath, '1'+bmh[4:])
            bar_num += 1
        if record['SCH12'] != '':
            barcode128(targer_filepath, '2'+bmh[4:])
            bar_num += 1
        if record['SCH21'] != '':
            barcode128(targer_filepath, '3'+bmh[4:])
            bar_num += 1
        if record['SCH22'] != '':
            barcode128(targer_filepath, '4'+bmh[4:])
            bar_num += 1
        if record['SCH31'] != '':
            barcode128(targer_filepath, '5'+bmh[4:])
            bar_num += 1
        xm = record['XM']
        rec += 1
        print(f"{rec}. 姓名：{xm}，报名号：{bmh} 生成 {bar_num} 张条形码。")
    print("条形码生成完毕！")


if __name__ == "__main__":
    main()