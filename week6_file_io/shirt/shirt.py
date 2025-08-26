import sys
from PIL import Image, ImageOps
import os

def main():
    argv_input()
    resized_image(sys.argv[1], sys.argv[2])


# Check file name.
def argv_input():
    input = sys.argv
    if len(input) < 3:
        sys.exit("Too few command-line arguments")
    elif len(input) > 3:
        sys.exit("Too many command-line arguments")
    elif input[1].endswith(".jpg") == True or input[1].endswith(".jpeg") == True or input[1].endswith(".png") == True:
        in_file_ext = os.path.splitext(sys.argv[1])
        out_file_ext = os.path.splitext(sys.argv[2])
        if in_file_ext[1] != out_file_ext[1]:
            sys.exit("Input and output have different extensions")
        else:
            pass
    else:
        sys.exit("Invalid input")

# Open input image and resize.
def resized_image(file_name, new_name):
    try:
        img = Image.open(file_name)
        shirt = Image.open("shirt.png")
        new_size = shirt.size
        resized_image = ImageOps.fit(img, new_size)
        resized_image.paste(shirt,shirt)
        resized_image.save(new_name)

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
