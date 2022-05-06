# UPD_CONTEST_ID = 68150108

from typing import List


def sleight_of_hand(time: int, train_num: str, user: int = 2) -> int:
    num_of_occur: List[int] = [
        train_num.count(index) for index in set(train_num) if index.isdigit()
    ]
    count: int = 0
    for index in num_of_occur:
        if 0 < index <= (time * user):
            count += 1
    return count


def main() -> None:
    time: int = int(input())
    train_num: str = input() + input() + input() + input()
    print(sleight_of_hand(time, train_num))


if __name__ == '__main__':
    main()
