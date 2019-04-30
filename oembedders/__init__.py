import sys
import json
import yaml

from glob import glob
from os import listdir
from os.path import join, abspath, dirname
from urllib.parse import urlparse
from oembed import OEmbedConsumer, OEmbedEndpoint, OEmbedNoEndpoint

def embed(url):
    try:
        resp = consumer.embed(url)
        return resp.getData()
    except OEmbedNoEndpoint as e:
        return None

def yaml_files():
    pattern = join(dirname(abspath(__file__)), 'providers', '*.yml')
    return glob(pattern)

def providers():
    for path in yaml_files():
        yield yaml.load(open(path), Loader=yaml.SafeLoader)[0]

# create a consumer for all provider yaml files!

consumer = OEmbedConsumer()
for provider in providers():
    for e in provider['endpoints']:
        schemes = e.get('schemes', [provider['provider_url'] + '*'])
        endpoint = OEmbedEndpoint(e['url'], schemes)
        consumer.addEndpoint(endpoint)

def main():
    if len(sys.argv) != 2:
        sys.exit("usage: oembedders <url>")
    url = sys.argv[1]
    try:
        print(json.dumps(embed(url), indent=2))
    except Exception as e:
        sys.exit(e)

if __name__ == "__main__":
    main()
