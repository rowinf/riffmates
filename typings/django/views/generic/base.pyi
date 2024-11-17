"""
This type stub file was generated by pyright.
"""

from django.template.response import TemplateResponse
from django.utils.decorators import classonlymethod
from django.utils.functional import classproperty

logger = ...
class ContextMixin:
    """
    A default context mixin that passes the keyword arguments received by
    get_context_data() as the template context.
    """
    extra_context = ...
    def get_context_data(self, **kwargs): # -> dict[str, Any]:
        ...
    


class View:
    """
    Intentionally simple parent class for all views. Only implements
    dispatch-by-method and simple sanity checking.
    """
    http_method_names = ...
    def __init__(self, **kwargs) -> None:
        """
        Constructor. Called in the URLconf; can contain helpful extra
        keyword arguments, and other things.
        """
        ...
    
    @classproperty
    def view_is_async(cls): # -> bool:
        ...
    
    @classonlymethod
    def as_view(cls, **initkwargs): # -> Callable[..., Any]:
        """Main entry point for a request-response process."""
        ...
    
    def setup(self, request, *args, **kwargs): # -> None:
        """Initialize attributes shared by all view methods."""
        ...
    
    def dispatch(self, request, *args, **kwargs): # -> Coroutine[Any, Any, HttpResponseNotAllowed] | HttpResponseNotAllowed | Any:
        ...
    
    def http_method_not_allowed(self, request, *args, **kwargs): # -> Coroutine[Any, Any, HttpResponseNotAllowed] | HttpResponseNotAllowed:
        ...
    
    def options(self, request, *args, **kwargs): # -> Coroutine[Any, Any, HttpResponse] | HttpResponse:
        """Handle responding to requests for the OPTIONS HTTP verb."""
        ...
    


class TemplateResponseMixin:
    """A mixin that can be used to render a template."""
    template_name = ...
    template_engine = ...
    response_class = TemplateResponse
    content_type = ...
    def render_to_response(self, context, **response_kwargs): # -> response_class:
        """
        Return a response, using the `response_class` for this view, with a
        template rendered with the given context.

        Pass response_kwargs to the constructor of the response class.
        """
        ...
    
    def get_template_names(self): # -> list[Never]:
        """
        Return a list of template names to be used for the request. Must return
        a list. May not be called if render_to_response() is overridden.
        """
        ...
    


class TemplateView(TemplateResponseMixin, ContextMixin, View):
    """
    Render a template. Pass keyword arguments from the URLconf to the context.
    """
    def get(self, request, *args, **kwargs): # -> response_class:
        ...
    


class RedirectView(View):
    """Provide a redirect on any GET request."""
    permanent = ...
    url = ...
    pattern_name = ...
    query_string = ...
    def get_redirect_url(self, *args, **kwargs): # -> str | None:
        """
        Return the URL redirect to. Keyword arguments from the URL pattern
        match generating the redirect request are provided as kwargs to this
        method.
        """
        ...
    
    def get(self, request, *args, **kwargs): # -> HttpResponsePermanentRedirect | HttpResponseRedirect | HttpResponseGone:
        ...
    
    def head(self, request, *args, **kwargs): # -> HttpResponsePermanentRedirect | HttpResponseRedirect | HttpResponseGone:
        ...
    
    def post(self, request, *args, **kwargs): # -> HttpResponsePermanentRedirect | HttpResponseRedirect | HttpResponseGone:
        ...
    
    def options(self, request, *args, **kwargs): # -> HttpResponsePermanentRedirect | HttpResponseRedirect | HttpResponseGone:
        ...
    
    def delete(self, request, *args, **kwargs): # -> HttpResponsePermanentRedirect | HttpResponseRedirect | HttpResponseGone:
        ...
    
    def put(self, request, *args, **kwargs): # -> HttpResponsePermanentRedirect | HttpResponseRedirect | HttpResponseGone:
        ...
    
    def patch(self, request, *args, **kwargs): # -> HttpResponsePermanentRedirect | HttpResponseRedirect | HttpResponseGone:
        ...
    


