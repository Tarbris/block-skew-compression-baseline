"""Weak editable compressor: independent global Top-K per worker/round."""

class Compressor:
    def __init__(self, n_workers=4, n_blocks=8, block_size=16, budget=8):
        self.budget = budget

    def compress(self, worker_id, gradient):
        chosen = sorted(range(len(gradient)), key=lambda i: (-abs(gradient[i]), i))[:self.budget]
        return [[i, float(gradient[i])] for i in chosen]
