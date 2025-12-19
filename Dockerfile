FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /src

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
# Install venv outside of the project root so it isn't masked by docker volume mounts
ENV UV_PROJECT_ENVIRONMENT="/venv"

# Install dependencies
# Copy the lock file and pyproject.toml first to leverage Docker cache
COPY uv.lock pyproject.toml /src/
RUN uv sync --frozen --no-install-project --no-dev

# Copy the rest of the application
COPY . /src/

# Install the project itself
RUN uv sync --frozen --no-dev

# Place executables in the environment at the front of the path
ENV PATH="/venv/bin:$PATH"

# Reset the entrypoint, don't invoke `uv`
ENTRYPOINT []

# Run the application
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]
