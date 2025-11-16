# another_module.py
import goodbye  # importing whole module as a name

from goodbye import nested  # module from package
from hello import hello  # name from a module


print(globals()["goodbye"])
print(globals()["hello"])
print(globals()["nested"])

