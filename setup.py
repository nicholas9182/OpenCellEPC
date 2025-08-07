from distutils.core import setup
from setuptools import find_packages
import pathlib
import re

root = pathlib.Path(__file__).parent
init = root / "steer-epc" / "__init__.py"
version = re.search(r'__version__\s*=\s*"([^"]+)"', init.read_text()).group(1)

setup(
    name='steer-epc',
    version=version, 
    description='Modelling Production Cost of Stationary Storage Sites',
    author='Nicholas Siemons',
    author_email='nsiemons@stanford.edu',
    url="https://github.com/nicholas9182/steer-epc/",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "datetime",
        "shapely",
        "plotly",
        "dash",
        "dash_bootstrap_components",
        "flask_caching",
        "nbformat"
    ],
    scripts=[],
    classifiers=[ 
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    entry_points={
        'console_scripts': [
            'launch_dash_app=dash_app.app:run',
        ],
    }
)
