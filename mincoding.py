st1 = input()
st2 = list(input())

def find(x) :
    if x in st1 :
        return x

length = len(st2)
start = 0
maxx = -21e8
while True :
    start += 1
    length -= 1
    for i in range(length) :
        word = ''.join(st2[start:start+i])
        same_word = find(word)
        if same_word is not None :
            if len(same_word) > maxx :
                maxx = len(same_word)
                long_word = same_word
    if start == len(st2)-1 :
        break
print(long_word)



