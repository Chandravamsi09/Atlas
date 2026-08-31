from setuptools import setup, find_packages

setup(
    name="atlas-ai",
    version="1.0.0",
    description="Python Client SDK for Atlas Enterprise AI Platform",
    packages=find_packages(),
    install_requires=["httpx>=0.27.0", "pydantic>=2.6.0"],
    python_requires=">=3.9",
)
