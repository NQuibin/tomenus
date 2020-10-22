# T.O. Menus

T.O. Menus is an app that records the menus of GTA
restaurants.

This repo serves as the Backend API.

## Local Development
**Prerequisites**
* Install `python3.8`.
* Install `node v14.8.0`.
* Install `yarn v1.19.1`

1. Install `serverless`:
    ```
    yarn global add serverless
    ```
2. Install `node_modules`:
    ```
    yarn install
    ```
3. Create python virtual env:
    ```
    python3 -m venv venv
    ```
4. Activate `venv`:
    ```
    source venv/bin/activate
    ```
5. Run `PostgreSQL` through docker:
    ```
   docker-compose up
    ```
6. Start `serverless`:
    ```
   sls offline
    ```