from setuptools import setup, find_packages

name = 'inouk.recipe.odoo.setup_db'
version = '0.1.1'


long_description = (
    '\nDetailed Documentation\n'
    '######################\n'
    + '\n' +
    open('readme.rst').read()
    + '\n' +
    'Contributors\n'
    '############\n'
    + '\n' +
    open('contributors.txt').read()
    + '\n' +
    'Change history\n'
    '##############\n'
    + '\n' +
    open('changes.txt').read()
    + '\n'
)

setup(
    name=name,
    version=version,
    packages=find_packages('src'),
    namespace_packages=['inouk', 'inouk.recipe', 'inouk.recipe.odoo'],
    package_dir={'': 'src'},
    url='https://github.com/cmorisse/inouk.recipe.odoo.setup_db',
    # license='AGPL v3', TO use only when licence do not exist in trove classifiers
    author='Cyril MORISSE',
    author_email='cmorisse@boxes3.net',
    description='A command to safely create openerp database for use with anybox.recipe.odoo upgrade.py command.',
    long_description=long_description,
    keywords="openerp odoo recipe command create database",
    include_package_data=True,
    install_requires=['setuptools',],
    classifiers=[
        'Framework :: Buildout :: Recipe',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python',
        'Natural Language :: English',
    ],
    entry_points="""
    [console_scripts]
    setup_db = inouk.recipe.odoo.setup_db:buildout_entry_point
    """
)
