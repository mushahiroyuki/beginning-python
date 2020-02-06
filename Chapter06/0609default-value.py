#ファイル名 Chapter06/0609default-value.py
def hello_3(name='皆さん', greeting='こんにちは'):
    print(f'{name}、{greeting}！')
#    print('{}、{}！'.format(name, greeting))    

hello_3()
hello_3('皆様')
hello_3('ご通行中の皆様', 'こんばんは')
