#!/usr/bin/env python

from setuptools import setup

setup(name='pystran3',
      version='0.3',
      description='Set of diagnostic tools for model structure analysis',
      url='https://github.com/stijnvanhoey/pystran',
      author='Stijn Van Hoey',
      author_email='stijnvanhoey@gmail.com',
      packages=['pystran3'],
      license='BSD 3-clause New or Revised License',
      install_requires=['matplotlib', 'numpy', 'scipy'],
      keywords='modelling, sensitivity analysis, optimization, metric calculation',)
