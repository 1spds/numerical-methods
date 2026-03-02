import tabulate
from num_methods.config import TOL, MAX_ITER

def secant_method(f, x0, x1):
    table = []

    for iteration in range(1, MAX_ITER + 1):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if abs(f_x1 - f_x0) < 1e-12:
            raise ValueError("f(x1) and f(x0) are too close. Secant method fails.")

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        abs_error = abs(x2 - x1)

        table.append([iteration, x0, x1, f_x0, f_x1, abs_error])

        # Stopping criteria
        if abs(f_x1) < TOL:
            break

        if abs_error < TOL:
            break

        x0 = x1
        x1 = x2

    headers = ["Iter", "x_{n-1}", "x_n", "f(x_{n-1})", "f(x_n)", "|Δx|"]
    print(tabulate.tabulate(table, headers=headers, tablefmt="outline", floatfmt=".6f"))

    print(f"\nTotal Iterations: {iteration}")
    print(f"Approximate Root: {x2:.6f}")

    return x2, iteration