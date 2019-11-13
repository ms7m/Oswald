![Oswald](./oswaldLogo.svg)

> Easy to create and maintain endpoints for an API. Built on top of Falcon.

![falconBadge](https://img.shields.io/badge/built%20on-Falcon-orange?style=flat-square) ![pythonBadge](https://img.shields.io/badge/Python-3.6%2F3.7-blue?style=flat-square) ![Actions Status](https://github.com/ms7m/Oswald/workflows/OswaldTests/badge.svg)

***

Automatic detection and addition of new endpoints. disable any endpoint in one line

# Sample Layout

```
📁Endpoints (Directory)
  ↳ - __init__.py
    - ShoppingCart.py
    - WebVideos.py
    - Announcements.py
    
```


# Sample Endpoint file

```python

class SampleResource:
  # Still Falcon
  def on_get(req, resp):
    resp.media = {
      "message": "hello world"
    }
    
  
  # Required Class + Variables in order for Oswald to detect it's valid.
  class Endpoint:
    API_ENDS = [
      {
        "endpoint": "/Sample",
        "endpointObj": SampleResource
      }
    ]
    
```

# Usage with Gunicorn/Others
Oswald simply returns a normal falcon WGSI object with the additions and removals.

```python
import oswald

stage_1 = oswald.Oswald("moduleFolder")

# Falcon object can be accessed
api = stage_1.api
```

# Sample Output

```python
2019-11-06 22:57:50.490 | DEBUG    | helpers.checkModuleFolder:detect_api_endpoints:21 - Ignoring Init.
2019-11-06 22:57:50.491 | INFO     | helpers.checkModuleFolder:detect_api_endpoints:34 - Importing modules.sampleResource.
2019-11-06 22:57:50.491 | INFO     | helpers.checkModuleFolder:detect_api_endpoints:36 - Imported modules.sampleResource
[-] Endpoints: 1
[-] Generating API Object.
[-] Attemping addition for /sample.
[-] 1 resource(s) added.
[-] Initalizing Webserver.
Serving on http://localhost:8874
```

# Installation

```
pip install oswald
```
