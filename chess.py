import sys
inputfile=open(sys.argv[1],"r")
commands=[line.split() for line in inputfile.readlines()]
inputfile.close()

chessindex = {"a8":"00", "b8":"01", "c8":"02", "d8":"03", "e8":"04", "f8":"05", "g8":"06", "h8":"07",
              "a7":"10", "b7":"11", "c7":"12", "d7":"13", "e7":"14", "f7":"15", "g7":"16", "h7":"17",
              "a6":"20", "b6":"21", "c6":"22", "d6":"23", "e6":"24", "f6":"25", "g6":"26", "h6":"27",
              "a5":"30", "b5":"31", "c5":"32", "d5":"33", "e5":"34", "f5":"35", "g5":"36", "h5":"37",
              "a4":"40", "b4":"41", "c4":"42", "d4":"43", "e4":"44", "f4":"45", "g4":"46", "h4":"47",
              "a3":"50", "b3":"51", "c3":"52", "d3":"53", "e3":"54", "f3":"55", "g3":"56", "h3":"57",
              "a2":"60", "b2":"61", "c2":"62", "d2":"63", "e2":"64", "f2":"65", "g2":"66", "h2":"67",
              "a1":"70", "b1":"71", "c1":"72", "d1":"73", "e1":"74", "f1":"75", "g1":"76", "h1":"77"}

chessboard = [["R1", "N1", "B1", "QU", "KI", "B2", "N2", "R2"],
    ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
    ["r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2"]]

initialize_chessboard = [["R1", "N1", "B1", "QU", "KI", "B2", "N2", "R2"],
    ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
    ["r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2"]]

def write(a):
    print("-------------------------")
    for i in a:
        print(*i)
    print("-------------------------")

def find_index(x):
    for i in chessboard:
        for j in i:
            if j==x:
                n=chessboard.index(i)
                m= i.index(j)
                return n,m

def get_key(val):
    key_list = list(chessindex.keys())
    val_list = list(chessindex.values())
    return (key_list[val_list.index(val)])

