#定义一个”老师“的语言
you_need_replace_this_with_name_you_give = '''
老师:年龄 职称 姓名 动作 授课门类 
姓名:张三 | 李四 | 王二
年龄:40岁 | 50岁 | 60岁 
职称:教授 | 副教授 | 讲师
动作:教 | 任教 | 玩耍 | 不知道
授课门类:数学 | 哲学 | 经济 | 计算机
'''
#定义一个"学生"的语言
you_need_replace_this_with_name_you_give_1 = '''
学生:年龄 姓名 动作 年级 专业课程
姓名:小二 | 小三 | 小四
年龄:21 | 22 | 23
动作: 学 | 学习 | 打架 | 赌博 
专业课程:数学 | 哲学 | 经济 | 计算机
'''
import random
def creat_grams(garmmmar_str, split = ":", line_split = "\n"):
    grammer = {}
    for line in garmmmar_str.split(line_split):
        if not line.split():
            continue
        exp, smat = line.split(split)
        grammer[exp] = [s.split() for s in smat.split("|")]
    return grammer

def gereate(garm,target):
    if target not in garm:
        return target
    else:
        expended = [gereate(garm,t) for t  in random.choice(garm[target])]
        return ''.join([e for e in expended])

from steamwork_02 import  get_probablity
from itertools import zip_longest
def gereate_n(garm,target,n = 10):
    gen = []
    for i in range(n):
            expended = [gereate(garm,t) for t  in random.choice(garm[target])]
            gen.append(expended)
    return gen
gereate_sentences = ([''.join(f) for f in gereate_n(creat_grams(you_need_replace_this_with_name_you_give),target="老师")])
p = []
for s in gereate_sentences:
    p2 = get_probablity(s)  # 预测句子合理性的分数
    p.append(p2)
h = [(x, y) for x, y in zip_longest(gereate_sentences, p)]
print(sorted(h, key=lambda x: x[0])) #排序
