"""
This type stub file was generated by pyright.
"""

from django.db.models.query_utils import DeferredAttribute
from django.db.models.utils import AltersData
from django.utils.functional import cached_property

"""
Accessors for related objects.

When a field defines a relation between two models, each model class provides
an attribute to access related instances of the other model class (unless the
reverse accessor has been disabled with related_name='+').

Accessors are implemented as descriptors in order to customize access and
assignment. This module defines the descriptor classes.

Forward accessors follow foreign keys. Reverse accessors trace them back. For
example, with the following models::

    class Parent(Model):
        pass

    class Child(Model):
        parent = ForeignKey(Parent, related_name='children')

 ``child.parent`` is a forward many-to-one relation. ``parent.children`` is a
reverse many-to-one relation.

There are three types of relations (many-to-one, one-to-one, and many-to-many)
and two directions (forward and reverse) for a total of six combinations.

1. Related instance on the forward side of a many-to-one relation:
   ``ForwardManyToOneDescriptor``.

   Uniqueness of foreign key values is irrelevant to accessing the related
   instance, making the many-to-one and one-to-one cases identical as far as
   the descriptor is concerned. The constraint is checked upstream (unicity
   validation in forms) or downstream (unique indexes in the database).

2. Related instance on the forward side of a one-to-one
   relation: ``ForwardOneToOneDescriptor``.

   It avoids querying the database when accessing the parent link field in
   a multi-table inheritance scenario.

3. Related instance on the reverse side of a one-to-one relation:
   ``ReverseOneToOneDescriptor``.

   One-to-one relations are asymmetrical, despite the apparent symmetry of the
   name, because they're implemented in the database with a foreign key from
   one table to another. As a consequence ``ReverseOneToOneDescriptor`` is
   slightly different from ``ForwardManyToOneDescriptor``.

4. Related objects manager for related instances on the reverse side of a
   many-to-one relation: ``ReverseManyToOneDescriptor``.

   Unlike the previous two classes, this one provides access to a collection
   of objects. It returns a manager rather than an instance.

5. Related objects manager for related instances on the forward or reverse
   sides of a many-to-many relation: ``ManyToManyDescriptor``.

   Many-to-many relations are symmetrical. The syntax of Django models
   requires declaring them on one side but that's an implementation detail.
   They could be declared on the other side without any change in behavior.
   Therefore the forward and reverse descriptors can be the same.

   If you're looking for ``ForwardManyToManyDescriptor`` or
   ``ReverseManyToManyDescriptor``, use ``ManyToManyDescriptor`` instead.
"""
class ForeignKeyDeferredAttribute(DeferredAttribute):
    def __set__(self, instance, value): # -> None:
        ...
    


class ForwardManyToOneDescriptor:
    """
    Accessor to the related object on the forward side of a many-to-one or
    one-to-one (via ForwardOneToOneDescriptor subclass) relation.

    In the example::

        class Child(Model):
            parent = ForeignKey(Parent, related_name='children')

    ``Child.parent`` is a ``ForwardManyToOneDescriptor`` instance.
    """
    def __init__(self, field_with_rel) -> None:
        ...
    
    @cached_property
    def RelatedObjectDoesNotExist(self): # -> type[RelatedObjectDoesNotExist]:
        ...
    
    def is_cached(self, instance):
        ...
    
    def get_queryset(self, **hints):
        ...
    
    def get_prefetch_queryset(self, instances, queryset=...): # -> tuple[Any, Any, Any, Literal[True], Any, Literal[False]]:
        ...
    
    def get_object(self, instance):
        ...
    
    def __get__(self, instance, cls=...): # -> Self | None:
        """
        Get the related instance through the forward relation.

        With the example above, when getting ``child.parent``:

        - ``self`` is the descriptor managing the ``parent`` attribute
        - ``instance`` is the ``child`` instance
        - ``cls`` is the ``Child`` class (we don't need it)
        """
        ...
    
    def __set__(self, instance, value): # -> None:
        """
        Set the related instance through the forward relation.

        With the example above, when setting ``child.parent = parent``:

        - ``self`` is the descriptor managing the ``parent`` attribute
        - ``instance`` is the ``child`` instance
        - ``value`` is the ``parent`` instance on the right of the equal sign
        """
        ...
    
    def __reduce__(self): # -> tuple[Callable[..., Any], tuple[Any, Any]]:
        """
        Pickling should return the instance attached by self.field on the
        model, not a new copy of that descriptor. Use getattr() to retrieve
        the instance directly from the model.
        """
        ...
    


