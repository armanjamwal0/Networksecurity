'''
The setup.py file is an essential part of packaging and distributing Python projects. It is used by setuptools (or distutils in older Python versions) 
to define the configuration of your porject, such as its metadata,dependencies, and more.



-e .  create a folder that contain all details about package and autor email or author name 
'''
from setuptools import find_packages,setup ## what this do it find init file in every folder if it get then make package of that folder 
from typing import List

def get_requirements()->List[str]:
    '''
    This funcation return list of requirements
    '''
    requirements_lst:List[str] = []
    try:
        with open('requirements.txt','r') as f:
            # read lines from file 
            lines = f.readlines()
            ## process each lines
            for lin in lines:
                requirements = lin.strip()
                ## ignore empty lines and -e.
                if requirements and requirements!= '-e .':
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print('requirements.txt file not Exist please chesk !!!!!!!!!!!!!!!!!!')
    return requirements_lst


setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Zoro',
    author_email='zoro@gmail.com',
    packages=find_packages(), ## this find for me a packages that have init file 
    install_requires=get_requirements()   ## this download package this funcation return package name 
)