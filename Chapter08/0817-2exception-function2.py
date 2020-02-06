#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter08/0817-2exception-function2.py
def faulty():
    raise Exception('例外が発生しました')

def ignore_exception():
    faulty()

def handle_exception():
    try:
        faulty()
    except:
        print('例外が処理されました')
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行        
ignore_exception() #←下記のエラー#
#Traceback (most recent call last):
#  File "0817-2exception-function2.py", line 17, in <module>
#    ignore_exception() #←下記のエラー
#  File "0817-2exception-function2.py", line 7, in ignore_exception
#    faulty()
#  File "0817-2exception-function2.py", line 4, in faulty
#    raise Exception('例外が発生しました')
#Exception: 例外が発生しました
