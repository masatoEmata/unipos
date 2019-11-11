import emoji
import re

class FormatText:
    def __init__(self,str):
        self.str = str
    def mySubstrings(self):
        text = ''.join(c for c in self.str if c not in emoji.UNICODE_EMOJI)#絵文字
        #text=re.sub(r'[!-~]', "", text)#半角記号,数字,英字
        #text=re.sub(r'[︰-＠]', "", text)#全角記号
        text=re.sub('\n', " ", text)#改行文字
        return text

# https://hacknote.jp/archives/19937/
# https://qiita.com/yoshimo123/items/85331d881aed9ad41020
