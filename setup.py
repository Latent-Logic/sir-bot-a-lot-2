import pathlib

import setuptools

if sys.version_info < (3, 6):
    raise RuntimeError("SirBot requires Python 3.6+")

LONG_DESCRIPTION = pathlib.Path("README.rst").read_text("utf-8")


def find_version():
    with open("sirbot/__version__.py") as f:
        version = f.readlines()[-1].split("=")[-1].strip().strip("'").strip('"')
        if not version:
            raise RuntimeError("No version found")

    return version


setuptools.setup(
    name="sirbot",
    long_description=LONG_DESCRIPTION,
    description="Rewrite of sir-bot-a-lot",
    keywords=["sirbot", "chatbot", "bot", "slack"],
    packages=setuptools.find_packages(),
    zip_safe=True,
    python_requires="~=3.6",
    install_requires=[
        "aiohttp",
        "aiofiles",
        "asyncpg",
        "asyncio-contextmanager",
        "slack-sansio>=0.5.0",
        "gidgethub",
        "ujson",
        "apscheduler",
    ],
    setup_requires=[],
    extras_require={
        "doc": ["sphinx", "sphinxcontrib-asyncio", "sphinxcontrib-napoleon"]
    },
    # See: http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    author=("Ovv <contact@ovv.wtf>",),
    author_email="contact@ovv.wtf",
    license="MIT",
    url="https://github.com/pyslackers/sir-bot-a-lot2",
    version=find_version(),
)
