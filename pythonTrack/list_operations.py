if __name__ == '__main__':
    N = int(input())
    List = []
    for _ in range(N):
        command = input()
        if command == "print":
            print(List)
        elif command == "sort":
            List.sort()
        elif command == "pop":
            List.pop()
        elif command == "reverse":
            List.reverse()
        else:
            command = list(command.split())
            if command[0] == "remove":
                List.remove(int(command[1]))
            elif command[0] == "append":
                List.append(int(command[1]))
            elif command[0] == "insert":
                List.insert(int(command[1]), int(command[2]))
            
