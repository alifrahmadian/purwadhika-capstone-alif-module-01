import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from features.show_data.books import show_book_data

def visualize_reserved_stocks(connection):
    try:
        df = show_book_data(connection)
        df_sorted = df.sort_values(by='Reserved Stock', ascending=False)

        plt.figure(figsize=(10,6))
        sns.barplot(x=df_sorted['Reserved Stock'], y=df_sorted['Book Name'], hue=df_sorted['Book Name'], legend=False, palette='Pastel2')

        for container in plt.gca().containers:
            plt.bar_label(container)

        plt.title('Jumlah Reserved Stock Per Buku')
        plt.xlabel('Jumlah Reserved Stock')
        plt.ylabel('Buku')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi error saat mengambil data buku: {e}")
        return

def visualize_reserved_stocks_by_genre(connection):
    try:
        df = show_book_data(connection)
        df_sorted = df.groupby('Genre')['Reserved Stock'].sum().reset_index().sort_values(by='Reserved Stock', ascending=False)

        plt.figure(figsize=(10,6))
        sns.barplot(x=df_sorted['Genre'], y=df_sorted['Reserved Stock'], hue=df_sorted['Genre'], legend=False, palette='Pastel2')

        for container in plt.gca().containers:
            plt.bar_label(container)

        plt.title('Jumlah Reserved Stock Per Genre')
        plt.xlabel('Genre')
        plt.ylabel('Jumlah Reserved Stock')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi error saat mengambil data buku: {e}")
        return

def visualize_reserved_stocks_by_author(connection):
    try:
        df = show_book_data(connection)
        df_sorted = df.groupby('Author')['Reserved Stock'].sum().reset_index().sort_values(by='Reserved Stock', ascending=False)
        
        plt.figure(figsize=(10,6))
        sns.barplot(x=df_sorted['Reserved Stock'], y=df_sorted['Author'], hue=df_sorted['Author'], legend=False, palette='Pastel2')

        for container in plt.gca().containers:
            plt.bar_label(container)

        plt.title('Jumlah Reserved Stock Berdasarkan Penulis')
        plt.xlabel('Penulis')
        plt.ylabel('Jumlah Reserved Stock')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi error saat mengambil data buku: {e}")
        return

def visualize_reserved_stocks_by_genre_type(connection):
    try:
        df = show_book_data(connection)
        df_sorted = df.groupby('Genre Type')['Reserved Stock'].sum().reset_index().sort_values(by='Reserved Stock', ascending=False)
        
        plt.figure(figsize=(10,6))
        sns.barplot(x=df_sorted['Genre Type'], y=df_sorted['Reserved Stock'], hue=df_sorted['Genre Type'], legend=False, palette='Pastel2')

        for container in plt.gca().containers:
            plt.bar_label(container)

        plt.title('Jumlah Reserved Stock Tipe Genre')
        plt.xlabel('Tipe Genre')
        plt.ylabel('Jumlah Reserved Stock')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi error saat mengambil data buku: {e}")
        return

def visualize_book_price_distribution(connection):
    try:
        df = show_book_data(connection)

        plt.figure(figsize=(10,6))
        sns.histplot(df['Price(Rp)'], bins=10, kde=True, color='#9AC91C')

        plt.title('Distribusi Harga Buku')
        plt.xlabel('Harga (Rp)')
        plt.ylabel('Frekuensi')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi error saat mengambil data buku: {e}")
        return
    
def visualize_book_reserved_stock_distribution(connection):
    try:
        df = show_book_data(connection)

        plt.figure(figsize=(10,6))
        sns.histplot(df['Reserved Stock'], bins=10, kde=True, color='#9AC91C')

        plt.title('Distribusi Reserved Stock')
        plt.xlabel('Reserved Stock)')
        plt.ylabel('Frekuensi')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Terjadi error saat mengambil data buku: {e}")
        return