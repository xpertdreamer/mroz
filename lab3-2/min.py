                # for i in range(4):
                #     for j in range(i + 1, 4):
                #         if xs[j] < xs[i]:
                #             xs[i], xs[j] = xs[j], xs[i]
                #             fs[i], fs[j] = fs[j], fs[i]
                # idx = 0
                # best_diff = abs(xs[0] - best)
                # for i in range(1, 4):
                #     diff = abs(xs[i] - best)
                #     if diff < best_diff:
                #         best_diff = diff
                #         idx = i
                # if idx == 0:
                #     idx += 1
                # if idx == 3:
                #     idx -= 1



def dich(func, a0, b0, l, eps):
    a_k = a0
    b_k = b0
    k = 0
    while True:
        y_k = (a_k+b_k-eps)/2
        z_k = (a_k+b_k+eps)/2
        if func(y_k) <= func(z_k):
            a_next = a_k
            b_next = z_k
        else:
            a_next = y_k
            b_next = b_k
        L_next = abs(b_next-a_next)
        if L_next <= l:
            return (a_next + b_next) / 2
        else:
            k += 1
            a_k = a_next
            b_k = b_next

import math


def interpolation(x, dx, e1, e2, func):
    # 1
    if dx <= 0 or func is None:
        return 0
    x1 = x
    while True:
        # 2
        x2 = x1 + dx
        # 3
        f1 = func(x1)
        f2 = func(x2)
        # 4 a
        if f1 > f2:
            x3 = x1 + 2.0 * dx
        # 4 b
        else:
            x3 = x1 - dx
        # 5
        f3 = func(x3)
        # 6
        Fmin, x_min = f1, x1
        if f2 < Fmin:
            Fmin, x_min = f2, x2
        if f3 < Fmin:
            Fmin, x_min = f3, x3
        while True:
            # 7
            num = (x2 * x2 - x3 * x3) * f1 + (x3 * x3 - x1 * x1) * f2 + (x1 * x1 - x2 * x2) * f3
            den = (x2 - x3) * f1 + (x3 - x1) * f2 + (x1 - x2) * f3
            if math.fabs(den) == 0:
                x1 = x_min
                # goto 2
                break
            x_bar = 0.5 * num / den
            f_bar = func(x_bar)
            # 8
            cond1 = math.fabs((Fmin - f_bar) / x_bar)
            cond2 = math.fabs((x_min - x_bar) / x_bar)
            # 8 a
            if cond1 < e1 and cond2 < e2:
                return x_bar
            # 8 b
            if x1 <= x_bar <= x3:
                best = x_bar if f_bar < Fmin else x_min
                xs = [x1, x2, x3, x_bar]
                fs = [f1, f2, f3, f_bar]
                # zip (xs[i], fs[i]) -> sort by xs -> unzip with * to xs, fs separately
                xs, fs = zip(*sorted(zip(xs, fs)))
                i = min(range(4), key=lambda j: abs(xs[j] - best))
                i = max(1, min(2, i))
                x1, f1 = xs[i - 1], fs[i - 1]
                x2, f2 = xs[i], fs[i]
                x3, f3 = xs[i + 1], fs[i + 1]
                Fmin, x_min = f1, x1
                if f2 < Fmin:
                    Fmin, x_min = f2, x2
                if f3 < Fmin:
                    Fmin, x_min = f3, x3
                # goto 6
                continue
            # 8v
            else:
                x1 = x_bar
                # goto 2
                break

func2 = lambda x: 2*x**2-x+7
func5 = lambda x: (127.0/4.0)*x**2-(61.0/4.0)*x+2.0
min2 = dich(func2, 0, 6, 0.001, 0.0001)
min5 = dich(func5, 0, 6, 0.001, 0.0001)
print('dichtomy')
print(f'function 2:', f'x_min = {min2}', sep='\t')
print(f'function 5:', f'x_min = {min5}', sep='\t')
print('interpolation')
min22 = interpolation(0, 0.5, 0.001, 0.0001, func2)
min25 = interpolation(0, 0.5, 0.001, 0.0001, func5)
print(f'function 2:', f'x_min = {min22}', sep='\t')
print(f'function 5:', f'x_min = {min25}', sep='\t')
