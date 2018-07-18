
def map_response(request, response):
    mapped_response = {}
    for key in request.keys():
        mapped_response[key] = response[key]

    return mapped_response
