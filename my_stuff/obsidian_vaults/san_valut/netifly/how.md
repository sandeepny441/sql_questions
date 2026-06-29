Now the architecture is much clearer.

What you actually want is:

```text
Same HTML Wireframe
        +
Different Embedded Datasets
        =
Different URLs for Different Teams
```

WITHOUT:

- exposing Excel upload
- asking users to upload files
- maintaining separate HTML codebases

This is absolutely doable.

---

# **Correct Architecture**

You should NOT keep Excel local-only if users must directly see output.

Because:

Browser cannot access Excel sitting on your computer.

So instead:

```text
Excel
   ↓
Convert to JSON
   ↓
Embed JSON into deployment
   ↓
Deploy same HTML template
```

Each deployment becomes:

```text
Team A URL → HTML + Team A data
Team B URL → HTML + Team B data
Team C URL → HTML + Team C data
```

Same wireframe.  
Different datasets.

---

# **The Real Trick**

You separate:

## **1. Presentation Layer**

(shared HTML wireframe)

from

## **2. Data Layer**

(team-specific JSON)

---

# **Recommended Folder Structure**

For Team A:

```text
team-a/
 ├── index.html
 ├── script.js
 ├── style.css
 └── data.json
```

For Team B:

```text
team-b/
 ├── index.html
 ├── script.js
 ├── style.css
 └── data.json
```

Only:

- `data.json` changes

Everything else remains identical.

---

# **Why JSON Instead of Excel**

Browsers handle JSON naturally.

Excel is:

- heavier
- slower
- harder to secure
- harder to automate

---

# **Your Workflow**

# **Step 1 — Maintain Excel Locally**

Example:

```text
mortgage_team_a.xlsx
mortgage_team_b.xlsx
```

---

# **Step 2 — Convert Each Excel to JSON**

Python:

```python
import pandas as pd

df = pd.read_excel("mortgage_team_a.xlsx")

df.to_json("data.json", orient="records")
```

---

# **Step 3 — Deploy Folder to Netlify**

Each folder:

- gets unique URL
- uses same UI
- loads different data

---

# **Inside HTML**

Your HTML simply does:

```javascript
fetch("data.json")
```

That’s it.

---

# **Result**

## **Team A sees:**

```text
netlify.com/team-a-dashboard
```

with Team A data.

---

## **Team B sees:**

```text
netlify.com/team-b-dashboard
```

with Team B data.

---

# **The Powerful Part**

You now have:

```text
ONE wireframe
MANY datasets
MANY URLs
```

This is exactly how:

- BI dashboards
- internal analytics tools
- lightweight SaaS apps
- fraud investigation portals

are often structured early on.

---

# **EVEN BETTER Architecture**

You can make:

```text
index.html?team=a
index.html?team=b
```

Then dynamically load:

```javascript
fetch("data-team-a.json")
```

based on URL parameter.

Then:

- only ONE deployed app
- multiple datasets
- cleaner maintenance

---

# **Enterprise Version Later**

Eventually you may evolve into:

```text
Shared UI
↓
Authentication
↓
Database/API
↓
Role-based access
```

But your current approach is actually very smart for:

- disconnected teams
- rapid prototyping
- fraud analytics demos
- internal investigation dashboards

---

# **Most Important Insight**

You are not deploying:

- Excel files
- user uploads

You are deploying:

- preprocessed datasets

inside:

- reusable frontend wireframe

That is the clean architecture you were aiming for.