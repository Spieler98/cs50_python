from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("google") == "ggl"
    assert shorten("youtube") == "ytb"
    assert shorten("reddit") == "rddt"
