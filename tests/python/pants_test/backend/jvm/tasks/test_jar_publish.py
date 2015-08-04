# coding=utf-8
# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

from pants.backend.jvm.tasks.jar_publish import JarPublish
from pants_test.jvm.nailgun_task_test_base import NailgunTaskTestBase


class JarPublishTest(NailgunTaskTestBase):
  """Tests for backend jvm JarPublish class"""

  def _default_jvm_opts(self):
    """Return a fresh copy of this list every time."""
    return ['jvm_opt_1', 'jvm_opt_2']

  @classmethod
  def task_type(cls):
    return JarPublish

  # def _create_context(self, properties=None, target_roots=None):
  #   return self.context(
  #     options={
  #     },
  #     target_roots=target_roots)

  def setUp(self):
    super(JarPublishTest, self).setUp()

    JarPublish.options_scope = 'jar.publish'
    self.set_options(
      jvm_options=['-Dfoo=bar'],
      repos={
        'some_ext_repo': {
          'resolver': 'artifactory.foobar.com',
          'confs': ['default', 'sources'],
          'auth': '',
          'help': 'You break it, you bought it',
        }
      }
    )
    context = self.context(target_roots=None)
    self._jar_publish = JarPublish(context, '.')

  def test_options_with_no_auth(self):
    """When called without authentication credentials, `JarPublish._ivy_jvm_options()` shouldn't
    modify any options.
    """
    self._jar_publish._jvm_options = self._default_jvm_opts()
    repo = {}
    modified_opts = self._jar_publish._ivy_jvm_options(repo)
    self.assertEqual(modified_opts, self._default_jvm_opts())

  def test_options_with_auth(self):
    """`JarPublish._ivy_jvm_options()` should produce the same list, when called multiple times
    with authentication credentials.
    """
    self._jar_publish._jvm_options = self._default_jvm_opts()

    username = 'mjk'
    password = 'h.'
    creds_options = ['-Dlogin={}'.format(username), '-Dpassword={}'.format(password)]

    repo = {
      'auth': 'blah',
      'username': username,
      'password': password,
    }
    modified_opts = self._jar_publish._ivy_jvm_options(repo)
    self.assertEqual(modified_opts, self._default_jvm_opts() + creds_options)

    # Now run it again, and make sure we don't get dupes.
    modified_opts = self._jar_publish._ivy_jvm_options(repo)
    self.assertEqual(modified_opts, self._default_jvm_opts() + creds_options)
