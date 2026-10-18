#!/usr/bin/env python3
"""Generate the English TeX summary and Spanish plain-text report from measured data."""
import csv
import json
import os
from pathlib import Path
import platform
import sys
os.environ.setdefault('MPLCONFIGDIR','/private/tmp/zCasanya_matplotlib')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    out=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parent
    s=json.loads((out/'summary.json').read_text())
    q=json.loads((out/'numeric_checks.json').read_text())
    a=json.loads((out/'input_audit.json').read_text())
    protocol=json.loads((out/'split_protocol.json').read_text())
    selected=json.loads((out/'selected.json').read_text())
    n_pilot=json.loads((out/'pilot_complete.json').read_text())['candidates']
    n_full=json.loads((out/'full_complete.json').read_text())['candidates']
    rows=list(csv.DictReader((out/'zCasanya_results.csv').open()))
    val=list(csv.DictReader((out/'selection_validation_results.csv').open()))
    get=lambda id,region:next(r for r in rows if r['id']==id and r['region']==region)
    methods=['Lambert/RvM','Casanya, 1 step','Casanya, 2 steps','Casanya, 3 steps','Casanya, 4 steps','Selected configuration']
    table=[]; text=[]
    for label,r in zip(methods,s['comparison']):
        improved='---' if r['id']=='Lambert' else f"{r['percent_improved']:.3f}"
        table.append(f"{label} & {r['rms']:.10f} & {r['max_abs']:.7f} & {improved} \\\\")
        text.append(f"{label:25s} RMS={r['rms']:.10f} max={r['max_abs']:.9f} mejora_indices={improved}% id={r['id']} cortes={r['cutoffs']}")
    regiontable=[]
    for region,label in [('tuning_full','Tuning'),('selection_validation','Selection validation'),('untouched_test','Untouched test'),('all','All indices')]:
        b=get('Lambert',region); r=get(s['selected_id'],region)
        regiontable.append(f"{label} & {int(r['n']):,} & {float(b['rms']):.10f} & {float(r['rms']):.10f} & {100*(1-float(r['rms'])/float(b['rms'])):.3f} \\\\")
    # Independent test metrics for winners by iteration count, selected using validation only.
    testtable=[]
    for j,r in enumerate(s['comparison'][1:5],1):
        t=get(r['id'],'untouched_test')
        v=get(r['id'],'selection_validation')
        testtable.append(f"{j} & {r['id']} & {float(v['rms']):.10f} & {float(t['rms']):.10f} & {r['nonpositive_gaps']} \\\\")
    xy=np.memmap(out/'zCasanya.bin',dtype='<f8',mode='r')
    first,last=float(xy[0]),float(xy[-1])
    c=s['configuration']; pair=s['matched_second_step']
    manifest=json.loads((out/'full_manifest.json').read_text())
    configs_by_id={x['id']:x for x in manifest}
    finalrow=get(s['selected_id'],'all')
    selected_v10=min((r for r in val if r['window']=='euler_v10' and r['intrinsically_eligible']=='True'),key=lambda r:float(r['rms']))
    selected_sharp=min((r for r in val if r['window']=='power_sharp' and r['intrinsically_eligible']=='True'),key=lambda r:float(r['rms']))
    # Portable plots: full-sample signed-error histogram and RMS by height.
    hist=list(csv.DictReader((out/'error_distribution.csv').open()))
    windows=list(csv.DictReader((out/'height_windows.csv').open()))
    fig,ax=plt.subplots(1,2,figsize=(11,3.5),layout='constrained')
    for id,label in [('Lambert','Lambert/RvM'),(s['selected_id'],'Selected Casanya')]:
        h=[r for r in hist if r['id']==id and np.isfinite(float(r['error_lower'])) and np.isfinite(float(r['error_upper']))]
        xx=np.array([(float(r['error_lower'])+float(r['error_upper']))/2 for r in h])
        yy=np.array([int(r['count']) for r in h])/(s['records']*.025)
        ax[0].plot(xx,yy,label=label,lw=1.5)
        w=[r for r in windows if r['id']==id]
        ax[1].plot([np.sqrt(float(r['T_lower'])*float(r['T_upper'])) for r in w],
                   [float(r['rms']) for r in w],marker='o',ms=3,label=label)
    ax[0].set(xlabel='Signed height error',ylabel='Density',xlim=(-.7,.7))
    ax[1].set(xlabel='Geometric midpoint of dyadic height window',ylabel='RMS height error',xscale='log',yscale='log')
    for z in ax:z.grid(alpha=.2);z.legend(fontsize=8)
    fig.savefig(out/'error_and_height.png',dpi=180)
    # No estimated coefficients or extrapolated asymptotic claims enter this report.
    template=r'''\documentclass[11pt]{amsart}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,amsfonts,amsthm,mathtools}
\usepackage[margin=1in]{geometry}
\usepackage{enumitem,booktabs,graphicx,longtable}
\usepackage[hidelinks]{hyperref}
\setlength{\emergencystretch}{3em}
\numberwithin{equation}{section}
\newtheorem{proposition}{Proposition}[section]
\theoremstyle{definition}\newtheorem{definition}[proposition]{Definition}
\newtheorem{experiment}[proposition]{Experiment}
\theoremstyle{remark}\newtheorem{remark}[proposition]{Remark}
\title[Arithmetic Newton iteration and prime corrections]{Arithmetic Newton iteration using the Riemann--von Mangoldt clock and primes: the zCasanya numerical experiment}
\author{}
\date{18 October 2026}
\begin{document}
\begin{abstract}
We construct and compare explicit prime-based ordinate approximations on all
2,001,052 supplied indices. The selected arithmetic iteration has RMS height
error @FINAL_RMS@, against @BASE_RMS@ for the original Lambert/RvM array,
a measured reduction of @GAIN@\%. Selection uses a separate validation region;
an untouched final region is evaluated only after the configuration is frozen.
The construction reads only the supplied clock and primes.
\end{abstract}
\maketitle
\tableofcontents

\section{Input data and the exact construction}\label{sec:construction}
\begin{experiment}\label{exp:inputs}
The input directory is the user's original MATLAB data directory, although
every program in this experiment is Python. Both ordinate arrays consist of
2,001,052 little-endian binary64 values (16,008,416 bytes each).
The original prime file actually contains @PRIME_COUNT@ little-endian
64-bit integers, not merely 148,933 records. Its complete order was checked
in bounded-memory blocks; its prefix through 1,999,993 was compared exactly
with an independently computed sieve. The next prime is 2,000,003.
The portable package includes this prefix and the next-prime sentinel,
rather than duplicating the @PRIME_BYTES@-byte original prime file.
SHA-256 hashes, endpoint values and binary layouts are recorded in the JSON audits.
Unsigned interpretation is also documented in the existing local script
\texttt{MOBIUS\_F\_EXACT\_LAST\_PRIMES\_R2024b.m}.
\end{experiment}

\begin{definition}\label{def:clock}
With $\tau_k$ the stored Lambert/RvM ordinate, the requested smooth clock is
\begin{equation}
N_0(t)=\frac{t}{2\pi}\left(\log\frac{t}{2\pi}-1\right)+\frac78,
\qquad \mathcal L(t)=\frac{\log(t/2\pi)}{2\pi}.
\label{eq:clock}
\end{equation}
The principal phase is the actual definition of the supplied v10 manuscript
\cite[Section 2.4, equation (2.10)]{Aynasac2026}:
\begin{equation}
S_X^{\rm Euler}(t)=-\frac1\pi\sum_{p\le X}\sum_{m\ge1}
\frac{\sin(mt\log p)}{m p^{m/2}}.
\label{eq:euler}
\end{equation}
There is no smoothing weight in this definition. Smooth auxiliary windows
used in proofs in the manuscript are not inserted into this phase.
The independently implemented sharp prime-power variant requested in the
task is
\begin{equation}
S_X^{\rm power}(t)=-\frac1\pi\sum_{p^m\le X}
\frac{\sin(mt\log p)}{m p^{m/2}}.
\label{eq:power}
\end{equation}
These phases are kept separate in every parameter record and CSV.
\end{definition}

\begin{proposition}[Elementary local-factor evaluation]\label{prop:factor}
For $a=p^{-1/2}<1$ and $u=t\log p$,
\begin{equation}
\sum_{m\ge1}\frac{a^m\sin(mu)}m
=\operatorname{atan2}(a\sin u,1-a\cos u).
\label{eq:factor}
\end{equation}
\end{proposition}
\begin{proof}
The absolutely convergent power series $-\log(1-z)=\sum_{m\ge1}z^m/m$
at $z=ae^{iu}$ has imaginary part equal to the left side.
Since $1-a\cos u>0$, the imaginary part of $-\log(1-ae^{iu})$
equals the displayed elementary angle, with no branch unwrapping.
\end{proof}
Thus all prime powers in \eqref{eq:euler} are included by an elementary
formula, with no truncation of the $m$-sum. No zeta function, zeta argument,
true ordinate or RH-dependent zero equation is evaluated by the constructor.

\begin{definition}[Requested arithmetic iteration]\label{def:iteration}
For either choice of phase the update is exactly the requested one:
\begin{equation}
t_k^{(0)}=\tau_k,\qquad
t_k^{(j+1)}=t_k^{(j)}-
\frac{N_0(t_k^{(j)})+S_{X_{j+1}}(t_k^{(j)})-(k-\tfrac12)}
{\mathcal L(t_k^{(j)})}.
\label{eq:iteration}
\end{equation}
The denominator is the derivative of the smooth clock, as specified in
the task; it is not replaced by $\mathcal L+S_X'$.
No damping, sorting, clipping, index reassignment or learned correction is used.
\end{definition}

\section{Stable clock differences and numerical checks}\label{sec:numerics}
\begin{proposition}[Stable difference, derived here]\label{prop:difference}
Put $d=t-\tau$ and $u=d/\tau$. Then
\begin{equation}
N_0(t)-N_0(\tau)=\mathcal L(\tau)d+
\frac{\tau}{2\pi}\bigl((1+u)\log(1+u)-u\bigr).
\label{eq:difference}
\end{equation}
For $|u|<1$ the bracket is
\begin{equation}
\sum_{n=2}^{\infty}\frac{(-1)^n u^n}{n(n-1)}
=\frac{u^2}{2}-\frac{u^3}{6}+\frac{u^4}{12}-\cdots.
\label{eq:series}
\end{equation}
\end{proposition}
\begin{proof}
Substitute $t=\tau(1+u)$ into \eqref{eq:clock}, cancel constants,
and separate $d\log(\tau/2\pi)/(2\pi)$. Integrating the Taylor series
of $\log(1+u)$ gives \eqref{eq:series}.
\end{proof}
The expression proposed in the pasted task has quadratic term
$-\tau u^2/(4\pi)$ instead of $+\tau u^2/(4\pi)$, so it was not used.
For $|u|<0.01$ the implementation evaluates \eqref{eq:series} through degree 14;
otherwise it uses \texttt{log1p} in \eqref{eq:difference}.
The small stored-clock residual $N_0(\tau_k)-(k-1/2)$ is retained.

\begin{experiment}\label{exp:precision}
Elementary calculations at 70 decimal digits tested sampled heights between
$@HEIGHT_FIRST@$ and $@HEIGHT_LAST@$, including the first 20 indices,
with displacements $-1,-0.01,0,0.01,1$.
The maximum stable-difference error was @DIFF_ERR@, and the sampled direct-clock
roundoff was @CLOCK_ERR@. Sampled phase errors at cutoffs 8, 128 and 8192
were at most @PHASE_ERR@. The elementary local factor agreed with a
500-power high-precision sum to @FACTOR_ERR@.
The audit hook was tested and rejected attempts by the construction process
to open a true-zero filename. These are sampled numerical checks, not
uniform floating-point error bounds for every possible input.
\end{experiment}

\section{Search and independent evaluation}\label{sec:protocol}
\begin{experiment}\label{exp:search}
The search generated @N_PILOT@ prime-only pilot arrays: both phases,
constant and dyadic policies, and all nondecreasing cutoff sequences of
length one through four on the grid
$\{8,\allowbreak32,\allowbreak128,\allowbreak512,\allowbreak2048,\allowbreak8192\}$.
The tuning sample consists of 12,000 approximately equally spaced indices
after the first 512 within the first 40\%; the first 512 consecutive
indices are extra arithmetic stability probes and are excluded from the
sample RMS used for tuning.
All shortlisted models, their prefixes and matched same-cutoff iteration
comparisons were then generated on every index, giving @N_FULL@ full arrays.
Earlier full pilot finalists are retained in the final comparison.
For the dyadic policy,
\begin{equation}
T_k=2^{\lfloor\log_2\tau_k\rfloor},\qquad
X_j(k)=\min\{X_{j,\max},\max(8,\lfloor\sqrt{T_k}\rfloor)\}.
\label{eq:dyadic}
\end{equation}
This is an explicitly defined finite-height search policy. The asymptotic
iterated-log prescription was not imposed: at the maximum supplied height
its iterated logarithms cease to define positive iteration scales after
only a few applications.
\end{experiment}

The fixed index regions are tuning @TUNE_RANGE@; selection validation
@VAL_RANGE@; untouched test @TEST_RANGE@. True-zero values were used only
by the separate validator: first for tuning the parameter shortlist,
then for validation ranking. The selected ID and SHA-256 were frozen in
\texttt{selected.json} before the final test region was evaluated.
The construction module has a process-level file-access hook blocking
the true-zero filename and accepts only the two arithmetic binary inputs
and parameter metadata. No zero values enter the update in \eqref{eq:iteration}.

Eligibility requires all iterates finite and above $2\pi$, with every step
less than eight smooth local spacings. This uses no true ordinates.
Steps exceeding two local spacings, maximum displacements and nonpositive
consecutive gaps are reported separately. Crossings are not repaired.
The selected eligible model minimizes selection-validation RMS among the
shortlisted models; the untouched test is not used for reselection.
Exact validation-RMS ties are resolved by fewer crossings in the full
arithmetic array, then by configuration ID.

\section{Measured results}\label{sec:results}
\begin{experiment}\label{exp:results}
The selected configuration is \texttt{@ID@}, phase \texttt{@PHASE@},
policy \texttt{@POLICY@}, cutoffs $@CUTOFFS@$.
Its overall mean absolute error is @MAE@, median absolute error @MEDIAN@,
maximum absolute error @MAX@, and @BETTER@\% of individual indices improve
over Lambert/RvM. It has @CROSSINGS@ nonpositive consecutive gaps.
\end{experiment}

\begin{table}[htbp]\centering\small
\caption{All-index metrics. Each iteration count uses its lowest-RMS eligible
configuration on selection validation, not on the full data or final test.}
\label{tab:overall}
\begin{tabular}{lrrr}\toprule
Method & RMS & Maximum error & Improved (\%)\\\midrule
@OVERALL_TABLE@
\bottomrule\end{tabular}
\end{table}

\begin{table}[htbp]\centering\small
\caption{Region-specific RMS for the frozen winner. Only the final test region
was unused both for pilot tuning and for selecting the winner.}
\label{tab:regions}
\begin{tabular}{lrrrr}\toprule
Region & Count & Lambert RMS & Casanya RMS & Reduction (\%)\\\midrule
@REGION_TABLE@
\bottomrule\end{tabular}
\end{table}

\begin{table}[htbp]\centering\small
\caption{Iteration-count winners selected before opening the final test.
Crossings are counted on the complete arrays.}
\label{tab:test}
\begin{tabular}{rlrrr}\toprule
Steps & ID & Validation RMS & Final test RMS & Crossings\\\midrule
@TEST_TABLE@
\bottomrule\end{tabular}
\end{table}

\begin{remark}[Second-step comparison]\label{rem:second}
For the matched path $@PAIR_CUTS@$, the first step (\texttt{@PAIR_FIRST@})
has all-index RMS @PAIR_RMS_FIRST@ and the second step
(\texttt{@PAIR_SECOND@}) has RMS @PAIR_RMS_SECOND@.
The measured answer to whether this second step improves its first step
is \textbf{@PAIR_ANSWER@}. Extra iterations are evaluated rather than assumed
to improve. Both phase definitions remain separately tabulated in the CSV;
their best validation IDs are \texttt{@V10_ID@} and \texttt{@SHARP_ID@}.
\end{remark}

\begin{figure}[htbp]\centering
\includegraphics[width=\textwidth]{error_and_height.png}
\caption{Full-sample signed errors and RMS by dyadic height windows. The
last height window is incomplete. These plots are descriptive after selection.}
\label{fig:errors}
\end{figure}

\section{Output, reproducibility and scope}\label{sec:delivery}
\texttt{zCasanya.bin} has exactly 2,001,052 little-endian binary64 values,
16,008,416 bytes, in the original index order. Its first and last values are
@FIRST@ and @LAST@. Its SHA-256 is
\begin{center}\ttfamily\footnotesize @HASH_A@\\@HASH_B@\end{center}
The delivered copy in the original data directory and the packaged copy
are byte-identical. The package contains all scripts, portable input arrays,
all pilot and full candidate outputs, CSV metrics, error histograms,
height-window results, logs, parameter manifests, numerical checks,
this source and its compiled PDF. Original input files are not changed.

\begin{remark}[Mathematical status]\label{rem:status}
The local-factor evaluation and stable difference are elementary identities;
the iteration is the finite construction specified by the user, with the
phase definition checked against the supplied manuscript. The measured
RMS reductions apply to the supplied finite sample. No uniform moment
bound or multiplicity control at the iterated corrected sampling points
is established here; no conclusion about an asymptotically growing number
of arithmetic Newton steps is inferred. The script contains no appeal to RH.
\end{remark}

\begin{thebibliography}{9}
\bibitem{Aynasac2026}
R.~Ayn\"asac, \emph{The Riemann--von Mangoldt clock and the zeros of the
Riemann zeta function: an exact defect identity, prime cutoffs and a
computable corrected clock}, supplied manuscript, version 10, 2026.
The exact source is archived as \texttt{source/ordinal\_prime\_cutoff\_v10.tex};
no DOI is supplied in that source for the manuscript itself.
\end{thebibliography}
\end{document}
'''
    sci=lambda x:f'{x:.3g}'
    params={'FINAL_RMS':f"{s['all_rms_Casanya']:.10f}",'BASE_RMS':f"{s['all_rms_original']:.10f}",
            'GAIN':f"{s['rms_improvement_percent']:.3f}",'PRIME_COUNT':f"{a['primes']['records']:,}",
            'PRIME_BYTES':f"{a['primes']['bytes']:,}",'HEIGHT_FIRST':f"{a['zLamb']['first'][0]:.7f}",
            'HEIGHT_LAST':f"{a['zLamb']['last'][-1]:.7f}",'DIFF_ERR':sci(q['clock_difference_max_error']),
            'CLOCK_ERR':sci(q['direct_clock_max_roundoff_vs_high_precision']),
            'PHASE_ERR':sci(max(q['phase_max_errors'].values())),
            'FACTOR_ERR':sci(q['local_factor_vs_500_powers_max_error']),
            'N_PILOT':str(n_pilot),'N_FULL':str(n_full),
            'TUNE_RANGE':str(protocol['tuning']),'VAL_RANGE':str(protocol['selection_validation']),
            'TEST_RANGE':str(protocol['untouched_test']),
            'ID':s['selected_id'],'PHASE':c['window'].replace('_',r'\_'),
            'POLICY':c['policy'],'CUTOFFS':str(c['cutoffs']),
            'MAE':f"{float(finalrow['mae']):.10f}",'MEDIAN':f"{float(finalrow['median_abs']):.10f}",
            'MAX':f"{float(finalrow['max_abs']):.10f}",'BETTER':f"{float(finalrow['percent_improved']):.3f}",
            'CROSSINGS':finalrow['nonpositive_gaps'],'OVERALL_TABLE':'\n'.join(table),
            'REGION_TABLE':'\n'.join(regiontable),'TEST_TABLE':'\n'.join(testtable),
            'PAIR_CUTS':str(pair['cutoffs']),'PAIR_FIRST':pair['first_id'],'PAIR_SECOND':pair['second_id'],
            'PAIR_RMS_FIRST':f"{pair['first_all_rms']:.10f}",'PAIR_RMS_SECOND':f"{pair['second_all_rms']:.10f}",
            'PAIR_ANSWER':'yes' if pair['improves'] else 'no',
            'V10_ID':selected_v10['id'],'SHARP_ID':selected_sharp['id'],
            'FIRST':f'{first:.16f}','LAST':f'{last:.16f}',
            'HASH_A':s['sha256'][:32],'HASH_B':s['sha256'][32:]}
    for k,v in params.items():template=template.replace('@'+k+'@',str(v))
    assert '@' not in template
    (out/'zCasanya_summary.tex').write_text(template)
    txt='zCasanya - construccion aritmetica en Python\n\n'+'\n'.join(text)+'\n\n'
    txt+=f"Configuracion seleccionada: {s['selected_id']} {c}\n"
    txt+=f"Reduccion RMS completo: {s['rms_improvement_percent']:.6f}%\n"
    txt+=f"Reduccion frente a 0.1880662998: {s['rms_improvement_percent_vs_task_reference']:.6f}%\n"
    txt+=f"Segundo paso emparejado: {pair}\n\n"
    for region in ['tuning_full','selection_validation','untouched_test','all']:
        txt+=region+': '+json.dumps(get(s['selected_id'],region))+'\n'
    txt+=f"\nRegistros: {s['records']}; bytes: {s['bytes']}; primer valor: {first:.16f}; ultimo: {last:.16f}\n"
    txt+=f"Ruta final original: /Users/vcasana/Documents/·.· MATLAB/·.· bin_unicos/zCasanya.bin\nSHA256: {s['sha256']}\n"
    txt+='\nLa v10 corta p<=X e incluye todos los exponentes. power_sharp corta p^m<=X. No se mezclan.\n'
    txt+='El constructor no abre zeross.bin. La seleccion de parametros usa validacion; el test final se abre despues de fijarla.\n'
    txt+='Se conserva la formula iterativa solicitada, sin amortiguacion, ordenacion, recorte, correcciones ajustadas ni evaluaciones de zeta.\n'
    txt+='Los cruces se publican sin repararlos. La mejora medida no establece uniformidad asintotica de momentos ni multiplicidad en puntos iterados.\n'
    (out/'zCasanya_report.txt').write_text(txt)
    env={'python':sys.version,'numpy':np.__version__,'matplotlib':matplotlib.__version__,
         'platform':platform.platform(),'executable':sys.executable}
    (out/'environment.json').write_text(json.dumps(env,indent=2))
    print(txt)


if __name__=='__main__':main()
