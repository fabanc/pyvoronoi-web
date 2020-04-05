import pyvoronoi
class MyProcessor:     
    def run(self):        
        # return [1,2,3]
        pv = pyvoronoi.Pyvoronoi(1)
        pv.AddSegment([[0, 0], [0, 2]])
        pv.AddSegment([[0, 2], [1, 2]])
        pv.AddSegment([[1, 2], [1, 0]])
        pv.AddSegment([[1, 0], [0, 0]])
        pv.Construct()
        edges = pv.GetEdges()
        vertices = pv.GetVertices()
        return vertices