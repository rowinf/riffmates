"""
This type stub file was generated by pyright.
"""

"Functions that help with dynamically creating decorators for views."
class classonlymethod(classmethod):
    def __get__(self, instance, cls=...): # -> Callable[..., Any]:
        ...
    


def method_decorator(decorator, name=...): # -> Callable[..., Callable[..., Any] | type]:
    """
    Convert a function decorator into a method decorator
    """
    ...

def decorator_from_middleware_with_args(middleware_class): # -> Callable[..., Callable[..., _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]]]:
    """
    Like decorator_from_middleware, but return a function
    that accepts the arguments to be passed to the middleware_class.
    Use like::

         cache_page = decorator_from_middleware_with_args(CacheMiddleware)
         # ...

         @cache_page(3600)
         def my_view(request):
             # ...
    """
    ...

def decorator_from_middleware(middleware_class): # -> Callable[..., _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]]:
    """
    Given a middleware class (not an instance), return a view decorator. This
    lets you use middleware functionality on a per-view basis. The middleware
    is created with no params passed.
    """
    ...

def make_middleware_decorator(middleware_class): # -> Callable[..., Callable[..., _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]]]:
    ...

def sync_and_async_middleware(func):
    """
    Mark a middleware factory as returning a hybrid middleware supporting both
    types of request.
    """
    ...

def sync_only_middleware(func):
    """
    Mark a middleware factory as returning a sync middleware.
    This is the default.
    """
    ...

def async_only_middleware(func):
    """Mark a middleware factory as returning an async middleware."""
    ...

