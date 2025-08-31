# Project Name

This project is a Python package that works with Apache Spark to process user interactions and reviews.  
**This project is about cleaning and analyzing the data from the input CSV files and producing output statistics for each user.**

---

## 🚀 Getting Started

### Open in Development Container

1. Install the **Dev Containers extension** in VS Code.  
2. Open this project folder in VS Code.  
3. Click on **"Open in Container"** (bottom right corner or via Command Palette).  
4. VS Code will build the development container with all dependencies.  
5. Once inside the container, you can run scripts like `main.py` or work with the package.

---

## ⚙️ Environment Variables

Before running the project, create a `.env` file in the root directory of the project and fill in the required values.

| Environment Variable         | Description                                        | Example Value              |
|------------------------------|--------------------------------------------------|---------------------------|
| `USER_INTERACTION_PATH`      | Path to the CSV file containing user interactions | `/data/user_interactions.csv` |
| `PRODUCT_CATALOG_PATH`       | Path to the CSV file containing product catalog  | `/data/product_catalog.csv`   |
| `USER_REVIEW_PATH`           | Path to the CSV file containing user reviews     | `/data/user_reviews.csv`      |
| `LOG_DIR`                | Path to the folder where log files will be saved | `/data/output/`              |

**Example `.env` file:**

```env
USER_INTERACTION_PATH=/data/user_interactions.csv
PRODUCT_CATALOG_PATH=/data/product_catalog.csv
USER_REVIEW_PATH=/data/user_reviews.csv
LOG_DIR=/data/logs/