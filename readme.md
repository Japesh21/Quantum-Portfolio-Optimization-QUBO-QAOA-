# Quantum Portfolio Optimization (QUBO + QAOA)

This project demonstrates a full workflow for portfolio optimization using both **classical** and **quantum-inspired** techniques:

- Classical QUBO brute-force solver  
- Quantum QAOA solver using Qiskit  
- Data preparation + feature engineering pipeline  
- Visualization and results export  

---

## 📁 Project File Overview

.
├── config.py
├── 01_data_prep.py
├── 02_feature_engineering.py
├── 03_qubo.py
├── 04_qaoa_runner.py
├── requirements.txt
├── README.md
└── .gitignore

yaml
Copy code

---

## 🧩 How the Project Works

### 1️⃣ **Data Preparation** (`01_data_prep.py`)
- Loads your CSV dataset  
- Picks the top N companies  
- Computes ExpectedReturn  
- Creates a random covariance matrix for demo  
- Saves results to: `01_result/`

---

### 2️⃣ **Feature Engineering** (`02_feature_engineering.py`)
- Normalizes numeric columns (MarketCap, Revenues, Profits, ExpectedReturn)  
- Copies covariance matrix  
- Saves results to: `02_feature/`

---

### 3️⃣ **Classical QUBO Solver** (`03_qubo.py`)
- Builds QUBO matrix (risk + return tradeoff)  
- Uses brute-force search  
- Saves optimized selections to `03_result/`

---

### 4️⃣ **Quantum QAOA Solver** (`04_qaoa_runner.py`)
- Converts the problem to a QuadraticProgram  
- Runs QAOA using Qiskit  
- Saves optimized selections to `04_result/`

---

## 🚀 Setup & Installation

### 1. Install dependencies

```bash
pip install -r requirements.txt
2. Add your dataset
Place your data file here:

bash
Copy code
data/fortune1000_2024.csv
Then update config.py:

python
Copy code
DATA_FILE = "data/fortune1000_2024.csv"
3. Run scripts in order
bash
Copy code
python 01_data_prep.py
python 02_feature_engineering.py
python 03_qubo.py
python 04_qaoa_runner.py
🛠 Configurable Parameters
Edit config.py to control:

Dataset path

Output folders

Number of companies (N)

Risk aversion