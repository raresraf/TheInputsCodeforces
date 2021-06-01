import numpy as np
import random
import string

if __name__ == '__main__':
	test_cases = np.linspace(1, 50, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			f.write(f"{int(test_case)} {np.random.randint(1, 50)}\n")
			l = np.random.randint(1, 50)
			f.write(f"{int(l)} ")
			for x in range(int(test_case) - 1):
				l = l - np.random.randint(0, 2)
				if l < 0:
					l = 0
				f.write(f"{int(l)} ")
