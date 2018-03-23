import os

class setup(object):
    def __init__(self, mount_point, testdata):
        self.mount_point = mount_point
        self.testdata = testdata
        
    def validate(self):
        if os.path.exists(self.mount_point) and os.path.exists(self.testdata):
            return True
        else:
            return False