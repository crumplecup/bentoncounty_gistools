from setuptools import setup, find_packages

with open("README.rst", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="bentoncounty",
    version="0.0.1",
    author="Erik Rose",
    author_email="erik.w.rose@gmail.com",
    description="Mapping tools for Benton County Community Development, Oregon",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/crumplecup/bentoncounty_gistools/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
