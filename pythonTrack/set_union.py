English_number = int(input())
English_Student = set(map(int, input().split()))
French_number = int(input())
French_Student = set(map(int, input().split()))

total = English_Student.union(French_Student)
print(len(total))
