class ViewModel:
    def __init__(self, items):
        self._items = items
    @property
    def items(self):
        return self._items
    
    @property
    def todo_items(self):
        todo_items=[]
        for item in self._items:
            if item.status == 'todo':
                todo_items.append(item)
        return todo_items
        # using self._items, pick out and return only the items that are in the 'todo' status
        
    @property
    def doing_items(self):
        doing_items=[]
        for item in self._items:
            if item.status == 'doing':
                doing_items.append(item)
        return doing_items
        # using self._items, pick out and return only the items that are in the 'doing' status 
        

    @property
    def done_items(self):
        done_items=[]
        for item in self._items:
            if item.status == 'done':
                done_items.append(item)
        return done_items
        # using self._items, pick out and return only the items that are in the 'done' status 