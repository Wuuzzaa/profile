# profil
Repository for performance and memory profiling.

## Performance
You can use the decorator (profile_decorator.py) and watch the results with the viewer.

## Memory
Memory monitoring is not as easy in Python as in C/C++. 

Do NOT use 

```python
sys.getsizeof()
``` 

because it only measures the references and not the true memory needed of the maybe stored objects in an list etc.

There are some usefull modules:

- https://pypi.org/project/Pympler/
- https://pypi.org/project/memory-profiler/


