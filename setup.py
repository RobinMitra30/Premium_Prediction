from setuptools import find_packages,setup
from typing import List

hyphen_remove = "-e ."




def get_requirments(file_path:str)->List[str]:
    '''
    This function will return the list of requirments

    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace('\n','')for req in requirements]

        if hyphen_remove in requirements:
            requirements.remove(hyphen_remove)
    
    return requirements        

setup (name='premium_calulator_project',
      version='0.0.1',
      description='Calculates the preiumfor a person as per details',
      author='Robin Mitra',
      author_email='robin.mitra1244212gmail.com',
      packages=find_packages(),
      install_requires=get_requirments('requirements.txt')
     ) 