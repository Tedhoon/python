def main():
    symbols = input()
    symlist = symbols.split(' ')
    for i in range(len(symlist)-1):
        print(symlist[0]*int(symlist[i+1]))
        try:
            symlist[i+2]=int(symlist[i+1])+int(symlist[i+2])
        except:
            pass

main()
