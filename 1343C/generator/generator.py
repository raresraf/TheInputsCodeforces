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
				n = np.random.randint(1, 2 * t)
				f.write(f"{n}\n")
				for j in range(1, n):
					p = np.random.randint(-100000000, 100000000)
					f.write(f"{p} ")
				f.write(f"\n")

