import os
from PIL import Image
import PIL.ImageOps
import glob

def check_pic(filename):
    """
    功能: 检测 jpg 文件为全黑或全白图像, 可用于高考报名相片检查
    参数: filename 文件名
    返回: 1=全黑、2=全白
    """
    with Image.open(filename) as img:
        if not img.getbbox():
           # all black
           # print(f"{filename} 为全黑图像")
           return 1
        elif not PIL.ImageOps.invert(img).getbbox():
           # all white
           # print(f"{filename} 为全白图像")
           return 2
        else:
           return 0


def main():
    count = 0
    # 获取当前执行脚本的绝对路径
    realpath = os.path.realpath(__file__)
    # 去掉文件名，返回目录
    dirname = os.path.dirname(realpath)
    g = os.walk(dirname)
    for path,d,filelist in g:
        filelist.sort()
        for filename in filelist:
            if filename.endswith('jpg'):
                fn = os.path.join(path, filename)
                result = check_pic(fn)
                if result == 1:
                   print(f"{fn} 为全黑图像")
                   count += 1
                if result == 2:
                   print(f"{fn} 为全白图像")
                   count += 1
    print(f"一共有 {count} 张全黑或全白图像")


if __name__ == "__main__":
   main()