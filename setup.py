from setuptools import setup, find_packages

setup(
    name="qhld-backend",
    version="1.0.0",
    description="QHLD Backend",
    url="https://github.com/politicalwatch/qhld-backend",
    author="pr3ssh",
    packages=find_packages(),
    install_requires=[
        "flask",
        "flask-restx",
    ],
)
