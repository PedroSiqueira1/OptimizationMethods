from functions import grad_rosenbrock
from generate_gif import  generate_rosenbrock_gif
from methods import gradient_method


def rosenbrock(method,initial_point_1, initial_point_2, alpha, theta, itermax):

    if method == "gradient":
        data_points_1, iterations_1 = gradient_method(grad_rosenbrock,0.001,[0,0], 0.000001, 10000)
        data_points_2, iterations_2 = gradient_method(grad_rosenbrock,0.001,[2,2], 0.000001, 10000)


        print("Minimun found at x = ", str(data_points_1[-1][0]), " y = ", str(data_points_1[-1][1]) + " in ", iterations_1, " iterations")
        print("Minimun found at x = ", str(data_points_2[-1][0]), " y = ", str(data_points_2[-1][1]) + " in ", iterations_2, " iterations")

        generate_rosenbrock_gif(data_points_1, initial_point_1, data_points_2, initial_point_2)

        return data_points_1[-1], data_points_2[-1]