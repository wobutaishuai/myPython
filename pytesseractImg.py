#coding:utf-8
from PIL import Image
import sys
from pytesseract import *
import re
import os



# 二值化
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

#由于都是数字
#对于识别成字母的 采用该表进行修正
rep={'O':'0',
     'I':'1',
     'L':'1',
     'Z':'2',
     'S':'8'
    }
#修正t 识别L
rep1={'l':'t'
    }
def getverify(name,flag):
    #打开图片
    im = Image.open(name)
    #转化到灰度图
    imgry = im.convert('L')
    #二值化，采用阈值分割法，threshold为分割点
    out = imgry.point(table, '1')
    #识别对吗
    if flag == 1:
        text = image_to_string(out)
        text = text.strip()
        text = text.upper()
        for r in rep:
            text = text.replace(r, rep[r])
    else:
        #将图片转为gif图
        imgif = out.convert('RGB').convert("P")
        #创建新的底板为白色  255为白色点 0 为黑色
        imnew = Image.new("P", im.size, 255)
        # 去掉边界的黑色从一到图片的边界最后一位
        for x in range(1, (imgif.size[0]-1)):
            for y in range(1, (imgif.size[1]-1)):
                pix = imgif.getpixel((x, y))
                if pix == 0:
                    imnew.putpixel((x, y), 0)
        if imnew:
            text = image_to_string(imnew)
            for r in rep1:
                text = text.strip()
                text = text.replace(r, rep1[r])
            text = text.lower()
    text = re.sub('[\W]', '', text)
    if len(text) == 4:
        print text
        return str(text)
    else:
        print "识别失败！！！！"
        return ''




if __name__ == '__main__':
   getverify("captcha1498121465864.jpg")
