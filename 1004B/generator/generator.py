import numpy as np
import random
import string

def max(a,b):
	if a > b:
		return a
	return b

if __name__ == '__main__':
	test_cases = np.linspace(1, 1000, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			m = int(test_case)
			n = np.random.randint(0, max(1000, m * 20))
			f.write(f"{n} {m}\n")
			for i in range(1, m+1):
				f.write(f"{np.random.randint(1, n)} {np.random.randint(1, n)}\n")
