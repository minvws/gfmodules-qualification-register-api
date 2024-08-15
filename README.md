# Qualification Register API

This application is the public API for the Qualification Register which is part of the GFModules project of the
iRealisatie cluster of the Ministry of Health, Welfare and Sport.


## First run

Before you run this application, make sure that you start the
[qualification admin api](https://github.com/minvws/nl-irealisatie-zmodules-qualification-register-admin-api) first.

If you need to run the application without actual development, you can use the autopilot functionality. When this
repository is checked out, just run the following command:

```bash
make autopilot
```

This will configure the whole system for you and you should be able to use the API right away at
https://localhost:8507/docs


## Usage

The application is a FastAPI application, so you can use the FastAPI documentation to see how to use the application.

## Development

Build and run the application

Firstly, copy the `app.conf.example` to `app.conf` and adjust values when needed.
If you run Linux, make sure you export your user ID and group ID to synchronize permissions with the Docker user.

export NEW_UID=$(id -u)
export NEW_GID=$(id -g)

The application uses a private shared python library. To be able to install this library inside docker using poetry the
auth.toml file needs to exist. Run to following shell script with your credentials to setup the auth.toml. You can
generate a new access token(repo) with the full repo scope or read more about managing your personal access tokens.

```
echo """[http-basic.git-minvws-gfmodules-python-shared]
username = "your-github-username"
password = "your-github-pat"""" > ~/.auth.toml2
```

When you're ready, run the application with: `make autopilot`
