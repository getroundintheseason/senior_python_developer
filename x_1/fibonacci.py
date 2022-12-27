def Fibonacci(index):
	if (index < 1) or not (isinstance(index, int)):
		return "Index of Fibonacci must be integer and greater than 0"

	if index in (1, 2):
		return 1

	return Fibonacci(index-1) + Fibonacci(index-2)

def Permutation(px, y):
	res = 1
	for i in range(1, px+1):
		if i >= (px-y):
			res*=i
	return res

if __name__ == "__main__":
	print(Fibonacci(0.1))
	print(Fibonacci(0))
	print(Fibonacci(1))
	print(Fibonacci(2))
	print("_________________")
	for i in range(1, 11):
		f = Fibonacci(i)
		px = int((f%100)/10)
		y = f%10
		print(f"{i},  {f}, ({px}, {y}),  {Permutation(px, y)}")
