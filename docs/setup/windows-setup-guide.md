# Windows Setup Guide for OSPF Ayurveda Knowledge Graph

This comprehensive guide walks you through setting up a complete development environment on Windows for the OSPF Ayurveda Knowledge Graph project. By the end, you'll have WSL2, Python, Git, Neo4j, and Claude Code all working together.

**Estimated Total Time**: 1-2 hours (depending on download speeds)

---

## Table of Contents

1. [Part 1: Setting Up WSL2 (Windows Subsystem for Linux)](#part-1-setting-up-wsl2-windows-subsystem-for-linux)
2. [Part 2: Accessing and Using WSL2](#part-2-accessing-and-using-wsl2)
3. [Part 3: Installing Git](#part-3-installing-git)
4. [Part 4: Installing Python](#part-4-installing-python)
5. [Part 5: Cloning the Repository](#part-5-cloning-the-repository)
6. [Part 6: Setting Up Virtual Environment](#part-6-setting-up-virtual-environment)
7. [Part 7: Installing Python Libraries](#part-7-installing-python-libraries)
8. [Part 8: Installing Neo4j](#part-8-installing-neo4j)
9. [Part 9: Importing Data into Neo4j](#part-9-importing-data-into-neo4j)
10. [Part 10: Installing Claude Code](#part-10-installing-claude-code)
11. [Part 11: Initializing Claude Code in the Project](#part-11-initializing-claude-code-in-the-project)
12. [Troubleshooting](#troubleshooting)
13. [Quick Reference](#quick-reference)

---

## Part 1: Setting Up WSL2 (Windows Subsystem for Linux)

WSL2 allows you to run a full Linux environment directly on Windows. This gives you access to bash, Linux tools, and a development environment that matches most servers and CI/CD systems.

### Prerequisites

- **Windows 10** version is v2004 or higher (Build 19041+), or **Windows 11**
- Administrator access to your computer
- At least 10GB of free disk space

### Step 1.1: Check Your Windows Version

1. Press `Win + R` to open the Run dialog
2. Type `winver` and press Enter
3. Verify your version is at least **v2004** (Build 19041) or you're on Windows 11

> **Note**: If your Windows version is older, you'll need to update Windows first via Settings → Update & Security → Windows Update.

### Step 1.2: Enable WSL2 Features (Recommended Method)

Microsoft has simplified WSL2 installation. Open **PowerShell as Administrator**:

1. Click the Start menu
2. Type `PowerShell`
3. Right-click on **Windows PowerShell**
4. Select **Run as administrator**
5. Click **Yes** if prompted by User Account Control

In the PowerShell window, run:

```powershell
wsl --install
```

This single command:
- Enables the WSL feature
- Enables the Virtual Machine Platform
- Downloads and installs the latest Linux kernel
- Sets WSL2 as the default
- Installs Ubuntu as the default Linux distribution

### Step 1.3: Restart Your Computer

After the installation completes, you **must restart** your computer:

```powershell
Restart-Computer
```

Or simply restart via the Start menu.

### Step 1.4: Complete Ubuntu Setup

After restarting, Windows will automatically open a terminal window to complete Ubuntu setup:

1. **Wait** for the message: "Installing, this may take a few minutes..."
2. When prompted, **create a UNIX username**:
   - Use lowercase letters only
   - Example: `janice` or `jsmith`
   - This is your Linux username (separate from Windows)
3. **Create a password**:
   - Type a password (characters won't show as you type—this is normal!)
   - Re-enter the password to confirm
   - **Remember this password**—you'll need it for installing software

> **Important**: When typing passwords in Linux terminals, nothing appears on screen. Just type your password and press Enter.

### Step 1.5: Verify WSL2 Installation

Open a new PowerShell window and run:

```powershell
wsl --list --verbose
```

You should see output like:

```
  NAME      STATE           VERSION
* Ubuntu    Running         2
```

The **VERSION** column should show `2`, confirming WSL2 is active.

### Alternative: Manual Installation (If Automatic Fails)

If `wsl --install` doesn't work, enable features manually:

```powershell
# Enable WSL
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

# Enable Virtual Machine Platform
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

Restart your computer, then:

```powershell
# Set WSL2 as default
wsl --set-default-version 2

# Install Ubuntu
wsl --install -d Ubuntu
```

---

## Part 2: Accessing and Using WSL2

Now that WSL2 is installed, let's learn how to access and use it.

### Method 1: Windows Terminal (Recommended)

Windows Terminal is a modern terminal app that makes working with WSL2 much nicer.

#### Installing Windows Terminal

1. Open the **Microsoft Store** (search for it in Start menu)
2. Search for **Windows Terminal**
3. Click **Get** or **Install**
4. Once installed, you can pin it to your taskbar

#### Opening WSL2 in Windows Terminal

1. Open **Windows Terminal**
2. Click the **dropdown arrow** (▼) next to the new tab button (+)
3. Select **Ubuntu** (or your Linux distribution)

Alternatively, press `Ctrl + Shift + 2` to open Ubuntu directly.

#### Setting Ubuntu as Default (Optional)

1. In Windows Terminal, press `Ctrl + ,` to open Settings
2. In the left sidebar, click **Startup**
3. Under "Default profile", select **Ubuntu**
4. Click **Save**

### Method 2: Direct Access via Start Menu

1. Click the **Start menu**
2. Type `Ubuntu`
3. Click on the **Ubuntu** app

### Method 3: From PowerShell or CMD

Simply type:

```powershell
wsl
```

This drops you into your default Linux distribution.

### Understanding Your File System

In WSL2, you have access to both Linux and Windows files:

| Location | Path in WSL2 | Description |
|----------|--------------|-------------|
| Linux Home | `~` or `/home/yourusername/` | Your Linux home directory |
| Windows C: Drive | `/mnt/c/` | Access Windows files |
| Windows User Folder | `/mnt/c/Users/YourWindowsUsername/` | Your Windows user directory |

#### Example: Navigating to Windows Desktop

```bash
cd /mnt/c/Users/YourName/Desktop
```

### Basic Linux Commands

Here are essential commands you'll use:

| Command | Description | Example |
|---------|-------------|---------|
| `cd` | Change directory | `cd /home/janice/projects` |
| `ls` | List files | `ls -la` |
| `pwd` | Print working directory | `pwd` |
| `mkdir` | Create directory | `mkdir projects` |
| `cp` | Copy files | `cp file.txt backup.txt` |
| `mv` | Move/rename files | `mv old.txt new.txt` |
| `rm` | Remove files | `rm file.txt` |
| `cat` | Display file contents | `cat readme.txt` |
| `clear` | Clear the terminal | `clear` |

---

## Part 3: Installing Git

Git is essential for version control and downloading (cloning) the project repository.

### Step 3.1: Update Package Lists

First, update Ubuntu's package manager:

```bash
sudo apt update
```

Enter your Linux password when prompted.

### Step 3.2: Install Git

```bash
sudo apt install git -y
```

The `-y` flag automatically answers "yes" to confirmation prompts.

### Step 3.3: Verify Installation

```bash
git --version
```

You should see output like: `git version 2.43.0`

### Step 3.4: Configure Git Identity

Git needs to know who you are for commits:

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"
```

Replace with your actual name and email.

### Step 3.5: Set Up GitHub Authentication

To push code to GitHub, you'll need authentication. The recommended method is SSH keys.

#### Generate an SSH Key

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

- Press **Enter** to accept the default file location
- Enter a passphrase (optional but recommended) or press **Enter** for none

#### Add SSH Key to ssh-agent

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

#### Copy Your Public Key

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the entire output (starts with `ssh-ed25519`).

#### Add Key to GitHub

1. Go to [github.com](https://github.com) and sign in
2. Click your profile picture → **Settings**
3. In the left sidebar, click **SSH and GPG keys**
4. Click **New SSH key**
5. Give it a title (e.g., "WSL2 Ubuntu")
6. Paste your key into the "Key" field
7. Click **Add SSH key**

#### Test the Connection

```bash
ssh -T git@github.com
```

Type `yes` if prompted about the fingerprint. You should see:
```
Hi username! You've successfully authenticated...
```

---

## Part 4: Installing Python

Ubuntu comes with Python, but we'll ensure you have the right version and tools.

### Step 4.1: Check Existing Python

```bash
python3 --version
```

Ubuntu 22.04+ includes Python 3.10+, which is suitable for this project.

### Step 4.2: Install Python Development Tools

Install pip (Python package manager) and venv (virtual environment support):

```bash
sudo apt install python3-pip python3-venv -y
```

### Step 4.3: Verify Installation

```bash
python3 --version
pip3 --version
```

You should see version numbers for both.

### Step 4.4: Create Convenient Aliases (Optional)

Make `python` and `pip` work without the `3`:

```bash
echo "alias python='python3'" >> ~/.bashrc
echo "alias pip='pip3'" >> ~/.bashrc
source ~/.bashrc
```

Now you can use `python` instead of `python3`.

---

## Part 5: Cloning the Repository

Now let's download the project from GitHub.

### Step 5.1: Create a Projects Directory

```bash
mkdir -p ~/projects
cd ~/projects
```

### Step 5.2: Clone the Repository

Using SSH (if you set up SSH keys):

```bash
git clone git@github.com:YOUR-ORGANIZATION/ospf-ayurveda-kg.git
```

Or using HTTPS (enter GitHub credentials when prompted):

```bash
git clone https://github.com/YOUR-ORGANIZATION/ospf-ayurveda-kg.git
```

> **Note**: Replace `YOUR-ORGANIZATION` with the actual GitHub organization or username.

### Step 5.3: Navigate to the Project

```bash
cd ospf-ayurveda-kg
```

### Step 5.4: Verify the Clone

```bash
ls -la
```

You should see files like:
```
CLAUDE.md
README.md
requirements.txt
src/
scripts/
docs/
data/
```

---

## Part 6: Setting Up Virtual Environment

A virtual environment isolates project dependencies from your system Python, preventing conflicts.

### Step 6.1: Create the Virtual Environment

From the project root directory:

```bash
python3 -m venv ./venv
```

This creates a `venv/` folder containing an isolated Python installation.

### Step 6.2: Activate the Virtual Environment

```bash
source ./venv/bin/activate
```

Your prompt should now show `(venv)` at the beginning:
```
(venv) janice@computer:~/projects/ospf-ayurveda-kg$
```

### Step 6.3: Verify Activation

```bash
which python
```

Should output something like:
```
/home/janice/projects/ospf-ayurveda-kg/venv/bin/python
```

### Understanding Virtual Environment Commands

| Command | Description |
|---------|-------------|
| `source ./venv/bin/activate` | Activate the virtual environment |
| `deactivate` | Exit the virtual environment |
| `which python` | Check which Python is active |

> **Important**: Always activate the virtual environment before working on the project!

---

## Part 7: Installing Python Libraries

With the virtual environment active, install the project dependencies.

### Step 7.1: Ensure Virtual Environment is Active

Look for `(venv)` in your prompt. If not visible:

```bash
source ./venv/bin/activate
```

### Step 7.2: Upgrade pip

```bash
pip install --upgrade pip
```

### Step 7.3: Install Project Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `beautifulsoup4` - HTML parsing for web scraping
- `pandas` - Data manipulation and analysis
- `requests` - HTTP requests for API calls
- Other dependencies listed in `requirements.txt`

### Step 7.4: Verify Installation

```bash
pip list
```

You should see all installed packages:
```
Package         Version
--------------- -------
beautifulsoup4  4.12.3
bs4             0.0.2
pandas          2.2.3
requests        2.32.3
...
```

### Step 7.5: Test a Quick Import

```bash
python -c "import pandas; import requests; import bs4; print('All imports successful!')"
```

---

## Part 8: Installing Neo4j

Neo4j is the graph database that stores the knowledge graph. We'll install **Neo4j Desktop** on Windows (not inside WSL2).

### Step 8.1: Download Neo4j Desktop

1. Open your Windows browser
2. Go to: [https://neo4j.com/download/](https://neo4j.com/download/)
3. Click **Download Neo4j Desktop**
4. Fill out the registration form (or sign in)
5. Download the Windows installer
6. **Copy the activation key** shown on the download page—you'll need this!

### Step 8.2: Install Neo4j Desktop

1. Run the downloaded installer (`neo4j-desktop-offline-X.X.X-setup.exe`)
2. Follow the installation wizard
3. Accept the license agreement
4. Choose installation location (default is fine)
5. Complete the installation

### Step 8.3: Launch and Activate Neo4j Desktop

1. Open **Neo4j Desktop** from the Start menu
2. When prompted, paste your **activation key**
3. Click **Activate**

### Step 8.4: Create a New Project

1. In Neo4j Desktop, click **New** → **Create project** (left sidebar)
2. Name it: `OSPF Ayurveda KG`
3. Click outside the name field to save

### Step 8.5: Create a New Database (DBMS)

1. Click on your new project
2. Click **Add** → **Local DBMS**
3. Configure:
   - **Name**: `ospf-ayurveda-kg`
   - **Password**: `neo4jneo4j`
   - **Version**: Select the latest **5.x** version (e.g., 5.26.0)
4. Click **Create**
5. Wait for the database to be created

### Step 8.6: Install the APOC Plugin

APOC provides advanced procedures needed for data import:

1. Click on your DBMS (`ospf-ayurveda-kg`)
2. Click the **Plugins** tab on the right panel
3. Find **APOC** in the list
4. Click **Install**
5. Wait for installation to complete

### Step 8.7: Configure APOC

1. Click the **...** (three dots) next to your DBMS
2. Select **Open folder** → **Configuration**
3. In the folder that opens, create a new file named `apoc.conf`
4. Add this content:

```properties
# APOC Configuration for OSPF Ayurveda KG
apoc.import.file.enabled=true
apoc.import.file.use_neo4j_config=true
apoc.export.file.enabled=true
```

5. Save the file

### Step 8.8: Start the Database

1. Click the **Start** button on your DBMS
2. Wait for the status to show **Active** (green indicator)

### Step 8.9: Test the Connection

1. Click **Open** to launch Neo4j Browser
2. Log in with:
   - **Username**: `neo4j`
   - **Password**: `neo4jneo4j`
3. Run a test query:

```cypher
RETURN "Hello from Neo4j!" AS message
```

You should see the message displayed.

---

## Part 9: Importing Data into Neo4j

Now let's load the knowledge graph data into Neo4j.

### Step 9.1: Locate the Neo4j Import Folder

1. In Neo4j Desktop, click **...** next to your DBMS
2. Select **Open folder** → **Import**
3. Note this folder path (you'll need it)

Typical path: `C:\Users\YourName\.Neo4jDesktop\relate-data\dbmss\dbms-XXXXX\import\`

### Step 9.2: Copy Data Files to Import Folder

You need to copy CSV files from the project to Neo4j's import folder.

#### Option A: Using Windows File Explorer

1. Open the project folder in WSL2:
   - In Windows Explorer, go to: `\\wsl$\Ubuntu\home\yourusername\projects\ospf-ayurveda-kg\data\processed`
   - Or navigate to `\\wsl$\Ubuntu` in the address bar
2. Copy all `.csv` files
3. Paste them into the Neo4j import folder

#### Option B: Using WSL2 Commands

From WSL2, copy files to Windows:

```bash
# First, find the Neo4j import path from Step 9.1
# Then copy files (adjust the path accordingly):

cp data/processed/*.csv /mnt/c/Users/YourName/.Neo4jDesktop/relate-data/dbmss/dbms-XXXXX/import/
cp data/raw/*.csv /mnt/c/Users/YourName/.Neo4jDesktop/relate-data/dbmss/dbms-XXXXX/import/
```

### Step 9.3: Run Cypher Import Scripts

The scripts must be run in order. Open Neo4j Browser and execute each script:

| Order | Script File | Purpose |
|-------|-------------|---------|
| 1 | `1_uniqueness_constraints.txt` | Create indexes and constraints |
| 2 | `2_formulation_plant_compound_target.txt` | Import Ayurvedic formulations |
| 3 | `3_disease_drug_target.txt` | Import disease-drug relationships |
| 4 | `4_chembl_constraints.txt` | ChemBL-specific constraints |
| 5 | `5_chembl_approved_drugs.txt` | Import approved drugs |
| 6 | `6_chembl_mechanisms_targets.txt` | Import drug mechanisms |
| 7 | `7_chembl_indications.txt` | Import drug indications |
| 8 | `8_chembl_warnings.txt` | Import safety warnings |

#### How to Run a Script

1. Open the script file from `scripts/cypher_scripts/` in a text editor
2. Copy the contents
3. Paste into Neo4j Browser's query editor
4. Click the **Play** button (▶) to execute

> **Important**: Run one `LOAD CSV` block at a time. Some scripts contain multiple blocks separated by comments.

### Step 9.4: Verify the Import

Run validation queries:

```cypher
// Count all nodes by type
MATCH (n)
RETURN labels(n) AS type, count(n) AS count
ORDER BY count DESC
```

```cypher
// Count all drugs
MATCH (d:Drug)
RETURN count(d) AS total_drugs
```

---

## Part 10: Installing Claude Code

Claude Code is an AI-powered coding assistant that runs in your terminal.

### Step 10.1: Install Node.js (Required for Claude Code)

Claude Code requires Node.js. Install it in WSL2:

```bash
# Install Node.js via NodeSource
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
```

Verify installation:

```bash
node --version
npm --version
```

### Step 10.2: Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

The `-g` flag installs it globally, making `claude` available from anywhere.

### Step 10.3: Verify Installation

```bash
claude --version
```

### Step 10.4: Authenticate Claude Code

Run Claude Code for the first time:

```bash
claude
```

Follow the prompts to:
1. Sign in with your Anthropic account
2. Authorize Claude Code to access your account
3. Complete the authentication flow

---

## Part 11: Initializing Claude Code in the Project

Claude Code uses a `CLAUDE.md` file to understand project context. This project already has one configured!

### Step 11.1: Navigate to the Project

```bash
cd ~/projects/ospf-ayurveda-kg
```

### Step 11.2: Verify CLAUDE.md Exists

```bash
ls -la CLAUDE.md
```

You should see the file listed.

### Step 11.3: Start Claude Code in the Project

```bash
claude
```

Claude Code automatically reads `CLAUDE.md` and understands:
- Project structure and architecture
- Available commands and scripts
- Data pipeline workflows
- Neo4j integration details

### Step 11.4: Test Claude Code Understanding

Try asking Claude Code about the project:

```
What data sources does this project use?
```

or

```
How do I run the ChemBL scraper?
```

### Step 11.5: Using Claude Code Effectively

| Command | Description |
|---------|-------------|
| `claude` | Start interactive session |
| `claude "your question"` | Ask a single question |
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `Ctrl + C` | Exit Claude Code |

---

## Troubleshooting

### WSL2 Issues

#### "WSL 2 requires an update to its kernel component"

Download and install the update from:
https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi

#### WSL2 is slow or unresponsive

Create a `.wslconfig` file in your Windows user folder (`C:\Users\YourName\.wslconfig`):

```ini
[wsl2]
memory=4GB
processors=2
```

Then restart WSL:
```powershell
wsl --shutdown
```

### Git Issues

#### "Permission denied (publickey)"

Your SSH key isn't set up correctly. Re-follow the SSH key steps in Part 3.

#### Git asks for password every time

You're using HTTPS. Switch to SSH:
```bash
git remote set-url origin git@github.com:ORG/ospf-ayurveda-kg.git
```

### Python Issues

#### "ModuleNotFoundError: No module named 'xyz'"

Make sure your virtual environment is activated:
```bash
source ./venv/bin/activate
pip install -r requirements.txt
```

### Neo4j Issues

#### "File not found" during LOAD CSV

- Ensure files are in the Neo4j import folder
- Verify file names are exact (case-sensitive)
- Check that APOC is configured with `apoc.import.file.enabled=true`

#### Cannot connect to database

- Verify the database is running (green "Active" status)
- Check that port 7687 is not blocked by firewall

### Claude Code Issues

#### "Command not found: claude"

Node.js wasn't installed correctly. Reinstall:
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
npm install -g @anthropic-ai/claude-code
```

---

## Quick Reference

### Essential Paths

| Item | Path |
|------|------|
| Project Root | `~/projects/ospf-ayurveda-kg` |
| Virtual Environment | `~/projects/ospf-ayurveda-kg/venv` |
| Data Files | `~/projects/ospf-ayurveda-kg/data/` |
| Cypher Scripts | `~/projects/ospf-ayurveda-kg/scripts/cypher_scripts/` |

### Essential Commands

```bash
# Navigate to project
cd ~/projects/ospf-ayurveda-kg

# Activate virtual environment
source ./venv/bin/activate

# Run ChemBL scraper (test mode)
python src/scrapers/chembl/chembl_scraper.py --test

# Start Claude Code
claude

# Deactivate virtual environment
deactivate
```

### Neo4j Credentials

| Property | Value |
|----------|-------|
| Username | neo4j |
| Password | neo4jneo4j |
| Bolt URI | bolt://localhost:7687 |
| HTTP URI | http://localhost:7474 |

### Daily Workflow

1. Open Windows Terminal
2. Select Ubuntu profile
3. Navigate to project: `cd ~/projects/ospf-ayurveda-kg`
4. Activate venv: `source ./venv/bin/activate`
5. Start Claude Code: `claude`
6. Work on your tasks!

---

## Next Steps

After completing this setup:

1. **Explore the codebase** - Read through `CLAUDE.md` and `docs/project-info.md`
2. **Run the scrapers** - Try `python src/scrapers/chembl/chembl_scraper.py --test`
3. **Query Neo4j** - Open Neo4j Browser and run `analysis_queries.txt`
4. **Ask Claude Code** - Use `claude` to help you understand and modify the code

Welcome to the OSPF Ayurveda Knowledge Graph project! 🎉
