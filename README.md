# portlandgeneral-api
An unofficial Python library for requesting data from the Portland General Electric (PGE) API.

Portland General (PGE): https://portlandgeneral.com/
API: https://api.portlandgeneral.com/
PGE GraphQL Endpoint: https://api.portlandgeneral.com/pge-graphql

## Installation

The package is availble via PyPi and can be installed with the following command:
```
pip3 install portlandgeneral-api
```

To install it from the repo, clone the repo and cd into the directory:

```
git clone https://github.com/piekstra/portlandgeneral-api.git
cd portlandgeneral-api
```

You can install this library with `pip`:

```
pip3 install .
```

## Testing

This project leverages `wiremock` to test the code to some extent. Note this will not protect the project from changes that Portland General makes to their API, but instead verifies that the existing code functions consistently as written.

### Local Testing 

Note that the tests setup leverages the [`local_env_vars.py`](tests/local_env_vars.py) file. The values for those environment variables need to be set based on the following:

* `PORTLANDGENERAL_USERNAME`: `example@email.com` - This must have parity with the `email` in the `body` specified in [`tests/wiremock/mappings/jwt_request.json`](tests/wiremock/mappings/jwt_request.json)
* `PORTLANDGENERAL_PASSWORD`: `portlandgeneral_password` - This must have parity with the `password` in the `body` specified in [`tests/wiremock/mappings/jwt_request.json`](tests/wiremock/mappings/jwt_request.json)
* `IDP_HOST_OVERRIDE`: `http://127.0.0.1:9090` - This URL is simply `http://127.0.0.1` but the url port must have parity with the [`docker-compose.yaml`](docker-compose.yaml) wiremock service's exposed http `port`. 
* `API_HOST_OVERRIDE`: `http://127.0.0.1:9090` - This URL is simply `http://127.0.0.1` but the url port must have parity with the [`docker-compose.yaml`](docker-compose.yaml) wiremock service's exposed http `port`. 

To run tests, you will first need to start the wiremock service by running:

```
docker-compose up -d
```

Then, you can run the actual tests with the following command:

```
pytest --verbose
```

### GitHub Testing

This project leverages GitHub Actions and has a [workflow](.github/workflows/python-package.yml) that will run these tests. The environment configuration for the tests must have parity with the [`local_env_vars.py`](tests/local_env_vars.py) file from the [local testing](#local-testing).


## Releases

Releases should follow a [Semantic Versioning](https://semver.org/) scheme. 

When changes have been made that warrant a new release that should be published, modify the `__version__` in [`setup.py`](setup.py) 

After the change is merged to the `main` branch, go to [releases](https://github.com/piekstra/portlandgeneral-api/releases) and `Draft a new release`. The `Tag version` should follow the pattern `v1.0.0` and should `Target` the `main` branch. 

The `Release title` should not include the `v` from the tag and should have a reasonably detailed description of the new release's changes. 

Once the release has been published, the [`.github/workflows/python-publish.yml`](.github/workflows/python-publish.yml) GitHub Actions Workflow should trigger and automatically upload the new version to [PyPi](https://pypi.org/) using GitHub secrets credentials.

## Not-so-ecret Keys

Certain values found in [config.ts](./misc/config.ts) are copied from the [Portland General's Website](https://portlandgeneral.com/) where they conveniently left their source maps. Those values are in fact ***not*** tied to a personal account with Portland General, but are instead specific to their deployments.
