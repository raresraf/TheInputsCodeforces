import numpy as np
import random
import string

if __name__ == '__main__':
	test_cases = np.linspace(1, 25, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			pos_i = int((int(test_case) - 1) / 5)
			pos_j = int(test_case) % 5
			for i in range(5):
				for j in range(5):
					if i == pos_i and j == pos_j:
						f.write(f"1 ")
					else:
						f.write(f"0 ")
				f.write(f"\n")
