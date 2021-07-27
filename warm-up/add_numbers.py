def add_numbers(n1,n2):
    return eval(n1)+eval(n2)



if __name__ == "__main__":
    n1,n2 = input().split()
    print(add_numbers(n1,n2))