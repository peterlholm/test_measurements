"Generate structured image"
from pathlib import Path
from PIL import Image, ImageDraw
#from PIL.ExifTags import TAGS
from PIL.PngImagePlugin import PngInfo

XPAUTHOR = 40094
XPTITLE = 40092
IMAGEDESCRIPTION = 0x010e

PICTURE_SIZE = 30   # mm
INCH = 25.4         # mm
DPI = [600, 1200, 2400]

def create_square(filename, size, dpi):
    "create the doble square img"
    pixel_size = int(size / INCH * dpi)
    grey = Image.new('L', (pixel_size, pixel_size), 255)
    cm1 = int(10 * dpi / INCH)
    mm1 = cm1 // 10
    print ("cm1", cm1, "mm", mm1, "size", pixel_size)
    center = pixel_size // 2
    start = center - cm1 // 2
    shape = [(start, start),(start + cm1, start + cm1)]
    start2 = center - cm1
    shape2 = [(start2, start2),(start2 + 2*cm1, start2 + 2*cm1)]
    img = ImageDraw.Draw(grey)
    img.rectangle(shape2, fill=255, outline=0, width=mm1//2)
    img.rectangle(shape, fill=255, outline=0, width=mm1)
    # for y in range(pixel_size):
    #     #print(val, intens)
    #     for x in range(pixel_size):
    #         val = 128 
    #         grey.putpixel((x, y), val)

    metadata = PngInfo()
    metadata.add_text(
        "Description", f"Freq ")
    metadata.add_text("Author", "Peter Holm")
    exif = grey.getexif()
    exif[XPAUTHOR] = "Peter Holm"
    exif[XPTITLE] = f"Freq (pic/period "
    exif[IMAGEDESCRIPTION] = f"Freq (pic/period "
    DPIXY = (dpi, dpi)

    grey.save(filename,  dpi=DPIXY, pnginfo=metadata)
    

create_square("1cm.png", PICTURE_SIZE, 600)
