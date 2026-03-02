import tabulate
from num_methods.config import TOL, MAX_ITER

def bisection_method(f, a, b):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    table = []
    prev_mid = None

    for iteration in range(1, MAX_ITER + 1):
        mid = (a + b) / 2.0
        f_mid = f(mid)
        # the maximum possible error--half the interval width--true root within [a, b] 
        abs_error = abs(b - a) / 2

        current_interval = f"[{a:.6f}, {b:.6f}]"
        table.append([iteration, current_interval, mid, f_mid, abs_error])

        # Stopping criteria
        if abs(f_mid) < TOL:
            break

        if abs_error < TOL:
            break

        if prev_mid is not None and abs(mid - prev_mid) < TOL:
            break

        # Update interval
        if f(a) * f_mid < 0:
            b = mid
        else:
            a = mid

        prev_mid = mid

    headers = ["Iter", "Interval", "Midpoint", "f(Mid)", "|Δx|"]
    print(tabulate.tabulate(table, headers=headers, tablefmt="outline", floatfmt=".6f"))

    print(f"\nTotal Iterations: {iteration}")
    print(f"Approximate Root: {mid:.6f}")

    return mid, iteration