from setuptools import setup, find_packages

setup(
    name="sampleproject",
    version="2.0.0",
    description="A sample Python project",
    author="A. Random Developer",
    author_email="author@example.com",
    keywords="sample, setuptools, development",
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    install_requires=["peppercorn"],
    package_data={
        "sample": ["package_data.dat"],
    },
    entry_points={
        "console_scripts": [
            "sample=sample:main",
        ],
    }
)

