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
See https://github.com/ncbi/DbGaP-FHIR-API-Docs/blob/production/obtaining_a_token.md
write the token to `tests/fixtures/dbgap-task-specific-token.json`



```
phs000178.v11.p8.c1: The Cancer Genome Atlas (TCGA) - General Research Use (GRU)
phs000710.v2.p5.c99: 1000 Genomes Used for Cloud Testing - Unrestricted (UR)
phs001140.v1.p1.c1: ALCHEMIST Study - General Research Use (GRU)
phs001175.v2.p2.c1: TSP: Clinical Trial Sequencing Project - General Research Use (GRU)
phs001486.v4.p4.c1: NCI Cancer Model Development for the Human Cancer Model Initiative (HCMI) - General Research Use (GRU)
phs002253.v1.p1.c1: CCG Multicentric Italian Lung Detection (MILD) - General Research Use (GRU)
```

