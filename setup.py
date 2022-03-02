# a setup file for pypi packages and librabr

# Third Party
from setuptools import setup

with open('README.md') as readme:
    long_description = readme.read()

with open('requirements.txt') as requirements_production:
    install_requires = requirements_production.readlines()

setup(
    name='pyshoket',

    description='A Python wrapper for Shoket API',

    long_description=long_description,

    long_description_content_type='text/markdown',

    version='0.0.1',    

    url='https://github.com/maen08/pyshoket',

    download_url='https://github.com/maen08/pyshoket/archive/refs/tags/v0.0.1.tar.gz',

    author='Stanley Ruheza',

    author_email='2001stany@gmail.com',

    license='MIT',

    packages=['pyshoket'],

    include_package_data=True,

    install_requires=install_requires,

    keywords=['shoket', 'online payment', 'python'],

    classifiers=[
       
        'Development Status :: 3 - Alpha',  
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
    ],

    

)
