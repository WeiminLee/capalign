import json, sys, math
inp = json.load(open(sys.argv[1]))
freqs = inp["frequencies"]
tmin, tmax, tstep = inp["tmin"], inp["tmax"], inp["tstep"]
# harmonic phonon thermal properties, hbar=kB=1 (fixture convention)
def row(T):
    F = S = Cv = 0.0
    for w in freqs:
        x = w / T
        e = math.exp(-x)
        F += T * math.log(1.0 - e)          # zero point + T ln(1-e^-x)
        S += (w / T) / (math.exp(x) - 1.0) - math.log(1.0 - e)
        Cv += x * x * math.exp(x) / ((math.exp(x) - 1.0) ** 2)
    return F, S, Cv
temps, Fs, Ss, Cvs = [], [], [], []
T = tmin
while T <= tmax + 1e-12:
    F, S, Cv = row(T)
    temps.append(T); Fs.append(F); Ss.append(S); Cvs.append(Cv)
    T = round(T + tstep, 12)
out = {"temperatures": temps, "free_energies": Fs, "entropies": Ss, "heat_capacities": Cvs}
open("thermo.json", "w").write(json.dumps(out))
print("OK thermo.json %d temperatures" % len(temps))
