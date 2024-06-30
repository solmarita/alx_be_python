size = int(input("Enter the size of the pattern: "))
init = 0

while init != size:
    for i in range(size):
        print("*", end="")
    print("", end="\n")
    init += 1