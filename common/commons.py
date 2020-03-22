import datetime
import json

from sqlalchemy.ext.declarative import DeclarativeMeta


def http_response(self, msg, code):
    self.write(json.dumps({ "data": msg, "code": code}))


if __name__ == "__main__":
    http_response()