from bot import is_location_valid


def test_is_location_valid_true():
    valid_gmap = 'https://goo.gl/maps/t7jMkdsQjKeRS8hp9'
    valid_gmap_app = 'https://maps.app.goo.gl/QtcRzGFA69weDufT9?g_st=ic'
    assert is_location_valid(valid_gmap)
    assert is_location_valid(valid_gmap)
    assert is_location_valid(valid_gmap_app)


def test_is_location_valid_false():
    not_valid_url = 'ciao mamma'
    valid_url_no_gmap = 'https://it.wikipedia.org/wiki/Ciao_mamma'
    assert is_location_valid(valid_url_no_gmap) == False
    assert is_location_valid(not_valid_url) == False
