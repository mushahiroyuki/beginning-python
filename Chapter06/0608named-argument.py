#ファイル名 Chapter06/0608named-argument.py
def  hello_1(greeting, name):
     print(f'{greeting}、{name}!')
#     print('{}、{}!'.format(greeting, name))     
def  hello_2(name, greeting):
     print(f'{greeting}、{name}!')
#         print('{}、{}!'.format(greeting, name))

hello_1("こんにちは", "太郎さん")
hello_2("太郎さん", "こんにちは")

print('-'*20)

hello_1(greeting='こんにちは', name='太郎さん')
hello_1(name='太郎さん', greeting='こんにちは')
hello_2(name='太郎さん', greeting='こんにちは')

