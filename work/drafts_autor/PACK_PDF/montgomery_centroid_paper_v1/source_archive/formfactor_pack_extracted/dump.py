import numpy as np
d=np.load("corrII.npz"); al,off=d["al"],d["off"]; N=int(d["N"]); T=float(d["T"]); LT=float(d["LT"])
with open("ff/formfactor_data.txt","w") as f:
    f.write(f"# Off(alpha) = F(alpha) - 1  (termino fuera de diagonal del factor de forma conectado)\n")
    f.write(f"# N = {N}   T = {T:.9f}   L_T = log(T/2pi) = {LT:.12f}\n")
    f.write(f"# ventana de Montgomery w(u)=4/(4+u^2), truncada en |u|<120, offsets j<=154\n")
    f.write(f"# F(alpha) = 1 (diagonal, exacto por normalizacion) + Off(alpha)\n")
    f.write(f"# columnas: alpha   c=alpha*L_T   Off(alpha)   F(alpha)\n")
    for a,o in zip(al,off): f.write(f"{a:.4f}\t{a*LT:.8f}\t{o:+.10e}\t{1+o:.10f}\n")
print(f"escritas {len(al)} filas -> ff/formfactor_data.txt")
