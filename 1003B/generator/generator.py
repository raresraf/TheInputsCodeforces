import numpy as np
import random
import string

if __name__ == '__main__':
	test_cases = np.linspace(1, 100, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			n = int(test_case)
			a = np.random.randint(int(n/2), n + 1)
			b = np.random.randint(int(n/2), n + 1)
			x = np.random.randint(1, a + b + 1)
			f.write(f"{a} {b} {x}\n")


