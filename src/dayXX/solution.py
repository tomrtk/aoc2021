from __future__ import annotations

import os.path
import time

import pytest


def load_input() -> list[str]:
    path = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(path) as f:
        data = f.readlines()

    data = [line.strip() for line in data]
    return data


def calculate_solution(s: list[str]) -> int:
    return 1


def main() -> int:
    data = load_input()
    print(f"Input example: {data[0:5]}")

    t0 = time.monotonic_ns()
    solution = calculate_solution(data)
    print(f"Solution: {solution} - Calculated in {time.monotonic_ns() - t0}ns")

    return 0


EKS = ["test"]


@pytest.mark.parametrize(
    "input_example,expected",
    [
        (EKS, 1),
    ],
)
def test(input_example, expected) -> None:
    assert calculate_solution(input_example) == expected


if __name__ == "__main__":
    raise SystemExit(main())
