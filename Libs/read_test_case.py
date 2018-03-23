import json
import os

class read_test_case(object):
    def __init__(self, path, file):
        self.file = file
        self.path = path

    def tc_dict(self):
        return json.load(open(os.path.join(self.path,"testcases", self.file)))
    
    def key_value(self, d1, key):
        try:
            return d1[key]
        except KeyError:
            return ""
    
if __name__ == "__main__":
    obj = read_test_case("test1.tc")
    d1 = obj.tc_dict()
    print(obj.key_value(d1, "name"))