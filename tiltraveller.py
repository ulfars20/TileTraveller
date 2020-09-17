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
    elif x == 1 and y == 3:
        return False
    else: 
        return True

def west(x, y):
    if x != 1 and y >= x:
        return True
    else:
        return False 

x = 1
y = 1

while True:
    print('You can travel: ', end='')
    n = north(x, y)
    e = east(x, y)
    s = south(x, y)
    w = west(x, y)
    
    if n == True:
        print('(N)orth', end='')
    if e == True:
        print('(E)ast', end='')
    if s == True:
        print('(S)outh', end='')
    if w == True:
        print('(W)est', end='')
    print()
    direction = input('Direction:')
    direction = direction.lower()
    if direction == 'n' or direction == 'e' or direction == 's' or direction == 'w':
        if direction == 'n':
            y += 1
        if direction == 'e':
            x += 1
        if direction == 's':
            y -= 1
        if direction == 'w':
            x -= 1
        
    else:
        print('Not a valid direction')
    print(f'{x} {y}')


