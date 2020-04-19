from model.group import Group


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="name EDITED"))
    new_group = app.group.get_group_list()
    assert len(old_groups) == len(new_group)


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="header EDITED"))
    new_group = app.group.get_group_list()
    assert len(old_groups) == len(new_group)