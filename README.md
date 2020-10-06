# T.O. Menus

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
5. Install `DynamoDB Local`
    ```
   sls dynamodb install
    ```
   __*Note:*__ For reference we use
   [sls-dynamodb-local](https://www.npmjs.com/package/serverless-dynamodb-local)
   plugin. Use `sls dynamodb remove` if installation fails and try again.
6. Start `serverless`.
    ```
   sls offline start
    ```