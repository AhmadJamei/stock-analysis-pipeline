import pandas as pd

def load_and_clean(file_path):
    df = pd.read_csv(file_path)

    # تبدیل ستون تاریخ به datetime
    df.rename(columns={df.columns[0]: "date"}, inplace=True)

    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)

    # مرتب‌سازی
    df = df.sort_index()

    # حذف NaN
    df = df.dropna()

    # تبدیل نوع داده‌ها
    df = df.astype(float)

    print("Cleaned Data:")
    print(df.head())
    print("\nSummary:")

    return df