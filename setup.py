from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="exifcli",
    version="1.0.0",
    author="Julien Sobczak",
    description="A CLI to manipulate EXIF data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/julien-sobczak/exif-cli",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'exif-cli=exifcli:main',
        ]
    },
    install_requires=[
        'setuptools',
        'pyyaml',
        'exif'
    ],
    python_requires='>=3.6',
)
