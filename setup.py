from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)-> List[str]:
    """
    Docstring for get_requirements
    
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: List[str]
    """
    requiments = []
    with open(file_path) as file_obj:
        requiments=file_obj.readlines()
        requiments = [req.replace("\n","") for req in requiments]
        if HYPEN_E_DOT in requiments:
            requiments.remove(HYPEN_E_DOT)

    return requiments

setup(
    name="mlproject", 
    version="0.0.1", 
    author='balajid',
    author_email="balajidegalas@gmail.com",
    packages=find_packages(), 
    install_requires=get_requirements("requirements.txt")
    )