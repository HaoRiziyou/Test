import os

from PIL import Image
import json
import glob
import sys


# 解决对应的问题  然后
def make_tuple():
    img_list = []
    res = []
    files = os.listdir('/home/mq/Pictures/grouting/real_db/txt_7/')
    #print(files)
    # files.sort(key = )
    my_tuple=()

    for filename in glob.glob('/home/mq/Pictures/grouting/real_db/txt_7/*.png'):  # assuming
        #print(filename)
        im = Image.open(filename)
        img_list.append(im)

    txt_list = []
    for filename in glob.glob('/home/mq/Pictures/grouting/real_db/txt_7/*.json'):  # assuming

        #print(filename)
        txt = json.load(open(filename))
        txt_list.append(txt)
    my_tuple=()
    file1 = glob.glob('/home/mq/Pictures/grouting/real_db/txt_7/*.png')
    file2 = glob.glob('/home/mq/Pictures/grouting/real_db/txt_7/*.json')
    for x in range(len(file1)):
        for y in range(len(file2)):
            if(os.path.basename(file1[x])[:-4] == os.path.basename(file2[y])[:-5]):
                my_tuple=(file1[x],file2[y])
                res.append(my_tuple)
    for filename in res:
        im = Image.open(filename[0])
        img_list.append(im)
        txt = json.load(open(filename[1]))
        txt_list.append(txt)
        #print(filename[0],filename[1])

    #print(img_list,txt_list)


    #return my_tuple
    return (img_list,txt_list)


#print(txt_list[1])
img=Image.open("/home/mq/Pictures/grouting/real_db/txt_7/0001-7-cropped.png")
gt=json.load(open("/home/mq/Pictures/grouting/real_db/txt_7/0001-7-cropped.json"))
res=[]
for n in range(len(gt["captions"])):
        textline=img.crop(gt['rectangles_ltrb'][n])
        caption=gt['captions'][n]
        caption=caption[caption.find("@")+1:]
        res.append((textline, caption))
        #textline.show()
#print(res)

dou=()

my_tuple= make_tuple()
for k in range(2):
    for n in range(len(my_tuple[1][k]["captions"])):

        textline=img.crop(my_tuple[1][k]['rectangles_ltrb'][n])
        caption=my_tuple[1][k]['captions'][n]
        caption=caption[caption.find("@")+1:]
        res.append((k,textline,caption))


    #dou = (k,res)

print(res)







#n = 0
#for x[0][]
#
# img_list=[]
# for x in (range(len(sec))):
#     for y in range(1):
#     #print(sec[x][1][x][0])
#         img_list.append(sec[x][1][y][0])
#
# print(img_list)
#print(sec[0][1][0][1])

#有问题 不知道从第几个是分割两幅图片  加了一个k知道是第几个了 还是没有解决我想知姐得到27个元素的问题 所以想到了 再来个tuple 放入sec

"""
/home/mq/PycharmProjects/pythonProject1/venv/bin/python /home/mq/PycharmProjects/pythonProject1/venv/grout.py
(<PIL.Image.Image image mode=RGB size=1856x158 at 0x7F50CE25CE80>, 'You have killed my love. You used to stir my')
(<PIL.Image.Image image mode=RGB size=1868x144 at 0x7F50CCC72AC0>, "imagination. Now you don't even stir my curiosity.")

Process finished with exit code 0
"""