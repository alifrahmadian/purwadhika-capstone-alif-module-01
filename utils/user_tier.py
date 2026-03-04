from constants.user_tier import UserTier as tier

"""
Aturan tier:

Dalam setiap transaksi Rp1.000, user akan mendapatkan 1 poin: 
    Jika user melakukan transaksi sebesar Rp250.000, maka perolehan poin yang didapat adalah Rp250.000/Rp1.000 = 250 poin

Tier yang tersedia:
1. Bronze (0 - 999 poin) 
2. Silver (1000 - 2499 poin)
3. Gold (2500 - 4999 poin)
4. Platinum (5000 - 7499 poin)
5. Diamond (7500+ poin)

Untuk saat ini, tidak ada fitur point expiry, sehingga jumlah poin yang didapat oleh user permanen

Fitur optional (tukar dengan point pada saat melakukan transaksi)
"""

def add_user_point(transaction_amount:float):
    """
    Fungsi ini bertujuan untuk menambahkan poin berdasarkan jumlah transaksi user tersebut
    """
    pass

def set_user_tier(points:int):
    """
    Fungsi ini bertujuan untuk setting tier user, dan selalu dipanggil ketika user melakukan transaksi meskipun tiernya tidak naik level (setiap user melakukan transaksi, tier user selalu dicek)
    """

    if points >= 0 and points <= 999:
        return tier.TIER_BRONZE.value
    elif points >= 1000 and points <= 2499:
        return tier.TIER_SILVER.value
    elif points >= 2500 and points <= 4999:
        return tier.TIER_GOLD.value
    elif points >= 5000 and points <= 7499:
        return tier.TIER_PLATINUM.value
    else:
        return tier.TIER_DIAMOND.value



