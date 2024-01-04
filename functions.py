def hexColor(n_color):
    r = int(n_color[1:3], 16)
    g = int(n_color[3:5], 16)
    b = int(n_color[5:], 16)
    return (r, g, b)


def convert_x(width, output_width, x):
    return int(x / width * output_width)


def convert_y(height, output_height, y):
    return int(y / height * output_height)


def convert_point(width, height, output_width, output_height, X):
    return (
        convert_x(width, output_width, X[0]),
        convert_y(height, output_height, X[1]),
    )


def clear(img, width_c, height_c, color):
    color = hexColor(color)
    for x in range(0, width_c):
        for y in range(0, height_c):
            img.putpixel((x, y), color)


def vnutri(x, y, img):
    width, height = img.size
    return 0 <= x < width and 0 <= y < height


def line(img, A, B, color):
    color = hexColor(color)

    if A[0] == B[0]:
        if A[1] > B[1]:
            A, B = B, A
        for y in range(A[1], B[1] + 1):
            if vnutri(A[0], y, img):
                img.putpixel((A[0], y), color)
    elif A[1] == B[1]:
        if A[0] > B[0]:
            A, B = B, A
        for x in range(A[0], B[0] + 1):
            if vnutri(x, A[1], img):
                img.putpixel((x, A[1]), color)
    else:
        if A[0] > B[0]:
            A, B = B, A
        dx = B[0] - A[0]
        dy = B[1] - A[1]
        if abs(dy / dx) > 1:
            for y in range(min(A[1], B[1]), max(A[1], B[1]) + 1):
                x = int((y - A[1] + (dy / dx) * A[0]) * (dx / dy))
                if vnutri(x, y, img):
                    img.putpixel((x, y), color)
        else:
            for x in range(min(A[0], B[0]), max(A[0], B[0]) + 1):
                y = int((B[1] - A[1]) / (B[0] - A[0]) * (x - A[0]) + A[1])
                if vnutri(x, y, img):
                    img.putpixel((x, y), color)


def linePixels(A, B):
    pixels = []
    if A[0] == B[0]:
        if A[1] > B[1]:
            A, B = B, A
        for y in range(A[1], B[1] + 1):
            pixels.append((A[0], y))
    elif A[1] == B[1]:
        if A[0] > B[0]:
            A, B = B, A
        for x in range(A[0], B[0] + 1):
            pixels.append((x, A[1]))
    else:
        if A[0] > B[0]:
            A, B = B, A
        dx = B[0] - A[0]
        dy = B[1] - A[1]
        if abs(dy / dx) > 1:
            for y in range(min(A[1], B[1]), max(A[1], B[1]) + 1):
                x = int((y - A[1] + (dy / dx) * A[0]) * (dx / dy))
                pixels.append((x, y))
        else:
            for x in range(min(A[0], B[0]), max(A[0], B[0]) + 1):
                y = int((B[1] - A[1]) / (B[0] - A[0]) * (x - A[0]) + A[1])
                pixels.append((x, y))
    return pixels


def filled_circle(img, S, r, color, user_width, user_height, change_size):
    width, height = img.size
    if change_size:
        S, r = (
            convert_point(width, height, user_width, user_height, S),
            r / width * user_width,
        )
    for x in range(0, int(r / 2 ** (1 / 2)) + 1):
        y = int((r**2 - x**2) ** (1 / 2))
        line(img, (x + S[0], y + S[1]), (x + S[0], -y + S[1]), color)
        line(img, (y + S[0], x + S[1]), (y + S[0], -x + S[1]), color)
        line(img, (-x + S[0], -y + S[1]), (-x + S[0], y + S[1]), color)
        line(img, (-y + S[0], -x + S[1]), (-y + S[0], x + S[1]), color)


def thick_line(img, A, B, thickness, color, user_width, user_height, change_size):
    width, height = img.size
    if change_size:
        A, B = convert_point(width, height, user_width, user_height, A), convert_point(
            width, height, user_width, user_height, B
        )
    pixels = linePixels(A, B)
    for X in pixels:
        filled_circle(img, X, thickness / 2, color, user_width, user_height, change_size=False)


