import jieba
from jieba import analyse
from jieba import posseg
from textrank4zh import TextRank4Keyword, TextRank4Sentence

class Derek_TextRange():
    def __init__(self, words, raw):
        # 停用词列表
        self.words = words
        # 源文本
        self.raw = raw
        self.cut = self.cut()
        #self.property()
        self.keyword()
        self.auto_abstract()

    # 去除停用词
    def remove_words(self, stopwords, wordlist):
        for i in stopwords:
            while i in wordlist:
                wordlist.remove(i)
        return wordlist

    # 分词
    def cut(self):
        cut_words = jieba.cut(raw, cut_all = False)
        wordlist = list(cut_words)
        self.remove_words(words, wordlist)
        return ''.join(wordlist)

    # 显示分词词性
    def property(self):
        prop_word = jieba.posseg.cut(self.cut)
        for a, b in prop_word:
            print('%s -> %s' % (a, b))

    # 提取关键词
    def keyword(self):
        keyword1 = jieba.analyse.textrank(self.cut, topK = 5, withWeight = True)
        keyword2 = jieba.analyse.extract_tags(self.cut, topK = 5, withWeight = True)
        print('Key word for jieba_textrank:')
        for m in keyword1:
            print(m[0], m[1])
        print('\nKey word for jieba_TF-IDF:')
        for n in keyword2:
            print(n[0], n[1])
        print('\nKey word for textrank4zh:')
        keyword3 = TextRank4Keyword()
        keyword3.analyze(text = self.cut, lower = True, window = 2)
        for i in keyword3.get_keywords(5):
            print(i.word, i.weight)

    # 自动生成摘要
    def auto_abstract(self):
        auto_sentence = TextRank4Sentence()
        auto_sentence.analyze(text = self.raw, lower = True)
        print('\nAbstract for textrank4zh:')
        for i in auto_sentence.get_key_sentences(num = 3, sentence_min_len = 10):
            print(i.index, i.weight, i.sentence)

if __name__ == '__main__':
    # 打开读取文件
    with open('C:/Users/Administrator/Desktop/RS/L4Data/textrank/news.txt') as f:
        raw = f.read()
    # 创建停用词列表words
    words = ['，', '。', '《', '》', '\n', ' ', '：','“', '”']
    d_tr = Derek_TextRange(words, raw)
