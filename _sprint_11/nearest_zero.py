# UPD_Context_ID = 68152437

from typing import List


def nearest_zero(length: int, num_street: List[int]) -> List[int]:
    pos_zero: List[int] = [
        index for index, value in enumerate(num_street) if value == 0
    ]
    for index in range(pos_zero[0]):
        num_street[index] = pos_zero[0] - index
    for zero in range(len(pos_zero) - 1):
        for index in range(pos_zero[zero] + 1, pos_zero[zero + 1]):
            num_street[index] = min(
                index - pos_zero[zero],
                pos_zero[zero + 1] - index
            )
    for index in range(pos_zero[-1] + 1, len(num_street)):
        num_street[index] = index - pos_zero[-1]
    return num_street


def main() -> None:
    length: int = int(input())
    num_street: List[int] = list(map(int, input().split()))
    result = nearest_zero(length, num_street)
    print(*result)


if __name__ == '__main__':
    main()
