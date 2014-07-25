********
pkginit
********
A package to automatically include all the modules inside another package.
Why? To remove duplication. The alternative to using pkgini would be to include all the files manually for each package.

Installation
############
.. code-block:: shell

    pip install pkginit

Usage
#####

The contents of your __init__.py files should be:

.. code-block:: python

    from pkginit import load_modules
    load_modules(__file__)
