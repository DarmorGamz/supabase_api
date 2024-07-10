from setuptools import setup, find_packages

setup(
    name='supabase_api',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'supabase'
    ],
    author='Darren Morrison',
    author_email='dmorrison@darmor.ca',
    description='Supabase API wrapper',
    url='https://github.com/darmorgamz/supabase_api',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)