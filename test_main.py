from main import read_dataset, generate_summary, create_visualization, save_report


def test_read_dataset():
    dataset = read_dataset("salary.csv")

    # Check if the dataset has the correct number of columns
    assert dataset.shape[1] == 6, "Incorrect number of columns"

    # Check if certain columns exist
    assert "Age" in dataset.columns, "Column 'Age' is missing"
    assert "Gender" in dataset.columns, "Column 'Gender' is missing"
    assert "Salary" in dataset.columns, "Column 'Salary' is missing"

    print("Success")


if __name__ == "__main__":
    file_path = "salary.csv"
    df = read_dataset(file_path)
    if df is not None:
        stats = generate_summary(df)
        create_visualization(df, column="Salary")
        save_report(stats)
