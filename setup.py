import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pychrone",
    version="0.0.1",
    author="Nikita Chistikov",
    author_email="chistikov@gmail.com",
    description="Small python module for building isochrones",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/headshaker/pychrone",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)