import math
import numpy as np



def disponibilidade(
        n: int,
        k: int,
        p: float) -> float:
    """
    n - número total de servidores, n > 0
    k - mínimo operacional, 0 < k <= n
    p - prob de um servidor estar up, 0 <= p <= 1
    X - número de servidores disponíveis em um dado momento
    """
    prob = 0.0
    for i in range(n - k + 1):
        prob += math.comb(n, k + i) * (p ** (k + i)) * ((1 - p) ** (n - (k + i)))
    return prob

def disponibilidade_vec(
        n: np.ndarray[int],
        k: np.ndarray[int],
        p: np.ndarray[float]) -> np.ndarray[float]:
    """
    n - número total de servidores, n > 0
    k - mínimo operacional, 0 < k <= n
    p - prob de um servidor estar up, 0 <= p <= 1
    X - número de servidores disponíveis em um dado momento
    """
    assert n.shape == k.shape == p.shape, f"n, k e p devem ter o mesmo tamanho. n: {len(n)}, k: {len(k)}, p: {len(p)}"
    print(n.shape, k.shape, p.shape)
    prob = np.zeros_like(p)
    for case in range(len(n)):
        for i in range(n[case] - k[case] + 1):
            # prob[case] += math.comb(n[case], k[case] + i) * (p[case] ** (k[case] + i)) * ((1 - p[case]) ** (n[case] - k[case] + i))
            prob[case] += math.comb(n[case], k[case] + i) * (p[case] ** (k[case] + i)) * ((1 - p[case]) ** (n[case] - (k[case] + i)))
    return prob


if __name__ == "__main__":
    n = 5
    k = 3
    p = 0.9
    print(disponibilidade(n, k, p))

    n = np.array([5, 10, 15])
    k = np.array([3, 7, 10])
    p = np.array([0.9, 0.8, 0.7])
    print(disponibilidade_vec(n, k, p))
