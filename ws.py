import json
import cherrypy
import myprocessor
p = myprocessor.MyProcessor()

class MyWebService(object):

   @cherrypy.expose
   @cherrypy.tools.json_out()
   # @cherrypy.tools.json_in()
   def process(self):
      # data = cherrypy.request.json
      voronoi_points = p.run()
      output = {'points': []}
      for point in voronoi_points:
         output['points'].append({'x':point.X, 'y': point.Y})
      return json.dumps(output)

if __name__ == '__main__':
   config = {'server.socket_host': '0.0.0.0'}
   cherrypy.config.update(config)
   cherrypy.quickstart(MyWebService())