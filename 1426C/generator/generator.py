import numpy as np
import random
import string

if __name__ == '__main__':
	test_cases = np.linspace(1, 1000, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			t = int(test_case)
			f.write(f"{t}\n")
			for i in range(1, t + 1):
				f.write(f"{np.random.randint(1, 10000 * t)}\n")
