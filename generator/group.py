from model.group import Group
import random
import string
import os.path
import jsonpickle


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).strip()


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name_", 10), header=random_string("header_", 20), footer=random_string("footer_", 20))
    for i in range(5)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")

with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(testdata))