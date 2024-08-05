# Streamlit Application with OAuth 2.0

This is a simple application built with [Streamlit](https://streamlit.io/) in order to demonstrate OAuth 2.0 protocol implementation.

## Getting Started

To run this application:

1. Run the Docker Compose: `docker compose up --build`
2. Access Streamlit App at: `localhost:8501`

Application is ready to use and fully set up. There is no need to change any settings.

## Components

The application consists of four components represented by Docker containers:

- **streamlit_app** -> a streamlit web app.
- **keycloak** -> contains a Keycloak authentication server.
- **postgres** -> a database for storing users and their credentials. Keycloak configs are also stored here.
- **reverse_proxy** -> maintains a communication between user's client and Keycloak container. 

## Demo user credentials

After successful start of Streamlit application, you can log in using these credentials:

  - Username: `testuser`
  - Password: `test`

## Keycloak admin interface

If you need to enter the Keycloak server admin interface, follow these steps:

1. Open your browser and type URL `localhost:8888`
2. When login screen pops up, use these credentials:
  - Username: `admin`
  - Password: `admin`

## streamlit_oauth

This application implements [streamlit_oauth](https://github.com/dnplus/streamlit-oauth).

## Information resources

For more information on how to set up OAuth 2.0 in web apps, check out the following resources:

- [Introduction to OAuth 2.0](https://medium.com/nerd-for-tech/introduction-to-oauth-2-0-7aa885a3db36)
- [Create and configure Keycloak OAuth 2.0 authorization server](https://wkrzywiec.medium.com/create-and-configure-keycloak-oauth-2-0-authorization-server-f75e2f6f6046)

## License

This project is licensed under the terms of the MIT license.
