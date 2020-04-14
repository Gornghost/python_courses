from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="test group name", header="test group header", footer="test group footer"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))