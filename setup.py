import os
from setuptools import setup

__version__ = 0.1.0

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md")) as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name="photochemistry",
    packages=["photochemistry"],
    entry_points={
        "console_scripts": ["photochemistry=photochemistry.main:main"]
    },
    version=__version__,
    description="Photochemistry data analysis tools",
    long_description=long_description,
    url="https://github.com/jschnab/photochemistry",
    author="Jonathan Schnabel",
    author_email="jonathan.schnabel31@gmail.com",
    license="GNU General Public Licence v3.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.6",
    ],
    python_requires=">=3.6.8",
    keywords="data analysis photochemistry plotting statistics",
    install_requires=requirements,
)