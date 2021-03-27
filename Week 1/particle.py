randomNumberList = [0.800, 0.801, 0.752, 0.661, 0.169, 0.956, 0.949,
                    0.003, 0.201, 0.291, 0.615, 0.131, 0.241, 0.685, 0.116, 0.241, 0.849]

A = 4
B = 3
k1 = 0.2
k2 = 0.2
N = A + B
t = 0
delta_t = 2

if __name__ == '__main__':

    while True:
        for _ in range(N):
            r = randomNumberList.pop(0)
            trnsf = False
            a = A/(A+B)

            print(
                f"2:  {r:.3f} < {a:.3f}({A}/{A+B})  {'True ' if r < a else 'False'} -> Choose {'A' if r < a else 'B'}")

            if(r < a):
                r = randomNumberList.pop(0)
                c = k1*delta_t

                if(r < c):
                    A -= 1
                    B += 1
                    trnsf = True

            else:
                r = randomNumberList.pop(0)
                c = k2*delta_t

                if(r < c):
                    A += 1
                    B -= 1
                    trnsf = True

            print(
                f"{'3A' if r < a else '3B'}: {r:.3f} < {c:.3f}\t{f'True  -> Transform -> A = {A} B = {B}' if trnsf else 'False -> No Transformation'} ")

        print(f"B = {B}")

        t += delta_t
        if delta_t == 2:
            break
