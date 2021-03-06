# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_library(
  name='bin',
  sources=globs('*.py'),
  dependencies=[
    '3rdparty/python:pex',
    '3rdparty/python:setuptools',
    'src/python/pants/backend/core/tasks:task',
    'src/python/pants/backend/jvm/tasks:nailgun_task',
    'src/python/pants/backend/python:python_setup',
    'src/python/pants/base:build_environment',
    'src/python/pants/base:build_file',
    'src/python/pants/base:build_file_address_mapper',
    'src/python/pants/base:build_file_parser',
    'src/python/pants/base:build_graph',
    'src/python/pants/base:cmd_line_spec_parser',
    'src/python/pants/base:extension_loader',
    'src/python/pants/base:scm_build_file',
    'src/python/pants/base:workunit',
    'src/python/pants/engine',
    'src/python/pants/goal',
    'src/python/pants/goal:context',
    'src/python/pants/goal:run_tracker',
    'src/python/pants/logging',
    'src/python/pants/option',
    'src/python/pants/reporting',
    'src/python/pants/subsystem',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:filtering',
    'src/python/pants/util:memo',
  ],
)

# This binary's entry_point is used by the pantsbuild.pants sdist to setup a binary for
# pip installers, ie: it is why this works to get `pants` on your PATH:
# $ pip install pantsbuild.pants
# $ pants
python_binary(
  name='pants',
  entry_point='pants.bin.pants_exe:main',
  dependencies=[
    ':bin',
  ],
)

# This binary is for internal use only.  It adds deps on both internal_backends not meant for
# publishing in the `pantsbuild.pants` sdist as well as deps on backend plugins published as
# separate sdists from the core `pantsbuild.pants` sdist that this repo uses.
python_binary(
  name='pants_local_binary',
  entry_point='pants.bin.pants_exe:main',
  dependencies=[
    ':bin',
    'pants-plugins/src/python/internal_backend:plugins',
    'src/python/pants/backend/android:plugin',
  ],
)
