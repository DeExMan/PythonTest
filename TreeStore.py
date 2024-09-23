class TreeStore:
    def __init__(self, items):
         self.items = items

    def getAll(self):
        return items

    def getItem(self, id):
        return str(next((i for i in items if i['id'] == id)))
    
    def getChildren(self, parentId):
        z = [] 
        for item in items:
            if item['parent'] == parentId:
                z.append(item)
        return z

    def getAllParents(self, parentId):
        parent_id = next((i for i in items if i['id'] == parentId)).get("parent")
        if parent_id != 'root':
            parent = next((i for i in items if i['id'] == parent_id))
            return [parent] + self.getAllParents(parent['id'])
        return []
    

items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

ts = TreeStore(items)

print(ts.getAll())
print(ts.getItem(7))
print(ts.getChildren(4))
print(ts.getChildren(5))
print(ts.getAllParents(7))
