#aim: find the minima of f(x,y)

from random import randint, random #random starting point

#################### gradient descent #################
def gradient_descent(domain, lr=0.03) :
    #domain
    x_min, x_max = domain[0][0], domain[0][1]
    y_min, y_max = domain[1][0], domain[1][1]

    #current point p (x,y)
    x = randint(x_min, x_max)
    y = randint(y_min, y_max)
    
    #do while loop
    while True:
        p1 = (x,y) #current point

        x = x - lr*df_by_dx(x)
        y = y - lr*df_by_dy(y)

        p2 = (x,y) #next point

        #condition of do-while loop
        if distance(p1, p2) < pow(10, -6):
            break

    #p2 is minima
    return p2


#returns distance btw 2 points
def distance(p1, p2):
    x1 = p1[0]
    x2 = p2[0]

    y1 = p1[1]
    y2 = p2[1]

    return (x1 - x2)**2 + (y1 - y2)**2



########################## function f(x,y) #################
#cost function
# p = (x,y)
def f(x,y):
    return 3*(x**2) + 4*y**2 - 5*x + 7

def df_by_dx(x) :
    return 6*x - 5  #df/dx

def df_by_dy(y) :
    return 8*y  #df/dy



#################### driver code ###################################
#parameters
domain = ((-100, 100) , (-100, 100)) #((x_min, x_max) , (y_min , y_max))
lr = 0.04

ans = gradient_descent(domain, lr)
x = ans[0]
y = ans[1]

print(ans)
print(f(x,y))
