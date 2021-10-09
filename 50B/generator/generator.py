import numpy as np
import random
import string

if __name__ == '__main__':
	test_cases = np.linspace(1, 10000, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			n = int(test_case)
			for x in range(n):
				f.write(random.choice(string.ascii_letters))
			


