#Hackerrank problem Nested Lists
main=[]
sc=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    main.append([name,score])
    sc.append(score)
list1=[sc[i] for i in range(len(sc)) if sc[i]!=min(sc)]

x=min(list1)
list2=[main[i][0] for i in range(len(main)) if main[i][1]==x]
list2.sort()
for j in range(len(list2)):
    print(list2[j])