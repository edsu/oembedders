import os
import sys
import glob

from setuptools import setup

long_description = open('README.md').read()

def yaml_files():
    files = []
    for filename in os.listdir(os.path.join('oembedders', 'providers')):
        files.append(os.path.join('providers', filename))
    return files


if __name__ == "__main__":
    setup(
        name='oembedders',
        version='0.0.3',
        url='https://github.com/oembedders',
        author='Ed Summers',
        author_email='ehs@pobox.com',
        packages=['oembedders', ],
        package_dir={'oembedders': 'oembedders'},
        package_data={'oembedders': ['providers/*.yml']},
        description='A utility for dispatching to known oembed providers',
        long_description=long_description,
        long_description_content_type="text/markdown",
        python_requires='>=3',
        install_requires=['python-oembed', 'pyyaml'],
        setup_requires=['pytest-runner'],
        tests_require=['pytest'],
        entry_points={'console_scripts': ['oembedders = oembedders:main']}
    )
