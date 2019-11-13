class SampleResource:
    def on_get(req, resp):
        resp.media = {
            "message": "hello world"
        }

class Endpoint:
    API_ENDS = [
        {
            "endpoint": "/Sample",
            "endpointObj": SampleResource
        }
    ]