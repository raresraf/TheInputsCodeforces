import numpy as np
import random
import string

if __name__ == '__main__':
	test_cases = np.linspace(1, 1000, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			f.write(f"{''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(int(test_case)))}\n")

