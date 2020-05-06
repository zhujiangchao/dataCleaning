import sys

def symbol_counter(line, symbol):
	pass

def main(argv):
	fn = argv[0]
	symbol = argv[1]
	f = open(fn)
	line = f.readline()
	count = 0
	while line:
		count = count + line.count(symbol)
		line = f.readline()
	print("count = ", count)

if __name__ == '__main__':
	main(sys.argv[1:])