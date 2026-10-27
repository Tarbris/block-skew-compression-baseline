# Block-skew gradient compression workspace

Edit `compressor.py` only. The evaluator creates one `Compressor` with
`n_workers=4`, `n_blocks=8`, `block_size=16`, `budget=8`. At each round it
calls `compress(worker_id, gradient)` once for each worker. `gradient` is a
length-128 list of finite floats computed at the current shared parameter
vector. Return at most eight `[index, value]` pairs, with distinct integer
indices 0..127 and finite numeric transmitted values. Unsent coordinates
become zero at the server; transmitted values are averaged over four workers
before the shared update. State may persist per worker across calls.

The training target and future worker gradients are not visible. Gradient
noise is uneven across eight fixed consecutive 16-coordinate blocks, and
several target blocks shift once mid-run. The evaluator scores normalized
mean squared parameter error after warmup under a fixed total sparse
communication budget. Python 3.12 standard library, CPU, no network.
The weak starter takes global magnitude Top-K every round.
