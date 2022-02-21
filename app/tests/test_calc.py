import unittest

import os
import sys
import inspect

#currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#parentdir = os.path.dirname(currentdir)
#sys.path.insert(0, parentdir) 

import app


class TestCVD(unittest.TestCase): # add testing capabilities
    # method to write 
    def setup(self):
        #appe = app.run()
        self.client = app.test_client()


    def test_home(self):
        #response = self.client.post("/", data={"content": "hello world"})
        response = self.client.get("/ping")
        assert response.status_code == 200
        assert "pong!" == response.get_data(as_text=True)




        #assert "POST method called" == response.get_data(as_text=True)

if __name__ == "__main__":
    unittest.main()


