from setuptools import find_packages,setup

def get_requirements(file_name):
    requirements=[]
    requirements_main=[]
    with open(file_name) as file_obj:
        requirements=file_obj.readlines()
        print('===================',requirements)
    for req in requirements:
        requirements_main.append(req.replace("\n",""))
    print('===================',requirements_main)    
    if '-e .' in requirements_main:
        requirements_main.remove('-e .')
    
    return requirements_main


setup(
    name="Data-Science-Project",
    version='0.0.1',
    author="RajPanjwani",
    author_email="rajpanjwani20@gmail.com",
    packages=find_packages(),
    requires=get_requirements('requirements.txt')
)