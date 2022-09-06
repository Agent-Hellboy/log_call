log_call
========

library to log function or bond-method calls


.. image:: https://img.shields.io/pypi/v/log_call
   :target: https://pypi.python.org/pypi/log_call/

.. image:: https://github.com/Agent-Hellboy/log_call/actions/workflows/python-package.yml/badge.svg
    :target: https://github.com/Agent-Hellboy/log_call/

.. image:: https://github.com/Agent-Hellboy/log_call/actions/workflows/python-publish.yml/badge.svg
    :target: https://github.com/Agent-Hellboy/log_call/

.. image:: https://img.shields.io/pypi/pyversions/log_call.svg
   :target: https://pypi.python.org/pypi/log_call/

.. image:: https://img.shields.io/pypi/l/log_call.svg
   :target: https://pypi.python.org/pypi/log_call/

.. image:: https://pepy.tech/badge/log_call
   :target: https://pepy.tech/project/log_call

.. image:: https://img.shields.io/pypi/format/log_call.svg
   :target: https://pypi.python.org/pypi/log_call/

.. image:: https://coveralls.io/repos/github/Agent-Hellboy/log_call/badge.svg?branch=main
   :target: https://coveralls.io/github/Agent-Hellboy/log_call?branch=main

Installation
============

::

   for stable version
      - pip install log_call

   for developement
      - git clone https://github.com/Agent-Hellboy/log_call
      - cd log_call
      - python -m venv .venv
      - source .venv/bin/activate
      

Example
-------

Import log_call from log_call and decorate your class or function with
it

.. code:: py

   from log_call import log_call

   @log_call
   class A:
       def __init__(self):
           pass 

       def a(self,*args,**kwargs):
           pass


   a=A()
   a.a(45,'str',s=34,g=43)

   @log_call
   def c(a,*args,**kwargs):
       pass

   c(34,56,p=23)

::

   response 
   2022-09-04 12:56:08,552 a called with {'args': [45, 'str'], 'kwargs': {'s': 34, 'g': 43}}
   2022-09-04 12:56:08,552 c called with {'a': 34, 'args': [56], 'kwargs': {'p': 23}}

Contributing
============

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
