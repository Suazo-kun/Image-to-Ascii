#!/usr/bin/python3
from os.path import abspath
from imagetoascii import ImageToAscii

if __name__ == '__main__':
    while True:
        try:
            image_path = input("Image path: ")
            width = int(input("Width (1-1000): "))
            result = ImageToAscii(image_path, width)

            with open("ascii-art.txt", "w", encoding="UTF-8") as f:
                f.write(result)

            print(f"Result in: {abspath('ascii-art.txt')}.")
            print("--- Sucess ---\n")

        except Exception as e:
            print(f"Error log: {repr(e)}")
