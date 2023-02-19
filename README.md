# Image to Ascii
Convert an image to ascii characters... And that's it XD.

# How to use
To use it import in your project **imagetoascii** and call the function **ImageToAscii**, this function accepts as first argument a **path** or an **Image** type object (from pillow) and as second element the **width** that the image will have (it only accepts as value a number between 1 and 1000).<br>

Example:
```Python
from imagetoascii import ImageToAscii

IMAGE_PATH = "/home/user/images/img.jpg"
WIDTH = 300

result = ImageToAscii(IMAGE_PATH, WIDTH)

with open("ascii-art.txt", "w", encoding="UTF-8") as f:
    f.write(result)
```
<br>

On the other hand, if you only want to use the utility, from the terminal/console run **main.py** and supply what is requested.<br>

Example:
```
> main.py
Image path: /home/user/images/img.jpg
Width (1-1000): 300
Result in: /home/user/images/ascii-art.txt
--- Sucess ---
```

# Requeriments
* **Pillow**

    python3 -m pip install pillow
