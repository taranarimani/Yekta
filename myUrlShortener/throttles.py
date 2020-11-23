from rest_framework.throttling import ScopedRateThrottle
'myUrlShortener.throttles.CreateUrlRateThrottle',
'myUrlShortener.throttles.RequestRateThrottle'


class CreateUrlRateThrottle(ScopedRateThrottle):
    scope = 'create_url_rate_throttle'


class RequestRateThrottle(ScopedRateThrottle):
    scope = 'request_rate_throttle'
