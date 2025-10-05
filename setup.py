import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "spaceToolsLib",
    version = "0.0.13",
    author = "C. Feltman",
    author_email = "cfeltman@uiowa.edu",
    description = "A small package containing useful variables, functions and methods to interface with CDF files in the field of Space Plasma Physics.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Rundus/spaceToolsLib",
    project_urls = {
        "Issues": "https://github.com/Rundus/spaceToolsLib/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "spaceToolsLib"},
    packages = setuptools.find_packages(where="spaceToolsLib"),
    python_requires = ">=3.10"
)