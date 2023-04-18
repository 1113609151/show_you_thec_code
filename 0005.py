#你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。


from PIL import Image
import os

path = './pic'

for file in os.listdir(path):
    print(file)
    im = Image.open(os.path.join(path, file))
    im.thumbnail((1136,640))
    im.show()
    # im.save(os.path.join(path, file), 'JPEG')
