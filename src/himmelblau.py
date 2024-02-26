from functions import grad_himmelblau
from generate_gif import generate_himmelblau_gif
from methods import gradient_method


def himmelblau(method,initial_point_1, initial_point_2, alpha, theta, itermax):

    if method == "gradient":

        data_points_1, iterations_1 = gradient_method(grad_himmelblau,alpha,initial_point_1, theta, itermax)
        data_points_2, iterations_2 = gradient_method(grad_himmelblau,alpha,initial_point_2, theta, itermax)

        print("Minimun found at x = ", str(data_points_1[-1][0]), " y = ", str(data_points_1[-1][1]) + " in ", iterations_1, " iterations")
        print("Minimun found at x = ", str(data_points_2[-1][0]), " y = ", str(data_points_2[-1][1]) + " in ", iterations_2, " iterations")

        generate_himmelblau_gif(data_points_1, initial_point_1, data_points_2, initial_point_2)
        
        
        return data_points_1[-1], data_points_2[-1]
        