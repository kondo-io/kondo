=====
Kondo
=====

A better way of ensuring a clean project workspace.

------------
Installation
------------

**NOTE:** Kondo is currently in alpha stages. There are no guarantees that it will not do crazy, horrible things to your system if used. Use at your own peril.

.. code-block:: bash

    $ git clone git@github.com:kondo-io/kondo.git ./kondo
    $ cd ./kondo
    $ poetry install

-------
Roadmap
-------

- [ ] Default setup: ``poetry config settings.virtualenvs.in-project true``
- [ ] Fill out a basic README
- [ ] Publish to PyPi.org
- [ ] Register hooks for project-type detection
- [ ] Global settings for "if no project found..."
- [ ] Python extras for installing packages to support default suggested project types
