from __future__ import annotations

import os.path
import time

import numpy as np
import pytest


def load_input() -> list[int]:
    path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(path) as f:
        data = f.readlines()

    res = [int(line.strip()) for line in data]
    return res


def calculate_solution(s: list[int]) -> int:
    count = 0
    for n in range(1, len(s)):
        if s[n] > s[n-1]:
            count += 1

    return count


def calculate_solution_2(s: list[int]) -> int:
    x = np.array(s)
    count = np.sum(x[1:] > x[:-1])
    return count


def main() -> int:
    data = load_input()
    print(f"Input example: {data[0:5]}")

    t0 = time.monotonic_ns()
    solution = calculate_solution(data)
    print(
        f"Calculated the solution: {solution} in {time.monotonic_ns() - t0}ns",
    )
    t0 = time.monotonic_ns()
    solution = calculate_solution_2(data)
    print(
        f"Calculated the solution: {solution} in {time.monotonic_ns() - t0}ns",
    )

    return 0


EKS = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]


@pytest.mark.parametrize(
    "input_example,expected",
    [
        (EKS, 7),
    ],
)
def test(input_example, expected) -> None:
    assert calculate_solution(input_example) == expected


if __name__ == "__main__":
    raise SystemExit(main())
