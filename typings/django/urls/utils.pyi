"""
This type stub file was generated by pyright.
"""

import functools

@functools.lru_cache(maxsize=None)
def get_callable(lookup_view): # -> Callable[..., object]:
    """
    Return a callable corresponding to lookup_view.
    * If lookup_view is already a callable, return it.
    * If lookup_view is a string import path that can be resolved to a callable,
      import that callable and return it, otherwise raise an exception
      (ImportError or ViewDoesNotExist).
    """
    ...

def get_mod_func(callback): # -> tuple[Any, Literal['']] | tuple[Any, Any]:
    ...
