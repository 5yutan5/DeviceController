import setuptools
from setuptools import setup

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="DeviceController",
    version="0.1.0",
    author="Yakitori",
    author_email="4yutan4@gmail.com",
    description="This library controls devices in my laboratory.",
    longdescription=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/5yutan5/DeviceController",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
