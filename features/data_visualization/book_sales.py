import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import calendar

from features.show_data.book_sales import show_sales_data

def visualize_book_sales(connection):
    try: 
        df = show_sales_data(connection)
        df_sorted = df.groupby('book_name')['quantity'].sum().reset_index().sort_values(by='quantity', ascending=False)

        plt.figure(figsize=(10,6))
        sns.barplot(x=df_sorted['quantity'], y=df_sorted['book_name'], hue=df_sorted['book_name'], legend=False, palette='Pastel2')

        for container in plt.gca().containers:
            plt.bar_label(container)
        
            
        plt.title('Jumlah Penjualan Buku')
        plt.xlabel('Jumlah Penjualan')
        plt.ylabel('Buku')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan saat memvisualisasikan data penjualan: {e}")
        return

    try: 
        df = show_sales_data(connection)

        plot_df = (
            df.groupby(['book_name', 'branch'], as_index=False)['quantity'].sum().head(20)
        )
        order = (
            plot_df.groupby('book_name')['quantity']
            .sum()
            .sort_values(ascending=False)
            .index
        )

        plt.figure(figsize=(20, 10))
        sns.barplot(data=plot_df, x='quantity', y='book_name', hue='branch', legend=True, palette='Pastel2')

        for container in plt.gca().containers:
            plt.bar_label(container)

        plt.title('Jumlah Penjualan Buku Di Setiap Cabang')
        plt.xlabel('Jumlah Penjualan')
        plt.ylabel('Buku')
        plt.xticks(rotation=45)
        plt.legend(title='Cabang')
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan saat memvisualisasikan data penjualan: {e}")
        return
def visualize_revenue_by_books(connection):
    try:
        df = show_sales_data(connection)
        df_sorted = df.groupby('book_name')['sales'].sum().reset_index().sort_values(by='sales', ascending=False)

        plt.figure(figsize=(10,6))
        sns.barplot(x=df_sorted['sales'], y=df_sorted['book_name'], hue=df_sorted['book_name'], legend=False, palette='Pastel2')

        for container in plt.gca().containers:
            plt.bar_label(container)
        
            
        plt.title('Pendapatan Dari Penjualan Buku')
        plt.xlabel('Pendapatan (Rp)')
        plt.ylabel('Buku')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan saat memvisualisasikan data penjualan: {e}")
        return

def visualize_point_redemption_by_books(connection):
    try:
        df = show_sales_data(connection)
        df_sorted = df.groupby('book_name')['redeemed_points'].sum().reset_index().sort_values(by='redeemed_points', ascending=False)

        plt.figure(figsize=(10,6))
        sns.barplot(x=df_sorted['redeemed_points'], y=df_sorted['book_name'], hue=df_sorted['book_name'], legend=False, palette='Pastel2')

        for container in plt.gca().containers:
            plt.bar_label(container)
        
            
        plt.title('Redemption Poin Dari Penjualan Buku')
        plt.xlabel('Poin')
        plt.ylabel('Buku')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan saat memvisualisasikan data penjualan: {e}")
        return

def visualize_member_distribution(connection):
    try:
        df = show_sales_data(connection)
        member_counts = df['user_name'].nunique()
        non_member_counts = df[df['user_name'].isnull()]['quantity'].sum()

        labels = ['Member', 'Non-Member']
        sizes = [member_counts, non_member_counts]
        colors = ['#66b3ff', '#ff9999']

        plt.figure(figsize=(6,6))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.title('Distribusi Member yang Melakukan Transaksi')
        plt.axis('equal')
        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan saat memvisualisasikan distribusi member: {e}")
        return

def visualize_sales_trend_per_year(connection):
    try:
        df = show_sales_data(connection)

        df['transaction_date'] = pd.to_datetime(df['transaction_date'])

        year = int(input("Masukkan tahun untuk melihat tren penjualan (YYYY): "))
        df_year = df[df['transaction_date'].dt.year == year]

        monthly_sales = (
            df_year.groupby(df_year['transaction_date'].dt.month)['sales'].sum()
        )

        monthly_sales.index = [calendar.month_abbr[m] for m in monthly_sales.index]

        plt.figure(figsize=(10,6))
        monthly_sales.plot(marker='o', color='#66b3ff')

        plt.title(f'Tren Penjualan - Tahun {year}')
        plt.xlabel('Bulan')
        plt.ylabel('Pendapatan')
        plt.grid(alpha=0.7)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan saat memvisualisasikan data: {e}")
        return