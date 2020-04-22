word = input()
masking = input()

def find_word(word):
    ls = list(word)
    for i,v in enumerate(ls):
        if v in ['a', 'e', 'i', 'o', 'u']:
            ls[i] = masking
    return ls

if __name__=="__main__":
    result = find_word(word)
    print("".join(result))