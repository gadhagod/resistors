from setuptools import setup, find_packages

setup(
    name="resistors",
    version="1.0.3",
    author="Aarav Borthakur",
    author_email="gadhaguy13@gmail.com",
    description="Decode resistor color codes and encode resistance values",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gadhagod/resistors",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)