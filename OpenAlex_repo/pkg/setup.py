from setuptools import setup

setup(
    name="s23openalex",
    version="0.0.1",
    description="s23openalex",
    maintainer="YXL",
    maintainer_email="yuxuanl4@andrew.cmu.edu",
    license="MIT",
    packages=["s23openalex"],
    entry_points={"console_scripts": ["oa = s23openalex.command_util:main"]},
    long_description="s23openalex about bibtex and RIS attributes.",
)
