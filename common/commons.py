import json

def http_response(self, msg, code):
    self.write(json.dumps({ "data": msg, "code": code}))


def serialize(model):
    from sqlalchemy.orm import class_mapper
    columns = [c.key for c in class_mapper(model.__class__).columns]
    return dict((c, getattr(model, c)) for c in columns)

if __name__ == "__main__":
    http_response()