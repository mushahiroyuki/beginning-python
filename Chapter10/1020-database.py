#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
# ファイル名 Chapter10/1020-database.py

import sys, shelve

def store_person(db):
    """
    ユーザーにデータを問い合わせ、得られたデータをshelfオブジェクトに保存する
    """
    pid = input('ID番号: ')
    person = {}
    person['name'] = input('名前: ')
    person['age'] = input('年齢: ')
    person['phone'] = input('電話番号: ')
    db[pid] = person

def lookup_person(db):
    """
    ユーザーにIDと取得したいフィールドを問い合わせ、該当するデータをshelfオブジェクトから取得する
    """
    pid = input('ID: ')
    field = input('どの項目を知りたいですか? name（名前）、age（年齢）、phone（電話番号）のいずれかを指定してください: ')
    field = field.strip().lower()
    print(field.capitalize() + ':', db[pid][field])

def print_help():
    print('使用可能なコマンド:')
    print('store  : 人についての情報を保存する')
    print('lookup : IDにより人を探す')

    print('quit   : 変更を保存して終了する')
    print('?      : このメッセージを出力する')

def enter_command():
    cmd = input('コマンドを入力してください（? でヘルプ表示）: ')
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open('database.dat') # ファイル名は適宜変更
    try:
        while True:
            cmd = enter_command()
            if  cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()

if __name__ == '__main__': main()
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
