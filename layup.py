from time import time
from rich import print
from argparse import ArgumentParser

import matplotlib.pyplot as plt


def layup_sequence(n: int) -> int:
    """Compute the value of the layup sequence at n"""

    memo: dict[int, int] = {1: 1, 2: 2}

    # base case
    match n:
        case 1:
            return memo[1]
        case 2:
            return memo[2]

    # recursive step (bottom up - iterative)
    for i in range(3, n + 1):
        match i % 2:
            case 0:
                memo[i] = memo[i - 1] + memo[i - 2]

            case 1:
                memo[i] = 2 * memo[i - 1] - memo[i - 2]

    return memo[n]


def plot(n: int) -> None:
    n_range: list[int] = [_ for _ in range(1, n + 1, 2)]
    runtimes: list[float] = []
    for j in n_range:
        start = time()
        layup_sequence(j)
        stop = time()
        runtimes.append(stop - start)

    _, ax = plt.subplots()
    ax.plot(n_range, runtimes, color="teal")
    ax.set_xlabel("N")
    ax.set_ylabel("Runtime (seconds)")
    ax.set_title("Runtime (seconds) over N")
    plt.show()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--plot", type=bool, default=False)

    args = parser.parse_args()

    n: int = 10_000
    start: float = time()
    value: int = layup_sequence(n=n)
    formatted_val: str = str(value)[:5] + "..." + str(value)[-5:]
    stop: float = time()

    print(f"n: {n} | Value: {formatted_val}")
    print(f"Runtime: {stop-start:0.5f} seconds")

    if args.plot:
        plot(n)
