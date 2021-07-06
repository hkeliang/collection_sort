# coding: utf-8

from setuptools import setup
setup(
    name='collection_sort',
    version='0.0.2',
    author='houkl',
    author_email='382954886@qq.com',
    url='https://github.com/hkeliang/collection_sort',
    install_requires=[],
    python_requires='>=3.4',
    entry_points={
        'collection_sort': [
            'quicksort=quicksort:quicksort'
        ]
    }
)
