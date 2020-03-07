import codecs
import os
import sys

from setuptools import find_packages, setup


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):            
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


long_description = read('README.md')

setup(
    name='canaa-base-model-creator',
    version=get_version("src/create_models/__init__.py"),
    description="Canaa Base model creator",
    long_description=long_description,
    license='MIT',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    url='https://pip.pypa.io/',
    keywords='canaa hbsis',
    project_urls={
        "Documentation": "https://pip.pypa.io",
        "Source": "https://github.com/guionardo/canaa-base-model-creator",
    },
    author='The pip developers',
    author_email='pypa-dev@groups.google.com',

    package_dir={"": "src"},
    packages=find_packages(
        where="src",
        exclude=["contrib", "docs", "tests*", "tasks"],
    ),
    entry_points={
        "console_scripts": [
            "canaa-model=canaa-base-model-creator._internal.cli.main:main"
        ],
    },

    zip_safe=False,
    python_requires='>=3.6.*',
)
