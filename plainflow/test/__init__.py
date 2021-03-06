import unittest
import pkgutil
import logging
import sys

def all_names():
    for _, modname, _ in pkgutil.iter_modules(__path__):
        yield 'plainflow.test.' + modname

def all():
    logging.basicConfig(stream=sys.stderr)
    return unittest.defaultTestLoader.loadTestsFromNames(all_names())
