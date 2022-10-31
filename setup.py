from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'The functions of a kazoon'
LONG_DESCRIPTION = 'A collection of functions that will make your life easier!'

setup(
    name="kazoon",
    version=VERSION,
    author="Osher Halil Solimany",
    author_email="solimani.osher@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
