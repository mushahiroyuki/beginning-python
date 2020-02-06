#ファイル名 Chapter06/0617hello3-reverse.py
def hello_3(name='皆さん', greeting='こんにちは'):
    print('{}、{}！'.format(name, greeting))

# 実行    
params = {'name': '次郎さん', 'greeting': 'お久しぶりです'}
hello_3(**params) #←次郎さん、お久しぶりです！
