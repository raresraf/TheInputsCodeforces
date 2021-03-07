import numpy as np

if __name__ == '__main__':
    test_cases = np.linspace(1, 1000, num=50)
    for test_case in test_cases:
        with open(f"../{int(test_case)}.DAT", 'w') as f:
            f.write(f"{int(test_case)}\r\n")
            for _ in range(int(test_case)):
                  f.write(f"{np.random.randint(1, 1000 + 1)} {np.random.randint(1, 1000 + 1)}\r\n")
