import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ip_pkg",
    version="0.0.1",
    author="Horey",
    author_email="alexey.beley@gmail.com",
    description="IP mgmt module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexeyBeley/IP",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
