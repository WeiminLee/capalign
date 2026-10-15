import json, sys, math
inp = json.load(open(sys.argv[1]))
freqs, sigma = inp["frequencies"], inp["sigma"]
fmin, fmax, fpitch = inp["fmin"], inp["fmax"], inp["fpitch"]
norm = 1.0 / (sigma * math.sqrt(2.0 * math.pi))
grid, dos = [], []
x = fmin
while x <= fmax + 1e-12:
    s = sum(math.exp(-((x - w) ** 2) / (2.0 * sigma * sigma)) * norm for w in freqs)
    grid.append(x); dos.append(s)
    x = round(x + fpitch, 12)
open("dos.json", "w").write(json.dumps({"grid": grid, "dos": dos}))
print("OK dos.json %d points" % len(grid))
