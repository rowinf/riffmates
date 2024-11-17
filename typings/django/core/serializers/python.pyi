"""
This type stub file was generated by pyright.
"""

from django.core.serializers import base

"""
A Python "serializer". Doesn't do much serializing per se -- just converts to
and from basic Python data types (lists, dicts, strings, etc.). Useful as a basis for
other serializers.
"""
class Serializer(base.Serializer):
    """
    Serialize a QuerySet to basic Python objects.
    """
    internal_use_only = ...
    def start_serialization(self): # -> None:
        ...
    
    def end_serialization(self): # -> None:
        ...
    
    def start_object(self, obj): # -> None:
        ...
    
    def end_object(self, obj): # -> None:
        ...
    
    def get_dump_object(self, obj): # -> dict[str, str]:
        ...
    
    def handle_field(self, obj, field): # -> None:
        ...
    
    def handle_fk_field(self, obj, field): # -> None:
        ...
    
    def handle_m2m_field(self, obj, field): # -> None:
        ...
    
    def getvalue(self): # -> list[Any]:
        ...
    


def Deserializer(object_list, *, using=..., ignorenonexistent=..., **options): # -> Generator[DeserializedObject, Any, None]:
    """
    Deserialize simple Python objects back into Django ORM instances.

    It's expected that you pass the Python objects themselves (instead of a
    stream or a string) to the constructor
    """
    ...

