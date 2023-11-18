# def prime_checker(num):
#     is_prime = True
#     for x in range(2, num):
#         result = num % x
#         if result == 0:
#             is_prime = False
#     if is_prime:
#         print("prime number")
#     else:
#         print("not a prime")


# prime_checker(6)
# prime_checker(5)


def prime_checker(num):
    for x in range(2, num):
        if num % x == 0:
            return "Not prime"
        else:
            return "prime"


print(prime_checker(6))
print(prime_checker(5))
print(prime_checker(53))
