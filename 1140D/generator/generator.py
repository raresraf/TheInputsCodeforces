import numpy as np
import random
import string

def max(a, b):
	if a > b:
		return a
	return b

if __name__ == '__main__':
	test_cases = np.linspace(3, 500, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			t = int(test_case)
			f.write(f"{t}\n")
