import random

def markov_pi(N, delta): 
    x, y = 1.0, 1.0
    n_hits = 0
    num_moves = 0
    for i in range(N):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
            num_moves +=1
        if x**2 + y**2 < 1.0: n_hits += 1
    print num_moves/float(n_trials)
    return n_hits

n_runs = 500
n_trials = 1000
delta = 0.1
for run in range(n_runs):
    print 4.0 * markov_pi(n_trials, delta) / float(n_trials)
