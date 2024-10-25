# Task 1

def cek_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def foo_bar_program():
    result = []
    for num in range(100, 0, -1):
        if cek_prima(num):
            continue
        if num % 3 == 0 and num % 5 == 0:
            result.append("FooBar")
        elif num % 3 == 0:
            result.append("Foo")
        elif num % 5 == 0:
            result.append("Bar")
        else:
            result.append(str(num))
    return " ".join(result)

print(foo_bar_program())
