import pandas as pd
import matplotlib.pyplot as plt


def read_dataset(file_path):
    df = pd.read_csv(file_path)
    print("Dataset successfully loaded!")
    print("Columns in dataset:", df.columns)
    return df


def generate_summary(df):
    numeric_columns = ["Age", "Years of Experience", "Salary"]
    print("\nImportant Summary Statistics (Rounded to 2 Decimals):")
    summary = (
        df[numeric_columns]
        .describe()
        .loc[["count", "mean", "std", "min", "50%", "max"]]
        .round(2)
    )
    print(summary)

    stats = {
        "Mean": df[numeric_columns].mean().round(2),
        "Median": df[numeric_columns].median().round(2),
        "Standard Deviation": df[numeric_columns].std().round(2),
    }
    return stats


def create_visualization(df, column):
    plt.figure(figsize=(10, 6))
    df[column].hist(bins=20, edgecolor="black")
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(False)
    plt.savefig("data_visualization.png")
    plt.show()


def save_report(stats, output_file="summary_report.md"):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Summary Report\n\n")
        for key, value in stats.items():
            f.write(f"## {key}\n\n")
            f.write(f"{value}\n\n")
    print(f"Summary report saved to {output_file}")
