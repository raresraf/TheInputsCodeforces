import numpy as np
import random
import string

if __name__ == '__main__':
	test_cases = np.linspace(3, 10000, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			q = int(test_case)
			f.write(f"{q}\n")
			for i in range(1, q + 1):
				c = np.random.randint(0, i)
				m = np.random.randint(0, i)
				x = np.random.randint(0, i)
				f.write(f"{c} {m} {x}\n")
