# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_library(
  name = 'distribution',
  sources = [ 'distribution.py' ],
  resources = globs('*.class'),
  dependencies = [
    '3rdparty/python:six',
    'src/python/pants/backend/jvm/subsystems:jvm',
    'src/python/pants/base:revision',
    'src/python/pants/util:contextutil',
  ]
)
