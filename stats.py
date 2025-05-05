import string
fulldeck = []
a = (string.ascii_lowercase+"æâêëô")
for i in range(0,len(a)):
	fulldeck.append(a[i])
the_main_dic = {}

def nmwrd(x):
	y = x.split()
	return(len(y))

def full_stat(x):
	x = x.lower()
	for i in fulldeck:
		the_main_dic[f"{i}"] = x.count(i)
	return(the_main_dic)	




