# Quick Start Guide

## What You Have Now

✅ **100 markdown files** — One per topic (statistics/ folder)  
✅ **statistics_data.json** — Auto-generated data file  
✅ **index-statistics.html** — Interactive wireframe viewer  
✅ **10 image folders** — One per chapter (ready for images)  

## Test It Now (2 minutes)

```bash
# From grok_files directory:
cd wireframe_HTML
python3 -m http.server 8000
```

Then open: **http://localhost:8000/index-statistics.html**

You should see:
- 10 chapters in left sidebar
- Topics listed in right column
- Content displays in center
- Search works across all topics

## Add Images (Optional)

Drop image files into any chapter's `images/` folder:

```
statistics/01-introduction-to-statistics/images/
├── descriptive-stats.png
├── population-sample.png
└── ... more images
```

Then run:
```bash
python3 generate_statistics_data.py
```

Refresh the browser → images appear automatically.

## Deploy in 3 Steps

### Step 1: Prepare Deploy Folder

```bash
mkdir -p deploy/statistics

# Copy files to deploy folder
cp wireframe_HTML/index-statistics.html deploy/index.html
cp wireframe_HTML/statistics_data.json deploy/
cp -r statistics/*/images deploy/statistics/
```

### Step 2: Choose Platform

**Netlify (Easiest)**
```bash
npm install -g netlify-cli
netlify deploy --prod --dir=./deploy
```

**Vercel**
```bash
npm install -g vercel
cd deploy && vercel --prod
```

**GitHub Pages**
- Push `deploy/` folder to GitHub
- Enable Pages in Settings
- Done!

### Step 3: Your Site is Live

Visit your deployed URL and share!

## Workflow Summary

```
Edit .md file
    ↓
Save changes
    ↓
Run: python3 generate_statistics_data.py
    ↓
Refresh browser (images auto-load)
    ↓
Test works? → Deploy!
```

## File Checklist for Deployment

```
deploy/
├── index.html                    ✅ (renamed from index-statistics.html)
├── statistics_data.json          ✅ (generated from markdown)
└── statistics/
    ├── 01-introduction-to-statistics/images/
    ├── 02-measures-of-central-tendency/images/
    ├── ... all 10 chapters with images/
```

If all 3 are present → ready to deploy!

## Questions?

- **Images not showing?** — Check file exists in `statistics/{chapter}/images/`
- **Content not updating?** — Run `python3 generate_statistics_data.py` again
- **JSON not loading?** — Make sure `statistics_data.json` is in same folder as HTML
- **Want to edit content?** — Edit the .md files directly, regenerate JSON

## Next: Add Content

1. Open any `.md` file in `statistics/01-*`, `statistics/02-*`, etc.
2. Edit the placeholder content
3. Save
4. Run: `python3 generate_statistics_data.py`
5. Refresh browser

That's it!
