# High-height Odlyzko block near n=10^12

Source: Odlyzko zeros3 (10,000 zeros), mirrored verbatim in NagusameCS/HyperTensor.
Base ordinate: 267653395647.
Global zero indices: 1000000000001 ... 1000000010000.

Files:
- zeross_1e12.bin: absolute ordinates, little-endian float64
- zLamb_1e12.bin: Lambert/RvM ordinates, little-endian float64
- zCasanya_1e12.bin: Law-Casanya c667 ordinates, little-endian float64
- *_offsets.bin: same arrays as offsets from 267653395647; preferred for error/gap work.

At this height the c667 dyadic cutoff saturates at 512, so the three effective prime-power cutoffs are [8,8,512].

Absolute float64 values around 2.676e11 have ~3e-5 spacing, so use the offset binaries for precision-sensitive comparisons.
