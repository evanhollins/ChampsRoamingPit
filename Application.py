def app(environ, start_response):

    paths = {
        "/": ("text/html", "pages/index.html"),
        "/test.png": ("image/png", "images/test.png")
    }


    if environ['PATH_INFO'] in paths.keys():
        if paths[environ['PATH_INFO']][0] == "text/html":
            with open(paths[environ['PATH_INFO']][1], 'r') as f:
                page = f.read()

            headers = [('content-type', paths[environ['PATH_INFO']][0])]
            start_response('200 OK', headers)
            return [page.encode()]

        else:
            with open(paths[environ['PATH_INFO']][1], 'rb') as f:
                page = f.read()

            headers = [('content-type', paths[environ['PATH_INFO']][0])]
            start_response('200 OK', headers)
            return [page]

    else:
        page = "404: The page you are looking for cannot be found."
        headers = [('content-type', 'text/html')]
        start_response('404 NOT FOUND', headers)
        return[page.encode()]