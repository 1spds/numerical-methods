import matplotlib.pyplot as plt     # for plotting functions and convergence behavior
import numpy as np                    # for array handling

# Using SymPy to parse user input and create callable functions for root finding methods
from sympy import symbols
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application
)
from sympy import lambdify
import numpy as np

x = symbols('x')

transformations = standard_transformations + (implicit_multiplication_application,)

from num_methods.roots.bisection import bisection_method
from num_methods.roots.false_position import false_position_method
from num_methods.roots.newton_raphson import newton_raphson_method
from num_methods.roots.secant import secant_method
from num_methods.roots.hybrid_bisec_NR import hybrid_bisection_newton

def main():
    user_input = input("Enter function in x: ")
    user_input = user_input.replace("^", "**")

    # Parsing user input into a sympy expression & create a callable function
    expr = parse_expr(user_input, transformations=transformations)  
    f = lambdify(x, expr, "numpy")  

    # calculating the derivative using sympy & creating a callable function
    derivative_expr = expr.diff(x)
    f_prime = lambdify(x, derivative_expr, "numpy")

# Plotting the function for visualization
    y = np.linspace(-5, 5, 6000)
    # plt.figure(figsize=(10, 6))
    plt.plot(y, f(y), label=f"f(x) = {user_input}")
    plt.ylim(-5, 5)
    plt.title("Plot of the Function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.show(block=False)

    
    while True:
        print("\n" + "="*50)
        print("Solving Nonlinear Equations - Iterative Methods")
        print("="*50)
        print("1 --> Bisection Method")
        print("2 --> False Position Method")
        print("3 --> Newton Raphson Method")
        print("4 --> Secant Method")
        print("5 --> Hybrid(N-R & Bisection) Method")
        print("0 --> Exit Program")
        
        choice = input("\nSelect an option: ").strip()

        if choice == '0':
            print("Exiting program!")
            plt.close('all')
            break
        
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid selection. Please try again.")
            continue

        try:
            if choice in ['1', '2', '5']:
                input_data = input("Enter a & b separated by spaces: ")
                a, b = map(float, input_data.split())

            if choice == '1':
                print("\n--- Running Bisection ---")
                bisection_method(f, a, b)

            elif choice == '2':
                print("\n--- Running False Position ---")
                false_position_method(f, a, b)

            elif choice == '5':
                print("\n--- Running Hybrid Bisection-Newton ---")
                hybrid_bisection_newton(f, f_prime, a, b)

            elif choice == '3':
                x0 = float(input("Enter initial guess x0: "))
                print("\n--- Running Newton-Raphson ---")
                newton_raphson_method(f, f_prime, x0)

            elif choice == '4':
                x0 = float(input("Enter initial guess x0: "))
                x1 = float(input("Enter initial guess x1: "))
                print("\n--- Running Secant Method ---")
                secant_method(f, x0, x1)   

        except ValueError as e:
            print(f"Input Error: {e}. Please ensure you enter numbers.")
        
        input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()