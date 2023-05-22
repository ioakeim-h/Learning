import sys
from PIL import Image, ImageOps


if 3 < len(sys.argv): 
    sys.exit("Too many command-line arguments")
elif 3 > len(sys.argv):
    sys.exit("Too few command-line arguments")
elif (sys.argv[1][-4:].casefold() or sys.argv[2][-4:].casefold()) not in [".jpg",".jpeg",".png"]:
    sys.exit("Invalid input")
elif sys.argv[1][-4:].casefold() != sys.argv[2][-4:].casefold():
        sys.exit("Input and output have different extensions")
else:
    
    try:
        
        shirt = Image.open("shirt.png")
        size = shirt.size

        input_img = Image.open(sys.argv[1])
        input_img = ImageOps.fit(input_img, size=size)
        
        input_img.paste(shirt, shirt)
        input_img.save(sys.argv[2])

    
    except FileNotFoundError:
        sys.exit("File does not exist")










