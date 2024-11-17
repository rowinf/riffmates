"""
This type stub file was generated by pyright.
"""

from functools import total_ordering

@total_ordering
class Node:
    """
    A single node in the migration graph. Contains direct links to adjacent
    nodes in either direction.
    """
    def __init__(self, key) -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __getitem__(self, item):
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def add_child(self, child): # -> None:
        ...
    
    def add_parent(self, parent): # -> None:
        ...
    


class DummyNode(Node):
    """
    A node that doesn't correspond to a migration file on disk.
    (A squashed migration that was removed, for example.)

    After the migration graph is processed, all dummy nodes should be removed.
    If there are any left, a nonexistent dependency error is raised.
    """
    def __init__(self, key, origin, error_message) -> None:
        ...
    
    def raise_error(self):
        ...
    


class MigrationGraph:
    """
    Represent the digraph of all migrations in a project.

    Each migration is a node, and each dependency is an edge. There are
    no implicit dependencies between numbered migrations - the numbering is
    merely a convention to aid file listing. Every new numbered migration
    has a declared dependency to the previous number, meaning that VCS
    branch merges can be detected and resolved.

    Migrations files can be marked as replacing another set of migrations -
    this is to support the "squash" feature. The graph handler isn't responsible
    for these; instead, the code to load them in here should examine the
    migration files and if the replaced migrations are all either unapplied
    or not present, it should ignore the replaced ones, load in just the
    replacing migration, and repoint any dependencies that pointed to the
    replaced migrations to point to the replacing one.

    A node should be a tuple: (app_path, migration_name). The tree special-cases
    things within an app - namely, root nodes and leaf nodes ignore dependencies
    to other apps.
    """
    def __init__(self) -> None:
        ...
    
    def add_node(self, key, migration): # -> None:
        ...
    
    def add_dummy_node(self, key, origin, error_message): # -> None:
        ...
    
    def add_dependency(self, migration, child, parent, skip_validation=...): # -> None:
        """
        This may create dummy nodes if they don't yet exist. If
        `skip_validation=True`, validate_consistency() should be called
        afterward.
        """
        ...
    
    def remove_replaced_nodes(self, replacement, replaced): # -> None:
        """
        Remove each of the `replaced` nodes (when they exist). Any
        dependencies that were referencing them are changed to reference the
        `replacement` node instead.
        """
        ...
    
    def remove_replacement_node(self, replacement, replaced): # -> None:
        """
        The inverse operation to `remove_replaced_nodes`. Almost. Remove the
        replacement node `replacement` and remap its child nodes to `replaced`
        - the list of nodes it would have replaced. Don't remap its parent
        nodes as they are expected to be correct already.
        """
        ...
    
    def validate_consistency(self): # -> None:
        """Ensure there are no dummy nodes remaining in the graph."""
        ...
    
    def forwards_plan(self, target): # -> list[Any]:
        """
        Given a node, return a list of which previous nodes (dependencies) must
        be applied, ending with the node itself. This is the list you would
        follow if applying the migrations to a database.
        """
        ...
    
    def backwards_plan(self, target): # -> list[Any]:
        """
        Given a node, return a list of which dependent nodes (dependencies)
        must be unapplied, ending with the node itself. This is the list you
        would follow if removing the migrations from a database.
        """
        ...
    
    def iterative_dfs(self, start, forwards=...): # -> list[Any]:
        """Iterative depth-first search for finding dependencies."""
        ...
    
    def root_nodes(self, app=...): # -> list[Any]:
        """
        Return all root nodes - that is, nodes with no dependencies inside
        their app. These are the starting point for an app.
        """
        ...
    
    def leaf_nodes(self, app=...): # -> list[Any]:
        """
        Return all leaf nodes - that is, nodes with no dependents in their app.
        These are the "most current" version of an app's schema.
        Having more than one per app is technically an error, but one that
        gets handled further up, in the interactive command - it's usually the
        result of a VCS merge and needs some user input.
        """
        ...
    
    def ensure_not_cyclic(self): # -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def make_state(self, nodes=..., at_end=..., real_apps=...): # -> ProjectState:
        """
        Given a migration node or nodes, return a complete ProjectState for it.
        If at_end is False, return the state before the migration has run.
        If nodes is not provided, return the overall most current project state.
        """
        ...
    
    def __contains__(self, node): # -> bool:
        ...
    


