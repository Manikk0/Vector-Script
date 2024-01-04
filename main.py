from PIL import Image
from re import match
from functions import *

def main():
    with open("text.ves", "r") as f:
        file_current = f.read().splitlines()

    try:
        user_width = int(input("Desired width: "))
    except:
        user_width = 0
    try:
        user_height = int(input("Desired height: "))
    except:
        user_height = 0

    pattern = r"VES v\d+\.\d+ \d+ \d+"
    try:
        match_found = match(pattern, file_current[0])
        if not match_found:
            raise TypeError("Use correct file type!")
    except TypeError as error:
        print(error)
        exit()


    width, height = int(file_current[0].split(" ")[2]), int(file_current[0].split(" ")[3])
    obr = Image.new("RGB", (width, height), (255, 255, 255))

    if user_width and user_height:
        if user_width/user_height == width/height:
            scale = True
        else:
            scale = False
            user_width, user_height = None, None
    elif user_width and not user_height:
        user_height = height / width * user_width
        scale = True
    elif user_height and not user_width:
        user_width = width / height * user_height
        scale = True
    else:
        scale = False
        user_width, user_height = None, None

    for command_current in file_current[1:]:
        try:
            object_current, object_size = command_current.split(" ")[0], command_current.split(" ")[1:]
            if object_current == "CLEAR":
                object_size = object_size[0]
                clear(obr, width, height, object_size)
            elif object_current == "LINE":
                bod_a, bod_b, weight, color_current = (
                    tuple(object_size[0:2]),
                    tuple(object_size[2:4]),
                    int(float(object_size[4])),
                    object_size[5],
                )
                bod_a, bod_b = tuple(int(float(x)) for x in bod_a), tuple(
                    int(float(x)) for x in bod_b
                )
                thick_line(obr, bod_a, bod_b, weight, color_current, user_width, user_height, scale)
            elif object_current == "CIRCLE":
                bod_a, radius, weight, color_current = (
                    tuple(object_size[0:2]),
                    int(float(object_size[2])),
                    int(float(object_size[3])),
                    object_size[4],
                )
                bod_a = tuple(int(float(x)) for x in bod_a)
                circle(obr, bod_a, radius, weight, color_current, user_width, user_height, scale)
            elif object_current == "FILL_CIRCLE":
                bod_a, radius, color_current = (
                    tuple(object_size[0:2]),
                    int(float(object_size[2])),
                    object_size[3],
                )
                bod_a = tuple(int(float(x)) for x in bod_a)
                filled_circle(obr, bod_a, radius, color_current, user_width, user_height, scale)
            elif object_current == "RECT":
                bod_a, width, height, weight, color_current = (
                    tuple(object_size[0:2]),
                    int(float(object_size[2])),
                    int(float(object_size[3])),
                    int(float(object_size[4])),
                    object_size[5],
                )
                bod_a = tuple(int(float(x)) for x in bod_a)
                rect(
                    obr, bod_a, width, height, weight, color_current, user_width, user_height, scale
                )
            elif object_current == "FILL_RECT":
                bod_a, width, height, color_current = (
                    tuple(object_size[0:2]),
                    int(float(object_size[2])),
                    int(float(object_size[3])),
                    object_size[4],
                )
                bod_a = tuple(int(float(x)) for x in bod_a)
                filled_rect(
                    obr, bod_a, width, height, color_current, user_width, user_height, scale
                )
            elif object_current == "FILL_TRIANGLE":
                bod_a, bod_b, bod_c, color_current = (
                    tuple(object_size[0:2]),
                    tuple(object_size[2:4]),
                    tuple(object_size[4:6]),
                    object_size[6],
                )
                bod_a, bod_b, bod_c = (
                    tuple(int(float(x)) for x in bod_a),
                    tuple(int(float(x)) for x in bod_b),
                    tuple(int(float(x)) for x in bod_c),
                )
                filled_triangle(
                    obr, bod_a, bod_b, bod_c, color_current, user_width, user_height, scale
                )
            elif object_current == "TRIANGLE":
                bod_a, bod_b, bod_c, weight, color_current = (
                    tuple(object_size[0:2]),
                    tuple(object_size[2:4]),
                    tuple(object_size[4:6]),
                    int(float(object_size[6])),
                    object_size[7],
                )
                bod_a, bod_b, bod_c = (
                    tuple(int(float(x)) for x in bod_a),
                    tuple(int(float(x)) for x in bod_b),
                    tuple(int(float(x)) for x in bod_c),
                )
                triangle(
                    obr, bod_a, bod_b, bod_c, weight, color_current, user_width, user_height, scale
                )
            elif command_current != "":
                raise SyntaxError(
                    f"Syntax error on line {file_current.index(command_current)+1}: Unknown command {object_current}."
                )
        except SyntaxError as error:
            print(error)

    obr.show()

if __name__ == "__main__":
    main()