### To develop ml app like a package and can also deploy to python pypy (The Python Package Index (PyPI) is a repository of software for the Python programming language).

## 
from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this func will give a list of req
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
   name='ML_project',
   version='0.0.1',
   author='Ashita',
   author_email='shtkapoor8@gmail.com',
   packages=find_packages(),
   install_requires=get_requirements('requirements.txt') 
)