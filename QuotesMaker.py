from PIL import Image, ImageDraw, ImageFont
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def main():
    print(f"{Fore.GREEN}Enter Your Quotes")
    template = input("Chose Background : ")
    templateBg = Image.open(f'Background/{template}.jpg')

    # ----- Fonts Library------
    print("Arial[0] , Roboto-Medium[1], LuckiestGuy[2]")
    Fonts_name = ['Arial', 'Roboto', 'LuckiestGuy']
    add_number = int(input("Enter Number Do you want to use : "))
    font = Fonts_name[add_number]
    fonts = font
    font_object =  ImageFont.truetype(f'Fonts/{fonts}.ttf', 35 )

    drawing_object = ImageDraw.Draw(templateBg)

    text0 = input("0 line : ")
    text1 = input("1 Line : ")
    text2 = input("2 Line : ")
    text3 = input("3 Line : ")
    text4 = input("4 Line : ")
    text5 = input("5 Line : ")
    text6 = input("6 Line : ")
    text7 = input("7 Line : ")
    text8 = input("8 Line : ")
    text9 = input("9 Line : ")
    # L0-450 L1-500 L2-550 L3-600 L4-650 L5-700 L6-750 L7-800 L8-850 L9-900
    print("")
    
    white = (251,255,255)
    black = (0,0,0)

    if white or black:
        color = input("White or black color : ")
      
    textcolor = color

    drawing_object.text((120,450), text0, fill=textcolor, font = font_object )
    drawing_object.text((120,500), text1, fill=textcolor, font = font_object )
    drawing_object.text((120,550), text2, fill=textcolor, font = font_object )
    drawing_object.text((120,600), text3, fill=textcolor, font = font_object )
    drawing_object.text((120,650), text4, fill=textcolor, font = font_object )
    drawing_object.text((120,700), text5, fill=textcolor, font = font_object )
    drawing_object.text((120,750), text6, fill=textcolor, font = font_object )
    drawing_object.text((120,800), text7, fill=textcolor, font = font_object )
    drawing_object.text((120,850), text8, fill=textcolor, font = font_object )
    drawing_object.text((120,900), text9, fill=textcolor, font = font_object )

    QuoteSave = input("Save Your Image Name : ")
    templateBg.save(f'Quotes/{QuoteSave}.jpg')

    Repeat = input("Would You Like To Run Again ? Y or N ",).lower()
    if Repeat =="y":
        main()
    else:
        print("n")
        exit()

    print("")


main()

