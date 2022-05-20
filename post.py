import requests

class Post:
      def __init__(self):
          self.response=requests.get(url="https://api.npoint.io/4ea9c6978dede52c7912")
          self.title=self.response.json()["title"]
          self.body=self.response.json()["subtitle"]


