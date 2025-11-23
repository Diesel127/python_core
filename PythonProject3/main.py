with open("image.bmp", "rb") as infile:
    image_file = infile.read()
with open("output.img", "wb") as outfile:
    outfile.write(image_file)
infile.close()
outfile.close()