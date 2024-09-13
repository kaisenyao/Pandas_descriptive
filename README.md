
# IDS706 Pandas Assignment by Kaisen Yao

[![CI](https://github.com/kaisenyao/Pandas_descriptive/actions/workflows/workflow.yml/badge.svg)](https://github.com/kaisenyao/Pandas_descriptive/actions/workflows/workflow.yml)

This repository contains my work for the **Pandas Descriptive Statistics Script** assignment in IDS 706. The script reads a dataset, generates summary statistics, and creates a data visualization. To use it, simply link it to a GitHub codespace and wait for the devcontainer to run the Makefile, which will execute the following tasks: install, format, lint, and test.

This repository includes the following components:

* `.devcontainer`
* `Makefile`
* `requirements.txt`
* `README.md` 
* `githubactions` 
* `Dockerfile`

## Purpose
The purpose of this project is to create a Python script that performs descriptive statistics on a given dataset using Pandas. The script:
1. Reads a dataset (CSV).
2. Generates key summary statistics such as mean, median, and standard deviation.
3. Creates a histogram to visualize the distribution of a numerical column.

The project uses `matplotlib` for data visualization and provides a markdown report summarizing the results.

## Preparation
1. Open codespaces.
2. Load repo to codespaces.
3. Wait for the installation of all the requirements in `requirements.txt`.
4. Run the Makefile code: `make all`.

## Outputs

1. **Summary Report**: The script computes and outputs important summary statistics rounded to 2 decimal places for numerical columns like `Age`, `Years of Experience`, and `Salary`. 

   [Download the summary report](sandbox:/mnt/data/summary_report.md)

2. **Salary Distribution Visualization**: A histogram showcasing the distribution of salary in the dataset is generated.

   ![Salary Distribution](data_visualization.png)

## Example Output

Here’s an example of the summary statistics generated by the script:

|       | Age   | Years of Experience | Salary   |
|-------|-------|---------------------|----------|
| count | 10.00 | 10.00               | 10.00    |
| mean  | 36.50 | 9.80                | 107500.00|
| std   | 9.63  | 5.64                | 50166.48 |
| min   | 22.00 | 3.00                | 60000.00 |
| 50%   | 36.00 | 7.50                | 90000.00 |
| max   | 52.00 | 20.00               | 200000.00|

The script provides a clean and concise summary of the dataset's most important numerical fields.
