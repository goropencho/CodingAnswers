def reverse_integer(x):
    string = str(x)
    if string[0] == "-":
        return int('-'+string[:0:-1])
    return int(str(x)[::-1])



if __name__ == "__main__":
    x = int(input())
    print(reverse_integer(x))