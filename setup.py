from setuptools import setup, find_packages

setup(
    name='mocks_handler',
    version='0.1.3',
    license="GNU GENERAL PUBLIC LICENSE",
    author="fcasalen",
    author_email="fcasalen@gmail.com",
    description="package to handle mocks folder and its content, allowing to load and write json and txt files in it",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').readlines(),
    long_description=open("README.md").read(),
    classifiers=[
        "Development Status :: 5 - Prodution/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12"
    ]
)
