"""
Little script to view a cprofiler file. Just change the filename variable and run.

For options and parameters see: https://docs.python.org/2/library/profile.html#pstats.Stats
"""
import pstats

filename = "main.profile"

stats = pstats.Stats(filename)
stats.sort_stats("cumtime")
stats.print_stats(20)
#stats.print_callers()
stats.print_callees(20)
