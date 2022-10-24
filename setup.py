from setuptools import setup, find_packages

setup(
    name='cover_letter_clf',
    version='1.0.0',
    install_requires=[
        'transformers == 4.23.1',
        'transformers-interpret == 0.9.6',
        'torch == 1.12.1',
    ],
    packages=find_packages(
        include=['cover_letter_clf'],
    ),
)
