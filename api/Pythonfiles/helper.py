import json
import jsonpath


def read_element(locator):
    file = "D:/Robot/Jsonfiles/Elements.json"
    with open(file, "r") as read_file:
        data = json.load(read_file)
        value = jsonpath.jsonpath(data, locator)
        locator = value[0]
        search_type = locator['searchtype']
        search_text = locator['searchtext']
        final = search_type+':'+search_text
        return final

x = read_element("search")
print(x)


