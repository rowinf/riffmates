"""
This type stub file was generated by pyright.
"""

import django.core.checks.async_checks
import django.core.checks.caches
import django.core.checks.compatibility.django_4_0
import django.core.checks.database
import django.core.checks.files
import django.core.checks.model_checks
import django.core.checks.security.base
import django.core.checks.security.csrf
import django.core.checks.security.sessions
import django.core.checks.templates
import django.core.checks.translation
import django.core.checks.urls
from .messages import CRITICAL, CheckMessage, Critical, DEBUG, Debug, ERROR, Error, INFO, Info, WARNING, Warning
from .registry import Tags, register, run_checks, tag_exists

__all__ = ["CheckMessage", "Debug", "Info", "Warning", "Error", "Critical", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL", "register", "run_checks", "tag_exists", "Tags"]
