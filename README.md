# Auckland Map

A simple web map app that displays Auckland, New Zealand using `Flask + Folium`.

## Live Deploy
- Platform: Render
- Repository: `https://github.com/zdy545801/auckland-map`

## Project Structure
```text
map_files/
  app.py
  requirements.txt
  Procfile
  render.yaml
  DEPLOY.md
```

## Local Run
From project root:

```bash
python -m pip install -r map_files/requirements.txt
python map_files/app.py
```

Open: `http://127.0.0.1:8000`

## Render Settings
- Build Command:
  - `pip install -r map_files/requirements.txt`
- Start Command:
  - `gunicorn --chdir map_files app:app`

## Update Flow
```bash
git add .
git commit -m "update map app"
git push
```

If Auto Deploy is enabled on Render, each push to `main` triggers a new deployment automatically.
