from todo_app.templates.view_model import ViewModel
from todo_app.data.item import Item

def test_view_can_ret_todo_items():
    items= [Item('1234', 'start', 'todo')]
    item_view_model = ViewModel(items)

    todo_items = item_view_model.todo_items

    assert len (todo_items) == 1

def test_view_can_ret_doing_items():
    items= [Item('5678', 'middle', 'doing')]
    item_view_model = ViewModel(items)

    doing_items = item_view_model.doing_items

    assert len (doing_items) == 1

def test_view_can_ret_done_items():
    items= [Item('91011', 'end', 'done')]
    item_view_model = ViewModel(items)

    done_items = item_view_model.done_items

    assert len (done_items) == 1

def test_view_can_ret_all_done_items():
    items= [Item('91011', 'end', 'done')]
    items= [Item('12489', 'end1', 'done')]

    item_view_model = ViewModel(items)

    done_items = item_view_model.done_items

    assert len (done_items) == 2

    

