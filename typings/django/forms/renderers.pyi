"""
This type stub file was generated by pyright.
"""

import functools
from django.template.backends.django import DjangoTemplates
from django.utils.functional import cached_property

@functools.lru_cache
def get_default_renderer(): # -> Any:
    ...

class BaseRenderer:
    form_template_name = ...
    formset_template_name = ...
    def get_template(self, template_name):
        ...
    
    def render(self, template_name, context, request=...):
        ...
    


class EngineMixin:
    def get_template(self, template_name):
        ...
    
    @cached_property
    def engine(self):
        ...
    


class DjangoTemplates(EngineMixin, BaseRenderer):
    """
    Load Django templates from the built-in widget templates in
    django/forms/templates and from apps' 'templates' directory.
    """
    backend = DjangoTemplates


class Jinja2(EngineMixin, BaseRenderer):
    """
    Load Jinja2 templates from the built-in widget templates in
    django/forms/jinja2 and from apps' 'jinja2' directory.
    """
    @cached_property
    def backend(self): # -> type[Jinja2]:
        ...
    


class DjangoDivFormRenderer(DjangoTemplates):
    """
    Load Django templates from django/forms/templates and from apps'
    'templates' directory and use the 'div.html' template to render forms and
    formsets.
    """
    form_template_name = ...
    formset_template_name = ...


class Jinja2DivFormRenderer(Jinja2):
    """
    Load Jinja2 templates from the built-in widget templates in
    django/forms/jinja2 and from apps' 'jinja2' directory.
    """
    form_template_name = ...
    formset_template_name = ...


class TemplatesSetting(BaseRenderer):
    """
    Load templates using template.loader.get_template() which is configured
    based on settings.TEMPLATES.
    """
    def get_template(self, template_name): # -> Any:
        ...
    


