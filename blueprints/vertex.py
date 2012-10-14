from jnius import autoclass

from element import Element


Direction = autoclass('com.tinkerpop.blueprints.Direction')


class Vertex(Element):

    def delete(self):
        self._db.removeVertex(self._element)

    def outgoings(self, *labels):
        from edge import Edge
        iterator = self._element.getEdges(Direction.OUT, *labels).iterator()
        while iterator.hasNext():
            yield Edge(iterator.next(), self._db)

    def incomings(self, *labels):
        from edge import Edge
        iterator = self._element.getEdges(Direction.IN, *labels).iterator()
        while iterator.hasNext():
            yield Edge(iterator.next(), self._db)
