import os
import sys
import glob

from setuptools import setup

long_description = open('README.md').read()

def yaml_files():
    return glob.glob(os.path.join('oembedders', 'providers', '*.yml'))

if __name__ == "__main__":
    setup(
        name='oembedders',
        version='0.0.1',
        url='https://github.com/oembedders',
        author='Ed Summers',
        author_email='ehs@pobox.com',
        packages=['oembedders', ],
        data_files=[('oembedders/providers', yaml_files())],
        description='A utility for dispatching to known oembed providers',
        long_description=long_description,
        long_description_content_type="text/markdown",
        python_requires='>=3',
        install_requires=['python-oembed', 'pyyaml'],
        setup_requires=['pytest-runner'],
        tests_require=['pytest'],
        entry_points={'console_scripts': ['oembedders = oembedders:main']}
    )
