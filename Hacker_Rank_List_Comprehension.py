def getting_text():
    """
    The function getting_text downloads a file in which line from first to third contains integers
    x, y, z representing the dimensions of a cuboid and in fourth line is integer n.
    """
    with open('List_Comprehension_data.txt', "r") as text:
        x = int(text.readline())
        y = int(text.readline())
        z = int(text.readline())
        n = int(text.readline())
    return x, y, z, n


def possible_coordinates(a, b, c, d):
    """
    function print a list of all possible coordinates given by (a,b,c)
    on a 3D grid where the sum of a+b+c is not equal to d.
    """
    coordinates_list = [[x, y, z] for x in range(a+1) for y in range(b+1)
                        for z in range(c+1) if x+y+z != d]

    return print(coordinates_list)


i, j, k, n = getting_text()
possible_coordinates(i, j, k, n)