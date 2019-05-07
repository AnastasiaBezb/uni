from app.lib import which_profession


def test_which():
    expected = "ISTG: "
    actual = which_profession('I', 'S', 'T', 'J')
    assert expected == actual
