import numpy as np
import random
import string

def max(a, b):
	if a > b:
		return a
	return b

if __name__ == '__main__':
	test_cases = np.linspace(1, 100, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			t = int(test_case)
			f.write(f"{t}\n")
			for i in range(1, t + 1):
				n = random.randint(1, i)
				m = random.randint(1, i)
				f.write(f"{n} {m}\n")
				for i in range(1, 2 * n + 1):
					f.write(f"{random.randint(1, i)} {random.randint(1, i)}\n")
