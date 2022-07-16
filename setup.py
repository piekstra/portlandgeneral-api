"""setup.py: setuptools control."""

from setuptools import setup, find_packages

__version__ = '1.0.1'

with open('README.md', 'r', encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name='portlandgeneral-api',
    author='Dev Piekstra',
    author_email='piekstra.dev@gmail.com',
    packages=find_packages(exclude=("tests", "misc")),
    version=__version__,
    description='Unofficial Python library for communicating with the Portland General (Electric) API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'requests>=2,<3',
    ],
    url='https://github.com/piekstra/portlandgeneral-api',
    python_requires='>=3.7',
    zip_safe=False,
    license='GPL-3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ]
)
