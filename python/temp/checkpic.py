import os
from PIL import Image
import PIL.ImageOps
import glob

def check_pic(filename):
    """
    功能: 检测 jpg 文件为全黑或全白图像
    参数: filename 文件名
    """
    with Image.open(filename) as img:
        if not img.getbbox():
           # all black
           print(f"{filename} 为全黑图像")
        elif not PIL.ImageOps.invert(img).getbbox():
           # all white
           print(f"{filename} 为全白图像")


if __name__ == "__main__":
    # 获取当前执行脚本的绝对路径
    realpath = os.path.realpath(__file__)
    # 去掉文件名，返回目录
    dirname = os.path.dirname(realpath)
    # 寻找 jpg 文件类型
    extension = 'jpg'
    # 获取当前工作目录下所有 jpg 文件
    file_list = glob.glob('*.'+extension)
    for filename in file_list:
        check_pic(filename)