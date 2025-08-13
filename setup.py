from setuptools import setup,find_packages

setup(
    author="Ayikwei Richard",
    description="Custom sentiment package for analysing swap related messages",
    name="sentiment",
    version="0.2.2",
    packages=find_packages(include=["sentiment", "sentiment.*"]),
    install_requires=['pandas','re'],
)