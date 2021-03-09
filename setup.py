from setuptools import setup, find_packages


setup(
    name="moneyball",
    version="1.0.0",
    description="Modules related to baseball analysis.",
    author="Josh Kim",
    author_email="joshkim47@gmail.com",
    packages=find_packages(exclude=["docs", "tests*"]),
    install_requires=[
        "pybaseball>=2.1.1",
    ],
    python_requires=">=3.6",
)
