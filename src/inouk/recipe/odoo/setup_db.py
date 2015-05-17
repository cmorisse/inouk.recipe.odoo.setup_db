# coding: utf-8
"""
A command to safely create db for Odoo servers built using anybox.recipe.odoo
"""
import datetime

__version__ = '0.1.0'
from odoo import main
import sys
import argparse
import subprocess
import openerp
from openerp.service.db import exp_drop, exp_create_database, exp_list, exp_rename, _create_empty_database


def get_current_git_tag():
    """
    If current directory is a git repo, we try to get a tag
    or at least current commit
    :return: git repository current tag
    :rtype: str
    """
    try:
        tag = subprocess.check_output(['git', 'describe'])
    except:
        try:
            tag = subprocess.check_output(['git', 'show', '-s', '--pretty=format:%h'])
        except:
            tag = ''
    return tag


def copy_existing_database(session, args):
    """
    Depending on the --no-copy argument either drop existing database
    or rename it.
    :param session:
    :type session: anybox.recipe.openerp.runtime.session
    :return:
    :rtype:
    """
    db_list = exp_list()

    if args.db_name in db_list:
        if args.no_copy:
            exp_drop(args.db_name)
            return 0
        else:
            now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            current_tag = get_current_git_tag()
            current_tag = '__%s' % current_tag if current_tag else ''
            archive_db_name = "%s__%s%s" % (args.db_name, now, current_tag,)
            exp_rename(args.db_name, archive_db_name)  # Be aware that rename preserve filestore

    else:
        print "Database '%s' does not exist" % args.db_name
        return 0


def create_database(session, args):
    _create_empty_database(args.db_name)
    return


def buildout_entry_point(session):
    """
    :param session:
    :type session: anybox.recipe.openerp.runtime.session
    :return: a unix exit code
    :rtype: int
    """

    parser = argparse.ArgumentParser(description="A tool to safely create Odoo database "
                                                 "ready to use with the bin/upgrade_openerp command.")
    parser.add_argument('-d', '--db-name', action='store', default=None,
                        required=False,
                        help="Name of the database to create. If unspecified, will default to"
                             "buildout db_name option.")
    parser.add_argument('-p', '--password', action='store', default='admin',
                        required=False,
                        help="Password for admin user of created database.")
    parser.add_argument('-l', '--lang', action='store', default='en_US',
                        required=False,
                        help="Initial language for new database.")
    parser.add_argument('--no-copy', action='store_true', default=False,
                        required=False,
                        help="Don't keep a copy of existing database")
    parser.add_argument('--demo', action='store_true', default=False,
                        required=False,
                        help="Create database with demo data")

    args = parser.parse_args()

    # retrieve db_name
    from openerp.tools import config
    args.db_name = args.db_name or config.options.get('db_name', None)
    if not args.db_name:
        print "ERROR: missing required database name parameter ( -d ) and no value found in buildout.cfg"
        return 1

    # We need to initialize environments like werkzeug would do it
    # See xxxx for an example
    openerp.api.Environment.reset()

    exit_code = copy_existing_database(session, args)
    if exit_code:
        return exit_code

    exit_code = create_database(session, args)

    return exit_code
