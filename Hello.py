import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/plain"
        self.response.write("Hi PublieseWeb, this is my openshift deployment!")

routes = [('/', MainPage)]

my_app = webapp2.WSGIApplication(routes, debug=True)