def circle(img, S, r, thickness, color, user_width, user_height, change_size):
    width, height = img.size
    if change_size:
        S, r = (
            convert_point(width, height, user_width, user_height, S),
            r / width * user_width,
        )
    for x in range(0, int(r / 2 ** (1 / 2)) + 1):
        y = int((r**2 - x**2) ** (1 / 2))

        filled_circle(
            img,
            (x + S[0], y + S[1]),
            thickness / 2,
            color,
            user_width,
            user_height,
            change_size=False,
        )
        filled_circle(
            img,
            (y + S[0], x + S[1]),
            thickness / 2,
            color,
            user_width,
            user_height,
            change_size=False,
        )
        filled_circle(
            img,
            (y + S[0], -x + S[1]),
            thickness / 2,
            color,
            user_width,
            user_height,
            change_size=False,
        )
        filled_circle(
            img,
            (x + S[0], -y + S[1]),
            thickness / 2,
            color,
            user_width,
            user_height,
            change_size=False,
        )
        filled_circle(
            img,
            (-x + S[0], -y + S[1]),
            thickness / 2,
            color,
            user_width,
            user_height,
            change_size=False,
        )
        filled_circle(
            img,
            (-y + S[0], -x + S[1]),
            thickness / 2,
            color,
            user_width,
            user_height,
            change_size=False,
        )
        filled_circle(
            img,
            (-y + S[0], x + S[1]),
            thickness / 2,
            color,
            user_width,
            user_height,
            change_size=False,
        )
        filled_circle(
            img,
            (-x + S[0], y + S[1]),
            thickness / 2,
            color,
            user_width,
            user_height,
            change_size=False,
        )


def rect(img, A, width_r, height_r, thickness, color, user_width, user_height, change_size):
    B = (A[0] + width_r, A[1] + height_r)
    width, height = img.size
    if change_size:
        A, B = convert_point(width, height, user_width, user_height, A), convert_point(
            width, height, user_width, user_height, B
        )
    thick_line(
        img, A, (B[0], A[1]), thickness, color, user_width, user_height, change_size=False
    )
    thick_line(
        img, A, (A[0], B[1]), thickness, color, user_width, user_height, change_size=False
    )
    thick_line(
        img, B, (B[0], A[1]), thickness, color, user_width, user_height, change_size=False
    )
    thick_line(
        img, B, (A[0], B[1]), thickness, color, user_width, user_height, change_size=False
    )


def filled_rect(img, A, width_r, height_r, color, user_width, user_height, change_size):
    width, height = img.size
    B = (A[0] + width_r, A[1] + height_r)
    if change_size:
        A, B = convert_point(width, height, user_width, user_height, A), convert_point(
            width, height, user_width, user_height, B
        )
    color = hexColor(color)
    for x in range(A[0], B[0] + 1):
        for y in range(A[1], B[1] + 1):
            if vnutri(x, y, img):
                img.putpixel((x, y), color)


def getY(point):
    return point[1]


def filled_triangle(img, A, B, C, color, user_width, user_height, change_size):
    width, height = img.size
    if change_size:
        A, B, C = (
            convert_point(width, height, user_width, user_height, A),
            convert_point(width, height, user_width, user_height, B),
            convert_point(width, height, user_width, user_height, C),
        )
    V = sorted([A, B, C], key=getY)
    left = linePixels(V[0], V[1]) + linePixels(V[1], V[2])
    right = linePixels(V[0], V[2])

    Xmax = max(A[0], B[0], C[0])
    Xmin = min(A[0], B[0], C[0])

    if V[1][0] == Xmax:
        left, right = right, left

    for y in range(getY(V[0]), getY(V[2]) + 1):
        x1 = Xmax
        for X in left:
            if X[1] == y and X[0] < x1:
                x1 = X[0]

        x2 = Xmin
        for X in right:
            if X[1] == y and X[0] > x2:
                x2 = X[0]

        if x2 < 0:
            continue
        if x2 > img.width:
            x2 = img.width - 1
        if x1 < 0:
            x1 = 0
        line(img, (x1, y), (x2, y), color)


def triangle(img, A, B, C, thickness, color, user_width, user_height, change_size):
    width, height = img.size
    if change_size:
        A, B, C = (
            convert_point(width, height, user_width, user_height, A),
            convert_point(width, height, user_width, user_height, B),
            convert_point(width, height, user_width, user_height, C),
        )
    thick_line(img, A, B, thickness, color, user_width, user_height, change_size=False)
    thick_line(img, B, C, thickness, color, user_width, user_height, change_size=False)
    thick_line(img, C, A, thickness, color, user_width, user_height, change_size=False)
