import os
import setuptools


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setuptools.setup(
    license="GNU Lesser General Public License v2.1",
    name="inotipy",
    author="Oliver Berger",
    author_email="diefans@gmail.com",
    url="https://github.com/diefans/inotipy",
    description="inotify for asyncio",
    long_description=read('README'),
    version='0.1.0',
    classifiers=[
        "Framework :: AsyncIO",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
    ],
    keywords="inotify asyncio",
    packages=setuptools.find_packages(),
    zip_safe=False,
    install_requires=[],
    tests_require=[],
)
