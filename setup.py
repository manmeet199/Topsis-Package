import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

VERSION = '0.0.4'
DESCRIPTION = 'Topsis Package'
LONG_DESCRIPTION = 'A package as part of Predictive Analysis course at Thapar Institute of Engineering'

# Setting up
setup(
    name="Topsis-Manmeet-101903767",
    version=VERSION,
    author="Manmeet Singh Chhabra",
    author_email="<manmeett29@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=README,
    packages=find_packages(),
    setup_requires=['wheel'],
    install_requires=['numpy', 'pandas'],
    keywords=['python', 'topsis', 'thapar', 'Prdictive-Analysis', '101903767'],
    classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',   
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  entry_points={
    "console_scripts":[
      "topsis=topsis.topsis:main",
    ]
  },
)