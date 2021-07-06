# coding: utf-8

from setuptools import setup

setup(
    name='collection_sort',
    version='0.0.1',
    author='hkl',
    author_email='shdjfhsa@qq.com',
    url='https://github.com/hkeliang/collection_sort',
    install_requires=[],
    entry_points={
        'collection_sort': [
            'quick_sort=quick_sort:quick_sort'
        ]
    }
)