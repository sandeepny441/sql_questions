# Statistics Wireframe Deployment Guide

## Setup Overview

You have:
- **100 markdown files** — organized by chapter
- **Python script** — generates JSON from markdown files
- **HTML file** — loads and displays the JSON

## Step 1: Generate the JSON Data File

```bash
# From the grok_files directory, run:
python3 generate_statistics_data.py
```

This creates: `statistics_data.json` (auto-generated from all .md files)

## Step 2: Create the Images Folders

For each chapter, create an `images/` subfolder:

```bash
mkdir -p statistics/01-introduction-to-statistics/images
mkdir -p statistics/02-measures-of-central-tendency/images
mkdir -p statistics/03-measures-of-spread/images
# ... repeat for all 10 chapters
```

Or use this one-liner:

```bash
for i in {01..10}; do
  dir=$(ls -d statistics/$i-* 2>/dev/null | head -1)
  [ -n "$dir" ] && mkdir -p "$dir/images"
done
```

## Step 3: Add Images (Optional for Now)

Drop images into each chapter's `images/` folder:

```
statistics/01-introduction-to-statistics/
├── images/
│   ├── descriptive-vs-inferential.png
│   ├── population-sample.png
│   └── ... more images
├── 01-descriptive-vs-inferential.md
├── 02-population-vs-sample.md
└── ...
```

Images will auto-appear in the wireframe when you refresh.

## Step 4: Deployment Folder Structure

For deployment, you need these files together:

```
deploy/
├── index-statistics.html          ← Rename to index.html for deployment
├── statistics_data.json           ← Auto-generated (copy here or symlink)
└── statistics/
    ├── 01-introduction-to-statistics/
    │   ├── images/                ← Images go here
    │   │   ├── *.png
    │   │   └── *.jpg
    ├── 02-measures-of-central-tendency/
    │   ├── images/
    │   └── ...
    └── ... (all 10 chapters with images/)
```

## Step 5: Test Locally

```bash
# Simple way: Open in browser (if no external dependencies)
open wireframe_HTML/index-statistics.html

# Better way: Use a simple server
cd wireframe_HTML
python3 -m http.server 8000
# Then visit: http://localhost:8000/index-statistics.html
```

## Step 6: Deployment Options

### Option A: Netlify (Simplest)

```bash
# 1. Install Netlify CLI
npm install -g netlify-cli

# 2. Create deploy folder with:
#    - index-statistics.html (renamed to index.html)
#    - statistics_data.json
#    - statistics/ folder with images

# 3. Deploy
netlify deploy --prod --dir=./deploy
```

### Option B: Vercel

```bash
# 1. Install Vercel CLI
npm install -g vercel

# 2. In deploy folder, run:
vercel --prod
```

### Option C: Fly.io (for server deployment)

Create `Dockerfile`:

```dockerfile
FROM nginx:alpine
COPY deploy/ /usr/share/nginx/html/
EXPOSE 80
```

Then:

```bash
fly launch
fly deploy
```

### Option D: GitHub Pages

```bash
# 1. Push deploy folder to GitHub repo
# 2. Enable GitHub Pages in Settings
# 3. Deploy from deploy/ folder
```

## Step 7: Regenerate JSON When Content Changes

After editing markdown files:

```bash
python3 generate_statistics_data.py
```

Then redeploy the `statistics_data.json` file.

## File Dependencies

| File | Purpose | Required for Deploy |
|------|---------|-------------------|
| index-statistics.html | Main interface | ✅ Yes |
| statistics_data.json | Content data | ✅ Yes |
| statistics/ folder | Images & source | ⚠️ Yes (for images) |
| *.md files | Source content | ❌ No (only for generation) |

## Workflow

```
Edit .md files
    ↓
Run: python3 generate_statistics_data.py
    ↓
Test locally: python3 -m http.server 8000
    ↓
Deploy: Copy to deploy folder → Upload to hosting
```

## Troubleshooting

### Images not showing?
- Check image path in `statistics_data.json`
- Verify images exist in `statistics/{chapter}/images/`
- Make sure relative paths are correct

### JSON not loading?
- `statistics_data.json` must be in same directory as HTML file
- Check browser console for CORS errors
- If using file:// protocol, use a local server instead

### Content not updating?
- Regenerate JSON: `python3 generate_statistics_data.py`
- Clear browser cache
- Make sure statistics_data.json is redeployed

## Next Steps

1. ✅ Run: `python3 generate_statistics_data.py`
2. ✅ Test locally with HTTP server
3. ✅ Add images to `statistics/{chapter}/images/`
4. ✅ Choose deployment platform
5. ✅ Deploy!
