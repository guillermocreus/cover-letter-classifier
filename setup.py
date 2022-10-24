from setuptools import setup, find_packages

setup(
    name='cover_letter_clf',
    version='1.0.0',
    install_requires=[
        'transformers == 4.23.1',
        'transformers-interpret == 0.9.6',
        'numpy == 1.23.4',
        'torch == 1.12.1',
        'torchvision == 0.13.1',
        'torchaudio == 0.12.1',
    ],
    packages=find_packages(
        include=['cover_letter_clf'],
    ),
)
