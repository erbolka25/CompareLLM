# CompareLLM

> A multi-LLM comparison tool for comparing responses, latency, token usage and cost across different Large Language Models.

## Overview

CompareLLM is a Python-based project that allows users to send the same prompt to different Large Language Models and compare their responses using measurable metrics.

The project is being developed as an AI Engineering portfolio project.

The main goal is to understand how different LLM APIs work and build a simple, practical tool around them.

## Current Status

🚧 **Work in progress**

The initial project structure and OpenAI API integration have been implemented.

The next development stages will add:

* Anthropic Claude integration
* Latency measurement
* Token usage tracking
* Cost calculation
* SQLite history
* Streamlit interface
* Preset test prompts
* Basic response metrics

## Planned Features

### Core Features

* Send the same prompt to multiple LLM providers
* Compare model responses
* Measure API latency
* Track input and output tokens
* Estimate API cost
* Store comparison history
* View results through a Streamlit interface

### Planned Metrics

Each model response will include:

* Model name
* Response text
* Input tokens
* Output tokens
* Latency
* Estimated cost
* Response length

## Planned Architecture

```text
CompareLLM/
│
├── app.py
│
├── llm_clients/
│   ├── base.py
│   ├── openai_client.py
│   └── anthropic_client.py
│
├── core/
│   ├── compare.py
│   ├── metrics.py
│   ├── database.py
│   └── pricing.py
│
├── data/
│   └── history.db
│
├── prompts/
│
├── tests/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Tech Stack

* Python
* OpenAI API
* Anthropic API
* Streamlit
* SQLite
* Pandas
* asyncio
* python-dotenv
* Git & GitHub

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/CompareLLM.git
cd CompareLLM
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

Never commit your `.env` file or expose API keys publicly.

A `.env.example` file is included as a template.

## Running the Application

The Streamlit interface will be started with:

```bash
streamlit run app.py
```

During early development, individual Python modules can also be tested directly.

## Example

A future comparison will look approximately like:

| Model  | Latency | Input Tokens | Output Tokens |   Cost |
| ------ | ------: | -----------: | ------------: | -----: |
| OpenAI |    1.4s |           25 |           120 | $0.00x |
| Claude |    1.2s |           25 |           115 | $0.00x |

The application will also display the complete response from each model.

## Development Roadmap

### Phase 1 — Foundation

* [x] Initialize Git repository
* [x] Create project structure
* [x] Configure environment variables
* [x] Create common LLM result structure
* [x] Implement initial OpenAI API client

### Phase 2 — Comparison Engine

* [ ] Add Anthropic client
* [ ] Implement parallel API requests
* [ ] Measure latency
* [ ] Track token usage
* [ ] Calculate API cost

### Phase 3 — Storage

* [ ] Add SQLite database
* [ ] Save comparison results
* [ ] Implement history

### Phase 4 — User Interface

* [ ] Build Streamlit interface
* [ ] Add comparison table
* [ ] Display model responses
* [ ] Add history page

### Phase 5 — Evaluation

* [ ] Add preset prompts
* [ ] Add response length metrics
* [ ] Add simple instruction-following checks

### Phase 6 — Deployment

* [ ] Prepare production configuration
* [ ] Deploy to Streamlit Cloud
* [ ] Add screenshots
* [ ] Finalize documentation

## Future Improvements

Possible future additions:

* Google Gemini support
* Additional LLM providers
* Response caching
* Charts and visualizations
* Custom prompt sets
* CSV export
* More advanced evaluation metrics

## Purpose

This project is built as a practical learning and portfolio project focused on:

* LLM API integration
* Python software architecture
* asynchronous programming
* API usage tracking
* data persistence
* AI application development
* deployment

## License

This project is currently intended as a personal portfolio and learning project.
