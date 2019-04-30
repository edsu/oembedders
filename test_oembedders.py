from oembedders import embed, yaml_files, providers

def test_no_scheme():
    e = embed('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    assert e['title'] == 'Rick Astley - Never Gonna Give You Up (Video)'

def test_scheme():
    e = embed('https://twitter.com/jack/status/20')
    assert e['url'] == 'https://twitter.com/jack/status/20'
    
def test_yaml_dir():
    assert len(yaml_files()) > 0

def test_providers():
    assert len(list(providers())) > 0


