from distutils.core import setup

REQUIRES = [
    'records',
    'structlog'
]

setup(
    name='db_client',
    version='0.0.1',
    packages=['db_client'],
    url='https://github.com/allezov/db_client.git',
    license='Apache-2.0 license',
    author='lezov',
    author_email='-',
    install_requires=REQUIRES,
    description='db_client'
)
