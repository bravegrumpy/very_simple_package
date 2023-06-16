Usage
=====

.. _installation:

Installation
------------

very-simple-package-braveGrumpy is published in the Test branch of Pypi.
You can install it using pip, however you must use some options.

.. code-block:: console

    (env) $ python3 -m pip install --index-url https://test.pypi.org/simple --no-deps very-simple-package-braveGrumpy


.. _importing:

Importing Arithmetic class
--------------------------
To use the Arithmetic class, you need to import the basic_arithmetic module into your code.

.. code-block:: python

    from very_simple_package_braveGrumpy.basic_arithmetic import Arithmetic



.. _class-summary:

Arithmetic Class
------------------------
You can use the class ``very_simple_package_braveGrumpy.basic_arithmetic.Arithmetic(*args)`` to multiply and add sets of numbers.


.. autoclass:: very_simple_package_braveGrumpy.basic_arithmetic::Arithmetic

    .. automethod:: sum(self)
    
    .. automethod:: add(self)
    
    .. automethod:: multiply()

>>> from very_simple_package_braveGrumpy.basic_arithmetic import Arithmetic
>>> Arithmetic(1,2,3).sum()
6