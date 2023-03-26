def palindrome(start_min_number,start_max_number):
    max_palindrome = 0
    for i in range(start_min_number, start_max_number):
        for  x in range(i, start_max_number):
            if str(i * x) == str(i * x)[::-1] and (i * x) > max_palindrome:
                max_palindrome = (i * x)
                
    print(max_palindrome)
    
    
    
palindrome(100,1000)


