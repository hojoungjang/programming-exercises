import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    print("SK" if n % 2 == 1 else "CY")
