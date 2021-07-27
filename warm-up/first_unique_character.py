def unique_char_first(string):
    return max(string, key= string.count)




if __name__ == "__main__":
    string = input()
    print(unique_char_first(string))