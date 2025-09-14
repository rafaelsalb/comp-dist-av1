import numpy as np
from analitico import disponibilidade

class StochasticSimulator:
    def __init__(self, n: int, p: float, k: int):
        """
        n - número total de máquinas
        p - probabilidade de cada máquina estar disponível
        k - número mínimo de máquinas disponíveis para o sistema estar operacional
        """
        self.n = n
        self.p = p
        self.k = k

    def run_simulation(self, sample_size: int) -> float:
        """
        Executa sample_size iterações, simulando a disponibilidade das n máquinas
        e retorna a disponibilidade (proporção de iterações com pelo menos k máquinas disponíveis)
        """
        # Vetorizado: cada iteração simula o número de servidores "up"
        resultados = np.random.binomial(n=self.n, p=self.p, size=sample_size)
        # Considera "sucesso" se o número de máquinas disponíveis for pelo menos k
        sucessos = resultados >= self.k
        disponibilidade_simulada = np.mean(sucessos, dtype="float64")
        return disponibilidade_simulada

    def simulate_multiple_samples(self, sample_sizes: list[int]) -> dict:
        """
        Executa simulações para diferentes tamanhos de amostra e retorna um dicionário
        com o tamanho da amostra e a disponibilidade simulada.
        """
        results = {}
        for size in sample_sizes:
            results[size] = self.run_simulation(size)
        return results

if __name__ == "__main__":
    # Parâmetros do sistema
    n = 5
    p = 0.9
    k = 3

    simulator = StochasticSimulator(n, p, k)

    # Exemplo de simulação com um tamanho de amostra grande
    sample_size = 10_000
    disponibilidade_simulada = simulator.run_simulation(sample_size)
    disponibilidade_analitica = disponibilidade(n, k, p)

    print("Disponibilidade simulada:", disponibilidade_simulada)
    print("Disponibilidade analítica:", disponibilidade_analitica)

    # Simulações para diferentes tamanhos de amostra
    sample_sizes = [10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]
    simulations = simulator.simulate_multiple_samples(sample_sizes)
    for size, value in simulations.items():
        print(f"Tamanho da amostra {size}: Disponibilidade simulada = {value}")