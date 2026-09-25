import random
computer=random.randint(1,3)
guess=int(input('输入1-3（1是石头，2是剪刀，3是布）：'))
if guess-computer==0:
    print('平局')
elif guess-computer==-2 or guess-computer==1:
    print('电脑赢')
else:
    print('玩家赢')