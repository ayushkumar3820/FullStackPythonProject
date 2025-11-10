# Copilot Instructions for Microservices_with_FastAPI

## Project Overview
- **Backend**: FastAPI-based microservice architecture. Key directories:
  - `core/`: Core logic, configuration, and utility modules.
  - `db/`: Database connection and setup.
  - `models/`: Pydantic and ORM models for jobs and stories.
  - `routers/`: API route definitions, organized by resource.
  - `schemas/`: Pydantic schemas for request/response validation.
- **Frontend**: React app bootstrapped with Vite, using Tailwind CSS for styling.

## Key Patterns & Conventions
- **Settings**: Centralized in `core/config.py` using Pydantic's `BaseSettings`. Environment variables are loaded from `.env`.
- **CORS**: Allowed origins are parsed from a comma-separated string in the environment.
- **API Prefix**: All backend routes are prefixed with `/api` (see `API_PREFIX` in `core/config.py`).
- **Router Structure**: Each resource (e.g., job, story) has its own router, schema, and model module.
- **Database**: Connection logic is in `db/database.py`. Models are in `models/`.

## Developer Workflows
- **Backend**:
  - Start server: `uvicorn main:app --reload` from the `Backend/` directory.
  - Add new endpoints: Create/modify routers and schemas, register routers in `main.py`.
  - Environment: Place secrets and config in `.env` (see `core/config.py`).
- **Frontend**:
  - Start dev server: `npm run dev` from `frontend/`.
  - Build: `npm run build`.
  - Tailwind CSS is configured via `tailwind.config.js` and `postcss.config.js`.

## Integration Points
- **API Communication**: Frontend communicates with backend via REST endpoints under `/api`.
- **OpenAI Integration**: API key is set via environment variable (`GEMINI_API_KEY`).

## Project-Specific Notes
- Use Pydantic's `field_validator` for custom environment variable parsing.
- All new backend features should follow the router/schema/model separation.
- Keep frontend assets in `frontend/public/` and `frontend/src/assets/`.

---

For more details, see `core/config.py`, `main.py`, and the respective `README.md` files in each major directory.
