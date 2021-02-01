from setuptools import setup, find_packages

setup(
    name="synapse_tools",
    version="1.0.0",
    author="sepo",
    author_email="sergei.polianskii@ptj.se",
    url="https://sepo.dev",
    description="testing wheels",
    packages=find_packages(),
    python_requires='>=3.6',
    zip_safe=False
)