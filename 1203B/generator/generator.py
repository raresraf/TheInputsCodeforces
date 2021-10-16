import numpy as np
import random
import string

if __name__ == '__main__':
	test_cases = np.linspace(1, 500, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			q = int(test_case)
			f.write(f"{q}\n")
			for i in range(1, q + 1):
				n = np.random.randint(1, 2 + int(i / 5))
				f.write(f"{n}\n")
				for j in range(1, n + 1):
					f.write(f"{np.random.randint(1,1000)} {np.random.randint(1,1000)} {np.random.randint(1,1000)} {np.random.randint(1,1000)} ")
				f.write(f"\n")


