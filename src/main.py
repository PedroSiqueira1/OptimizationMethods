import rosenbrock as rosenbrock
import himmelblau as himmelblau

def main():

    print("Himmelblau")
    minimum_1, minimum_2 = himmelblau.himmelblau("gradient",[5,5],[1,3], 0.001, 0.000001, 10000)

    print("Rosenbrock")
    minimum_1, minimum_2 = rosenbrock.rosenbrock("gradient",[3,1],[1,2], 0.001, 0.000001, 10000)

if __name__ == "__main__":
    main()