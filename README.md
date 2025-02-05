# SP25_DS5111_djz6nn

## VM Bootstrap Setup

### Overview
This repository contains automation scripts to quickly set up a development environment on an AWS Ubuntu VM. These steps ensure that a new instance can be configured efficiently in case of failure or new setup.

---

## 1. Recreate a VM with Bootstrap Script

### Step 1: Manually Update the System
A new VM should **always** start with updating its package list:
```bash
sudo apt update
```

### Step 2: Run the Initialization Script
This script installs necessary packages for development:
```bash
bash init.sh
```

---

## 2. Setting Up the Project

### Step 3: Clone This Repository
```bash
git clone <your-repo-url>
cd SP25_DS5111_djz6nn
```

### Step 4: Install Required Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Set Up Virtual Environment
```bash
make update
```

---

## 3. Testing the Headless Chrome Browser

### Step 6: Run the Test Script
```bash
python scripts/test_chrome_headless.py
```
Expected output:
```
Example Domain
```

### Step 7: Run the Makefile Job
```bash
make ygainers.csv
```

---

## 4. Project Structure
To verify your setup:
```bash
tree -I env
```
Expected output:
```
.
├── LICENSE
├── Makefile
├── README.md
├── init.sh
├── requirements.txt
├── sample_data
│   └── ygainers.csv
└── scripts
    └── test_chrome_headless.py
```

---

## 5. Notes on Organization
- **Scripts** are stored in `scripts/`
- **Sample data** is in `sample_data/`
- The `Makefile` automates setup and testing.
