from setuptools import setup


setup(
    name='bling-integration',
    version='0.1.0',
    url='https://gitlab.com/vinicius.g.roque/bling',
    author='Vinícius Gonçalves Roque',
    author_email='vinicius.g.roque@gmail.com',
    description='Integração bling',
    packages=['bling', ],
    install_requires=[
        'dicttoxml>=1.7.4',
    ],
)
