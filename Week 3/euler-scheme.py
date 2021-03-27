def euler_integrate(delta_t, j, scheme):

    s = [1.]

    if scheme == 'implicit':
        for i in range(j):
            s_ = s[i] / (1 + (10*delta_t))
            s.append(s_)

        return s[j]

    elif scheme == 'explicit':
        for i in range(j):
            s_ = s[i] * (1 - (10*delta_t))
            s.append(s_)

        return s[j]

    return "\nInvalid input."


if __name__ == '__main__':

    sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

    while(True):
        try:
            print("Input Δ𝘵, j and scheme seperated by spaces.", end='\n→ ')
            delta_t, j, scheme = input().split()

            print(f"\nS{j.translate(sub)}: {euler_integrate(float(delta_t), int(j), scheme.lower())}", end='\n\n')
        except:
            print("\nInvalid input!\n")


