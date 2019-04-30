# oembedders

[![Build Status](https://secure.travis-ci.org/edsu/oembedders.png)](http://travis-ci.org/edsu/oembedders)

*oembedders* is a small wrapper around [python-oembed] and the [oembed provider
registry] to set up an oembed consumer that is configured with all known
providers.

```python
from oembedders import embed

e = embed('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
```

You can also use it from the command line:

    oembedders https://www.youtube.com/watch?v=dQw4w9WgXcQ
    {
      "author_url": "https://www.youtube.com/user/RickAstleyVEVO",
      "title": "Rick Astley - Never Gonna Give You Up (Video)",
      "thumbnail_width": 480,
      "html": "<iframe width=\"480\" height=\"270\" src=\"https://www.youtube.com/embed/dQw4w9WgXcQ?feature=oembed\" frameborder=\"0\" allow=\"accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>",
      "type": "video",
      "thumbnail_url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg",
      "version": "1.0",
      "author_name": "RickAstleyVEVO",
      "provider_url": "https://www.youtube.com/",
      "width": 480,
      "provider_name": "YouTube",
      "thumbnail_height": 360,
      "height": 270
    }

## Providers

The provider registry data is maintained in [iamcal/oembed]. It can be updated
at any time in oembedders with the supplied Makefile which will download the
latest data and put it into place so it can be committed.

[python-oembed]: https://github.com/abarmat/python-oembed
[oembed provider registry]: https://github.com/iamcal/oembed
[iamcal/oembed]: https://github.com/iamcal/oembed

