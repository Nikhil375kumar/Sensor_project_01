from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Remove newline characters

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='Fault detection',
    version='0.0.1',
    author='Nikhil',
    author_email='nikhil375kumar@gmail.com',  # Corrected 'author_mail' to 'author_email'
    install_requires=get_requirements('requirements.txt'),  # Corrected 'install_requirements' to 'install_requires'
    packages=find_packages()
)
