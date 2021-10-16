import numpy as np
import random
import string

if __name__ == '__main__':
	test_cases = np.linspace(1, 5000, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			n = int(test_case)
			k = np.random.randint(1, n + 1)
			f.write(f"{n} {k}\n")
			for i in range(1, n + 1):
				c = np.random.randint(1, 5000)
				f.write(f"{c} ")
			f.write(f"\n")
