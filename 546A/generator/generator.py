import numpy as np
import random
import string

if __name__ == '__main__':
	test_cases = np.linspace(1, 1000000000, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			f.write(f"{np.random.randint(1, 1000)} {np.random.randint(1, 1000)} {int(test_case)}\n")


