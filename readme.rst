==========================
inouk.recipe.odoo.setup_db
==========================

inouk.recipe.setup_db is an anybox.recipe.odoo console script that
complement upgrade.py script to create database. upgrade.py will
abort if launched without a existing database. setup_db fills this
gap by creating a database with correct owner after backing up any
existing database.

Installation
============

In the openerp section your buildout.cfg, add inouk.recipe.odoo.setup_db egg:

::

    [openerp] 
    recipe = anybox.recipe.openerp:server
    ...

    # ask buildout to get the package
    eggs = inouk.recipe.odoo.setup_db

    # ask the odoo recipe to create a script from inouk.recipe.setup_db
    openerp_scripts = setup_db arguments=session

Then buildout your server with *bin/buildout* to get a bin/setup_db_openerp command.

Usage
=====

Once your buildout is finished, *bin/setup_db_openerp* is ready to use.

When launched, bin/setup_db_openerp will:

- rename existing database by completing name with operation timestamp current tag of the buildout repository
- create a new Odoo database owned by openerp db_user

Parameters
==========

Invoke with -h for a description of supported parameters.


License
=======

inouk.recipe.odoo.setup_db is licensed under the GNU Affero General Public License v3. See LICENCE.txt

