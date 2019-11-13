import pytest
import oswald
import oswald.tools.generatePlainAPI

import falcon

def get_all_routes(api):
    routes_list = []

    def get_children(node):
        if len(node.children):
            for child_node in node.children:
                get_children(child_node)
        else:
            routes_list.append((node.uri_template, node.resource))
    [get_children(node) for node in api._router._roots]
    return routes_list

def test_valid_directory_object_creation():
    prov_oswald = oswald.Oswald("modules")
    assert isinstance(prov_oswald, oswald.Oswald) == True

def test_addition_of_endpoint():
    prov_oswald = oswald.Oswald("modules")
    assert len(get_all_routes(prov_oswald.api)) > 0
    assert get_all_routes(prov_oswald.api)[0][0] == "/Sample"

def test_invalid_directory_object_creation():
    with pytest.raises(Exception):
        prov_oswald = oswald.Oswald("modulesS")