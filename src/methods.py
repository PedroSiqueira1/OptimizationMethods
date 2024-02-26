import numpy as np
from functions import grad_himmelblau, grad_rosenbrock

def gradient_method(gradient_function,alpha,x0, theta, itermax):
        data_points = [x0]
        iteration = 0
        x0 = np.array(x0)
        x1 = np.array([1000, 1000])
        while iteration < itermax:
            iteration+=1
            if gradient_function == grad_himmelblau:
                direction = np.array(gradient_function(x0))
            elif gradient_function == grad_rosenbrock:
                direction = np.array(gradient_function(x0,2))
            else:
                raise ValueError("Invalid gradient function")
            x1 = np.array(x0) - direction * alpha
            if  np.linalg.norm(x1 - x0) <= theta:
                return data_points, iteration
            data_points.append(x1)
            x0 = x1
        
        return data_points, iteration
