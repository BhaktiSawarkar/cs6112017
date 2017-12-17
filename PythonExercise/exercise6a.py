def if_prime(a):
    if a == 2:
        return True
    else:
        for x in range(2, a):
            if a % x == 0:
                return False
            else:
                return True


print(is_prime(5))
