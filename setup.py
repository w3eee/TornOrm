# coding: utf8

try:
    from setuptools import setup
    has_setuptools = True
except ImportError:
    from distutils.core import setup
    has_setuptools = False


setup(
    name='TornOrm',
    version='1.41',
    license='BSD',
    author='Gee',
    author_email='hatcatxyz@gmail.com',
    description='A simple ORM base on Torndb',
    packages=[
        'tornorm',
    ],
    py_modules=['tornorm', ],
    install_requires=['torndb', 'DBUtils'],
)