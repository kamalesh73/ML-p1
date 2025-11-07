from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    Return a list of requirements from a requirements file.

    Strips whitespace on each line and ignores editable-install lines like '-e .'.
    """
    requirements: List[str] = []
    with open(file_path) as file_obj:
        # splitlines() avoids keeping trailing newlines and is robust to different line endings
        raw_reqs = file_obj.read().splitlines()
        for req in raw_reqs:
            req = req.strip()
            if not req or req.startswith('#'):
                continue
            if req == HYPEN_E_DOT:
                # skip editable local install directives
                continue
            requirements.append(req)
    return requirements



setup(
    name='ml-project',
    version='0.0.1',
    author='Kamalesh',
    author_email='kamaleshsunkara7@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)