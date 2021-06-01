# TheInputsCodeforces
A custom suite of inputs for various CodeForces problems.

The inputs can be generated from sample python scripts(`generator.py`) with respect to the requested input size.

## Sample generator

```
import numpy as np

if __name__ == '__main__':
	test_cases = np.linspace(1, 1000000, num=50)
	for test_case in test_cases:
		with open(f"../{int(test_case)}.DAT", 'w') as f:
			f.write(f"{int(test_case)}")
```

## Contibutions

Contibutions to the TheInputsCodeforces are welcomed.

For any non-existent problem, you can write sample python scripts generators ([example](https://github.com/raresraf/TheInputsCodeforces/blob/master/670A/generator/generator.py)) in the problem specific folder and generate a range of sample inputs for various input size.


## Stats:

- Total Number of synthetic inputs: `$ find . -mindepth 1 -type f -name "*.DAT" -printf x | wc -c`
