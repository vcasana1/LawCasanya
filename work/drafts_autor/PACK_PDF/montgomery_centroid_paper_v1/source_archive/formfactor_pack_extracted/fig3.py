import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
d=np.load("corrII.npz"); al,off,N,LT=d["al"],d["off"],int(d["N"]),float(d["LT"])
INK="#1a1a1a";MUT="#8a8a8a";C1="#0b6fa4";C2="#c8681c"
fig,(a1,a2)=plt.subplots(1,2,figsize=(11.5,4.4),dpi=170,gridspec_kw={"width_ratios":[1.25,1]})
a1.axhline(0,color=MUT,lw=.7); a1.axvline(1,color=C2,lw=1.1,ls="--")
a1.plot(al,off,color=C1,lw=1.0)
a1.annotate(r"$\alpha=1$",(1.03,3.6),fontsize=9,color=C2)
a1.annotate("masa absoluta $\\approx L_T = 8.07$\nrms 0.774 aquí",(0.06,-2.4),fontsize=8,color=MUT)
a1.annotate("rms 0.019\n(factor 40 menor)",(2.0,1.2),fontsize=8,color=MUT)
a1.set_xlabel(r"$\alpha$",fontsize=10);a1.set_ylabel(r"Off$(\alpha)=F(\alpha)-1$",fontsize=10)
a1.set_title(r"Todo el contenido de la meseta está en Off$(\alpha)$",fontsize=11,loc="left")
k=al>=1.05
a2.axhline(0,color=MUT,lw=.7)
a2.plot(al[k],off[k],color=C1,lw=1.0,label=r"Off$(\alpha)$, $\alpha>1$")
for s,lab,c in [(0.34*LT/np.sqrt(N),r"$\pm\,0.34\,L_T/\sqrt{N}$",C2)]:
    a2.axhline(s,color=c,lw=1.2,ls="--",label=lab); a2.axhline(-s,color=c,lw=1.2,ls="--")
a2.set_ylim(-0.09,0.09);a2.set_xlabel(r"$\alpha$",fontsize=10)
a2.legend(frameon=False,fontsize=8.5,loc="upper right")
a2.set_title("La meseta, ampliada: ruido de raíz",fontsize=11,loc="left")
for ax in (a1,a2):
    ax.tick_params(labelsize=8.5);ax.spines["top"].set_visible(False);ax.spines["right"].set_visible(False)
    [s.set_color(MUT) for s in ax.spines.values()]
fig.suptitle(f"Factor de forma conectado, {N:,} ceros: la diagonal da 1 exacto, la conjetura entera es Off$\\to$0",
             fontsize=12,x=0.012,ha="left",y=1.03,color=INK)
plt.tight_layout();plt.savefig("formfactor.png",bbox_inches="tight",facecolor="white");print("ok")
