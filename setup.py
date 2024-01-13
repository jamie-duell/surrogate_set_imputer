from setuptools import setup, find_packages
from surrogate_set_imputer import __version__

setup(
    name='surrogate_set_imputer',
    version=__version__,
    description='A description of your library',
    long_description='A longer description of your library',
    url='https://github.com/.../...',
    author='Jamie Duell',
    author_email='853435@swansea.ac.uk',
    packages=find_packages(),
    install_requires=['numpy', 'scikit-learn'],  # Add any dependencies your library has
)