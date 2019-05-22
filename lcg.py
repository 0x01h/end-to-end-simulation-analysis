import time


class LCG:
    def __init__(self, seed=time.time()):
        self.set_seed_lcg(seed)

    # Set a starting seed for LCG.
    def set_seed_lcg(self, seed):  # Timestamp as a seed for default.
        global rand
        rand = float(seed)

    # Parameters taken from https://www.wikiwand.com/en/Numerical_Recipes
    # "Numerical Recipes: The Art of Scientific Computing", William H. Press, Saul A. Teukolsky, William T. Vetterling and Brian P. Flannery.
    def custom_uniform(self, low_lim=0.0, up_lim=100.0, precision=True):
        # Linear Congruential Method
        # x1 = (x0 * a + c) % m
        a = 1664525
        c = 1013904223
        m = 2**32 - 1  # -1 is for precision.
        global rand
        rand = (((a*rand + c) % m) % up_lim) + low_lim
        # Get precision between 0 and 1.
        if (precision):
            rand = rand + self.custom_uniform(0, 1000, False) / 1000
        if up_lim == 1:
            rand = rand % 1
        else:
            rand
        return rand
