#循环练习
#                for i in range(1,6):
#                    print(i)
#                for i in range(5,0,-1):
#                     print(i)
#                num=0
#                for i in range(1,101):
#                    num+=i
#                print(num)
#                total=0
#                for i in range(1,101):
#                   total+=i
#                print(total)
#                num_l=0
#                text='hello world'
#                for i in range(0,len(text)):
#                    if(text[i]=='l'):
#                        num_l+=1
#                print(num_l)
#                names = ['小明', '小红', '小刚']
#                 for i in range(0,len(names)):
#                     print(f'第{i+1}名：{names[i]}')
#                for i,name in enumerate(['小明', '小红', '小刚']):
#                    print(f'第{i+1}名，',name)
#1
friend_names=['鲁明凤','陈xx','李xx']
for i in range(3):
    print(f'你好，{friend_names[i]}')
#2
nums=[]
total_num=0
for i in range(5):
    num=float(input(f'第{i+1}次请输入数字(共5次)：'))
    max=num
    min=num
    nums.append(num)
for i in range(5):
    total_num+=nums[i]
    if nums[i]>=max:
        max=nums[i]
    elif nums[i]<=min:
        min=nums[i]
print(f'总和：{total_num}')
print(f'最大值：{max}')
print(f'最小值：{min}')
print(f'平均值：{total_num/5:.2f}')
#3
#（1）
for i in range(5):
    print(nums[4-i])
#(2)
print(nums[::-1])


