#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter20/rules.py (listing20-5.py)
class Rule:
    """
    すべてのルールの基底クラス
    """
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
class HeadingRule(Rule):
    """
    見出しとは、最長70文字で、最後の文字が「:」でも「.」でも「。」でもない単一の行。
    """
    type = 'heading'
    def condition(self, block):
        return not '\n' in block and len(block) <= 70 and not (block[-1] == ':'  or block[-1] == '.' or block[-1] == '。')
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list3)  # ←この行は無視してください。本文に引用するためのものです。
class TitleRule(HeadingRule):
    """
    表題とは、文書の最初のブロックで、かつ見出しであるもの。
    """
    type = 'title'
    first = True
    def condition(self, block):
        if not self.first: return False
        self.first = False
        return HeadingRule.condition(self, block)
#@@range_end(list3)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list4)  # ←この行は無視してください。本文に引用するためのものです。
class ListItemRule(Rule):
    """
    リスト項目とは、「-」で始まるブロック。
    書式付け処理の一環として、「-」は削除する。
    """
    type = 'listitem'
    def condition(self, block):
        return block[0] == '-'
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True
#@@range_end(list4)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list5)  # ←この行は無視してください。本文に引用するためのものです。
class ListRule(ListItemRule):
    """
    リストは、リスト項目ではないブロックとリスト項目の間から始まり、
    連続したリスト項目の最後のものが終わるところまで。
    """
    type = 'list'
    inside = False
    def condition(self, block):
        return True
    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False
#@@range_end(list5)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list6)  # ←この行は無視してください。本文に引用するためのものです。
class ParagraphRule(Rule):
    """
    パラグラフとは単に他のどのルールにも当てはまらないブロック。
    """
    type = 'paragraph'
    def condition(self, block):
        return True
#@@range_end(list6)  # ←この行は無視してください。本文に引用するためのものです。
