from decouple import config, Csv
from fastapi.security import HTTPBearer

SECURITY_ALGORITHM = config('SECURITY_ALGORITHM')
PRIVATE_KEY = config('PRIVATE_KEY')
# PUBLIC_KEY = config('PUBLIC_KEY')
PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA6S7asUuzq5Q/3U9rbs+P
kDVIdjgmtgWreG5qWPsC9xXZKiMV1AiV9LXyqQsAYpCqEDM3XbfmZqGb48yLhb/X
qZaKgSYaC/h2DjM7lgrIQAp9902Rr8fUmLN2ivr5tnLxUUOnMOc2SQtr9dgzTONY
W5Zu3PwyvAWk5D6ueIUhLtYzpcB+etoNdL3Ir2746KIy/VUsDwAM7dhrqSK8U2xF
CGlau4ikOTtvzDownAMHMrfE7q1B6WZQDAQlBmxRQsyKln5DIsKv6xauNsHRgBAK
ctUxZG8M4QJIx3S6Aughd3RZC4Ca5Ae9fd8L8mlNYBCrQhOZ7dS0f4at4arlLcaj
twIDAQAB
-----END PUBLIC KEY-----"""
OPTIONS = {
    "verify_signature": True,
    "verify_aud": False,
    "verify_iss": False,
    "verify_exp": True,
    "verify_iat": False,
    "verify_nbf": False
}
ALGORITHMS = config('SECURITY_ALGORITHM', cast=Csv())
oauth2_scheme = HTTPBearer(scheme_name="Authorization")

scope_prefix = config("SCOPE_PREFIX")
scope_write = config("SCOPE_WRITE")
method_to_scope = {
    "POST": scope_prefix + scope_write
}
