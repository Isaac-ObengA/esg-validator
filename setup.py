from setuptools import setup, find_packages
setup(
    name='esgvalidator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Isaac Obeng-Amoako',
    author_email='paakayjnr97@gmail.com',
    description='A Python package for validating ESG data disclosures in FinTech applications.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Isaac-ObengA/esg-validator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
