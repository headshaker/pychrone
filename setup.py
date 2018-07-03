import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pychrone",
    version="0.0.2",
    author="Nikita Chistikov",
    author_email="chistikov@gmail.com",
    description="Small python module for building isochrones",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/headshaker/pychrone",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)