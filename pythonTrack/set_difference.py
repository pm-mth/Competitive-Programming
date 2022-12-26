# Enter your code here. Read input from STDIN. Print output to STDOUT
English_number = int(input())
English_Student = set(map(int, input().split()))
French_number = int(input())
French_Student = set(map(int, input().split()))

English_only = English_Student.difference(French_Student)
print(len(English_only))
