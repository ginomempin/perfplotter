from setuptools import find_packages
from setuptools import setup

setup(
    name="perfplotter",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    python_requires='~=3.7',
    install_requires=[
        "bokeh",
        "Click",
        "pandas"
    ],
    entry_points="""
        [console_scripts]
        perfplotter=perfplotter.main:cli
    """
)
