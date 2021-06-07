import os
from PIL import Image
# numbers = ['1.png','2.png','6.png','4.png','10.png']
# # Sorting list of Integers in ascending
# numbers.sort(key=lambda x: int(x[:-4]))
#
#
# print(numbers)

def aef():
    pass
def modify(input)->str:
    # change dir
        os.chdir(input)
        output = '/home/mq/Pictures'
        # iterative
        for image_name in os.listdir(os.getcwd()):
            print(image_name)
            #im = Image.open(os.path.join(input, image_name))
            #im.thumbnail((768, 128))
            #im.save(os.path.join(output, image_name))


if __name__ == "__main__":
    modify('/home/mq/Documents/Writer_identification/data/cvl/cvl-database-cropped-1-1/train')

