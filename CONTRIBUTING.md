# Contributing to FHIR Aggregator

We welcome contributions from developers of all skill levels. To contribute to FHIR Aggregator, please follow these guidelines.

## Getting Started

1. **Fork the repository** on GitHub.
2. **Clone your fork** locally on your machine.
3. **Create a new branch** for your contribution. Use a name that describes the feature or fix you're working on.

## Making Changes

1. Make your changes in your local repository. Keep your changes as focused as possible. If you're working on multiple unrelated fixes or features, please create separate branches and pull requests for each.
2. **Write tests** where applicable and ensure that all tests pass.
3. **Follow the coding standards** and best practices for Python and any frameworks or libraries you use.
4. **Update the documentation** if you're adding new features or changing existing functionality.

## Submitting Your Contribution

1. **Push your changes** to your fork on GitHub.
2. **Submit a pull request** to the main FHIR Aggregator repository. Provide a clear description of the problem you're solving and any relevant issue numbers.
3. **Participate in the code review process**. Be open to feedback and willing to make changes as necessary. It's a collaborative effort, and communication is key.

## Code Reviews

All submissions require review. We use GitHub's pull request and review process. Here are some things to keep in mind:

- Ensure your code adheres to the project's coding standards.
- Write clear, understandable code with comments where necessary.
- Maintain backward compatibility, or clearly state why it cannot be maintained.

## Branch Management

- Use feature branches, not the `development` branch, for development.
- Rebase your feature branch onto upstream `development` before submitting your pull request. This keeps the project history clean and simplifies the integration of your changes.
- Keep your branches as focused as possible. Each branch should represent a specific feature or fix.


## PyPI Distribution

To distribute a new version of FHIR Aggregator to PyPI, follow these steps:

1. **Ensure all tests pass** and your changes adhere to the project's coding standards.
2. **Update the version number** in `setup.py` according to semantic versioning.
3. **Build the package**. Run the following command from the root of the project:

```commandline
python setup.py sdist bdist_wheel
twine upload dist/*
```
This command generates distribution archives in the `dist` directory.
4. **Upload the package to PyPI** using [twine](https://pypi.org/project/twine/):
Note: You must have permissions to upload to the project on PyPI and may need to authenticate with your PyPI account.
5. **Tag the release** in GitHub with the new version number to maintain a record of the release and its corresponding code state.

Please ensure you have the necessary permissions and have coordinated with the project maintainers before distributing a new version.

## Code of Conduct

FHIR Aggregator is committed to providing a welcoming and inspiring community for all. We expect participants in the project to adhere to our Code of Conduct. This code applies to all project spaces, including GitHub, mailing lists, and any other forums the project uses, both online and off.

### Our Standards

Examples of behavior that contributes to creating a positive environment include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members


## Questions?

If you have any questions or need help with your setup or contribution, please open an issue. We're here to help and appreciate your interest in contributing to FHIR Aggregator!

Thank you for contributing to FHIR Aggregator!
