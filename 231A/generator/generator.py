import numpy as np
import random
import string

if __name__ == '__main__':
	test_cases = np.linspace(1, 1000, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			f.write(f"{int(test_case)}\n")
			for x in range(int(test_case)):
				a = np.random.randint(0, 2)
				b = np.random.randint(0, 2)
				c = np.random.randint(0, 2)
				f.write(f"{int(a)} {int(b)} {int(c)}\n")

