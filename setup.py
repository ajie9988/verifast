import os
from setuptools import setup, find_packages

def get_version():
    with open(os.path.join("verifast", "__init__.py")) as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"').strip("'")
    return "0.1.0"

setup(
    name="verifast",
    version=get_version(),
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "verifast": ["data/*.json"],
    },
    install_requires=[],
    author="Verifast Team",
    description="Cross-country phone and email validation library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ajie9988/verifast",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
