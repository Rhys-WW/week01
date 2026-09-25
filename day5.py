# 猜数字游戏 v2
# 玩法：选难度 → 有限次数内猜中电脑生成的随机数
# 难点：三层循环（重玩 / 次数 / 输入校验），break 只跳出最内层
# 日期：2026.09.16
import random
while True:
    print('1. 简单（1~10，3 次机会）')
    print('2. 普通（1~50，5 次机会）')
    print('3. 困难（1~100，7 次机会）')
    while True:
        try:
            DifficultyLevel = int(input('请输入 1/2/3：'))
        except ValueError:
            print('请输入数字！')
            continue
        break
    if DifficultyLevel==1:
        remaining=3
        low=1
        high=10
    elif DifficultyLevel==2:
        remaining=5
        low = 1
        high = 50
    elif DifficultyLevel==3:
        remaining=7
        low = 1
        high = 100
    else:
        print('等级选择错误哦，重新选择')
        continue
    answer = random.randint(low, high)
    used=0
    while remaining > 0:
        while True:
            try:
                num = int(input(f'请猜一个数字（{low}-{high}）：'))
            except ValueError:
                print('请输入数字！')
                continue
            if num < low or num > high:
                print(f'输入范围错误哦，请重新输入正确范围数字（{low}-{high}）：')
                continue
            break
        used+=1
        if answer == num:
            print(f'正确！！！,在{used}次猜中')
            break
        remaining -= 1
        if remaining == 0:
            print(f'次数用完了，答案是 {answer}')
        elif num < answer:
            print(f'太小了，还剩 {remaining} 次机会')
        else:
            print(f'太大了，还剩 {remaining} 次机会')
    again=input('再来一局吗？（y/n）：')
    if again != 'y' :
        break