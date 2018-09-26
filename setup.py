from setuptools import setup, find_packages

setup(
    name="raincloud",
    url="https://github.com/tfiers/raincloud",
    packages=find_packages(),
    install_requires=("seaborn", "parachute"),
)
