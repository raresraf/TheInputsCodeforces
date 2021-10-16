import numpy as np
import random
import string

def max(a, b):
	if a > b:
		return a
	return b

if __name__ == '__main__':
	test_cases = np.linspace(1, 10000000, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			n = int(test_case)
			f.write(f"{random.randint(n - random.randint(1, 1999),n)}\n")
			f.write(f"{random.randint(max(0, n - random.randint(1, n)),n)}\n")
			f.write(f"{random.randint(max(0, n - random.randint(1, n)),n)}\n")



