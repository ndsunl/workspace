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
    g = os.walk(dirname)
    for path,d,filelist in g:
        filelist.sort()
        for filename in filelist:
            if filename.endswith('jpg'):
                count += 1
                check_pic(os.path.join(path, filename))