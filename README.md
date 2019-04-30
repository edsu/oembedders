# oembedders

*oembedders* is a small wrapper around [python-oembed] and the [oembed provider
registry] to set up an oembed consumer that is configured with all known
providers.

```python
import json
from oembedders import embed

e = embed('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
```

You can use it from the command line too:

    oembedders https://www.youtube.com/watch?v=dQw4w9WgXcQ

## Providers

The provider registry data is maintained in [iamcal/oembed]. It can be updated
at any time in oembedders with the supplied Makefile which will download the
latest data and put it into place so it can be committed.

[python-oembed]: https://github.com/abarmat/python-oembed
[oembed provider registry]: https://github.com/iamcal/oembed
[iamcal/oembed]: https://github.com/iamcal/oembed

