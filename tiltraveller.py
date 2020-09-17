#def north(x, y)
#def south(x, y)
#def west(x, y)
    # Check if error?
#def east(x, y)

# Set x and y equal to 1 (start)
# Check which direction is available
    # If y > x you can move east?
    # If x is 1 then west is unavailable
    # If x is 3 then east is unavailable
    # If y is 1 then south is unavailable
    # If y is 3 then north is anavailable
# Prompt for a direction
# Error if wrong direction is called
# Call a function based on the input

# If you are in 3, 1 then print Victory



def north(x, y):
    if y==3:
        return False
    elif x == 2 and y == 2:
        return False
    else:
        return True 

def east(x, y):
    if y>x:
        return True
    else:
        return False

def south(x, y):
    if y == 1:
        return False
    elif x == 2 and y == 3:
        return False
    else: 
        return True

def west(x, y):
    if x != 1 and x >= y:
        return True
    else:
        return False 

x = 1, y = 1

    
