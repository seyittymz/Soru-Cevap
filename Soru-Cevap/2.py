def fibonacci():
    a = 0
    b = 1
    total = 0
    while b < 5000000:
        if b % 3 == 0:
            total += b
        a , b = b , a + b
    print( total)



fibonacci()

