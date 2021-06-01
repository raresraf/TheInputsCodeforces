import numpy as np
import random
import string

if __name__ == '__main__':
	test_cases = np.linspace(1, 1000, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			f.write(f"{int(test_case)}\n")
			f.write(f"0 10\n")
			for x in range(int(test_case)-2):
				up = np.random.randint(0, 1000)
				down = np.random.randint(0, 1000)
				f.write(f"{up} {down}\n")
			f.write(f"10 0\n")
