name = input('May I have your name? ')
if name.endswith('Potter'):
    if name.startswith('Mr.'):
        print('Hello, Mr. Potter!')
    elif name.startswith('Mrs.'):
        print('Hello, Mrs. Potter!')
    else:
        print('Hello, Potter!')
else:
    print('Hello, stranger.')  # 知らない人
