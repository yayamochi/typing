from PIL import Image
import sys
import pyocr
import pyocr.builders
import pyautogui as p
import webbrowser
import time

tools = pyocr.get_available_tools()
tool = tools[0]

def read(screen_region):

    im = p.screenshot(region=screen_region)
    width = screen_region[2]#読み込みの幅
    height = screen_region[3]#読み込みの高さ

    minx = -1
    maxx = width

    for x in range(width):
        # get pixel in (x, height / 2)
        (r, g, b, a) = im.getpixel((x,height//2))#座標指定
        # calculate value
        value = max(r, g, b)

        if value < 80:
            if minx == -1:
                minx = x
            maxx = x
    #im.putpixel((minx,height//2),(255,0,0))
    #im.putpixel((maxx,height//2),(0,0,255))
    print("crop: {0} to {1}".format(minx,maxx))
    #im = im.crop((minx, 0, maxx, height))
    im.save("crop.png")

    txt = tool.image_to_string(
        im,
        lang="eng",
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )

    txt = txt.replace("I","").replace(" ","").replace("—","-").replace("\'","").replace("`","").replace("\\","")
    return txt

if __name__ == '__main__':
    while True:
        txt = read((850*2,392*2,(1250-850)*2,(416-392)*2))

        print(txt)
        p.typewrite(txt)
        time.sleep(0.17)