def showmoves(x):
    n,m=find_index(x)
    moveslist = []
    if x=="p1" or x=="p2"or x=="p3" or x=="p4" or x=="p5" or x=="p6" or x=="p7" or x=="p8":
        if n>0:
            if (chessboard[n-1][m][0].isupper() or chessboard[n-1][m]=="  ") and chessboard[n-1][m]!="KI":
                a=get_key(str(n-1)+str(m))
                moveslist.append(a)
        return moveslist
    if x=="P1" or x=="P2"or x=="P3" or x=="P4" or x=="P5" or x=="P6" or x=="P7" or x=="P8":
        if n<7:
            if (chessboard[n+1][m][0].islower() or chessboard[n+1][m]=="  ") and chessboard[n+1][m]!="ki":
                a=get_key(str(n+1)+str(m))
                moveslist.append(a)
        return moveslist
    elif x=="r1" or x=="r2":
        while n>0:
            if chessboard[n-1][m]=="  " :
                n-=1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n-1][m][0].isupper() and chessboard[n-1][m]!="KI":
                a=get_key(str(n-1)+str(m))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while n<7:
            if chessboard[n+1][m]=="  ":
                n+=1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n+1][m][0].isupper() and chessboard[n+1][m]!="KI":
                a=get_key(str(n+1)+str(m))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while m<7:
            if chessboard[n][m+1]=="  ":
                m+=1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n][m+1][0].isupper() and chessboard[n][m+1]!="KI":
                a=get_key(str(n)+str(m+1))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while m>0:
            if chessboard[n][m-1]=="  ":
                m-=1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n][m-1][0].isupper() and chessboard[n][m-1]!="KI":
                a=get_key(str(n)+str(m-1))
                moveslist.append(a)
                break
            else:
                break
        return sorted(moveslist)
    elif x=="R1" or x=="R2":
        while n>0:
            if chessboard[n-1][m]=="  " :
                n-=1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n-1][m][0].islower() and chessboard[n-1][m]!="ki":
                a=get_key(str(n-1)+str(m))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while n<7:
            if chessboard[n+1][m]=="  " :
                n+=1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n+1][m][0].islower() and chessboard[n+1][m]!="ki":
                a=get_key(str(n+1)+str(m))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while m<7:
            if chessboard[n][m+1]=="  ":
                m+=1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n][m+1][0].islower() and chessboard[n][m+1]!="ki":
                a=get_key(str(n)+str(m+1))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while m>0:
            if chessboard[n][m-1]=="  ":
                m-=1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n][m-1][0].islower() and chessboard[n][m-1]!="ki":
                a=get_key(str(n)+str(m-1))
                moveslist.append(a)
                break
            else:
                break
        return sorted(moveslist)
    elif x=="b1" or x=="b2":
        while n>0 and m<7:
            if chessboard[n-1][m+1]=="  ":
                n,m=n-1,m+1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n-1][m+1][0].isupper() and chessboard[n-1][m+1]!="KI":
                a=get_key(str(n-1)+str(m+1))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while m>0 and n>0:
            if chessboard[n-1][m-1]=="  ":
                n,m=n-1,m-1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n-1][m-1][0].isupper() and chessboard[n-1][m-1]!="KI":
                a=get_key(str(n-1)+str(m-1))
                moveslist.append(a)
                break
            else:
                break
        return sorted(moveslist)
    elif x=="B1" or x=="B2":
        while n<7 and m<7:
            if chessboard[n+1][m+1]=="  ":
                n,m=n+1,m+1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n+1][m+1][0].islower() and chessboard[n+1][m+1]!="ki":
                a=get_key(str(n+1)+str(m+1))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while m>0 and n<7:
            if chessboard[n+1][m-1]=="  ":
                n,m=n+1,m-1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n+1][m-1][0].islower() and chessboard[n+1][m-1]!="ki":
                a=get_key(str(n+1)+str(m-1))
                moveslist.append(a)
                break
            else:
                break
        return sorted(moveslist)
    elif x=="qu":
        while n>0:
            if chessboard[n-1][m]=="  " :
                n-=1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n-1][m][0].isupper() and chessboard[n-1][m]!="KI":
                a=get_key(str(n-1)+str(m))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while n<7:
            if chessboard[n+1][m]=="  " :
                n+=1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n+1][m][0].isupper() and chessboard[n+1][m]!="KI":
                a=get_key(str(n+1)+str(m))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while m<7:
            if chessboard[n][m+1]=="  ":
                m+=1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n][m+1][0].isupper() and chessboard[n][m+1]!="KI":
                a=get_key(str(n)+str(m+1))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while m>0:
            if chessboard[n][m-1]=="  ":
                m-=1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n][m-1][0].isupper() and chessboard[n][m-1]!="KI":
                a=get_key(str(n)+str(m-1))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while n>0 and m<7:
            if chessboard[n-1][m+1]=="  ":
                n,m=n-1,m+1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n-1][m+1][0].isupper() and chessboard[n-1][m+1]!="KI":
                a=get_key(str(n-1)+str(m+1))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while m>0 and n>0:
            if chessboard[n-1][m-1]=="  ":
                n,m=n-1,m-1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n-1][m-1][0].isupper() and chessboard[n-1][m-1]!="KI":
                a=get_key(str(n-1)+str(m-1))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while n<7 and m<7:
            if chessboard[n+1][m+1]=="  ":
                n,m=n+1,m+1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n+1][m+1][0].isupper() and chessboard[n+1][m+1]!="KI":
                a=get_key(str(n+1)+str(m+1))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while m>0 and n<7:
            if chessboard[n+1][m-1]=="  ":
                n,m=n+1,m-1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n+1][m-1][0].isupper() and chessboard[n+1][m-1]!="KI":
                a=get_key(str(n+1)+str(m-1))
                moveslist.append(a)
                break
            else:
                break
        return sorted(moveslist)
    elif x=="QU":
        while n>0:
            if chessboard[n-1][m]=="  ":
                n-=1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n-1][m][0].islower() and chessboard[n-1][m]!="ki":
                a=get_key(str(n-1)+str(m))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while n<7:
            if chessboard[n+1][m]=="  ":
                n+=1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n+1][m][0].islower() and chessboard[n+1][m]!="ki":
                a=get_key(str(n+1)+str(m))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while m<7:
            if chessboard[n][m+1]=="  ":
                m+=1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n][m+1][0].islower() and chessboard[n][m+1]!="ki":
                a=get_key(str(n)+str(m+1))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while m>0:
            if chessboard[n][m-1]=="  ":
                m-=1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n][m-1][0].islower() and chessboard[n][m-1]!="ki":
                a=get_key(str(n)+str(m-1))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while n>0 and m<7:
            if chessboard[n-1][m+1]=="  ":
                n,m=n-1,m+1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n-1][m+1][0].islower() and chessboard[n-1][m+1]!="ki":
                a=get_key(str(n-1)+str(m+1))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while m>0 and n>0:
            if chessboard[n-1][m-1]=="  ":
                n,m=n-1,m-1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n-1][m-1][0].islower() and chessboard[n-1][m-1]!="ki":
                a=get_key(str(n-1)+str(m-1))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while n<7 and m<7:
            if chessboard[n+1][m+1]=="  ":
                n,m=n+1,m+1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n+1][m+1][0].islower() and chessboard[n+1][m+1]!="ki":
                a=get_key(str(n+1)+str(m+1))
                moveslist.append(a)
                break
            else:
                break
        n,m=find_index(x)
        while m>0 and n<7:
            if chessboard[n+1][m-1]=="  ":
                n,m=n+1,m-1
                a=get_key(str(n)+str(m))
                moveslist.append(a)
            elif chessboard[n+1][m-1][0].islower() and chessboard[n+1][m-1]!="ki":
                a=get_key(str(n+1)+str(m-1))
                moveslist.append(a)
                break
            else:
                break
        return sorted(moveslist)
    elif x=="ki":
        if n<7:
            if (chessboard[n+1][m][0].isupper() or chessboard[n+1][m]=="  ") and chessboard[n+1][m]!="KI":
                a=get_key(str(n+1)+str(m))
                moveslist.append(a)
        if n>0:
            if (chessboard[n-1][m][0].isupper() or chessboard[n-1][m]=="  ") and chessboard[n-1][m]!="KI":
                a=get_key(str(n-1)+str(m))
                moveslist.append(a)
        if m<7:
            if (chessboard[n][m+1][0].isupper() or chessboard[n][m+1]=="  ") and chessboard[n][m+1]!="KI":
                a=get_key(str(n)+str(m+1))
                moveslist.append(a)
        if m>0:
            if (chessboard[n][m-1][0].isupper() or chessboard[n][m-1]=="  ") and chessboard[n][m-1]!="KI":
                a=get_key(str(n)+str(m-1))
                moveslist.append(a)
        if n<7 and m<7:
            if (chessboard[n+1][m+1][0].isupper() or chessboard[n+1][m+1]=="  ") and chessboard[n+1][m+1]!="KI":
                a=get_key(str(n+1)+str(m+1))
                moveslist.append(a)
        if n<7 and m>0:
            if (chessboard[n+1][m-1][0].isupper() or chessboard[n+1][m-1]=="  ") and chessboard[n+1][m-1]!="KI":
                a=get_key(str(n+1)+str(m-1))
                moveslist.append(a)
        if n>0 and m<7:
            if (chessboard[n-1][m+1][0].isupper() or chessboard[n-1][m+1]=="  ") and chessboard[n-1][m+1]!="KI":
                a=get_key(str(n-1)+str(m+1))
                moveslist.append(a)
        if n>0 and m>0:
            if (chessboard[n-1][m-1][0].isupper() or chessboard[n-1][m-1]=="  ") and chessboard[n-1][m-1]!="KI":
                a=get_key(str(n-1)+str(m-1))
                moveslist.append(a)
        return sorted(moveslist)
    elif x=="KI":
        if n<7 :
            if (chessboard[n+1][m][0].islower() or chessboard[n+1][m]=="  ") and chessboard[n+1][m]!="ki":
                a=get_key(str(n+1)+str(m))
                moveslist.append(a)
        if n>0:
            if (chessboard[n-1][m][0].islower() or chessboard[n-1][m]=="  ") and chessboard[n-1][m]!="ki":
                a=get_key(str(n-1)+str(m))
                moveslist.append(a)
        if m<7:
            if (chessboard[n][m+1][0].islower() or chessboard[n][m+1]=="  ") and chessboard[n][m+1]!="ki":
                a=get_key(str(n)+str(m+1))
                moveslist.append(a)
        if m>0:
            if (chessboard[n][m-1][0].islower() or chessboard[n][m-1]=="  ") and chessboard[n][m-1]!="ki":
                a=get_key(str(n)+str(m-1))
                moveslist.append(a)
        if n<7 and m<7:
            if (chessboard[n+1][m+1][0].islower() or chessboard[n+1][m+1]=="  ") and chessboard[n+1][m+1]!="ki":
                a=get_key(str(n+1)+str(m+1))
                moveslist.append(a)
        if n<7 and m>0:
            if (chessboard[n+1][m-1][0].islower() or chessboard[n+1][m-1]=="  ") and chessboard[n+1][m-1]!="ki":
                a=get_key(str(n+1)+str(m-1))
                moveslist.append(a)
        if n>0 and m<7:
            if (chessboard[n-1][m+1][0].islower() or chessboard[n-1][m+1]=="  ") and chessboard[n-1][m+1]!="ki":
                a=get_key(str(n-1)+str(m+1))
                moveslist.append(a)
        if n>0 and m>0:
            if (chessboard[n-1][m-1][0].islower() or chessboard[n-1][m-1]=="  ") and chessboard[n-1][m-1]!="ki":
                a=get_key(str(n-1)+str(m-1))
                moveslist.append(a)
        return sorted(moveslist)
    elif x=="n1" or x=="n2":
        if n>0 and m<7:
            if chessboard[n-1][m+1]=="  ":
                a=get_key(str(n-1)+str(m+1))
                moveslist.append(a)
        if n>1 and m<7:
            if (chessboard[n-2][m+1][0].isupper() or chessboard[n-2][m+1]=="  ") and chessboard[n-2][m+1]!="KI":
                a=get_key(str(n-2)+str(m+1))
                moveslist.append(a)
        if n>0 and m<6:
            if (chessboard[n-1][m+2][0].isupper() or chessboard[n-1][m+2]=="  ") and chessboard[n-1][m+2]!="KI":
                a=get_key(str(n-1)+str(m+2))
                moveslist.append(a)
        if n>0 and m>0:
            if chessboard[n-1][m-1]=="  ":
                a=get_key(str(n-1)+str(m-1))
                moveslist.append(a)
        if n>1 and m>0:
            if (chessboard[n-2][m-1][0].isupper() or chessboard[n-2][m-1]=="  ") and chessboard[n-2][m-1]!="KI":
                a=get_key(str(n-2)+str(m-1))
                moveslist.append(a)
        if n>0 and m>1:
            if (chessboard[n-1][m-2][0].isupper() or chessboard[n-1][m-2]=="  ") and chessboard[n-1][m-2]!="KI":
                a=get_key(str(n-1)+str(m-2))
                moveslist.append(a)
        if n<7 and m<7:
            if chessboard[n+1][m+1]=="  ":
                a=get_key(str(n+1)+str(m+1))
                moveslist.append(a)
        if n<6 and m<7:
            if (chessboard[n+2][m+1][0].isupper() or chessboard[n+2][m+1]=="  ") and chessboard[n+2][m+1]!="KI":
                a=get_key(str(n+2)+str(m+1))
                moveslist.append(a)
        if n<7 and m<6:
            if (chessboard[n+1][m+2][0].isupper() or chessboard[n+1][m+2]=="  ") and chessboard[n+1][m+2]!="KI":
                a=get_key(str(n+1)+str(m+2))
                moveslist.append(a)
        if n<7 and m>0:
            if chessboard[n+1][m-1]=="  ":
                a=get_key(str(n+1)+str(m-1))
                moveslist.append(a)
        if n<6 and m>0:
            if (chessboard[n+2][m-1][0].isupper() or chessboard[n+2][m-1]=="  ") and chessboard[n+2][m-1]!="KI":
                a=get_key(str(n+2)+str(m-1))
                moveslist.append(a)
        if n<7 and m>1:
            if (chessboard[n+1][m-2][0].isupper() or chessboard[n+1][m-2]=="  ") and chessboard[n+1][m-2]!="KI":
                a=get_key(str(n+1)+str(m-2))
                moveslist.append(a)
        return sorted(moveslist)
    elif x=="N1" or x=="N2":
        if n>0 and m<7:
            if chessboard[n-1][m+1]=="  ":
                a=get_key(str(n-1)+str(m+1))
                moveslist.append(a)
        if n>1 and m<7:
            if (chessboard[n-2][m+1][0].islower() or chessboard[n-2][m+1]=="  ") and chessboard[n-2][m+1]!="ki":
                a=get_key(str(n-2)+str(m+1))
                moveslist.append(a)
        if n>0 and m<6:
            if (chessboard[n-1][m+2][0].islower() or chessboard[n-1][m+2]=="  ") and chessboard[n-1][m+2]!="ki":
                a=get_key(str(n-1)+str(m+2))
                moveslist.append(a)
        if n>0 and m>0:
            if chessboard[n-1][m-1]=="  ":
                a=get_key(str(n-1)+str(m-1))
                moveslist.append(a)
        if n>1 and m>0:
            if (chessboard[n-2][m-1][0].islower() or chessboard[n-2][m-1]=="  ") and chessboard[n-2][m-1]!="ki":
                a=get_key(str(n-2)+str(m-1))
                moveslist.append(a)
        if n>0 and m>1:
            if (chessboard[n-1][m-2][0].islower() or chessboard[n-1][m-2]=="  ") and chessboard[n-1][m-2]!="ki":
                a=get_key(str(n-1)+str(m-2))
                moveslist.append(a)
        if n<7 and m<7:
            if chessboard[n+1][m+1]=="  ":
                a=get_key(str(n+1)+str(m+1))
                moveslist.append(a)
        if n<6 and m<7:
            if (chessboard[n+2][m+1][0].islower() or chessboard[n+2][m+1]=="  ") and chessboard[n+2][m+1]!="ki":
                a=get_key(str(n+2)+str(m+1))
                moveslist.append(a)
        if n<7 and m<6:
            if (chessboard[n+1][m+2][0].islower() or chessboard[n+1][m+2]=="  ") and chessboard[n+1][m+2]!="ki":
                a=get_key(str(n+1)+str(m+2))
                moveslist.append(a)
        if n<7 and m>0:
            if chessboard[n+1][m-1]=="  ":
                a=get_key(str(n+1)+str(m-1))
                moveslist.append(a)
        if n<6 and m>0:
            if (chessboard[n+2][m-1][0].islower() or chessboard[n+2][m-1]=="  ") and chessboard[n+2][m-1]!="ki":
                a=get_key(str(n+2)+str(m-1))
                moveslist.append(a)
        if n<7 and m>1:
            if (chessboard[n+1][m-2][0].islower() or chessboard[n+1][m-2]=="  ") and chessboard[n+1][m-2]!="ki":
                a=get_key(str(n+1)+str(m-2))
                moveslist.append(a)
        return sorted(moveslist)

def move(x,y):
    a=showmoves(x)
    n,m=find_index(x)
    if bool(a)==True:
        if y in a:
            print("OK")
            chessboard[n][m]="  "
            k,l=int(chessindex[y][0]),int(chessindex[y][1])
            chessboard[k][l]=x
        else:
            print("FAILED")
    else:
        print("FAILED")

for i in commands:
    print(">",end=" ")
    print(*i)
    if i[0]=="move":
        move(i[1],i[2])
    if i[0]=="print":
        write(chessboard)
    if i[0]=="showmoves":
        a=showmoves(i[1])
        if bool(a)==True:
            print(*a)
        else:
            print("FAILED")
    if i[0]=="initialize":
        print("OK")
        write(initialize_chessboard)
        chessboard = initialize_chessboard.copy()
    if i[0]=="exit":
        exit()
