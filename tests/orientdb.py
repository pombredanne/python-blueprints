import os
import shutil
import unittest

from base import BaseTestGraph

from blueprints import Graph


class TestGraphOrient(BaseTestGraph):

    __test__ = True

    name = 'orientdb'
    _path = '/tmp/orientdb-python-blueprints-tests'

    def path(self):
        return 'local:%s' % self._path

    def setUp(self):
        os.makedirs(self._path)
        self.graph = Graph(self.name, self.path())

    def tearDown(self):
        self.graph.close()
        shutil.rmtree(self._path)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGraphOrient)
    unittest.TextTestRunner(verbosity=2).run(suite)
