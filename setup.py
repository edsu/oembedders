import sys

from setuptools import setup

long_description = open('README.md').read()

if __name__ == "__main__":
    setup(
        name='oembedders',
        version='0.0.1',
        url='https://github.com/oembedders',
        author='Ed Summers',
        author_email='ehs@pobox.com',
        packages=['oembedders', ],
        description='A utility for dispatching to known oembed providers',
        long_description=long_description,
        long_description_content_type="text/markdown",
        python_requires='>=3',
        install_requires=['python-oembed', 'pyyaml'],
        setup_requires=['pytest-runner'],
        tests_require=['pytest'],
        entry_points={'console_scripts': ['oembedders = oembedders:main']}
    )
