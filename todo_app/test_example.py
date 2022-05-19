from todo_app.templates.view_model import ViewModel
from todo_app.data.item import Item

def test_view_can_only_ret_todo_items():
    items= [Item('1234', 'work', 'todo')]
    item_view_model = ViewModel(items)

    todo_items = item_view_model.todo_items

    assert len (todo_items) == 1
