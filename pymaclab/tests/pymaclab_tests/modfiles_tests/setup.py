#!/usr/bin/env python

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('modfiles_tests', parent_package, top_path)
    config.add_subpackage('templates_tests')
    config.add_subpackage('dynare_tests')
    return config

if __name__ == '__main__':
    print('This is the wrong setup.py file to run')
