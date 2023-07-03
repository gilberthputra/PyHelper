from setuptools import setup, find_packages

setup(
    name='PyHelper',
    version='0.1',
    packages=find_packages(),
    description='A collections of Python Helper functions.',
    author='Gilbert Putra',
    author_email='harlimgilbert@gmail.com',
    url='https://github.com/gilberthputra/PyHelper',  # if you have a github repo for this package
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',  # example license
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'create-ml-dir = PyHelper.create_ml_dir:main',
        ],
    },
)
