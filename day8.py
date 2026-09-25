students={'姓名':'李秋果','年龄':'18','专业':'计算机科学'}
for k,v in students.items():
    print(f'{k}->{v}')
#
name = {1: '石头', 2: '剪刀', 3: '布'}
import random
computer=random.randint(1,3)
print(f'电脑出的是：{name[computer]}')
#
text='abracadabra'
counts={}
for c in text:
    if c in counts:
        counts[c]+=1
    else:
        counts[c]=1
print(counts)
text2='hello,world,gays'
counts2={}
for c in text2:
    counts2[c]=counts2.get(c,0)+1
print(counts2)
#
dict1={'鲁明凤':'豆包','李秋果':'gpt','xxx':'无'}
print(dict1)
dict1['zxr']='sb'
print(dict1)
dict1['鲁明凤']='gpt'
print(dict1)
del dict1['xxx']
print(dict1)
#
student2={'姓名':'鲁明凤','年龄':'19'}
#print([student2'[成绩'])#SyntaxError: invalid syntax
print(student2.get('成绩',0))
#
total_nums=0
total_score=0
scores = {'小明': 90, '小红': 85, '小刚': 77}
max_score=scores['小明']
max_score_name='小明'
for k,v in scores.items():
    total_score+=v
    total_nums+=1
    if max_score<v:
        max_score_name=k
        max_score=v
print(f'总人数：{total_nums}，总分：{total_score}，平均分：{total_score/total_nums:.2f}，最高分是：{max_score_name}')
#
text3 = 'the cat sat on the mat the end'
counts3={}
word=text3.split()
for c in word:
    counts3[c]=counts3.get(c,0)+1
print(counts3)
