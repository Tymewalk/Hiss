url = 'http://localhost:8000'
try:                            # It will check if using python 2
    import SimpleHTTPServer
    import SocketServer
    import webbrowser
    PORT = 8000
    HANDLER = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("",PORT), HANDLER)
    print "Closed the page and want to come back? Enter localhost:8000 in your browser."
    webbrowser.open(url, new=0, autoraise=True)
    httpd.serve_forever()
except ImportError:             # If using python 3 this is run.
    import http.server
    import webbrowser
    from http.server import HTTPServer
    server_class = HTTPServer
    server_address = ("", 8000)
    httpd = server_class(server_adress, handler_class)
    print("Closed the page and want to come back? Enter localhost:8000 in your browser.")
    webbrowser.open(url,new=0,autoraise=True)
    httpd.serve_forever()
