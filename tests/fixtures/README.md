# Fixtures Directory

The `fixtures` directory is used to store static data files that are used for testing purposes. These files contain predefined data that can be used to mock responses and ensure consistent test results.

## Usage Instructions

### fetch_fixtures.py

The `fetch_fixtures.py` script is used to retrieve and store fixture data. This script can be used to fetch data from a server and save it to the `tests/fixtures` directory for use in tests.

### How to Use

1. **Run the Script**: Execute the `fetch_fixtures.py` script to fetch the required data from the project's root directory
    ```bash
    python fetch_fixtures.py
    ```
   

2. **Check the `tests/fixtures` Directory**: Verify that the data files have been downloaded and stored in the `tests/fixtures` directory

3. **Use the Data in Tests**: Use the data files in your tests to mock responses and ensure consistent test results

## dbGap Token
The dbGap token is required to run the tests.  It expires every 12 hours.
* See https://github.com/ncbi/DbGaP-FHIR-API-Docs/blob/production/obtaining_a_token.md#task-specific-token-1 section `Task Specific Token` for instructions on how to obtain the token.
* Write the token to `tests/fixtures/dbgap-task-specific-token.txt`



