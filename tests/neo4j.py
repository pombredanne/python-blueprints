import unittest

from base import BaseTestGraph


class TestGraphNeo(BaseTestGraph):

    __test__ = True

    name = 'neo4j'

    def path(self):
        return '/tmp/neo4j-python-blueprints-tests'


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGraphNeo)
    unittest.TextTestRunner(verbosity=2).run(suite)
