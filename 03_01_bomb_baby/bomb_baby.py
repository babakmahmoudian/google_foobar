def solution(m, f):
    M, F = [int(m), int(f)]
    m, f = [M, F] if M > F else [F, M]

    cycles = 0
    while m % f != 0:
        cycles += (m // f)
        m, f = f, m % f

    return 'impossible' if f != 1 else str(cycles + m - 1)
