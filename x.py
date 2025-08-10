def print_star_pyramid_python():
    stars = 5 
    spaces = 0  
    
    while stars > 0:
        
        print(' ' * spaces + '*' * stars)
        stars -= 2  
        spaces += 1  

# Call the function
print_star_pyramid_python()