class ForwardOneToOneDescriptor(ForwardManyToOneDescriptor):
    """
    Accessor to the related object on the forward side of a one-to-one relation.

    In the example::

        class Restaurant(Model):
            place = OneToOneField(Place, related_name='restaurant')

    ``Restaurant.place`` is a ``ForwardOneToOneDescriptor`` instance.
    """
    def get_object(self, instance):
        ...
    
    def __set__(self, instance, value): # -> None:
        ...
    


class ReverseOneToOneDescriptor:
    """
    Accessor to the related object on the reverse side of a one-to-one
    relation.

    In the example::

        class Restaurant(Model):
            place = OneToOneField(Place, related_name='restaurant')

    ``Place.restaurant`` is a ``ReverseOneToOneDescriptor`` instance.
    """
    def __init__(self, related) -> None:
        ...
    
    @cached_property
    def RelatedObjectDoesNotExist(self): # -> type[RelatedObjectDoesNotExist]:
        ...
    
    def is_cached(self, instance):
        ...
    
    def get_queryset(self, **hints):
        ...
    
    def get_prefetch_queryset(self, instances, queryset=...): # -> tuple[Any, Any, Any, Literal[True], Any, Literal[False]]:
        ...
    
    def __get__(self, instance, cls=...): # -> Self:
        """
        Get the related instance through the reverse relation.

        With the example above, when getting ``place.restaurant``:

        - ``self`` is the descriptor managing the ``restaurant`` attribute
        - ``instance`` is the ``place`` instance
        - ``cls`` is the ``Place`` class (unused)

        Keep in mind that ``Restaurant`` holds the foreign key to ``Place``.
        """
        ...
    
    def __set__(self, instance, value): # -> None:
        """
        Set the related instance through the reverse relation.

        With the example above, when setting ``place.restaurant = restaurant``:

        - ``self`` is the descriptor managing the ``restaurant`` attribute
        - ``instance`` is the ``place`` instance
        - ``value`` is the ``restaurant`` instance on the right of the equal sign

        Keep in mind that ``Restaurant`` holds the foreign key to ``Place``.
        """
        ...
    
    def __reduce__(self): # -> tuple[Callable[..., Any], tuple[Any, Any]]:
        ...
    


class ReverseManyToOneDescriptor:
    """
    Accessor to the related objects manager on the reverse side of a
    many-to-one relation.

    In the example::

        class Child(Model):
            parent = ForeignKey(Parent, related_name='children')

    ``Parent.children`` is a ``ReverseManyToOneDescriptor`` instance.

    Most of the implementation is delegated to a dynamically defined manager
    class built by ``create_forward_many_to_many_manager()`` defined below.
    """
    def __init__(self, rel) -> None:
        ...
    
    @cached_property
    def related_manager_cls(self): # -> type[RelatedManager]:
        ...
    
    def __get__(self, instance, cls=...): # -> Self:
        """
        Get the related objects through the reverse relation.

        With the example above, when getting ``parent.children``:

        - ``self`` is the descriptor managing the ``children`` attribute
        - ``instance`` is the ``parent`` instance
        - ``cls`` is the ``Parent`` class (unused)
        """
        ...
    
    def __set__(self, instance, value):
        ...
    


def create_reverse_many_to_one_manager(superclass, rel): # -> type[RelatedManager]:
    """
    Create a manager for the reverse side of a many-to-one relation.

    This manager subclasses another manager, generally the default manager of
    the related model, and adds behaviors specific to many-to-one relations.
    """
    class RelatedManager(superclass, AltersData):
        ...
    
    

class ManyToManyDescriptor(ReverseManyToOneDescriptor):
    """
    Accessor to the related objects manager on the forward and reverse sides of
    a many-to-many relation.

    In the example::

        class Pizza(Model):
            toppings = ManyToManyField(Topping, related_name='pizzas')

    ``Pizza.toppings`` and ``Topping.pizzas`` are ``ManyToManyDescriptor``
    instances.

    Most of the implementation is delegated to a dynamically defined manager
    class built by ``create_forward_many_to_many_manager()`` defined below.
    """
    def __init__(self, rel, reverse=...) -> None:
        ...
    
    @property
    def through(self):
        ...
    
    @cached_property
    def related_manager_cls(self): # -> type[ManyRelatedManager]:
        ...
    


def create_forward_many_to_many_manager(superclass, rel, reverse): # -> type[ManyRelatedManager]:
    """
    Create a manager for the either side of a many-to-many relation.

    This manager subclasses another manager, generally the default manager of
    the related model, and adds behaviors specific to many-to-many relations.
    """
    class ManyRelatedManager(superclass, AltersData):
        ...
    
    

