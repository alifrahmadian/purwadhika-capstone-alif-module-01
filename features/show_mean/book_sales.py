import pandas as pd

from features.show_data.book_sales import show_sales_data

def show_sales_summary(connection):
    df = show_sales_data(connection)

    total_transactions = len(df)
    total_books_sold = df['quantity'].sum()
    total_revenue = df['sales'].sum()
    avg_sales = df['sales'].mean()

    member_transactions = df['user_name'].notna().sum() if 'user_name' in df.columns else 0
    non_member_transactions = df['user_name'].isna().sum() if 'user_name' in df.columns else 0

    print("\n=== SALES SUMMARY ===")
    print(f"Total transaksi       : {total_transactions}")
    print(f"Total buku terjual    : {total_books_sold}")
    print(f"Total revenue         : Rp{total_revenue:,.0f}")
    print(f"Rata-rata per transaksi: Rp{avg_sales:,.0f}")
    print(f"Transaksi member      : {member_transactions}")
    print(f"Transaksi non-member  : {non_member_transactions}")

def show_best_selling_books(connection, top_n=10):
    df = show_sales_data(connection)

    result = (
        df.groupby('book_name', as_index=False)
          .agg(
              total_sold=('quantity', 'sum'),
              total_revenue=('sales', 'sum')
          )
          .sort_values(by='total_sold', ascending=False)
          .head(top_n)
    )

    print(f"\n=== {top_n} BUKU TERLARIS===")
    print(result.to_string(index=False))

def show_top_branches(connection):
    df = show_sales_data(connection)

    result = (
        df.groupby('branch', as_index=False)
          .agg(
              total_transactions=('sales', 'count'),
              total_quantity=('quantity', 'sum'),
              total_revenue=('sales', 'sum'),
              avg_sales=('sales', 'mean')
          )
          .sort_values(by='total_revenue', ascending=False)
    )

    result['avg_sales'] = result['avg_sales'].round(2)

    print("\n=== Cabang Dengan Penjualan Tertinggi ===")
    print(result.to_string(index=False))

def show_monthly_sales_trend(connection, year):
    df = show_sales_data(connection)
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])

    df_year = df[df['transaction_date'].dt.year == year]

    if df_year.empty:
        print(f"\nTidak ada data penjualan untuk tahun {year}.")
        return

    result = (
        df_year.groupby(df_year['transaction_date'].dt.month, as_index=False)
               .agg(
                   total_quantity=('quantity', 'sum'),
                   total_revenue=('sales', 'sum'),
                   avg_sales=('sales', 'mean')
               )
               .sort_values(by='transaction_date')
    )

    result['avg_sales'] = result['avg_sales'].round(2)

    month_map = {
        1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr',
        5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
        9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
    }

    result['month'] = result['transaction_date'].map(month_map)
    result = result[['month', 'total_quantity', 'total_revenue', 'avg_sales']]

    print(f"\n=== TREND PENJUALAN BULANAN - {year} ===")
    print(result.to_string(index=False))
    print(f"Jumlah rata-rata penjualan dalam satu tahun: Rp{result['avg_sales'].sum()}")

def show_payment_method_stats(connection):
    df = show_sales_data(connection)

    result = (
        df.groupby('payment_method', as_index=False)
          .agg(
              total_transactions=('payment_method', 'count'),
              total_revenue=('sales', 'sum'),
              avg_sales=('sales', 'mean')
          )
          .sort_values(by='total_transactions', ascending=False)
    )
    result['avg_sales'] = result['avg_sales'].round(2)

    print("\n=== STATISTIK METODE PEMBAYARAN ===")
    print(result.to_string(index=False))