import numpy as np
import random
import string

if __name__ == '__main__':
	test_cases = np.linspace(1, 100000, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			n = int(test_case)
			f.write(f"{n}\n")
			for _ in range(n):
				f.write(f"{random.randint(1,1000000)} {random.randint(1,1000000)}\n")



