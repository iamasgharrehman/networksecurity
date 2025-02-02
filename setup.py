'''
The setup.py file is an essential part of packaging and
distributing Python Projects. It is used by setuptools
(or distutils in older Python versions) to define the
configuration of project, such as its metadata, dependencies,
and more

'''
from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement=line.strip()

                ## ignore empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirement.txt file not found")

    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author = 'Asghar Rehman',
    author_email='asghareme94@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)