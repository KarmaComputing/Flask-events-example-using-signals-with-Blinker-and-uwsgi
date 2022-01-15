from app import app

if __name__ == '__main__':
    app.debug = 1
    server = Server(app.wsgi_app)
    server.serve()
else:
  application = app
