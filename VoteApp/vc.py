
import os
from PIL import Image, ImageDraw
import base64
from PIL import ImageFont
def encryption(fn):
    image = Image.open(r"E:\e_voting\media\img/"+fn)
    image1=Image.open(r"E:\e_voting\media\img/"+fn)
    image2=Image.open(r"E:\e_voting\media/"+fn)
    width, height = image.size
    #
    for row in range(height):
        for col in range(width):
            try:
                r, g, b = image.getpixel((col, row))
            except:
                r, g, b,_ = image.getpixel((col, row))
            r1=(r&240)>>4
            r2=r&15



            g1 = (g & 240) >> 4
            g2 = g & 15

            b1 = (b & 240) >> 4
            b2 = b & 15


            r1=r1^g1
            g1=g1^b1
            b1=b1^r1





            r2 = r2 ^ g2
            g2 = g2 ^ b2
            b2 = b2 ^ r2



            image1.putpixel((col, row), (r1, g1, b1))
            image2.putpixel((col, row), (r2, g2, b2))
    # #


    # image1.save("s1"+fn)
    # image2.save("s2"+fn)
    #
    image11=image1#Image.open("sample1.bmp")
    image22=image2#Image.open("sample2.bmp")
    #
    # sl=[0,3,2,1]
    bs=width//10
    #
    # print(bs)
    for row in range(height):

        for col in range(width//10):
                try:
                    r, g, b = image1.getpixel(((bs*1)+col, row))
                    r1, g1, b1 = image1.getpixel(((bs * 5) + col, row))
                except:
                    r, g, b,_ = image1.getpixel(((bs * 1) + col, row))
                    r1, g1, b1,_ = image1.getpixel(((bs * 5) + col, row))
                image11.putpixel((((bs*1)+col), row), (r1, g1, b1))
                image11.putpixel((((bs * 5) + col), row), (r, g, b))
                try:
                    r, g, b = image1.getpixel(((bs * 2) + col, row))
                    r1, g1, b1 = image1.getpixel(((bs * 7) + col, row))
                except:
                    r, g, b,_ = image1.getpixel(((bs * 2) + col, row))
                    r1, g1, b1,_ = image1.getpixel(((bs * 7) + col, row))
                image11.putpixel((((bs * 2) + col), row), (r1, g1, b1))
                image11.putpixel((((bs * 7) + col), row), (r, g, b))
                try:
                    r, g, b = image1.getpixel(((bs * 4) + col, row))
                    r1, g1, b1 = image1.getpixel(((bs * 9) + col, row))
                except:
                    r, g, b,_ = image1.getpixel(((bs * 4) + col, row))
                    r1, g1, b1,_ = image1.getpixel(((bs * 9) + col, row))
                image11.putpixel((((bs * 4) + col), row), (r1, g1, b1))
                image11.putpixel((((bs * 9) + col), row), (r, g, b))



                try:
                    r, g, b = image2.getpixel(((bs*1)+col, row))
                    r1, g1, b1 = image22.getpixel(((bs * 5) + col, row))
                except:
                    r, g, b,_ = image2.getpixel(((bs * 1) + col, row))
                    r1, g1, b1,_ = image22.getpixel(((bs * 5) + col, row))
                image22.putpixel((((bs*1)+col), row), (r1, g1, b1))
                image22.putpixel((((bs * 5) + col), row), (r, g, b))
                try:
                    r, g, b = image2.getpixel(((bs * 2) + col, row))
                    r1, g1, b1 = image2.getpixel(((bs * 7) + col, row))
                except:
                    r, g, b,_ = image2.getpixel(((bs * 2) + col, row))
                    r1, g1, b1,_ = image2.getpixel(((bs * 7) + col, row))
                image22.putpixel((((bs * 2) + col), row), (r1, g1, b1))
                image22.putpixel((((bs * 7) + col), row), (r, g, b))
                try:
                    r, g, b = image2.getpixel(((bs * 4) + col, row))
                    r1, g1, b1 = image2.getpixel(((bs * 9) + col, row))
                except:
                    r, g, b,_ = image2.getpixel(((bs * 4) + col, row))
                    r1, g1, b1,_ = image2.getpixel(((bs * 9) + col, row))
                image22.putpixel((((bs * 4) + col), row), (r1, g1, b1))
                image22.putpixel((((bs * 9) + col), row), (r, g, b))
    #
    image11.save(r"E:\e_voting\media\share1/"+fn)
    image22.save(r"E:\e_voting\media\share2/"+fn)

def decription(fn1,fn):
    print(fn,"===========")

    try:
        image = Image.open(r"E:\e_voting\media/"+fn)
        image11 = Image.open(r"E:\e_voting\media/"+fn)
        image22 = Image.open(r"E:\e_voting\media/share2/"+fn1)
        image1 = Image.open(r"E:\e_voting\media/"+fn)
        image2 = Image.open(r"E:\e_voting\media/share2/"+fn1)

        width, height = image.size
        #

        sl = [0, 3, 2, 1]
        bs = width // 10

        print(bs)
        for row in range(height):

            for col in range(width // 10):
                try:
                    r, g, b = image11.getpixel(((bs * 1) + col, row))
                    r1, g1, b1 = image11.getpixel(((bs * 5) + col, row))
                except:
                    r, g, b,_ = image11.getpixel(((bs * 1) + col, row))
                    r1, g1, b1,_ = image11.getpixel(((bs * 5) + col, row))
                image1.putpixel((((bs * 1) + col), row), (r1, g1, b1))
                image1.putpixel((((bs * 5) + col), row), (r, g, b))
                try:
                    r, g, b = image11.getpixel(((bs * 2) + col, row))
                    r1, g1, b1 = image11.getpixel(((bs * 7) + col, row))
                except:
                    r, g, b,_ = image11.getpixel(((bs * 2) + col, row))
                    r1, g1, b1,_ = image11.getpixel(((bs * 7) + col, row))

                image1.putpixel((((bs * 2) + col), row), (r1, g1, b1))
                image1.putpixel((((bs * 7) + col), row), (r, g, b))
                try:
                    r, g, b = image11.getpixel(((bs * 4) + col, row))
                    r1, g1, b1 = image11.getpixel(((bs * 9) + col, row))
                except:
                    r, g, b,_ = image11.getpixel(((bs * 4) + col, row))
                    r1, g1, b1,_ = image11.getpixel(((bs * 9) + col, row))
                image1.putpixel((((bs * 4) + col), row), (r1, g1, b1))
                image1.putpixel((((bs * 9) + col), row), (r, g, b))
                try:
                    r, g, b = image22.getpixel(((bs * 1) + col, row))
                    r1, g1, b1 = image22.getpixel(((bs * 5) + col, row))
                except:
                    r, g, b,_ = image22.getpixel(((bs * 1) + col, row))
                    r1, g1, b1,_ = image22.getpixel(((bs * 5) + col, row))
                image2.putpixel((((bs * 1) + col), row), (r1, g1, b1))
                image2.putpixel((((bs * 5) + col), row), (r, g, b))
                try:
                    r, g, b = image22.getpixel(((bs * 2) + col, row))
                    r1, g1, b1 = image22.getpixel(((bs * 7) + col, row))
                except:
                    r, g, b,_ = image22.getpixel(((bs * 2) + col, row))
                    r1, g1, b1,_ = image22.getpixel(((bs * 7) + col, row))

                image2.putpixel((((bs * 2) + col), row), (r1, g1, b1))
                image2.putpixel((((bs * 7) + col), row), (r, g, b))
                try:
                    r, g, b = image22.getpixel(((bs * 4) + col, row))
                    r1, g1, b1 = image22.getpixel(((bs * 9) + col, row))
                except:
                    r, g, b,_ = image22.getpixel(((bs * 4) + col, row))
                    r1, g1, b1,_ = image22.getpixel(((bs * 9) + col, row))
                image2.putpixel((((bs * 4) + col), row), (r1, g1, b1))
                image2.putpixel((((bs * 9) + col), row), (r, g, b))
        width, height = image.size
        # #
        for row in range(height):
            for col in range(width):
                try:
                    r1, g1, b1 = image1.getpixel((col, row))
                    r2, g2, b2 = image2.getpixel((col, row))
                except:
                    r1, g1, b1,_ = image1.getpixel((col, row))
                    r2, g2, b2,_ = image2.getpixel((col, row))

                b1 = b1 ^ r1
                g1 = g1 ^ b1
                r1 = r1 ^ g1

                b2 = b2 ^ r2
                g2 = g2 ^ b2
                r2 = r2 ^ g2

                r1 = r1 << 4
                r = r1 | r2

                g1 = g1 << 4
                g = g1 | g2

                b1 = b1 << 4
                b = b1 | b2

                image.putpixel((col, row), (r, g, b))

        image.save(r"E:\e_voting\media\final/" + fn1)

        return "true"
    except:
        return "false"

def makeimg(st,fn):
    my_image = Image.open(r"E:\e_voting\voteApp\sample.png")
    title_font = ImageFont.truetype(r'E:\e_voting\voteApp\Montserrat-SemiBold.otf', 80)
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((35, 15), st, (0, 0, 0), font=title_font)
    my_image.save(r"E:\e_voting\media\img/"+fn)

# makeimg("2345","24.png")
# encryption("24.png")
# decription("img.png")