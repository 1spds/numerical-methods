import tabulate
from num_methods.config import TOL, MAX_ITER

def newton_raphson_method(f, f_prime, x0):
    table = []

    for iteration in range(1, MAX_ITER + 1):
        f_x = f(x0)
        f_prime_x = f_prime(x0)

        if abs(f_prime_x) < 1e-12:
            raise ValueError("Derivative is zero. Newton method fails.")

        x1 = x0 - f_x / f_prime_x

        abs_error = abs(x1 - x0)

        table.append([iteration, x0, f_x, f_prime_x, abs_error])

        # Stopping criteria
        if abs(f_x) < TOL:
            break

        if abs_error < TOL:
            break

        if abs(f_x)==0:
            break

        x0 = x1

    headers = ["Iter", "x_n", "f(x_n)", "f'(x_n)", "|Δx|"]
    print(tabulate.tabulate(table, headers=headers, tablefmt="outline", floatfmt=".6f"))

    print(f"\nTotal Iterations: {iteration}")
    print(f"Approximate Root: {x1:.6f}")

    return x1, iteration