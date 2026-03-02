import tabulate
from num_methods.config import TOL, MAX_ITER

def hybrid_bisection_newton(f, f_prime, a, b):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    table = []
    prev_x = None

    for iteration in range(1, 4):
        mid = (a + b) / 2
        f_mid = f(mid)

        interval_str = f"[{a:.6f}, {b:.6f}]"

        if prev_x is not None:
            abs_error = abs(mid - prev_x)
        else:
            abs_error = 0.0

        table.append([iteration,"Bisection",interval_str,mid,f_mid,abs_error])

        if f(a) * f_mid < 0:
            b = mid
        else:
            a = mid

        prev_x = mid

    x = (a + b) / 2

   
    for iteration in range(4, MAX_ITER + 1):
        f_x = f(x)
        f_prime_x = f_prime(x)

        if abs(f_prime_x) < 1e-12:
            raise ValueError("Derivative too small. Newton fails.")

        x_new = x - f_x / f_prime_x
        f_new = f(x_new)

        abs_error = abs(x_new - x)

        guess_str = f"{x:.6f}"

        table.append([iteration,"Newton",guess_str,x_new,f_new,abs_error])

        if abs_error < TOL or abs(f_new) < TOL:
            x = x_new
            break

        prev_x = x
        x = x_new

    headers = ["Iter", "Method", "Interval / Guess", "x_new", "f(x_new)", "|Δx|"]
    print(tabulate.tabulate(table,headers=headers,tablefmt="outline",floatfmt=".6f"))

    print(f"Total Iterations: {iteration}")
    print(f"\nApproximate Root: {x:.6f}")

    return x, iteration