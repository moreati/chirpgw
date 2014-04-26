"""A simple webapp2 server."""

import cgi
import json
import urllib2

import webapp2


class MainPage(webapp2.RequestHandler):

    def post(self):
        data = json.loads(cgi.escape(self.request.body))
        data = json.dumps(data)
        req = urllib2.Request('https://api.chirp.io/0/chirp', data,
                              {'Content-Type': 'application/json'})
        try:
            f = urllib2.urlopen(req)
        except urllib2.HTTPError as e:
            response = e.read()
        else:
            response = f.read()
            self.response.headers['Content-Type'] = 'application/json'
        self.response.headers['Content-Length'] = len(response)
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.write(response)


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
