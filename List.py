if __name__ == '__main__':
    N = int(input())
    l = []
    ops=[]
    for _ in range(N):
        op = input()
        list1 = op.split()
        ops.append(list1)
    for i in range(len(ops)):
        if ops[i][0]=="insert":
            l.insert(int(ops[i][1]),int(ops[i][2]))
        elif ops[i][0]=="print":
            print(l)
        elif ops[i][0] == "remove":
            l.remove(int(ops[i][1]))
        elif ops[i][0]=="append":
            l.append(int(ops[i][1]))
        elif ops[i][0]=="sort":
            l.sort()
        elif ops[i][0]=="pop":
            l.pop()
        elif ops[i][0]=="reverse":
            l.reverse()
