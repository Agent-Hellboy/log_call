
import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="log_call",
    author="Prince Roshan",
    author_email="princekrroshan01@gmail.com",
    url="https://github.com/Agent-Hellboy/log_call",
    description=("Library to log function or bond-method calls"),
    long_description=read("README.rst"),
    license="MIT",
    package_dir={'': 'src'},
    packages=['log_call'],
    keywords=[
        "logger","logging-tool"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)