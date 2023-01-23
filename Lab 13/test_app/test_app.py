from app import bubble

def test_bubble():
    got = bubble(["abcdefghijk","abcd","abcd","a","abc","ab"])
    want = ["a","ab","abc","abcd","abcd","abcdefghijk"]

    assert got == want