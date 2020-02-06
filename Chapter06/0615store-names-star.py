#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter06/0615store-names-star.py
def store(data, *full_names):
    for full_name in full_names:  # 引数で指定された氏名の各々について実行
        names = full_name.split()  # フルネームをスペースで分割
        if len(names) == 2: names.insert(1, '') # ミドルネームがない場合は、空白を挿入
        labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names): # labelとnameのzipオブジェクト（第5章)
            people = lookup(data, label, name) # いずれかにnameをもつ人がいるか？
            if people: # いる場合
                people.append(full_name)
            else: # いない場合
                data[label][name] = [full_name]

#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data, label, name):
    return data[label].get(name)

#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
#実行
d = {}
init(d)
store(d, 'Han Solo')
store(d, 'Luke Skywalker', 'Anakin Skywalker') #←2人指定
print(lookup(d, 'last', 'Skywalker')) #←['Luke Skywalker', 'Anakin Skywalker']
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
# print(d)
