from PIL import Image

TABLE = [
    ' ', '.', '\'', ',', ':', 'c', 'l', 'o', 'd', 'x', 'k', 'O', 'K', 'X',
    'N', 'W', 'M']


def _split_list(list_: list, split_length: int):
    return list(
        list_[i:i+split_length] for i in range(0, len(list_), split_length))


def _data_to_text(data: list, width: int):
    out = ""
    data = _split_list(data, width)

    for convert in data:

        convert = "".join(
            TABLE[int(value/len(TABLE))] for value in convert) + '\n'
        out += convert

    return out


def ImageToAscii(path: str, width: int):
    if type(path) != Image:
        img = Image.open(path)
    else:
        img = path

    if width < 1 or width > 1000:
        raise ValueError(
            "Limit error. Only a width between 1 and 1000 is accepted.")

    if img.width > width:
        aspect_ration = img.width / img.height
        new_width = width
        new_height = int(width / aspect_ration / 2)
        new_height = new_height if new_height > 0 else 1

        img = img.resize((new_width, new_height))

    elif img.width < width:
        aspect_ration = img.width / img.height
        new_width = width
        new_height = int(width * aspect_ration / 2)
        new_height = new_height if new_height > 0 else 1

        img = img.resize((new_width, new_height))

    else:
        img = img.resize((img.width, img.height // 2))

    img = img.convert("L")

    return _data_to_text(list(img.getdata()), img.width)
