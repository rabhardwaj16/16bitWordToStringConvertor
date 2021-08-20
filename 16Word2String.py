
def word_2_2Dbyte(x):
    c = (int(x) >> 8) & 0xff
    b = int(x) & 0xff
    return b,c

def word2string(l):
    byte_list_2d = [word_2_2Dbyte(i) for i in l]
    b = [j for s in byte_list_2d for j in s]
    chr_list = [chr(l) for l in b]
    # return ch
    st = ''
    for k in chr_list:
        st += k

    return st


lst = ['18498','21057','22340','19009']
var = word2string(lst)
print(var)