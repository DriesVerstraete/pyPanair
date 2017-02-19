# pyPanair
A pre / post processor for Panair.  
"Panair" and "Panin" are not included in this repository.  
A copy of these software can be obtained at [Public Domain Aeronautical Software](http://www.pdas.com/contents15.html).  

## What can "pyPanair" do?  
Currently, post processors for agps files (agps_converter, section_force) and ffmf files (ffmf_converter) are implemented.  

List of things that will be implemented **soon<sup>TM</sup>**  
* Preprocessor for a simple wing geometry
* Preprocessor for a wing & body geometry
* Preprocessor for converting LaWGS files to stl  format

## Installation
Download the repository and type

```commandline
python setup.py install
```

or if you have git installed, simply type

```commandline
pip install git+https://github.com/SaTa999/pyPanair
```

## Requirements
pyPanair requires python 3  
(tests have only been performed for python 3.6)  
An [Anaconda3](https://www.continuum.io/) environment is recommended.

## Example
Example scripts and files are bundled in the "examples" directory.  
Run the scripts in each directory to check out how pyPanair works.   