# こんなことはしないように...
def get_price(object):
    if isinstance(object, tuple):  # 品物がタプルであれば
        return object[1]  # タプルの2番目の要素を返す
    else:
        return magic_network_method(object)  # ネットワーク上で魔法を使う

