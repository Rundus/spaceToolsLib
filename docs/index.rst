.. spaceToolsLib documentation master file, created by
   sphinx-quickstart on Sun Oct  5 14:19:17 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

spaceToolsLib |version| documentation
=====================================
spaceToolsLib is a python module with many tools to interface with Heliophysics/Space physics data.
The module leverages the `spacepy <https://spacepy.github.io/index.html>`_ and `cdflib <https://cdf-lib.readthedocs.io/en/latest/>`_ libraries to perform many of its underlying functions.
This package aims to make reading/writing common file extensions in the space physics community (like .cdf) easy and quick at the cost of customizability.
Refer to `spacepy <https://spacepy.github.io/index.html>`_ or `cdflib <https://cdf-lib.readthedocs.io/en/latest/>`_ when specific file needs aren't met by spaceToolsLib.

Getting Started
===============

First steps in spaceToolsLib

.. toctree::
   :maxdepth: 1
   install
   quickstart
   help
   spaceToolsLib.tools.CDF_load


spaceToolsLib Module Reference
==============================

Description of all functions within spaceToolsLib, by module.

.. autosummary::
    :toctree: autosummary
    :recursive:

    spaceToolsLib
    ~spaceToolsLib.colorbars
    ~spaceToolsLib.math
    ~spaceToolsLib.setupFuncs
    ~spaceToolsLib.supportPackages
    ~spaceToolsLib.tools
    ~spaceToolsLib.variables


--------------------------
:Release: |version|
:Doc generation date: |today|
