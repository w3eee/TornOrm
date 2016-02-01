# coding: utf8

try:
    from setuptools import setup
    has_setuptools = True
except ImportError:
    from distutils.core import setup
    has_setuptools = False


setup(
    name='tornorm',
    version='1.45',
    author='Wee',
    author_email='hatcatxyz@gmail.com',
    description='A simple ORM base on Torndb',
    py_modules=['tornorm', ],
    install_requires=['torndb', ],
)
