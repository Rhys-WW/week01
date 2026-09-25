#4
nums_list=[1,4,5,6,7,8,9,0]
Even_numbers=0
for i in range(0,len(nums_list)):
    if nums_list[i]%2==0:
        Even_numbers+=1
print(f'nums_list中有{Even_numbers}个偶数')
#5
nums = [34, 7, 91, 12, 58]
max=nums[0]
for i in range(0,len(nums)):
    if nums[i]>max:
        max=nums[i]
print(max)
#6,使用5的列表
for i in range(0,len(nums)):
    nums[i]=nums[i]+1
    print(nums[i])
#7
toal_list=[]
for i in range(0,len(nums_list)):
    toal_list.append(nums_list[i])
for i in range(0,len(nums)):
    toal_list.append(nums[i])
print(len(toal_list))
