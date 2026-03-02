import tabulate
from num_methods.config import TOL, MAX_ITER

def false_position_method(f, a, b):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    table = []
    prev_c = None

    for iteration in range(1, MAX_ITER + 1):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        f_c = f(c)

        # Estimated absolute error (successive difference)
        if prev_c is not None:
            abs_error = abs(c - prev_c)
        else:
            abs_error = None

        current_interval = f"[{a:.6f}, {b:.6f}]"
        table.append([iteration, current_interval, c, f_c, abs_error if abs_error is not None else 0.0])

        # Stopping criteria
        if abs(f_c) < TOL:
            break

        if prev_c is not None and abs_error is not None and abs_error < TOL:
            break

        # Update interval
        if f(a) * f_c < 0:
            b = c
        else:
            a = c

        prev_c = c

    headers = ["Iter", "Interval", "c (Root)", "f(c)", "|Δc|"]
    print(tabulate.tabulate(table, headers=headers, tablefmt="outline", floatfmt=".6f"))

    print(f"\nTotal Iterations: {iteration}")
    print(f"Approximate Root: {c:.6f}")

    return c, iteration