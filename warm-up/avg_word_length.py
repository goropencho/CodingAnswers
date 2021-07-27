def avg_word_length(string):
    for i in ".?!,';":
        string.replace(i,"")
    
    words = string.split()
    return round(sum(len(word) for word in words)/len(words),2)



if __name__ == "__main__":
    string = input()
    print(avg_word_length(string))