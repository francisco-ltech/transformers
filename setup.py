from setuptools import setup

setup(
    name='transformers',
    version='0.5',
    description='POI Transformers Modules',
    url='http://github.com/{user}/{package}',
    author='FRA',
    author_email='author@domain.com',
    license='MIT',
    packages=['transformers'],
    install_requires=[
        'pyspark',
    ],
    zip_safe=False
)