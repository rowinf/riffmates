"""
This type stub file was generated by pyright.
"""

from django.utils.deconstruct import deconstructible

EMPTY_VALUES = ...
@deconstructible
class RegexValidator:
    regex = ...
    message = ...
    code = ...
    inverse_match = ...
    flags = ...
    def __init__(self, regex=..., message=..., code=..., inverse_match=..., flags=...) -> None:
        ...
    
    def __call__(self, value): # -> None:
        """
        Validate that the input contains (or does *not* contain, if
        inverse_match is True) a match for the regular expression.
        """
        ...
    
    def __eq__(self, other) -> bool:
        ...
    


@deconstructible
class URLValidator(RegexValidator):
    ul = ...
    ipv4_re = ...
    ipv6_re = ...
    hostname_re = ...
    domain_re = ...
    tld_re = ...
    host_re = ...
    regex = ...
    message = ...
    schemes = ...
    unsafe_chars = ...
    max_length = ...
    def __init__(self, schemes=..., **kwargs) -> None:
        ...
    
    def __call__(self, value): # -> None:
        ...
    


integer_validator = ...
def validate_integer(value): # -> None:
    ...

@deconstructible
class EmailValidator:
    message = ...
    code = ...
    user_regex = ...
    domain_regex = ...
    literal_regex = ...
    domain_allowlist = ...
    def __init__(self, message=..., code=..., allowlist=...) -> None:
        ...
    
    def __call__(self, value): # -> None:
        ...
    
    def validate_domain_part(self, domain_part): # -> bool:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    


validate_email = ...
slug_re = ...
validate_slug = ...
slug_unicode_re = ...
validate_unicode_slug = ...
def validate_ipv4_address(value): # -> None:
    ...

def validate_ipv6_address(value): # -> None:
    ...

def validate_ipv46_address(value): # -> None:
    ...

ip_address_validator_map = ...
def ip_address_validators(protocol, unpack_ipv4): # -> tuple[list[Callable[..., None]], __proxy__]:
    """
    Depending on the given parameters, return the appropriate validators for
    the GenericIPAddressField.
    """
    ...

def int_list_validator(sep=..., message=..., code=..., allow_negative=...): # -> RegexValidator:
    ...

validate_comma_separated_integer_list = ...
@deconstructible
class BaseValidator:
    message = ...
    code = ...
    def __init__(self, limit_value, message=...) -> None:
        ...
    
    def __call__(self, value): # -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def compare(self, a, b): # -> bool:
        ...
    
    def clean(self, x):
        ...
    


@deconstructible
class MaxValueValidator(BaseValidator):
    message = ...
    code = ...
    def compare(self, a, b):
        ...
    


@deconstructible
class MinValueValidator(BaseValidator):
    message = ...
    code = ...
    def compare(self, a, b):
        ...
    


@deconstructible
class StepValueValidator(BaseValidator):
    message = ...
    code = ...
    def compare(self, a, b): # -> bool:
        ...
    


@deconstructible
class MinLengthValidator(BaseValidator):
    message = ...
    code = ...
    def compare(self, a, b):
        ...
    
    def clean(self, x): # -> int:
        ...
    


@deconstructible
class MaxLengthValidator(BaseValidator):
    message = ...
    code = ...
    def compare(self, a, b):
        ...
    
    def clean(self, x): # -> int:
        ...
    


@deconstructible
class DecimalValidator:
    """
    Validate that the input does not exceed the maximum number of digits
    expected, otherwise raise ValidationError.
    """
    messages = ...
    def __init__(self, max_digits, decimal_places) -> None:
        ...
    
    def __call__(self, value): # -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    


@deconstructible
class FileExtensionValidator:
    message = ...
    code = ...
    def __init__(self, allowed_extensions=..., message=..., code=...) -> None:
        ...
    
    def __call__(self, value): # -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    


def get_available_image_extensions(): # -> list[Any]:
    ...

def validate_image_file_extension(value): # -> None:
    ...

@deconstructible
class ProhibitNullCharactersValidator:
    """Validate that the string doesn't contain the null character."""
    message = ...
    code = ...
    def __init__(self, message=..., code=...) -> None:
        ...
    
    def __call__(self, value): # -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    


