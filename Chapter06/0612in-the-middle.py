#ファイル名 Chapter06/0612in-the-middle.py
def in_the_middle(x, *y, z):
    print(x, y, z)

in_the_middle(1, 2, 3, 4, 5, z=7)

in_the_middle(1, 2, 3, 4, 5, 7)
