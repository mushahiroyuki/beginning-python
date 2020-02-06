#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter08/0817-1exception-function1.py
def faulty():
    raise Exception('例外が発生しました。')

def ignore_exception():
    faulty()

def handle_exception():
    try:
        faulty()
    except:
        print('例外が処理されました。')
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
#実行        
handle_exception() #←「例外が処理されました。」

# ignore_exception()

