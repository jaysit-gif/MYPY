def print_diamond_python():
    
    letters = "ABCDEFGH"

    for i in range(len(letters)):
        
        left = letters[:len(letters)-i]
        

        spaces = " " * (2*i + 1) if i > 0 else ""
        
    
        right = letters[len(letters)-i-1::-1] if i == 0 else letters[len(letters)-i-1::-1]
        
        
        print(left + spaces + right)
    
    
    for i in range(len(letters)-2, -1, -1):
        
        left = letters[:len(letters)-i]
        
        
        spaces = " " * (2*i + 1)
        
    
        right = letters[len(letters)-i-1::-1]
        
        
        print(left + spaces + right)


print_diamond_python()