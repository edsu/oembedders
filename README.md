# oembedders

This is a small wrapper around [python-oembed] and the [oembed provider
registry] to set up an oembed consumer that is configured with all known
providers.

```python
import json
from oembedders import embed

e = embed('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
```

You can use it from the command line too:

    oembedders https://www.youtube.com/watch?v=dQw4w9WgXcQ

