#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter20/handlers.py (listing20-4.py)
class Handler:
    """
    Parserからのメソッド呼び出しを処理するオブジェクト

    Parserは各ブロックの開始時点で、ブロックに応じた名前を引数として
    start()とend()を呼び出す。sub()メソッドは正規表現の置換に使われる。
    'emphasis'などの名前を引数として呼び出されると、それに応じた置換関数を返す。
    """
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method):
            return method(*args)
    def start(self, name):
        self.callback('start_', name)
    def end(self, name):
        self.callback('end_', name)
    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None: match.group(0)
            return result
        return substitution
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

class HTMLRenderer(Handler):
    """
    HTMLのレンダリング用ハンドラ

    HTMLRendererのメソッドはスーパークラスを通じて利用する。
    ハンドラのメソッドstart()、end()、sub()は、HTML文書で
    使われる基本的なマークアップを行う。
    """
    def start_document(self):
        print('<html><head><title>...</title></head><body>')
    def end_document(self):
        print('</body></html>')
    def start_paragraph(self):
        print('<p>')
    def end_paragraph(self):
        print('</p>')
    def start_heading(self):
        print('<h2>')
    def end_heading(self):
        print('</h2>')
    def start_list(self):
        print('<ul>')
    def end_list(self):
        print('</ul>')
    def start_listitem(self):
        print('<li>')
    def end_listitem(self):
        print('</li>')
    def start_title(self):
        print('<h1>')
    def end_title(self):
        print('</h1>')
    def sub_emphasis(self, match):
        return f'<span style="font-weight: bold;">{match.group(1)}</span>'
#@#     return f'<em>{match.group(1)}</em>'
    def sub_url(self, match):
        return f'<a href="{match.group(1)}">{match.group(1)}</a>'
    def sub_mail(self, match):
        return f'<a href="mailto:{match.group(1)}">{match.group(1)}</a>'
    def feed(self, data):
        print(data)
