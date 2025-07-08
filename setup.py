from setuptools import setup, find_packages
setup(
    name="esg-validator",
    version="0.1.0",
    author="Isaac Obeng-Amoako",
    author_email="paakayjnr97@gmail.com",
    description="A blockchain-style ESG data validator for FinTechs, using Python logic and regulatory alignment.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Isaac-ObengA/esg-validator",
    project_urls={
        "Source Code": "https://github.com/Isaac-ObengA/esg-validator",
        "Issue Tracker": "https://github.com/Isaac-ObengA/esg-validator/issues",},
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Sustainability",
        "Topic :: Software Development :: Libraries :: Python Modules"],
    python_requires='>=3.7',
    install_requires=[
        "jsonschema>=4.0.0",
        "pytest>=7.0.0"],
    include_package_data=True,
    zip_safe=False,)
