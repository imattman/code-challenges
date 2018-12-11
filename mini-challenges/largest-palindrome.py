#!/usr/bin/env python3

def main():
    found = []
    for i in range(999, 0, -1):
        for j in range(999, 0, -1):
            product = i * j
            if str(product) == str(product)[::-1]:
                found.append((product, i, j))
                break
    found.sort(reverse=True)
    found = found[:10]

    for pair in found:
        print(pair)


if __name__ == "__main__":
    main()
