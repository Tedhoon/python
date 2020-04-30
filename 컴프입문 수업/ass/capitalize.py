str = input()

res= []

def init(str):
    tmp_list = str.split(' ')
    capitalize(tmp_list)

def capitalize(tmp_list):
    for i,v in enumerate(tmp_list):
        if len(v)>4:
            tmp = v[0].upper() + v[1::]
            res.append(tmp)
        else:
            res.append(v)

    print((' ').join(res))

if __name__=="__main__":
    init(str)
