"""
This type stub file was generated by pyright.
"""

from io import IOBase
from django.core.handlers.base import BaseHandler

__all__ = ("AsyncClient", "AsyncRequestFactory", "Client", "RedirectCycleError", "RequestFactory", "encode_file", "encode_multipart")
BOUNDARY = ...
MULTIPART_CONTENT = ...
CONTENT_TYPE_RE = ...
JSON_CONTENT_TYPE_RE = ...
class RedirectCycleError(Exception):
    """The test client has been asked to follow a redirect loop."""
    def __init__(self, message, last_response) -> None:
        ...
    


class FakePayload(IOBase):
    """
    A wrapper around BytesIO that restricts what can be read since data from
    the network can't be sought and cannot be read outside of its content
    length. This makes sure that views can't do anything under the test client
    that wouldn't work in real life.
    """
    def __init__(self, initial_bytes=...) -> None:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def read(self, size=..., /): # -> bytes:
        ...
    
    def readline(self, size=..., /): # -> bytes:
        ...
    
    def write(self, b, /): # -> None:
        ...
    


def closing_iterator_wrapper(iterable, close): # -> Generator[Any, Any, None]:
    ...

async def aclosing_iterator_wrapper(iterable, close): # -> Generator[Any, Any, None]:
    ...

def conditional_content_removal(request, response):
    """
    Simulate the behavior of most web servers by removing the content of
    responses for HEAD requests, 1xx, 204, and 304 responses. Ensure
    compliance with RFC 9112 Section 6.3.
    """
    ...

class ClientHandler(BaseHandler):
    """
    An HTTP Handler that can be used for testing purposes. Use the WSGI
    interface to compose requests, but return the raw HttpResponse object with
    the originating WSGIRequest attached to its ``wsgi_request`` attribute.
    """
    def __init__(self, enforce_csrf_checks=..., *args, **kwargs) -> None:
        ...
    
    def __call__(self, environ): # -> Coroutine[Any, Any, Any]:
        ...
    


class AsyncClientHandler(BaseHandler):
    """An async version of ClientHandler."""
    def __init__(self, enforce_csrf_checks=..., *args, **kwargs) -> None:
        ...
    
    async def __call__(self, scope):
        ...
    


def store_rendered_templates(store, signal, sender, template, context, **kwargs): # -> None:
    """
    Store templates and contexts that are rendered.

    The context is copied so that it is an accurate representation at the time
    of rendering.
    """
    ...

def encode_multipart(boundary, data): # -> bytes:
    """
    Encode multipart POST data from a dictionary of form values.

    The key will be used as the form data name; the value will be transmitted
    as content. If the value is a file, the contents of the file will be sent
    as an application/octet-stream; otherwise, str(value) will be sent.
    """
    ...

def encode_file(boundary, key, file): # -> list[Any]:
    ...

class RequestFactory:
    """
    Class that lets you create mock Request objects for use in testing.

    Usage:

    rf = RequestFactory()
    get_request = rf.get('/hello/')
    post_request = rf.post('/submit/', {'foo': 'bar'})

    Once you have a request object you can pass it to any view function,
    just as if that view had been hooked up using a URLconf.
    """
    def __init__(self, *, json_encoder=..., headers=..., **defaults) -> None:
        ...
    
    def request(self, **request): # -> WSGIRequest:
        "Construct a generic request object."
        ...
    
    def get(self, path, data=..., secure=..., *, headers=..., **extra): # -> WSGIRequest:
        """Construct a GET request."""
        ...
    
    def post(self, path, data=..., content_type=..., secure=..., *, headers=..., **extra): # -> WSGIRequest:
        """Construct a POST request."""
        ...
    
    def head(self, path, data=..., secure=..., *, headers=..., **extra): # -> WSGIRequest:
        """Construct a HEAD request."""
        ...
    
    def trace(self, path, secure=..., *, headers=..., **extra): # -> WSGIRequest:
        """Construct a TRACE request."""
        ...
    
    def options(self, path, data=..., content_type=..., secure=..., *, headers=..., **extra): # -> WSGIRequest:
        "Construct an OPTIONS request."
        ...
    
    def put(self, path, data=..., content_type=..., secure=..., *, headers=..., **extra): # -> WSGIRequest:
        """Construct a PUT request."""
        ...
    
    def patch(self, path, data=..., content_type=..., secure=..., *, headers=..., **extra): # -> WSGIRequest:
        """Construct a PATCH request."""
        ...
    
    def delete(self, path, data=..., content_type=..., secure=..., *, headers=..., **extra): # -> WSGIRequest:
        """Construct a DELETE request."""
        ...
    
    def generic(self, method, path, data=..., content_type=..., secure=..., *, headers=..., **extra): # -> WSGIRequest:
        """Construct an arbitrary HTTP request."""
        ...
    


