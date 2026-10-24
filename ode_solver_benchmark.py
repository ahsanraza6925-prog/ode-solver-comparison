"""Run: python -m pip install numpy scipy pandas matplotlib
Then: python ode_solver_benchmark.py
Compares established explicit/implicit solvers; not a novel algorithm."""
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
RTOL, ATOL = 1e-6, 1e-9
T = np.linspace(0, 20, 2001)
METHODS = ["RK45", "DOP853", "Radau", "BDF"]
def vdp(mu):
    def f(t,y):
        x,z=y
        return [z, mu*(1-x*x)*z-x]
    return f
problems=[("Van der Pol (mu=1)",vdp(1),[2.,0.]),
          ("Van der Pol (mu=50)",vdp(50),[2.,0.])]
rows=[]
for name,f,y0 in problems:
    ref=solve_ivp(f,(0,20),y0,method="Radau",t_eval=T,rtol=2e-12,atol=2e-14)
    for m in METHODS:
        tic=time.perf_counter()
        s=solve_ivp(f,(0,20),y0,method=m,t_eval=T,rtol=RTOL,atol=ATOL)
        elapsed=time.perf_counter()-tic
        err=float(np.max(np.abs(s.y-ref.y))) if s.success and s.y.shape[1]==len(T) else float("nan")
        rows.append({"problem":name,"method":m,"success":s.success,"nfev":s.nfev,
          "njev":getattr(s,"njev",0),"nlu":getattr(s,"nlu",0),
          "max_abs_state_error_vs_reference":err,"runtime_seconds_single_run":elapsed})
df=pd.DataFrame(rows)
df.to_csv("ode_solver_benchmark_results.csv",index=False)
print(df.to_string(index=False))
for name in df.problem.unique():
    ss=df[df.problem==name]
    plt.plot(ss.method,ss.nfev,marker="o",label=name)
plt.ylabel("RHS evaluations (nfev)"); plt.title("Solver effort at fixed tolerances")
plt.grid(True,alpha=.3); plt.legend(); plt.tight_layout()
plt.savefig("ode_solver_effort.png",dpi=180); plt.show()
