"""
This type stub file was generated by pyright.
"""

import hashlib
from django.utils.inspect import func_supports_parameter

"""
Django's standard crypto functions and utilities.
"""
class InvalidAlgorithm(ValueError):
    """Algorithm is not supported by hashlib."""
    ...


def salted_hmac(key_salt, value, secret=..., *, algorithm=...): # -> HMAC:
    """
    Return the HMAC of 'value', using a key generated from key_salt and a
    secret (which defaults to settings.SECRET_KEY). Default algorithm is SHA1,
    but any algorithm name supported by hashlib can be passed.

    A different key_salt should be passed in for every application of HMAC.
    """
    ...

RANDOM_STRING_CHARS = ...
def get_random_string(length, allowed_chars=...): # -> str:
    """
    Return a securely generated random string.

    The bit length of the returned value can be calculated with the formula:
        log_2(len(allowed_chars)^length)

    For example, with default `allowed_chars` (26+26+10), this gives:
      * length: 12, bit length =~ 71 bits
      * length: 22, bit length =~ 131 bits
    """
    ...

def constant_time_compare(val1, val2): # -> bool:
    """Return True if the two strings are equal, False otherwise."""
    ...

def pbkdf2(password, salt, iterations, dklen=..., digest=...): # -> bytes:
    """Return the hash of password using pbkdf2."""
    ...

if func_supports_parameter(hashlib.md5, "usedforsecurity"):
    md5 = ...
    new_hash = ...
else:
    def md5(data=..., *, usedforsecurity=...): # -> _Hash:
        ...
    
    def new_hash(hash_algorithm, *, usedforsecurity=...): # -> _Hash:
        ...
    
