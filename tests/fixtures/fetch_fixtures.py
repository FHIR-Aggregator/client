import json

import click
from pandas import DataFrame

from fhir_aggregator.client import FHIRClient, ResearchStudySummary
from tests.integration import SERVERS


def write_capability_statement_fixture(name: str, server: FHIRClient):
    """Query server for capability_statement, write to fixture file."""

    responses = [_ for _ in server.retrieve(['metadata'])]

    capability_statement = responses[0]
    fixture_path = f'tests/fixtures/{name}_capability_statement.json'
    print(f'wrote {fixture_path}')
    with open(fixture_path, 'w') as fp:
        json.dump(capability_statement, fp, indent=2)


def write_research_study_fixture(name: str, server: FHIRClient):
    """Query server for research study, write to fixture file."""
    queries = ['ResearchStudy?_maxresults=1&_count=1']
    if name == 'dbgap':
        queries = ['ResearchStudy?_id=phs000635']
    responses = [_ for _ in server.retrieve(queries, fetch_all=False)]
    if len(responses) == 0:
        print(f'WARNING no research_study found for {name}')
        print(responses)
        return
    research_study = responses[0]
    fixture_path = f'tests/fixtures/{name}_research_study.json'
    print(f'wrote {fixture_path}')
    with open(fixture_path, 'w') as fp:
        json.dump(research_study, fp, indent=2)


def write_operation_definition_fixture(name: str, server: FHIRClient):
    """Query server for operation_definition, write to fixture file."""

    responses = [_ for _ in server.retrieve(['OperationDefinition?_count=1000'])]
    if len(responses) == 0:
        print(f'WARNING no operation_definition found for {name}')

    fixture_path = f'tests/fixtures/{name}_operation_definition.json'
    with open(fixture_path, 'w') as fp:
        json.dump(responses, fp, indent=2)
    print(f'wrote {fixture_path}')


def simplify_research_studies(names):

    def summaries():
        for name in names:
            with open(f'tests/fixtures/{name}_research_study.json') as fp:
                research_study = json.load(fp)
                assert research_study
                summary = ResearchStudySummary(research_study=research_study)
                yield summary
                # _ = {k: v for k, v in summary.simplified.items()}
                # _['identifier'] = summary.simplified['identifier']
                # yield _

    # save to tsv
    simplified = [summary.simplified for summary in summaries()]
    df = DataFrame(simplified)
    df.to_csv('tests/fixtures/research_studies.tsv', index=False, sep='\t')


@click.command()
def cli():
    """Query servers and write fixture files."""
    for name, server in SERVERS.items():
        write_research_study_fixture(name, server)
        write_capability_statement_fixture(name, server)
        write_operation_definition_fixture(name, server)
    simplify_research_studies(names=SERVERS.keys())


if __name__ == '__main__':
    cli()
