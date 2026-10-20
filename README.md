# Text-to-SQL Agent — Single-agent vs Multi-agent Comparison

**Text-to-SQL Agent** is a research project that will compare single-agent and multi-agent approaches to translating natural-language questions into SQL. Both approaches will use the same BIRD Mini-Dev examples so their results can be evaluated consistently.

This is an initial project setup. The repository currently includes the dataset layout, an exploratory notebook, and a small OpenRouter experiment. The agent workflows and evaluation pipeline have not been implemented yet.

## 📋 Project Overview

The planned comparison has four stages:

1. **Question and schema input:** Load a Mini-Dev question and the schema of its associated database.
2. **SQL generation:** Let a single agent or a coordinated group of agents produce a SQL query.
3. **Execution:** Run the query against the corresponding database.
4. **Comparison:** Evaluate the generated result against the dataset's reference SQL or result.

The current OpenRouter script is a preliminary API experiment. It sends one fixed prompt to two models and prints their raw responses; it does not perform these four stages.

## 📂 Project Structure

```text
text-to-sql-agent/
├── src/
│   ├── test_openrouter.py    # Direct OpenRouter API experiment
│   └── .env.example          # Example API key configuration
├── notebooks/
│   └── notebook.ipynb        # Early database and dataset exploration
├── data/                     # BIRD Mini-Dev dataset; excluded from Git
│   ├── MINIDEV/              # Questions, gold SQL, metadata, SQLite databases
│   ├── MINIDEV_mysql/        # MySQL SQL dump
│   └── MINIDEV_postgresql/   # PostgreSQL SQL dump
├── pyproject.toml            # Project dependencies and Python requirement
├── uv.lock                   # Locked dependency versions
└── README.md
```

`docs/` contains local thesis drafts and is also excluded from Git.

## 🛠️ Tech Stack

- **Python 3.10+:** Main programming language.
- **uv:** Dependency and virtual environment management.
- **LangChain and LangGraph:** Declared dependencies for the planned agent workflows.
- **OpenRouter:** Model access for the current API experiment.
- **BIRD Mini-Dev:** Text-to-SQL questions, reference queries, and databases for the planned comparison.

## 🚀 Getting Started

### 1. Install dependencies

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then run this command from the project root:

```bash
uv sync
```

### 2. Prepare the dataset

Download the [BIRD Mini-Dev ZIP](https://drive.google.com/file/d/13VLWIwpw5E3d5DUkMvzw7hvHE67a4XkG/view) linked by the [official repository](https://github.com/bird-bench/mini_dev). After extraction, copy these three folders from `minidev/minidev/` directly into the project's `data/` folder:

```text
data/
├── MINIDEV/
├── MINIDEV_mysql/
└── MINIDEV_postgresql/
```

The archive's outer `minidev/` layer and `_MACOSX/` folder are not needed in `data/`. The dataset is excluded from Git, so it must be downloaded separately after cloning this repository. The OpenRouter experiment below does not require the dataset yet.

### 3. Configure OpenRouter

Copy `src/.env.example` to `src/.env` and replace the example value with your `OPENROUTER_API_KEY`. The `.env` file is excluded from Git.

### 4. Run the current experiment

```bash
uv run python src/test_openrouter.py
```

The script calls `openai/gpt-4o-mini` and `meta-llama/llama-3.1-8b-instruct` with a fixed SQL-generation prompt. It writes each response body from OpenRouter directly to standard output and model labels or errors to standard error. API usage may consume account credits.

## ✨ Features

**Available now**

- A local BIRD Mini-Dev layout with SQLite databases and MySQL/PostgreSQL dumps.
- Direct OpenRouter requests that preserve the API response body.

**Planned**

- Single-agent and multi-agent SQL generation workflows.
- Execution and evaluation on the same BIRD Mini-Dev examples.

## 📚 References

- [BIRD Mini-Dev repository](https://github.com/bird-bench/mini_dev)
- [BIRD Mini-Dev dataset ZIP](https://drive.google.com/file/d/13VLWIwpw5E3d5DUkMvzw7hvHE67a4XkG/view)
- [OpenRouter API documentation](https://openrouter.ai/docs/api/api-reference/chat/send-chat-completion-request)

## 🤝 Contributing

Suggestions and contributions are welcome through issues or pull requests. Keep API keys and the downloaded dataset out of commits; document new environment variables in `src/.env.example`.
