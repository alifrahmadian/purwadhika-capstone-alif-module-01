import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from features.show_data.book_stocks import show_book_stock_data

def visualize_book_stocks(connection):
    try:
        df = show_book_stock_data(connection)
        df_sorted = df.groupby('book_name')['stock'].sum().reset_index().sort_values(by='stock', ascending=False)

        plt.figure(figsize=(10,6))
        sns.barplot(x=df_sorted['stock'], y=df_sorted['book_name'], hue=df_sorted['book_name'], legend=False, palette='Pastel2')

        for container in plt.gca().containers:
            plt.bar_label(container)
        
        plt.title('Jumlah Stok Buku Yang Tersedia di Seluruh Cabang')
        plt.xlabel('Jumlah Stok')
        plt.ylabel('Buku')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan saat memvisualisasikan data stok buku: {e}")
        return

def visualize_book_stocks_by_branch(connection):
    try:
        df = show_book_stock_data(connection)

        plot_df = (
            df.groupby(['book_name', 'branch'], as_index=False)['stock'].sum()
        )

        order = (
            plot_df.groupby('book_name')['stock']
            .sum()
            .sort_values(ascending=False)
            .index
        )

        plt.figure(figsize=(10,6))
        sns.barplot(data=plot_df, y='book_name', x='stock', hue='branch', legend=True, palette='Pastel2', order=order)

        for container in plt.gca().containers:
            plt.bar_label(container)
        
        plt.title('Jumlah Stok Buku Yang Tersedia di Setiap Cabang')
        plt.xlabel('Stok')
        plt.ylabel('Buku')
        plt.legend(title='Cabang')
        plt.xticks(rotation=45)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan saat memvisualisasikan data stok buku berdasarkan cabang: {e}")
        return

def visualize_book_stocks_by_genre(connection):
    try:
        df = show_book_stock_data(connection)
        df_sorted = df.groupby('genre_name')['stock'].sum().reset_index().sort_values(by='stock', ascending=False)

        plt.figure(figsize=(10,6))
        sns.barplot(x=df_sorted['genre_name'], y=df_sorted['stock'], hue=df_sorted['stock'], legend=False, palette='Pastel2')

        for container in plt.gca().containers:
            plt.bar_label(container)
        
        plt.title('Jumlah Stok Buku Berdasarkan Genre')
        plt.xlabel('Jumlah Stok')
        plt.ylabel('Genre')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan saat memvisualisasikan data stok buku berdasarkan genre: {e}")
        return

def visualize_book_stocks_by_genre_and_branch(connection):
    try:
        df = show_book_stock_data(connection)

        plot_df = (
            df.groupby(['genre_name', 'branch'], as_index=False)['stock'].sum()
        )

        order = (
            plot_df.groupby('genre_name')['stock']
            .sum()
            .sort_values(ascending=False)
            .index
        )

        plt.figure(figsize=(10,6))
        sns.barplot(data=plot_df, y='genre_name', x='stock', hue='branch', legend=True, palette='Pastel2', order=order)

        for container in plt.gca().containers:
            plt.bar_label(container)
        
        plt.title('Jumlah Stok Buku Berdasarkan Genre di Setiap Cabang')
        plt.xlabel('Stok')
        plt.ylabel('Genre')
        plt.legend(title='Cabang')
        plt.xticks(rotation=45)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan saat memvisualisasikan data stok buku berdasarkan genre dan cabang: {e}")
        return

def visualize_book_stocks_by_genre_type(connection):
    try:
        df = show_book_stock_data(connection)
        df_sorted = df.groupby('type')['stock'].sum().reset_index().sort_values(by='stock', ascending=False)

        plt.figure(figsize=(10,6))
        sns.barplot(x=df_sorted['type'], y=df_sorted['stock'], hue=df_sorted['stock'], legend=False, palette='Pastel2')

        for container in plt.gca().containers:
            plt.bar_label(container)
        
        plt.title('Jumlah Stok Buku Berdasarkan Tipe Genre')
        plt.xlabel('Jumlah Stok')
        plt.ylabel('Tipe Genre')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan saat memvisualisasikan data stok buku berdasarkan tipe genre: {e}")
        return

def visualize_book_stocks_by_genre_type_and_branch(connection):
    try:
        df = show_book_stock_data(connection)

        plot_df = (
            df.groupby(['type', 'branch'], as_index=False)['stock'].sum()
        )

        order = (
            plot_df.groupby('type')['stock']
            .sum()
            .sort_values(ascending=False)
            .index
        )

        plt.figure(figsize=(10,6))
        sns.barplot(data=plot_df, y='type', x='stock', hue='branch', legend=True, palette='Pastel2', order=order)

        for container in plt.gca().containers:
            plt.bar_label(container)
        
        plt.title('Jumlah Stok Buku Berdasarkan Tipe Genre di Setiap Cabang')
        plt.xlabel('Stok')
        plt.ylabel('Tipe Genre')
        plt.legend(title='Cabang')
        plt.xticks(rotation=45)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan saat memvisualisasikan data stok buku berdasarkan tipe genre dan cabang: {e}")
        return

def visualize_book_stock_distribution(connection):
    try:
        df = show_book_stock_data(connection)

        plt.figure(figsize=(10,6))
        sns.histplot(df['stock'], bins=20, kde=True, color='skyblue')

        plt.title('Distribusi Stok Buku')
        plt.xlabel('Stok')
        plt.ylabel('Frekuensi')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan saat memvisualisasikan distribusi stok buku: {e}")
        return
    
def visualize_book_stock_heatmap(connection):
    try:
        df = show_book_stock_data(connection)
        pivot_table = df.pivot_table(values='stock', index='book_name', columns='branch', aggfunc='sum')

        plt.figure(figsize=(12,8))
        sns.heatmap(pivot_table, annot=True, fmt='g', cmap='Pastel2')

        plt.title('Heatmap Stok Buku Berdasarkan Buku dan Cabang')
        plt.xlabel('Cabang')
        plt.ylabel('Buku')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan saat memvisualisasikan heatmap stok buku: {e}")
        return

def visualize_book_distribution(connection):
    try:
        df = show_book_stock_data(connection)

        plt.figure(figsize=(20,10))
        sns.histplot(df['book_name'], bins=20, kde=True, color='skyblue')

        plt.title('Distribusi Buku Yang Tersedia')
        plt.xlabel('Buku')
        plt.ylabel('Frekuensi')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi kesalahan saat memvisualisasikan distribusi buku: {e}")
        return