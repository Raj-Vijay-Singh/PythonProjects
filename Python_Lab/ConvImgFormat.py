from PIL import Image

def conv(fpath, path, imgname):
    img = Image.open(fpath)
    changedir = False

    ch = input("Enter the path to the FOLDER where you want to save converted image. (Leave blank to save in source folder):\n")

    if r"\\" in ch:
        path = ch


    if img.format == "PNG":
        resf = ".jpg"
        print("Your file was in png format. It has been saved in JPG format in the source directory.")
    else:
        resf = ".png"
        print(f"Your file was in {img.format} format. It has been saved in PNG format in the source directory.")

    path = path + imgname + resf
    img.save(path)

fp = input("Enter the path of the image you want to convert: ")
path = fp[0: (fp.rfind(r"\\")) + 2]
filename = fp[(fp.rfind(r"\\")) + 2: fp.find(".")]
conv(fp, path, filename)
