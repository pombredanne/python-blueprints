import shutil
from unittest import TestCase

from blueprints import Graph


class BaseTestGraph(TestCase):

    __test__ = False

    def setUp(self):
        self.graph = Graph(self.name, self.path())

    def test_graph(self):
        # test graph creation
        pass

    def test_create_vertex(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
        self.assertTrue(vertex)

    def test_create_edge(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
            other = self.graph.vertex()
            edge = self.graph.edge(vertex, 'link', other)
        self.assertTrue(edge)

    def test_vertex_outgoings(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
            other = self.graph.vertex()
            edge = self.graph.edge(vertex, 'link', other)
        copy_edge = next(vertex.outgoings())
        self.assertEqual(copy_edge, edge)

    def test_vertex_incomings(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
            other = self.graph.vertex()
            edge = self.graph.edge(vertex, 'link', other)
        copy_edge = next(other.incomings())
        self.assertEqual(copy_edge, edge)

    def test_vertex_outgoings_with_label(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
            other = self.graph.vertex()
            link = self.graph.edge(vertex, 'link', other)
            self.graph.edge(vertex, 'edge', other)
        copy_link = next(vertex.outgoings('link'))
        self.assertEqual(copy_link, link)

    def test_vertex_incomings_with_labels(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
            other = self.graph.vertex()
            link = self.graph.edge(vertex, 'link', other)
            self.graph.edge(vertex, 'edge', other)
        copy_link = next(other.incomings('link'))
        self.assertEqual(copy_link, link)

    def test_test_get_vertex(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
        id = vertex.id()
        self.assertEqual(self.graph.get_vertex(id), vertex)

    def test_test_get_edge(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
            other = self.graph.vertex()
            edge = self.graph.edge(vertex, 'link', other)
        id = edge.id()
        self.assertEqual(self.graph.get_edge(id), edge)

    def test_iter_vertices(self):
        with self.graph.transaction():
            self.graph.vertex()
            self.graph.vertex()
            self.graph.vertex()
        num = 0
        for vertex in self.graph.vertices():
            self.assertTrue(vertex)
            num += 1
        self.assertEqual(num, 3)

    def test_iter_edges(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
            other = self.graph.vertex()
            moar = self.graph.vertex()
            self.graph.edge(vertex, 'link', other)
            self.graph.edge(other, 'link', moar)
            self.graph.edge(moar, 'link', vertex)
        num = 0
        for edge in self.graph.edges():
            self.assertTrue(edge)
            num += 1
        self.assertEqual(num, 3)

    def test_edge_label(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
            other = self.graph.vertex()
            edge = self.graph.edge(vertex, 'link', other)
        self.assertEqual(edge.label(), 'link')

    def test_edge_start(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
            other = self.graph.vertex()
            edge = self.graph.edge(vertex, 'link', other)
        self.assertEqual(edge.start(), vertex)

    def test_edge_end(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
            other = self.graph.vertex()
            edge = self.graph.edge(vertex, 'link', other)
        self.assertEqual(edge.end(), other)

    def test_set_property_string(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
            vertex['foo'] = 'bar'
        self.assertEqual(vertex['foo'], 'bar')

    def test_set_property_integer(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
            vertex['foo'] = 123
        self.assertEqual(vertex['foo'], 123)

    def test_set_property_list_of_interger(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
            vertex['foo'] = [1, 2, 3]
        self.assertItemsEqual(vertex['foo'], [1, 2, 3])

    def test_set_property_list_of_string(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
            vertex['foo'] = ['1', '2', '3']
        self.assertItemsEqual(vertex['foo'], ['1', '2', '3'])

    def test_delete_vertex(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
        with self.graph.transaction():
            vertex.delete()
        self.assertEqual(len(list(self.graph.vertices())), 0)

    def test_delete_edge(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
            other = self.graph.vertex()
            edge = self.graph.edge(vertex, 'link', other)
        with self.graph.transaction():
            edge.delete()
        self.assertEqual(len(list(self.graph.edges())), 0)

    def test_keys(self):
        with self.graph.transaction():
            vertex = self.graph.vertex()
            vertex['foo'] = 'bar'
            vertex['baz'] = 'egg'
        self.assertItemsEqual(vertex.keys(), ['foo', 'baz'])

    def test_create_vertex_index(self):
        index = self.graph.index.create('foo', self.graph.VERTEX)
        self.assertTrue(index)

    def test_create_edge_index(self):
        index = self.graph.index.create('foo', self.graph.EDGE)
        self.assertTrue(index)

    def test_index_put(self):
        index = self.graph.index.create('foo', self.graph.VERTEX)
        with self.graph.transaction():
            vertex = self.graph.vertex()
        index.put('key', 'value', vertex)

    def test_index_retrieve(self):
        index = self.graph.index.create('foo', self.graph.VERTEX)
        with self.graph.transaction():
            vertex = self.graph.vertex()
        index.put('key', 'value', vertex)
        vertex_copy = next(index.get('key', 'value'))
        self.assertEqual(vertex, vertex_copy)

    def tearDown(self):
        self.graph.close()
        shutil.rmtree(self.path())
