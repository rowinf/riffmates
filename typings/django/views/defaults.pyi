"""
This type stub file was generated by pyright.
"""

from django.views.decorators.csrf import requires_csrf_token

ERROR_404_TEMPLATE_NAME = ...
ERROR_403_TEMPLATE_NAME = ...
ERROR_400_TEMPLATE_NAME = ...
ERROR_500_TEMPLATE_NAME = ...
ERROR_PAGE_TEMPLATE = ...
@requires_csrf_token
def page_not_found(request, exception, template_name=...): # -> HttpResponseNotFound:
    """
    Default 404 handler.

    Templates: :template:`404.html`
    Context:
        request_path
            The path of the requested URL (e.g., '/app/pages/bad_page/'). It's
            quoted to prevent a content injection attack.
        exception
            The message from the exception which triggered the 404 (if one was
            supplied), or the exception class name
    """
    ...

@requires_csrf_token
def server_error(request, template_name=...): # -> HttpResponseServerError:
    """
    500 error handler.

    Templates: :template:`500.html`
    Context: None
    """
    ...

@requires_csrf_token
def bad_request(request, exception, template_name=...): # -> HttpResponseBadRequest:
    """
    400 error handler.

    Templates: :template:`400.html`
    Context: None
    """
    ...

@requires_csrf_token
def permission_denied(request, exception, template_name=...): # -> HttpResponseForbidden:
    """
    Permission denied (403) handler.

    Templates: :template:`403.html`
    Context:
        exception
            The message from the exception which triggered the 403 (if one was
            supplied).

    If the template does not exist, an Http403 response containing the text
    "403 Forbidden" (as per RFC 9110 Section 15.5.4) will be returned.
    """
    ...
