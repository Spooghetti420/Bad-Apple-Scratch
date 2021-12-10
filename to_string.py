import os
import time
from PIL import Image


def to_string(image: Image):
    pixels = [ ((255,255,255) if (pixel[0]+pixel[1]+pixel[2])/3 > 127 else (0,0,0)) for pixel in list(image.getdata()) ]
    string_output = ""
    current_run_type = None # Either black or white, depending on what sequence of colors is being encoded
    run_length = 0 # How long the current string of values is
    for pixel in pixels:
        if current_run_type != pixel:
            if current_run_type is not None:
                string_output += str(run_length) + ("W" if current_run_type == (255, 255, 255) else "B")
            current_run_type = pixel
            run_length = 1
        else:
            run_length += 1
    string_output += str(run_length) + ("W" if current_run_type == (255, 255, 255) else "B")
    return string_output

def test_numbers(image_string: str):
    total = 0
    current_num = ""
    for char in image_string:
        if char.isdigit():
            current_num += char
        elif current_num != "":
            total += int(current_num)
            current_num = ""
    if current_num != "":
        total += int(current_num)
    return total

try:
    os.mkdir("string")
except:
    pass # Folder already exists

content = ""
for i in range(1, 6573, 2):
    file = f"{i:04}.png"
    print(f"[{time.asctime(time.gmtime())}]: Opening file {file}")
    im = Image.open(os.path.join("frames", file))
    im = im.resize((120, 90))
    string_ver = to_string(im)
    content += string_ver + "\n"
    im.close()
content = content[:-1]

with open("string/output.txt", mode="w") as output:
    output.write(content)