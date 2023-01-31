from hello import hello

def test_input():
    assert hello("Pink") == "Hello, Pink"
    
def test_default():
    assert hello() == "Hello, World"