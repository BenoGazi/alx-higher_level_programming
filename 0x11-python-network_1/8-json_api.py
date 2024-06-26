#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    query = {'q': q}

    response = requests.post(url, data=query)
    if response.status_code != requests.codes.ok or len(response.text) <= 0:
        print('No result')
        sys.exit()
    else:
        try:
            _obj = response.json()
            if len(_obj) == 0:
                print('No result')
                sys.exit()
            my_id = _obj.get('id')                                            
            my_name =_obj.get('name')
            print("[{}] {}".format(my_id, my_name))
        except ValueError as invalid_json:
            print('Not a valid JSON')
