from app.lib import which_profession


def test_which():
    expected = "ISTJ: "
    actual = which_profession('I', 'S', 'T', 'J')
    assert expected == actual
