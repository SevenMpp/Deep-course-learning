import codecs
import re
import jieba
from collections import Counter
def clean_text(filename): #清洗文本
    data = codecs.open(filename,"r",encoding='utf-8').read()
    k = re.compile(r'\d+')
    result = re.findall("[++$++](.*)[？]",data)
    for context  in result:
        context_ = re.findall('[\u4e00-\u9fa5]',context)
        clear_word = ''.join(context_)
        with codecs.open(r'F:\资料\项目\Lession-01\datasource-master\train.txt\clean.txt.','a+',encoding='utf-8') as f:
            f.write(clear_word +'\n')
    print("finished...")
filename_or= r"F:\资料\项目\Lession-01\datasource-master\train.txt\train.txt" #源文件
#clean_text(filename)
filename_cl =r"F:\资料\项目\Lession-01\datasource-master\train.txt\clean.txt"
with codecs.open(r"F:\资料\项目\Lession-01\datasource-master\train.txt\clean.txt",'r',encoding='utf-8')as f1: #读取清理后的文本
    clean_t=f1.readlines()
def cut(string): #分词
    return list(jieba.cut(string))

Token = []  #存储分词后的文本 方便处理
for i, line in enumerate(clean_t):
    Token+=cut(line)
TOKEN_GRAM = [''.join(Token[i:i+2]) for i in range(len(Token[:-2]))]   #形成2_GRAM词组
words_count = Counter(TOKEN_GRAM) #词频统计
def prob_2(word1,word2):  # 概率计算
     if word1 + word2 in words_count:
         return words_count[word1+word2]
     else:
         return 1 / len(TOKEN_GRAM)
def get_probablity(sentence): #预测概率
    words = cut(sentence)
    sentence_pro = 1
    for i, word in enumerate(words[:-1]):
        _next = words[i + 1]
        probablity = prob_2(word, _next)
        sentence_pro *= probablity
    return sentence_pro
# need_compared = [
#     "今天晚上请你吃大餐，我们一起吃日料 明天晚上请你吃大餐，我们一起吃苹果",
#     "真事一只好看的小猫 真是一只好看的小猫",
#     "今晚我去吃火锅 今晚火锅去吃我",
#     "洋葱奶昔来一杯 养乐多绿来一杯"
# ]
#
# for s in need_compared:
#     s1, s2 = s.split()
#     p1, p2 = get_probablity(s1), get_probablity(s2)
#
#     better = s1 if p1 > p2 else s2
#
#     print('{} is more possible'.format(better))
#     print('-' * 4 + ' {} with probility {}'.format(s1, p1))
#     print('-' * 4 + ' {} with probility {}'.format(s2, p2))
