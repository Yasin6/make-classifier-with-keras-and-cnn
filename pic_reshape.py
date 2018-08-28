# coding=utf-8
_author_ = 'Yasin'
_date_ = '2018-08-27 17:03'

import os
from PIL import Image

# 统一图片类型，对图片格式、名称进行处理
def renamesJPG(filepath, kind):    # 两参数分别为：文件路径及我们设置猫的种类
    images = os.listdir(filepath)  # 遍历指定文件夹，并将所有文件存入images变量中
    for name in images:            # 重命名后的格式为：种类_原名称.jpg
        os.rename(filepath+name, filepath+kind+'_'+name.split('.')[0]+'.jpg')
# 调用三次函数，分别对不同种类的猫进行处理
renamesJPG('C:\\Users\\Administrator\\Desktop\\cat_kinds\\布偶猫\\','0')
renamesJPG('C:\\Users\\Administrator\\Desktop\\cat_kinds\\孟买猫\\','1')
renamesJPG('C:\\Users\\Administrator\\Desktop\\cat_kinds\\暹罗猫\\','2')
renamesJPG('C:\\Users\\Administrator\\Desktop\\cat_kinds\\英国短毛猫/','3')


# 该函数可以将图片裁剪成指定大小
def reshape(filepath ,outdir,width=100,height=100):
    images = os.listdir(filepath)
    for imgs in images:
        img = Image.open(filepath+imgs)
        try:
            new_img = img.resize((width, height), Image.BILINEAR)
            new_img.save(os.path.join(outdir, os.path.basename(imgs))) # 注意这里是imgs而不是img!!!
        except Exception as e:
            print(e)
# 调用函数，指定传入文件和图片修改后的存储路径
reshape("C:\\Users\\Administrator\\Desktop\\cat_kinds\\布偶猫\\","C:\\Users\\Administrator\\Desktop\\cat_kinds\\buou")
reshape("C:\\Users\\Administrator\\Desktop\\cat_kinds\\孟买猫\\","C:\\Users\\Administrator\\Desktop\\cat_kinds\\mengmai")
reshape("C:\\Users\\Administrator\\Desktop\\cat_kinds\\暹罗猫\\","C:\\Users\\Administrator\\Desktop\\cat_kinds\\xianluo")
reshape("C:\\Users\\Administrator\\Desktop\\cat_kinds\\英国短毛猫\\","C:\\Users\\Administrator\\Desktop\\cat_kinds\\duanmao")
#
#
#


#将图片大小统一修改成100*100
# def convertjpg(jpgfile,outdir,width=100,height=100):
#     img = Image.open('F:/Github/cat_class/data/布偶猫/'+jpgfile)
#     try:
#         new_img = img.resize((width, height), Image.BILINEAR)
#         new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
#     except Exception as e:
#         print(e)
# for jpgfile in os.listdir('F:/Github/cat_class/data/布偶猫/'):
#     print(jpgfile)
#     convertjpg(jpgfile, "./buou")

# def convertjpg(jpgfile,outdir,width=100,height=100):
#     img = Image.open('F:/Github/cat_class/data/孟买猫/'+jpgfile)
#     try:
#         new_img = img.resize((width, height), Image.BILINEAR)
#         new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
#     except Exception as e:
#         print(e)
# for jpgfile in os.listdir('F:/Github/cat_class/data/孟买猫/'):
#     print(jpgfile)
#     convertjpg(jpgfile, "./mengmai")
#
# def convertjpg(jpgfile,outdir,width=100,height=100):
#     img = Image.open('F:/Github/cat_class/data/暹罗猫/'+jpgfile)
#     try:
#         new_img = img.resize((width, height), Image.BILINEAR)
#         new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
#     except Exception as e:
#         print(e)
# for jpgfile in os.listdir('F:/Github/cat_class/data/暹罗猫/'):
#     print(jpgfile)
#     convertjpg(jpgfile, "./xieluo")
#
# def convertjpg(jpgfile,outdir,width=100,height=100):
#     img = Image.open('F:/Github/cat_class/data/英国短毛猫/'+jpgfile)
#     try:
#         new_img = img.resize((width, height), Image.BILINEAR)
#         new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
#     except Exception as e:
#         print(e)
# for jpgfile in os.listdir('F:/Github/cat_class/data/英国短毛猫/'):
#     print(jpgfile)
#     convertjpg(jpgfile, "./duanmao")


