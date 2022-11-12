list=[1,3,4,7,8,1]
list1=[list[i] for i in range(len(list)) if list[i]!=min(list)]
x=min(list1)
