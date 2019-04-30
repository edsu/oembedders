import sys
import json
import yaml

from glob import glob
from os.path import join, abspath, dirname
from oembed import OEmbedConsumer, OEmbedEndpoint, OEmbedNoEndpoint

def embed(url):
    """
    Try to get oembed metadata for a given URL. If no provider is known you will
    get back None.
    """
    try:
        resp = consumer.embed(url)
        return resp.getData()
    except OEmbedNoEndpoint as e:
        return None

def yaml_files():
    """
    Returns a list of the known provider yaml files.
    """
    pattern = join(dirname(abspath(__file__)), 'providers', '*.yml')
    return glob(pattern)

def providers():
    """
    Returns JSON for each of the providers.
    """
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
    """
    The basic command line interface.
    """
    if len(sys.argv) != 2:
        sys.exit("usage: oembedders <url>")
    url = sys.argv[1]
    try:
        print(json.dumps(embed(url), indent=2))
    except Exception as e:
        sys.exit(e)


if __name__ == "__main__":
    main()
