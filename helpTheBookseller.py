
def stock_list(listOfArt, listOfCat):
    if listOfCat == [] or listOfArt == []:
        return ""
    x = {}
    for i in listOfArt:
        i = i.split()
        if i[0][0] not in x.keys():
            x[i[0][0]] = int(i[1])
        else:
            
            x[i[0][0]] = int(x.get(i[0][0])) + int(i[1])
    
    l = {}
    for i in listOfCat:
        if i in x.keys():
            l[i] = x[i]
        else:
            l[i] = 0
    
    la = []
    i = 0
    while(i<len(listOfCat)):
        la.append('(' + str(listOfCat[i]) + " : " + str(l[listOfCat[i]]) + ")")
        i+=1
    return " - ".join(la)


if __name__ == "__main__":
    n = 3
    l = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] 
    c = ["A", "B", "C", "W"]
    print(stock_list(l,c))