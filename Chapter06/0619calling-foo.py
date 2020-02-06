#ファイル名 Chapter06/0619calling-foo.py
def foo(x, y, z, m=0, n=0):
    print(x, y, z, m, n)

def call_foo(*args, **kwds):
    print("fooを呼び出す！")
    foo(*args, **kwds)

call_foo(1, 2, 3)
call_foo(1, 2, 3, 4)
call_foo(1, 2, 3, 4, 5)
call_foo(1, 2, 3, 4, 5, 6)
