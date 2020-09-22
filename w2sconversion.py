
def word_2_2Dbyte(x):
	c = (int(x) >> 8) & 0xff
	b = int(x) & 0xff
	return b,c

def word2string(v):
	conv = [word_2_2Dbyte(i) for i in v]
	b = [j for s in conv for j in s]
	ch = [chr(l) for l in b]
	# return ch
	st = ''
	for k in ch:
		st += k
	# st = list(map(lambda chrs: chrs[0], ch))
	return st

lst = ['16722','19274','19797','21057']
str1 = word2string(lst)
print(str1)
a = [i for i in range(6)]
a.

