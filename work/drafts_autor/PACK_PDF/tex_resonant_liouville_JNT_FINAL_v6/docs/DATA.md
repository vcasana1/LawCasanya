# Data used

The paper uses only `data/liouville_int8_N21000000.bin`.

Encoding:
- raw signed int8
- byte 0 = lambda(1)
- byte n-1 = lambda(n)
- N = 21,000,000

The binary is deterministic and can be regenerated with
`src/generate_liouville_bin.py`.

No zeta-zero, RVM, prime-list, or other project binaries are used by this paper.
