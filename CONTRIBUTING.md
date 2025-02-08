# Contributing to FastAPI REST API

Thank you for your interest in contributing to this project! We welcome contributions of all kinds. Please follow these guidelines to help us improve the project efficiently.

## 📌 Getting Started
1. Fork the repository.
2. Clone your forked repository:
   ```sh
   git clone https://github.com/your-username/gerador_api_rest.git
   ```
3. Create a virtual environment:
   ```sh
   make venv
   ```
4. Activate the virtual environment and install dependencies:
   ```sh
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   make install
   ```

## 🚀 Development Workflow
- Use `make run` to start the FastAPI server.
- Use `make test` to run tests before submitting changes.
- Format the code using `make format`.
- Ensure code quality with `make lint`.

## 🛠️ Making Changes
1. Create a new branch for your feature or fix:
   ```sh
   git checkout -b feature/my-new-feature
   ```
2. Implement your changes.
3. Ensure tests pass and code is formatted.
4. Commit your changes following conventional commits:
   ```sh
   git commit -m ":sparkles: feat: Added new authentication method"
   ```
5. Push to your branch and create a pull request.

## 📜 Code of Conduct
Be respectful, inclusive, and follow best practices. Read our [Code of Conduct](CODE_OF_CONDUCT.md) for more details.

## 🎯 Need Help?
If you have any questions, feel free to open an issue or reach out via discussions.

Thank you for contributing! 🙌

