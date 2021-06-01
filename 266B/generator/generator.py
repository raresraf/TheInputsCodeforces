import numpy as np
import random
import string

if __name__ == '__main__':
	test_cases = np.linspace(1, 50, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			n = int(test_case)
			t = np.random.randint(n - 2, n + 2)
			f.write(f"{n} {t}\n")
			for x in range(int(test_case)):
				l = np.random.randint(0, 2)
				if int(l) == 0:
					f.write(f"G")
				else:
					f.write(f"B")

