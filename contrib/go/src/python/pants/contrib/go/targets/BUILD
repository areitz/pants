target(
  name='targets',
  dependencies=[
    ':go_binary',
    ':go_library',
    ':go_local_source',
    ':go_remote_library',
  ]
)

python_library(
  name='go_binary',
  sources=['go_binary.py'],
  dependencies=[
    'contrib/go/src/python/pants/contrib/go/targets:go_local_source',
  ],
)

python_library(
  name='go_library',
  sources=['go_library.py'],
  dependencies=[
    'contrib/go/src/python/pants/contrib/go/targets:go_local_source',
  ],
)

python_library(
  name='go_local_source',
  sources=['go_local_source.py'],
  dependencies=[
    ':go_target',
    'src/python/pants/base:payload',
  ],
)

python_library(
  name='go_remote_library',
  sources=['go_remote_library.py'],
  dependencies=[
    ':go_target',
    'src/python/pants/base:exceptions',
    'src/python/pants/base:payload',
    'src/python/pants/base:payload_field',
  ],
)

python_library(
  name='go_target',
  sources=['go_target.py'],
  dependencies=[
    'src/python/pants/base:target'
  ]
)
