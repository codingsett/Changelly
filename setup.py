from setuptools import setup, find_packages

setup(name='changelly',

      version='0.1',

      url='https://github.com/codingsett/Changelly',

      license='GNU',

      author='Joseph Kuria',

      author_email='josephkiurire@gmail.com',

      description='Changelly Exchange API client',

      packages=find_packages(exclude=['tests']),

      long_description=open('README.md').read(),

      zip_safe=False,

      setup_requires=['requests==2.31.0','requests-mock==1.5.2'],

      test_suite='requests-mock')