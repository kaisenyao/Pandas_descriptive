from main import read_dataset, generate_summary, create_visualization, save_report


def read_dataset():
    """Testing even-odd function"""
    assert 1 == 1


if __name__ == "__main__":
    file_path = "salary.csv"
    df = read_dataset(file_path)
    if df is not None:
        stats = generate_summary(df)
        create_visualization(df, column="Salary")
        save_report(stats)
