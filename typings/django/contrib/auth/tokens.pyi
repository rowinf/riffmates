"""
This type stub file was generated by pyright.
"""

class PasswordResetTokenGenerator:
    """
    Strategy object used to generate and check tokens for the password
    reset mechanism.
    """
    key_salt = ...
    algorithm = ...
    _secret = ...
    _secret_fallbacks = ...
    def __init__(self) -> None:
        ...
    
    secret = ...
    secret_fallbacks = ...
    def make_token(self, user): # -> str:
        """
        Return a token that can be used once to do a password reset
        for the given user.
        """
        ...
    
    def check_token(self, user, token): # -> bool:
        """
        Check that a password reset token is correct for a given user.
        """
        ...
    


default_token_generator = ...