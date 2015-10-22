from distutils.core import setup

setup(
    name='srs-features',
    version='0.1',
    description='Feature tests for the Sail Regatta Scoring',
    packages=['features'],
    install_requires=[
        'behave',
        'selenium'
    ],
    url='https://github.com/dave-m/srs-features/',
    license='',
    author='David Mcilwee',
    author_email='blak631@gmail.com',
)
