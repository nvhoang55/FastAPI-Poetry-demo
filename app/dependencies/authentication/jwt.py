from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials
from pydantic import ValidationError
from starlette import status

import jwt
from app.dependencies.authentication.auth_common import oauth2_scheme, ALGORITHMS, PUBLIC_KEY, OPTIONS, method_to_scope


# Receive a token from the request header's bearer
def has_access(request: Request, http_auth_credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme)):
    try:
        # Obtain jwt from the header
        token = http_auth_credentials.credentials
        # Decode jwt to get the payload
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=ALGORITHMS, options=OPTIONS)
        # Check if the required scope exists
        _check_scope(request, payload)

        return payload

    except(jwt.PyJWTError, ValidationError) as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Could not validate credentials by error: [{e.__str__()}]",
        )
    except Exception as other_e:
        raise HTTPException(
            status_code=status.HTTP_102_PROCESSING,
            detail=f"Processing error: [{other_e.__str__()}]",
        )


def _check_scope(request: Request, payload):
    try:
        if payload.get('scope'):
            required_scope = method_to_scope.get(str.upper(request.method))
            if required_scope in payload.get('scope'):
                return True
            else:
                raise RuntimeError(f"The required scope is missing: {required_scope}")
        else:
            raise RuntimeError("Can't find scope in the payload")

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Forbidden access with an error: [{e.__str__()}]",
        )
