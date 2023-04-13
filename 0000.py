#题目：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from PIL import Image, ImageDraw, ImageFont

def solution(img):
    #打开图像
    img = Image.open(img)

    #对img进行绘画
    draw = ImageDraw.Draw(img)

    #获取图像的长宽
    width, height = img.size

    #定位到右上角
    x = width - 150
    y = 0
    
    #创建字体对象
    font = ImageFont.truetype('C:/windows/fonts/Arial.ttf', 150)

    #在右上角加上红色的数字
    draw.text((x, y), '34', (255, 0, 0), font=font)

    #显示修改后的图像
    img.show()


if __name__ == '__main__':
    img = './pic/1.jpg'
    solution(img)
    