class AsyncRequestFactory(RequestFactory):
    """
    Class that lets you create mock ASGI-like Request objects for use in
    testing. Usage:

    rf = AsyncRequestFactory()
    get_request = await rf.get('/hello/')
    post_request = await rf.post('/submit/', {'foo': 'bar'})

    Once you have a request object you can pass it to any view function,
    including synchronous ones. The reason we have a separate class here is:
    a) this makes ASGIRequest subclasses, and
    b) AsyncTestClient can subclass it.
    """
    def request(self, **request): # -> ASGIRequest:
        """Construct a generic request object."""
        ...
    
    def generic(self, method, path, data=..., content_type=..., secure=..., *, headers=..., **extra): # -> ASGIRequest:
        """Construct an arbitrary HTTP request."""
        ...
    


class ClientMixin:
    """
    Mixin with common methods between Client and AsyncClient.
    """
    def store_exc_info(self, **kwargs): # -> None:
        """Store exceptions when they are generated by a view."""
        ...
    
    def check_exception(self, response): # -> None:
        """
        Look for a signaled exception, clear the current context exception
        data, re-raise the signaled exception, and clear the signaled exception
        from the local cache.
        """
        ...
    
    @property
    def session(self): # -> Any:
        """Return the current session variables."""
        ...
    
    def login(self, **credentials): # -> bool:
        """
        Set the Factory to appear as if it has successfully logged into a site.

        Return True if login is possible or False if the provided credentials
        are incorrect.
        """
        ...
    
    def force_login(self, user, backend=...): # -> None:
        ...
    
    def logout(self): # -> None:
        """Log out the user by removing the cookies and session object."""
        ...
    


class Client(ClientMixin, RequestFactory):
    """
    A class that can act as a client for testing purposes.

    It allows the user to compose GET and POST requests, and
    obtain the response that the server gave to those requests.
    The server Response objects are annotated with the details
    of the contexts and templates that were rendered during the
    process of serving the request.

    Client objects are stateful - they will retain cookie (and
    thus session) details for the lifetime of the Client instance.

    This is not intended as a replacement for Twill/Selenium or
    the like - it is here to allow testing against the
    contexts and templates produced by a view, rather than the
    HTML rendered to the end-user.
    """
    def __init__(self, enforce_csrf_checks=..., raise_request_exception=..., *, headers=..., **defaults) -> None:
        ...
    
    def request(self, **request): # -> Coroutine[Any, Any, Any]:
        """
        Make a generic request. Compose the environment dictionary and pass
        to the handler, return the result of the handler. Assume defaults for
        the query environment, which can be overridden using the arguments to
        the request.
        """
        ...
    
    def get(self, path, data=..., follow=..., secure=..., *, headers=..., **extra): # -> Any | WSGIRequest:
        """Request a response from the server using GET."""
        ...
    
    def post(self, path, data=..., content_type=..., follow=..., secure=..., *, headers=..., **extra): # -> Any | WSGIRequest:
        """Request a response from the server using POST."""
        ...
    
    def head(self, path, data=..., follow=..., secure=..., *, headers=..., **extra): # -> Any | WSGIRequest:
        """Request a response from the server using HEAD."""
        ...
    
    def options(self, path, data=..., content_type=..., follow=..., secure=..., *, headers=..., **extra): # -> Any | WSGIRequest:
        """Request a response from the server using OPTIONS."""
        ...
    
    def put(self, path, data=..., content_type=..., follow=..., secure=..., *, headers=..., **extra): # -> Any | WSGIRequest:
        """Send a resource to the server using PUT."""
        ...
    
    def patch(self, path, data=..., content_type=..., follow=..., secure=..., *, headers=..., **extra): # -> Any | WSGIRequest:
        """Send a resource to the server using PATCH."""
        ...
    
    def delete(self, path, data=..., content_type=..., follow=..., secure=..., *, headers=..., **extra): # -> Any | WSGIRequest:
        """Send a DELETE request to the server."""
        ...
    
    def trace(self, path, data=..., follow=..., secure=..., *, headers=..., **extra): # -> Any | WSGIRequest:
        """Send a TRACE request to the server."""
        ...
    


class AsyncClient(ClientMixin, AsyncRequestFactory):
    """
    An async version of Client that creates ASGIRequests and calls through an
    async request path.

    Does not currently support "follow" on its methods.
    """
    def __init__(self, enforce_csrf_checks=..., raise_request_exception=..., *, headers=..., **defaults) -> None:
        ...
    
    async def request(self, **request):
        """
        Make a generic request. Compose the scope dictionary and pass to the
        handler, return the result of the handler. Assume defaults for the
        query environment, which can be overridden using the arguments to the
        request.
        """
        ...
    


