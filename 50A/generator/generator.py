import numpy as np
import random
import string

if __name__ == '__main__':
	test_cases = np.linspace(1, 256, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			n = int(test_case)
			x = int(n / 16)
			if x == 0:
				x = 1
			y = int(n / x)
			f.write(f"{x} {y}\n")
			


