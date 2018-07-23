# mapping response json with all keys to the request json, which can contain less number of keys
def map_response(request, response):
    mapped_response = {}
    for key in request.keys():
        subdict = {}
        if type(request[key]) == dict:
            for dict_key in request[key].keys():
                subdict[dict_key] = response[key][dict_key]
            mapped_response[key] = subdict
        else:
            mapped_response[key] = response[key]

    return mapped_response
