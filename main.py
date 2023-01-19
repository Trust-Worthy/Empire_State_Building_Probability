import numpy as np
from matplotlib import pyplot as plt

# simulating rolling the die 100 times
def single_sim():
    track_steps = []
    for i in range(100):
        step = 0
        die = np.random.randint(1,7)
        if die <= 2:
            max(0,step - 1) # ensures that person can't go below step 0
        elif die < 6:
            step += 1
        else:
            step = step + np.random.randint(1,7)
        track_steps.append(step)
    
    return track_steps

def main():
    track_steps = single_sim()
    print(track_steps)

if __name__ == "__main__":
    main()




