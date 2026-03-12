# Deploy Notes

## Project
- GitHub repository: `https://github.com/zdy545801/auckland-map`
- Deploy platform: `Render`

## Daily Update Flow
1. Modify code locally.
2. Commit and push to GitHub:
   - `git add .`
   - `git commit -m "your message"`
   - `git push`
3. Render behavior:
   - If `Auto Deploy` is ON, Render redeploys automatically after push.
   - If `Auto Deploy` is OFF, trigger deploy manually in Render dashboard.

## Local Run
- From project root:
  - `python map_files/app.py`
- Or enter folder and run:
  - `cd map_files`
  - `python app.py`

## Render Service Settings
- Build Command: `pip install -r map_files/requirements.txt`
- Start Command: `gunicorn --chdir map_files app:app`

## Useful Commands
- Check git status: `git status`
- View remote: `git remote -v`
- View latest commits: `git log --oneline -5`
