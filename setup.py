from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys


setup(name='ommperator',
      version='0.1',
      description='',
      author='Alex Yang',
      author_email='ayang41@gmail.com',
      license='MIT',
      packages=['ommperator'],
      zip_safe=False,
      #test_suite='tests',
      #cmdclass={'test': PyTest},
      #extras_require={'utils': ['pytest']},
)
