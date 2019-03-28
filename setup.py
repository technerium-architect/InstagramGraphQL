import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / 'README.md').read_text()

# This call to setup() does all the work
setup(
    name='InstagramGraphQL',
    version='1.0.8',
    description='InstagramGraphQL Unoffical API',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/technerium/InstagramGraphQL',
    author='Technerium',
    author_email='technerium@gmail.com',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['InstagramGraphQL'],
    install_requires=['SmoothAPI']
)
