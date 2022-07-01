import os
import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urlencode


class TokenResponse:
    def __init__(self, data, server=None):
        self._data = data

        if server:
            r = requests.get(server.url + "api/v4/user", params=dict(
                access_token=self.access_token,
            ))
            r.raise_for_status()
            data = r.json()
            self.id = {
                "sub": data["username"]
            }

    @property
    def access_token(self):
        return self._data["access_token"]


class AuthorizationServer:
    def __init__(self, url, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

        self.url = url

    @property
    def authorization_endpoint(self):
        return self.url + "oauth/authorize"

    @property
    def token_endpoint(self):
        return self.url + "oauth/token"

    def authorize(self, redirect_uri, state, scope="read_user"):
        return self.authorization_endpoint + "?" + urlencode(dict(
            client_id=self.client_id,
            response_type="code",
            redirect_uri=redirect_uri,
            state=state,
            scope=scope,
        ))

    def request_token(self, redirect_uri, code):
        client_auth = HTTPBasicAuth(self.client_id, self.client_secret)
        r = requests.post(self.token_endpoint, auth=client_auth, data=dict(
            grant_type="authorization_code",
            redirect_uri=redirect_uri,
            code=code,
        ))
        r.raise_for_status()
        return TokenResponse(r.json(), self)


SERVER = os.getenv("GITLAB_SERVER", "https://gitlab.com/")
CLIENT_ID = os.getenv("GITLAB_CLIENT_ID")
CLIENT_SECRET = os.getenv("GITLAB_CLIENT_SECRET")

if SERVER and CLIENT_ID and CLIENT_SECRET:
    server = AuthorizationServer(SERVER, CLIENT_ID, CLIENT_SECRET)
