def himmelblau(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

def rosenbrock(x, n):
    return sum(100*(x[i+1] - x[i]**2)**2 + (1 - x[i])**2 for i in range(n-1))

def grad_himmelblau(x):
    return [4*x[0]**3+4*x[0]*x[1]-42*x[0]+2*x[1]**2-14,
            4*x[1]**3+4*x[0]*x[1]-26*x[1]+2*x[0]**2-22]

def first_grad_rosenbrock(x):
    return 400*x[0]**3 + 2*x[0] - 400*x[1]*x[0] - 2

def last_grad_rosenbrock(x):
    return 200*x[-1] - 200*x[-2]**2

def middle_grad_rosenbrock(x,i):
    return 400*x[i]**3 + 202*x[i] - 400*x[i+1]*x[i] - 200*x[i-1]**2 - 2

def grad_rosenbrock(x,n):
    
    grad = []

    if n == 1:
        return IndexError 
    if n == 2:
        grad.append(first_grad_rosenbrock(x))
        grad.append(last_grad_rosenbrock(x))
        return grad
    else:
        grad.append(first_grad_rosenbrock(x))
        
        for i in range(1,n-1):
            grad.append(middle_grad_rosenbrock(x,i))  

        grad.append(last_grad_rosenbrock(x))
    
    return grad


