# SP25_DS5111_djz6nn

![Feature Validation](https://github.com/lmedal/SP25_DS5111_djz6nn/actions/workflows/validations.yml/badge.svg)

## VM Bootstrap & Project Setup Guide

### Overview
This repository contains automation scripts to quickly set up a development environment on an AWS Ubuntu VM. These steps ensure a new instance can be configured efficiently in case of failure or a fresh setup.

---

## 1. Recreate a VM with Bootstrap Script

### Step 1: Manually Update the System
```bash
sudo apt update
```

### Step 2: Set Up SSH & Clone Repository
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
git clone git@github.com:your-username/SP25_DS5111_djz6nn.git
cd SP25_DS5111_djz6nn
```

### Step 3: Run the Initialization Script
```bash
bash init.sh
```
This installs `make`, `python3-venv`, `tree`, and updates packages.

---

## 2. Setting Up the Project

### Step 4: Install Required Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Set Up Virtual Environment
```bash
make update
```

---

## 3. Running & Testing the Headless Chrome Browser

### Step 6: Verify Chrome Headless
```bash
python scripts/test_chrome_headless.py
```
✅ Expected Output:
```
Example Domain
```

### Step 7: Run Data Scraping
```bash
make ygainers.csv
make wjsgainers.csv
```
This scrapes stock gainers from Yahoo Finance & WSJ.

---

## 4. Project Structure
```bash
tree -I env
```
✅ Expected output:
```
.
├── LICENSE
├── Makefile
├── README.md
├── init.sh
├── requirements.txt
├── sample_data
│   ├── wjsgainers.csv
│   ├── ygainers.csv
│   ├── wjsgainers.html
│   └── ygainers.html
└── scripts
    ├── test_chrome_headless.py
    └── test_wsj_selenium.py
```

---




