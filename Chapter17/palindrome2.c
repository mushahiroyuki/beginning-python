//ファイル名 palindrome2.c（listing17-6.c）
#include <Python.h>

static PyObject *is_palindrome(PyObject *self, PyObject *args) {
    int i, n;
    const char *text;
    int result;
    /* "s" は単一の文字列を意味する */
    if (!PyArg_ParseTuple(args, "s", &text)) {
        return NULL;
    }
    /* 以前のコードと基本的に同じ */
    n=strlen(text);
    result = 1;
    for (i = 0; i <= n/2; ++i) {
        if (text[i] != text[n-i-1]) {
            result = 0;
            break;
        }
    }
    /* "i"は単一の整数を意味する */
    return Py_BuildValue("i", result);
}

/* メソッド/関数のリスト */
static PyMethodDef PalindromeMethods[] = {

    /* 名前, 関数, 引数の型, docstring */
    {"is_palindrome", is_palindrome, METH_VARARGS, "Detect palindromes"},
    /* リストの終わりの目印 */
    {NULL, NULL, 0, NULL}

};

static struct PyModuleDef palindrome =
{
    PyModuleDef_HEAD_INIT,
    "palindrome", /* モジュール名 */
    "",           /* docstring（ドキュメンテーション文字列） */
    -1,           /* 大域変数に保持されるシグナルの状態 */
    PalindromeMethods
};

/* モジュールの初期化関数 */
PyMODINIT_FUNC PyInit_palindrome(void)
{
    return PyModule_Create(&palindrome); 
}
