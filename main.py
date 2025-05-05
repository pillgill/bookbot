import sys
from stats import nmwrd , full_stat

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

path = "./" +sys.argv[1]#input(str(": ")) #"./books/frankenstein.txt"
def get_book_text(path):
	with open(path) as f:
		file_contents = f.read()
		return(str(file_contents))

num = (f"{nmwrd(get_book_text(f"{path}"))}")
	

fldc_unsort = full_stat(get_book_text(f"{path}"))
fldc = dict(sorted(fldc_unsort.items(), key=lambda item: item[1], reverse=True))
	
print(f"""
============ BOOKBOT ============
Analyzing book found at {path}... 
----------- Word Count ----------
Found {num} total words 
--------- Character Count -------""")

for i in fldc:
	print(f"{i}: {fldc[i]}")



print('============= END ===============')