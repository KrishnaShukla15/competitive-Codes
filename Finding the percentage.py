if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in range(len(student_marks)):
        if query_name in student_marks:
            x = student_marks[query_name]
    y=sum(x)/len(x)
    print(format(y,".2f")) 