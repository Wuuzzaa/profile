"""
Taken from https://stackoverflow.com/a/5376616

Decorator to profile the performance of a function/method. Profiles the function and saves the output.

See: https://docs.python.org/3.8/library/profile.html#module-cProfile
"""

import cProfile

def profileit(func):
    def wrapper(*args, **kwargs):
        datafn = func.__name__ + ".profile"
        prof = cProfile.Profile()
        retval = prof.runcall(func, *args, **kwargs)
        prof.dump_stats(datafn)
        return retval

    return wrapper
