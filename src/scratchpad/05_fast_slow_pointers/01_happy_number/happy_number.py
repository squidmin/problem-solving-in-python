def find(num):
    def sum_of_squares(n):
        s = 0
        while n > 0:
            digit = n % 10
            n //= 10
            s += digit ** 2
        return s

    slow = num
    fast = num
    while True:
        slow = sum_of_squares(slow)
        fast = sum_of_squares(sum_of_squares(fast))
        if slow == fast:
            break

    return slow == 1

if __name__ == "__main__":
    print(find(23))
    print(find(12))
