import sys
from PIL import Image
import PIL.ImageOps
import random

def main():
    im_mask, im_output = validate_arguments()
    im_background = f"before{random.randint(1, 3)}.jpg"
    image_convert(im_background, im_mask, im_output)
    

def image_convert(im_background, im_mask, im_output):
    with Image.open(im_background) as image_before, Image.open(im_mask) as image_input:
        new_image = PIL.ImageOps.fit(image_before, size=[600,600])
        new_image.paste(im=image_input, mask=image_input)
        new_image.save(im_output)

def validate_arguments():
    extension_list = (".png", ".jpeg", ".jpg")
    args = [x.lower() for x in sys.argv]
    if len(args) == 3:
        if args[1].endswith(extension_list)and args[2].endswith(extension_list):
            for x in extension_list:
                if args[1].endswith(x) and args[2].endswith(x):
                    return args[1], args[2]
            print("File extension dont match")
            sys.exit()
        else:
            print("Wrong File extension")
            sys.exit()
    elif len(args) < 3:
        print("Too few arguments")
        sys.exit()
    else:
        print("Too many arguments")
        sys.exit()

if __name__ == "__main__":
    main()