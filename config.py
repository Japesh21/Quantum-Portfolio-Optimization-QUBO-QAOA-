"""
Global project configuration file.

Modify this file instead of editing paths inside each script.
"""

import os

# ----------------------------------------
# 🔹 1. Dataset Location
# ----------------------------------------
DATA_FILE = os.path.join("data", "fortune1000_2024.csv")

# ----------------------------------------
# 🔹 2. Output Folders
# ----------------------------------------
RESULT_01 = "01_result"
RESULT_02 = "02_feature"
RESULT_03 = "03_result"
RESULT_04 = "04_result"

# Create folders if needed
for folder in [RESULT_01, RESULT_02, RESULT_03, RESULT_04]:
    os.makedirs(folder, exist_ok=True)

# ----------------------------------------
# 🔹 3. Model Parameters
# ----------------------------------------
TOP_N_COMPANIES = 20          # How many companies to include
RISK_AVERSION = 0.5           # Risk-return tradeoff

# ----------------------------------------
# 🔹 4. Random Covariance Matrix Seed
# ----------------------------------------
RANDOM_SEED = 42
