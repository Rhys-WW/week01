#1
score=int(input('输入一个分数：'))
if score>100 or score<0:
    print('输入错误，重新输入')
    score = int(input('输入一个分数：'))
if score >=90:
    print('优秀')
elif score >=80:
    print('良好')
elif score>=70:
    print('中等')
elif score>=60:
    print('及格')
else:
    print('不及格')
#2
height=float(input('输入身高(m)：'))
weight=float(input('输入体重(kg)：'))
BMI=weight/(height*height)
print(f'BMI为:{BMI:.2f}')
if BMI<=0:
    print('输入错误')
elif BMI<18.5:
    print('偏瘦，该多吃一点了')
elif BMI <24:
    print('正常,保持好哦')
elif BMI <28:
    print('偏胖，该少吃一点了')
else:
    print('肥胖，别吃了，减肥')
#3
import random
answer=random.randint(1,100)
guess=int(input('猜一个数：'))
if guess>answer:
    print('猜大了')
elif guess<answer:
    print('猜小了')
else:
    print('正确！！！')

