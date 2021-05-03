from setuptools import find_packages, setup

setup(
    name='perfplotter',
    version='0.1.0',
    packages=find_packages(
        where='.',
        exclude=('tests', 'tutorials'),
        include=('perfplotter', ),
    ),
    include_package_data=True,
    python_requires='>=3.8',
    install_requires=[
        'bokeh',
        'Click',
        'pandas',
    ],
    entry_points="""
        [console_scripts]
        perfplotter=perfplotter.main:cli
    """,
)
