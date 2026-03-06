from enum import Enum

USER_POINT_DIVIDER = float(1000)
class UserTier(Enum):
    TIER_BRONZE = "bronze"
    TIER_SILVER = "silver"
    TIER_GOLD = "gold"
    TIER_PLATINUM = "platinum"
    TIER_DIAMOND = "diamond"