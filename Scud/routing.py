from channels.routing import route
channel_routing = [
    route('http.request', 'testd.consumers.http_request_consumer')
]