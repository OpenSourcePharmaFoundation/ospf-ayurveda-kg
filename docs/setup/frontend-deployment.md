# Frontend Deployment Guide

Deploy the prototype frontend to Vercel directly from the OpenSourcePharmaFoundation/ospf-ayurveda-kg repository.

## Prerequisites

- A GitHub account with write access to `OpenSourcePharmaFoundation/ospf-ayurveda-kg`
- A Vercel account (free tier is sufficient)

## What gets deployed

The `frontend-demo/` directory — a static React SPA that displays pre-generated drug discovery analysis data. There is no backend server, no database connection, and no secrets. All data (CSV, JSON, Markdown) is bundled into the build and served as static files.

## Step 1: Sign in to Vercel

Go to https://vercel.com/signup and sign in with your GitHub account.

If you already have an account: https://vercel.com/login

## Step 2: Grant Vercel access to the org

1. Go to https://vercel.com/new
2. You should see a list of repositories you can import
3. If `OpenSourcePharmaFoundation` repos are not visible:
   - At the top of the repo list, there's a GitHub account/org dropdown and an **"Adjust GitHub App Permissions"** link nearby
   - Click it — it opens GitHub's app installation settings
   - Alternatively, go directly to https://github.com/settings/installations, find **Vercel**, click **Configure**
   - Under "Organization access", click **Grant** next to `OpenSourcePharmaFoundation`
   - Save and return to Vercel

This gives Vercel read access to deploy directly from the org repo. Nothing is forked or cloned to a personal account.

## Step 3: Import the repository

1. On the https://vercel.com/new page, find **ospf-ayurveda-kg** in the repository list
2. Click **Import**

## Step 4: Configure the project

On the "Configure Project" screen, set the following:

| Setting | Value | Notes |
|---------|-------|-------|
| Project Name | `ospf-ayurveda-kg` | Or any name you prefer |
| Framework Preset | Vite | Should auto-detect |
| **Root Directory** | **`frontend-demo`** | **Click "Edit" to set this. CRITICAL — without it the build fails.** |
| Build Command | Leave default | Inherited from `vercel.json`: `npm run build` |
| Output Directory | Leave default | Inherited from `vercel.json`: `dist` |
| Node.js Version | 22.x | Under "Build & Development Settings" |
| Environment Variables | None | Leave blank — no secrets needed |

### Why "Root Directory" matters

The frontend lives in the `frontend-demo/` subdirectory, not at the repo root. Setting Root Directory tells Vercel to `cd frontend-demo` before running `npm install` and `npm run build`. Without this, Vercel looks for a `package.json` at the repo root, finds nothing, and the build fails.

## Step 5: Deploy

Click **Deploy**. The first build takes 30-60 seconds.

When finished, Vercel assigns a production URL like:
```
https://ospf-ayurveda-kg.vercel.app
```

The exact subdomain depends on your project name and team.

## Step 6: Verify the deployment

Open the production URL and confirm:

- [ ] The app loads and shows the Drug Candidates tab with a list of compounds
- [ ] Clicking a drug in the list opens its detail panel on the right
- [ ] The Analysis tab renders markdown analysis documents
- [ ] Deep links work — append `?drug=CHEMBL704` to the URL and reload; it should open Mesalamine
- [ ] URL state survives page refresh (the same tab, drug, and section remain selected)

## Step 7: Confirm branch settings

Go to your project's Git settings:
```
https://vercel.com/[your-team]/ospf-ayurveda-kg/settings/git
```

Confirm:
- **Production Branch** is set to `main`
- All other branches generate **preview deployments** (this is the default)

## Step 8 (Optional): Install the Vercel GitHub App

Go to https://github.com/apps/vercel and install it for the `OpenSourcePharmaFoundation` org.

This enables Vercel to post comments on pull requests with a link to the preview deployment URL. Without it, deploys still happen — you just have to find the preview URL in the Vercel dashboard instead of on the PR.

## How it works after setup

| Action | Result |
|--------|--------|
| Push to `main` | Automatic production deploy |
| Open a pull request | Automatic preview deploy with a unique URL |
| Push new commits to a PR branch | Preview deploy updates automatically |
| Changes outside `frontend-demo/` | No deploy triggered (Vercel only watches the root directory) |

## Redeploying manually

If you need to trigger a redeploy without pushing a commit:

1. Go to https://vercel.com/[your-team]/ospf-ayurveda-kg/deployments
2. Find the most recent deployment
3. Click the three-dot menu and select **Redeploy**

## Custom domain (future)

To serve the app from a custom domain (e.g. `kg.ospf.org`):

1. Go to https://vercel.com/[your-team]/ospf-ayurveda-kg/settings/domains
2. Add the desired domain
3. Vercel displays DNS records to configure:
   - Subdomain (e.g. `kg.ospf.org`): add a **CNAME** record pointing to `cname.vercel-dns.com`
   - Apex domain (e.g. `ospf.org`): add an **A** record pointing to `76.76.21.21`
4. Configure these records with your domain registrar
5. Vercel automatically provisions and renews an SSL certificate

No code changes are needed for custom domains.

## What is NOT deployed

These components remain local and are not part of the Vercel deployment:

- **Neo4j database** — runs locally via Neo4j Desktop; the frontend uses pre-exported static data files instead
- **Python scrapers** (`src/scrapers/`) — data collection scripts that run on a developer's machine; their output is already baked into `frontend-demo/public/data/`
- **Data pipeline** (`scripts/`, `data/`) — Cypher scripts, raw CSVs, and processing tools are not served to users
- **Python virtualenv** (`venv/`) — gitignored, local development only

## Troubleshooting

### Build fails with "Could not find package.json"
You forgot to set Root Directory to `frontend-demo`. Go to project settings and fix it.

### Build fails with TypeScript errors
Run `npm run build` locally inside `frontend-demo/` to see the exact error. Fix it, push, and Vercel will auto-redeploy.

### The page loads but shows a blank white screen
Open browser DevTools (F12) and check the Console tab for errors. Most likely a data file path changed — verify that `public/data/analysis/` contains the expected CSV, JSON, and Markdown files.

### Deep links return 404
The SPA rewrite in `vercel.json` should handle this. Verify the file contains:
```json
{
  "rewrites": [
    { "source": "/(.*)", "destination": "/index.html" }
  ]
}
```
