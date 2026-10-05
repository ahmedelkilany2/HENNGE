# Fourth-Power Sum

A Python solution for the test-case problem described in the mission.

## What it does

For each test case, the program checks whether the input line contains exactly the declared number of integers. If the count differs, it outputs `-1`. Otherwise, it sums the fourth powers of all values that are zero or negative, skipping positive values.

## Input format

- The first line contains the number of test cases, `N`.
- For each test case, one line contains `X`, the expected number of values.
- The next line contains the space-separated values for that test case.

## Run

Save the solution as `main.py`, then run:

```sh
python main.py < input.txt
```

The program reads all input before printing results. It prints one result per test case with no blank lines between them.
