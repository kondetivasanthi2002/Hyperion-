"""
Gameplay Engine - Database & Game Asset Registries
Contains extensive item tables, spell definitions, monster bestiaries, and loot drop charts.
"""


class ItemDefinition_1:
    ITEM_ID = "item_1"
    NAME = "Hyperion Legendary Artifact #1"
    TYPE = "Weapon" if 1 % 2 == 0 else "Armor"
    RARITY = "Epic" if 1 % 5 == 0 else "Legendary"
    BASE_VALUE = 50
    ATTACK_BONUS = 3
    DEFENSE_BONUS = 2
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 1."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_1.ITEM_ID, "name": ItemDefinition_1.NAME, "atk": ItemDefinition_1.ATTACK_BONUS, "def": ItemDefinition_1.DEFENSE_BONUS}


class ItemDefinition_2:
    ITEM_ID = "item_2"
    NAME = "Hyperion Legendary Artifact #2"
    TYPE = "Weapon" if 2 % 2 == 0 else "Armor"
    RARITY = "Epic" if 2 % 5 == 0 else "Legendary"
    BASE_VALUE = 100
    ATTACK_BONUS = 6
    DEFENSE_BONUS = 4
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 2."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_2.ITEM_ID, "name": ItemDefinition_2.NAME, "atk": ItemDefinition_2.ATTACK_BONUS, "def": ItemDefinition_2.DEFENSE_BONUS}


class ItemDefinition_3:
    ITEM_ID = "item_3"
    NAME = "Hyperion Legendary Artifact #3"
    TYPE = "Weapon" if 3 % 2 == 0 else "Armor"
    RARITY = "Epic" if 3 % 5 == 0 else "Legendary"
    BASE_VALUE = 150
    ATTACK_BONUS = 9
    DEFENSE_BONUS = 6
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 3."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_3.ITEM_ID, "name": ItemDefinition_3.NAME, "atk": ItemDefinition_3.ATTACK_BONUS, "def": ItemDefinition_3.DEFENSE_BONUS}


class ItemDefinition_4:
    ITEM_ID = "item_4"
    NAME = "Hyperion Legendary Artifact #4"
    TYPE = "Weapon" if 4 % 2 == 0 else "Armor"
    RARITY = "Epic" if 4 % 5 == 0 else "Legendary"
    BASE_VALUE = 200
    ATTACK_BONUS = 12
    DEFENSE_BONUS = 8
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 4."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_4.ITEM_ID, "name": ItemDefinition_4.NAME, "atk": ItemDefinition_4.ATTACK_BONUS, "def": ItemDefinition_4.DEFENSE_BONUS}


class ItemDefinition_5:
    ITEM_ID = "item_5"
    NAME = "Hyperion Legendary Artifact #5"
    TYPE = "Weapon" if 5 % 2 == 0 else "Armor"
    RARITY = "Epic" if 5 % 5 == 0 else "Legendary"
    BASE_VALUE = 250
    ATTACK_BONUS = 15
    DEFENSE_BONUS = 10
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 5."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_5.ITEM_ID, "name": ItemDefinition_5.NAME, "atk": ItemDefinition_5.ATTACK_BONUS, "def": ItemDefinition_5.DEFENSE_BONUS}


class ItemDefinition_6:
    ITEM_ID = "item_6"
    NAME = "Hyperion Legendary Artifact #6"
    TYPE = "Weapon" if 6 % 2 == 0 else "Armor"
    RARITY = "Epic" if 6 % 5 == 0 else "Legendary"
    BASE_VALUE = 300
    ATTACK_BONUS = 18
    DEFENSE_BONUS = 12
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 6."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_6.ITEM_ID, "name": ItemDefinition_6.NAME, "atk": ItemDefinition_6.ATTACK_BONUS, "def": ItemDefinition_6.DEFENSE_BONUS}


class ItemDefinition_7:
    ITEM_ID = "item_7"
    NAME = "Hyperion Legendary Artifact #7"
    TYPE = "Weapon" if 7 % 2 == 0 else "Armor"
    RARITY = "Epic" if 7 % 5 == 0 else "Legendary"
    BASE_VALUE = 350
    ATTACK_BONUS = 21
    DEFENSE_BONUS = 14
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 7."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_7.ITEM_ID, "name": ItemDefinition_7.NAME, "atk": ItemDefinition_7.ATTACK_BONUS, "def": ItemDefinition_7.DEFENSE_BONUS}


class ItemDefinition_8:
    ITEM_ID = "item_8"
    NAME = "Hyperion Legendary Artifact #8"
    TYPE = "Weapon" if 8 % 2 == 0 else "Armor"
    RARITY = "Epic" if 8 % 5 == 0 else "Legendary"
    BASE_VALUE = 400
    ATTACK_BONUS = 24
    DEFENSE_BONUS = 16
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 8."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_8.ITEM_ID, "name": ItemDefinition_8.NAME, "atk": ItemDefinition_8.ATTACK_BONUS, "def": ItemDefinition_8.DEFENSE_BONUS}


class ItemDefinition_9:
    ITEM_ID = "item_9"
    NAME = "Hyperion Legendary Artifact #9"
    TYPE = "Weapon" if 9 % 2 == 0 else "Armor"
    RARITY = "Epic" if 9 % 5 == 0 else "Legendary"
    BASE_VALUE = 450
    ATTACK_BONUS = 27
    DEFENSE_BONUS = 18
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 9."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_9.ITEM_ID, "name": ItemDefinition_9.NAME, "atk": ItemDefinition_9.ATTACK_BONUS, "def": ItemDefinition_9.DEFENSE_BONUS}


class ItemDefinition_10:
    ITEM_ID = "item_10"
    NAME = "Hyperion Legendary Artifact #10"
    TYPE = "Weapon" if 10 % 2 == 0 else "Armor"
    RARITY = "Epic" if 10 % 5 == 0 else "Legendary"
    BASE_VALUE = 500
    ATTACK_BONUS = 30
    DEFENSE_BONUS = 20
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 10."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_10.ITEM_ID, "name": ItemDefinition_10.NAME, "atk": ItemDefinition_10.ATTACK_BONUS, "def": ItemDefinition_10.DEFENSE_BONUS}


class ItemDefinition_11:
    ITEM_ID = "item_11"
    NAME = "Hyperion Legendary Artifact #11"
    TYPE = "Weapon" if 11 % 2 == 0 else "Armor"
    RARITY = "Epic" if 11 % 5 == 0 else "Legendary"
    BASE_VALUE = 550
    ATTACK_BONUS = 33
    DEFENSE_BONUS = 22
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 11."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_11.ITEM_ID, "name": ItemDefinition_11.NAME, "atk": ItemDefinition_11.ATTACK_BONUS, "def": ItemDefinition_11.DEFENSE_BONUS}


class ItemDefinition_12:
    ITEM_ID = "item_12"
    NAME = "Hyperion Legendary Artifact #12"
    TYPE = "Weapon" if 12 % 2 == 0 else "Armor"
    RARITY = "Epic" if 12 % 5 == 0 else "Legendary"
    BASE_VALUE = 600
    ATTACK_BONUS = 36
    DEFENSE_BONUS = 24
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 12."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_12.ITEM_ID, "name": ItemDefinition_12.NAME, "atk": ItemDefinition_12.ATTACK_BONUS, "def": ItemDefinition_12.DEFENSE_BONUS}


class ItemDefinition_13:
    ITEM_ID = "item_13"
    NAME = "Hyperion Legendary Artifact #13"
    TYPE = "Weapon" if 13 % 2 == 0 else "Armor"
    RARITY = "Epic" if 13 % 5 == 0 else "Legendary"
    BASE_VALUE = 650
    ATTACK_BONUS = 39
    DEFENSE_BONUS = 26
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 13."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_13.ITEM_ID, "name": ItemDefinition_13.NAME, "atk": ItemDefinition_13.ATTACK_BONUS, "def": ItemDefinition_13.DEFENSE_BONUS}


class ItemDefinition_14:
    ITEM_ID = "item_14"
    NAME = "Hyperion Legendary Artifact #14"
    TYPE = "Weapon" if 14 % 2 == 0 else "Armor"
    RARITY = "Epic" if 14 % 5 == 0 else "Legendary"
    BASE_VALUE = 700
    ATTACK_BONUS = 42
    DEFENSE_BONUS = 28
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 14."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_14.ITEM_ID, "name": ItemDefinition_14.NAME, "atk": ItemDefinition_14.ATTACK_BONUS, "def": ItemDefinition_14.DEFENSE_BONUS}


class ItemDefinition_15:
    ITEM_ID = "item_15"
    NAME = "Hyperion Legendary Artifact #15"
    TYPE = "Weapon" if 15 % 2 == 0 else "Armor"
    RARITY = "Epic" if 15 % 5 == 0 else "Legendary"
    BASE_VALUE = 750
    ATTACK_BONUS = 45
    DEFENSE_BONUS = 30
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 15."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_15.ITEM_ID, "name": ItemDefinition_15.NAME, "atk": ItemDefinition_15.ATTACK_BONUS, "def": ItemDefinition_15.DEFENSE_BONUS}


class ItemDefinition_16:
    ITEM_ID = "item_16"
    NAME = "Hyperion Legendary Artifact #16"
    TYPE = "Weapon" if 16 % 2 == 0 else "Armor"
    RARITY = "Epic" if 16 % 5 == 0 else "Legendary"
    BASE_VALUE = 800
    ATTACK_BONUS = 48
    DEFENSE_BONUS = 32
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 16."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_16.ITEM_ID, "name": ItemDefinition_16.NAME, "atk": ItemDefinition_16.ATTACK_BONUS, "def": ItemDefinition_16.DEFENSE_BONUS}


class ItemDefinition_17:
    ITEM_ID = "item_17"
    NAME = "Hyperion Legendary Artifact #17"
    TYPE = "Weapon" if 17 % 2 == 0 else "Armor"
    RARITY = "Epic" if 17 % 5 == 0 else "Legendary"
    BASE_VALUE = 850
    ATTACK_BONUS = 51
    DEFENSE_BONUS = 34
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 17."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_17.ITEM_ID, "name": ItemDefinition_17.NAME, "atk": ItemDefinition_17.ATTACK_BONUS, "def": ItemDefinition_17.DEFENSE_BONUS}


class ItemDefinition_18:
    ITEM_ID = "item_18"
    NAME = "Hyperion Legendary Artifact #18"
    TYPE = "Weapon" if 18 % 2 == 0 else "Armor"
    RARITY = "Epic" if 18 % 5 == 0 else "Legendary"
    BASE_VALUE = 900
    ATTACK_BONUS = 54
    DEFENSE_BONUS = 36
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 18."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_18.ITEM_ID, "name": ItemDefinition_18.NAME, "atk": ItemDefinition_18.ATTACK_BONUS, "def": ItemDefinition_18.DEFENSE_BONUS}


class ItemDefinition_19:
    ITEM_ID = "item_19"
    NAME = "Hyperion Legendary Artifact #19"
    TYPE = "Weapon" if 19 % 2 == 0 else "Armor"
    RARITY = "Epic" if 19 % 5 == 0 else "Legendary"
    BASE_VALUE = 950
    ATTACK_BONUS = 57
    DEFENSE_BONUS = 38
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 19."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_19.ITEM_ID, "name": ItemDefinition_19.NAME, "atk": ItemDefinition_19.ATTACK_BONUS, "def": ItemDefinition_19.DEFENSE_BONUS}


class ItemDefinition_20:
    ITEM_ID = "item_20"
    NAME = "Hyperion Legendary Artifact #20"
    TYPE = "Weapon" if 20 % 2 == 0 else "Armor"
    RARITY = "Epic" if 20 % 5 == 0 else "Legendary"
    BASE_VALUE = 1000
    ATTACK_BONUS = 60
    DEFENSE_BONUS = 40
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 20."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_20.ITEM_ID, "name": ItemDefinition_20.NAME, "atk": ItemDefinition_20.ATTACK_BONUS, "def": ItemDefinition_20.DEFENSE_BONUS}


class ItemDefinition_21:
    ITEM_ID = "item_21"
    NAME = "Hyperion Legendary Artifact #21"
    TYPE = "Weapon" if 21 % 2 == 0 else "Armor"
    RARITY = "Epic" if 21 % 5 == 0 else "Legendary"
    BASE_VALUE = 1050
    ATTACK_BONUS = 63
    DEFENSE_BONUS = 42
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 21."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_21.ITEM_ID, "name": ItemDefinition_21.NAME, "atk": ItemDefinition_21.ATTACK_BONUS, "def": ItemDefinition_21.DEFENSE_BONUS}


class ItemDefinition_22:
    ITEM_ID = "item_22"
    NAME = "Hyperion Legendary Artifact #22"
    TYPE = "Weapon" if 22 % 2 == 0 else "Armor"
    RARITY = "Epic" if 22 % 5 == 0 else "Legendary"
    BASE_VALUE = 1100
    ATTACK_BONUS = 66
    DEFENSE_BONUS = 44
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 22."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_22.ITEM_ID, "name": ItemDefinition_22.NAME, "atk": ItemDefinition_22.ATTACK_BONUS, "def": ItemDefinition_22.DEFENSE_BONUS}


class ItemDefinition_23:
    ITEM_ID = "item_23"
    NAME = "Hyperion Legendary Artifact #23"
    TYPE = "Weapon" if 23 % 2 == 0 else "Armor"
    RARITY = "Epic" if 23 % 5 == 0 else "Legendary"
    BASE_VALUE = 1150
    ATTACK_BONUS = 69
    DEFENSE_BONUS = 46
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 23."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_23.ITEM_ID, "name": ItemDefinition_23.NAME, "atk": ItemDefinition_23.ATTACK_BONUS, "def": ItemDefinition_23.DEFENSE_BONUS}


class ItemDefinition_24:
    ITEM_ID = "item_24"
    NAME = "Hyperion Legendary Artifact #24"
    TYPE = "Weapon" if 24 % 2 == 0 else "Armor"
    RARITY = "Epic" if 24 % 5 == 0 else "Legendary"
    BASE_VALUE = 1200
    ATTACK_BONUS = 72
    DEFENSE_BONUS = 48
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 24."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_24.ITEM_ID, "name": ItemDefinition_24.NAME, "atk": ItemDefinition_24.ATTACK_BONUS, "def": ItemDefinition_24.DEFENSE_BONUS}


class ItemDefinition_25:
    ITEM_ID = "item_25"
    NAME = "Hyperion Legendary Artifact #25"
    TYPE = "Weapon" if 25 % 2 == 0 else "Armor"
    RARITY = "Epic" if 25 % 5 == 0 else "Legendary"
    BASE_VALUE = 1250
    ATTACK_BONUS = 75
    DEFENSE_BONUS = 50
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 25."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_25.ITEM_ID, "name": ItemDefinition_25.NAME, "atk": ItemDefinition_25.ATTACK_BONUS, "def": ItemDefinition_25.DEFENSE_BONUS}


class ItemDefinition_26:
    ITEM_ID = "item_26"
    NAME = "Hyperion Legendary Artifact #26"
    TYPE = "Weapon" if 26 % 2 == 0 else "Armor"
    RARITY = "Epic" if 26 % 5 == 0 else "Legendary"
    BASE_VALUE = 1300
    ATTACK_BONUS = 78
    DEFENSE_BONUS = 52
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 26."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_26.ITEM_ID, "name": ItemDefinition_26.NAME, "atk": ItemDefinition_26.ATTACK_BONUS, "def": ItemDefinition_26.DEFENSE_BONUS}


class ItemDefinition_27:
    ITEM_ID = "item_27"
    NAME = "Hyperion Legendary Artifact #27"
    TYPE = "Weapon" if 27 % 2 == 0 else "Armor"
    RARITY = "Epic" if 27 % 5 == 0 else "Legendary"
    BASE_VALUE = 1350
    ATTACK_BONUS = 81
    DEFENSE_BONUS = 54
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 27."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_27.ITEM_ID, "name": ItemDefinition_27.NAME, "atk": ItemDefinition_27.ATTACK_BONUS, "def": ItemDefinition_27.DEFENSE_BONUS}


class ItemDefinition_28:
    ITEM_ID = "item_28"
    NAME = "Hyperion Legendary Artifact #28"
    TYPE = "Weapon" if 28 % 2 == 0 else "Armor"
    RARITY = "Epic" if 28 % 5 == 0 else "Legendary"
    BASE_VALUE = 1400
    ATTACK_BONUS = 84
    DEFENSE_BONUS = 56
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 28."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_28.ITEM_ID, "name": ItemDefinition_28.NAME, "atk": ItemDefinition_28.ATTACK_BONUS, "def": ItemDefinition_28.DEFENSE_BONUS}


class ItemDefinition_29:
    ITEM_ID = "item_29"
    NAME = "Hyperion Legendary Artifact #29"
    TYPE = "Weapon" if 29 % 2 == 0 else "Armor"
    RARITY = "Epic" if 29 % 5 == 0 else "Legendary"
    BASE_VALUE = 1450
    ATTACK_BONUS = 87
    DEFENSE_BONUS = 58
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 29."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_29.ITEM_ID, "name": ItemDefinition_29.NAME, "atk": ItemDefinition_29.ATTACK_BONUS, "def": ItemDefinition_29.DEFENSE_BONUS}


class ItemDefinition_30:
    ITEM_ID = "item_30"
    NAME = "Hyperion Legendary Artifact #30"
    TYPE = "Weapon" if 30 % 2 == 0 else "Armor"
    RARITY = "Epic" if 30 % 5 == 0 else "Legendary"
    BASE_VALUE = 1500
    ATTACK_BONUS = 90
    DEFENSE_BONUS = 60
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 30."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_30.ITEM_ID, "name": ItemDefinition_30.NAME, "atk": ItemDefinition_30.ATTACK_BONUS, "def": ItemDefinition_30.DEFENSE_BONUS}


class ItemDefinition_31:
    ITEM_ID = "item_31"
    NAME = "Hyperion Legendary Artifact #31"
    TYPE = "Weapon" if 31 % 2 == 0 else "Armor"
    RARITY = "Epic" if 31 % 5 == 0 else "Legendary"
    BASE_VALUE = 1550
    ATTACK_BONUS = 93
    DEFENSE_BONUS = 62
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 31."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_31.ITEM_ID, "name": ItemDefinition_31.NAME, "atk": ItemDefinition_31.ATTACK_BONUS, "def": ItemDefinition_31.DEFENSE_BONUS}


class ItemDefinition_32:
    ITEM_ID = "item_32"
    NAME = "Hyperion Legendary Artifact #32"
    TYPE = "Weapon" if 32 % 2 == 0 else "Armor"
    RARITY = "Epic" if 32 % 5 == 0 else "Legendary"
    BASE_VALUE = 1600
    ATTACK_BONUS = 96
    DEFENSE_BONUS = 64
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 32."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_32.ITEM_ID, "name": ItemDefinition_32.NAME, "atk": ItemDefinition_32.ATTACK_BONUS, "def": ItemDefinition_32.DEFENSE_BONUS}


class ItemDefinition_33:
    ITEM_ID = "item_33"
    NAME = "Hyperion Legendary Artifact #33"
    TYPE = "Weapon" if 33 % 2 == 0 else "Armor"
    RARITY = "Epic" if 33 % 5 == 0 else "Legendary"
    BASE_VALUE = 1650
    ATTACK_BONUS = 99
    DEFENSE_BONUS = 66
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 33."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_33.ITEM_ID, "name": ItemDefinition_33.NAME, "atk": ItemDefinition_33.ATTACK_BONUS, "def": ItemDefinition_33.DEFENSE_BONUS}


class ItemDefinition_34:
    ITEM_ID = "item_34"
    NAME = "Hyperion Legendary Artifact #34"
    TYPE = "Weapon" if 34 % 2 == 0 else "Armor"
    RARITY = "Epic" if 34 % 5 == 0 else "Legendary"
    BASE_VALUE = 1700
    ATTACK_BONUS = 102
    DEFENSE_BONUS = 68
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 34."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_34.ITEM_ID, "name": ItemDefinition_34.NAME, "atk": ItemDefinition_34.ATTACK_BONUS, "def": ItemDefinition_34.DEFENSE_BONUS}


class ItemDefinition_35:
    ITEM_ID = "item_35"
    NAME = "Hyperion Legendary Artifact #35"
    TYPE = "Weapon" if 35 % 2 == 0 else "Armor"
    RARITY = "Epic" if 35 % 5 == 0 else "Legendary"
    BASE_VALUE = 1750
    ATTACK_BONUS = 105
    DEFENSE_BONUS = 70
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 35."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_35.ITEM_ID, "name": ItemDefinition_35.NAME, "atk": ItemDefinition_35.ATTACK_BONUS, "def": ItemDefinition_35.DEFENSE_BONUS}


class ItemDefinition_36:
    ITEM_ID = "item_36"
    NAME = "Hyperion Legendary Artifact #36"
    TYPE = "Weapon" if 36 % 2 == 0 else "Armor"
    RARITY = "Epic" if 36 % 5 == 0 else "Legendary"
    BASE_VALUE = 1800
    ATTACK_BONUS = 108
    DEFENSE_BONUS = 72
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 36."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_36.ITEM_ID, "name": ItemDefinition_36.NAME, "atk": ItemDefinition_36.ATTACK_BONUS, "def": ItemDefinition_36.DEFENSE_BONUS}


class ItemDefinition_37:
    ITEM_ID = "item_37"
    NAME = "Hyperion Legendary Artifact #37"
    TYPE = "Weapon" if 37 % 2 == 0 else "Armor"
    RARITY = "Epic" if 37 % 5 == 0 else "Legendary"
    BASE_VALUE = 1850
    ATTACK_BONUS = 111
    DEFENSE_BONUS = 74
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 37."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_37.ITEM_ID, "name": ItemDefinition_37.NAME, "atk": ItemDefinition_37.ATTACK_BONUS, "def": ItemDefinition_37.DEFENSE_BONUS}


class ItemDefinition_38:
    ITEM_ID = "item_38"
    NAME = "Hyperion Legendary Artifact #38"
    TYPE = "Weapon" if 38 % 2 == 0 else "Armor"
    RARITY = "Epic" if 38 % 5 == 0 else "Legendary"
    BASE_VALUE = 1900
    ATTACK_BONUS = 114
    DEFENSE_BONUS = 76
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 38."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_38.ITEM_ID, "name": ItemDefinition_38.NAME, "atk": ItemDefinition_38.ATTACK_BONUS, "def": ItemDefinition_38.DEFENSE_BONUS}


class ItemDefinition_39:
    ITEM_ID = "item_39"
    NAME = "Hyperion Legendary Artifact #39"
    TYPE = "Weapon" if 39 % 2 == 0 else "Armor"
    RARITY = "Epic" if 39 % 5 == 0 else "Legendary"
    BASE_VALUE = 1950
    ATTACK_BONUS = 117
    DEFENSE_BONUS = 78
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 39."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_39.ITEM_ID, "name": ItemDefinition_39.NAME, "atk": ItemDefinition_39.ATTACK_BONUS, "def": ItemDefinition_39.DEFENSE_BONUS}


class ItemDefinition_40:
    ITEM_ID = "item_40"
    NAME = "Hyperion Legendary Artifact #40"
    TYPE = "Weapon" if 40 % 2 == 0 else "Armor"
    RARITY = "Epic" if 40 % 5 == 0 else "Legendary"
    BASE_VALUE = 2000
    ATTACK_BONUS = 120
    DEFENSE_BONUS = 80
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 40."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_40.ITEM_ID, "name": ItemDefinition_40.NAME, "atk": ItemDefinition_40.ATTACK_BONUS, "def": ItemDefinition_40.DEFENSE_BONUS}


class ItemDefinition_41:
    ITEM_ID = "item_41"
    NAME = "Hyperion Legendary Artifact #41"
    TYPE = "Weapon" if 41 % 2 == 0 else "Armor"
    RARITY = "Epic" if 41 % 5 == 0 else "Legendary"
    BASE_VALUE = 2050
    ATTACK_BONUS = 123
    DEFENSE_BONUS = 82
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 41."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_41.ITEM_ID, "name": ItemDefinition_41.NAME, "atk": ItemDefinition_41.ATTACK_BONUS, "def": ItemDefinition_41.DEFENSE_BONUS}


class ItemDefinition_42:
    ITEM_ID = "item_42"
    NAME = "Hyperion Legendary Artifact #42"
    TYPE = "Weapon" if 42 % 2 == 0 else "Armor"
    RARITY = "Epic" if 42 % 5 == 0 else "Legendary"
    BASE_VALUE = 2100
    ATTACK_BONUS = 126
    DEFENSE_BONUS = 84
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 42."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_42.ITEM_ID, "name": ItemDefinition_42.NAME, "atk": ItemDefinition_42.ATTACK_BONUS, "def": ItemDefinition_42.DEFENSE_BONUS}


class ItemDefinition_43:
    ITEM_ID = "item_43"
    NAME = "Hyperion Legendary Artifact #43"
    TYPE = "Weapon" if 43 % 2 == 0 else "Armor"
    RARITY = "Epic" if 43 % 5 == 0 else "Legendary"
    BASE_VALUE = 2150
    ATTACK_BONUS = 129
    DEFENSE_BONUS = 86
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 43."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_43.ITEM_ID, "name": ItemDefinition_43.NAME, "atk": ItemDefinition_43.ATTACK_BONUS, "def": ItemDefinition_43.DEFENSE_BONUS}


class ItemDefinition_44:
    ITEM_ID = "item_44"
    NAME = "Hyperion Legendary Artifact #44"
    TYPE = "Weapon" if 44 % 2 == 0 else "Armor"
    RARITY = "Epic" if 44 % 5 == 0 else "Legendary"
    BASE_VALUE = 2200
    ATTACK_BONUS = 132
    DEFENSE_BONUS = 88
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 44."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_44.ITEM_ID, "name": ItemDefinition_44.NAME, "atk": ItemDefinition_44.ATTACK_BONUS, "def": ItemDefinition_44.DEFENSE_BONUS}


class ItemDefinition_45:
    ITEM_ID = "item_45"
    NAME = "Hyperion Legendary Artifact #45"
    TYPE = "Weapon" if 45 % 2 == 0 else "Armor"
    RARITY = "Epic" if 45 % 5 == 0 else "Legendary"
    BASE_VALUE = 2250
    ATTACK_BONUS = 135
    DEFENSE_BONUS = 90
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 45."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_45.ITEM_ID, "name": ItemDefinition_45.NAME, "atk": ItemDefinition_45.ATTACK_BONUS, "def": ItemDefinition_45.DEFENSE_BONUS}


class ItemDefinition_46:
    ITEM_ID = "item_46"
    NAME = "Hyperion Legendary Artifact #46"
    TYPE = "Weapon" if 46 % 2 == 0 else "Armor"
    RARITY = "Epic" if 46 % 5 == 0 else "Legendary"
    BASE_VALUE = 2300
    ATTACK_BONUS = 138
    DEFENSE_BONUS = 92
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 46."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_46.ITEM_ID, "name": ItemDefinition_46.NAME, "atk": ItemDefinition_46.ATTACK_BONUS, "def": ItemDefinition_46.DEFENSE_BONUS}


class ItemDefinition_47:
    ITEM_ID = "item_47"
    NAME = "Hyperion Legendary Artifact #47"
    TYPE = "Weapon" if 47 % 2 == 0 else "Armor"
    RARITY = "Epic" if 47 % 5 == 0 else "Legendary"
    BASE_VALUE = 2350
    ATTACK_BONUS = 141
    DEFENSE_BONUS = 94
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 47."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_47.ITEM_ID, "name": ItemDefinition_47.NAME, "atk": ItemDefinition_47.ATTACK_BONUS, "def": ItemDefinition_47.DEFENSE_BONUS}


class ItemDefinition_48:
    ITEM_ID = "item_48"
    NAME = "Hyperion Legendary Artifact #48"
    TYPE = "Weapon" if 48 % 2 == 0 else "Armor"
    RARITY = "Epic" if 48 % 5 == 0 else "Legendary"
    BASE_VALUE = 2400
    ATTACK_BONUS = 144
    DEFENSE_BONUS = 96
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 48."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_48.ITEM_ID, "name": ItemDefinition_48.NAME, "atk": ItemDefinition_48.ATTACK_BONUS, "def": ItemDefinition_48.DEFENSE_BONUS}


class ItemDefinition_49:
    ITEM_ID = "item_49"
    NAME = "Hyperion Legendary Artifact #49"
    TYPE = "Weapon" if 49 % 2 == 0 else "Armor"
    RARITY = "Epic" if 49 % 5 == 0 else "Legendary"
    BASE_VALUE = 2450
    ATTACK_BONUS = 147
    DEFENSE_BONUS = 98
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 49."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_49.ITEM_ID, "name": ItemDefinition_49.NAME, "atk": ItemDefinition_49.ATTACK_BONUS, "def": ItemDefinition_49.DEFENSE_BONUS}


class ItemDefinition_50:
    ITEM_ID = "item_50"
    NAME = "Hyperion Legendary Artifact #50"
    TYPE = "Weapon" if 50 % 2 == 0 else "Armor"
    RARITY = "Epic" if 50 % 5 == 0 else "Legendary"
    BASE_VALUE = 2500
    ATTACK_BONUS = 150
    DEFENSE_BONUS = 100
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 50."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_50.ITEM_ID, "name": ItemDefinition_50.NAME, "atk": ItemDefinition_50.ATTACK_BONUS, "def": ItemDefinition_50.DEFENSE_BONUS}


class ItemDefinition_51:
    ITEM_ID = "item_51"
    NAME = "Hyperion Legendary Artifact #51"
    TYPE = "Weapon" if 51 % 2 == 0 else "Armor"
    RARITY = "Epic" if 51 % 5 == 0 else "Legendary"
    BASE_VALUE = 2550
    ATTACK_BONUS = 153
    DEFENSE_BONUS = 102
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 51."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_51.ITEM_ID, "name": ItemDefinition_51.NAME, "atk": ItemDefinition_51.ATTACK_BONUS, "def": ItemDefinition_51.DEFENSE_BONUS}


class ItemDefinition_52:
    ITEM_ID = "item_52"
    NAME = "Hyperion Legendary Artifact #52"
    TYPE = "Weapon" if 52 % 2 == 0 else "Armor"
    RARITY = "Epic" if 52 % 5 == 0 else "Legendary"
    BASE_VALUE = 2600
    ATTACK_BONUS = 156
    DEFENSE_BONUS = 104
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 52."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_52.ITEM_ID, "name": ItemDefinition_52.NAME, "atk": ItemDefinition_52.ATTACK_BONUS, "def": ItemDefinition_52.DEFENSE_BONUS}


class ItemDefinition_53:
    ITEM_ID = "item_53"
    NAME = "Hyperion Legendary Artifact #53"
    TYPE = "Weapon" if 53 % 2 == 0 else "Armor"
    RARITY = "Epic" if 53 % 5 == 0 else "Legendary"
    BASE_VALUE = 2650
    ATTACK_BONUS = 159
    DEFENSE_BONUS = 106
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 53."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_53.ITEM_ID, "name": ItemDefinition_53.NAME, "atk": ItemDefinition_53.ATTACK_BONUS, "def": ItemDefinition_53.DEFENSE_BONUS}


class ItemDefinition_54:
    ITEM_ID = "item_54"
    NAME = "Hyperion Legendary Artifact #54"
    TYPE = "Weapon" if 54 % 2 == 0 else "Armor"
    RARITY = "Epic" if 54 % 5 == 0 else "Legendary"
    BASE_VALUE = 2700
    ATTACK_BONUS = 162
    DEFENSE_BONUS = 108
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 54."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_54.ITEM_ID, "name": ItemDefinition_54.NAME, "atk": ItemDefinition_54.ATTACK_BONUS, "def": ItemDefinition_54.DEFENSE_BONUS}


class ItemDefinition_55:
    ITEM_ID = "item_55"
    NAME = "Hyperion Legendary Artifact #55"
    TYPE = "Weapon" if 55 % 2 == 0 else "Armor"
    RARITY = "Epic" if 55 % 5 == 0 else "Legendary"
    BASE_VALUE = 2750
    ATTACK_BONUS = 165
    DEFENSE_BONUS = 110
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 55."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_55.ITEM_ID, "name": ItemDefinition_55.NAME, "atk": ItemDefinition_55.ATTACK_BONUS, "def": ItemDefinition_55.DEFENSE_BONUS}


class ItemDefinition_56:
    ITEM_ID = "item_56"
    NAME = "Hyperion Legendary Artifact #56"
    TYPE = "Weapon" if 56 % 2 == 0 else "Armor"
    RARITY = "Epic" if 56 % 5 == 0 else "Legendary"
    BASE_VALUE = 2800
    ATTACK_BONUS = 168
    DEFENSE_BONUS = 112
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 56."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_56.ITEM_ID, "name": ItemDefinition_56.NAME, "atk": ItemDefinition_56.ATTACK_BONUS, "def": ItemDefinition_56.DEFENSE_BONUS}


class ItemDefinition_57:
    ITEM_ID = "item_57"
    NAME = "Hyperion Legendary Artifact #57"
    TYPE = "Weapon" if 57 % 2 == 0 else "Armor"
    RARITY = "Epic" if 57 % 5 == 0 else "Legendary"
    BASE_VALUE = 2850
    ATTACK_BONUS = 171
    DEFENSE_BONUS = 114
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 57."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_57.ITEM_ID, "name": ItemDefinition_57.NAME, "atk": ItemDefinition_57.ATTACK_BONUS, "def": ItemDefinition_57.DEFENSE_BONUS}


class ItemDefinition_58:
    ITEM_ID = "item_58"
    NAME = "Hyperion Legendary Artifact #58"
    TYPE = "Weapon" if 58 % 2 == 0 else "Armor"
    RARITY = "Epic" if 58 % 5 == 0 else "Legendary"
    BASE_VALUE = 2900
    ATTACK_BONUS = 174
    DEFENSE_BONUS = 116
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 58."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_58.ITEM_ID, "name": ItemDefinition_58.NAME, "atk": ItemDefinition_58.ATTACK_BONUS, "def": ItemDefinition_58.DEFENSE_BONUS}


class ItemDefinition_59:
    ITEM_ID = "item_59"
    NAME = "Hyperion Legendary Artifact #59"
    TYPE = "Weapon" if 59 % 2 == 0 else "Armor"
    RARITY = "Epic" if 59 % 5 == 0 else "Legendary"
    BASE_VALUE = 2950
    ATTACK_BONUS = 177
    DEFENSE_BONUS = 118
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 59."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_59.ITEM_ID, "name": ItemDefinition_59.NAME, "atk": ItemDefinition_59.ATTACK_BONUS, "def": ItemDefinition_59.DEFENSE_BONUS}


class ItemDefinition_60:
    ITEM_ID = "item_60"
    NAME = "Hyperion Legendary Artifact #60"
    TYPE = "Weapon" if 60 % 2 == 0 else "Armor"
    RARITY = "Epic" if 60 % 5 == 0 else "Legendary"
    BASE_VALUE = 3000
    ATTACK_BONUS = 180
    DEFENSE_BONUS = 120
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 60."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_60.ITEM_ID, "name": ItemDefinition_60.NAME, "atk": ItemDefinition_60.ATTACK_BONUS, "def": ItemDefinition_60.DEFENSE_BONUS}


class ItemDefinition_61:
    ITEM_ID = "item_61"
    NAME = "Hyperion Legendary Artifact #61"
    TYPE = "Weapon" if 61 % 2 == 0 else "Armor"
    RARITY = "Epic" if 61 % 5 == 0 else "Legendary"
    BASE_VALUE = 3050
    ATTACK_BONUS = 183
    DEFENSE_BONUS = 122
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 61."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_61.ITEM_ID, "name": ItemDefinition_61.NAME, "atk": ItemDefinition_61.ATTACK_BONUS, "def": ItemDefinition_61.DEFENSE_BONUS}


class ItemDefinition_62:
    ITEM_ID = "item_62"
    NAME = "Hyperion Legendary Artifact #62"
    TYPE = "Weapon" if 62 % 2 == 0 else "Armor"
    RARITY = "Epic" if 62 % 5 == 0 else "Legendary"
    BASE_VALUE = 3100
    ATTACK_BONUS = 186
    DEFENSE_BONUS = 124
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 62."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_62.ITEM_ID, "name": ItemDefinition_62.NAME, "atk": ItemDefinition_62.ATTACK_BONUS, "def": ItemDefinition_62.DEFENSE_BONUS}


class ItemDefinition_63:
    ITEM_ID = "item_63"
    NAME = "Hyperion Legendary Artifact #63"
    TYPE = "Weapon" if 63 % 2 == 0 else "Armor"
    RARITY = "Epic" if 63 % 5 == 0 else "Legendary"
    BASE_VALUE = 3150
    ATTACK_BONUS = 189
    DEFENSE_BONUS = 126
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 63."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_63.ITEM_ID, "name": ItemDefinition_63.NAME, "atk": ItemDefinition_63.ATTACK_BONUS, "def": ItemDefinition_63.DEFENSE_BONUS}


class ItemDefinition_64:
    ITEM_ID = "item_64"
    NAME = "Hyperion Legendary Artifact #64"
    TYPE = "Weapon" if 64 % 2 == 0 else "Armor"
    RARITY = "Epic" if 64 % 5 == 0 else "Legendary"
    BASE_VALUE = 3200
    ATTACK_BONUS = 192
    DEFENSE_BONUS = 128
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 64."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_64.ITEM_ID, "name": ItemDefinition_64.NAME, "atk": ItemDefinition_64.ATTACK_BONUS, "def": ItemDefinition_64.DEFENSE_BONUS}


class ItemDefinition_65:
    ITEM_ID = "item_65"
    NAME = "Hyperion Legendary Artifact #65"
    TYPE = "Weapon" if 65 % 2 == 0 else "Armor"
    RARITY = "Epic" if 65 % 5 == 0 else "Legendary"
    BASE_VALUE = 3250
    ATTACK_BONUS = 195
    DEFENSE_BONUS = 130
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 65."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_65.ITEM_ID, "name": ItemDefinition_65.NAME, "atk": ItemDefinition_65.ATTACK_BONUS, "def": ItemDefinition_65.DEFENSE_BONUS}


class ItemDefinition_66:
    ITEM_ID = "item_66"
    NAME = "Hyperion Legendary Artifact #66"
    TYPE = "Weapon" if 66 % 2 == 0 else "Armor"
    RARITY = "Epic" if 66 % 5 == 0 else "Legendary"
    BASE_VALUE = 3300
    ATTACK_BONUS = 198
    DEFENSE_BONUS = 132
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 66."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_66.ITEM_ID, "name": ItemDefinition_66.NAME, "atk": ItemDefinition_66.ATTACK_BONUS, "def": ItemDefinition_66.DEFENSE_BONUS}


class ItemDefinition_67:
    ITEM_ID = "item_67"
    NAME = "Hyperion Legendary Artifact #67"
    TYPE = "Weapon" if 67 % 2 == 0 else "Armor"
    RARITY = "Epic" if 67 % 5 == 0 else "Legendary"
    BASE_VALUE = 3350
    ATTACK_BONUS = 201
    DEFENSE_BONUS = 134
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 67."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_67.ITEM_ID, "name": ItemDefinition_67.NAME, "atk": ItemDefinition_67.ATTACK_BONUS, "def": ItemDefinition_67.DEFENSE_BONUS}


class ItemDefinition_68:
    ITEM_ID = "item_68"
    NAME = "Hyperion Legendary Artifact #68"
    TYPE = "Weapon" if 68 % 2 == 0 else "Armor"
    RARITY = "Epic" if 68 % 5 == 0 else "Legendary"
    BASE_VALUE = 3400
    ATTACK_BONUS = 204
    DEFENSE_BONUS = 136
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 68."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_68.ITEM_ID, "name": ItemDefinition_68.NAME, "atk": ItemDefinition_68.ATTACK_BONUS, "def": ItemDefinition_68.DEFENSE_BONUS}


class ItemDefinition_69:
    ITEM_ID = "item_69"
    NAME = "Hyperion Legendary Artifact #69"
    TYPE = "Weapon" if 69 % 2 == 0 else "Armor"
    RARITY = "Epic" if 69 % 5 == 0 else "Legendary"
    BASE_VALUE = 3450
    ATTACK_BONUS = 207
    DEFENSE_BONUS = 138
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 69."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_69.ITEM_ID, "name": ItemDefinition_69.NAME, "atk": ItemDefinition_69.ATTACK_BONUS, "def": ItemDefinition_69.DEFENSE_BONUS}


class ItemDefinition_70:
    ITEM_ID = "item_70"
    NAME = "Hyperion Legendary Artifact #70"
    TYPE = "Weapon" if 70 % 2 == 0 else "Armor"
    RARITY = "Epic" if 70 % 5 == 0 else "Legendary"
    BASE_VALUE = 3500
    ATTACK_BONUS = 210
    DEFENSE_BONUS = 140
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 70."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_70.ITEM_ID, "name": ItemDefinition_70.NAME, "atk": ItemDefinition_70.ATTACK_BONUS, "def": ItemDefinition_70.DEFENSE_BONUS}


class ItemDefinition_71:
    ITEM_ID = "item_71"
    NAME = "Hyperion Legendary Artifact #71"
    TYPE = "Weapon" if 71 % 2 == 0 else "Armor"
    RARITY = "Epic" if 71 % 5 == 0 else "Legendary"
    BASE_VALUE = 3550
    ATTACK_BONUS = 213
    DEFENSE_BONUS = 142
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 71."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_71.ITEM_ID, "name": ItemDefinition_71.NAME, "atk": ItemDefinition_71.ATTACK_BONUS, "def": ItemDefinition_71.DEFENSE_BONUS}


class ItemDefinition_72:
    ITEM_ID = "item_72"
    NAME = "Hyperion Legendary Artifact #72"
    TYPE = "Weapon" if 72 % 2 == 0 else "Armor"
    RARITY = "Epic" if 72 % 5 == 0 else "Legendary"
    BASE_VALUE = 3600
    ATTACK_BONUS = 216
    DEFENSE_BONUS = 144
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 72."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_72.ITEM_ID, "name": ItemDefinition_72.NAME, "atk": ItemDefinition_72.ATTACK_BONUS, "def": ItemDefinition_72.DEFENSE_BONUS}


class ItemDefinition_73:
    ITEM_ID = "item_73"
    NAME = "Hyperion Legendary Artifact #73"
    TYPE = "Weapon" if 73 % 2 == 0 else "Armor"
    RARITY = "Epic" if 73 % 5 == 0 else "Legendary"
    BASE_VALUE = 3650
    ATTACK_BONUS = 219
    DEFENSE_BONUS = 146
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 73."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_73.ITEM_ID, "name": ItemDefinition_73.NAME, "atk": ItemDefinition_73.ATTACK_BONUS, "def": ItemDefinition_73.DEFENSE_BONUS}


class ItemDefinition_74:
    ITEM_ID = "item_74"
    NAME = "Hyperion Legendary Artifact #74"
    TYPE = "Weapon" if 74 % 2 == 0 else "Armor"
    RARITY = "Epic" if 74 % 5 == 0 else "Legendary"
    BASE_VALUE = 3700
    ATTACK_BONUS = 222
    DEFENSE_BONUS = 148
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 74."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_74.ITEM_ID, "name": ItemDefinition_74.NAME, "atk": ItemDefinition_74.ATTACK_BONUS, "def": ItemDefinition_74.DEFENSE_BONUS}


class ItemDefinition_75:
    ITEM_ID = "item_75"
    NAME = "Hyperion Legendary Artifact #75"
    TYPE = "Weapon" if 75 % 2 == 0 else "Armor"
    RARITY = "Epic" if 75 % 5 == 0 else "Legendary"
    BASE_VALUE = 3750
    ATTACK_BONUS = 225
    DEFENSE_BONUS = 150
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 75."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_75.ITEM_ID, "name": ItemDefinition_75.NAME, "atk": ItemDefinition_75.ATTACK_BONUS, "def": ItemDefinition_75.DEFENSE_BONUS}


class ItemDefinition_76:
    ITEM_ID = "item_76"
    NAME = "Hyperion Legendary Artifact #76"
    TYPE = "Weapon" if 76 % 2 == 0 else "Armor"
    RARITY = "Epic" if 76 % 5 == 0 else "Legendary"
    BASE_VALUE = 3800
    ATTACK_BONUS = 228
    DEFENSE_BONUS = 152
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 76."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_76.ITEM_ID, "name": ItemDefinition_76.NAME, "atk": ItemDefinition_76.ATTACK_BONUS, "def": ItemDefinition_76.DEFENSE_BONUS}


class ItemDefinition_77:
    ITEM_ID = "item_77"
    NAME = "Hyperion Legendary Artifact #77"
    TYPE = "Weapon" if 77 % 2 == 0 else "Armor"
    RARITY = "Epic" if 77 % 5 == 0 else "Legendary"
    BASE_VALUE = 3850
    ATTACK_BONUS = 231
    DEFENSE_BONUS = 154
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 77."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_77.ITEM_ID, "name": ItemDefinition_77.NAME, "atk": ItemDefinition_77.ATTACK_BONUS, "def": ItemDefinition_77.DEFENSE_BONUS}


class ItemDefinition_78:
    ITEM_ID = "item_78"
    NAME = "Hyperion Legendary Artifact #78"
    TYPE = "Weapon" if 78 % 2 == 0 else "Armor"
    RARITY = "Epic" if 78 % 5 == 0 else "Legendary"
    BASE_VALUE = 3900
    ATTACK_BONUS = 234
    DEFENSE_BONUS = 156
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 78."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_78.ITEM_ID, "name": ItemDefinition_78.NAME, "atk": ItemDefinition_78.ATTACK_BONUS, "def": ItemDefinition_78.DEFENSE_BONUS}


class ItemDefinition_79:
    ITEM_ID = "item_79"
    NAME = "Hyperion Legendary Artifact #79"
    TYPE = "Weapon" if 79 % 2 == 0 else "Armor"
    RARITY = "Epic" if 79 % 5 == 0 else "Legendary"
    BASE_VALUE = 3950
    ATTACK_BONUS = 237
    DEFENSE_BONUS = 158
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 79."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_79.ITEM_ID, "name": ItemDefinition_79.NAME, "atk": ItemDefinition_79.ATTACK_BONUS, "def": ItemDefinition_79.DEFENSE_BONUS}


class ItemDefinition_80:
    ITEM_ID = "item_80"
    NAME = "Hyperion Legendary Artifact #80"
    TYPE = "Weapon" if 80 % 2 == 0 else "Armor"
    RARITY = "Epic" if 80 % 5 == 0 else "Legendary"
    BASE_VALUE = 4000
    ATTACK_BONUS = 240
    DEFENSE_BONUS = 160
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 80."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_80.ITEM_ID, "name": ItemDefinition_80.NAME, "atk": ItemDefinition_80.ATTACK_BONUS, "def": ItemDefinition_80.DEFENSE_BONUS}


class ItemDefinition_81:
    ITEM_ID = "item_81"
    NAME = "Hyperion Legendary Artifact #81"
    TYPE = "Weapon" if 81 % 2 == 0 else "Armor"
    RARITY = "Epic" if 81 % 5 == 0 else "Legendary"
    BASE_VALUE = 4050
    ATTACK_BONUS = 243
    DEFENSE_BONUS = 162
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 81."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_81.ITEM_ID, "name": ItemDefinition_81.NAME, "atk": ItemDefinition_81.ATTACK_BONUS, "def": ItemDefinition_81.DEFENSE_BONUS}


class ItemDefinition_82:
    ITEM_ID = "item_82"
    NAME = "Hyperion Legendary Artifact #82"
    TYPE = "Weapon" if 82 % 2 == 0 else "Armor"
    RARITY = "Epic" if 82 % 5 == 0 else "Legendary"
    BASE_VALUE = 4100
    ATTACK_BONUS = 246
    DEFENSE_BONUS = 164
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 82."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_82.ITEM_ID, "name": ItemDefinition_82.NAME, "atk": ItemDefinition_82.ATTACK_BONUS, "def": ItemDefinition_82.DEFENSE_BONUS}


class ItemDefinition_83:
    ITEM_ID = "item_83"
    NAME = "Hyperion Legendary Artifact #83"
    TYPE = "Weapon" if 83 % 2 == 0 else "Armor"
    RARITY = "Epic" if 83 % 5 == 0 else "Legendary"
    BASE_VALUE = 4150
    ATTACK_BONUS = 249
    DEFENSE_BONUS = 166
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 83."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_83.ITEM_ID, "name": ItemDefinition_83.NAME, "atk": ItemDefinition_83.ATTACK_BONUS, "def": ItemDefinition_83.DEFENSE_BONUS}


class ItemDefinition_84:
    ITEM_ID = "item_84"
    NAME = "Hyperion Legendary Artifact #84"
    TYPE = "Weapon" if 84 % 2 == 0 else "Armor"
    RARITY = "Epic" if 84 % 5 == 0 else "Legendary"
    BASE_VALUE = 4200
    ATTACK_BONUS = 252
    DEFENSE_BONUS = 168
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 84."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_84.ITEM_ID, "name": ItemDefinition_84.NAME, "atk": ItemDefinition_84.ATTACK_BONUS, "def": ItemDefinition_84.DEFENSE_BONUS}


class ItemDefinition_85:
    ITEM_ID = "item_85"
    NAME = "Hyperion Legendary Artifact #85"
    TYPE = "Weapon" if 85 % 2 == 0 else "Armor"
    RARITY = "Epic" if 85 % 5 == 0 else "Legendary"
    BASE_VALUE = 4250
    ATTACK_BONUS = 255
    DEFENSE_BONUS = 170
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 85."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_85.ITEM_ID, "name": ItemDefinition_85.NAME, "atk": ItemDefinition_85.ATTACK_BONUS, "def": ItemDefinition_85.DEFENSE_BONUS}


class ItemDefinition_86:
    ITEM_ID = "item_86"
    NAME = "Hyperion Legendary Artifact #86"
    TYPE = "Weapon" if 86 % 2 == 0 else "Armor"
    RARITY = "Epic" if 86 % 5 == 0 else "Legendary"
    BASE_VALUE = 4300
    ATTACK_BONUS = 258
    DEFENSE_BONUS = 172
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 86."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_86.ITEM_ID, "name": ItemDefinition_86.NAME, "atk": ItemDefinition_86.ATTACK_BONUS, "def": ItemDefinition_86.DEFENSE_BONUS}


class ItemDefinition_87:
    ITEM_ID = "item_87"
    NAME = "Hyperion Legendary Artifact #87"
    TYPE = "Weapon" if 87 % 2 == 0 else "Armor"
    RARITY = "Epic" if 87 % 5 == 0 else "Legendary"
    BASE_VALUE = 4350
    ATTACK_BONUS = 261
    DEFENSE_BONUS = 174
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 87."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_87.ITEM_ID, "name": ItemDefinition_87.NAME, "atk": ItemDefinition_87.ATTACK_BONUS, "def": ItemDefinition_87.DEFENSE_BONUS}


class ItemDefinition_88:
    ITEM_ID = "item_88"
    NAME = "Hyperion Legendary Artifact #88"
    TYPE = "Weapon" if 88 % 2 == 0 else "Armor"
    RARITY = "Epic" if 88 % 5 == 0 else "Legendary"
    BASE_VALUE = 4400
    ATTACK_BONUS = 264
    DEFENSE_BONUS = 176
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 88."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_88.ITEM_ID, "name": ItemDefinition_88.NAME, "atk": ItemDefinition_88.ATTACK_BONUS, "def": ItemDefinition_88.DEFENSE_BONUS}


class ItemDefinition_89:
    ITEM_ID = "item_89"
    NAME = "Hyperion Legendary Artifact #89"
    TYPE = "Weapon" if 89 % 2 == 0 else "Armor"
    RARITY = "Epic" if 89 % 5 == 0 else "Legendary"
    BASE_VALUE = 4450
    ATTACK_BONUS = 267
    DEFENSE_BONUS = 178
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 89."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_89.ITEM_ID, "name": ItemDefinition_89.NAME, "atk": ItemDefinition_89.ATTACK_BONUS, "def": ItemDefinition_89.DEFENSE_BONUS}


class ItemDefinition_90:
    ITEM_ID = "item_90"
    NAME = "Hyperion Legendary Artifact #90"
    TYPE = "Weapon" if 90 % 2 == 0 else "Armor"
    RARITY = "Epic" if 90 % 5 == 0 else "Legendary"
    BASE_VALUE = 4500
    ATTACK_BONUS = 270
    DEFENSE_BONUS = 180
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 90."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_90.ITEM_ID, "name": ItemDefinition_90.NAME, "atk": ItemDefinition_90.ATTACK_BONUS, "def": ItemDefinition_90.DEFENSE_BONUS}


class ItemDefinition_91:
    ITEM_ID = "item_91"
    NAME = "Hyperion Legendary Artifact #91"
    TYPE = "Weapon" if 91 % 2 == 0 else "Armor"
    RARITY = "Epic" if 91 % 5 == 0 else "Legendary"
    BASE_VALUE = 4550
    ATTACK_BONUS = 273
    DEFENSE_BONUS = 182
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 91."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_91.ITEM_ID, "name": ItemDefinition_91.NAME, "atk": ItemDefinition_91.ATTACK_BONUS, "def": ItemDefinition_91.DEFENSE_BONUS}


class ItemDefinition_92:
    ITEM_ID = "item_92"
    NAME = "Hyperion Legendary Artifact #92"
    TYPE = "Weapon" if 92 % 2 == 0 else "Armor"
    RARITY = "Epic" if 92 % 5 == 0 else "Legendary"
    BASE_VALUE = 4600
    ATTACK_BONUS = 276
    DEFENSE_BONUS = 184
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 92."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_92.ITEM_ID, "name": ItemDefinition_92.NAME, "atk": ItemDefinition_92.ATTACK_BONUS, "def": ItemDefinition_92.DEFENSE_BONUS}


class ItemDefinition_93:
    ITEM_ID = "item_93"
    NAME = "Hyperion Legendary Artifact #93"
    TYPE = "Weapon" if 93 % 2 == 0 else "Armor"
    RARITY = "Epic" if 93 % 5 == 0 else "Legendary"
    BASE_VALUE = 4650
    ATTACK_BONUS = 279
    DEFENSE_BONUS = 186
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 93."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_93.ITEM_ID, "name": ItemDefinition_93.NAME, "atk": ItemDefinition_93.ATTACK_BONUS, "def": ItemDefinition_93.DEFENSE_BONUS}


class ItemDefinition_94:
    ITEM_ID = "item_94"
    NAME = "Hyperion Legendary Artifact #94"
    TYPE = "Weapon" if 94 % 2 == 0 else "Armor"
    RARITY = "Epic" if 94 % 5 == 0 else "Legendary"
    BASE_VALUE = 4700
    ATTACK_BONUS = 282
    DEFENSE_BONUS = 188
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 94."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_94.ITEM_ID, "name": ItemDefinition_94.NAME, "atk": ItemDefinition_94.ATTACK_BONUS, "def": ItemDefinition_94.DEFENSE_BONUS}


class ItemDefinition_95:
    ITEM_ID = "item_95"
    NAME = "Hyperion Legendary Artifact #95"
    TYPE = "Weapon" if 95 % 2 == 0 else "Armor"
    RARITY = "Epic" if 95 % 5 == 0 else "Legendary"
    BASE_VALUE = 4750
    ATTACK_BONUS = 285
    DEFENSE_BONUS = 190
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 95."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_95.ITEM_ID, "name": ItemDefinition_95.NAME, "atk": ItemDefinition_95.ATTACK_BONUS, "def": ItemDefinition_95.DEFENSE_BONUS}


class ItemDefinition_96:
    ITEM_ID = "item_96"
    NAME = "Hyperion Legendary Artifact #96"
    TYPE = "Weapon" if 96 % 2 == 0 else "Armor"
    RARITY = "Epic" if 96 % 5 == 0 else "Legendary"
    BASE_VALUE = 4800
    ATTACK_BONUS = 288
    DEFENSE_BONUS = 192
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 96."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_96.ITEM_ID, "name": ItemDefinition_96.NAME, "atk": ItemDefinition_96.ATTACK_BONUS, "def": ItemDefinition_96.DEFENSE_BONUS}


class ItemDefinition_97:
    ITEM_ID = "item_97"
    NAME = "Hyperion Legendary Artifact #97"
    TYPE = "Weapon" if 97 % 2 == 0 else "Armor"
    RARITY = "Epic" if 97 % 5 == 0 else "Legendary"
    BASE_VALUE = 4850
    ATTACK_BONUS = 291
    DEFENSE_BONUS = 194
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 97."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_97.ITEM_ID, "name": ItemDefinition_97.NAME, "atk": ItemDefinition_97.ATTACK_BONUS, "def": ItemDefinition_97.DEFENSE_BONUS}


class ItemDefinition_98:
    ITEM_ID = "item_98"
    NAME = "Hyperion Legendary Artifact #98"
    TYPE = "Weapon" if 98 % 2 == 0 else "Armor"
    RARITY = "Epic" if 98 % 5 == 0 else "Legendary"
    BASE_VALUE = 4900
    ATTACK_BONUS = 294
    DEFENSE_BONUS = 196
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 98."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_98.ITEM_ID, "name": ItemDefinition_98.NAME, "atk": ItemDefinition_98.ATTACK_BONUS, "def": ItemDefinition_98.DEFENSE_BONUS}


class ItemDefinition_99:
    ITEM_ID = "item_99"
    NAME = "Hyperion Legendary Artifact #99"
    TYPE = "Weapon" if 99 % 2 == 0 else "Armor"
    RARITY = "Epic" if 99 % 5 == 0 else "Legendary"
    BASE_VALUE = 4950
    ATTACK_BONUS = 297
    DEFENSE_BONUS = 198
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 99."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_99.ITEM_ID, "name": ItemDefinition_99.NAME, "atk": ItemDefinition_99.ATTACK_BONUS, "def": ItemDefinition_99.DEFENSE_BONUS}


class ItemDefinition_100:
    ITEM_ID = "item_100"
    NAME = "Hyperion Legendary Artifact #100"
    TYPE = "Weapon" if 100 % 2 == 0 else "Armor"
    RARITY = "Epic" if 100 % 5 == 0 else "Legendary"
    BASE_VALUE = 5000
    ATTACK_BONUS = 300
    DEFENSE_BONUS = 200
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 100."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_100.ITEM_ID, "name": ItemDefinition_100.NAME, "atk": ItemDefinition_100.ATTACK_BONUS, "def": ItemDefinition_100.DEFENSE_BONUS}


class ItemDefinition_101:
    ITEM_ID = "item_101"
    NAME = "Hyperion Legendary Artifact #101"
    TYPE = "Weapon" if 101 % 2 == 0 else "Armor"
    RARITY = "Epic" if 101 % 5 == 0 else "Legendary"
    BASE_VALUE = 5050
    ATTACK_BONUS = 303
    DEFENSE_BONUS = 202
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 101."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_101.ITEM_ID, "name": ItemDefinition_101.NAME, "atk": ItemDefinition_101.ATTACK_BONUS, "def": ItemDefinition_101.DEFENSE_BONUS}


class ItemDefinition_102:
    ITEM_ID = "item_102"
    NAME = "Hyperion Legendary Artifact #102"
    TYPE = "Weapon" if 102 % 2 == 0 else "Armor"
    RARITY = "Epic" if 102 % 5 == 0 else "Legendary"
    BASE_VALUE = 5100
    ATTACK_BONUS = 306
    DEFENSE_BONUS = 204
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 102."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_102.ITEM_ID, "name": ItemDefinition_102.NAME, "atk": ItemDefinition_102.ATTACK_BONUS, "def": ItemDefinition_102.DEFENSE_BONUS}


class ItemDefinition_103:
    ITEM_ID = "item_103"
    NAME = "Hyperion Legendary Artifact #103"
    TYPE = "Weapon" if 103 % 2 == 0 else "Armor"
    RARITY = "Epic" if 103 % 5 == 0 else "Legendary"
    BASE_VALUE = 5150
    ATTACK_BONUS = 309
    DEFENSE_BONUS = 206
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 103."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_103.ITEM_ID, "name": ItemDefinition_103.NAME, "atk": ItemDefinition_103.ATTACK_BONUS, "def": ItemDefinition_103.DEFENSE_BONUS}


class ItemDefinition_104:
    ITEM_ID = "item_104"
    NAME = "Hyperion Legendary Artifact #104"
    TYPE = "Weapon" if 104 % 2 == 0 else "Armor"
    RARITY = "Epic" if 104 % 5 == 0 else "Legendary"
    BASE_VALUE = 5200
    ATTACK_BONUS = 312
    DEFENSE_BONUS = 208
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 104."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_104.ITEM_ID, "name": ItemDefinition_104.NAME, "atk": ItemDefinition_104.ATTACK_BONUS, "def": ItemDefinition_104.DEFENSE_BONUS}


class ItemDefinition_105:
    ITEM_ID = "item_105"
    NAME = "Hyperion Legendary Artifact #105"
    TYPE = "Weapon" if 105 % 2 == 0 else "Armor"
    RARITY = "Epic" if 105 % 5 == 0 else "Legendary"
    BASE_VALUE = 5250
    ATTACK_BONUS = 315
    DEFENSE_BONUS = 210
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 105."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_105.ITEM_ID, "name": ItemDefinition_105.NAME, "atk": ItemDefinition_105.ATTACK_BONUS, "def": ItemDefinition_105.DEFENSE_BONUS}


class ItemDefinition_106:
    ITEM_ID = "item_106"
    NAME = "Hyperion Legendary Artifact #106"
    TYPE = "Weapon" if 106 % 2 == 0 else "Armor"
    RARITY = "Epic" if 106 % 5 == 0 else "Legendary"
    BASE_VALUE = 5300
    ATTACK_BONUS = 318
    DEFENSE_BONUS = 212
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 106."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_106.ITEM_ID, "name": ItemDefinition_106.NAME, "atk": ItemDefinition_106.ATTACK_BONUS, "def": ItemDefinition_106.DEFENSE_BONUS}


class ItemDefinition_107:
    ITEM_ID = "item_107"
    NAME = "Hyperion Legendary Artifact #107"
    TYPE = "Weapon" if 107 % 2 == 0 else "Armor"
    RARITY = "Epic" if 107 % 5 == 0 else "Legendary"
    BASE_VALUE = 5350
    ATTACK_BONUS = 321
    DEFENSE_BONUS = 214
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 107."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_107.ITEM_ID, "name": ItemDefinition_107.NAME, "atk": ItemDefinition_107.ATTACK_BONUS, "def": ItemDefinition_107.DEFENSE_BONUS}


class ItemDefinition_108:
    ITEM_ID = "item_108"
    NAME = "Hyperion Legendary Artifact #108"
    TYPE = "Weapon" if 108 % 2 == 0 else "Armor"
    RARITY = "Epic" if 108 % 5 == 0 else "Legendary"
    BASE_VALUE = 5400
    ATTACK_BONUS = 324
    DEFENSE_BONUS = 216
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 108."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_108.ITEM_ID, "name": ItemDefinition_108.NAME, "atk": ItemDefinition_108.ATTACK_BONUS, "def": ItemDefinition_108.DEFENSE_BONUS}


class ItemDefinition_109:
    ITEM_ID = "item_109"
    NAME = "Hyperion Legendary Artifact #109"
    TYPE = "Weapon" if 109 % 2 == 0 else "Armor"
    RARITY = "Epic" if 109 % 5 == 0 else "Legendary"
    BASE_VALUE = 5450
    ATTACK_BONUS = 327
    DEFENSE_BONUS = 218
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 109."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_109.ITEM_ID, "name": ItemDefinition_109.NAME, "atk": ItemDefinition_109.ATTACK_BONUS, "def": ItemDefinition_109.DEFENSE_BONUS}


class ItemDefinition_110:
    ITEM_ID = "item_110"
    NAME = "Hyperion Legendary Artifact #110"
    TYPE = "Weapon" if 110 % 2 == 0 else "Armor"
    RARITY = "Epic" if 110 % 5 == 0 else "Legendary"
    BASE_VALUE = 5500
    ATTACK_BONUS = 330
    DEFENSE_BONUS = 220
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 110."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_110.ITEM_ID, "name": ItemDefinition_110.NAME, "atk": ItemDefinition_110.ATTACK_BONUS, "def": ItemDefinition_110.DEFENSE_BONUS}


class ItemDefinition_111:
    ITEM_ID = "item_111"
    NAME = "Hyperion Legendary Artifact #111"
    TYPE = "Weapon" if 111 % 2 == 0 else "Armor"
    RARITY = "Epic" if 111 % 5 == 0 else "Legendary"
    BASE_VALUE = 5550
    ATTACK_BONUS = 333
    DEFENSE_BONUS = 222
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 111."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_111.ITEM_ID, "name": ItemDefinition_111.NAME, "atk": ItemDefinition_111.ATTACK_BONUS, "def": ItemDefinition_111.DEFENSE_BONUS}


class ItemDefinition_112:
    ITEM_ID = "item_112"
    NAME = "Hyperion Legendary Artifact #112"
    TYPE = "Weapon" if 112 % 2 == 0 else "Armor"
    RARITY = "Epic" if 112 % 5 == 0 else "Legendary"
    BASE_VALUE = 5600
    ATTACK_BONUS = 336
    DEFENSE_BONUS = 224
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 112."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_112.ITEM_ID, "name": ItemDefinition_112.NAME, "atk": ItemDefinition_112.ATTACK_BONUS, "def": ItemDefinition_112.DEFENSE_BONUS}


class ItemDefinition_113:
    ITEM_ID = "item_113"
    NAME = "Hyperion Legendary Artifact #113"
    TYPE = "Weapon" if 113 % 2 == 0 else "Armor"
    RARITY = "Epic" if 113 % 5 == 0 else "Legendary"
    BASE_VALUE = 5650
    ATTACK_BONUS = 339
    DEFENSE_BONUS = 226
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 113."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_113.ITEM_ID, "name": ItemDefinition_113.NAME, "atk": ItemDefinition_113.ATTACK_BONUS, "def": ItemDefinition_113.DEFENSE_BONUS}


class ItemDefinition_114:
    ITEM_ID = "item_114"
    NAME = "Hyperion Legendary Artifact #114"
    TYPE = "Weapon" if 114 % 2 == 0 else "Armor"
    RARITY = "Epic" if 114 % 5 == 0 else "Legendary"
    BASE_VALUE = 5700
    ATTACK_BONUS = 342
    DEFENSE_BONUS = 228
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 114."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_114.ITEM_ID, "name": ItemDefinition_114.NAME, "atk": ItemDefinition_114.ATTACK_BONUS, "def": ItemDefinition_114.DEFENSE_BONUS}


class ItemDefinition_115:
    ITEM_ID = "item_115"
    NAME = "Hyperion Legendary Artifact #115"
    TYPE = "Weapon" if 115 % 2 == 0 else "Armor"
    RARITY = "Epic" if 115 % 5 == 0 else "Legendary"
    BASE_VALUE = 5750
    ATTACK_BONUS = 345
    DEFENSE_BONUS = 230
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 115."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_115.ITEM_ID, "name": ItemDefinition_115.NAME, "atk": ItemDefinition_115.ATTACK_BONUS, "def": ItemDefinition_115.DEFENSE_BONUS}


class ItemDefinition_116:
    ITEM_ID = "item_116"
    NAME = "Hyperion Legendary Artifact #116"
    TYPE = "Weapon" if 116 % 2 == 0 else "Armor"
    RARITY = "Epic" if 116 % 5 == 0 else "Legendary"
    BASE_VALUE = 5800
    ATTACK_BONUS = 348
    DEFENSE_BONUS = 232
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 116."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_116.ITEM_ID, "name": ItemDefinition_116.NAME, "atk": ItemDefinition_116.ATTACK_BONUS, "def": ItemDefinition_116.DEFENSE_BONUS}


class ItemDefinition_117:
    ITEM_ID = "item_117"
    NAME = "Hyperion Legendary Artifact #117"
    TYPE = "Weapon" if 117 % 2 == 0 else "Armor"
    RARITY = "Epic" if 117 % 5 == 0 else "Legendary"
    BASE_VALUE = 5850
    ATTACK_BONUS = 351
    DEFENSE_BONUS = 234
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 117."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_117.ITEM_ID, "name": ItemDefinition_117.NAME, "atk": ItemDefinition_117.ATTACK_BONUS, "def": ItemDefinition_117.DEFENSE_BONUS}


class ItemDefinition_118:
    ITEM_ID = "item_118"
    NAME = "Hyperion Legendary Artifact #118"
    TYPE = "Weapon" if 118 % 2 == 0 else "Armor"
    RARITY = "Epic" if 118 % 5 == 0 else "Legendary"
    BASE_VALUE = 5900
    ATTACK_BONUS = 354
    DEFENSE_BONUS = 236
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 118."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_118.ITEM_ID, "name": ItemDefinition_118.NAME, "atk": ItemDefinition_118.ATTACK_BONUS, "def": ItemDefinition_118.DEFENSE_BONUS}


class ItemDefinition_119:
    ITEM_ID = "item_119"
    NAME = "Hyperion Legendary Artifact #119"
    TYPE = "Weapon" if 119 % 2 == 0 else "Armor"
    RARITY = "Epic" if 119 % 5 == 0 else "Legendary"
    BASE_VALUE = 5950
    ATTACK_BONUS = 357
    DEFENSE_BONUS = 238
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 119."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_119.ITEM_ID, "name": ItemDefinition_119.NAME, "atk": ItemDefinition_119.ATTACK_BONUS, "def": ItemDefinition_119.DEFENSE_BONUS}


class ItemDefinition_120:
    ITEM_ID = "item_120"
    NAME = "Hyperion Legendary Artifact #120"
    TYPE = "Weapon" if 120 % 2 == 0 else "Armor"
    RARITY = "Epic" if 120 % 5 == 0 else "Legendary"
    BASE_VALUE = 6000
    ATTACK_BONUS = 360
    DEFENSE_BONUS = 240
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 120."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_120.ITEM_ID, "name": ItemDefinition_120.NAME, "atk": ItemDefinition_120.ATTACK_BONUS, "def": ItemDefinition_120.DEFENSE_BONUS}


class ItemDefinition_121:
    ITEM_ID = "item_121"
    NAME = "Hyperion Legendary Artifact #121"
    TYPE = "Weapon" if 121 % 2 == 0 else "Armor"
    RARITY = "Epic" if 121 % 5 == 0 else "Legendary"
    BASE_VALUE = 6050
    ATTACK_BONUS = 363
    DEFENSE_BONUS = 242
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 121."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_121.ITEM_ID, "name": ItemDefinition_121.NAME, "atk": ItemDefinition_121.ATTACK_BONUS, "def": ItemDefinition_121.DEFENSE_BONUS}


class ItemDefinition_122:
    ITEM_ID = "item_122"
    NAME = "Hyperion Legendary Artifact #122"
    TYPE = "Weapon" if 122 % 2 == 0 else "Armor"
    RARITY = "Epic" if 122 % 5 == 0 else "Legendary"
    BASE_VALUE = 6100
    ATTACK_BONUS = 366
    DEFENSE_BONUS = 244
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 122."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_122.ITEM_ID, "name": ItemDefinition_122.NAME, "atk": ItemDefinition_122.ATTACK_BONUS, "def": ItemDefinition_122.DEFENSE_BONUS}


class ItemDefinition_123:
    ITEM_ID = "item_123"
    NAME = "Hyperion Legendary Artifact #123"
    TYPE = "Weapon" if 123 % 2 == 0 else "Armor"
    RARITY = "Epic" if 123 % 5 == 0 else "Legendary"
    BASE_VALUE = 6150
    ATTACK_BONUS = 369
    DEFENSE_BONUS = 246
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 123."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_123.ITEM_ID, "name": ItemDefinition_123.NAME, "atk": ItemDefinition_123.ATTACK_BONUS, "def": ItemDefinition_123.DEFENSE_BONUS}


class ItemDefinition_124:
    ITEM_ID = "item_124"
    NAME = "Hyperion Legendary Artifact #124"
    TYPE = "Weapon" if 124 % 2 == 0 else "Armor"
    RARITY = "Epic" if 124 % 5 == 0 else "Legendary"
    BASE_VALUE = 6200
    ATTACK_BONUS = 372
    DEFENSE_BONUS = 248
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 124."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_124.ITEM_ID, "name": ItemDefinition_124.NAME, "atk": ItemDefinition_124.ATTACK_BONUS, "def": ItemDefinition_124.DEFENSE_BONUS}


class ItemDefinition_125:
    ITEM_ID = "item_125"
    NAME = "Hyperion Legendary Artifact #125"
    TYPE = "Weapon" if 125 % 2 == 0 else "Armor"
    RARITY = "Epic" if 125 % 5 == 0 else "Legendary"
    BASE_VALUE = 6250
    ATTACK_BONUS = 375
    DEFENSE_BONUS = 250
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 125."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_125.ITEM_ID, "name": ItemDefinition_125.NAME, "atk": ItemDefinition_125.ATTACK_BONUS, "def": ItemDefinition_125.DEFENSE_BONUS}


class ItemDefinition_126:
    ITEM_ID = "item_126"
    NAME = "Hyperion Legendary Artifact #126"
    TYPE = "Weapon" if 126 % 2 == 0 else "Armor"
    RARITY = "Epic" if 126 % 5 == 0 else "Legendary"
    BASE_VALUE = 6300
    ATTACK_BONUS = 378
    DEFENSE_BONUS = 252
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 126."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_126.ITEM_ID, "name": ItemDefinition_126.NAME, "atk": ItemDefinition_126.ATTACK_BONUS, "def": ItemDefinition_126.DEFENSE_BONUS}


class ItemDefinition_127:
    ITEM_ID = "item_127"
    NAME = "Hyperion Legendary Artifact #127"
    TYPE = "Weapon" if 127 % 2 == 0 else "Armor"
    RARITY = "Epic" if 127 % 5 == 0 else "Legendary"
    BASE_VALUE = 6350
    ATTACK_BONUS = 381
    DEFENSE_BONUS = 254
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 127."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_127.ITEM_ID, "name": ItemDefinition_127.NAME, "atk": ItemDefinition_127.ATTACK_BONUS, "def": ItemDefinition_127.DEFENSE_BONUS}


class ItemDefinition_128:
    ITEM_ID = "item_128"
    NAME = "Hyperion Legendary Artifact #128"
    TYPE = "Weapon" if 128 % 2 == 0 else "Armor"
    RARITY = "Epic" if 128 % 5 == 0 else "Legendary"
    BASE_VALUE = 6400
    ATTACK_BONUS = 384
    DEFENSE_BONUS = 256
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 128."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_128.ITEM_ID, "name": ItemDefinition_128.NAME, "atk": ItemDefinition_128.ATTACK_BONUS, "def": ItemDefinition_128.DEFENSE_BONUS}


class ItemDefinition_129:
    ITEM_ID = "item_129"
    NAME = "Hyperion Legendary Artifact #129"
    TYPE = "Weapon" if 129 % 2 == 0 else "Armor"
    RARITY = "Epic" if 129 % 5 == 0 else "Legendary"
    BASE_VALUE = 6450
    ATTACK_BONUS = 387
    DEFENSE_BONUS = 258
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 129."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_129.ITEM_ID, "name": ItemDefinition_129.NAME, "atk": ItemDefinition_129.ATTACK_BONUS, "def": ItemDefinition_129.DEFENSE_BONUS}


class ItemDefinition_130:
    ITEM_ID = "item_130"
    NAME = "Hyperion Legendary Artifact #130"
    TYPE = "Weapon" if 130 % 2 == 0 else "Armor"
    RARITY = "Epic" if 130 % 5 == 0 else "Legendary"
    BASE_VALUE = 6500
    ATTACK_BONUS = 390
    DEFENSE_BONUS = 260
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 130."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_130.ITEM_ID, "name": ItemDefinition_130.NAME, "atk": ItemDefinition_130.ATTACK_BONUS, "def": ItemDefinition_130.DEFENSE_BONUS}


class ItemDefinition_131:
    ITEM_ID = "item_131"
    NAME = "Hyperion Legendary Artifact #131"
    TYPE = "Weapon" if 131 % 2 == 0 else "Armor"
    RARITY = "Epic" if 131 % 5 == 0 else "Legendary"
    BASE_VALUE = 6550
    ATTACK_BONUS = 393
    DEFENSE_BONUS = 262
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 131."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_131.ITEM_ID, "name": ItemDefinition_131.NAME, "atk": ItemDefinition_131.ATTACK_BONUS, "def": ItemDefinition_131.DEFENSE_BONUS}


class ItemDefinition_132:
    ITEM_ID = "item_132"
    NAME = "Hyperion Legendary Artifact #132"
    TYPE = "Weapon" if 132 % 2 == 0 else "Armor"
    RARITY = "Epic" if 132 % 5 == 0 else "Legendary"
    BASE_VALUE = 6600
    ATTACK_BONUS = 396
    DEFENSE_BONUS = 264
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 132."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_132.ITEM_ID, "name": ItemDefinition_132.NAME, "atk": ItemDefinition_132.ATTACK_BONUS, "def": ItemDefinition_132.DEFENSE_BONUS}


class ItemDefinition_133:
    ITEM_ID = "item_133"
    NAME = "Hyperion Legendary Artifact #133"
    TYPE = "Weapon" if 133 % 2 == 0 else "Armor"
    RARITY = "Epic" if 133 % 5 == 0 else "Legendary"
    BASE_VALUE = 6650
    ATTACK_BONUS = 399
    DEFENSE_BONUS = 266
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 133."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_133.ITEM_ID, "name": ItemDefinition_133.NAME, "atk": ItemDefinition_133.ATTACK_BONUS, "def": ItemDefinition_133.DEFENSE_BONUS}


class ItemDefinition_134:
    ITEM_ID = "item_134"
    NAME = "Hyperion Legendary Artifact #134"
    TYPE = "Weapon" if 134 % 2 == 0 else "Armor"
    RARITY = "Epic" if 134 % 5 == 0 else "Legendary"
    BASE_VALUE = 6700
    ATTACK_BONUS = 402
    DEFENSE_BONUS = 268
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 134."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_134.ITEM_ID, "name": ItemDefinition_134.NAME, "atk": ItemDefinition_134.ATTACK_BONUS, "def": ItemDefinition_134.DEFENSE_BONUS}


class ItemDefinition_135:
    ITEM_ID = "item_135"
    NAME = "Hyperion Legendary Artifact #135"
    TYPE = "Weapon" if 135 % 2 == 0 else "Armor"
    RARITY = "Epic" if 135 % 5 == 0 else "Legendary"
    BASE_VALUE = 6750
    ATTACK_BONUS = 405
    DEFENSE_BONUS = 270
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 135."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_135.ITEM_ID, "name": ItemDefinition_135.NAME, "atk": ItemDefinition_135.ATTACK_BONUS, "def": ItemDefinition_135.DEFENSE_BONUS}


class ItemDefinition_136:
    ITEM_ID = "item_136"
    NAME = "Hyperion Legendary Artifact #136"
    TYPE = "Weapon" if 136 % 2 == 0 else "Armor"
    RARITY = "Epic" if 136 % 5 == 0 else "Legendary"
    BASE_VALUE = 6800
    ATTACK_BONUS = 408
    DEFENSE_BONUS = 272
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 136."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_136.ITEM_ID, "name": ItemDefinition_136.NAME, "atk": ItemDefinition_136.ATTACK_BONUS, "def": ItemDefinition_136.DEFENSE_BONUS}


class ItemDefinition_137:
    ITEM_ID = "item_137"
    NAME = "Hyperion Legendary Artifact #137"
    TYPE = "Weapon" if 137 % 2 == 0 else "Armor"
    RARITY = "Epic" if 137 % 5 == 0 else "Legendary"
    BASE_VALUE = 6850
    ATTACK_BONUS = 411
    DEFENSE_BONUS = 274
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 137."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_137.ITEM_ID, "name": ItemDefinition_137.NAME, "atk": ItemDefinition_137.ATTACK_BONUS, "def": ItemDefinition_137.DEFENSE_BONUS}


class ItemDefinition_138:
    ITEM_ID = "item_138"
    NAME = "Hyperion Legendary Artifact #138"
    TYPE = "Weapon" if 138 % 2 == 0 else "Armor"
    RARITY = "Epic" if 138 % 5 == 0 else "Legendary"
    BASE_VALUE = 6900
    ATTACK_BONUS = 414
    DEFENSE_BONUS = 276
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 138."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_138.ITEM_ID, "name": ItemDefinition_138.NAME, "atk": ItemDefinition_138.ATTACK_BONUS, "def": ItemDefinition_138.DEFENSE_BONUS}


class ItemDefinition_139:
    ITEM_ID = "item_139"
    NAME = "Hyperion Legendary Artifact #139"
    TYPE = "Weapon" if 139 % 2 == 0 else "Armor"
    RARITY = "Epic" if 139 % 5 == 0 else "Legendary"
    BASE_VALUE = 6950
    ATTACK_BONUS = 417
    DEFENSE_BONUS = 278
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 139."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_139.ITEM_ID, "name": ItemDefinition_139.NAME, "atk": ItemDefinition_139.ATTACK_BONUS, "def": ItemDefinition_139.DEFENSE_BONUS}


class ItemDefinition_140:
    ITEM_ID = "item_140"
    NAME = "Hyperion Legendary Artifact #140"
    TYPE = "Weapon" if 140 % 2 == 0 else "Armor"
    RARITY = "Epic" if 140 % 5 == 0 else "Legendary"
    BASE_VALUE = 7000
    ATTACK_BONUS = 420
    DEFENSE_BONUS = 280
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 140."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_140.ITEM_ID, "name": ItemDefinition_140.NAME, "atk": ItemDefinition_140.ATTACK_BONUS, "def": ItemDefinition_140.DEFENSE_BONUS}


class ItemDefinition_141:
    ITEM_ID = "item_141"
    NAME = "Hyperion Legendary Artifact #141"
    TYPE = "Weapon" if 141 % 2 == 0 else "Armor"
    RARITY = "Epic" if 141 % 5 == 0 else "Legendary"
    BASE_VALUE = 7050
    ATTACK_BONUS = 423
    DEFENSE_BONUS = 282
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 141."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_141.ITEM_ID, "name": ItemDefinition_141.NAME, "atk": ItemDefinition_141.ATTACK_BONUS, "def": ItemDefinition_141.DEFENSE_BONUS}


class ItemDefinition_142:
    ITEM_ID = "item_142"
    NAME = "Hyperion Legendary Artifact #142"
    TYPE = "Weapon" if 142 % 2 == 0 else "Armor"
    RARITY = "Epic" if 142 % 5 == 0 else "Legendary"
    BASE_VALUE = 7100
    ATTACK_BONUS = 426
    DEFENSE_BONUS = 284
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 142."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_142.ITEM_ID, "name": ItemDefinition_142.NAME, "atk": ItemDefinition_142.ATTACK_BONUS, "def": ItemDefinition_142.DEFENSE_BONUS}


class ItemDefinition_143:
    ITEM_ID = "item_143"
    NAME = "Hyperion Legendary Artifact #143"
    TYPE = "Weapon" if 143 % 2 == 0 else "Armor"
    RARITY = "Epic" if 143 % 5 == 0 else "Legendary"
    BASE_VALUE = 7150
    ATTACK_BONUS = 429
    DEFENSE_BONUS = 286
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 143."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_143.ITEM_ID, "name": ItemDefinition_143.NAME, "atk": ItemDefinition_143.ATTACK_BONUS, "def": ItemDefinition_143.DEFENSE_BONUS}


class ItemDefinition_144:
    ITEM_ID = "item_144"
    NAME = "Hyperion Legendary Artifact #144"
    TYPE = "Weapon" if 144 % 2 == 0 else "Armor"
    RARITY = "Epic" if 144 % 5 == 0 else "Legendary"
    BASE_VALUE = 7200
    ATTACK_BONUS = 432
    DEFENSE_BONUS = 288
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 144."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_144.ITEM_ID, "name": ItemDefinition_144.NAME, "atk": ItemDefinition_144.ATTACK_BONUS, "def": ItemDefinition_144.DEFENSE_BONUS}


class ItemDefinition_145:
    ITEM_ID = "item_145"
    NAME = "Hyperion Legendary Artifact #145"
    TYPE = "Weapon" if 145 % 2 == 0 else "Armor"
    RARITY = "Epic" if 145 % 5 == 0 else "Legendary"
    BASE_VALUE = 7250
    ATTACK_BONUS = 435
    DEFENSE_BONUS = 290
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 145."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_145.ITEM_ID, "name": ItemDefinition_145.NAME, "atk": ItemDefinition_145.ATTACK_BONUS, "def": ItemDefinition_145.DEFENSE_BONUS}


class ItemDefinition_146:
    ITEM_ID = "item_146"
    NAME = "Hyperion Legendary Artifact #146"
    TYPE = "Weapon" if 146 % 2 == 0 else "Armor"
    RARITY = "Epic" if 146 % 5 == 0 else "Legendary"
    BASE_VALUE = 7300
    ATTACK_BONUS = 438
    DEFENSE_BONUS = 292
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 146."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_146.ITEM_ID, "name": ItemDefinition_146.NAME, "atk": ItemDefinition_146.ATTACK_BONUS, "def": ItemDefinition_146.DEFENSE_BONUS}


class ItemDefinition_147:
    ITEM_ID = "item_147"
    NAME = "Hyperion Legendary Artifact #147"
    TYPE = "Weapon" if 147 % 2 == 0 else "Armor"
    RARITY = "Epic" if 147 % 5 == 0 else "Legendary"
    BASE_VALUE = 7350
    ATTACK_BONUS = 441
    DEFENSE_BONUS = 294
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 147."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_147.ITEM_ID, "name": ItemDefinition_147.NAME, "atk": ItemDefinition_147.ATTACK_BONUS, "def": ItemDefinition_147.DEFENSE_BONUS}


class ItemDefinition_148:
    ITEM_ID = "item_148"
    NAME = "Hyperion Legendary Artifact #148"
    TYPE = "Weapon" if 148 % 2 == 0 else "Armor"
    RARITY = "Epic" if 148 % 5 == 0 else "Legendary"
    BASE_VALUE = 7400
    ATTACK_BONUS = 444
    DEFENSE_BONUS = 296
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 148."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_148.ITEM_ID, "name": ItemDefinition_148.NAME, "atk": ItemDefinition_148.ATTACK_BONUS, "def": ItemDefinition_148.DEFENSE_BONUS}


class ItemDefinition_149:
    ITEM_ID = "item_149"
    NAME = "Hyperion Legendary Artifact #149"
    TYPE = "Weapon" if 149 % 2 == 0 else "Armor"
    RARITY = "Epic" if 149 % 5 == 0 else "Legendary"
    BASE_VALUE = 7450
    ATTACK_BONUS = 447
    DEFENSE_BONUS = 298
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 149."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_149.ITEM_ID, "name": ItemDefinition_149.NAME, "atk": ItemDefinition_149.ATTACK_BONUS, "def": ItemDefinition_149.DEFENSE_BONUS}


class ItemDefinition_150:
    ITEM_ID = "item_150"
    NAME = "Hyperion Legendary Artifact #150"
    TYPE = "Weapon" if 150 % 2 == 0 else "Armor"
    RARITY = "Epic" if 150 % 5 == 0 else "Legendary"
    BASE_VALUE = 7500
    ATTACK_BONUS = 450
    DEFENSE_BONUS = 300
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 150."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_150.ITEM_ID, "name": ItemDefinition_150.NAME, "atk": ItemDefinition_150.ATTACK_BONUS, "def": ItemDefinition_150.DEFENSE_BONUS}


class ItemDefinition_151:
    ITEM_ID = "item_151"
    NAME = "Hyperion Legendary Artifact #151"
    TYPE = "Weapon" if 151 % 2 == 0 else "Armor"
    RARITY = "Epic" if 151 % 5 == 0 else "Legendary"
    BASE_VALUE = 7550
    ATTACK_BONUS = 453
    DEFENSE_BONUS = 302
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 151."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_151.ITEM_ID, "name": ItemDefinition_151.NAME, "atk": ItemDefinition_151.ATTACK_BONUS, "def": ItemDefinition_151.DEFENSE_BONUS}


class ItemDefinition_152:
    ITEM_ID = "item_152"
    NAME = "Hyperion Legendary Artifact #152"
    TYPE = "Weapon" if 152 % 2 == 0 else "Armor"
    RARITY = "Epic" if 152 % 5 == 0 else "Legendary"
    BASE_VALUE = 7600
    ATTACK_BONUS = 456
    DEFENSE_BONUS = 304
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 152."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_152.ITEM_ID, "name": ItemDefinition_152.NAME, "atk": ItemDefinition_152.ATTACK_BONUS, "def": ItemDefinition_152.DEFENSE_BONUS}


class ItemDefinition_153:
    ITEM_ID = "item_153"
    NAME = "Hyperion Legendary Artifact #153"
    TYPE = "Weapon" if 153 % 2 == 0 else "Armor"
    RARITY = "Epic" if 153 % 5 == 0 else "Legendary"
    BASE_VALUE = 7650
    ATTACK_BONUS = 459
    DEFENSE_BONUS = 306
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 153."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_153.ITEM_ID, "name": ItemDefinition_153.NAME, "atk": ItemDefinition_153.ATTACK_BONUS, "def": ItemDefinition_153.DEFENSE_BONUS}


class ItemDefinition_154:
    ITEM_ID = "item_154"
    NAME = "Hyperion Legendary Artifact #154"
    TYPE = "Weapon" if 154 % 2 == 0 else "Armor"
    RARITY = "Epic" if 154 % 5 == 0 else "Legendary"
    BASE_VALUE = 7700
    ATTACK_BONUS = 462
    DEFENSE_BONUS = 308
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 154."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_154.ITEM_ID, "name": ItemDefinition_154.NAME, "atk": ItemDefinition_154.ATTACK_BONUS, "def": ItemDefinition_154.DEFENSE_BONUS}


class ItemDefinition_155:
    ITEM_ID = "item_155"
    NAME = "Hyperion Legendary Artifact #155"
    TYPE = "Weapon" if 155 % 2 == 0 else "Armor"
    RARITY = "Epic" if 155 % 5 == 0 else "Legendary"
    BASE_VALUE = 7750
    ATTACK_BONUS = 465
    DEFENSE_BONUS = 310
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 155."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_155.ITEM_ID, "name": ItemDefinition_155.NAME, "atk": ItemDefinition_155.ATTACK_BONUS, "def": ItemDefinition_155.DEFENSE_BONUS}


class ItemDefinition_156:
    ITEM_ID = "item_156"
    NAME = "Hyperion Legendary Artifact #156"
    TYPE = "Weapon" if 156 % 2 == 0 else "Armor"
    RARITY = "Epic" if 156 % 5 == 0 else "Legendary"
    BASE_VALUE = 7800
    ATTACK_BONUS = 468
    DEFENSE_BONUS = 312
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 156."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_156.ITEM_ID, "name": ItemDefinition_156.NAME, "atk": ItemDefinition_156.ATTACK_BONUS, "def": ItemDefinition_156.DEFENSE_BONUS}


class ItemDefinition_157:
    ITEM_ID = "item_157"
    NAME = "Hyperion Legendary Artifact #157"
    TYPE = "Weapon" if 157 % 2 == 0 else "Armor"
    RARITY = "Epic" if 157 % 5 == 0 else "Legendary"
    BASE_VALUE = 7850
    ATTACK_BONUS = 471
    DEFENSE_BONUS = 314
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 157."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_157.ITEM_ID, "name": ItemDefinition_157.NAME, "atk": ItemDefinition_157.ATTACK_BONUS, "def": ItemDefinition_157.DEFENSE_BONUS}


class ItemDefinition_158:
    ITEM_ID = "item_158"
    NAME = "Hyperion Legendary Artifact #158"
    TYPE = "Weapon" if 158 % 2 == 0 else "Armor"
    RARITY = "Epic" if 158 % 5 == 0 else "Legendary"
    BASE_VALUE = 7900
    ATTACK_BONUS = 474
    DEFENSE_BONUS = 316
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 158."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_158.ITEM_ID, "name": ItemDefinition_158.NAME, "atk": ItemDefinition_158.ATTACK_BONUS, "def": ItemDefinition_158.DEFENSE_BONUS}


class ItemDefinition_159:
    ITEM_ID = "item_159"
    NAME = "Hyperion Legendary Artifact #159"
    TYPE = "Weapon" if 159 % 2 == 0 else "Armor"
    RARITY = "Epic" if 159 % 5 == 0 else "Legendary"
    BASE_VALUE = 7950
    ATTACK_BONUS = 477
    DEFENSE_BONUS = 318
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 159."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_159.ITEM_ID, "name": ItemDefinition_159.NAME, "atk": ItemDefinition_159.ATTACK_BONUS, "def": ItemDefinition_159.DEFENSE_BONUS}


class ItemDefinition_160:
    ITEM_ID = "item_160"
    NAME = "Hyperion Legendary Artifact #160"
    TYPE = "Weapon" if 160 % 2 == 0 else "Armor"
    RARITY = "Epic" if 160 % 5 == 0 else "Legendary"
    BASE_VALUE = 8000
    ATTACK_BONUS = 480
    DEFENSE_BONUS = 320
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 160."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_160.ITEM_ID, "name": ItemDefinition_160.NAME, "atk": ItemDefinition_160.ATTACK_BONUS, "def": ItemDefinition_160.DEFENSE_BONUS}


class ItemDefinition_161:
    ITEM_ID = "item_161"
    NAME = "Hyperion Legendary Artifact #161"
    TYPE = "Weapon" if 161 % 2 == 0 else "Armor"
    RARITY = "Epic" if 161 % 5 == 0 else "Legendary"
    BASE_VALUE = 8050
    ATTACK_BONUS = 483
    DEFENSE_BONUS = 322
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 161."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_161.ITEM_ID, "name": ItemDefinition_161.NAME, "atk": ItemDefinition_161.ATTACK_BONUS, "def": ItemDefinition_161.DEFENSE_BONUS}


class ItemDefinition_162:
    ITEM_ID = "item_162"
    NAME = "Hyperion Legendary Artifact #162"
    TYPE = "Weapon" if 162 % 2 == 0 else "Armor"
    RARITY = "Epic" if 162 % 5 == 0 else "Legendary"
    BASE_VALUE = 8100
    ATTACK_BONUS = 486
    DEFENSE_BONUS = 324
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 162."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_162.ITEM_ID, "name": ItemDefinition_162.NAME, "atk": ItemDefinition_162.ATTACK_BONUS, "def": ItemDefinition_162.DEFENSE_BONUS}


class ItemDefinition_163:
    ITEM_ID = "item_163"
    NAME = "Hyperion Legendary Artifact #163"
    TYPE = "Weapon" if 163 % 2 == 0 else "Armor"
    RARITY = "Epic" if 163 % 5 == 0 else "Legendary"
    BASE_VALUE = 8150
    ATTACK_BONUS = 489
    DEFENSE_BONUS = 326
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 163."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_163.ITEM_ID, "name": ItemDefinition_163.NAME, "atk": ItemDefinition_163.ATTACK_BONUS, "def": ItemDefinition_163.DEFENSE_BONUS}


class ItemDefinition_164:
    ITEM_ID = "item_164"
    NAME = "Hyperion Legendary Artifact #164"
    TYPE = "Weapon" if 164 % 2 == 0 else "Armor"
    RARITY = "Epic" if 164 % 5 == 0 else "Legendary"
    BASE_VALUE = 8200
    ATTACK_BONUS = 492
    DEFENSE_BONUS = 328
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 164."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_164.ITEM_ID, "name": ItemDefinition_164.NAME, "atk": ItemDefinition_164.ATTACK_BONUS, "def": ItemDefinition_164.DEFENSE_BONUS}


class ItemDefinition_165:
    ITEM_ID = "item_165"
    NAME = "Hyperion Legendary Artifact #165"
    TYPE = "Weapon" if 165 % 2 == 0 else "Armor"
    RARITY = "Epic" if 165 % 5 == 0 else "Legendary"
    BASE_VALUE = 8250
    ATTACK_BONUS = 495
    DEFENSE_BONUS = 330
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 165."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_165.ITEM_ID, "name": ItemDefinition_165.NAME, "atk": ItemDefinition_165.ATTACK_BONUS, "def": ItemDefinition_165.DEFENSE_BONUS}


class ItemDefinition_166:
    ITEM_ID = "item_166"
    NAME = "Hyperion Legendary Artifact #166"
    TYPE = "Weapon" if 166 % 2 == 0 else "Armor"
    RARITY = "Epic" if 166 % 5 == 0 else "Legendary"
    BASE_VALUE = 8300
    ATTACK_BONUS = 498
    DEFENSE_BONUS = 332
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 166."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_166.ITEM_ID, "name": ItemDefinition_166.NAME, "atk": ItemDefinition_166.ATTACK_BONUS, "def": ItemDefinition_166.DEFENSE_BONUS}


class ItemDefinition_167:
    ITEM_ID = "item_167"
    NAME = "Hyperion Legendary Artifact #167"
    TYPE = "Weapon" if 167 % 2 == 0 else "Armor"
    RARITY = "Epic" if 167 % 5 == 0 else "Legendary"
    BASE_VALUE = 8350
    ATTACK_BONUS = 501
    DEFENSE_BONUS = 334
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 167."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_167.ITEM_ID, "name": ItemDefinition_167.NAME, "atk": ItemDefinition_167.ATTACK_BONUS, "def": ItemDefinition_167.DEFENSE_BONUS}


class ItemDefinition_168:
    ITEM_ID = "item_168"
    NAME = "Hyperion Legendary Artifact #168"
    TYPE = "Weapon" if 168 % 2 == 0 else "Armor"
    RARITY = "Epic" if 168 % 5 == 0 else "Legendary"
    BASE_VALUE = 8400
    ATTACK_BONUS = 504
    DEFENSE_BONUS = 336
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 168."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_168.ITEM_ID, "name": ItemDefinition_168.NAME, "atk": ItemDefinition_168.ATTACK_BONUS, "def": ItemDefinition_168.DEFENSE_BONUS}


class ItemDefinition_169:
    ITEM_ID = "item_169"
    NAME = "Hyperion Legendary Artifact #169"
    TYPE = "Weapon" if 169 % 2 == 0 else "Armor"
    RARITY = "Epic" if 169 % 5 == 0 else "Legendary"
    BASE_VALUE = 8450
    ATTACK_BONUS = 507
    DEFENSE_BONUS = 338
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 169."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_169.ITEM_ID, "name": ItemDefinition_169.NAME, "atk": ItemDefinition_169.ATTACK_BONUS, "def": ItemDefinition_169.DEFENSE_BONUS}


class ItemDefinition_170:
    ITEM_ID = "item_170"
    NAME = "Hyperion Legendary Artifact #170"
    TYPE = "Weapon" if 170 % 2 == 0 else "Armor"
    RARITY = "Epic" if 170 % 5 == 0 else "Legendary"
    BASE_VALUE = 8500
    ATTACK_BONUS = 510
    DEFENSE_BONUS = 340
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 170."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_170.ITEM_ID, "name": ItemDefinition_170.NAME, "atk": ItemDefinition_170.ATTACK_BONUS, "def": ItemDefinition_170.DEFENSE_BONUS}


class ItemDefinition_171:
    ITEM_ID = "item_171"
    NAME = "Hyperion Legendary Artifact #171"
    TYPE = "Weapon" if 171 % 2 == 0 else "Armor"
    RARITY = "Epic" if 171 % 5 == 0 else "Legendary"
    BASE_VALUE = 8550
    ATTACK_BONUS = 513
    DEFENSE_BONUS = 342
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 171."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_171.ITEM_ID, "name": ItemDefinition_171.NAME, "atk": ItemDefinition_171.ATTACK_BONUS, "def": ItemDefinition_171.DEFENSE_BONUS}


class ItemDefinition_172:
    ITEM_ID = "item_172"
    NAME = "Hyperion Legendary Artifact #172"
    TYPE = "Weapon" if 172 % 2 == 0 else "Armor"
    RARITY = "Epic" if 172 % 5 == 0 else "Legendary"
    BASE_VALUE = 8600
    ATTACK_BONUS = 516
    DEFENSE_BONUS = 344
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 172."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_172.ITEM_ID, "name": ItemDefinition_172.NAME, "atk": ItemDefinition_172.ATTACK_BONUS, "def": ItemDefinition_172.DEFENSE_BONUS}


class ItemDefinition_173:
    ITEM_ID = "item_173"
    NAME = "Hyperion Legendary Artifact #173"
    TYPE = "Weapon" if 173 % 2 == 0 else "Armor"
    RARITY = "Epic" if 173 % 5 == 0 else "Legendary"
    BASE_VALUE = 8650
    ATTACK_BONUS = 519
    DEFENSE_BONUS = 346
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 173."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_173.ITEM_ID, "name": ItemDefinition_173.NAME, "atk": ItemDefinition_173.ATTACK_BONUS, "def": ItemDefinition_173.DEFENSE_BONUS}


class ItemDefinition_174:
    ITEM_ID = "item_174"
    NAME = "Hyperion Legendary Artifact #174"
    TYPE = "Weapon" if 174 % 2 == 0 else "Armor"
    RARITY = "Epic" if 174 % 5 == 0 else "Legendary"
    BASE_VALUE = 8700
    ATTACK_BONUS = 522
    DEFENSE_BONUS = 348
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 174."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_174.ITEM_ID, "name": ItemDefinition_174.NAME, "atk": ItemDefinition_174.ATTACK_BONUS, "def": ItemDefinition_174.DEFENSE_BONUS}


class ItemDefinition_175:
    ITEM_ID = "item_175"
    NAME = "Hyperion Legendary Artifact #175"
    TYPE = "Weapon" if 175 % 2 == 0 else "Armor"
    RARITY = "Epic" if 175 % 5 == 0 else "Legendary"
    BASE_VALUE = 8750
    ATTACK_BONUS = 525
    DEFENSE_BONUS = 350
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 175."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_175.ITEM_ID, "name": ItemDefinition_175.NAME, "atk": ItemDefinition_175.ATTACK_BONUS, "def": ItemDefinition_175.DEFENSE_BONUS}


class ItemDefinition_176:
    ITEM_ID = "item_176"
    NAME = "Hyperion Legendary Artifact #176"
    TYPE = "Weapon" if 176 % 2 == 0 else "Armor"
    RARITY = "Epic" if 176 % 5 == 0 else "Legendary"
    BASE_VALUE = 8800
    ATTACK_BONUS = 528
    DEFENSE_BONUS = 352
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 176."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_176.ITEM_ID, "name": ItemDefinition_176.NAME, "atk": ItemDefinition_176.ATTACK_BONUS, "def": ItemDefinition_176.DEFENSE_BONUS}


class ItemDefinition_177:
    ITEM_ID = "item_177"
    NAME = "Hyperion Legendary Artifact #177"
    TYPE = "Weapon" if 177 % 2 == 0 else "Armor"
    RARITY = "Epic" if 177 % 5 == 0 else "Legendary"
    BASE_VALUE = 8850
    ATTACK_BONUS = 531
    DEFENSE_BONUS = 354
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 177."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_177.ITEM_ID, "name": ItemDefinition_177.NAME, "atk": ItemDefinition_177.ATTACK_BONUS, "def": ItemDefinition_177.DEFENSE_BONUS}


class ItemDefinition_178:
    ITEM_ID = "item_178"
    NAME = "Hyperion Legendary Artifact #178"
    TYPE = "Weapon" if 178 % 2 == 0 else "Armor"
    RARITY = "Epic" if 178 % 5 == 0 else "Legendary"
    BASE_VALUE = 8900
    ATTACK_BONUS = 534
    DEFENSE_BONUS = 356
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 178."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_178.ITEM_ID, "name": ItemDefinition_178.NAME, "atk": ItemDefinition_178.ATTACK_BONUS, "def": ItemDefinition_178.DEFENSE_BONUS}


class ItemDefinition_179:
    ITEM_ID = "item_179"
    NAME = "Hyperion Legendary Artifact #179"
    TYPE = "Weapon" if 179 % 2 == 0 else "Armor"
    RARITY = "Epic" if 179 % 5 == 0 else "Legendary"
    BASE_VALUE = 8950
    ATTACK_BONUS = 537
    DEFENSE_BONUS = 358
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 179."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_179.ITEM_ID, "name": ItemDefinition_179.NAME, "atk": ItemDefinition_179.ATTACK_BONUS, "def": ItemDefinition_179.DEFENSE_BONUS}


class ItemDefinition_180:
    ITEM_ID = "item_180"
    NAME = "Hyperion Legendary Artifact #180"
    TYPE = "Weapon" if 180 % 2 == 0 else "Armor"
    RARITY = "Epic" if 180 % 5 == 0 else "Legendary"
    BASE_VALUE = 9000
    ATTACK_BONUS = 540
    DEFENSE_BONUS = 360
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 180."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_180.ITEM_ID, "name": ItemDefinition_180.NAME, "atk": ItemDefinition_180.ATTACK_BONUS, "def": ItemDefinition_180.DEFENSE_BONUS}


class ItemDefinition_181:
    ITEM_ID = "item_181"
    NAME = "Hyperion Legendary Artifact #181"
    TYPE = "Weapon" if 181 % 2 == 0 else "Armor"
    RARITY = "Epic" if 181 % 5 == 0 else "Legendary"
    BASE_VALUE = 9050
    ATTACK_BONUS = 543
    DEFENSE_BONUS = 362
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 181."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_181.ITEM_ID, "name": ItemDefinition_181.NAME, "atk": ItemDefinition_181.ATTACK_BONUS, "def": ItemDefinition_181.DEFENSE_BONUS}


class ItemDefinition_182:
    ITEM_ID = "item_182"
    NAME = "Hyperion Legendary Artifact #182"
    TYPE = "Weapon" if 182 % 2 == 0 else "Armor"
    RARITY = "Epic" if 182 % 5 == 0 else "Legendary"
    BASE_VALUE = 9100
    ATTACK_BONUS = 546
    DEFENSE_BONUS = 364
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 182."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_182.ITEM_ID, "name": ItemDefinition_182.NAME, "atk": ItemDefinition_182.ATTACK_BONUS, "def": ItemDefinition_182.DEFENSE_BONUS}


class ItemDefinition_183:
    ITEM_ID = "item_183"
    NAME = "Hyperion Legendary Artifact #183"
    TYPE = "Weapon" if 183 % 2 == 0 else "Armor"
    RARITY = "Epic" if 183 % 5 == 0 else "Legendary"
    BASE_VALUE = 9150
    ATTACK_BONUS = 549
    DEFENSE_BONUS = 366
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 183."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_183.ITEM_ID, "name": ItemDefinition_183.NAME, "atk": ItemDefinition_183.ATTACK_BONUS, "def": ItemDefinition_183.DEFENSE_BONUS}


class ItemDefinition_184:
    ITEM_ID = "item_184"
    NAME = "Hyperion Legendary Artifact #184"
    TYPE = "Weapon" if 184 % 2 == 0 else "Armor"
    RARITY = "Epic" if 184 % 5 == 0 else "Legendary"
    BASE_VALUE = 9200
    ATTACK_BONUS = 552
    DEFENSE_BONUS = 368
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 184."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_184.ITEM_ID, "name": ItemDefinition_184.NAME, "atk": ItemDefinition_184.ATTACK_BONUS, "def": ItemDefinition_184.DEFENSE_BONUS}


class ItemDefinition_185:
    ITEM_ID = "item_185"
    NAME = "Hyperion Legendary Artifact #185"
    TYPE = "Weapon" if 185 % 2 == 0 else "Armor"
    RARITY = "Epic" if 185 % 5 == 0 else "Legendary"
    BASE_VALUE = 9250
    ATTACK_BONUS = 555
    DEFENSE_BONUS = 370
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 185."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_185.ITEM_ID, "name": ItemDefinition_185.NAME, "atk": ItemDefinition_185.ATTACK_BONUS, "def": ItemDefinition_185.DEFENSE_BONUS}


class ItemDefinition_186:
    ITEM_ID = "item_186"
    NAME = "Hyperion Legendary Artifact #186"
    TYPE = "Weapon" if 186 % 2 == 0 else "Armor"
    RARITY = "Epic" if 186 % 5 == 0 else "Legendary"
    BASE_VALUE = 9300
    ATTACK_BONUS = 558
    DEFENSE_BONUS = 372
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 186."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_186.ITEM_ID, "name": ItemDefinition_186.NAME, "atk": ItemDefinition_186.ATTACK_BONUS, "def": ItemDefinition_186.DEFENSE_BONUS}


class ItemDefinition_187:
    ITEM_ID = "item_187"
    NAME = "Hyperion Legendary Artifact #187"
    TYPE = "Weapon" if 187 % 2 == 0 else "Armor"
    RARITY = "Epic" if 187 % 5 == 0 else "Legendary"
    BASE_VALUE = 9350
    ATTACK_BONUS = 561
    DEFENSE_BONUS = 374
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 187."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_187.ITEM_ID, "name": ItemDefinition_187.NAME, "atk": ItemDefinition_187.ATTACK_BONUS, "def": ItemDefinition_187.DEFENSE_BONUS}


class ItemDefinition_188:
    ITEM_ID = "item_188"
    NAME = "Hyperion Legendary Artifact #188"
    TYPE = "Weapon" if 188 % 2 == 0 else "Armor"
    RARITY = "Epic" if 188 % 5 == 0 else "Legendary"
    BASE_VALUE = 9400
    ATTACK_BONUS = 564
    DEFENSE_BONUS = 376
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 188."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_188.ITEM_ID, "name": ItemDefinition_188.NAME, "atk": ItemDefinition_188.ATTACK_BONUS, "def": ItemDefinition_188.DEFENSE_BONUS}


class ItemDefinition_189:
    ITEM_ID = "item_189"
    NAME = "Hyperion Legendary Artifact #189"
    TYPE = "Weapon" if 189 % 2 == 0 else "Armor"
    RARITY = "Epic" if 189 % 5 == 0 else "Legendary"
    BASE_VALUE = 9450
    ATTACK_BONUS = 567
    DEFENSE_BONUS = 378
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 189."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_189.ITEM_ID, "name": ItemDefinition_189.NAME, "atk": ItemDefinition_189.ATTACK_BONUS, "def": ItemDefinition_189.DEFENSE_BONUS}


class ItemDefinition_190:
    ITEM_ID = "item_190"
    NAME = "Hyperion Legendary Artifact #190"
    TYPE = "Weapon" if 190 % 2 == 0 else "Armor"
    RARITY = "Epic" if 190 % 5 == 0 else "Legendary"
    BASE_VALUE = 9500
    ATTACK_BONUS = 570
    DEFENSE_BONUS = 380
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 190."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_190.ITEM_ID, "name": ItemDefinition_190.NAME, "atk": ItemDefinition_190.ATTACK_BONUS, "def": ItemDefinition_190.DEFENSE_BONUS}


class ItemDefinition_191:
    ITEM_ID = "item_191"
    NAME = "Hyperion Legendary Artifact #191"
    TYPE = "Weapon" if 191 % 2 == 0 else "Armor"
    RARITY = "Epic" if 191 % 5 == 0 else "Legendary"
    BASE_VALUE = 9550
    ATTACK_BONUS = 573
    DEFENSE_BONUS = 382
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 191."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_191.ITEM_ID, "name": ItemDefinition_191.NAME, "atk": ItemDefinition_191.ATTACK_BONUS, "def": ItemDefinition_191.DEFENSE_BONUS}


class ItemDefinition_192:
    ITEM_ID = "item_192"
    NAME = "Hyperion Legendary Artifact #192"
    TYPE = "Weapon" if 192 % 2 == 0 else "Armor"
    RARITY = "Epic" if 192 % 5 == 0 else "Legendary"
    BASE_VALUE = 9600
    ATTACK_BONUS = 576
    DEFENSE_BONUS = 384
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 192."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_192.ITEM_ID, "name": ItemDefinition_192.NAME, "atk": ItemDefinition_192.ATTACK_BONUS, "def": ItemDefinition_192.DEFENSE_BONUS}


class ItemDefinition_193:
    ITEM_ID = "item_193"
    NAME = "Hyperion Legendary Artifact #193"
    TYPE = "Weapon" if 193 % 2 == 0 else "Armor"
    RARITY = "Epic" if 193 % 5 == 0 else "Legendary"
    BASE_VALUE = 9650
    ATTACK_BONUS = 579
    DEFENSE_BONUS = 386
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 193."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_193.ITEM_ID, "name": ItemDefinition_193.NAME, "atk": ItemDefinition_193.ATTACK_BONUS, "def": ItemDefinition_193.DEFENSE_BONUS}


class ItemDefinition_194:
    ITEM_ID = "item_194"
    NAME = "Hyperion Legendary Artifact #194"
    TYPE = "Weapon" if 194 % 2 == 0 else "Armor"
    RARITY = "Epic" if 194 % 5 == 0 else "Legendary"
    BASE_VALUE = 9700
    ATTACK_BONUS = 582
    DEFENSE_BONUS = 388
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 194."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_194.ITEM_ID, "name": ItemDefinition_194.NAME, "atk": ItemDefinition_194.ATTACK_BONUS, "def": ItemDefinition_194.DEFENSE_BONUS}


class ItemDefinition_195:
    ITEM_ID = "item_195"
    NAME = "Hyperion Legendary Artifact #195"
    TYPE = "Weapon" if 195 % 2 == 0 else "Armor"
    RARITY = "Epic" if 195 % 5 == 0 else "Legendary"
    BASE_VALUE = 9750
    ATTACK_BONUS = 585
    DEFENSE_BONUS = 390
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 195."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_195.ITEM_ID, "name": ItemDefinition_195.NAME, "atk": ItemDefinition_195.ATTACK_BONUS, "def": ItemDefinition_195.DEFENSE_BONUS}


class ItemDefinition_196:
    ITEM_ID = "item_196"
    NAME = "Hyperion Legendary Artifact #196"
    TYPE = "Weapon" if 196 % 2 == 0 else "Armor"
    RARITY = "Epic" if 196 % 5 == 0 else "Legendary"
    BASE_VALUE = 9800
    ATTACK_BONUS = 588
    DEFENSE_BONUS = 392
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 196."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_196.ITEM_ID, "name": ItemDefinition_196.NAME, "atk": ItemDefinition_196.ATTACK_BONUS, "def": ItemDefinition_196.DEFENSE_BONUS}


class ItemDefinition_197:
    ITEM_ID = "item_197"
    NAME = "Hyperion Legendary Artifact #197"
    TYPE = "Weapon" if 197 % 2 == 0 else "Armor"
    RARITY = "Epic" if 197 % 5 == 0 else "Legendary"
    BASE_VALUE = 9850
    ATTACK_BONUS = 591
    DEFENSE_BONUS = 394
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 197."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_197.ITEM_ID, "name": ItemDefinition_197.NAME, "atk": ItemDefinition_197.ATTACK_BONUS, "def": ItemDefinition_197.DEFENSE_BONUS}


class ItemDefinition_198:
    ITEM_ID = "item_198"
    NAME = "Hyperion Legendary Artifact #198"
    TYPE = "Weapon" if 198 % 2 == 0 else "Armor"
    RARITY = "Epic" if 198 % 5 == 0 else "Legendary"
    BASE_VALUE = 9900
    ATTACK_BONUS = 594
    DEFENSE_BONUS = 396
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 198."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_198.ITEM_ID, "name": ItemDefinition_198.NAME, "atk": ItemDefinition_198.ATTACK_BONUS, "def": ItemDefinition_198.DEFENSE_BONUS}


class ItemDefinition_199:
    ITEM_ID = "item_199"
    NAME = "Hyperion Legendary Artifact #199"
    TYPE = "Weapon" if 199 % 2 == 0 else "Armor"
    RARITY = "Epic" if 199 % 5 == 0 else "Legendary"
    BASE_VALUE = 9950
    ATTACK_BONUS = 597
    DEFENSE_BONUS = 398
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 199."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_199.ITEM_ID, "name": ItemDefinition_199.NAME, "atk": ItemDefinition_199.ATTACK_BONUS, "def": ItemDefinition_199.DEFENSE_BONUS}


class ItemDefinition_200:
    ITEM_ID = "item_200"
    NAME = "Hyperion Legendary Artifact #200"
    TYPE = "Weapon" if 200 % 2 == 0 else "Armor"
    RARITY = "Epic" if 200 % 5 == 0 else "Legendary"
    BASE_VALUE = 10000
    ATTACK_BONUS = 600
    DEFENSE_BONUS = 400
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 200."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_200.ITEM_ID, "name": ItemDefinition_200.NAME, "atk": ItemDefinition_200.ATTACK_BONUS, "def": ItemDefinition_200.DEFENSE_BONUS}


class ItemDefinition_201:
    ITEM_ID = "item_201"
    NAME = "Hyperion Legendary Artifact #201"
    TYPE = "Weapon" if 201 % 2 == 0 else "Armor"
    RARITY = "Epic" if 201 % 5 == 0 else "Legendary"
    BASE_VALUE = 10050
    ATTACK_BONUS = 603
    DEFENSE_BONUS = 402
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 201."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_201.ITEM_ID, "name": ItemDefinition_201.NAME, "atk": ItemDefinition_201.ATTACK_BONUS, "def": ItemDefinition_201.DEFENSE_BONUS}


class ItemDefinition_202:
    ITEM_ID = "item_202"
    NAME = "Hyperion Legendary Artifact #202"
    TYPE = "Weapon" if 202 % 2 == 0 else "Armor"
    RARITY = "Epic" if 202 % 5 == 0 else "Legendary"
    BASE_VALUE = 10100
    ATTACK_BONUS = 606
    DEFENSE_BONUS = 404
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 202."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_202.ITEM_ID, "name": ItemDefinition_202.NAME, "atk": ItemDefinition_202.ATTACK_BONUS, "def": ItemDefinition_202.DEFENSE_BONUS}


class ItemDefinition_203:
    ITEM_ID = "item_203"
    NAME = "Hyperion Legendary Artifact #203"
    TYPE = "Weapon" if 203 % 2 == 0 else "Armor"
    RARITY = "Epic" if 203 % 5 == 0 else "Legendary"
    BASE_VALUE = 10150
    ATTACK_BONUS = 609
    DEFENSE_BONUS = 406
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 203."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_203.ITEM_ID, "name": ItemDefinition_203.NAME, "atk": ItemDefinition_203.ATTACK_BONUS, "def": ItemDefinition_203.DEFENSE_BONUS}


class ItemDefinition_204:
    ITEM_ID = "item_204"
    NAME = "Hyperion Legendary Artifact #204"
    TYPE = "Weapon" if 204 % 2 == 0 else "Armor"
    RARITY = "Epic" if 204 % 5 == 0 else "Legendary"
    BASE_VALUE = 10200
    ATTACK_BONUS = 612
    DEFENSE_BONUS = 408
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 204."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_204.ITEM_ID, "name": ItemDefinition_204.NAME, "atk": ItemDefinition_204.ATTACK_BONUS, "def": ItemDefinition_204.DEFENSE_BONUS}


class ItemDefinition_205:
    ITEM_ID = "item_205"
    NAME = "Hyperion Legendary Artifact #205"
    TYPE = "Weapon" if 205 % 2 == 0 else "Armor"
    RARITY = "Epic" if 205 % 5 == 0 else "Legendary"
    BASE_VALUE = 10250
    ATTACK_BONUS = 615
    DEFENSE_BONUS = 410
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 205."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_205.ITEM_ID, "name": ItemDefinition_205.NAME, "atk": ItemDefinition_205.ATTACK_BONUS, "def": ItemDefinition_205.DEFENSE_BONUS}


class ItemDefinition_206:
    ITEM_ID = "item_206"
    NAME = "Hyperion Legendary Artifact #206"
    TYPE = "Weapon" if 206 % 2 == 0 else "Armor"
    RARITY = "Epic" if 206 % 5 == 0 else "Legendary"
    BASE_VALUE = 10300
    ATTACK_BONUS = 618
    DEFENSE_BONUS = 412
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 206."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_206.ITEM_ID, "name": ItemDefinition_206.NAME, "atk": ItemDefinition_206.ATTACK_BONUS, "def": ItemDefinition_206.DEFENSE_BONUS}


class ItemDefinition_207:
    ITEM_ID = "item_207"
    NAME = "Hyperion Legendary Artifact #207"
    TYPE = "Weapon" if 207 % 2 == 0 else "Armor"
    RARITY = "Epic" if 207 % 5 == 0 else "Legendary"
    BASE_VALUE = 10350
    ATTACK_BONUS = 621
    DEFENSE_BONUS = 414
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 207."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_207.ITEM_ID, "name": ItemDefinition_207.NAME, "atk": ItemDefinition_207.ATTACK_BONUS, "def": ItemDefinition_207.DEFENSE_BONUS}


class ItemDefinition_208:
    ITEM_ID = "item_208"
    NAME = "Hyperion Legendary Artifact #208"
    TYPE = "Weapon" if 208 % 2 == 0 else "Armor"
    RARITY = "Epic" if 208 % 5 == 0 else "Legendary"
    BASE_VALUE = 10400
    ATTACK_BONUS = 624
    DEFENSE_BONUS = 416
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 208."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_208.ITEM_ID, "name": ItemDefinition_208.NAME, "atk": ItemDefinition_208.ATTACK_BONUS, "def": ItemDefinition_208.DEFENSE_BONUS}


class ItemDefinition_209:
    ITEM_ID = "item_209"
    NAME = "Hyperion Legendary Artifact #209"
    TYPE = "Weapon" if 209 % 2 == 0 else "Armor"
    RARITY = "Epic" if 209 % 5 == 0 else "Legendary"
    BASE_VALUE = 10450
    ATTACK_BONUS = 627
    DEFENSE_BONUS = 418
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 209."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_209.ITEM_ID, "name": ItemDefinition_209.NAME, "atk": ItemDefinition_209.ATTACK_BONUS, "def": ItemDefinition_209.DEFENSE_BONUS}


class ItemDefinition_210:
    ITEM_ID = "item_210"
    NAME = "Hyperion Legendary Artifact #210"
    TYPE = "Weapon" if 210 % 2 == 0 else "Armor"
    RARITY = "Epic" if 210 % 5 == 0 else "Legendary"
    BASE_VALUE = 10500
    ATTACK_BONUS = 630
    DEFENSE_BONUS = 420
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 210."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_210.ITEM_ID, "name": ItemDefinition_210.NAME, "atk": ItemDefinition_210.ATTACK_BONUS, "def": ItemDefinition_210.DEFENSE_BONUS}


class ItemDefinition_211:
    ITEM_ID = "item_211"
    NAME = "Hyperion Legendary Artifact #211"
    TYPE = "Weapon" if 211 % 2 == 0 else "Armor"
    RARITY = "Epic" if 211 % 5 == 0 else "Legendary"
    BASE_VALUE = 10550
    ATTACK_BONUS = 633
    DEFENSE_BONUS = 422
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 211."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_211.ITEM_ID, "name": ItemDefinition_211.NAME, "atk": ItemDefinition_211.ATTACK_BONUS, "def": ItemDefinition_211.DEFENSE_BONUS}


class ItemDefinition_212:
    ITEM_ID = "item_212"
    NAME = "Hyperion Legendary Artifact #212"
    TYPE = "Weapon" if 212 % 2 == 0 else "Armor"
    RARITY = "Epic" if 212 % 5 == 0 else "Legendary"
    BASE_VALUE = 10600
    ATTACK_BONUS = 636
    DEFENSE_BONUS = 424
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 212."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_212.ITEM_ID, "name": ItemDefinition_212.NAME, "atk": ItemDefinition_212.ATTACK_BONUS, "def": ItemDefinition_212.DEFENSE_BONUS}


class ItemDefinition_213:
    ITEM_ID = "item_213"
    NAME = "Hyperion Legendary Artifact #213"
    TYPE = "Weapon" if 213 % 2 == 0 else "Armor"
    RARITY = "Epic" if 213 % 5 == 0 else "Legendary"
    BASE_VALUE = 10650
    ATTACK_BONUS = 639
    DEFENSE_BONUS = 426
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 213."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_213.ITEM_ID, "name": ItemDefinition_213.NAME, "atk": ItemDefinition_213.ATTACK_BONUS, "def": ItemDefinition_213.DEFENSE_BONUS}


class ItemDefinition_214:
    ITEM_ID = "item_214"
    NAME = "Hyperion Legendary Artifact #214"
    TYPE = "Weapon" if 214 % 2 == 0 else "Armor"
    RARITY = "Epic" if 214 % 5 == 0 else "Legendary"
    BASE_VALUE = 10700
    ATTACK_BONUS = 642
    DEFENSE_BONUS = 428
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 214."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_214.ITEM_ID, "name": ItemDefinition_214.NAME, "atk": ItemDefinition_214.ATTACK_BONUS, "def": ItemDefinition_214.DEFENSE_BONUS}


class ItemDefinition_215:
    ITEM_ID = "item_215"
    NAME = "Hyperion Legendary Artifact #215"
    TYPE = "Weapon" if 215 % 2 == 0 else "Armor"
    RARITY = "Epic" if 215 % 5 == 0 else "Legendary"
    BASE_VALUE = 10750
    ATTACK_BONUS = 645
    DEFENSE_BONUS = 430
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 215."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_215.ITEM_ID, "name": ItemDefinition_215.NAME, "atk": ItemDefinition_215.ATTACK_BONUS, "def": ItemDefinition_215.DEFENSE_BONUS}


class ItemDefinition_216:
    ITEM_ID = "item_216"
    NAME = "Hyperion Legendary Artifact #216"
    TYPE = "Weapon" if 216 % 2 == 0 else "Armor"
    RARITY = "Epic" if 216 % 5 == 0 else "Legendary"
    BASE_VALUE = 10800
    ATTACK_BONUS = 648
    DEFENSE_BONUS = 432
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 216."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_216.ITEM_ID, "name": ItemDefinition_216.NAME, "atk": ItemDefinition_216.ATTACK_BONUS, "def": ItemDefinition_216.DEFENSE_BONUS}


class ItemDefinition_217:
    ITEM_ID = "item_217"
    NAME = "Hyperion Legendary Artifact #217"
    TYPE = "Weapon" if 217 % 2 == 0 else "Armor"
    RARITY = "Epic" if 217 % 5 == 0 else "Legendary"
    BASE_VALUE = 10850
    ATTACK_BONUS = 651
    DEFENSE_BONUS = 434
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 217."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_217.ITEM_ID, "name": ItemDefinition_217.NAME, "atk": ItemDefinition_217.ATTACK_BONUS, "def": ItemDefinition_217.DEFENSE_BONUS}


class ItemDefinition_218:
    ITEM_ID = "item_218"
    NAME = "Hyperion Legendary Artifact #218"
    TYPE = "Weapon" if 218 % 2 == 0 else "Armor"
    RARITY = "Epic" if 218 % 5 == 0 else "Legendary"
    BASE_VALUE = 10900
    ATTACK_BONUS = 654
    DEFENSE_BONUS = 436
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 218."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_218.ITEM_ID, "name": ItemDefinition_218.NAME, "atk": ItemDefinition_218.ATTACK_BONUS, "def": ItemDefinition_218.DEFENSE_BONUS}


class ItemDefinition_219:
    ITEM_ID = "item_219"
    NAME = "Hyperion Legendary Artifact #219"
    TYPE = "Weapon" if 219 % 2 == 0 else "Armor"
    RARITY = "Epic" if 219 % 5 == 0 else "Legendary"
    BASE_VALUE = 10950
    ATTACK_BONUS = 657
    DEFENSE_BONUS = 438
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 219."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_219.ITEM_ID, "name": ItemDefinition_219.NAME, "atk": ItemDefinition_219.ATTACK_BONUS, "def": ItemDefinition_219.DEFENSE_BONUS}


class ItemDefinition_220:
    ITEM_ID = "item_220"
    NAME = "Hyperion Legendary Artifact #220"
    TYPE = "Weapon" if 220 % 2 == 0 else "Armor"
    RARITY = "Epic" if 220 % 5 == 0 else "Legendary"
    BASE_VALUE = 11000
    ATTACK_BONUS = 660
    DEFENSE_BONUS = 440
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 220."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_220.ITEM_ID, "name": ItemDefinition_220.NAME, "atk": ItemDefinition_220.ATTACK_BONUS, "def": ItemDefinition_220.DEFENSE_BONUS}


class ItemDefinition_221:
    ITEM_ID = "item_221"
    NAME = "Hyperion Legendary Artifact #221"
    TYPE = "Weapon" if 221 % 2 == 0 else "Armor"
    RARITY = "Epic" if 221 % 5 == 0 else "Legendary"
    BASE_VALUE = 11050
    ATTACK_BONUS = 663
    DEFENSE_BONUS = 442
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 221."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_221.ITEM_ID, "name": ItemDefinition_221.NAME, "atk": ItemDefinition_221.ATTACK_BONUS, "def": ItemDefinition_221.DEFENSE_BONUS}


class ItemDefinition_222:
    ITEM_ID = "item_222"
    NAME = "Hyperion Legendary Artifact #222"
    TYPE = "Weapon" if 222 % 2 == 0 else "Armor"
    RARITY = "Epic" if 222 % 5 == 0 else "Legendary"
    BASE_VALUE = 11100
    ATTACK_BONUS = 666
    DEFENSE_BONUS = 444
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 222."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_222.ITEM_ID, "name": ItemDefinition_222.NAME, "atk": ItemDefinition_222.ATTACK_BONUS, "def": ItemDefinition_222.DEFENSE_BONUS}


class ItemDefinition_223:
    ITEM_ID = "item_223"
    NAME = "Hyperion Legendary Artifact #223"
    TYPE = "Weapon" if 223 % 2 == 0 else "Armor"
    RARITY = "Epic" if 223 % 5 == 0 else "Legendary"
    BASE_VALUE = 11150
    ATTACK_BONUS = 669
    DEFENSE_BONUS = 446
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 223."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_223.ITEM_ID, "name": ItemDefinition_223.NAME, "atk": ItemDefinition_223.ATTACK_BONUS, "def": ItemDefinition_223.DEFENSE_BONUS}


class ItemDefinition_224:
    ITEM_ID = "item_224"
    NAME = "Hyperion Legendary Artifact #224"
    TYPE = "Weapon" if 224 % 2 == 0 else "Armor"
    RARITY = "Epic" if 224 % 5 == 0 else "Legendary"
    BASE_VALUE = 11200
    ATTACK_BONUS = 672
    DEFENSE_BONUS = 448
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 224."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_224.ITEM_ID, "name": ItemDefinition_224.NAME, "atk": ItemDefinition_224.ATTACK_BONUS, "def": ItemDefinition_224.DEFENSE_BONUS}


class ItemDefinition_225:
    ITEM_ID = "item_225"
    NAME = "Hyperion Legendary Artifact #225"
    TYPE = "Weapon" if 225 % 2 == 0 else "Armor"
    RARITY = "Epic" if 225 % 5 == 0 else "Legendary"
    BASE_VALUE = 11250
    ATTACK_BONUS = 675
    DEFENSE_BONUS = 450
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 225."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_225.ITEM_ID, "name": ItemDefinition_225.NAME, "atk": ItemDefinition_225.ATTACK_BONUS, "def": ItemDefinition_225.DEFENSE_BONUS}


class ItemDefinition_226:
    ITEM_ID = "item_226"
    NAME = "Hyperion Legendary Artifact #226"
    TYPE = "Weapon" if 226 % 2 == 0 else "Armor"
    RARITY = "Epic" if 226 % 5 == 0 else "Legendary"
    BASE_VALUE = 11300
    ATTACK_BONUS = 678
    DEFENSE_BONUS = 452
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 226."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_226.ITEM_ID, "name": ItemDefinition_226.NAME, "atk": ItemDefinition_226.ATTACK_BONUS, "def": ItemDefinition_226.DEFENSE_BONUS}


class ItemDefinition_227:
    ITEM_ID = "item_227"
    NAME = "Hyperion Legendary Artifact #227"
    TYPE = "Weapon" if 227 % 2 == 0 else "Armor"
    RARITY = "Epic" if 227 % 5 == 0 else "Legendary"
    BASE_VALUE = 11350
    ATTACK_BONUS = 681
    DEFENSE_BONUS = 454
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 227."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_227.ITEM_ID, "name": ItemDefinition_227.NAME, "atk": ItemDefinition_227.ATTACK_BONUS, "def": ItemDefinition_227.DEFENSE_BONUS}


class ItemDefinition_228:
    ITEM_ID = "item_228"
    NAME = "Hyperion Legendary Artifact #228"
    TYPE = "Weapon" if 228 % 2 == 0 else "Armor"
    RARITY = "Epic" if 228 % 5 == 0 else "Legendary"
    BASE_VALUE = 11400
    ATTACK_BONUS = 684
    DEFENSE_BONUS = 456
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 228."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_228.ITEM_ID, "name": ItemDefinition_228.NAME, "atk": ItemDefinition_228.ATTACK_BONUS, "def": ItemDefinition_228.DEFENSE_BONUS}


class ItemDefinition_229:
    ITEM_ID = "item_229"
    NAME = "Hyperion Legendary Artifact #229"
    TYPE = "Weapon" if 229 % 2 == 0 else "Armor"
    RARITY = "Epic" if 229 % 5 == 0 else "Legendary"
    BASE_VALUE = 11450
    ATTACK_BONUS = 687
    DEFENSE_BONUS = 458
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 229."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_229.ITEM_ID, "name": ItemDefinition_229.NAME, "atk": ItemDefinition_229.ATTACK_BONUS, "def": ItemDefinition_229.DEFENSE_BONUS}


class ItemDefinition_230:
    ITEM_ID = "item_230"
    NAME = "Hyperion Legendary Artifact #230"
    TYPE = "Weapon" if 230 % 2 == 0 else "Armor"
    RARITY = "Epic" if 230 % 5 == 0 else "Legendary"
    BASE_VALUE = 11500
    ATTACK_BONUS = 690
    DEFENSE_BONUS = 460
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 230."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_230.ITEM_ID, "name": ItemDefinition_230.NAME, "atk": ItemDefinition_230.ATTACK_BONUS, "def": ItemDefinition_230.DEFENSE_BONUS}


class ItemDefinition_231:
    ITEM_ID = "item_231"
    NAME = "Hyperion Legendary Artifact #231"
    TYPE = "Weapon" if 231 % 2 == 0 else "Armor"
    RARITY = "Epic" if 231 % 5 == 0 else "Legendary"
    BASE_VALUE = 11550
    ATTACK_BONUS = 693
    DEFENSE_BONUS = 462
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 231."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_231.ITEM_ID, "name": ItemDefinition_231.NAME, "atk": ItemDefinition_231.ATTACK_BONUS, "def": ItemDefinition_231.DEFENSE_BONUS}


class ItemDefinition_232:
    ITEM_ID = "item_232"
    NAME = "Hyperion Legendary Artifact #232"
    TYPE = "Weapon" if 232 % 2 == 0 else "Armor"
    RARITY = "Epic" if 232 % 5 == 0 else "Legendary"
    BASE_VALUE = 11600
    ATTACK_BONUS = 696
    DEFENSE_BONUS = 464
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 232."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_232.ITEM_ID, "name": ItemDefinition_232.NAME, "atk": ItemDefinition_232.ATTACK_BONUS, "def": ItemDefinition_232.DEFENSE_BONUS}


class ItemDefinition_233:
    ITEM_ID = "item_233"
    NAME = "Hyperion Legendary Artifact #233"
    TYPE = "Weapon" if 233 % 2 == 0 else "Armor"
    RARITY = "Epic" if 233 % 5 == 0 else "Legendary"
    BASE_VALUE = 11650
    ATTACK_BONUS = 699
    DEFENSE_BONUS = 466
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 233."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_233.ITEM_ID, "name": ItemDefinition_233.NAME, "atk": ItemDefinition_233.ATTACK_BONUS, "def": ItemDefinition_233.DEFENSE_BONUS}


class ItemDefinition_234:
    ITEM_ID = "item_234"
    NAME = "Hyperion Legendary Artifact #234"
    TYPE = "Weapon" if 234 % 2 == 0 else "Armor"
    RARITY = "Epic" if 234 % 5 == 0 else "Legendary"
    BASE_VALUE = 11700
    ATTACK_BONUS = 702
    DEFENSE_BONUS = 468
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 234."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_234.ITEM_ID, "name": ItemDefinition_234.NAME, "atk": ItemDefinition_234.ATTACK_BONUS, "def": ItemDefinition_234.DEFENSE_BONUS}


class ItemDefinition_235:
    ITEM_ID = "item_235"
    NAME = "Hyperion Legendary Artifact #235"
    TYPE = "Weapon" if 235 % 2 == 0 else "Armor"
    RARITY = "Epic" if 235 % 5 == 0 else "Legendary"
    BASE_VALUE = 11750
    ATTACK_BONUS = 705
    DEFENSE_BONUS = 470
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 235."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_235.ITEM_ID, "name": ItemDefinition_235.NAME, "atk": ItemDefinition_235.ATTACK_BONUS, "def": ItemDefinition_235.DEFENSE_BONUS}


class ItemDefinition_236:
    ITEM_ID = "item_236"
    NAME = "Hyperion Legendary Artifact #236"
    TYPE = "Weapon" if 236 % 2 == 0 else "Armor"
    RARITY = "Epic" if 236 % 5 == 0 else "Legendary"
    BASE_VALUE = 11800
    ATTACK_BONUS = 708
    DEFENSE_BONUS = 472
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 236."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_236.ITEM_ID, "name": ItemDefinition_236.NAME, "atk": ItemDefinition_236.ATTACK_BONUS, "def": ItemDefinition_236.DEFENSE_BONUS}


class ItemDefinition_237:
    ITEM_ID = "item_237"
    NAME = "Hyperion Legendary Artifact #237"
    TYPE = "Weapon" if 237 % 2 == 0 else "Armor"
    RARITY = "Epic" if 237 % 5 == 0 else "Legendary"
    BASE_VALUE = 11850
    ATTACK_BONUS = 711
    DEFENSE_BONUS = 474
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 237."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_237.ITEM_ID, "name": ItemDefinition_237.NAME, "atk": ItemDefinition_237.ATTACK_BONUS, "def": ItemDefinition_237.DEFENSE_BONUS}


class ItemDefinition_238:
    ITEM_ID = "item_238"
    NAME = "Hyperion Legendary Artifact #238"
    TYPE = "Weapon" if 238 % 2 == 0 else "Armor"
    RARITY = "Epic" if 238 % 5 == 0 else "Legendary"
    BASE_VALUE = 11900
    ATTACK_BONUS = 714
    DEFENSE_BONUS = 476
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 238."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_238.ITEM_ID, "name": ItemDefinition_238.NAME, "atk": ItemDefinition_238.ATTACK_BONUS, "def": ItemDefinition_238.DEFENSE_BONUS}


class ItemDefinition_239:
    ITEM_ID = "item_239"
    NAME = "Hyperion Legendary Artifact #239"
    TYPE = "Weapon" if 239 % 2 == 0 else "Armor"
    RARITY = "Epic" if 239 % 5 == 0 else "Legendary"
    BASE_VALUE = 11950
    ATTACK_BONUS = 717
    DEFENSE_BONUS = 478
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 239."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_239.ITEM_ID, "name": ItemDefinition_239.NAME, "atk": ItemDefinition_239.ATTACK_BONUS, "def": ItemDefinition_239.DEFENSE_BONUS}


class ItemDefinition_240:
    ITEM_ID = "item_240"
    NAME = "Hyperion Legendary Artifact #240"
    TYPE = "Weapon" if 240 % 2 == 0 else "Armor"
    RARITY = "Epic" if 240 % 5 == 0 else "Legendary"
    BASE_VALUE = 12000
    ATTACK_BONUS = 720
    DEFENSE_BONUS = 480
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 240."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_240.ITEM_ID, "name": ItemDefinition_240.NAME, "atk": ItemDefinition_240.ATTACK_BONUS, "def": ItemDefinition_240.DEFENSE_BONUS}


class ItemDefinition_241:
    ITEM_ID = "item_241"
    NAME = "Hyperion Legendary Artifact #241"
    TYPE = "Weapon" if 241 % 2 == 0 else "Armor"
    RARITY = "Epic" if 241 % 5 == 0 else "Legendary"
    BASE_VALUE = 12050
    ATTACK_BONUS = 723
    DEFENSE_BONUS = 482
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 241."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_241.ITEM_ID, "name": ItemDefinition_241.NAME, "atk": ItemDefinition_241.ATTACK_BONUS, "def": ItemDefinition_241.DEFENSE_BONUS}


class ItemDefinition_242:
    ITEM_ID = "item_242"
    NAME = "Hyperion Legendary Artifact #242"
    TYPE = "Weapon" if 242 % 2 == 0 else "Armor"
    RARITY = "Epic" if 242 % 5 == 0 else "Legendary"
    BASE_VALUE = 12100
    ATTACK_BONUS = 726
    DEFENSE_BONUS = 484
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 242."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_242.ITEM_ID, "name": ItemDefinition_242.NAME, "atk": ItemDefinition_242.ATTACK_BONUS, "def": ItemDefinition_242.DEFENSE_BONUS}


class ItemDefinition_243:
    ITEM_ID = "item_243"
    NAME = "Hyperion Legendary Artifact #243"
    TYPE = "Weapon" if 243 % 2 == 0 else "Armor"
    RARITY = "Epic" if 243 % 5 == 0 else "Legendary"
    BASE_VALUE = 12150
    ATTACK_BONUS = 729
    DEFENSE_BONUS = 486
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 243."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_243.ITEM_ID, "name": ItemDefinition_243.NAME, "atk": ItemDefinition_243.ATTACK_BONUS, "def": ItemDefinition_243.DEFENSE_BONUS}


class ItemDefinition_244:
    ITEM_ID = "item_244"
    NAME = "Hyperion Legendary Artifact #244"
    TYPE = "Weapon" if 244 % 2 == 0 else "Armor"
    RARITY = "Epic" if 244 % 5 == 0 else "Legendary"
    BASE_VALUE = 12200
    ATTACK_BONUS = 732
    DEFENSE_BONUS = 488
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 244."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_244.ITEM_ID, "name": ItemDefinition_244.NAME, "atk": ItemDefinition_244.ATTACK_BONUS, "def": ItemDefinition_244.DEFENSE_BONUS}


class ItemDefinition_245:
    ITEM_ID = "item_245"
    NAME = "Hyperion Legendary Artifact #245"
    TYPE = "Weapon" if 245 % 2 == 0 else "Armor"
    RARITY = "Epic" if 245 % 5 == 0 else "Legendary"
    BASE_VALUE = 12250
    ATTACK_BONUS = 735
    DEFENSE_BONUS = 490
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 245."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_245.ITEM_ID, "name": ItemDefinition_245.NAME, "atk": ItemDefinition_245.ATTACK_BONUS, "def": ItemDefinition_245.DEFENSE_BONUS}


class ItemDefinition_246:
    ITEM_ID = "item_246"
    NAME = "Hyperion Legendary Artifact #246"
    TYPE = "Weapon" if 246 % 2 == 0 else "Armor"
    RARITY = "Epic" if 246 % 5 == 0 else "Legendary"
    BASE_VALUE = 12300
    ATTACK_BONUS = 738
    DEFENSE_BONUS = 492
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 246."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_246.ITEM_ID, "name": ItemDefinition_246.NAME, "atk": ItemDefinition_246.ATTACK_BONUS, "def": ItemDefinition_246.DEFENSE_BONUS}


class ItemDefinition_247:
    ITEM_ID = "item_247"
    NAME = "Hyperion Legendary Artifact #247"
    TYPE = "Weapon" if 247 % 2 == 0 else "Armor"
    RARITY = "Epic" if 247 % 5 == 0 else "Legendary"
    BASE_VALUE = 12350
    ATTACK_BONUS = 741
    DEFENSE_BONUS = 494
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 247."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_247.ITEM_ID, "name": ItemDefinition_247.NAME, "atk": ItemDefinition_247.ATTACK_BONUS, "def": ItemDefinition_247.DEFENSE_BONUS}


class ItemDefinition_248:
    ITEM_ID = "item_248"
    NAME = "Hyperion Legendary Artifact #248"
    TYPE = "Weapon" if 248 % 2 == 0 else "Armor"
    RARITY = "Epic" if 248 % 5 == 0 else "Legendary"
    BASE_VALUE = 12400
    ATTACK_BONUS = 744
    DEFENSE_BONUS = 496
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 248."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_248.ITEM_ID, "name": ItemDefinition_248.NAME, "atk": ItemDefinition_248.ATTACK_BONUS, "def": ItemDefinition_248.DEFENSE_BONUS}


class ItemDefinition_249:
    ITEM_ID = "item_249"
    NAME = "Hyperion Legendary Artifact #249"
    TYPE = "Weapon" if 249 % 2 == 0 else "Armor"
    RARITY = "Epic" if 249 % 5 == 0 else "Legendary"
    BASE_VALUE = 12450
    ATTACK_BONUS = 747
    DEFENSE_BONUS = 498
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 249."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_249.ITEM_ID, "name": ItemDefinition_249.NAME, "atk": ItemDefinition_249.ATTACK_BONUS, "def": ItemDefinition_249.DEFENSE_BONUS}


class ItemDefinition_250:
    ITEM_ID = "item_250"
    NAME = "Hyperion Legendary Artifact #250"
    TYPE = "Weapon" if 250 % 2 == 0 else "Armor"
    RARITY = "Epic" if 250 % 5 == 0 else "Legendary"
    BASE_VALUE = 12500
    ATTACK_BONUS = 750
    DEFENSE_BONUS = 500
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 250."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_250.ITEM_ID, "name": ItemDefinition_250.NAME, "atk": ItemDefinition_250.ATTACK_BONUS, "def": ItemDefinition_250.DEFENSE_BONUS}


class ItemDefinition_251:
    ITEM_ID = "item_251"
    NAME = "Hyperion Legendary Artifact #251"
    TYPE = "Weapon" if 251 % 2 == 0 else "Armor"
    RARITY = "Epic" if 251 % 5 == 0 else "Legendary"
    BASE_VALUE = 12550
    ATTACK_BONUS = 753
    DEFENSE_BONUS = 502
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 251."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_251.ITEM_ID, "name": ItemDefinition_251.NAME, "atk": ItemDefinition_251.ATTACK_BONUS, "def": ItemDefinition_251.DEFENSE_BONUS}


class ItemDefinition_252:
    ITEM_ID = "item_252"
    NAME = "Hyperion Legendary Artifact #252"
    TYPE = "Weapon" if 252 % 2 == 0 else "Armor"
    RARITY = "Epic" if 252 % 5 == 0 else "Legendary"
    BASE_VALUE = 12600
    ATTACK_BONUS = 756
    DEFENSE_BONUS = 504
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 252."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_252.ITEM_ID, "name": ItemDefinition_252.NAME, "atk": ItemDefinition_252.ATTACK_BONUS, "def": ItemDefinition_252.DEFENSE_BONUS}


class ItemDefinition_253:
    ITEM_ID = "item_253"
    NAME = "Hyperion Legendary Artifact #253"
    TYPE = "Weapon" if 253 % 2 == 0 else "Armor"
    RARITY = "Epic" if 253 % 5 == 0 else "Legendary"
    BASE_VALUE = 12650
    ATTACK_BONUS = 759
    DEFENSE_BONUS = 506
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 253."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_253.ITEM_ID, "name": ItemDefinition_253.NAME, "atk": ItemDefinition_253.ATTACK_BONUS, "def": ItemDefinition_253.DEFENSE_BONUS}


class ItemDefinition_254:
    ITEM_ID = "item_254"
    NAME = "Hyperion Legendary Artifact #254"
    TYPE = "Weapon" if 254 % 2 == 0 else "Armor"
    RARITY = "Epic" if 254 % 5 == 0 else "Legendary"
    BASE_VALUE = 12700
    ATTACK_BONUS = 762
    DEFENSE_BONUS = 508
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 254."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_254.ITEM_ID, "name": ItemDefinition_254.NAME, "atk": ItemDefinition_254.ATTACK_BONUS, "def": ItemDefinition_254.DEFENSE_BONUS}


class ItemDefinition_255:
    ITEM_ID = "item_255"
    NAME = "Hyperion Legendary Artifact #255"
    TYPE = "Weapon" if 255 % 2 == 0 else "Armor"
    RARITY = "Epic" if 255 % 5 == 0 else "Legendary"
    BASE_VALUE = 12750
    ATTACK_BONUS = 765
    DEFENSE_BONUS = 510
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 255."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_255.ITEM_ID, "name": ItemDefinition_255.NAME, "atk": ItemDefinition_255.ATTACK_BONUS, "def": ItemDefinition_255.DEFENSE_BONUS}


class ItemDefinition_256:
    ITEM_ID = "item_256"
    NAME = "Hyperion Legendary Artifact #256"
    TYPE = "Weapon" if 256 % 2 == 0 else "Armor"
    RARITY = "Epic" if 256 % 5 == 0 else "Legendary"
    BASE_VALUE = 12800
    ATTACK_BONUS = 768
    DEFENSE_BONUS = 512
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 256."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_256.ITEM_ID, "name": ItemDefinition_256.NAME, "atk": ItemDefinition_256.ATTACK_BONUS, "def": ItemDefinition_256.DEFENSE_BONUS}


class ItemDefinition_257:
    ITEM_ID = "item_257"
    NAME = "Hyperion Legendary Artifact #257"
    TYPE = "Weapon" if 257 % 2 == 0 else "Armor"
    RARITY = "Epic" if 257 % 5 == 0 else "Legendary"
    BASE_VALUE = 12850
    ATTACK_BONUS = 771
    DEFENSE_BONUS = 514
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 257."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_257.ITEM_ID, "name": ItemDefinition_257.NAME, "atk": ItemDefinition_257.ATTACK_BONUS, "def": ItemDefinition_257.DEFENSE_BONUS}


class ItemDefinition_258:
    ITEM_ID = "item_258"
    NAME = "Hyperion Legendary Artifact #258"
    TYPE = "Weapon" if 258 % 2 == 0 else "Armor"
    RARITY = "Epic" if 258 % 5 == 0 else "Legendary"
    BASE_VALUE = 12900
    ATTACK_BONUS = 774
    DEFENSE_BONUS = 516
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 258."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_258.ITEM_ID, "name": ItemDefinition_258.NAME, "atk": ItemDefinition_258.ATTACK_BONUS, "def": ItemDefinition_258.DEFENSE_BONUS}


class ItemDefinition_259:
    ITEM_ID = "item_259"
    NAME = "Hyperion Legendary Artifact #259"
    TYPE = "Weapon" if 259 % 2 == 0 else "Armor"
    RARITY = "Epic" if 259 % 5 == 0 else "Legendary"
    BASE_VALUE = 12950
    ATTACK_BONUS = 777
    DEFENSE_BONUS = 518
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 259."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_259.ITEM_ID, "name": ItemDefinition_259.NAME, "atk": ItemDefinition_259.ATTACK_BONUS, "def": ItemDefinition_259.DEFENSE_BONUS}


class ItemDefinition_260:
    ITEM_ID = "item_260"
    NAME = "Hyperion Legendary Artifact #260"
    TYPE = "Weapon" if 260 % 2 == 0 else "Armor"
    RARITY = "Epic" if 260 % 5 == 0 else "Legendary"
    BASE_VALUE = 13000
    ATTACK_BONUS = 780
    DEFENSE_BONUS = 520
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 260."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_260.ITEM_ID, "name": ItemDefinition_260.NAME, "atk": ItemDefinition_260.ATTACK_BONUS, "def": ItemDefinition_260.DEFENSE_BONUS}


class ItemDefinition_261:
    ITEM_ID = "item_261"
    NAME = "Hyperion Legendary Artifact #261"
    TYPE = "Weapon" if 261 % 2 == 0 else "Armor"
    RARITY = "Epic" if 261 % 5 == 0 else "Legendary"
    BASE_VALUE = 13050
    ATTACK_BONUS = 783
    DEFENSE_BONUS = 522
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 261."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_261.ITEM_ID, "name": ItemDefinition_261.NAME, "atk": ItemDefinition_261.ATTACK_BONUS, "def": ItemDefinition_261.DEFENSE_BONUS}


class ItemDefinition_262:
    ITEM_ID = "item_262"
    NAME = "Hyperion Legendary Artifact #262"
    TYPE = "Weapon" if 262 % 2 == 0 else "Armor"
    RARITY = "Epic" if 262 % 5 == 0 else "Legendary"
    BASE_VALUE = 13100
    ATTACK_BONUS = 786
    DEFENSE_BONUS = 524
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 262."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_262.ITEM_ID, "name": ItemDefinition_262.NAME, "atk": ItemDefinition_262.ATTACK_BONUS, "def": ItemDefinition_262.DEFENSE_BONUS}


class ItemDefinition_263:
    ITEM_ID = "item_263"
    NAME = "Hyperion Legendary Artifact #263"
    TYPE = "Weapon" if 263 % 2 == 0 else "Armor"
    RARITY = "Epic" if 263 % 5 == 0 else "Legendary"
    BASE_VALUE = 13150
    ATTACK_BONUS = 789
    DEFENSE_BONUS = 526
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 263."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_263.ITEM_ID, "name": ItemDefinition_263.NAME, "atk": ItemDefinition_263.ATTACK_BONUS, "def": ItemDefinition_263.DEFENSE_BONUS}


class ItemDefinition_264:
    ITEM_ID = "item_264"
    NAME = "Hyperion Legendary Artifact #264"
    TYPE = "Weapon" if 264 % 2 == 0 else "Armor"
    RARITY = "Epic" if 264 % 5 == 0 else "Legendary"
    BASE_VALUE = 13200
    ATTACK_BONUS = 792
    DEFENSE_BONUS = 528
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 264."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_264.ITEM_ID, "name": ItemDefinition_264.NAME, "atk": ItemDefinition_264.ATTACK_BONUS, "def": ItemDefinition_264.DEFENSE_BONUS}


class ItemDefinition_265:
    ITEM_ID = "item_265"
    NAME = "Hyperion Legendary Artifact #265"
    TYPE = "Weapon" if 265 % 2 == 0 else "Armor"
    RARITY = "Epic" if 265 % 5 == 0 else "Legendary"
    BASE_VALUE = 13250
    ATTACK_BONUS = 795
    DEFENSE_BONUS = 530
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 265."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_265.ITEM_ID, "name": ItemDefinition_265.NAME, "atk": ItemDefinition_265.ATTACK_BONUS, "def": ItemDefinition_265.DEFENSE_BONUS}


class ItemDefinition_266:
    ITEM_ID = "item_266"
    NAME = "Hyperion Legendary Artifact #266"
    TYPE = "Weapon" if 266 % 2 == 0 else "Armor"
    RARITY = "Epic" if 266 % 5 == 0 else "Legendary"
    BASE_VALUE = 13300
    ATTACK_BONUS = 798
    DEFENSE_BONUS = 532
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 266."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_266.ITEM_ID, "name": ItemDefinition_266.NAME, "atk": ItemDefinition_266.ATTACK_BONUS, "def": ItemDefinition_266.DEFENSE_BONUS}


class ItemDefinition_267:
    ITEM_ID = "item_267"
    NAME = "Hyperion Legendary Artifact #267"
    TYPE = "Weapon" if 267 % 2 == 0 else "Armor"
    RARITY = "Epic" if 267 % 5 == 0 else "Legendary"
    BASE_VALUE = 13350
    ATTACK_BONUS = 801
    DEFENSE_BONUS = 534
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 267."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_267.ITEM_ID, "name": ItemDefinition_267.NAME, "atk": ItemDefinition_267.ATTACK_BONUS, "def": ItemDefinition_267.DEFENSE_BONUS}


class ItemDefinition_268:
    ITEM_ID = "item_268"
    NAME = "Hyperion Legendary Artifact #268"
    TYPE = "Weapon" if 268 % 2 == 0 else "Armor"
    RARITY = "Epic" if 268 % 5 == 0 else "Legendary"
    BASE_VALUE = 13400
    ATTACK_BONUS = 804
    DEFENSE_BONUS = 536
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 268."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_268.ITEM_ID, "name": ItemDefinition_268.NAME, "atk": ItemDefinition_268.ATTACK_BONUS, "def": ItemDefinition_268.DEFENSE_BONUS}


class ItemDefinition_269:
    ITEM_ID = "item_269"
    NAME = "Hyperion Legendary Artifact #269"
    TYPE = "Weapon" if 269 % 2 == 0 else "Armor"
    RARITY = "Epic" if 269 % 5 == 0 else "Legendary"
    BASE_VALUE = 13450
    ATTACK_BONUS = 807
    DEFENSE_BONUS = 538
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 269."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_269.ITEM_ID, "name": ItemDefinition_269.NAME, "atk": ItemDefinition_269.ATTACK_BONUS, "def": ItemDefinition_269.DEFENSE_BONUS}


class ItemDefinition_270:
    ITEM_ID = "item_270"
    NAME = "Hyperion Legendary Artifact #270"
    TYPE = "Weapon" if 270 % 2 == 0 else "Armor"
    RARITY = "Epic" if 270 % 5 == 0 else "Legendary"
    BASE_VALUE = 13500
    ATTACK_BONUS = 810
    DEFENSE_BONUS = 540
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 270."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_270.ITEM_ID, "name": ItemDefinition_270.NAME, "atk": ItemDefinition_270.ATTACK_BONUS, "def": ItemDefinition_270.DEFENSE_BONUS}


class ItemDefinition_271:
    ITEM_ID = "item_271"
    NAME = "Hyperion Legendary Artifact #271"
    TYPE = "Weapon" if 271 % 2 == 0 else "Armor"
    RARITY = "Epic" if 271 % 5 == 0 else "Legendary"
    BASE_VALUE = 13550
    ATTACK_BONUS = 813
    DEFENSE_BONUS = 542
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 271."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_271.ITEM_ID, "name": ItemDefinition_271.NAME, "atk": ItemDefinition_271.ATTACK_BONUS, "def": ItemDefinition_271.DEFENSE_BONUS}


class ItemDefinition_272:
    ITEM_ID = "item_272"
    NAME = "Hyperion Legendary Artifact #272"
    TYPE = "Weapon" if 272 % 2 == 0 else "Armor"
    RARITY = "Epic" if 272 % 5 == 0 else "Legendary"
    BASE_VALUE = 13600
    ATTACK_BONUS = 816
    DEFENSE_BONUS = 544
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 272."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_272.ITEM_ID, "name": ItemDefinition_272.NAME, "atk": ItemDefinition_272.ATTACK_BONUS, "def": ItemDefinition_272.DEFENSE_BONUS}


class ItemDefinition_273:
    ITEM_ID = "item_273"
    NAME = "Hyperion Legendary Artifact #273"
    TYPE = "Weapon" if 273 % 2 == 0 else "Armor"
    RARITY = "Epic" if 273 % 5 == 0 else "Legendary"
    BASE_VALUE = 13650
    ATTACK_BONUS = 819
    DEFENSE_BONUS = 546
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 273."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_273.ITEM_ID, "name": ItemDefinition_273.NAME, "atk": ItemDefinition_273.ATTACK_BONUS, "def": ItemDefinition_273.DEFENSE_BONUS}


class ItemDefinition_274:
    ITEM_ID = "item_274"
    NAME = "Hyperion Legendary Artifact #274"
    TYPE = "Weapon" if 274 % 2 == 0 else "Armor"
    RARITY = "Epic" if 274 % 5 == 0 else "Legendary"
    BASE_VALUE = 13700
    ATTACK_BONUS = 822
    DEFENSE_BONUS = 548
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 274."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_274.ITEM_ID, "name": ItemDefinition_274.NAME, "atk": ItemDefinition_274.ATTACK_BONUS, "def": ItemDefinition_274.DEFENSE_BONUS}


class ItemDefinition_275:
    ITEM_ID = "item_275"
    NAME = "Hyperion Legendary Artifact #275"
    TYPE = "Weapon" if 275 % 2 == 0 else "Armor"
    RARITY = "Epic" if 275 % 5 == 0 else "Legendary"
    BASE_VALUE = 13750
    ATTACK_BONUS = 825
    DEFENSE_BONUS = 550
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 275."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_275.ITEM_ID, "name": ItemDefinition_275.NAME, "atk": ItemDefinition_275.ATTACK_BONUS, "def": ItemDefinition_275.DEFENSE_BONUS}


class ItemDefinition_276:
    ITEM_ID = "item_276"
    NAME = "Hyperion Legendary Artifact #276"
    TYPE = "Weapon" if 276 % 2 == 0 else "Armor"
    RARITY = "Epic" if 276 % 5 == 0 else "Legendary"
    BASE_VALUE = 13800
    ATTACK_BONUS = 828
    DEFENSE_BONUS = 552
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 276."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_276.ITEM_ID, "name": ItemDefinition_276.NAME, "atk": ItemDefinition_276.ATTACK_BONUS, "def": ItemDefinition_276.DEFENSE_BONUS}


class ItemDefinition_277:
    ITEM_ID = "item_277"
    NAME = "Hyperion Legendary Artifact #277"
    TYPE = "Weapon" if 277 % 2 == 0 else "Armor"
    RARITY = "Epic" if 277 % 5 == 0 else "Legendary"
    BASE_VALUE = 13850
    ATTACK_BONUS = 831
    DEFENSE_BONUS = 554
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 277."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_277.ITEM_ID, "name": ItemDefinition_277.NAME, "atk": ItemDefinition_277.ATTACK_BONUS, "def": ItemDefinition_277.DEFENSE_BONUS}


class ItemDefinition_278:
    ITEM_ID = "item_278"
    NAME = "Hyperion Legendary Artifact #278"
    TYPE = "Weapon" if 278 % 2 == 0 else "Armor"
    RARITY = "Epic" if 278 % 5 == 0 else "Legendary"
    BASE_VALUE = 13900
    ATTACK_BONUS = 834
    DEFENSE_BONUS = 556
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 278."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_278.ITEM_ID, "name": ItemDefinition_278.NAME, "atk": ItemDefinition_278.ATTACK_BONUS, "def": ItemDefinition_278.DEFENSE_BONUS}


class ItemDefinition_279:
    ITEM_ID = "item_279"
    NAME = "Hyperion Legendary Artifact #279"
    TYPE = "Weapon" if 279 % 2 == 0 else "Armor"
    RARITY = "Epic" if 279 % 5 == 0 else "Legendary"
    BASE_VALUE = 13950
    ATTACK_BONUS = 837
    DEFENSE_BONUS = 558
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 279."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_279.ITEM_ID, "name": ItemDefinition_279.NAME, "atk": ItemDefinition_279.ATTACK_BONUS, "def": ItemDefinition_279.DEFENSE_BONUS}


class ItemDefinition_280:
    ITEM_ID = "item_280"
    NAME = "Hyperion Legendary Artifact #280"
    TYPE = "Weapon" if 280 % 2 == 0 else "Armor"
    RARITY = "Epic" if 280 % 5 == 0 else "Legendary"
    BASE_VALUE = 14000
    ATTACK_BONUS = 840
    DEFENSE_BONUS = 560
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 280."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_280.ITEM_ID, "name": ItemDefinition_280.NAME, "atk": ItemDefinition_280.ATTACK_BONUS, "def": ItemDefinition_280.DEFENSE_BONUS}


class ItemDefinition_281:
    ITEM_ID = "item_281"
    NAME = "Hyperion Legendary Artifact #281"
    TYPE = "Weapon" if 281 % 2 == 0 else "Armor"
    RARITY = "Epic" if 281 % 5 == 0 else "Legendary"
    BASE_VALUE = 14050
    ATTACK_BONUS = 843
    DEFENSE_BONUS = 562
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 281."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_281.ITEM_ID, "name": ItemDefinition_281.NAME, "atk": ItemDefinition_281.ATTACK_BONUS, "def": ItemDefinition_281.DEFENSE_BONUS}


class ItemDefinition_282:
    ITEM_ID = "item_282"
    NAME = "Hyperion Legendary Artifact #282"
    TYPE = "Weapon" if 282 % 2 == 0 else "Armor"
    RARITY = "Epic" if 282 % 5 == 0 else "Legendary"
    BASE_VALUE = 14100
    ATTACK_BONUS = 846
    DEFENSE_BONUS = 564
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 282."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_282.ITEM_ID, "name": ItemDefinition_282.NAME, "atk": ItemDefinition_282.ATTACK_BONUS, "def": ItemDefinition_282.DEFENSE_BONUS}


class ItemDefinition_283:
    ITEM_ID = "item_283"
    NAME = "Hyperion Legendary Artifact #283"
    TYPE = "Weapon" if 283 % 2 == 0 else "Armor"
    RARITY = "Epic" if 283 % 5 == 0 else "Legendary"
    BASE_VALUE = 14150
    ATTACK_BONUS = 849
    DEFENSE_BONUS = 566
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 283."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_283.ITEM_ID, "name": ItemDefinition_283.NAME, "atk": ItemDefinition_283.ATTACK_BONUS, "def": ItemDefinition_283.DEFENSE_BONUS}


class ItemDefinition_284:
    ITEM_ID = "item_284"
    NAME = "Hyperion Legendary Artifact #284"
    TYPE = "Weapon" if 284 % 2 == 0 else "Armor"
    RARITY = "Epic" if 284 % 5 == 0 else "Legendary"
    BASE_VALUE = 14200
    ATTACK_BONUS = 852
    DEFENSE_BONUS = 568
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 284."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_284.ITEM_ID, "name": ItemDefinition_284.NAME, "atk": ItemDefinition_284.ATTACK_BONUS, "def": ItemDefinition_284.DEFENSE_BONUS}


class ItemDefinition_285:
    ITEM_ID = "item_285"
    NAME = "Hyperion Legendary Artifact #285"
    TYPE = "Weapon" if 285 % 2 == 0 else "Armor"
    RARITY = "Epic" if 285 % 5 == 0 else "Legendary"
    BASE_VALUE = 14250
    ATTACK_BONUS = 855
    DEFENSE_BONUS = 570
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 285."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_285.ITEM_ID, "name": ItemDefinition_285.NAME, "atk": ItemDefinition_285.ATTACK_BONUS, "def": ItemDefinition_285.DEFENSE_BONUS}


class ItemDefinition_286:
    ITEM_ID = "item_286"
    NAME = "Hyperion Legendary Artifact #286"
    TYPE = "Weapon" if 286 % 2 == 0 else "Armor"
    RARITY = "Epic" if 286 % 5 == 0 else "Legendary"
    BASE_VALUE = 14300
    ATTACK_BONUS = 858
    DEFENSE_BONUS = 572
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 286."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_286.ITEM_ID, "name": ItemDefinition_286.NAME, "atk": ItemDefinition_286.ATTACK_BONUS, "def": ItemDefinition_286.DEFENSE_BONUS}


class ItemDefinition_287:
    ITEM_ID = "item_287"
    NAME = "Hyperion Legendary Artifact #287"
    TYPE = "Weapon" if 287 % 2 == 0 else "Armor"
    RARITY = "Epic" if 287 % 5 == 0 else "Legendary"
    BASE_VALUE = 14350
    ATTACK_BONUS = 861
    DEFENSE_BONUS = 574
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 287."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_287.ITEM_ID, "name": ItemDefinition_287.NAME, "atk": ItemDefinition_287.ATTACK_BONUS, "def": ItemDefinition_287.DEFENSE_BONUS}


class ItemDefinition_288:
    ITEM_ID = "item_288"
    NAME = "Hyperion Legendary Artifact #288"
    TYPE = "Weapon" if 288 % 2 == 0 else "Armor"
    RARITY = "Epic" if 288 % 5 == 0 else "Legendary"
    BASE_VALUE = 14400
    ATTACK_BONUS = 864
    DEFENSE_BONUS = 576
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 288."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_288.ITEM_ID, "name": ItemDefinition_288.NAME, "atk": ItemDefinition_288.ATTACK_BONUS, "def": ItemDefinition_288.DEFENSE_BONUS}


class ItemDefinition_289:
    ITEM_ID = "item_289"
    NAME = "Hyperion Legendary Artifact #289"
    TYPE = "Weapon" if 289 % 2 == 0 else "Armor"
    RARITY = "Epic" if 289 % 5 == 0 else "Legendary"
    BASE_VALUE = 14450
    ATTACK_BONUS = 867
    DEFENSE_BONUS = 578
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 289."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_289.ITEM_ID, "name": ItemDefinition_289.NAME, "atk": ItemDefinition_289.ATTACK_BONUS, "def": ItemDefinition_289.DEFENSE_BONUS}


class ItemDefinition_290:
    ITEM_ID = "item_290"
    NAME = "Hyperion Legendary Artifact #290"
    TYPE = "Weapon" if 290 % 2 == 0 else "Armor"
    RARITY = "Epic" if 290 % 5 == 0 else "Legendary"
    BASE_VALUE = 14500
    ATTACK_BONUS = 870
    DEFENSE_BONUS = 580
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 290."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_290.ITEM_ID, "name": ItemDefinition_290.NAME, "atk": ItemDefinition_290.ATTACK_BONUS, "def": ItemDefinition_290.DEFENSE_BONUS}


class ItemDefinition_291:
    ITEM_ID = "item_291"
    NAME = "Hyperion Legendary Artifact #291"
    TYPE = "Weapon" if 291 % 2 == 0 else "Armor"
    RARITY = "Epic" if 291 % 5 == 0 else "Legendary"
    BASE_VALUE = 14550
    ATTACK_BONUS = 873
    DEFENSE_BONUS = 582
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 291."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_291.ITEM_ID, "name": ItemDefinition_291.NAME, "atk": ItemDefinition_291.ATTACK_BONUS, "def": ItemDefinition_291.DEFENSE_BONUS}


class ItemDefinition_292:
    ITEM_ID = "item_292"
    NAME = "Hyperion Legendary Artifact #292"
    TYPE = "Weapon" if 292 % 2 == 0 else "Armor"
    RARITY = "Epic" if 292 % 5 == 0 else "Legendary"
    BASE_VALUE = 14600
    ATTACK_BONUS = 876
    DEFENSE_BONUS = 584
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 292."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_292.ITEM_ID, "name": ItemDefinition_292.NAME, "atk": ItemDefinition_292.ATTACK_BONUS, "def": ItemDefinition_292.DEFENSE_BONUS}


class ItemDefinition_293:
    ITEM_ID = "item_293"
    NAME = "Hyperion Legendary Artifact #293"
    TYPE = "Weapon" if 293 % 2 == 0 else "Armor"
    RARITY = "Epic" if 293 % 5 == 0 else "Legendary"
    BASE_VALUE = 14650
    ATTACK_BONUS = 879
    DEFENSE_BONUS = 586
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 293."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_293.ITEM_ID, "name": ItemDefinition_293.NAME, "atk": ItemDefinition_293.ATTACK_BONUS, "def": ItemDefinition_293.DEFENSE_BONUS}


class ItemDefinition_294:
    ITEM_ID = "item_294"
    NAME = "Hyperion Legendary Artifact #294"
    TYPE = "Weapon" if 294 % 2 == 0 else "Armor"
    RARITY = "Epic" if 294 % 5 == 0 else "Legendary"
    BASE_VALUE = 14700
    ATTACK_BONUS = 882
    DEFENSE_BONUS = 588
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 294."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_294.ITEM_ID, "name": ItemDefinition_294.NAME, "atk": ItemDefinition_294.ATTACK_BONUS, "def": ItemDefinition_294.DEFENSE_BONUS}


class ItemDefinition_295:
    ITEM_ID = "item_295"
    NAME = "Hyperion Legendary Artifact #295"
    TYPE = "Weapon" if 295 % 2 == 0 else "Armor"
    RARITY = "Epic" if 295 % 5 == 0 else "Legendary"
    BASE_VALUE = 14750
    ATTACK_BONUS = 885
    DEFENSE_BONUS = 590
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 295."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_295.ITEM_ID, "name": ItemDefinition_295.NAME, "atk": ItemDefinition_295.ATTACK_BONUS, "def": ItemDefinition_295.DEFENSE_BONUS}


class ItemDefinition_296:
    ITEM_ID = "item_296"
    NAME = "Hyperion Legendary Artifact #296"
    TYPE = "Weapon" if 296 % 2 == 0 else "Armor"
    RARITY = "Epic" if 296 % 5 == 0 else "Legendary"
    BASE_VALUE = 14800
    ATTACK_BONUS = 888
    DEFENSE_BONUS = 592
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 296."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_296.ITEM_ID, "name": ItemDefinition_296.NAME, "atk": ItemDefinition_296.ATTACK_BONUS, "def": ItemDefinition_296.DEFENSE_BONUS}


class ItemDefinition_297:
    ITEM_ID = "item_297"
    NAME = "Hyperion Legendary Artifact #297"
    TYPE = "Weapon" if 297 % 2 == 0 else "Armor"
    RARITY = "Epic" if 297 % 5 == 0 else "Legendary"
    BASE_VALUE = 14850
    ATTACK_BONUS = 891
    DEFENSE_BONUS = 594
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 297."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_297.ITEM_ID, "name": ItemDefinition_297.NAME, "atk": ItemDefinition_297.ATTACK_BONUS, "def": ItemDefinition_297.DEFENSE_BONUS}


class ItemDefinition_298:
    ITEM_ID = "item_298"
    NAME = "Hyperion Legendary Artifact #298"
    TYPE = "Weapon" if 298 % 2 == 0 else "Armor"
    RARITY = "Epic" if 298 % 5 == 0 else "Legendary"
    BASE_VALUE = 14900
    ATTACK_BONUS = 894
    DEFENSE_BONUS = 596
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 298."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_298.ITEM_ID, "name": ItemDefinition_298.NAME, "atk": ItemDefinition_298.ATTACK_BONUS, "def": ItemDefinition_298.DEFENSE_BONUS}


class ItemDefinition_299:
    ITEM_ID = "item_299"
    NAME = "Hyperion Legendary Artifact #299"
    TYPE = "Weapon" if 299 % 2 == 0 else "Armor"
    RARITY = "Epic" if 299 % 5 == 0 else "Legendary"
    BASE_VALUE = 14950
    ATTACK_BONUS = 897
    DEFENSE_BONUS = 598
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 299."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_299.ITEM_ID, "name": ItemDefinition_299.NAME, "atk": ItemDefinition_299.ATTACK_BONUS, "def": ItemDefinition_299.DEFENSE_BONUS}


class ItemDefinition_300:
    ITEM_ID = "item_300"
    NAME = "Hyperion Legendary Artifact #300"
    TYPE = "Weapon" if 300 % 2 == 0 else "Armor"
    RARITY = "Epic" if 300 % 5 == 0 else "Legendary"
    BASE_VALUE = 15000
    ATTACK_BONUS = 900
    DEFENSE_BONUS = 600
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 300."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_300.ITEM_ID, "name": ItemDefinition_300.NAME, "atk": ItemDefinition_300.ATTACK_BONUS, "def": ItemDefinition_300.DEFENSE_BONUS}


class ItemDefinition_301:
    ITEM_ID = "item_301"
    NAME = "Hyperion Legendary Artifact #301"
    TYPE = "Weapon" if 301 % 2 == 0 else "Armor"
    RARITY = "Epic" if 301 % 5 == 0 else "Legendary"
    BASE_VALUE = 15050
    ATTACK_BONUS = 903
    DEFENSE_BONUS = 602
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 301."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_301.ITEM_ID, "name": ItemDefinition_301.NAME, "atk": ItemDefinition_301.ATTACK_BONUS, "def": ItemDefinition_301.DEFENSE_BONUS}


class ItemDefinition_302:
    ITEM_ID = "item_302"
    NAME = "Hyperion Legendary Artifact #302"
    TYPE = "Weapon" if 302 % 2 == 0 else "Armor"
    RARITY = "Epic" if 302 % 5 == 0 else "Legendary"
    BASE_VALUE = 15100
    ATTACK_BONUS = 906
    DEFENSE_BONUS = 604
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 302."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_302.ITEM_ID, "name": ItemDefinition_302.NAME, "atk": ItemDefinition_302.ATTACK_BONUS, "def": ItemDefinition_302.DEFENSE_BONUS}


class ItemDefinition_303:
    ITEM_ID = "item_303"
    NAME = "Hyperion Legendary Artifact #303"
    TYPE = "Weapon" if 303 % 2 == 0 else "Armor"
    RARITY = "Epic" if 303 % 5 == 0 else "Legendary"
    BASE_VALUE = 15150
    ATTACK_BONUS = 909
    DEFENSE_BONUS = 606
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 303."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_303.ITEM_ID, "name": ItemDefinition_303.NAME, "atk": ItemDefinition_303.ATTACK_BONUS, "def": ItemDefinition_303.DEFENSE_BONUS}


class ItemDefinition_304:
    ITEM_ID = "item_304"
    NAME = "Hyperion Legendary Artifact #304"
    TYPE = "Weapon" if 304 % 2 == 0 else "Armor"
    RARITY = "Epic" if 304 % 5 == 0 else "Legendary"
    BASE_VALUE = 15200
    ATTACK_BONUS = 912
    DEFENSE_BONUS = 608
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 304."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_304.ITEM_ID, "name": ItemDefinition_304.NAME, "atk": ItemDefinition_304.ATTACK_BONUS, "def": ItemDefinition_304.DEFENSE_BONUS}


class ItemDefinition_305:
    ITEM_ID = "item_305"
    NAME = "Hyperion Legendary Artifact #305"
    TYPE = "Weapon" if 305 % 2 == 0 else "Armor"
    RARITY = "Epic" if 305 % 5 == 0 else "Legendary"
    BASE_VALUE = 15250
    ATTACK_BONUS = 915
    DEFENSE_BONUS = 610
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 305."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_305.ITEM_ID, "name": ItemDefinition_305.NAME, "atk": ItemDefinition_305.ATTACK_BONUS, "def": ItemDefinition_305.DEFENSE_BONUS}


class ItemDefinition_306:
    ITEM_ID = "item_306"
    NAME = "Hyperion Legendary Artifact #306"
    TYPE = "Weapon" if 306 % 2 == 0 else "Armor"
    RARITY = "Epic" if 306 % 5 == 0 else "Legendary"
    BASE_VALUE = 15300
    ATTACK_BONUS = 918
    DEFENSE_BONUS = 612
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 306."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_306.ITEM_ID, "name": ItemDefinition_306.NAME, "atk": ItemDefinition_306.ATTACK_BONUS, "def": ItemDefinition_306.DEFENSE_BONUS}


class ItemDefinition_307:
    ITEM_ID = "item_307"
    NAME = "Hyperion Legendary Artifact #307"
    TYPE = "Weapon" if 307 % 2 == 0 else "Armor"
    RARITY = "Epic" if 307 % 5 == 0 else "Legendary"
    BASE_VALUE = 15350
    ATTACK_BONUS = 921
    DEFENSE_BONUS = 614
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 307."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_307.ITEM_ID, "name": ItemDefinition_307.NAME, "atk": ItemDefinition_307.ATTACK_BONUS, "def": ItemDefinition_307.DEFENSE_BONUS}


class ItemDefinition_308:
    ITEM_ID = "item_308"
    NAME = "Hyperion Legendary Artifact #308"
    TYPE = "Weapon" if 308 % 2 == 0 else "Armor"
    RARITY = "Epic" if 308 % 5 == 0 else "Legendary"
    BASE_VALUE = 15400
    ATTACK_BONUS = 924
    DEFENSE_BONUS = 616
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 308."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_308.ITEM_ID, "name": ItemDefinition_308.NAME, "atk": ItemDefinition_308.ATTACK_BONUS, "def": ItemDefinition_308.DEFENSE_BONUS}


class ItemDefinition_309:
    ITEM_ID = "item_309"
    NAME = "Hyperion Legendary Artifact #309"
    TYPE = "Weapon" if 309 % 2 == 0 else "Armor"
    RARITY = "Epic" if 309 % 5 == 0 else "Legendary"
    BASE_VALUE = 15450
    ATTACK_BONUS = 927
    DEFENSE_BONUS = 618
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 309."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_309.ITEM_ID, "name": ItemDefinition_309.NAME, "atk": ItemDefinition_309.ATTACK_BONUS, "def": ItemDefinition_309.DEFENSE_BONUS}


class ItemDefinition_310:
    ITEM_ID = "item_310"
    NAME = "Hyperion Legendary Artifact #310"
    TYPE = "Weapon" if 310 % 2 == 0 else "Armor"
    RARITY = "Epic" if 310 % 5 == 0 else "Legendary"
    BASE_VALUE = 15500
    ATTACK_BONUS = 930
    DEFENSE_BONUS = 620
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 310."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_310.ITEM_ID, "name": ItemDefinition_310.NAME, "atk": ItemDefinition_310.ATTACK_BONUS, "def": ItemDefinition_310.DEFENSE_BONUS}


class ItemDefinition_311:
    ITEM_ID = "item_311"
    NAME = "Hyperion Legendary Artifact #311"
    TYPE = "Weapon" if 311 % 2 == 0 else "Armor"
    RARITY = "Epic" if 311 % 5 == 0 else "Legendary"
    BASE_VALUE = 15550
    ATTACK_BONUS = 933
    DEFENSE_BONUS = 622
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 311."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_311.ITEM_ID, "name": ItemDefinition_311.NAME, "atk": ItemDefinition_311.ATTACK_BONUS, "def": ItemDefinition_311.DEFENSE_BONUS}


class ItemDefinition_312:
    ITEM_ID = "item_312"
    NAME = "Hyperion Legendary Artifact #312"
    TYPE = "Weapon" if 312 % 2 == 0 else "Armor"
    RARITY = "Epic" if 312 % 5 == 0 else "Legendary"
    BASE_VALUE = 15600
    ATTACK_BONUS = 936
    DEFENSE_BONUS = 624
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 312."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_312.ITEM_ID, "name": ItemDefinition_312.NAME, "atk": ItemDefinition_312.ATTACK_BONUS, "def": ItemDefinition_312.DEFENSE_BONUS}


class ItemDefinition_313:
    ITEM_ID = "item_313"
    NAME = "Hyperion Legendary Artifact #313"
    TYPE = "Weapon" if 313 % 2 == 0 else "Armor"
    RARITY = "Epic" if 313 % 5 == 0 else "Legendary"
    BASE_VALUE = 15650
    ATTACK_BONUS = 939
    DEFENSE_BONUS = 626
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 313."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_313.ITEM_ID, "name": ItemDefinition_313.NAME, "atk": ItemDefinition_313.ATTACK_BONUS, "def": ItemDefinition_313.DEFENSE_BONUS}


class ItemDefinition_314:
    ITEM_ID = "item_314"
    NAME = "Hyperion Legendary Artifact #314"
    TYPE = "Weapon" if 314 % 2 == 0 else "Armor"
    RARITY = "Epic" if 314 % 5 == 0 else "Legendary"
    BASE_VALUE = 15700
    ATTACK_BONUS = 942
    DEFENSE_BONUS = 628
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 314."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_314.ITEM_ID, "name": ItemDefinition_314.NAME, "atk": ItemDefinition_314.ATTACK_BONUS, "def": ItemDefinition_314.DEFENSE_BONUS}


class ItemDefinition_315:
    ITEM_ID = "item_315"
    NAME = "Hyperion Legendary Artifact #315"
    TYPE = "Weapon" if 315 % 2 == 0 else "Armor"
    RARITY = "Epic" if 315 % 5 == 0 else "Legendary"
    BASE_VALUE = 15750
    ATTACK_BONUS = 945
    DEFENSE_BONUS = 630
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 315."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_315.ITEM_ID, "name": ItemDefinition_315.NAME, "atk": ItemDefinition_315.ATTACK_BONUS, "def": ItemDefinition_315.DEFENSE_BONUS}


class ItemDefinition_316:
    ITEM_ID = "item_316"
    NAME = "Hyperion Legendary Artifact #316"
    TYPE = "Weapon" if 316 % 2 == 0 else "Armor"
    RARITY = "Epic" if 316 % 5 == 0 else "Legendary"
    BASE_VALUE = 15800
    ATTACK_BONUS = 948
    DEFENSE_BONUS = 632
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 316."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_316.ITEM_ID, "name": ItemDefinition_316.NAME, "atk": ItemDefinition_316.ATTACK_BONUS, "def": ItemDefinition_316.DEFENSE_BONUS}


class ItemDefinition_317:
    ITEM_ID = "item_317"
    NAME = "Hyperion Legendary Artifact #317"
    TYPE = "Weapon" if 317 % 2 == 0 else "Armor"
    RARITY = "Epic" if 317 % 5 == 0 else "Legendary"
    BASE_VALUE = 15850
    ATTACK_BONUS = 951
    DEFENSE_BONUS = 634
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 317."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_317.ITEM_ID, "name": ItemDefinition_317.NAME, "atk": ItemDefinition_317.ATTACK_BONUS, "def": ItemDefinition_317.DEFENSE_BONUS}


class ItemDefinition_318:
    ITEM_ID = "item_318"
    NAME = "Hyperion Legendary Artifact #318"
    TYPE = "Weapon" if 318 % 2 == 0 else "Armor"
    RARITY = "Epic" if 318 % 5 == 0 else "Legendary"
    BASE_VALUE = 15900
    ATTACK_BONUS = 954
    DEFENSE_BONUS = 636
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 318."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_318.ITEM_ID, "name": ItemDefinition_318.NAME, "atk": ItemDefinition_318.ATTACK_BONUS, "def": ItemDefinition_318.DEFENSE_BONUS}


class ItemDefinition_319:
    ITEM_ID = "item_319"
    NAME = "Hyperion Legendary Artifact #319"
    TYPE = "Weapon" if 319 % 2 == 0 else "Armor"
    RARITY = "Epic" if 319 % 5 == 0 else "Legendary"
    BASE_VALUE = 15950
    ATTACK_BONUS = 957
    DEFENSE_BONUS = 638
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 319."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_319.ITEM_ID, "name": ItemDefinition_319.NAME, "atk": ItemDefinition_319.ATTACK_BONUS, "def": ItemDefinition_319.DEFENSE_BONUS}


class ItemDefinition_320:
    ITEM_ID = "item_320"
    NAME = "Hyperion Legendary Artifact #320"
    TYPE = "Weapon" if 320 % 2 == 0 else "Armor"
    RARITY = "Epic" if 320 % 5 == 0 else "Legendary"
    BASE_VALUE = 16000
    ATTACK_BONUS = 960
    DEFENSE_BONUS = 640
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 320."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_320.ITEM_ID, "name": ItemDefinition_320.NAME, "atk": ItemDefinition_320.ATTACK_BONUS, "def": ItemDefinition_320.DEFENSE_BONUS}


class ItemDefinition_321:
    ITEM_ID = "item_321"
    NAME = "Hyperion Legendary Artifact #321"
    TYPE = "Weapon" if 321 % 2 == 0 else "Armor"
    RARITY = "Epic" if 321 % 5 == 0 else "Legendary"
    BASE_VALUE = 16050
    ATTACK_BONUS = 963
    DEFENSE_BONUS = 642
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 321."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_321.ITEM_ID, "name": ItemDefinition_321.NAME, "atk": ItemDefinition_321.ATTACK_BONUS, "def": ItemDefinition_321.DEFENSE_BONUS}


class ItemDefinition_322:
    ITEM_ID = "item_322"
    NAME = "Hyperion Legendary Artifact #322"
    TYPE = "Weapon" if 322 % 2 == 0 else "Armor"
    RARITY = "Epic" if 322 % 5 == 0 else "Legendary"
    BASE_VALUE = 16100
    ATTACK_BONUS = 966
    DEFENSE_BONUS = 644
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 322."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_322.ITEM_ID, "name": ItemDefinition_322.NAME, "atk": ItemDefinition_322.ATTACK_BONUS, "def": ItemDefinition_322.DEFENSE_BONUS}


class ItemDefinition_323:
    ITEM_ID = "item_323"
    NAME = "Hyperion Legendary Artifact #323"
    TYPE = "Weapon" if 323 % 2 == 0 else "Armor"
    RARITY = "Epic" if 323 % 5 == 0 else "Legendary"
    BASE_VALUE = 16150
    ATTACK_BONUS = 969
    DEFENSE_BONUS = 646
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 323."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_323.ITEM_ID, "name": ItemDefinition_323.NAME, "atk": ItemDefinition_323.ATTACK_BONUS, "def": ItemDefinition_323.DEFENSE_BONUS}


class ItemDefinition_324:
    ITEM_ID = "item_324"
    NAME = "Hyperion Legendary Artifact #324"
    TYPE = "Weapon" if 324 % 2 == 0 else "Armor"
    RARITY = "Epic" if 324 % 5 == 0 else "Legendary"
    BASE_VALUE = 16200
    ATTACK_BONUS = 972
    DEFENSE_BONUS = 648
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 324."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_324.ITEM_ID, "name": ItemDefinition_324.NAME, "atk": ItemDefinition_324.ATTACK_BONUS, "def": ItemDefinition_324.DEFENSE_BONUS}


class ItemDefinition_325:
    ITEM_ID = "item_325"
    NAME = "Hyperion Legendary Artifact #325"
    TYPE = "Weapon" if 325 % 2 == 0 else "Armor"
    RARITY = "Epic" if 325 % 5 == 0 else "Legendary"
    BASE_VALUE = 16250
    ATTACK_BONUS = 975
    DEFENSE_BONUS = 650
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 325."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_325.ITEM_ID, "name": ItemDefinition_325.NAME, "atk": ItemDefinition_325.ATTACK_BONUS, "def": ItemDefinition_325.DEFENSE_BONUS}


class ItemDefinition_326:
    ITEM_ID = "item_326"
    NAME = "Hyperion Legendary Artifact #326"
    TYPE = "Weapon" if 326 % 2 == 0 else "Armor"
    RARITY = "Epic" if 326 % 5 == 0 else "Legendary"
    BASE_VALUE = 16300
    ATTACK_BONUS = 978
    DEFENSE_BONUS = 652
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 326."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_326.ITEM_ID, "name": ItemDefinition_326.NAME, "atk": ItemDefinition_326.ATTACK_BONUS, "def": ItemDefinition_326.DEFENSE_BONUS}


class ItemDefinition_327:
    ITEM_ID = "item_327"
    NAME = "Hyperion Legendary Artifact #327"
    TYPE = "Weapon" if 327 % 2 == 0 else "Armor"
    RARITY = "Epic" if 327 % 5 == 0 else "Legendary"
    BASE_VALUE = 16350
    ATTACK_BONUS = 981
    DEFENSE_BONUS = 654
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 327."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_327.ITEM_ID, "name": ItemDefinition_327.NAME, "atk": ItemDefinition_327.ATTACK_BONUS, "def": ItemDefinition_327.DEFENSE_BONUS}


class ItemDefinition_328:
    ITEM_ID = "item_328"
    NAME = "Hyperion Legendary Artifact #328"
    TYPE = "Weapon" if 328 % 2 == 0 else "Armor"
    RARITY = "Epic" if 328 % 5 == 0 else "Legendary"
    BASE_VALUE = 16400
    ATTACK_BONUS = 984
    DEFENSE_BONUS = 656
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 328."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_328.ITEM_ID, "name": ItemDefinition_328.NAME, "atk": ItemDefinition_328.ATTACK_BONUS, "def": ItemDefinition_328.DEFENSE_BONUS}


class ItemDefinition_329:
    ITEM_ID = "item_329"
    NAME = "Hyperion Legendary Artifact #329"
    TYPE = "Weapon" if 329 % 2 == 0 else "Armor"
    RARITY = "Epic" if 329 % 5 == 0 else "Legendary"
    BASE_VALUE = 16450
    ATTACK_BONUS = 987
    DEFENSE_BONUS = 658
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 329."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_329.ITEM_ID, "name": ItemDefinition_329.NAME, "atk": ItemDefinition_329.ATTACK_BONUS, "def": ItemDefinition_329.DEFENSE_BONUS}


class ItemDefinition_330:
    ITEM_ID = "item_330"
    NAME = "Hyperion Legendary Artifact #330"
    TYPE = "Weapon" if 330 % 2 == 0 else "Armor"
    RARITY = "Epic" if 330 % 5 == 0 else "Legendary"
    BASE_VALUE = 16500
    ATTACK_BONUS = 990
    DEFENSE_BONUS = 660
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 330."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_330.ITEM_ID, "name": ItemDefinition_330.NAME, "atk": ItemDefinition_330.ATTACK_BONUS, "def": ItemDefinition_330.DEFENSE_BONUS}


class ItemDefinition_331:
    ITEM_ID = "item_331"
    NAME = "Hyperion Legendary Artifact #331"
    TYPE = "Weapon" if 331 % 2 == 0 else "Armor"
    RARITY = "Epic" if 331 % 5 == 0 else "Legendary"
    BASE_VALUE = 16550
    ATTACK_BONUS = 993
    DEFENSE_BONUS = 662
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 331."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_331.ITEM_ID, "name": ItemDefinition_331.NAME, "atk": ItemDefinition_331.ATTACK_BONUS, "def": ItemDefinition_331.DEFENSE_BONUS}


class ItemDefinition_332:
    ITEM_ID = "item_332"
    NAME = "Hyperion Legendary Artifact #332"
    TYPE = "Weapon" if 332 % 2 == 0 else "Armor"
    RARITY = "Epic" if 332 % 5 == 0 else "Legendary"
    BASE_VALUE = 16600
    ATTACK_BONUS = 996
    DEFENSE_BONUS = 664
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 332."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_332.ITEM_ID, "name": ItemDefinition_332.NAME, "atk": ItemDefinition_332.ATTACK_BONUS, "def": ItemDefinition_332.DEFENSE_BONUS}


class ItemDefinition_333:
    ITEM_ID = "item_333"
    NAME = "Hyperion Legendary Artifact #333"
    TYPE = "Weapon" if 333 % 2 == 0 else "Armor"
    RARITY = "Epic" if 333 % 5 == 0 else "Legendary"
    BASE_VALUE = 16650
    ATTACK_BONUS = 999
    DEFENSE_BONUS = 666
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 333."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_333.ITEM_ID, "name": ItemDefinition_333.NAME, "atk": ItemDefinition_333.ATTACK_BONUS, "def": ItemDefinition_333.DEFENSE_BONUS}


class ItemDefinition_334:
    ITEM_ID = "item_334"
    NAME = "Hyperion Legendary Artifact #334"
    TYPE = "Weapon" if 334 % 2 == 0 else "Armor"
    RARITY = "Epic" if 334 % 5 == 0 else "Legendary"
    BASE_VALUE = 16700
    ATTACK_BONUS = 1002
    DEFENSE_BONUS = 668
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 334."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_334.ITEM_ID, "name": ItemDefinition_334.NAME, "atk": ItemDefinition_334.ATTACK_BONUS, "def": ItemDefinition_334.DEFENSE_BONUS}


class ItemDefinition_335:
    ITEM_ID = "item_335"
    NAME = "Hyperion Legendary Artifact #335"
    TYPE = "Weapon" if 335 % 2 == 0 else "Armor"
    RARITY = "Epic" if 335 % 5 == 0 else "Legendary"
    BASE_VALUE = 16750
    ATTACK_BONUS = 1005
    DEFENSE_BONUS = 670
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 335."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_335.ITEM_ID, "name": ItemDefinition_335.NAME, "atk": ItemDefinition_335.ATTACK_BONUS, "def": ItemDefinition_335.DEFENSE_BONUS}


class ItemDefinition_336:
    ITEM_ID = "item_336"
    NAME = "Hyperion Legendary Artifact #336"
    TYPE = "Weapon" if 336 % 2 == 0 else "Armor"
    RARITY = "Epic" if 336 % 5 == 0 else "Legendary"
    BASE_VALUE = 16800
    ATTACK_BONUS = 1008
    DEFENSE_BONUS = 672
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 336."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_336.ITEM_ID, "name": ItemDefinition_336.NAME, "atk": ItemDefinition_336.ATTACK_BONUS, "def": ItemDefinition_336.DEFENSE_BONUS}


class ItemDefinition_337:
    ITEM_ID = "item_337"
    NAME = "Hyperion Legendary Artifact #337"
    TYPE = "Weapon" if 337 % 2 == 0 else "Armor"
    RARITY = "Epic" if 337 % 5 == 0 else "Legendary"
    BASE_VALUE = 16850
    ATTACK_BONUS = 1011
    DEFENSE_BONUS = 674
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 337."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_337.ITEM_ID, "name": ItemDefinition_337.NAME, "atk": ItemDefinition_337.ATTACK_BONUS, "def": ItemDefinition_337.DEFENSE_BONUS}


class ItemDefinition_338:
    ITEM_ID = "item_338"
    NAME = "Hyperion Legendary Artifact #338"
    TYPE = "Weapon" if 338 % 2 == 0 else "Armor"
    RARITY = "Epic" if 338 % 5 == 0 else "Legendary"
    BASE_VALUE = 16900
    ATTACK_BONUS = 1014
    DEFENSE_BONUS = 676
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 338."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_338.ITEM_ID, "name": ItemDefinition_338.NAME, "atk": ItemDefinition_338.ATTACK_BONUS, "def": ItemDefinition_338.DEFENSE_BONUS}


class ItemDefinition_339:
    ITEM_ID = "item_339"
    NAME = "Hyperion Legendary Artifact #339"
    TYPE = "Weapon" if 339 % 2 == 0 else "Armor"
    RARITY = "Epic" if 339 % 5 == 0 else "Legendary"
    BASE_VALUE = 16950
    ATTACK_BONUS = 1017
    DEFENSE_BONUS = 678
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 339."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_339.ITEM_ID, "name": ItemDefinition_339.NAME, "atk": ItemDefinition_339.ATTACK_BONUS, "def": ItemDefinition_339.DEFENSE_BONUS}


class ItemDefinition_340:
    ITEM_ID = "item_340"
    NAME = "Hyperion Legendary Artifact #340"
    TYPE = "Weapon" if 340 % 2 == 0 else "Armor"
    RARITY = "Epic" if 340 % 5 == 0 else "Legendary"
    BASE_VALUE = 17000
    ATTACK_BONUS = 1020
    DEFENSE_BONUS = 680
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 340."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_340.ITEM_ID, "name": ItemDefinition_340.NAME, "atk": ItemDefinition_340.ATTACK_BONUS, "def": ItemDefinition_340.DEFENSE_BONUS}


class ItemDefinition_341:
    ITEM_ID = "item_341"
    NAME = "Hyperion Legendary Artifact #341"
    TYPE = "Weapon" if 341 % 2 == 0 else "Armor"
    RARITY = "Epic" if 341 % 5 == 0 else "Legendary"
    BASE_VALUE = 17050
    ATTACK_BONUS = 1023
    DEFENSE_BONUS = 682
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 341."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_341.ITEM_ID, "name": ItemDefinition_341.NAME, "atk": ItemDefinition_341.ATTACK_BONUS, "def": ItemDefinition_341.DEFENSE_BONUS}


class ItemDefinition_342:
    ITEM_ID = "item_342"
    NAME = "Hyperion Legendary Artifact #342"
    TYPE = "Weapon" if 342 % 2 == 0 else "Armor"
    RARITY = "Epic" if 342 % 5 == 0 else "Legendary"
    BASE_VALUE = 17100
    ATTACK_BONUS = 1026
    DEFENSE_BONUS = 684
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 342."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_342.ITEM_ID, "name": ItemDefinition_342.NAME, "atk": ItemDefinition_342.ATTACK_BONUS, "def": ItemDefinition_342.DEFENSE_BONUS}


class ItemDefinition_343:
    ITEM_ID = "item_343"
    NAME = "Hyperion Legendary Artifact #343"
    TYPE = "Weapon" if 343 % 2 == 0 else "Armor"
    RARITY = "Epic" if 343 % 5 == 0 else "Legendary"
    BASE_VALUE = 17150
    ATTACK_BONUS = 1029
    DEFENSE_BONUS = 686
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 343."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_343.ITEM_ID, "name": ItemDefinition_343.NAME, "atk": ItemDefinition_343.ATTACK_BONUS, "def": ItemDefinition_343.DEFENSE_BONUS}


class ItemDefinition_344:
    ITEM_ID = "item_344"
    NAME = "Hyperion Legendary Artifact #344"
    TYPE = "Weapon" if 344 % 2 == 0 else "Armor"
    RARITY = "Epic" if 344 % 5 == 0 else "Legendary"
    BASE_VALUE = 17200
    ATTACK_BONUS = 1032
    DEFENSE_BONUS = 688
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 344."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_344.ITEM_ID, "name": ItemDefinition_344.NAME, "atk": ItemDefinition_344.ATTACK_BONUS, "def": ItemDefinition_344.DEFENSE_BONUS}


class ItemDefinition_345:
    ITEM_ID = "item_345"
    NAME = "Hyperion Legendary Artifact #345"
    TYPE = "Weapon" if 345 % 2 == 0 else "Armor"
    RARITY = "Epic" if 345 % 5 == 0 else "Legendary"
    BASE_VALUE = 17250
    ATTACK_BONUS = 1035
    DEFENSE_BONUS = 690
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 345."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_345.ITEM_ID, "name": ItemDefinition_345.NAME, "atk": ItemDefinition_345.ATTACK_BONUS, "def": ItemDefinition_345.DEFENSE_BONUS}


class ItemDefinition_346:
    ITEM_ID = "item_346"
    NAME = "Hyperion Legendary Artifact #346"
    TYPE = "Weapon" if 346 % 2 == 0 else "Armor"
    RARITY = "Epic" if 346 % 5 == 0 else "Legendary"
    BASE_VALUE = 17300
    ATTACK_BONUS = 1038
    DEFENSE_BONUS = 692
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 346."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_346.ITEM_ID, "name": ItemDefinition_346.NAME, "atk": ItemDefinition_346.ATTACK_BONUS, "def": ItemDefinition_346.DEFENSE_BONUS}


class ItemDefinition_347:
    ITEM_ID = "item_347"
    NAME = "Hyperion Legendary Artifact #347"
    TYPE = "Weapon" if 347 % 2 == 0 else "Armor"
    RARITY = "Epic" if 347 % 5 == 0 else "Legendary"
    BASE_VALUE = 17350
    ATTACK_BONUS = 1041
    DEFENSE_BONUS = 694
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 347."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_347.ITEM_ID, "name": ItemDefinition_347.NAME, "atk": ItemDefinition_347.ATTACK_BONUS, "def": ItemDefinition_347.DEFENSE_BONUS}


class ItemDefinition_348:
    ITEM_ID = "item_348"
    NAME = "Hyperion Legendary Artifact #348"
    TYPE = "Weapon" if 348 % 2 == 0 else "Armor"
    RARITY = "Epic" if 348 % 5 == 0 else "Legendary"
    BASE_VALUE = 17400
    ATTACK_BONUS = 1044
    DEFENSE_BONUS = 696
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 348."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_348.ITEM_ID, "name": ItemDefinition_348.NAME, "atk": ItemDefinition_348.ATTACK_BONUS, "def": ItemDefinition_348.DEFENSE_BONUS}


class ItemDefinition_349:
    ITEM_ID = "item_349"
    NAME = "Hyperion Legendary Artifact #349"
    TYPE = "Weapon" if 349 % 2 == 0 else "Armor"
    RARITY = "Epic" if 349 % 5 == 0 else "Legendary"
    BASE_VALUE = 17450
    ATTACK_BONUS = 1047
    DEFENSE_BONUS = 698
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 349."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_349.ITEM_ID, "name": ItemDefinition_349.NAME, "atk": ItemDefinition_349.ATTACK_BONUS, "def": ItemDefinition_349.DEFENSE_BONUS}


class ItemDefinition_350:
    ITEM_ID = "item_350"
    NAME = "Hyperion Legendary Artifact #350"
    TYPE = "Weapon" if 350 % 2 == 0 else "Armor"
    RARITY = "Epic" if 350 % 5 == 0 else "Legendary"
    BASE_VALUE = 17500
    ATTACK_BONUS = 1050
    DEFENSE_BONUS = 700
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 350."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_350.ITEM_ID, "name": ItemDefinition_350.NAME, "atk": ItemDefinition_350.ATTACK_BONUS, "def": ItemDefinition_350.DEFENSE_BONUS}


class ItemDefinition_351:
    ITEM_ID = "item_351"
    NAME = "Hyperion Legendary Artifact #351"
    TYPE = "Weapon" if 351 % 2 == 0 else "Armor"
    RARITY = "Epic" if 351 % 5 == 0 else "Legendary"
    BASE_VALUE = 17550
    ATTACK_BONUS = 1053
    DEFENSE_BONUS = 702
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 351."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_351.ITEM_ID, "name": ItemDefinition_351.NAME, "atk": ItemDefinition_351.ATTACK_BONUS, "def": ItemDefinition_351.DEFENSE_BONUS}


class ItemDefinition_352:
    ITEM_ID = "item_352"
    NAME = "Hyperion Legendary Artifact #352"
    TYPE = "Weapon" if 352 % 2 == 0 else "Armor"
    RARITY = "Epic" if 352 % 5 == 0 else "Legendary"
    BASE_VALUE = 17600
    ATTACK_BONUS = 1056
    DEFENSE_BONUS = 704
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 352."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_352.ITEM_ID, "name": ItemDefinition_352.NAME, "atk": ItemDefinition_352.ATTACK_BONUS, "def": ItemDefinition_352.DEFENSE_BONUS}


class ItemDefinition_353:
    ITEM_ID = "item_353"
    NAME = "Hyperion Legendary Artifact #353"
    TYPE = "Weapon" if 353 % 2 == 0 else "Armor"
    RARITY = "Epic" if 353 % 5 == 0 else "Legendary"
    BASE_VALUE = 17650
    ATTACK_BONUS = 1059
    DEFENSE_BONUS = 706
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 353."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_353.ITEM_ID, "name": ItemDefinition_353.NAME, "atk": ItemDefinition_353.ATTACK_BONUS, "def": ItemDefinition_353.DEFENSE_BONUS}


class ItemDefinition_354:
    ITEM_ID = "item_354"
    NAME = "Hyperion Legendary Artifact #354"
    TYPE = "Weapon" if 354 % 2 == 0 else "Armor"
    RARITY = "Epic" if 354 % 5 == 0 else "Legendary"
    BASE_VALUE = 17700
    ATTACK_BONUS = 1062
    DEFENSE_BONUS = 708
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 354."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_354.ITEM_ID, "name": ItemDefinition_354.NAME, "atk": ItemDefinition_354.ATTACK_BONUS, "def": ItemDefinition_354.DEFENSE_BONUS}


class ItemDefinition_355:
    ITEM_ID = "item_355"
    NAME = "Hyperion Legendary Artifact #355"
    TYPE = "Weapon" if 355 % 2 == 0 else "Armor"
    RARITY = "Epic" if 355 % 5 == 0 else "Legendary"
    BASE_VALUE = 17750
    ATTACK_BONUS = 1065
    DEFENSE_BONUS = 710
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 355."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_355.ITEM_ID, "name": ItemDefinition_355.NAME, "atk": ItemDefinition_355.ATTACK_BONUS, "def": ItemDefinition_355.DEFENSE_BONUS}


class ItemDefinition_356:
    ITEM_ID = "item_356"
    NAME = "Hyperion Legendary Artifact #356"
    TYPE = "Weapon" if 356 % 2 == 0 else "Armor"
    RARITY = "Epic" if 356 % 5 == 0 else "Legendary"
    BASE_VALUE = 17800
    ATTACK_BONUS = 1068
    DEFENSE_BONUS = 712
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 356."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_356.ITEM_ID, "name": ItemDefinition_356.NAME, "atk": ItemDefinition_356.ATTACK_BONUS, "def": ItemDefinition_356.DEFENSE_BONUS}


class ItemDefinition_357:
    ITEM_ID = "item_357"
    NAME = "Hyperion Legendary Artifact #357"
    TYPE = "Weapon" if 357 % 2 == 0 else "Armor"
    RARITY = "Epic" if 357 % 5 == 0 else "Legendary"
    BASE_VALUE = 17850
    ATTACK_BONUS = 1071
    DEFENSE_BONUS = 714
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 357."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_357.ITEM_ID, "name": ItemDefinition_357.NAME, "atk": ItemDefinition_357.ATTACK_BONUS, "def": ItemDefinition_357.DEFENSE_BONUS}


class ItemDefinition_358:
    ITEM_ID = "item_358"
    NAME = "Hyperion Legendary Artifact #358"
    TYPE = "Weapon" if 358 % 2 == 0 else "Armor"
    RARITY = "Epic" if 358 % 5 == 0 else "Legendary"
    BASE_VALUE = 17900
    ATTACK_BONUS = 1074
    DEFENSE_BONUS = 716
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 358."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_358.ITEM_ID, "name": ItemDefinition_358.NAME, "atk": ItemDefinition_358.ATTACK_BONUS, "def": ItemDefinition_358.DEFENSE_BONUS}


class ItemDefinition_359:
    ITEM_ID = "item_359"
    NAME = "Hyperion Legendary Artifact #359"
    TYPE = "Weapon" if 359 % 2 == 0 else "Armor"
    RARITY = "Epic" if 359 % 5 == 0 else "Legendary"
    BASE_VALUE = 17950
    ATTACK_BONUS = 1077
    DEFENSE_BONUS = 718
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 359."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_359.ITEM_ID, "name": ItemDefinition_359.NAME, "atk": ItemDefinition_359.ATTACK_BONUS, "def": ItemDefinition_359.DEFENSE_BONUS}


class ItemDefinition_360:
    ITEM_ID = "item_360"
    NAME = "Hyperion Legendary Artifact #360"
    TYPE = "Weapon" if 360 % 2 == 0 else "Armor"
    RARITY = "Epic" if 360 % 5 == 0 else "Legendary"
    BASE_VALUE = 18000
    ATTACK_BONUS = 1080
    DEFENSE_BONUS = 720
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 360."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_360.ITEM_ID, "name": ItemDefinition_360.NAME, "atk": ItemDefinition_360.ATTACK_BONUS, "def": ItemDefinition_360.DEFENSE_BONUS}


class ItemDefinition_361:
    ITEM_ID = "item_361"
    NAME = "Hyperion Legendary Artifact #361"
    TYPE = "Weapon" if 361 % 2 == 0 else "Armor"
    RARITY = "Epic" if 361 % 5 == 0 else "Legendary"
    BASE_VALUE = 18050
    ATTACK_BONUS = 1083
    DEFENSE_BONUS = 722
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 361."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_361.ITEM_ID, "name": ItemDefinition_361.NAME, "atk": ItemDefinition_361.ATTACK_BONUS, "def": ItemDefinition_361.DEFENSE_BONUS}


class ItemDefinition_362:
    ITEM_ID = "item_362"
    NAME = "Hyperion Legendary Artifact #362"
    TYPE = "Weapon" if 362 % 2 == 0 else "Armor"
    RARITY = "Epic" if 362 % 5 == 0 else "Legendary"
    BASE_VALUE = 18100
    ATTACK_BONUS = 1086
    DEFENSE_BONUS = 724
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 362."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_362.ITEM_ID, "name": ItemDefinition_362.NAME, "atk": ItemDefinition_362.ATTACK_BONUS, "def": ItemDefinition_362.DEFENSE_BONUS}


class ItemDefinition_363:
    ITEM_ID = "item_363"
    NAME = "Hyperion Legendary Artifact #363"
    TYPE = "Weapon" if 363 % 2 == 0 else "Armor"
    RARITY = "Epic" if 363 % 5 == 0 else "Legendary"
    BASE_VALUE = 18150
    ATTACK_BONUS = 1089
    DEFENSE_BONUS = 726
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 363."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_363.ITEM_ID, "name": ItemDefinition_363.NAME, "atk": ItemDefinition_363.ATTACK_BONUS, "def": ItemDefinition_363.DEFENSE_BONUS}


class ItemDefinition_364:
    ITEM_ID = "item_364"
    NAME = "Hyperion Legendary Artifact #364"
    TYPE = "Weapon" if 364 % 2 == 0 else "Armor"
    RARITY = "Epic" if 364 % 5 == 0 else "Legendary"
    BASE_VALUE = 18200
    ATTACK_BONUS = 1092
    DEFENSE_BONUS = 728
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 364."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_364.ITEM_ID, "name": ItemDefinition_364.NAME, "atk": ItemDefinition_364.ATTACK_BONUS, "def": ItemDefinition_364.DEFENSE_BONUS}


class ItemDefinition_365:
    ITEM_ID = "item_365"
    NAME = "Hyperion Legendary Artifact #365"
    TYPE = "Weapon" if 365 % 2 == 0 else "Armor"
    RARITY = "Epic" if 365 % 5 == 0 else "Legendary"
    BASE_VALUE = 18250
    ATTACK_BONUS = 1095
    DEFENSE_BONUS = 730
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 365."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_365.ITEM_ID, "name": ItemDefinition_365.NAME, "atk": ItemDefinition_365.ATTACK_BONUS, "def": ItemDefinition_365.DEFENSE_BONUS}


class ItemDefinition_366:
    ITEM_ID = "item_366"
    NAME = "Hyperion Legendary Artifact #366"
    TYPE = "Weapon" if 366 % 2 == 0 else "Armor"
    RARITY = "Epic" if 366 % 5 == 0 else "Legendary"
    BASE_VALUE = 18300
    ATTACK_BONUS = 1098
    DEFENSE_BONUS = 732
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 366."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_366.ITEM_ID, "name": ItemDefinition_366.NAME, "atk": ItemDefinition_366.ATTACK_BONUS, "def": ItemDefinition_366.DEFENSE_BONUS}


class ItemDefinition_367:
    ITEM_ID = "item_367"
    NAME = "Hyperion Legendary Artifact #367"
    TYPE = "Weapon" if 367 % 2 == 0 else "Armor"
    RARITY = "Epic" if 367 % 5 == 0 else "Legendary"
    BASE_VALUE = 18350
    ATTACK_BONUS = 1101
    DEFENSE_BONUS = 734
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 367."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_367.ITEM_ID, "name": ItemDefinition_367.NAME, "atk": ItemDefinition_367.ATTACK_BONUS, "def": ItemDefinition_367.DEFENSE_BONUS}


class ItemDefinition_368:
    ITEM_ID = "item_368"
    NAME = "Hyperion Legendary Artifact #368"
    TYPE = "Weapon" if 368 % 2 == 0 else "Armor"
    RARITY = "Epic" if 368 % 5 == 0 else "Legendary"
    BASE_VALUE = 18400
    ATTACK_BONUS = 1104
    DEFENSE_BONUS = 736
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 368."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_368.ITEM_ID, "name": ItemDefinition_368.NAME, "atk": ItemDefinition_368.ATTACK_BONUS, "def": ItemDefinition_368.DEFENSE_BONUS}


class ItemDefinition_369:
    ITEM_ID = "item_369"
    NAME = "Hyperion Legendary Artifact #369"
    TYPE = "Weapon" if 369 % 2 == 0 else "Armor"
    RARITY = "Epic" if 369 % 5 == 0 else "Legendary"
    BASE_VALUE = 18450
    ATTACK_BONUS = 1107
    DEFENSE_BONUS = 738
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 369."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_369.ITEM_ID, "name": ItemDefinition_369.NAME, "atk": ItemDefinition_369.ATTACK_BONUS, "def": ItemDefinition_369.DEFENSE_BONUS}


class ItemDefinition_370:
    ITEM_ID = "item_370"
    NAME = "Hyperion Legendary Artifact #370"
    TYPE = "Weapon" if 370 % 2 == 0 else "Armor"
    RARITY = "Epic" if 370 % 5 == 0 else "Legendary"
    BASE_VALUE = 18500
    ATTACK_BONUS = 1110
    DEFENSE_BONUS = 740
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 370."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_370.ITEM_ID, "name": ItemDefinition_370.NAME, "atk": ItemDefinition_370.ATTACK_BONUS, "def": ItemDefinition_370.DEFENSE_BONUS}


class ItemDefinition_371:
    ITEM_ID = "item_371"
    NAME = "Hyperion Legendary Artifact #371"
    TYPE = "Weapon" if 371 % 2 == 0 else "Armor"
    RARITY = "Epic" if 371 % 5 == 0 else "Legendary"
    BASE_VALUE = 18550
    ATTACK_BONUS = 1113
    DEFENSE_BONUS = 742
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 371."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_371.ITEM_ID, "name": ItemDefinition_371.NAME, "atk": ItemDefinition_371.ATTACK_BONUS, "def": ItemDefinition_371.DEFENSE_BONUS}


class ItemDefinition_372:
    ITEM_ID = "item_372"
    NAME = "Hyperion Legendary Artifact #372"
    TYPE = "Weapon" if 372 % 2 == 0 else "Armor"
    RARITY = "Epic" if 372 % 5 == 0 else "Legendary"
    BASE_VALUE = 18600
    ATTACK_BONUS = 1116
    DEFENSE_BONUS = 744
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 372."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_372.ITEM_ID, "name": ItemDefinition_372.NAME, "atk": ItemDefinition_372.ATTACK_BONUS, "def": ItemDefinition_372.DEFENSE_BONUS}


class ItemDefinition_373:
    ITEM_ID = "item_373"
    NAME = "Hyperion Legendary Artifact #373"
    TYPE = "Weapon" if 373 % 2 == 0 else "Armor"
    RARITY = "Epic" if 373 % 5 == 0 else "Legendary"
    BASE_VALUE = 18650
    ATTACK_BONUS = 1119
    DEFENSE_BONUS = 746
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 373."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_373.ITEM_ID, "name": ItemDefinition_373.NAME, "atk": ItemDefinition_373.ATTACK_BONUS, "def": ItemDefinition_373.DEFENSE_BONUS}


class ItemDefinition_374:
    ITEM_ID = "item_374"
    NAME = "Hyperion Legendary Artifact #374"
    TYPE = "Weapon" if 374 % 2 == 0 else "Armor"
    RARITY = "Epic" if 374 % 5 == 0 else "Legendary"
    BASE_VALUE = 18700
    ATTACK_BONUS = 1122
    DEFENSE_BONUS = 748
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 374."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_374.ITEM_ID, "name": ItemDefinition_374.NAME, "atk": ItemDefinition_374.ATTACK_BONUS, "def": ItemDefinition_374.DEFENSE_BONUS}


class ItemDefinition_375:
    ITEM_ID = "item_375"
    NAME = "Hyperion Legendary Artifact #375"
    TYPE = "Weapon" if 375 % 2 == 0 else "Armor"
    RARITY = "Epic" if 375 % 5 == 0 else "Legendary"
    BASE_VALUE = 18750
    ATTACK_BONUS = 1125
    DEFENSE_BONUS = 750
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 375."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_375.ITEM_ID, "name": ItemDefinition_375.NAME, "atk": ItemDefinition_375.ATTACK_BONUS, "def": ItemDefinition_375.DEFENSE_BONUS}


class ItemDefinition_376:
    ITEM_ID = "item_376"
    NAME = "Hyperion Legendary Artifact #376"
    TYPE = "Weapon" if 376 % 2 == 0 else "Armor"
    RARITY = "Epic" if 376 % 5 == 0 else "Legendary"
    BASE_VALUE = 18800
    ATTACK_BONUS = 1128
    DEFENSE_BONUS = 752
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 376."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_376.ITEM_ID, "name": ItemDefinition_376.NAME, "atk": ItemDefinition_376.ATTACK_BONUS, "def": ItemDefinition_376.DEFENSE_BONUS}


class ItemDefinition_377:
    ITEM_ID = "item_377"
    NAME = "Hyperion Legendary Artifact #377"
    TYPE = "Weapon" if 377 % 2 == 0 else "Armor"
    RARITY = "Epic" if 377 % 5 == 0 else "Legendary"
    BASE_VALUE = 18850
    ATTACK_BONUS = 1131
    DEFENSE_BONUS = 754
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 377."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_377.ITEM_ID, "name": ItemDefinition_377.NAME, "atk": ItemDefinition_377.ATTACK_BONUS, "def": ItemDefinition_377.DEFENSE_BONUS}


class ItemDefinition_378:
    ITEM_ID = "item_378"
    NAME = "Hyperion Legendary Artifact #378"
    TYPE = "Weapon" if 378 % 2 == 0 else "Armor"
    RARITY = "Epic" if 378 % 5 == 0 else "Legendary"
    BASE_VALUE = 18900
    ATTACK_BONUS = 1134
    DEFENSE_BONUS = 756
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 378."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_378.ITEM_ID, "name": ItemDefinition_378.NAME, "atk": ItemDefinition_378.ATTACK_BONUS, "def": ItemDefinition_378.DEFENSE_BONUS}


class ItemDefinition_379:
    ITEM_ID = "item_379"
    NAME = "Hyperion Legendary Artifact #379"
    TYPE = "Weapon" if 379 % 2 == 0 else "Armor"
    RARITY = "Epic" if 379 % 5 == 0 else "Legendary"
    BASE_VALUE = 18950
    ATTACK_BONUS = 1137
    DEFENSE_BONUS = 758
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 379."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_379.ITEM_ID, "name": ItemDefinition_379.NAME, "atk": ItemDefinition_379.ATTACK_BONUS, "def": ItemDefinition_379.DEFENSE_BONUS}


class ItemDefinition_380:
    ITEM_ID = "item_380"
    NAME = "Hyperion Legendary Artifact #380"
    TYPE = "Weapon" if 380 % 2 == 0 else "Armor"
    RARITY = "Epic" if 380 % 5 == 0 else "Legendary"
    BASE_VALUE = 19000
    ATTACK_BONUS = 1140
    DEFENSE_BONUS = 760
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 380."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_380.ITEM_ID, "name": ItemDefinition_380.NAME, "atk": ItemDefinition_380.ATTACK_BONUS, "def": ItemDefinition_380.DEFENSE_BONUS}


class ItemDefinition_381:
    ITEM_ID = "item_381"
    NAME = "Hyperion Legendary Artifact #381"
    TYPE = "Weapon" if 381 % 2 == 0 else "Armor"
    RARITY = "Epic" if 381 % 5 == 0 else "Legendary"
    BASE_VALUE = 19050
    ATTACK_BONUS = 1143
    DEFENSE_BONUS = 762
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 381."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_381.ITEM_ID, "name": ItemDefinition_381.NAME, "atk": ItemDefinition_381.ATTACK_BONUS, "def": ItemDefinition_381.DEFENSE_BONUS}


class ItemDefinition_382:
    ITEM_ID = "item_382"
    NAME = "Hyperion Legendary Artifact #382"
    TYPE = "Weapon" if 382 % 2 == 0 else "Armor"
    RARITY = "Epic" if 382 % 5 == 0 else "Legendary"
    BASE_VALUE = 19100
    ATTACK_BONUS = 1146
    DEFENSE_BONUS = 764
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 382."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_382.ITEM_ID, "name": ItemDefinition_382.NAME, "atk": ItemDefinition_382.ATTACK_BONUS, "def": ItemDefinition_382.DEFENSE_BONUS}


class ItemDefinition_383:
    ITEM_ID = "item_383"
    NAME = "Hyperion Legendary Artifact #383"
    TYPE = "Weapon" if 383 % 2 == 0 else "Armor"
    RARITY = "Epic" if 383 % 5 == 0 else "Legendary"
    BASE_VALUE = 19150
    ATTACK_BONUS = 1149
    DEFENSE_BONUS = 766
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 383."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_383.ITEM_ID, "name": ItemDefinition_383.NAME, "atk": ItemDefinition_383.ATTACK_BONUS, "def": ItemDefinition_383.DEFENSE_BONUS}


class ItemDefinition_384:
    ITEM_ID = "item_384"
    NAME = "Hyperion Legendary Artifact #384"
    TYPE = "Weapon" if 384 % 2 == 0 else "Armor"
    RARITY = "Epic" if 384 % 5 == 0 else "Legendary"
    BASE_VALUE = 19200
    ATTACK_BONUS = 1152
    DEFENSE_BONUS = 768
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 384."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_384.ITEM_ID, "name": ItemDefinition_384.NAME, "atk": ItemDefinition_384.ATTACK_BONUS, "def": ItemDefinition_384.DEFENSE_BONUS}


class ItemDefinition_385:
    ITEM_ID = "item_385"
    NAME = "Hyperion Legendary Artifact #385"
    TYPE = "Weapon" if 385 % 2 == 0 else "Armor"
    RARITY = "Epic" if 385 % 5 == 0 else "Legendary"
    BASE_VALUE = 19250
    ATTACK_BONUS = 1155
    DEFENSE_BONUS = 770
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 385."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_385.ITEM_ID, "name": ItemDefinition_385.NAME, "atk": ItemDefinition_385.ATTACK_BONUS, "def": ItemDefinition_385.DEFENSE_BONUS}


class ItemDefinition_386:
    ITEM_ID = "item_386"
    NAME = "Hyperion Legendary Artifact #386"
    TYPE = "Weapon" if 386 % 2 == 0 else "Armor"
    RARITY = "Epic" if 386 % 5 == 0 else "Legendary"
    BASE_VALUE = 19300
    ATTACK_BONUS = 1158
    DEFENSE_BONUS = 772
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 386."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_386.ITEM_ID, "name": ItemDefinition_386.NAME, "atk": ItemDefinition_386.ATTACK_BONUS, "def": ItemDefinition_386.DEFENSE_BONUS}


class ItemDefinition_387:
    ITEM_ID = "item_387"
    NAME = "Hyperion Legendary Artifact #387"
    TYPE = "Weapon" if 387 % 2 == 0 else "Armor"
    RARITY = "Epic" if 387 % 5 == 0 else "Legendary"
    BASE_VALUE = 19350
    ATTACK_BONUS = 1161
    DEFENSE_BONUS = 774
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 387."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_387.ITEM_ID, "name": ItemDefinition_387.NAME, "atk": ItemDefinition_387.ATTACK_BONUS, "def": ItemDefinition_387.DEFENSE_BONUS}


class ItemDefinition_388:
    ITEM_ID = "item_388"
    NAME = "Hyperion Legendary Artifact #388"
    TYPE = "Weapon" if 388 % 2 == 0 else "Armor"
    RARITY = "Epic" if 388 % 5 == 0 else "Legendary"
    BASE_VALUE = 19400
    ATTACK_BONUS = 1164
    DEFENSE_BONUS = 776
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 388."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_388.ITEM_ID, "name": ItemDefinition_388.NAME, "atk": ItemDefinition_388.ATTACK_BONUS, "def": ItemDefinition_388.DEFENSE_BONUS}


class ItemDefinition_389:
    ITEM_ID = "item_389"
    NAME = "Hyperion Legendary Artifact #389"
    TYPE = "Weapon" if 389 % 2 == 0 else "Armor"
    RARITY = "Epic" if 389 % 5 == 0 else "Legendary"
    BASE_VALUE = 19450
    ATTACK_BONUS = 1167
    DEFENSE_BONUS = 778
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 389."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_389.ITEM_ID, "name": ItemDefinition_389.NAME, "atk": ItemDefinition_389.ATTACK_BONUS, "def": ItemDefinition_389.DEFENSE_BONUS}


class ItemDefinition_390:
    ITEM_ID = "item_390"
    NAME = "Hyperion Legendary Artifact #390"
    TYPE = "Weapon" if 390 % 2 == 0 else "Armor"
    RARITY = "Epic" if 390 % 5 == 0 else "Legendary"
    BASE_VALUE = 19500
    ATTACK_BONUS = 1170
    DEFENSE_BONUS = 780
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 390."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_390.ITEM_ID, "name": ItemDefinition_390.NAME, "atk": ItemDefinition_390.ATTACK_BONUS, "def": ItemDefinition_390.DEFENSE_BONUS}


class ItemDefinition_391:
    ITEM_ID = "item_391"
    NAME = "Hyperion Legendary Artifact #391"
    TYPE = "Weapon" if 391 % 2 == 0 else "Armor"
    RARITY = "Epic" if 391 % 5 == 0 else "Legendary"
    BASE_VALUE = 19550
    ATTACK_BONUS = 1173
    DEFENSE_BONUS = 782
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 391."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_391.ITEM_ID, "name": ItemDefinition_391.NAME, "atk": ItemDefinition_391.ATTACK_BONUS, "def": ItemDefinition_391.DEFENSE_BONUS}


class ItemDefinition_392:
    ITEM_ID = "item_392"
    NAME = "Hyperion Legendary Artifact #392"
    TYPE = "Weapon" if 392 % 2 == 0 else "Armor"
    RARITY = "Epic" if 392 % 5 == 0 else "Legendary"
    BASE_VALUE = 19600
    ATTACK_BONUS = 1176
    DEFENSE_BONUS = 784
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 392."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_392.ITEM_ID, "name": ItemDefinition_392.NAME, "atk": ItemDefinition_392.ATTACK_BONUS, "def": ItemDefinition_392.DEFENSE_BONUS}


class ItemDefinition_393:
    ITEM_ID = "item_393"
    NAME = "Hyperion Legendary Artifact #393"
    TYPE = "Weapon" if 393 % 2 == 0 else "Armor"
    RARITY = "Epic" if 393 % 5 == 0 else "Legendary"
    BASE_VALUE = 19650
    ATTACK_BONUS = 1179
    DEFENSE_BONUS = 786
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 393."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_393.ITEM_ID, "name": ItemDefinition_393.NAME, "atk": ItemDefinition_393.ATTACK_BONUS, "def": ItemDefinition_393.DEFENSE_BONUS}


class ItemDefinition_394:
    ITEM_ID = "item_394"
    NAME = "Hyperion Legendary Artifact #394"
    TYPE = "Weapon" if 394 % 2 == 0 else "Armor"
    RARITY = "Epic" if 394 % 5 == 0 else "Legendary"
    BASE_VALUE = 19700
    ATTACK_BONUS = 1182
    DEFENSE_BONUS = 788
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 394."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_394.ITEM_ID, "name": ItemDefinition_394.NAME, "atk": ItemDefinition_394.ATTACK_BONUS, "def": ItemDefinition_394.DEFENSE_BONUS}


class ItemDefinition_395:
    ITEM_ID = "item_395"
    NAME = "Hyperion Legendary Artifact #395"
    TYPE = "Weapon" if 395 % 2 == 0 else "Armor"
    RARITY = "Epic" if 395 % 5 == 0 else "Legendary"
    BASE_VALUE = 19750
    ATTACK_BONUS = 1185
    DEFENSE_BONUS = 790
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 395."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_395.ITEM_ID, "name": ItemDefinition_395.NAME, "atk": ItemDefinition_395.ATTACK_BONUS, "def": ItemDefinition_395.DEFENSE_BONUS}


class ItemDefinition_396:
    ITEM_ID = "item_396"
    NAME = "Hyperion Legendary Artifact #396"
    TYPE = "Weapon" if 396 % 2 == 0 else "Armor"
    RARITY = "Epic" if 396 % 5 == 0 else "Legendary"
    BASE_VALUE = 19800
    ATTACK_BONUS = 1188
    DEFENSE_BONUS = 792
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 396."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_396.ITEM_ID, "name": ItemDefinition_396.NAME, "atk": ItemDefinition_396.ATTACK_BONUS, "def": ItemDefinition_396.DEFENSE_BONUS}


class ItemDefinition_397:
    ITEM_ID = "item_397"
    NAME = "Hyperion Legendary Artifact #397"
    TYPE = "Weapon" if 397 % 2 == 0 else "Armor"
    RARITY = "Epic" if 397 % 5 == 0 else "Legendary"
    BASE_VALUE = 19850
    ATTACK_BONUS = 1191
    DEFENSE_BONUS = 794
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 397."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_397.ITEM_ID, "name": ItemDefinition_397.NAME, "atk": ItemDefinition_397.ATTACK_BONUS, "def": ItemDefinition_397.DEFENSE_BONUS}


class ItemDefinition_398:
    ITEM_ID = "item_398"
    NAME = "Hyperion Legendary Artifact #398"
    TYPE = "Weapon" if 398 % 2 == 0 else "Armor"
    RARITY = "Epic" if 398 % 5 == 0 else "Legendary"
    BASE_VALUE = 19900
    ATTACK_BONUS = 1194
    DEFENSE_BONUS = 796
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 398."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_398.ITEM_ID, "name": ItemDefinition_398.NAME, "atk": ItemDefinition_398.ATTACK_BONUS, "def": ItemDefinition_398.DEFENSE_BONUS}


class ItemDefinition_399:
    ITEM_ID = "item_399"
    NAME = "Hyperion Legendary Artifact #399"
    TYPE = "Weapon" if 399 % 2 == 0 else "Armor"
    RARITY = "Epic" if 399 % 5 == 0 else "Legendary"
    BASE_VALUE = 19950
    ATTACK_BONUS = 1197
    DEFENSE_BONUS = 798
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 399."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_399.ITEM_ID, "name": ItemDefinition_399.NAME, "atk": ItemDefinition_399.ATTACK_BONUS, "def": ItemDefinition_399.DEFENSE_BONUS}


class ItemDefinition_400:
    ITEM_ID = "item_400"
    NAME = "Hyperion Legendary Artifact #400"
    TYPE = "Weapon" if 400 % 2 == 0 else "Armor"
    RARITY = "Epic" if 400 % 5 == 0 else "Legendary"
    BASE_VALUE = 20000
    ATTACK_BONUS = 1200
    DEFENSE_BONUS = 800
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 400."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_400.ITEM_ID, "name": ItemDefinition_400.NAME, "atk": ItemDefinition_400.ATTACK_BONUS, "def": ItemDefinition_400.DEFENSE_BONUS}


class ItemDefinition_401:
    ITEM_ID = "item_401"
    NAME = "Hyperion Legendary Artifact #401"
    TYPE = "Weapon" if 401 % 2 == 0 else "Armor"
    RARITY = "Epic" if 401 % 5 == 0 else "Legendary"
    BASE_VALUE = 20050
    ATTACK_BONUS = 1203
    DEFENSE_BONUS = 802
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 401."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_401.ITEM_ID, "name": ItemDefinition_401.NAME, "atk": ItemDefinition_401.ATTACK_BONUS, "def": ItemDefinition_401.DEFENSE_BONUS}


class ItemDefinition_402:
    ITEM_ID = "item_402"
    NAME = "Hyperion Legendary Artifact #402"
    TYPE = "Weapon" if 402 % 2 == 0 else "Armor"
    RARITY = "Epic" if 402 % 5 == 0 else "Legendary"
    BASE_VALUE = 20100
    ATTACK_BONUS = 1206
    DEFENSE_BONUS = 804
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 402."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_402.ITEM_ID, "name": ItemDefinition_402.NAME, "atk": ItemDefinition_402.ATTACK_BONUS, "def": ItemDefinition_402.DEFENSE_BONUS}


class ItemDefinition_403:
    ITEM_ID = "item_403"
    NAME = "Hyperion Legendary Artifact #403"
    TYPE = "Weapon" if 403 % 2 == 0 else "Armor"
    RARITY = "Epic" if 403 % 5 == 0 else "Legendary"
    BASE_VALUE = 20150
    ATTACK_BONUS = 1209
    DEFENSE_BONUS = 806
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 403."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_403.ITEM_ID, "name": ItemDefinition_403.NAME, "atk": ItemDefinition_403.ATTACK_BONUS, "def": ItemDefinition_403.DEFENSE_BONUS}


class ItemDefinition_404:
    ITEM_ID = "item_404"
    NAME = "Hyperion Legendary Artifact #404"
    TYPE = "Weapon" if 404 % 2 == 0 else "Armor"
    RARITY = "Epic" if 404 % 5 == 0 else "Legendary"
    BASE_VALUE = 20200
    ATTACK_BONUS = 1212
    DEFENSE_BONUS = 808
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 404."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_404.ITEM_ID, "name": ItemDefinition_404.NAME, "atk": ItemDefinition_404.ATTACK_BONUS, "def": ItemDefinition_404.DEFENSE_BONUS}


class ItemDefinition_405:
    ITEM_ID = "item_405"
    NAME = "Hyperion Legendary Artifact #405"
    TYPE = "Weapon" if 405 % 2 == 0 else "Armor"
    RARITY = "Epic" if 405 % 5 == 0 else "Legendary"
    BASE_VALUE = 20250
    ATTACK_BONUS = 1215
    DEFENSE_BONUS = 810
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 405."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_405.ITEM_ID, "name": ItemDefinition_405.NAME, "atk": ItemDefinition_405.ATTACK_BONUS, "def": ItemDefinition_405.DEFENSE_BONUS}


class ItemDefinition_406:
    ITEM_ID = "item_406"
    NAME = "Hyperion Legendary Artifact #406"
    TYPE = "Weapon" if 406 % 2 == 0 else "Armor"
    RARITY = "Epic" if 406 % 5 == 0 else "Legendary"
    BASE_VALUE = 20300
    ATTACK_BONUS = 1218
    DEFENSE_BONUS = 812
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 406."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_406.ITEM_ID, "name": ItemDefinition_406.NAME, "atk": ItemDefinition_406.ATTACK_BONUS, "def": ItemDefinition_406.DEFENSE_BONUS}


class ItemDefinition_407:
    ITEM_ID = "item_407"
    NAME = "Hyperion Legendary Artifact #407"
    TYPE = "Weapon" if 407 % 2 == 0 else "Armor"
    RARITY = "Epic" if 407 % 5 == 0 else "Legendary"
    BASE_VALUE = 20350
    ATTACK_BONUS = 1221
    DEFENSE_BONUS = 814
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 407."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_407.ITEM_ID, "name": ItemDefinition_407.NAME, "atk": ItemDefinition_407.ATTACK_BONUS, "def": ItemDefinition_407.DEFENSE_BONUS}


class ItemDefinition_408:
    ITEM_ID = "item_408"
    NAME = "Hyperion Legendary Artifact #408"
    TYPE = "Weapon" if 408 % 2 == 0 else "Armor"
    RARITY = "Epic" if 408 % 5 == 0 else "Legendary"
    BASE_VALUE = 20400
    ATTACK_BONUS = 1224
    DEFENSE_BONUS = 816
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 408."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_408.ITEM_ID, "name": ItemDefinition_408.NAME, "atk": ItemDefinition_408.ATTACK_BONUS, "def": ItemDefinition_408.DEFENSE_BONUS}


class ItemDefinition_409:
    ITEM_ID = "item_409"
    NAME = "Hyperion Legendary Artifact #409"
    TYPE = "Weapon" if 409 % 2 == 0 else "Armor"
    RARITY = "Epic" if 409 % 5 == 0 else "Legendary"
    BASE_VALUE = 20450
    ATTACK_BONUS = 1227
    DEFENSE_BONUS = 818
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 409."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_409.ITEM_ID, "name": ItemDefinition_409.NAME, "atk": ItemDefinition_409.ATTACK_BONUS, "def": ItemDefinition_409.DEFENSE_BONUS}


class ItemDefinition_410:
    ITEM_ID = "item_410"
    NAME = "Hyperion Legendary Artifact #410"
    TYPE = "Weapon" if 410 % 2 == 0 else "Armor"
    RARITY = "Epic" if 410 % 5 == 0 else "Legendary"
    BASE_VALUE = 20500
    ATTACK_BONUS = 1230
    DEFENSE_BONUS = 820
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 410."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_410.ITEM_ID, "name": ItemDefinition_410.NAME, "atk": ItemDefinition_410.ATTACK_BONUS, "def": ItemDefinition_410.DEFENSE_BONUS}


class ItemDefinition_411:
    ITEM_ID = "item_411"
    NAME = "Hyperion Legendary Artifact #411"
    TYPE = "Weapon" if 411 % 2 == 0 else "Armor"
    RARITY = "Epic" if 411 % 5 == 0 else "Legendary"
    BASE_VALUE = 20550
    ATTACK_BONUS = 1233
    DEFENSE_BONUS = 822
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 411."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_411.ITEM_ID, "name": ItemDefinition_411.NAME, "atk": ItemDefinition_411.ATTACK_BONUS, "def": ItemDefinition_411.DEFENSE_BONUS}


class ItemDefinition_412:
    ITEM_ID = "item_412"
    NAME = "Hyperion Legendary Artifact #412"
    TYPE = "Weapon" if 412 % 2 == 0 else "Armor"
    RARITY = "Epic" if 412 % 5 == 0 else "Legendary"
    BASE_VALUE = 20600
    ATTACK_BONUS = 1236
    DEFENSE_BONUS = 824
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 412."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_412.ITEM_ID, "name": ItemDefinition_412.NAME, "atk": ItemDefinition_412.ATTACK_BONUS, "def": ItemDefinition_412.DEFENSE_BONUS}


class ItemDefinition_413:
    ITEM_ID = "item_413"
    NAME = "Hyperion Legendary Artifact #413"
    TYPE = "Weapon" if 413 % 2 == 0 else "Armor"
    RARITY = "Epic" if 413 % 5 == 0 else "Legendary"
    BASE_VALUE = 20650
    ATTACK_BONUS = 1239
    DEFENSE_BONUS = 826
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 413."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_413.ITEM_ID, "name": ItemDefinition_413.NAME, "atk": ItemDefinition_413.ATTACK_BONUS, "def": ItemDefinition_413.DEFENSE_BONUS}


class ItemDefinition_414:
    ITEM_ID = "item_414"
    NAME = "Hyperion Legendary Artifact #414"
    TYPE = "Weapon" if 414 % 2 == 0 else "Armor"
    RARITY = "Epic" if 414 % 5 == 0 else "Legendary"
    BASE_VALUE = 20700
    ATTACK_BONUS = 1242
    DEFENSE_BONUS = 828
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 414."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_414.ITEM_ID, "name": ItemDefinition_414.NAME, "atk": ItemDefinition_414.ATTACK_BONUS, "def": ItemDefinition_414.DEFENSE_BONUS}


class ItemDefinition_415:
    ITEM_ID = "item_415"
    NAME = "Hyperion Legendary Artifact #415"
    TYPE = "Weapon" if 415 % 2 == 0 else "Armor"
    RARITY = "Epic" if 415 % 5 == 0 else "Legendary"
    BASE_VALUE = 20750
    ATTACK_BONUS = 1245
    DEFENSE_BONUS = 830
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 415."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_415.ITEM_ID, "name": ItemDefinition_415.NAME, "atk": ItemDefinition_415.ATTACK_BONUS, "def": ItemDefinition_415.DEFENSE_BONUS}


class ItemDefinition_416:
    ITEM_ID = "item_416"
    NAME = "Hyperion Legendary Artifact #416"
    TYPE = "Weapon" if 416 % 2 == 0 else "Armor"
    RARITY = "Epic" if 416 % 5 == 0 else "Legendary"
    BASE_VALUE = 20800
    ATTACK_BONUS = 1248
    DEFENSE_BONUS = 832
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 416."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_416.ITEM_ID, "name": ItemDefinition_416.NAME, "atk": ItemDefinition_416.ATTACK_BONUS, "def": ItemDefinition_416.DEFENSE_BONUS}


class ItemDefinition_417:
    ITEM_ID = "item_417"
    NAME = "Hyperion Legendary Artifact #417"
    TYPE = "Weapon" if 417 % 2 == 0 else "Armor"
    RARITY = "Epic" if 417 % 5 == 0 else "Legendary"
    BASE_VALUE = 20850
    ATTACK_BONUS = 1251
    DEFENSE_BONUS = 834
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 417."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_417.ITEM_ID, "name": ItemDefinition_417.NAME, "atk": ItemDefinition_417.ATTACK_BONUS, "def": ItemDefinition_417.DEFENSE_BONUS}


class ItemDefinition_418:
    ITEM_ID = "item_418"
    NAME = "Hyperion Legendary Artifact #418"
    TYPE = "Weapon" if 418 % 2 == 0 else "Armor"
    RARITY = "Epic" if 418 % 5 == 0 else "Legendary"
    BASE_VALUE = 20900
    ATTACK_BONUS = 1254
    DEFENSE_BONUS = 836
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 418."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_418.ITEM_ID, "name": ItemDefinition_418.NAME, "atk": ItemDefinition_418.ATTACK_BONUS, "def": ItemDefinition_418.DEFENSE_BONUS}


class ItemDefinition_419:
    ITEM_ID = "item_419"
    NAME = "Hyperion Legendary Artifact #419"
    TYPE = "Weapon" if 419 % 2 == 0 else "Armor"
    RARITY = "Epic" if 419 % 5 == 0 else "Legendary"
    BASE_VALUE = 20950
    ATTACK_BONUS = 1257
    DEFENSE_BONUS = 838
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 419."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_419.ITEM_ID, "name": ItemDefinition_419.NAME, "atk": ItemDefinition_419.ATTACK_BONUS, "def": ItemDefinition_419.DEFENSE_BONUS}


class ItemDefinition_420:
    ITEM_ID = "item_420"
    NAME = "Hyperion Legendary Artifact #420"
    TYPE = "Weapon" if 420 % 2 == 0 else "Armor"
    RARITY = "Epic" if 420 % 5 == 0 else "Legendary"
    BASE_VALUE = 21000
    ATTACK_BONUS = 1260
    DEFENSE_BONUS = 840
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 420."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_420.ITEM_ID, "name": ItemDefinition_420.NAME, "atk": ItemDefinition_420.ATTACK_BONUS, "def": ItemDefinition_420.DEFENSE_BONUS}


class ItemDefinition_421:
    ITEM_ID = "item_421"
    NAME = "Hyperion Legendary Artifact #421"
    TYPE = "Weapon" if 421 % 2 == 0 else "Armor"
    RARITY = "Epic" if 421 % 5 == 0 else "Legendary"
    BASE_VALUE = 21050
    ATTACK_BONUS = 1263
    DEFENSE_BONUS = 842
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 421."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_421.ITEM_ID, "name": ItemDefinition_421.NAME, "atk": ItemDefinition_421.ATTACK_BONUS, "def": ItemDefinition_421.DEFENSE_BONUS}


class ItemDefinition_422:
    ITEM_ID = "item_422"
    NAME = "Hyperion Legendary Artifact #422"
    TYPE = "Weapon" if 422 % 2 == 0 else "Armor"
    RARITY = "Epic" if 422 % 5 == 0 else "Legendary"
    BASE_VALUE = 21100
    ATTACK_BONUS = 1266
    DEFENSE_BONUS = 844
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 422."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_422.ITEM_ID, "name": ItemDefinition_422.NAME, "atk": ItemDefinition_422.ATTACK_BONUS, "def": ItemDefinition_422.DEFENSE_BONUS}


class ItemDefinition_423:
    ITEM_ID = "item_423"
    NAME = "Hyperion Legendary Artifact #423"
    TYPE = "Weapon" if 423 % 2 == 0 else "Armor"
    RARITY = "Epic" if 423 % 5 == 0 else "Legendary"
    BASE_VALUE = 21150
    ATTACK_BONUS = 1269
    DEFENSE_BONUS = 846
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 423."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_423.ITEM_ID, "name": ItemDefinition_423.NAME, "atk": ItemDefinition_423.ATTACK_BONUS, "def": ItemDefinition_423.DEFENSE_BONUS}


class ItemDefinition_424:
    ITEM_ID = "item_424"
    NAME = "Hyperion Legendary Artifact #424"
    TYPE = "Weapon" if 424 % 2 == 0 else "Armor"
    RARITY = "Epic" if 424 % 5 == 0 else "Legendary"
    BASE_VALUE = 21200
    ATTACK_BONUS = 1272
    DEFENSE_BONUS = 848
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 424."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_424.ITEM_ID, "name": ItemDefinition_424.NAME, "atk": ItemDefinition_424.ATTACK_BONUS, "def": ItemDefinition_424.DEFENSE_BONUS}


class ItemDefinition_425:
    ITEM_ID = "item_425"
    NAME = "Hyperion Legendary Artifact #425"
    TYPE = "Weapon" if 425 % 2 == 0 else "Armor"
    RARITY = "Epic" if 425 % 5 == 0 else "Legendary"
    BASE_VALUE = 21250
    ATTACK_BONUS = 1275
    DEFENSE_BONUS = 850
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 425."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_425.ITEM_ID, "name": ItemDefinition_425.NAME, "atk": ItemDefinition_425.ATTACK_BONUS, "def": ItemDefinition_425.DEFENSE_BONUS}


class ItemDefinition_426:
    ITEM_ID = "item_426"
    NAME = "Hyperion Legendary Artifact #426"
    TYPE = "Weapon" if 426 % 2 == 0 else "Armor"
    RARITY = "Epic" if 426 % 5 == 0 else "Legendary"
    BASE_VALUE = 21300
    ATTACK_BONUS = 1278
    DEFENSE_BONUS = 852
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 426."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_426.ITEM_ID, "name": ItemDefinition_426.NAME, "atk": ItemDefinition_426.ATTACK_BONUS, "def": ItemDefinition_426.DEFENSE_BONUS}


class ItemDefinition_427:
    ITEM_ID = "item_427"
    NAME = "Hyperion Legendary Artifact #427"
    TYPE = "Weapon" if 427 % 2 == 0 else "Armor"
    RARITY = "Epic" if 427 % 5 == 0 else "Legendary"
    BASE_VALUE = 21350
    ATTACK_BONUS = 1281
    DEFENSE_BONUS = 854
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 427."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_427.ITEM_ID, "name": ItemDefinition_427.NAME, "atk": ItemDefinition_427.ATTACK_BONUS, "def": ItemDefinition_427.DEFENSE_BONUS}


class ItemDefinition_428:
    ITEM_ID = "item_428"
    NAME = "Hyperion Legendary Artifact #428"
    TYPE = "Weapon" if 428 % 2 == 0 else "Armor"
    RARITY = "Epic" if 428 % 5 == 0 else "Legendary"
    BASE_VALUE = 21400
    ATTACK_BONUS = 1284
    DEFENSE_BONUS = 856
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 428."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_428.ITEM_ID, "name": ItemDefinition_428.NAME, "atk": ItemDefinition_428.ATTACK_BONUS, "def": ItemDefinition_428.DEFENSE_BONUS}


class ItemDefinition_429:
    ITEM_ID = "item_429"
    NAME = "Hyperion Legendary Artifact #429"
    TYPE = "Weapon" if 429 % 2 == 0 else "Armor"
    RARITY = "Epic" if 429 % 5 == 0 else "Legendary"
    BASE_VALUE = 21450
    ATTACK_BONUS = 1287
    DEFENSE_BONUS = 858
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 429."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_429.ITEM_ID, "name": ItemDefinition_429.NAME, "atk": ItemDefinition_429.ATTACK_BONUS, "def": ItemDefinition_429.DEFENSE_BONUS}


class ItemDefinition_430:
    ITEM_ID = "item_430"
    NAME = "Hyperion Legendary Artifact #430"
    TYPE = "Weapon" if 430 % 2 == 0 else "Armor"
    RARITY = "Epic" if 430 % 5 == 0 else "Legendary"
    BASE_VALUE = 21500
    ATTACK_BONUS = 1290
    DEFENSE_BONUS = 860
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 430."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_430.ITEM_ID, "name": ItemDefinition_430.NAME, "atk": ItemDefinition_430.ATTACK_BONUS, "def": ItemDefinition_430.DEFENSE_BONUS}


class ItemDefinition_431:
    ITEM_ID = "item_431"
    NAME = "Hyperion Legendary Artifact #431"
    TYPE = "Weapon" if 431 % 2 == 0 else "Armor"
    RARITY = "Epic" if 431 % 5 == 0 else "Legendary"
    BASE_VALUE = 21550
    ATTACK_BONUS = 1293
    DEFENSE_BONUS = 862
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 431."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_431.ITEM_ID, "name": ItemDefinition_431.NAME, "atk": ItemDefinition_431.ATTACK_BONUS, "def": ItemDefinition_431.DEFENSE_BONUS}


class ItemDefinition_432:
    ITEM_ID = "item_432"
    NAME = "Hyperion Legendary Artifact #432"
    TYPE = "Weapon" if 432 % 2 == 0 else "Armor"
    RARITY = "Epic" if 432 % 5 == 0 else "Legendary"
    BASE_VALUE = 21600
    ATTACK_BONUS = 1296
    DEFENSE_BONUS = 864
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 432."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_432.ITEM_ID, "name": ItemDefinition_432.NAME, "atk": ItemDefinition_432.ATTACK_BONUS, "def": ItemDefinition_432.DEFENSE_BONUS}


class ItemDefinition_433:
    ITEM_ID = "item_433"
    NAME = "Hyperion Legendary Artifact #433"
    TYPE = "Weapon" if 433 % 2 == 0 else "Armor"
    RARITY = "Epic" if 433 % 5 == 0 else "Legendary"
    BASE_VALUE = 21650
    ATTACK_BONUS = 1299
    DEFENSE_BONUS = 866
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 433."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_433.ITEM_ID, "name": ItemDefinition_433.NAME, "atk": ItemDefinition_433.ATTACK_BONUS, "def": ItemDefinition_433.DEFENSE_BONUS}


class ItemDefinition_434:
    ITEM_ID = "item_434"
    NAME = "Hyperion Legendary Artifact #434"
    TYPE = "Weapon" if 434 % 2 == 0 else "Armor"
    RARITY = "Epic" if 434 % 5 == 0 else "Legendary"
    BASE_VALUE = 21700
    ATTACK_BONUS = 1302
    DEFENSE_BONUS = 868
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 434."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_434.ITEM_ID, "name": ItemDefinition_434.NAME, "atk": ItemDefinition_434.ATTACK_BONUS, "def": ItemDefinition_434.DEFENSE_BONUS}


class ItemDefinition_435:
    ITEM_ID = "item_435"
    NAME = "Hyperion Legendary Artifact #435"
    TYPE = "Weapon" if 435 % 2 == 0 else "Armor"
    RARITY = "Epic" if 435 % 5 == 0 else "Legendary"
    BASE_VALUE = 21750
    ATTACK_BONUS = 1305
    DEFENSE_BONUS = 870
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 435."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_435.ITEM_ID, "name": ItemDefinition_435.NAME, "atk": ItemDefinition_435.ATTACK_BONUS, "def": ItemDefinition_435.DEFENSE_BONUS}


class ItemDefinition_436:
    ITEM_ID = "item_436"
    NAME = "Hyperion Legendary Artifact #436"
    TYPE = "Weapon" if 436 % 2 == 0 else "Armor"
    RARITY = "Epic" if 436 % 5 == 0 else "Legendary"
    BASE_VALUE = 21800
    ATTACK_BONUS = 1308
    DEFENSE_BONUS = 872
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 436."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_436.ITEM_ID, "name": ItemDefinition_436.NAME, "atk": ItemDefinition_436.ATTACK_BONUS, "def": ItemDefinition_436.DEFENSE_BONUS}


class ItemDefinition_437:
    ITEM_ID = "item_437"
    NAME = "Hyperion Legendary Artifact #437"
    TYPE = "Weapon" if 437 % 2 == 0 else "Armor"
    RARITY = "Epic" if 437 % 5 == 0 else "Legendary"
    BASE_VALUE = 21850
    ATTACK_BONUS = 1311
    DEFENSE_BONUS = 874
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 437."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_437.ITEM_ID, "name": ItemDefinition_437.NAME, "atk": ItemDefinition_437.ATTACK_BONUS, "def": ItemDefinition_437.DEFENSE_BONUS}


class ItemDefinition_438:
    ITEM_ID = "item_438"
    NAME = "Hyperion Legendary Artifact #438"
    TYPE = "Weapon" if 438 % 2 == 0 else "Armor"
    RARITY = "Epic" if 438 % 5 == 0 else "Legendary"
    BASE_VALUE = 21900
    ATTACK_BONUS = 1314
    DEFENSE_BONUS = 876
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 438."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_438.ITEM_ID, "name": ItemDefinition_438.NAME, "atk": ItemDefinition_438.ATTACK_BONUS, "def": ItemDefinition_438.DEFENSE_BONUS}


class ItemDefinition_439:
    ITEM_ID = "item_439"
    NAME = "Hyperion Legendary Artifact #439"
    TYPE = "Weapon" if 439 % 2 == 0 else "Armor"
    RARITY = "Epic" if 439 % 5 == 0 else "Legendary"
    BASE_VALUE = 21950
    ATTACK_BONUS = 1317
    DEFENSE_BONUS = 878
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 439."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_439.ITEM_ID, "name": ItemDefinition_439.NAME, "atk": ItemDefinition_439.ATTACK_BONUS, "def": ItemDefinition_439.DEFENSE_BONUS}


class ItemDefinition_440:
    ITEM_ID = "item_440"
    NAME = "Hyperion Legendary Artifact #440"
    TYPE = "Weapon" if 440 % 2 == 0 else "Armor"
    RARITY = "Epic" if 440 % 5 == 0 else "Legendary"
    BASE_VALUE = 22000
    ATTACK_BONUS = 1320
    DEFENSE_BONUS = 880
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 440."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_440.ITEM_ID, "name": ItemDefinition_440.NAME, "atk": ItemDefinition_440.ATTACK_BONUS, "def": ItemDefinition_440.DEFENSE_BONUS}


class ItemDefinition_441:
    ITEM_ID = "item_441"
    NAME = "Hyperion Legendary Artifact #441"
    TYPE = "Weapon" if 441 % 2 == 0 else "Armor"
    RARITY = "Epic" if 441 % 5 == 0 else "Legendary"
    BASE_VALUE = 22050
    ATTACK_BONUS = 1323
    DEFENSE_BONUS = 882
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 441."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_441.ITEM_ID, "name": ItemDefinition_441.NAME, "atk": ItemDefinition_441.ATTACK_BONUS, "def": ItemDefinition_441.DEFENSE_BONUS}


class ItemDefinition_442:
    ITEM_ID = "item_442"
    NAME = "Hyperion Legendary Artifact #442"
    TYPE = "Weapon" if 442 % 2 == 0 else "Armor"
    RARITY = "Epic" if 442 % 5 == 0 else "Legendary"
    BASE_VALUE = 22100
    ATTACK_BONUS = 1326
    DEFENSE_BONUS = 884
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 442."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_442.ITEM_ID, "name": ItemDefinition_442.NAME, "atk": ItemDefinition_442.ATTACK_BONUS, "def": ItemDefinition_442.DEFENSE_BONUS}


class ItemDefinition_443:
    ITEM_ID = "item_443"
    NAME = "Hyperion Legendary Artifact #443"
    TYPE = "Weapon" if 443 % 2 == 0 else "Armor"
    RARITY = "Epic" if 443 % 5 == 0 else "Legendary"
    BASE_VALUE = 22150
    ATTACK_BONUS = 1329
    DEFENSE_BONUS = 886
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 443."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_443.ITEM_ID, "name": ItemDefinition_443.NAME, "atk": ItemDefinition_443.ATTACK_BONUS, "def": ItemDefinition_443.DEFENSE_BONUS}


class ItemDefinition_444:
    ITEM_ID = "item_444"
    NAME = "Hyperion Legendary Artifact #444"
    TYPE = "Weapon" if 444 % 2 == 0 else "Armor"
    RARITY = "Epic" if 444 % 5 == 0 else "Legendary"
    BASE_VALUE = 22200
    ATTACK_BONUS = 1332
    DEFENSE_BONUS = 888
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 444."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_444.ITEM_ID, "name": ItemDefinition_444.NAME, "atk": ItemDefinition_444.ATTACK_BONUS, "def": ItemDefinition_444.DEFENSE_BONUS}


class ItemDefinition_445:
    ITEM_ID = "item_445"
    NAME = "Hyperion Legendary Artifact #445"
    TYPE = "Weapon" if 445 % 2 == 0 else "Armor"
    RARITY = "Epic" if 445 % 5 == 0 else "Legendary"
    BASE_VALUE = 22250
    ATTACK_BONUS = 1335
    DEFENSE_BONUS = 890
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 445."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_445.ITEM_ID, "name": ItemDefinition_445.NAME, "atk": ItemDefinition_445.ATTACK_BONUS, "def": ItemDefinition_445.DEFENSE_BONUS}


class ItemDefinition_446:
    ITEM_ID = "item_446"
    NAME = "Hyperion Legendary Artifact #446"
    TYPE = "Weapon" if 446 % 2 == 0 else "Armor"
    RARITY = "Epic" if 446 % 5 == 0 else "Legendary"
    BASE_VALUE = 22300
    ATTACK_BONUS = 1338
    DEFENSE_BONUS = 892
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 446."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_446.ITEM_ID, "name": ItemDefinition_446.NAME, "atk": ItemDefinition_446.ATTACK_BONUS, "def": ItemDefinition_446.DEFENSE_BONUS}


class ItemDefinition_447:
    ITEM_ID = "item_447"
    NAME = "Hyperion Legendary Artifact #447"
    TYPE = "Weapon" if 447 % 2 == 0 else "Armor"
    RARITY = "Epic" if 447 % 5 == 0 else "Legendary"
    BASE_VALUE = 22350
    ATTACK_BONUS = 1341
    DEFENSE_BONUS = 894
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 447."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_447.ITEM_ID, "name": ItemDefinition_447.NAME, "atk": ItemDefinition_447.ATTACK_BONUS, "def": ItemDefinition_447.DEFENSE_BONUS}


class ItemDefinition_448:
    ITEM_ID = "item_448"
    NAME = "Hyperion Legendary Artifact #448"
    TYPE = "Weapon" if 448 % 2 == 0 else "Armor"
    RARITY = "Epic" if 448 % 5 == 0 else "Legendary"
    BASE_VALUE = 22400
    ATTACK_BONUS = 1344
    DEFENSE_BONUS = 896
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 448."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_448.ITEM_ID, "name": ItemDefinition_448.NAME, "atk": ItemDefinition_448.ATTACK_BONUS, "def": ItemDefinition_448.DEFENSE_BONUS}


class ItemDefinition_449:
    ITEM_ID = "item_449"
    NAME = "Hyperion Legendary Artifact #449"
    TYPE = "Weapon" if 449 % 2 == 0 else "Armor"
    RARITY = "Epic" if 449 % 5 == 0 else "Legendary"
    BASE_VALUE = 22450
    ATTACK_BONUS = 1347
    DEFENSE_BONUS = 898
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 449."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_449.ITEM_ID, "name": ItemDefinition_449.NAME, "atk": ItemDefinition_449.ATTACK_BONUS, "def": ItemDefinition_449.DEFENSE_BONUS}


class ItemDefinition_450:
    ITEM_ID = "item_450"
    NAME = "Hyperion Legendary Artifact #450"
    TYPE = "Weapon" if 450 % 2 == 0 else "Armor"
    RARITY = "Epic" if 450 % 5 == 0 else "Legendary"
    BASE_VALUE = 22500
    ATTACK_BONUS = 1350
    DEFENSE_BONUS = 900
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 450."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_450.ITEM_ID, "name": ItemDefinition_450.NAME, "atk": ItemDefinition_450.ATTACK_BONUS, "def": ItemDefinition_450.DEFENSE_BONUS}


class ItemDefinition_451:
    ITEM_ID = "item_451"
    NAME = "Hyperion Legendary Artifact #451"
    TYPE = "Weapon" if 451 % 2 == 0 else "Armor"
    RARITY = "Epic" if 451 % 5 == 0 else "Legendary"
    BASE_VALUE = 22550
    ATTACK_BONUS = 1353
    DEFENSE_BONUS = 902
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 451."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_451.ITEM_ID, "name": ItemDefinition_451.NAME, "atk": ItemDefinition_451.ATTACK_BONUS, "def": ItemDefinition_451.DEFENSE_BONUS}


class ItemDefinition_452:
    ITEM_ID = "item_452"
    NAME = "Hyperion Legendary Artifact #452"
    TYPE = "Weapon" if 452 % 2 == 0 else "Armor"
    RARITY = "Epic" if 452 % 5 == 0 else "Legendary"
    BASE_VALUE = 22600
    ATTACK_BONUS = 1356
    DEFENSE_BONUS = 904
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 452."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_452.ITEM_ID, "name": ItemDefinition_452.NAME, "atk": ItemDefinition_452.ATTACK_BONUS, "def": ItemDefinition_452.DEFENSE_BONUS}


class ItemDefinition_453:
    ITEM_ID = "item_453"
    NAME = "Hyperion Legendary Artifact #453"
    TYPE = "Weapon" if 453 % 2 == 0 else "Armor"
    RARITY = "Epic" if 453 % 5 == 0 else "Legendary"
    BASE_VALUE = 22650
    ATTACK_BONUS = 1359
    DEFENSE_BONUS = 906
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 453."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_453.ITEM_ID, "name": ItemDefinition_453.NAME, "atk": ItemDefinition_453.ATTACK_BONUS, "def": ItemDefinition_453.DEFENSE_BONUS}


class ItemDefinition_454:
    ITEM_ID = "item_454"
    NAME = "Hyperion Legendary Artifact #454"
    TYPE = "Weapon" if 454 % 2 == 0 else "Armor"
    RARITY = "Epic" if 454 % 5 == 0 else "Legendary"
    BASE_VALUE = 22700
    ATTACK_BONUS = 1362
    DEFENSE_BONUS = 908
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 454."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_454.ITEM_ID, "name": ItemDefinition_454.NAME, "atk": ItemDefinition_454.ATTACK_BONUS, "def": ItemDefinition_454.DEFENSE_BONUS}


class ItemDefinition_455:
    ITEM_ID = "item_455"
    NAME = "Hyperion Legendary Artifact #455"
    TYPE = "Weapon" if 455 % 2 == 0 else "Armor"
    RARITY = "Epic" if 455 % 5 == 0 else "Legendary"
    BASE_VALUE = 22750
    ATTACK_BONUS = 1365
    DEFENSE_BONUS = 910
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 455."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_455.ITEM_ID, "name": ItemDefinition_455.NAME, "atk": ItemDefinition_455.ATTACK_BONUS, "def": ItemDefinition_455.DEFENSE_BONUS}


class ItemDefinition_456:
    ITEM_ID = "item_456"
    NAME = "Hyperion Legendary Artifact #456"
    TYPE = "Weapon" if 456 % 2 == 0 else "Armor"
    RARITY = "Epic" if 456 % 5 == 0 else "Legendary"
    BASE_VALUE = 22800
    ATTACK_BONUS = 1368
    DEFENSE_BONUS = 912
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 456."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_456.ITEM_ID, "name": ItemDefinition_456.NAME, "atk": ItemDefinition_456.ATTACK_BONUS, "def": ItemDefinition_456.DEFENSE_BONUS}


class ItemDefinition_457:
    ITEM_ID = "item_457"
    NAME = "Hyperion Legendary Artifact #457"
    TYPE = "Weapon" if 457 % 2 == 0 else "Armor"
    RARITY = "Epic" if 457 % 5 == 0 else "Legendary"
    BASE_VALUE = 22850
    ATTACK_BONUS = 1371
    DEFENSE_BONUS = 914
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 457."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_457.ITEM_ID, "name": ItemDefinition_457.NAME, "atk": ItemDefinition_457.ATTACK_BONUS, "def": ItemDefinition_457.DEFENSE_BONUS}


class ItemDefinition_458:
    ITEM_ID = "item_458"
    NAME = "Hyperion Legendary Artifact #458"
    TYPE = "Weapon" if 458 % 2 == 0 else "Armor"
    RARITY = "Epic" if 458 % 5 == 0 else "Legendary"
    BASE_VALUE = 22900
    ATTACK_BONUS = 1374
    DEFENSE_BONUS = 916
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 458."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_458.ITEM_ID, "name": ItemDefinition_458.NAME, "atk": ItemDefinition_458.ATTACK_BONUS, "def": ItemDefinition_458.DEFENSE_BONUS}


class ItemDefinition_459:
    ITEM_ID = "item_459"
    NAME = "Hyperion Legendary Artifact #459"
    TYPE = "Weapon" if 459 % 2 == 0 else "Armor"
    RARITY = "Epic" if 459 % 5 == 0 else "Legendary"
    BASE_VALUE = 22950
    ATTACK_BONUS = 1377
    DEFENSE_BONUS = 918
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 459."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_459.ITEM_ID, "name": ItemDefinition_459.NAME, "atk": ItemDefinition_459.ATTACK_BONUS, "def": ItemDefinition_459.DEFENSE_BONUS}


class ItemDefinition_460:
    ITEM_ID = "item_460"
    NAME = "Hyperion Legendary Artifact #460"
    TYPE = "Weapon" if 460 % 2 == 0 else "Armor"
    RARITY = "Epic" if 460 % 5 == 0 else "Legendary"
    BASE_VALUE = 23000
    ATTACK_BONUS = 1380
    DEFENSE_BONUS = 920
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 460."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_460.ITEM_ID, "name": ItemDefinition_460.NAME, "atk": ItemDefinition_460.ATTACK_BONUS, "def": ItemDefinition_460.DEFENSE_BONUS}


class ItemDefinition_461:
    ITEM_ID = "item_461"
    NAME = "Hyperion Legendary Artifact #461"
    TYPE = "Weapon" if 461 % 2 == 0 else "Armor"
    RARITY = "Epic" if 461 % 5 == 0 else "Legendary"
    BASE_VALUE = 23050
    ATTACK_BONUS = 1383
    DEFENSE_BONUS = 922
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 461."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_461.ITEM_ID, "name": ItemDefinition_461.NAME, "atk": ItemDefinition_461.ATTACK_BONUS, "def": ItemDefinition_461.DEFENSE_BONUS}


class ItemDefinition_462:
    ITEM_ID = "item_462"
    NAME = "Hyperion Legendary Artifact #462"
    TYPE = "Weapon" if 462 % 2 == 0 else "Armor"
    RARITY = "Epic" if 462 % 5 == 0 else "Legendary"
    BASE_VALUE = 23100
    ATTACK_BONUS = 1386
    DEFENSE_BONUS = 924
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 462."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_462.ITEM_ID, "name": ItemDefinition_462.NAME, "atk": ItemDefinition_462.ATTACK_BONUS, "def": ItemDefinition_462.DEFENSE_BONUS}


class ItemDefinition_463:
    ITEM_ID = "item_463"
    NAME = "Hyperion Legendary Artifact #463"
    TYPE = "Weapon" if 463 % 2 == 0 else "Armor"
    RARITY = "Epic" if 463 % 5 == 0 else "Legendary"
    BASE_VALUE = 23150
    ATTACK_BONUS = 1389
    DEFENSE_BONUS = 926
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 463."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_463.ITEM_ID, "name": ItemDefinition_463.NAME, "atk": ItemDefinition_463.ATTACK_BONUS, "def": ItemDefinition_463.DEFENSE_BONUS}


class ItemDefinition_464:
    ITEM_ID = "item_464"
    NAME = "Hyperion Legendary Artifact #464"
    TYPE = "Weapon" if 464 % 2 == 0 else "Armor"
    RARITY = "Epic" if 464 % 5 == 0 else "Legendary"
    BASE_VALUE = 23200
    ATTACK_BONUS = 1392
    DEFENSE_BONUS = 928
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 464."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_464.ITEM_ID, "name": ItemDefinition_464.NAME, "atk": ItemDefinition_464.ATTACK_BONUS, "def": ItemDefinition_464.DEFENSE_BONUS}


class ItemDefinition_465:
    ITEM_ID = "item_465"
    NAME = "Hyperion Legendary Artifact #465"
    TYPE = "Weapon" if 465 % 2 == 0 else "Armor"
    RARITY = "Epic" if 465 % 5 == 0 else "Legendary"
    BASE_VALUE = 23250
    ATTACK_BONUS = 1395
    DEFENSE_BONUS = 930
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 465."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_465.ITEM_ID, "name": ItemDefinition_465.NAME, "atk": ItemDefinition_465.ATTACK_BONUS, "def": ItemDefinition_465.DEFENSE_BONUS}


class ItemDefinition_466:
    ITEM_ID = "item_466"
    NAME = "Hyperion Legendary Artifact #466"
    TYPE = "Weapon" if 466 % 2 == 0 else "Armor"
    RARITY = "Epic" if 466 % 5 == 0 else "Legendary"
    BASE_VALUE = 23300
    ATTACK_BONUS = 1398
    DEFENSE_BONUS = 932
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 466."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_466.ITEM_ID, "name": ItemDefinition_466.NAME, "atk": ItemDefinition_466.ATTACK_BONUS, "def": ItemDefinition_466.DEFENSE_BONUS}


class ItemDefinition_467:
    ITEM_ID = "item_467"
    NAME = "Hyperion Legendary Artifact #467"
    TYPE = "Weapon" if 467 % 2 == 0 else "Armor"
    RARITY = "Epic" if 467 % 5 == 0 else "Legendary"
    BASE_VALUE = 23350
    ATTACK_BONUS = 1401
    DEFENSE_BONUS = 934
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 467."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_467.ITEM_ID, "name": ItemDefinition_467.NAME, "atk": ItemDefinition_467.ATTACK_BONUS, "def": ItemDefinition_467.DEFENSE_BONUS}


class ItemDefinition_468:
    ITEM_ID = "item_468"
    NAME = "Hyperion Legendary Artifact #468"
    TYPE = "Weapon" if 468 % 2 == 0 else "Armor"
    RARITY = "Epic" if 468 % 5 == 0 else "Legendary"
    BASE_VALUE = 23400
    ATTACK_BONUS = 1404
    DEFENSE_BONUS = 936
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 468."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_468.ITEM_ID, "name": ItemDefinition_468.NAME, "atk": ItemDefinition_468.ATTACK_BONUS, "def": ItemDefinition_468.DEFENSE_BONUS}


class ItemDefinition_469:
    ITEM_ID = "item_469"
    NAME = "Hyperion Legendary Artifact #469"
    TYPE = "Weapon" if 469 % 2 == 0 else "Armor"
    RARITY = "Epic" if 469 % 5 == 0 else "Legendary"
    BASE_VALUE = 23450
    ATTACK_BONUS = 1407
    DEFENSE_BONUS = 938
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 469."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_469.ITEM_ID, "name": ItemDefinition_469.NAME, "atk": ItemDefinition_469.ATTACK_BONUS, "def": ItemDefinition_469.DEFENSE_BONUS}


class ItemDefinition_470:
    ITEM_ID = "item_470"
    NAME = "Hyperion Legendary Artifact #470"
    TYPE = "Weapon" if 470 % 2 == 0 else "Armor"
    RARITY = "Epic" if 470 % 5 == 0 else "Legendary"
    BASE_VALUE = 23500
    ATTACK_BONUS = 1410
    DEFENSE_BONUS = 940
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 470."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_470.ITEM_ID, "name": ItemDefinition_470.NAME, "atk": ItemDefinition_470.ATTACK_BONUS, "def": ItemDefinition_470.DEFENSE_BONUS}


class ItemDefinition_471:
    ITEM_ID = "item_471"
    NAME = "Hyperion Legendary Artifact #471"
    TYPE = "Weapon" if 471 % 2 == 0 else "Armor"
    RARITY = "Epic" if 471 % 5 == 0 else "Legendary"
    BASE_VALUE = 23550
    ATTACK_BONUS = 1413
    DEFENSE_BONUS = 942
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 471."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_471.ITEM_ID, "name": ItemDefinition_471.NAME, "atk": ItemDefinition_471.ATTACK_BONUS, "def": ItemDefinition_471.DEFENSE_BONUS}


class ItemDefinition_472:
    ITEM_ID = "item_472"
    NAME = "Hyperion Legendary Artifact #472"
    TYPE = "Weapon" if 472 % 2 == 0 else "Armor"
    RARITY = "Epic" if 472 % 5 == 0 else "Legendary"
    BASE_VALUE = 23600
    ATTACK_BONUS = 1416
    DEFENSE_BONUS = 944
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 472."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_472.ITEM_ID, "name": ItemDefinition_472.NAME, "atk": ItemDefinition_472.ATTACK_BONUS, "def": ItemDefinition_472.DEFENSE_BONUS}


class ItemDefinition_473:
    ITEM_ID = "item_473"
    NAME = "Hyperion Legendary Artifact #473"
    TYPE = "Weapon" if 473 % 2 == 0 else "Armor"
    RARITY = "Epic" if 473 % 5 == 0 else "Legendary"
    BASE_VALUE = 23650
    ATTACK_BONUS = 1419
    DEFENSE_BONUS = 946
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 473."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_473.ITEM_ID, "name": ItemDefinition_473.NAME, "atk": ItemDefinition_473.ATTACK_BONUS, "def": ItemDefinition_473.DEFENSE_BONUS}


class ItemDefinition_474:
    ITEM_ID = "item_474"
    NAME = "Hyperion Legendary Artifact #474"
    TYPE = "Weapon" if 474 % 2 == 0 else "Armor"
    RARITY = "Epic" if 474 % 5 == 0 else "Legendary"
    BASE_VALUE = 23700
    ATTACK_BONUS = 1422
    DEFENSE_BONUS = 948
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 474."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_474.ITEM_ID, "name": ItemDefinition_474.NAME, "atk": ItemDefinition_474.ATTACK_BONUS, "def": ItemDefinition_474.DEFENSE_BONUS}


class ItemDefinition_475:
    ITEM_ID = "item_475"
    NAME = "Hyperion Legendary Artifact #475"
    TYPE = "Weapon" if 475 % 2 == 0 else "Armor"
    RARITY = "Epic" if 475 % 5 == 0 else "Legendary"
    BASE_VALUE = 23750
    ATTACK_BONUS = 1425
    DEFENSE_BONUS = 950
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 475."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_475.ITEM_ID, "name": ItemDefinition_475.NAME, "atk": ItemDefinition_475.ATTACK_BONUS, "def": ItemDefinition_475.DEFENSE_BONUS}


class ItemDefinition_476:
    ITEM_ID = "item_476"
    NAME = "Hyperion Legendary Artifact #476"
    TYPE = "Weapon" if 476 % 2 == 0 else "Armor"
    RARITY = "Epic" if 476 % 5 == 0 else "Legendary"
    BASE_VALUE = 23800
    ATTACK_BONUS = 1428
    DEFENSE_BONUS = 952
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 476."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_476.ITEM_ID, "name": ItemDefinition_476.NAME, "atk": ItemDefinition_476.ATTACK_BONUS, "def": ItemDefinition_476.DEFENSE_BONUS}


class ItemDefinition_477:
    ITEM_ID = "item_477"
    NAME = "Hyperion Legendary Artifact #477"
    TYPE = "Weapon" if 477 % 2 == 0 else "Armor"
    RARITY = "Epic" if 477 % 5 == 0 else "Legendary"
    BASE_VALUE = 23850
    ATTACK_BONUS = 1431
    DEFENSE_BONUS = 954
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 477."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_477.ITEM_ID, "name": ItemDefinition_477.NAME, "atk": ItemDefinition_477.ATTACK_BONUS, "def": ItemDefinition_477.DEFENSE_BONUS}


class ItemDefinition_478:
    ITEM_ID = "item_478"
    NAME = "Hyperion Legendary Artifact #478"
    TYPE = "Weapon" if 478 % 2 == 0 else "Armor"
    RARITY = "Epic" if 478 % 5 == 0 else "Legendary"
    BASE_VALUE = 23900
    ATTACK_BONUS = 1434
    DEFENSE_BONUS = 956
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 478."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_478.ITEM_ID, "name": ItemDefinition_478.NAME, "atk": ItemDefinition_478.ATTACK_BONUS, "def": ItemDefinition_478.DEFENSE_BONUS}


class ItemDefinition_479:
    ITEM_ID = "item_479"
    NAME = "Hyperion Legendary Artifact #479"
    TYPE = "Weapon" if 479 % 2 == 0 else "Armor"
    RARITY = "Epic" if 479 % 5 == 0 else "Legendary"
    BASE_VALUE = 23950
    ATTACK_BONUS = 1437
    DEFENSE_BONUS = 958
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 479."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_479.ITEM_ID, "name": ItemDefinition_479.NAME, "atk": ItemDefinition_479.ATTACK_BONUS, "def": ItemDefinition_479.DEFENSE_BONUS}


class ItemDefinition_480:
    ITEM_ID = "item_480"
    NAME = "Hyperion Legendary Artifact #480"
    TYPE = "Weapon" if 480 % 2 == 0 else "Armor"
    RARITY = "Epic" if 480 % 5 == 0 else "Legendary"
    BASE_VALUE = 24000
    ATTACK_BONUS = 1440
    DEFENSE_BONUS = 960
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 480."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_480.ITEM_ID, "name": ItemDefinition_480.NAME, "atk": ItemDefinition_480.ATTACK_BONUS, "def": ItemDefinition_480.DEFENSE_BONUS}


class ItemDefinition_481:
    ITEM_ID = "item_481"
    NAME = "Hyperion Legendary Artifact #481"
    TYPE = "Weapon" if 481 % 2 == 0 else "Armor"
    RARITY = "Epic" if 481 % 5 == 0 else "Legendary"
    BASE_VALUE = 24050
    ATTACK_BONUS = 1443
    DEFENSE_BONUS = 962
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 481."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_481.ITEM_ID, "name": ItemDefinition_481.NAME, "atk": ItemDefinition_481.ATTACK_BONUS, "def": ItemDefinition_481.DEFENSE_BONUS}


class ItemDefinition_482:
    ITEM_ID = "item_482"
    NAME = "Hyperion Legendary Artifact #482"
    TYPE = "Weapon" if 482 % 2 == 0 else "Armor"
    RARITY = "Epic" if 482 % 5 == 0 else "Legendary"
    BASE_VALUE = 24100
    ATTACK_BONUS = 1446
    DEFENSE_BONUS = 964
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 482."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_482.ITEM_ID, "name": ItemDefinition_482.NAME, "atk": ItemDefinition_482.ATTACK_BONUS, "def": ItemDefinition_482.DEFENSE_BONUS}


class ItemDefinition_483:
    ITEM_ID = "item_483"
    NAME = "Hyperion Legendary Artifact #483"
    TYPE = "Weapon" if 483 % 2 == 0 else "Armor"
    RARITY = "Epic" if 483 % 5 == 0 else "Legendary"
    BASE_VALUE = 24150
    ATTACK_BONUS = 1449
    DEFENSE_BONUS = 966
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 483."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_483.ITEM_ID, "name": ItemDefinition_483.NAME, "atk": ItemDefinition_483.ATTACK_BONUS, "def": ItemDefinition_483.DEFENSE_BONUS}


class ItemDefinition_484:
    ITEM_ID = "item_484"
    NAME = "Hyperion Legendary Artifact #484"
    TYPE = "Weapon" if 484 % 2 == 0 else "Armor"
    RARITY = "Epic" if 484 % 5 == 0 else "Legendary"
    BASE_VALUE = 24200
    ATTACK_BONUS = 1452
    DEFENSE_BONUS = 968
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 484."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_484.ITEM_ID, "name": ItemDefinition_484.NAME, "atk": ItemDefinition_484.ATTACK_BONUS, "def": ItemDefinition_484.DEFENSE_BONUS}


class ItemDefinition_485:
    ITEM_ID = "item_485"
    NAME = "Hyperion Legendary Artifact #485"
    TYPE = "Weapon" if 485 % 2 == 0 else "Armor"
    RARITY = "Epic" if 485 % 5 == 0 else "Legendary"
    BASE_VALUE = 24250
    ATTACK_BONUS = 1455
    DEFENSE_BONUS = 970
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 485."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_485.ITEM_ID, "name": ItemDefinition_485.NAME, "atk": ItemDefinition_485.ATTACK_BONUS, "def": ItemDefinition_485.DEFENSE_BONUS}


class ItemDefinition_486:
    ITEM_ID = "item_486"
    NAME = "Hyperion Legendary Artifact #486"
    TYPE = "Weapon" if 486 % 2 == 0 else "Armor"
    RARITY = "Epic" if 486 % 5 == 0 else "Legendary"
    BASE_VALUE = 24300
    ATTACK_BONUS = 1458
    DEFENSE_BONUS = 972
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 486."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_486.ITEM_ID, "name": ItemDefinition_486.NAME, "atk": ItemDefinition_486.ATTACK_BONUS, "def": ItemDefinition_486.DEFENSE_BONUS}


class ItemDefinition_487:
    ITEM_ID = "item_487"
    NAME = "Hyperion Legendary Artifact #487"
    TYPE = "Weapon" if 487 % 2 == 0 else "Armor"
    RARITY = "Epic" if 487 % 5 == 0 else "Legendary"
    BASE_VALUE = 24350
    ATTACK_BONUS = 1461
    DEFENSE_BONUS = 974
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 487."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_487.ITEM_ID, "name": ItemDefinition_487.NAME, "atk": ItemDefinition_487.ATTACK_BONUS, "def": ItemDefinition_487.DEFENSE_BONUS}


class ItemDefinition_488:
    ITEM_ID = "item_488"
    NAME = "Hyperion Legendary Artifact #488"
    TYPE = "Weapon" if 488 % 2 == 0 else "Armor"
    RARITY = "Epic" if 488 % 5 == 0 else "Legendary"
    BASE_VALUE = 24400
    ATTACK_BONUS = 1464
    DEFENSE_BONUS = 976
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 488."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_488.ITEM_ID, "name": ItemDefinition_488.NAME, "atk": ItemDefinition_488.ATTACK_BONUS, "def": ItemDefinition_488.DEFENSE_BONUS}


class ItemDefinition_489:
    ITEM_ID = "item_489"
    NAME = "Hyperion Legendary Artifact #489"
    TYPE = "Weapon" if 489 % 2 == 0 else "Armor"
    RARITY = "Epic" if 489 % 5 == 0 else "Legendary"
    BASE_VALUE = 24450
    ATTACK_BONUS = 1467
    DEFENSE_BONUS = 978
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 489."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_489.ITEM_ID, "name": ItemDefinition_489.NAME, "atk": ItemDefinition_489.ATTACK_BONUS, "def": ItemDefinition_489.DEFENSE_BONUS}


class ItemDefinition_490:
    ITEM_ID = "item_490"
    NAME = "Hyperion Legendary Artifact #490"
    TYPE = "Weapon" if 490 % 2 == 0 else "Armor"
    RARITY = "Epic" if 490 % 5 == 0 else "Legendary"
    BASE_VALUE = 24500
    ATTACK_BONUS = 1470
    DEFENSE_BONUS = 980
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 490."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_490.ITEM_ID, "name": ItemDefinition_490.NAME, "atk": ItemDefinition_490.ATTACK_BONUS, "def": ItemDefinition_490.DEFENSE_BONUS}


class ItemDefinition_491:
    ITEM_ID = "item_491"
    NAME = "Hyperion Legendary Artifact #491"
    TYPE = "Weapon" if 491 % 2 == 0 else "Armor"
    RARITY = "Epic" if 491 % 5 == 0 else "Legendary"
    BASE_VALUE = 24550
    ATTACK_BONUS = 1473
    DEFENSE_BONUS = 982
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 491."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_491.ITEM_ID, "name": ItemDefinition_491.NAME, "atk": ItemDefinition_491.ATTACK_BONUS, "def": ItemDefinition_491.DEFENSE_BONUS}


class ItemDefinition_492:
    ITEM_ID = "item_492"
    NAME = "Hyperion Legendary Artifact #492"
    TYPE = "Weapon" if 492 % 2 == 0 else "Armor"
    RARITY = "Epic" if 492 % 5 == 0 else "Legendary"
    BASE_VALUE = 24600
    ATTACK_BONUS = 1476
    DEFENSE_BONUS = 984
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 492."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_492.ITEM_ID, "name": ItemDefinition_492.NAME, "atk": ItemDefinition_492.ATTACK_BONUS, "def": ItemDefinition_492.DEFENSE_BONUS}


class ItemDefinition_493:
    ITEM_ID = "item_493"
    NAME = "Hyperion Legendary Artifact #493"
    TYPE = "Weapon" if 493 % 2 == 0 else "Armor"
    RARITY = "Epic" if 493 % 5 == 0 else "Legendary"
    BASE_VALUE = 24650
    ATTACK_BONUS = 1479
    DEFENSE_BONUS = 986
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 493."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_493.ITEM_ID, "name": ItemDefinition_493.NAME, "atk": ItemDefinition_493.ATTACK_BONUS, "def": ItemDefinition_493.DEFENSE_BONUS}


class ItemDefinition_494:
    ITEM_ID = "item_494"
    NAME = "Hyperion Legendary Artifact #494"
    TYPE = "Weapon" if 494 % 2 == 0 else "Armor"
    RARITY = "Epic" if 494 % 5 == 0 else "Legendary"
    BASE_VALUE = 24700
    ATTACK_BONUS = 1482
    DEFENSE_BONUS = 988
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 494."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_494.ITEM_ID, "name": ItemDefinition_494.NAME, "atk": ItemDefinition_494.ATTACK_BONUS, "def": ItemDefinition_494.DEFENSE_BONUS}


class ItemDefinition_495:
    ITEM_ID = "item_495"
    NAME = "Hyperion Legendary Artifact #495"
    TYPE = "Weapon" if 495 % 2 == 0 else "Armor"
    RARITY = "Epic" if 495 % 5 == 0 else "Legendary"
    BASE_VALUE = 24750
    ATTACK_BONUS = 1485
    DEFENSE_BONUS = 990
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 495."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_495.ITEM_ID, "name": ItemDefinition_495.NAME, "atk": ItemDefinition_495.ATTACK_BONUS, "def": ItemDefinition_495.DEFENSE_BONUS}


class ItemDefinition_496:
    ITEM_ID = "item_496"
    NAME = "Hyperion Legendary Artifact #496"
    TYPE = "Weapon" if 496 % 2 == 0 else "Armor"
    RARITY = "Epic" if 496 % 5 == 0 else "Legendary"
    BASE_VALUE = 24800
    ATTACK_BONUS = 1488
    DEFENSE_BONUS = 992
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 496."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_496.ITEM_ID, "name": ItemDefinition_496.NAME, "atk": ItemDefinition_496.ATTACK_BONUS, "def": ItemDefinition_496.DEFENSE_BONUS}


class ItemDefinition_497:
    ITEM_ID = "item_497"
    NAME = "Hyperion Legendary Artifact #497"
    TYPE = "Weapon" if 497 % 2 == 0 else "Armor"
    RARITY = "Epic" if 497 % 5 == 0 else "Legendary"
    BASE_VALUE = 24850
    ATTACK_BONUS = 1491
    DEFENSE_BONUS = 994
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 497."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_497.ITEM_ID, "name": ItemDefinition_497.NAME, "atk": ItemDefinition_497.ATTACK_BONUS, "def": ItemDefinition_497.DEFENSE_BONUS}


class ItemDefinition_498:
    ITEM_ID = "item_498"
    NAME = "Hyperion Legendary Artifact #498"
    TYPE = "Weapon" if 498 % 2 == 0 else "Armor"
    RARITY = "Epic" if 498 % 5 == 0 else "Legendary"
    BASE_VALUE = 24900
    ATTACK_BONUS = 1494
    DEFENSE_BONUS = 996
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 498."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_498.ITEM_ID, "name": ItemDefinition_498.NAME, "atk": ItemDefinition_498.ATTACK_BONUS, "def": ItemDefinition_498.DEFENSE_BONUS}


class ItemDefinition_499:
    ITEM_ID = "item_499"
    NAME = "Hyperion Legendary Artifact #499"
    TYPE = "Weapon" if 499 % 2 == 0 else "Armor"
    RARITY = "Epic" if 499 % 5 == 0 else "Legendary"
    BASE_VALUE = 24950
    ATTACK_BONUS = 1497
    DEFENSE_BONUS = 998
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 499."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_499.ITEM_ID, "name": ItemDefinition_499.NAME, "atk": ItemDefinition_499.ATTACK_BONUS, "def": ItemDefinition_499.DEFENSE_BONUS}


class ItemDefinition_500:
    ITEM_ID = "item_500"
    NAME = "Hyperion Legendary Artifact #500"
    TYPE = "Weapon" if 500 % 2 == 0 else "Armor"
    RARITY = "Epic" if 500 % 5 == 0 else "Legendary"
    BASE_VALUE = 25000
    ATTACK_BONUS = 1500
    DEFENSE_BONUS = 1000
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 500."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_500.ITEM_ID, "name": ItemDefinition_500.NAME, "atk": ItemDefinition_500.ATTACK_BONUS, "def": ItemDefinition_500.DEFENSE_BONUS}


class ItemDefinition_501:
    ITEM_ID = "item_501"
    NAME = "Hyperion Legendary Artifact #501"
    TYPE = "Weapon" if 501 % 2 == 0 else "Armor"
    RARITY = "Epic" if 501 % 5 == 0 else "Legendary"
    BASE_VALUE = 25050
    ATTACK_BONUS = 1503
    DEFENSE_BONUS = 1002
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 501."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_501.ITEM_ID, "name": ItemDefinition_501.NAME, "atk": ItemDefinition_501.ATTACK_BONUS, "def": ItemDefinition_501.DEFENSE_BONUS}


class ItemDefinition_502:
    ITEM_ID = "item_502"
    NAME = "Hyperion Legendary Artifact #502"
    TYPE = "Weapon" if 502 % 2 == 0 else "Armor"
    RARITY = "Epic" if 502 % 5 == 0 else "Legendary"
    BASE_VALUE = 25100
    ATTACK_BONUS = 1506
    DEFENSE_BONUS = 1004
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 502."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_502.ITEM_ID, "name": ItemDefinition_502.NAME, "atk": ItemDefinition_502.ATTACK_BONUS, "def": ItemDefinition_502.DEFENSE_BONUS}


class ItemDefinition_503:
    ITEM_ID = "item_503"
    NAME = "Hyperion Legendary Artifact #503"
    TYPE = "Weapon" if 503 % 2 == 0 else "Armor"
    RARITY = "Epic" if 503 % 5 == 0 else "Legendary"
    BASE_VALUE = 25150
    ATTACK_BONUS = 1509
    DEFENSE_BONUS = 1006
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 503."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_503.ITEM_ID, "name": ItemDefinition_503.NAME, "atk": ItemDefinition_503.ATTACK_BONUS, "def": ItemDefinition_503.DEFENSE_BONUS}


class ItemDefinition_504:
    ITEM_ID = "item_504"
    NAME = "Hyperion Legendary Artifact #504"
    TYPE = "Weapon" if 504 % 2 == 0 else "Armor"
    RARITY = "Epic" if 504 % 5 == 0 else "Legendary"
    BASE_VALUE = 25200
    ATTACK_BONUS = 1512
    DEFENSE_BONUS = 1008
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 504."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_504.ITEM_ID, "name": ItemDefinition_504.NAME, "atk": ItemDefinition_504.ATTACK_BONUS, "def": ItemDefinition_504.DEFENSE_BONUS}


class ItemDefinition_505:
    ITEM_ID = "item_505"
    NAME = "Hyperion Legendary Artifact #505"
    TYPE = "Weapon" if 505 % 2 == 0 else "Armor"
    RARITY = "Epic" if 505 % 5 == 0 else "Legendary"
    BASE_VALUE = 25250
    ATTACK_BONUS = 1515
    DEFENSE_BONUS = 1010
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 505."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_505.ITEM_ID, "name": ItemDefinition_505.NAME, "atk": ItemDefinition_505.ATTACK_BONUS, "def": ItemDefinition_505.DEFENSE_BONUS}


class ItemDefinition_506:
    ITEM_ID = "item_506"
    NAME = "Hyperion Legendary Artifact #506"
    TYPE = "Weapon" if 506 % 2 == 0 else "Armor"
    RARITY = "Epic" if 506 % 5 == 0 else "Legendary"
    BASE_VALUE = 25300
    ATTACK_BONUS = 1518
    DEFENSE_BONUS = 1012
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 506."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_506.ITEM_ID, "name": ItemDefinition_506.NAME, "atk": ItemDefinition_506.ATTACK_BONUS, "def": ItemDefinition_506.DEFENSE_BONUS}


class ItemDefinition_507:
    ITEM_ID = "item_507"
    NAME = "Hyperion Legendary Artifact #507"
    TYPE = "Weapon" if 507 % 2 == 0 else "Armor"
    RARITY = "Epic" if 507 % 5 == 0 else "Legendary"
    BASE_VALUE = 25350
    ATTACK_BONUS = 1521
    DEFENSE_BONUS = 1014
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 507."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_507.ITEM_ID, "name": ItemDefinition_507.NAME, "atk": ItemDefinition_507.ATTACK_BONUS, "def": ItemDefinition_507.DEFENSE_BONUS}


class ItemDefinition_508:
    ITEM_ID = "item_508"
    NAME = "Hyperion Legendary Artifact #508"
    TYPE = "Weapon" if 508 % 2 == 0 else "Armor"
    RARITY = "Epic" if 508 % 5 == 0 else "Legendary"
    BASE_VALUE = 25400
    ATTACK_BONUS = 1524
    DEFENSE_BONUS = 1016
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 508."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_508.ITEM_ID, "name": ItemDefinition_508.NAME, "atk": ItemDefinition_508.ATTACK_BONUS, "def": ItemDefinition_508.DEFENSE_BONUS}


class ItemDefinition_509:
    ITEM_ID = "item_509"
    NAME = "Hyperion Legendary Artifact #509"
    TYPE = "Weapon" if 509 % 2 == 0 else "Armor"
    RARITY = "Epic" if 509 % 5 == 0 else "Legendary"
    BASE_VALUE = 25450
    ATTACK_BONUS = 1527
    DEFENSE_BONUS = 1018
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 509."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_509.ITEM_ID, "name": ItemDefinition_509.NAME, "atk": ItemDefinition_509.ATTACK_BONUS, "def": ItemDefinition_509.DEFENSE_BONUS}


class ItemDefinition_510:
    ITEM_ID = "item_510"
    NAME = "Hyperion Legendary Artifact #510"
    TYPE = "Weapon" if 510 % 2 == 0 else "Armor"
    RARITY = "Epic" if 510 % 5 == 0 else "Legendary"
    BASE_VALUE = 25500
    ATTACK_BONUS = 1530
    DEFENSE_BONUS = 1020
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 510."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_510.ITEM_ID, "name": ItemDefinition_510.NAME, "atk": ItemDefinition_510.ATTACK_BONUS, "def": ItemDefinition_510.DEFENSE_BONUS}


class ItemDefinition_511:
    ITEM_ID = "item_511"
    NAME = "Hyperion Legendary Artifact #511"
    TYPE = "Weapon" if 511 % 2 == 0 else "Armor"
    RARITY = "Epic" if 511 % 5 == 0 else "Legendary"
    BASE_VALUE = 25550
    ATTACK_BONUS = 1533
    DEFENSE_BONUS = 1022
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 511."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_511.ITEM_ID, "name": ItemDefinition_511.NAME, "atk": ItemDefinition_511.ATTACK_BONUS, "def": ItemDefinition_511.DEFENSE_BONUS}


class ItemDefinition_512:
    ITEM_ID = "item_512"
    NAME = "Hyperion Legendary Artifact #512"
    TYPE = "Weapon" if 512 % 2 == 0 else "Armor"
    RARITY = "Epic" if 512 % 5 == 0 else "Legendary"
    BASE_VALUE = 25600
    ATTACK_BONUS = 1536
    DEFENSE_BONUS = 1024
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 512."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_512.ITEM_ID, "name": ItemDefinition_512.NAME, "atk": ItemDefinition_512.ATTACK_BONUS, "def": ItemDefinition_512.DEFENSE_BONUS}


class ItemDefinition_513:
    ITEM_ID = "item_513"
    NAME = "Hyperion Legendary Artifact #513"
    TYPE = "Weapon" if 513 % 2 == 0 else "Armor"
    RARITY = "Epic" if 513 % 5 == 0 else "Legendary"
    BASE_VALUE = 25650
    ATTACK_BONUS = 1539
    DEFENSE_BONUS = 1026
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 513."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_513.ITEM_ID, "name": ItemDefinition_513.NAME, "atk": ItemDefinition_513.ATTACK_BONUS, "def": ItemDefinition_513.DEFENSE_BONUS}


class ItemDefinition_514:
    ITEM_ID = "item_514"
    NAME = "Hyperion Legendary Artifact #514"
    TYPE = "Weapon" if 514 % 2 == 0 else "Armor"
    RARITY = "Epic" if 514 % 5 == 0 else "Legendary"
    BASE_VALUE = 25700
    ATTACK_BONUS = 1542
    DEFENSE_BONUS = 1028
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 514."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_514.ITEM_ID, "name": ItemDefinition_514.NAME, "atk": ItemDefinition_514.ATTACK_BONUS, "def": ItemDefinition_514.DEFENSE_BONUS}


class ItemDefinition_515:
    ITEM_ID = "item_515"
    NAME = "Hyperion Legendary Artifact #515"
    TYPE = "Weapon" if 515 % 2 == 0 else "Armor"
    RARITY = "Epic" if 515 % 5 == 0 else "Legendary"
    BASE_VALUE = 25750
    ATTACK_BONUS = 1545
    DEFENSE_BONUS = 1030
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 515."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_515.ITEM_ID, "name": ItemDefinition_515.NAME, "atk": ItemDefinition_515.ATTACK_BONUS, "def": ItemDefinition_515.DEFENSE_BONUS}


class ItemDefinition_516:
    ITEM_ID = "item_516"
    NAME = "Hyperion Legendary Artifact #516"
    TYPE = "Weapon" if 516 % 2 == 0 else "Armor"
    RARITY = "Epic" if 516 % 5 == 0 else "Legendary"
    BASE_VALUE = 25800
    ATTACK_BONUS = 1548
    DEFENSE_BONUS = 1032
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 516."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_516.ITEM_ID, "name": ItemDefinition_516.NAME, "atk": ItemDefinition_516.ATTACK_BONUS, "def": ItemDefinition_516.DEFENSE_BONUS}


class ItemDefinition_517:
    ITEM_ID = "item_517"
    NAME = "Hyperion Legendary Artifact #517"
    TYPE = "Weapon" if 517 % 2 == 0 else "Armor"
    RARITY = "Epic" if 517 % 5 == 0 else "Legendary"
    BASE_VALUE = 25850
    ATTACK_BONUS = 1551
    DEFENSE_BONUS = 1034
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 517."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_517.ITEM_ID, "name": ItemDefinition_517.NAME, "atk": ItemDefinition_517.ATTACK_BONUS, "def": ItemDefinition_517.DEFENSE_BONUS}


class ItemDefinition_518:
    ITEM_ID = "item_518"
    NAME = "Hyperion Legendary Artifact #518"
    TYPE = "Weapon" if 518 % 2 == 0 else "Armor"
    RARITY = "Epic" if 518 % 5 == 0 else "Legendary"
    BASE_VALUE = 25900
    ATTACK_BONUS = 1554
    DEFENSE_BONUS = 1036
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 518."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_518.ITEM_ID, "name": ItemDefinition_518.NAME, "atk": ItemDefinition_518.ATTACK_BONUS, "def": ItemDefinition_518.DEFENSE_BONUS}


class ItemDefinition_519:
    ITEM_ID = "item_519"
    NAME = "Hyperion Legendary Artifact #519"
    TYPE = "Weapon" if 519 % 2 == 0 else "Armor"
    RARITY = "Epic" if 519 % 5 == 0 else "Legendary"
    BASE_VALUE = 25950
    ATTACK_BONUS = 1557
    DEFENSE_BONUS = 1038
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 519."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_519.ITEM_ID, "name": ItemDefinition_519.NAME, "atk": ItemDefinition_519.ATTACK_BONUS, "def": ItemDefinition_519.DEFENSE_BONUS}


class ItemDefinition_520:
    ITEM_ID = "item_520"
    NAME = "Hyperion Legendary Artifact #520"
    TYPE = "Weapon" if 520 % 2 == 0 else "Armor"
    RARITY = "Epic" if 520 % 5 == 0 else "Legendary"
    BASE_VALUE = 26000
    ATTACK_BONUS = 1560
    DEFENSE_BONUS = 1040
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 520."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_520.ITEM_ID, "name": ItemDefinition_520.NAME, "atk": ItemDefinition_520.ATTACK_BONUS, "def": ItemDefinition_520.DEFENSE_BONUS}


class ItemDefinition_521:
    ITEM_ID = "item_521"
    NAME = "Hyperion Legendary Artifact #521"
    TYPE = "Weapon" if 521 % 2 == 0 else "Armor"
    RARITY = "Epic" if 521 % 5 == 0 else "Legendary"
    BASE_VALUE = 26050
    ATTACK_BONUS = 1563
    DEFENSE_BONUS = 1042
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 521."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_521.ITEM_ID, "name": ItemDefinition_521.NAME, "atk": ItemDefinition_521.ATTACK_BONUS, "def": ItemDefinition_521.DEFENSE_BONUS}


class ItemDefinition_522:
    ITEM_ID = "item_522"
    NAME = "Hyperion Legendary Artifact #522"
    TYPE = "Weapon" if 522 % 2 == 0 else "Armor"
    RARITY = "Epic" if 522 % 5 == 0 else "Legendary"
    BASE_VALUE = 26100
    ATTACK_BONUS = 1566
    DEFENSE_BONUS = 1044
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 522."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_522.ITEM_ID, "name": ItemDefinition_522.NAME, "atk": ItemDefinition_522.ATTACK_BONUS, "def": ItemDefinition_522.DEFENSE_BONUS}


class ItemDefinition_523:
    ITEM_ID = "item_523"
    NAME = "Hyperion Legendary Artifact #523"
    TYPE = "Weapon" if 523 % 2 == 0 else "Armor"
    RARITY = "Epic" if 523 % 5 == 0 else "Legendary"
    BASE_VALUE = 26150
    ATTACK_BONUS = 1569
    DEFENSE_BONUS = 1046
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 523."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_523.ITEM_ID, "name": ItemDefinition_523.NAME, "atk": ItemDefinition_523.ATTACK_BONUS, "def": ItemDefinition_523.DEFENSE_BONUS}


class ItemDefinition_524:
    ITEM_ID = "item_524"
    NAME = "Hyperion Legendary Artifact #524"
    TYPE = "Weapon" if 524 % 2 == 0 else "Armor"
    RARITY = "Epic" if 524 % 5 == 0 else "Legendary"
    BASE_VALUE = 26200
    ATTACK_BONUS = 1572
    DEFENSE_BONUS = 1048
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 524."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_524.ITEM_ID, "name": ItemDefinition_524.NAME, "atk": ItemDefinition_524.ATTACK_BONUS, "def": ItemDefinition_524.DEFENSE_BONUS}


class ItemDefinition_525:
    ITEM_ID = "item_525"
    NAME = "Hyperion Legendary Artifact #525"
    TYPE = "Weapon" if 525 % 2 == 0 else "Armor"
    RARITY = "Epic" if 525 % 5 == 0 else "Legendary"
    BASE_VALUE = 26250
    ATTACK_BONUS = 1575
    DEFENSE_BONUS = 1050
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 525."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_525.ITEM_ID, "name": ItemDefinition_525.NAME, "atk": ItemDefinition_525.ATTACK_BONUS, "def": ItemDefinition_525.DEFENSE_BONUS}


class ItemDefinition_526:
    ITEM_ID = "item_526"
    NAME = "Hyperion Legendary Artifact #526"
    TYPE = "Weapon" if 526 % 2 == 0 else "Armor"
    RARITY = "Epic" if 526 % 5 == 0 else "Legendary"
    BASE_VALUE = 26300
    ATTACK_BONUS = 1578
    DEFENSE_BONUS = 1052
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 526."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_526.ITEM_ID, "name": ItemDefinition_526.NAME, "atk": ItemDefinition_526.ATTACK_BONUS, "def": ItemDefinition_526.DEFENSE_BONUS}


class ItemDefinition_527:
    ITEM_ID = "item_527"
    NAME = "Hyperion Legendary Artifact #527"
    TYPE = "Weapon" if 527 % 2 == 0 else "Armor"
    RARITY = "Epic" if 527 % 5 == 0 else "Legendary"
    BASE_VALUE = 26350
    ATTACK_BONUS = 1581
    DEFENSE_BONUS = 1054
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 527."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_527.ITEM_ID, "name": ItemDefinition_527.NAME, "atk": ItemDefinition_527.ATTACK_BONUS, "def": ItemDefinition_527.DEFENSE_BONUS}


class ItemDefinition_528:
    ITEM_ID = "item_528"
    NAME = "Hyperion Legendary Artifact #528"
    TYPE = "Weapon" if 528 % 2 == 0 else "Armor"
    RARITY = "Epic" if 528 % 5 == 0 else "Legendary"
    BASE_VALUE = 26400
    ATTACK_BONUS = 1584
    DEFENSE_BONUS = 1056
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 528."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_528.ITEM_ID, "name": ItemDefinition_528.NAME, "atk": ItemDefinition_528.ATTACK_BONUS, "def": ItemDefinition_528.DEFENSE_BONUS}


class ItemDefinition_529:
    ITEM_ID = "item_529"
    NAME = "Hyperion Legendary Artifact #529"
    TYPE = "Weapon" if 529 % 2 == 0 else "Armor"
    RARITY = "Epic" if 529 % 5 == 0 else "Legendary"
    BASE_VALUE = 26450
    ATTACK_BONUS = 1587
    DEFENSE_BONUS = 1058
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 529."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_529.ITEM_ID, "name": ItemDefinition_529.NAME, "atk": ItemDefinition_529.ATTACK_BONUS, "def": ItemDefinition_529.DEFENSE_BONUS}


class ItemDefinition_530:
    ITEM_ID = "item_530"
    NAME = "Hyperion Legendary Artifact #530"
    TYPE = "Weapon" if 530 % 2 == 0 else "Armor"
    RARITY = "Epic" if 530 % 5 == 0 else "Legendary"
    BASE_VALUE = 26500
    ATTACK_BONUS = 1590
    DEFENSE_BONUS = 1060
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 530."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_530.ITEM_ID, "name": ItemDefinition_530.NAME, "atk": ItemDefinition_530.ATTACK_BONUS, "def": ItemDefinition_530.DEFENSE_BONUS}


class ItemDefinition_531:
    ITEM_ID = "item_531"
    NAME = "Hyperion Legendary Artifact #531"
    TYPE = "Weapon" if 531 % 2 == 0 else "Armor"
    RARITY = "Epic" if 531 % 5 == 0 else "Legendary"
    BASE_VALUE = 26550
    ATTACK_BONUS = 1593
    DEFENSE_BONUS = 1062
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 531."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_531.ITEM_ID, "name": ItemDefinition_531.NAME, "atk": ItemDefinition_531.ATTACK_BONUS, "def": ItemDefinition_531.DEFENSE_BONUS}


class ItemDefinition_532:
    ITEM_ID = "item_532"
    NAME = "Hyperion Legendary Artifact #532"
    TYPE = "Weapon" if 532 % 2 == 0 else "Armor"
    RARITY = "Epic" if 532 % 5 == 0 else "Legendary"
    BASE_VALUE = 26600
    ATTACK_BONUS = 1596
    DEFENSE_BONUS = 1064
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 532."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_532.ITEM_ID, "name": ItemDefinition_532.NAME, "atk": ItemDefinition_532.ATTACK_BONUS, "def": ItemDefinition_532.DEFENSE_BONUS}


class ItemDefinition_533:
    ITEM_ID = "item_533"
    NAME = "Hyperion Legendary Artifact #533"
    TYPE = "Weapon" if 533 % 2 == 0 else "Armor"
    RARITY = "Epic" if 533 % 5 == 0 else "Legendary"
    BASE_VALUE = 26650
    ATTACK_BONUS = 1599
    DEFENSE_BONUS = 1066
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 533."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_533.ITEM_ID, "name": ItemDefinition_533.NAME, "atk": ItemDefinition_533.ATTACK_BONUS, "def": ItemDefinition_533.DEFENSE_BONUS}


class ItemDefinition_534:
    ITEM_ID = "item_534"
    NAME = "Hyperion Legendary Artifact #534"
    TYPE = "Weapon" if 534 % 2 == 0 else "Armor"
    RARITY = "Epic" if 534 % 5 == 0 else "Legendary"
    BASE_VALUE = 26700
    ATTACK_BONUS = 1602
    DEFENSE_BONUS = 1068
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 534."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_534.ITEM_ID, "name": ItemDefinition_534.NAME, "atk": ItemDefinition_534.ATTACK_BONUS, "def": ItemDefinition_534.DEFENSE_BONUS}


class ItemDefinition_535:
    ITEM_ID = "item_535"
    NAME = "Hyperion Legendary Artifact #535"
    TYPE = "Weapon" if 535 % 2 == 0 else "Armor"
    RARITY = "Epic" if 535 % 5 == 0 else "Legendary"
    BASE_VALUE = 26750
    ATTACK_BONUS = 1605
    DEFENSE_BONUS = 1070
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 535."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_535.ITEM_ID, "name": ItemDefinition_535.NAME, "atk": ItemDefinition_535.ATTACK_BONUS, "def": ItemDefinition_535.DEFENSE_BONUS}


class ItemDefinition_536:
    ITEM_ID = "item_536"
    NAME = "Hyperion Legendary Artifact #536"
    TYPE = "Weapon" if 536 % 2 == 0 else "Armor"
    RARITY = "Epic" if 536 % 5 == 0 else "Legendary"
    BASE_VALUE = 26800
    ATTACK_BONUS = 1608
    DEFENSE_BONUS = 1072
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 536."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_536.ITEM_ID, "name": ItemDefinition_536.NAME, "atk": ItemDefinition_536.ATTACK_BONUS, "def": ItemDefinition_536.DEFENSE_BONUS}


class ItemDefinition_537:
    ITEM_ID = "item_537"
    NAME = "Hyperion Legendary Artifact #537"
    TYPE = "Weapon" if 537 % 2 == 0 else "Armor"
    RARITY = "Epic" if 537 % 5 == 0 else "Legendary"
    BASE_VALUE = 26850
    ATTACK_BONUS = 1611
    DEFENSE_BONUS = 1074
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 537."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_537.ITEM_ID, "name": ItemDefinition_537.NAME, "atk": ItemDefinition_537.ATTACK_BONUS, "def": ItemDefinition_537.DEFENSE_BONUS}


class ItemDefinition_538:
    ITEM_ID = "item_538"
    NAME = "Hyperion Legendary Artifact #538"
    TYPE = "Weapon" if 538 % 2 == 0 else "Armor"
    RARITY = "Epic" if 538 % 5 == 0 else "Legendary"
    BASE_VALUE = 26900
    ATTACK_BONUS = 1614
    DEFENSE_BONUS = 1076
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 538."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_538.ITEM_ID, "name": ItemDefinition_538.NAME, "atk": ItemDefinition_538.ATTACK_BONUS, "def": ItemDefinition_538.DEFENSE_BONUS}


class ItemDefinition_539:
    ITEM_ID = "item_539"
    NAME = "Hyperion Legendary Artifact #539"
    TYPE = "Weapon" if 539 % 2 == 0 else "Armor"
    RARITY = "Epic" if 539 % 5 == 0 else "Legendary"
    BASE_VALUE = 26950
    ATTACK_BONUS = 1617
    DEFENSE_BONUS = 1078
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 539."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_539.ITEM_ID, "name": ItemDefinition_539.NAME, "atk": ItemDefinition_539.ATTACK_BONUS, "def": ItemDefinition_539.DEFENSE_BONUS}


class ItemDefinition_540:
    ITEM_ID = "item_540"
    NAME = "Hyperion Legendary Artifact #540"
    TYPE = "Weapon" if 540 % 2 == 0 else "Armor"
    RARITY = "Epic" if 540 % 5 == 0 else "Legendary"
    BASE_VALUE = 27000
    ATTACK_BONUS = 1620
    DEFENSE_BONUS = 1080
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 540."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_540.ITEM_ID, "name": ItemDefinition_540.NAME, "atk": ItemDefinition_540.ATTACK_BONUS, "def": ItemDefinition_540.DEFENSE_BONUS}


class ItemDefinition_541:
    ITEM_ID = "item_541"
    NAME = "Hyperion Legendary Artifact #541"
    TYPE = "Weapon" if 541 % 2 == 0 else "Armor"
    RARITY = "Epic" if 541 % 5 == 0 else "Legendary"
    BASE_VALUE = 27050
    ATTACK_BONUS = 1623
    DEFENSE_BONUS = 1082
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 541."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_541.ITEM_ID, "name": ItemDefinition_541.NAME, "atk": ItemDefinition_541.ATTACK_BONUS, "def": ItemDefinition_541.DEFENSE_BONUS}


class ItemDefinition_542:
    ITEM_ID = "item_542"
    NAME = "Hyperion Legendary Artifact #542"
    TYPE = "Weapon" if 542 % 2 == 0 else "Armor"
    RARITY = "Epic" if 542 % 5 == 0 else "Legendary"
    BASE_VALUE = 27100
    ATTACK_BONUS = 1626
    DEFENSE_BONUS = 1084
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 542."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_542.ITEM_ID, "name": ItemDefinition_542.NAME, "atk": ItemDefinition_542.ATTACK_BONUS, "def": ItemDefinition_542.DEFENSE_BONUS}


class ItemDefinition_543:
    ITEM_ID = "item_543"
    NAME = "Hyperion Legendary Artifact #543"
    TYPE = "Weapon" if 543 % 2 == 0 else "Armor"
    RARITY = "Epic" if 543 % 5 == 0 else "Legendary"
    BASE_VALUE = 27150
    ATTACK_BONUS = 1629
    DEFENSE_BONUS = 1086
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 543."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_543.ITEM_ID, "name": ItemDefinition_543.NAME, "atk": ItemDefinition_543.ATTACK_BONUS, "def": ItemDefinition_543.DEFENSE_BONUS}


class ItemDefinition_544:
    ITEM_ID = "item_544"
    NAME = "Hyperion Legendary Artifact #544"
    TYPE = "Weapon" if 544 % 2 == 0 else "Armor"
    RARITY = "Epic" if 544 % 5 == 0 else "Legendary"
    BASE_VALUE = 27200
    ATTACK_BONUS = 1632
    DEFENSE_BONUS = 1088
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 544."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_544.ITEM_ID, "name": ItemDefinition_544.NAME, "atk": ItemDefinition_544.ATTACK_BONUS, "def": ItemDefinition_544.DEFENSE_BONUS}


class ItemDefinition_545:
    ITEM_ID = "item_545"
    NAME = "Hyperion Legendary Artifact #545"
    TYPE = "Weapon" if 545 % 2 == 0 else "Armor"
    RARITY = "Epic" if 545 % 5 == 0 else "Legendary"
    BASE_VALUE = 27250
    ATTACK_BONUS = 1635
    DEFENSE_BONUS = 1090
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 545."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_545.ITEM_ID, "name": ItemDefinition_545.NAME, "atk": ItemDefinition_545.ATTACK_BONUS, "def": ItemDefinition_545.DEFENSE_BONUS}


class ItemDefinition_546:
    ITEM_ID = "item_546"
    NAME = "Hyperion Legendary Artifact #546"
    TYPE = "Weapon" if 546 % 2 == 0 else "Armor"
    RARITY = "Epic" if 546 % 5 == 0 else "Legendary"
    BASE_VALUE = 27300
    ATTACK_BONUS = 1638
    DEFENSE_BONUS = 1092
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 546."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_546.ITEM_ID, "name": ItemDefinition_546.NAME, "atk": ItemDefinition_546.ATTACK_BONUS, "def": ItemDefinition_546.DEFENSE_BONUS}


class ItemDefinition_547:
    ITEM_ID = "item_547"
    NAME = "Hyperion Legendary Artifact #547"
    TYPE = "Weapon" if 547 % 2 == 0 else "Armor"
    RARITY = "Epic" if 547 % 5 == 0 else "Legendary"
    BASE_VALUE = 27350
    ATTACK_BONUS = 1641
    DEFENSE_BONUS = 1094
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 547."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_547.ITEM_ID, "name": ItemDefinition_547.NAME, "atk": ItemDefinition_547.ATTACK_BONUS, "def": ItemDefinition_547.DEFENSE_BONUS}


class ItemDefinition_548:
    ITEM_ID = "item_548"
    NAME = "Hyperion Legendary Artifact #548"
    TYPE = "Weapon" if 548 % 2 == 0 else "Armor"
    RARITY = "Epic" if 548 % 5 == 0 else "Legendary"
    BASE_VALUE = 27400
    ATTACK_BONUS = 1644
    DEFENSE_BONUS = 1096
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 548."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_548.ITEM_ID, "name": ItemDefinition_548.NAME, "atk": ItemDefinition_548.ATTACK_BONUS, "def": ItemDefinition_548.DEFENSE_BONUS}


class ItemDefinition_549:
    ITEM_ID = "item_549"
    NAME = "Hyperion Legendary Artifact #549"
    TYPE = "Weapon" if 549 % 2 == 0 else "Armor"
    RARITY = "Epic" if 549 % 5 == 0 else "Legendary"
    BASE_VALUE = 27450
    ATTACK_BONUS = 1647
    DEFENSE_BONUS = 1098
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 549."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_549.ITEM_ID, "name": ItemDefinition_549.NAME, "atk": ItemDefinition_549.ATTACK_BONUS, "def": ItemDefinition_549.DEFENSE_BONUS}


class ItemDefinition_550:
    ITEM_ID = "item_550"
    NAME = "Hyperion Legendary Artifact #550"
    TYPE = "Weapon" if 550 % 2 == 0 else "Armor"
    RARITY = "Epic" if 550 % 5 == 0 else "Legendary"
    BASE_VALUE = 27500
    ATTACK_BONUS = 1650
    DEFENSE_BONUS = 1100
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 550."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_550.ITEM_ID, "name": ItemDefinition_550.NAME, "atk": ItemDefinition_550.ATTACK_BONUS, "def": ItemDefinition_550.DEFENSE_BONUS}


class ItemDefinition_551:
    ITEM_ID = "item_551"
    NAME = "Hyperion Legendary Artifact #551"
    TYPE = "Weapon" if 551 % 2 == 0 else "Armor"
    RARITY = "Epic" if 551 % 5 == 0 else "Legendary"
    BASE_VALUE = 27550
    ATTACK_BONUS = 1653
    DEFENSE_BONUS = 1102
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 551."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_551.ITEM_ID, "name": ItemDefinition_551.NAME, "atk": ItemDefinition_551.ATTACK_BONUS, "def": ItemDefinition_551.DEFENSE_BONUS}


class ItemDefinition_552:
    ITEM_ID = "item_552"
    NAME = "Hyperion Legendary Artifact #552"
    TYPE = "Weapon" if 552 % 2 == 0 else "Armor"
    RARITY = "Epic" if 552 % 5 == 0 else "Legendary"
    BASE_VALUE = 27600
    ATTACK_BONUS = 1656
    DEFENSE_BONUS = 1104
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 552."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_552.ITEM_ID, "name": ItemDefinition_552.NAME, "atk": ItemDefinition_552.ATTACK_BONUS, "def": ItemDefinition_552.DEFENSE_BONUS}


class ItemDefinition_553:
    ITEM_ID = "item_553"
    NAME = "Hyperion Legendary Artifact #553"
    TYPE = "Weapon" if 553 % 2 == 0 else "Armor"
    RARITY = "Epic" if 553 % 5 == 0 else "Legendary"
    BASE_VALUE = 27650
    ATTACK_BONUS = 1659
    DEFENSE_BONUS = 1106
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 553."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_553.ITEM_ID, "name": ItemDefinition_553.NAME, "atk": ItemDefinition_553.ATTACK_BONUS, "def": ItemDefinition_553.DEFENSE_BONUS}


class ItemDefinition_554:
    ITEM_ID = "item_554"
    NAME = "Hyperion Legendary Artifact #554"
    TYPE = "Weapon" if 554 % 2 == 0 else "Armor"
    RARITY = "Epic" if 554 % 5 == 0 else "Legendary"
    BASE_VALUE = 27700
    ATTACK_BONUS = 1662
    DEFENSE_BONUS = 1108
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 554."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_554.ITEM_ID, "name": ItemDefinition_554.NAME, "atk": ItemDefinition_554.ATTACK_BONUS, "def": ItemDefinition_554.DEFENSE_BONUS}


class ItemDefinition_555:
    ITEM_ID = "item_555"
    NAME = "Hyperion Legendary Artifact #555"
    TYPE = "Weapon" if 555 % 2 == 0 else "Armor"
    RARITY = "Epic" if 555 % 5 == 0 else "Legendary"
    BASE_VALUE = 27750
    ATTACK_BONUS = 1665
    DEFENSE_BONUS = 1110
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 555."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_555.ITEM_ID, "name": ItemDefinition_555.NAME, "atk": ItemDefinition_555.ATTACK_BONUS, "def": ItemDefinition_555.DEFENSE_BONUS}


class ItemDefinition_556:
    ITEM_ID = "item_556"
    NAME = "Hyperion Legendary Artifact #556"
    TYPE = "Weapon" if 556 % 2 == 0 else "Armor"
    RARITY = "Epic" if 556 % 5 == 0 else "Legendary"
    BASE_VALUE = 27800
    ATTACK_BONUS = 1668
    DEFENSE_BONUS = 1112
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 556."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_556.ITEM_ID, "name": ItemDefinition_556.NAME, "atk": ItemDefinition_556.ATTACK_BONUS, "def": ItemDefinition_556.DEFENSE_BONUS}


class ItemDefinition_557:
    ITEM_ID = "item_557"
    NAME = "Hyperion Legendary Artifact #557"
    TYPE = "Weapon" if 557 % 2 == 0 else "Armor"
    RARITY = "Epic" if 557 % 5 == 0 else "Legendary"
    BASE_VALUE = 27850
    ATTACK_BONUS = 1671
    DEFENSE_BONUS = 1114
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 557."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_557.ITEM_ID, "name": ItemDefinition_557.NAME, "atk": ItemDefinition_557.ATTACK_BONUS, "def": ItemDefinition_557.DEFENSE_BONUS}


class ItemDefinition_558:
    ITEM_ID = "item_558"
    NAME = "Hyperion Legendary Artifact #558"
    TYPE = "Weapon" if 558 % 2 == 0 else "Armor"
    RARITY = "Epic" if 558 % 5 == 0 else "Legendary"
    BASE_VALUE = 27900
    ATTACK_BONUS = 1674
    DEFENSE_BONUS = 1116
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 558."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_558.ITEM_ID, "name": ItemDefinition_558.NAME, "atk": ItemDefinition_558.ATTACK_BONUS, "def": ItemDefinition_558.DEFENSE_BONUS}


class ItemDefinition_559:
    ITEM_ID = "item_559"
    NAME = "Hyperion Legendary Artifact #559"
    TYPE = "Weapon" if 559 % 2 == 0 else "Armor"
    RARITY = "Epic" if 559 % 5 == 0 else "Legendary"
    BASE_VALUE = 27950
    ATTACK_BONUS = 1677
    DEFENSE_BONUS = 1118
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 559."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_559.ITEM_ID, "name": ItemDefinition_559.NAME, "atk": ItemDefinition_559.ATTACK_BONUS, "def": ItemDefinition_559.DEFENSE_BONUS}


class ItemDefinition_560:
    ITEM_ID = "item_560"
    NAME = "Hyperion Legendary Artifact #560"
    TYPE = "Weapon" if 560 % 2 == 0 else "Armor"
    RARITY = "Epic" if 560 % 5 == 0 else "Legendary"
    BASE_VALUE = 28000
    ATTACK_BONUS = 1680
    DEFENSE_BONUS = 1120
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 560."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_560.ITEM_ID, "name": ItemDefinition_560.NAME, "atk": ItemDefinition_560.ATTACK_BONUS, "def": ItemDefinition_560.DEFENSE_BONUS}


class ItemDefinition_561:
    ITEM_ID = "item_561"
    NAME = "Hyperion Legendary Artifact #561"
    TYPE = "Weapon" if 561 % 2 == 0 else "Armor"
    RARITY = "Epic" if 561 % 5 == 0 else "Legendary"
    BASE_VALUE = 28050
    ATTACK_BONUS = 1683
    DEFENSE_BONUS = 1122
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 561."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_561.ITEM_ID, "name": ItemDefinition_561.NAME, "atk": ItemDefinition_561.ATTACK_BONUS, "def": ItemDefinition_561.DEFENSE_BONUS}


class ItemDefinition_562:
    ITEM_ID = "item_562"
    NAME = "Hyperion Legendary Artifact #562"
    TYPE = "Weapon" if 562 % 2 == 0 else "Armor"
    RARITY = "Epic" if 562 % 5 == 0 else "Legendary"
    BASE_VALUE = 28100
    ATTACK_BONUS = 1686
    DEFENSE_BONUS = 1124
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 562."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_562.ITEM_ID, "name": ItemDefinition_562.NAME, "atk": ItemDefinition_562.ATTACK_BONUS, "def": ItemDefinition_562.DEFENSE_BONUS}


class ItemDefinition_563:
    ITEM_ID = "item_563"
    NAME = "Hyperion Legendary Artifact #563"
    TYPE = "Weapon" if 563 % 2 == 0 else "Armor"
    RARITY = "Epic" if 563 % 5 == 0 else "Legendary"
    BASE_VALUE = 28150
    ATTACK_BONUS = 1689
    DEFENSE_BONUS = 1126
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 563."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_563.ITEM_ID, "name": ItemDefinition_563.NAME, "atk": ItemDefinition_563.ATTACK_BONUS, "def": ItemDefinition_563.DEFENSE_BONUS}


class ItemDefinition_564:
    ITEM_ID = "item_564"
    NAME = "Hyperion Legendary Artifact #564"
    TYPE = "Weapon" if 564 % 2 == 0 else "Armor"
    RARITY = "Epic" if 564 % 5 == 0 else "Legendary"
    BASE_VALUE = 28200
    ATTACK_BONUS = 1692
    DEFENSE_BONUS = 1128
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 564."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_564.ITEM_ID, "name": ItemDefinition_564.NAME, "atk": ItemDefinition_564.ATTACK_BONUS, "def": ItemDefinition_564.DEFENSE_BONUS}


class ItemDefinition_565:
    ITEM_ID = "item_565"
    NAME = "Hyperion Legendary Artifact #565"
    TYPE = "Weapon" if 565 % 2 == 0 else "Armor"
    RARITY = "Epic" if 565 % 5 == 0 else "Legendary"
    BASE_VALUE = 28250
    ATTACK_BONUS = 1695
    DEFENSE_BONUS = 1130
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 565."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_565.ITEM_ID, "name": ItemDefinition_565.NAME, "atk": ItemDefinition_565.ATTACK_BONUS, "def": ItemDefinition_565.DEFENSE_BONUS}


class ItemDefinition_566:
    ITEM_ID = "item_566"
    NAME = "Hyperion Legendary Artifact #566"
    TYPE = "Weapon" if 566 % 2 == 0 else "Armor"
    RARITY = "Epic" if 566 % 5 == 0 else "Legendary"
    BASE_VALUE = 28300
    ATTACK_BONUS = 1698
    DEFENSE_BONUS = 1132
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 566."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_566.ITEM_ID, "name": ItemDefinition_566.NAME, "atk": ItemDefinition_566.ATTACK_BONUS, "def": ItemDefinition_566.DEFENSE_BONUS}


class ItemDefinition_567:
    ITEM_ID = "item_567"
    NAME = "Hyperion Legendary Artifact #567"
    TYPE = "Weapon" if 567 % 2 == 0 else "Armor"
    RARITY = "Epic" if 567 % 5 == 0 else "Legendary"
    BASE_VALUE = 28350
    ATTACK_BONUS = 1701
    DEFENSE_BONUS = 1134
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 567."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_567.ITEM_ID, "name": ItemDefinition_567.NAME, "atk": ItemDefinition_567.ATTACK_BONUS, "def": ItemDefinition_567.DEFENSE_BONUS}


class ItemDefinition_568:
    ITEM_ID = "item_568"
    NAME = "Hyperion Legendary Artifact #568"
    TYPE = "Weapon" if 568 % 2 == 0 else "Armor"
    RARITY = "Epic" if 568 % 5 == 0 else "Legendary"
    BASE_VALUE = 28400
    ATTACK_BONUS = 1704
    DEFENSE_BONUS = 1136
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 568."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_568.ITEM_ID, "name": ItemDefinition_568.NAME, "atk": ItemDefinition_568.ATTACK_BONUS, "def": ItemDefinition_568.DEFENSE_BONUS}


class ItemDefinition_569:
    ITEM_ID = "item_569"
    NAME = "Hyperion Legendary Artifact #569"
    TYPE = "Weapon" if 569 % 2 == 0 else "Armor"
    RARITY = "Epic" if 569 % 5 == 0 else "Legendary"
    BASE_VALUE = 28450
    ATTACK_BONUS = 1707
    DEFENSE_BONUS = 1138
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 569."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_569.ITEM_ID, "name": ItemDefinition_569.NAME, "atk": ItemDefinition_569.ATTACK_BONUS, "def": ItemDefinition_569.DEFENSE_BONUS}


class ItemDefinition_570:
    ITEM_ID = "item_570"
    NAME = "Hyperion Legendary Artifact #570"
    TYPE = "Weapon" if 570 % 2 == 0 else "Armor"
    RARITY = "Epic" if 570 % 5 == 0 else "Legendary"
    BASE_VALUE = 28500
    ATTACK_BONUS = 1710
    DEFENSE_BONUS = 1140
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 570."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_570.ITEM_ID, "name": ItemDefinition_570.NAME, "atk": ItemDefinition_570.ATTACK_BONUS, "def": ItemDefinition_570.DEFENSE_BONUS}


class ItemDefinition_571:
    ITEM_ID = "item_571"
    NAME = "Hyperion Legendary Artifact #571"
    TYPE = "Weapon" if 571 % 2 == 0 else "Armor"
    RARITY = "Epic" if 571 % 5 == 0 else "Legendary"
    BASE_VALUE = 28550
    ATTACK_BONUS = 1713
    DEFENSE_BONUS = 1142
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 571."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_571.ITEM_ID, "name": ItemDefinition_571.NAME, "atk": ItemDefinition_571.ATTACK_BONUS, "def": ItemDefinition_571.DEFENSE_BONUS}


class ItemDefinition_572:
    ITEM_ID = "item_572"
    NAME = "Hyperion Legendary Artifact #572"
    TYPE = "Weapon" if 572 % 2 == 0 else "Armor"
    RARITY = "Epic" if 572 % 5 == 0 else "Legendary"
    BASE_VALUE = 28600
    ATTACK_BONUS = 1716
    DEFENSE_BONUS = 1144
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 572."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_572.ITEM_ID, "name": ItemDefinition_572.NAME, "atk": ItemDefinition_572.ATTACK_BONUS, "def": ItemDefinition_572.DEFENSE_BONUS}


class ItemDefinition_573:
    ITEM_ID = "item_573"
    NAME = "Hyperion Legendary Artifact #573"
    TYPE = "Weapon" if 573 % 2 == 0 else "Armor"
    RARITY = "Epic" if 573 % 5 == 0 else "Legendary"
    BASE_VALUE = 28650
    ATTACK_BONUS = 1719
    DEFENSE_BONUS = 1146
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 573."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_573.ITEM_ID, "name": ItemDefinition_573.NAME, "atk": ItemDefinition_573.ATTACK_BONUS, "def": ItemDefinition_573.DEFENSE_BONUS}


class ItemDefinition_574:
    ITEM_ID = "item_574"
    NAME = "Hyperion Legendary Artifact #574"
    TYPE = "Weapon" if 574 % 2 == 0 else "Armor"
    RARITY = "Epic" if 574 % 5 == 0 else "Legendary"
    BASE_VALUE = 28700
    ATTACK_BONUS = 1722
    DEFENSE_BONUS = 1148
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 574."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_574.ITEM_ID, "name": ItemDefinition_574.NAME, "atk": ItemDefinition_574.ATTACK_BONUS, "def": ItemDefinition_574.DEFENSE_BONUS}


class ItemDefinition_575:
    ITEM_ID = "item_575"
    NAME = "Hyperion Legendary Artifact #575"
    TYPE = "Weapon" if 575 % 2 == 0 else "Armor"
    RARITY = "Epic" if 575 % 5 == 0 else "Legendary"
    BASE_VALUE = 28750
    ATTACK_BONUS = 1725
    DEFENSE_BONUS = 1150
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 575."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_575.ITEM_ID, "name": ItemDefinition_575.NAME, "atk": ItemDefinition_575.ATTACK_BONUS, "def": ItemDefinition_575.DEFENSE_BONUS}


class ItemDefinition_576:
    ITEM_ID = "item_576"
    NAME = "Hyperion Legendary Artifact #576"
    TYPE = "Weapon" if 576 % 2 == 0 else "Armor"
    RARITY = "Epic" if 576 % 5 == 0 else "Legendary"
    BASE_VALUE = 28800
    ATTACK_BONUS = 1728
    DEFENSE_BONUS = 1152
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 576."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_576.ITEM_ID, "name": ItemDefinition_576.NAME, "atk": ItemDefinition_576.ATTACK_BONUS, "def": ItemDefinition_576.DEFENSE_BONUS}


class ItemDefinition_577:
    ITEM_ID = "item_577"
    NAME = "Hyperion Legendary Artifact #577"
    TYPE = "Weapon" if 577 % 2 == 0 else "Armor"
    RARITY = "Epic" if 577 % 5 == 0 else "Legendary"
    BASE_VALUE = 28850
    ATTACK_BONUS = 1731
    DEFENSE_BONUS = 1154
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 577."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_577.ITEM_ID, "name": ItemDefinition_577.NAME, "atk": ItemDefinition_577.ATTACK_BONUS, "def": ItemDefinition_577.DEFENSE_BONUS}


class ItemDefinition_578:
    ITEM_ID = "item_578"
    NAME = "Hyperion Legendary Artifact #578"
    TYPE = "Weapon" if 578 % 2 == 0 else "Armor"
    RARITY = "Epic" if 578 % 5 == 0 else "Legendary"
    BASE_VALUE = 28900
    ATTACK_BONUS = 1734
    DEFENSE_BONUS = 1156
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 578."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_578.ITEM_ID, "name": ItemDefinition_578.NAME, "atk": ItemDefinition_578.ATTACK_BONUS, "def": ItemDefinition_578.DEFENSE_BONUS}


class ItemDefinition_579:
    ITEM_ID = "item_579"
    NAME = "Hyperion Legendary Artifact #579"
    TYPE = "Weapon" if 579 % 2 == 0 else "Armor"
    RARITY = "Epic" if 579 % 5 == 0 else "Legendary"
    BASE_VALUE = 28950
    ATTACK_BONUS = 1737
    DEFENSE_BONUS = 1158
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 579."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_579.ITEM_ID, "name": ItemDefinition_579.NAME, "atk": ItemDefinition_579.ATTACK_BONUS, "def": ItemDefinition_579.DEFENSE_BONUS}


class ItemDefinition_580:
    ITEM_ID = "item_580"
    NAME = "Hyperion Legendary Artifact #580"
    TYPE = "Weapon" if 580 % 2 == 0 else "Armor"
    RARITY = "Epic" if 580 % 5 == 0 else "Legendary"
    BASE_VALUE = 29000
    ATTACK_BONUS = 1740
    DEFENSE_BONUS = 1160
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 580."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_580.ITEM_ID, "name": ItemDefinition_580.NAME, "atk": ItemDefinition_580.ATTACK_BONUS, "def": ItemDefinition_580.DEFENSE_BONUS}


class ItemDefinition_581:
    ITEM_ID = "item_581"
    NAME = "Hyperion Legendary Artifact #581"
    TYPE = "Weapon" if 581 % 2 == 0 else "Armor"
    RARITY = "Epic" if 581 % 5 == 0 else "Legendary"
    BASE_VALUE = 29050
    ATTACK_BONUS = 1743
    DEFENSE_BONUS = 1162
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 581."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_581.ITEM_ID, "name": ItemDefinition_581.NAME, "atk": ItemDefinition_581.ATTACK_BONUS, "def": ItemDefinition_581.DEFENSE_BONUS}


class ItemDefinition_582:
    ITEM_ID = "item_582"
    NAME = "Hyperion Legendary Artifact #582"
    TYPE = "Weapon" if 582 % 2 == 0 else "Armor"
    RARITY = "Epic" if 582 % 5 == 0 else "Legendary"
    BASE_VALUE = 29100
    ATTACK_BONUS = 1746
    DEFENSE_BONUS = 1164
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 582."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_582.ITEM_ID, "name": ItemDefinition_582.NAME, "atk": ItemDefinition_582.ATTACK_BONUS, "def": ItemDefinition_582.DEFENSE_BONUS}


class ItemDefinition_583:
    ITEM_ID = "item_583"
    NAME = "Hyperion Legendary Artifact #583"
    TYPE = "Weapon" if 583 % 2 == 0 else "Armor"
    RARITY = "Epic" if 583 % 5 == 0 else "Legendary"
    BASE_VALUE = 29150
    ATTACK_BONUS = 1749
    DEFENSE_BONUS = 1166
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 583."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_583.ITEM_ID, "name": ItemDefinition_583.NAME, "atk": ItemDefinition_583.ATTACK_BONUS, "def": ItemDefinition_583.DEFENSE_BONUS}


class ItemDefinition_584:
    ITEM_ID = "item_584"
    NAME = "Hyperion Legendary Artifact #584"
    TYPE = "Weapon" if 584 % 2 == 0 else "Armor"
    RARITY = "Epic" if 584 % 5 == 0 else "Legendary"
    BASE_VALUE = 29200
    ATTACK_BONUS = 1752
    DEFENSE_BONUS = 1168
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 584."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_584.ITEM_ID, "name": ItemDefinition_584.NAME, "atk": ItemDefinition_584.ATTACK_BONUS, "def": ItemDefinition_584.DEFENSE_BONUS}


class ItemDefinition_585:
    ITEM_ID = "item_585"
    NAME = "Hyperion Legendary Artifact #585"
    TYPE = "Weapon" if 585 % 2 == 0 else "Armor"
    RARITY = "Epic" if 585 % 5 == 0 else "Legendary"
    BASE_VALUE = 29250
    ATTACK_BONUS = 1755
    DEFENSE_BONUS = 1170
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 585."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_585.ITEM_ID, "name": ItemDefinition_585.NAME, "atk": ItemDefinition_585.ATTACK_BONUS, "def": ItemDefinition_585.DEFENSE_BONUS}


class ItemDefinition_586:
    ITEM_ID = "item_586"
    NAME = "Hyperion Legendary Artifact #586"
    TYPE = "Weapon" if 586 % 2 == 0 else "Armor"
    RARITY = "Epic" if 586 % 5 == 0 else "Legendary"
    BASE_VALUE = 29300
    ATTACK_BONUS = 1758
    DEFENSE_BONUS = 1172
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 586."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_586.ITEM_ID, "name": ItemDefinition_586.NAME, "atk": ItemDefinition_586.ATTACK_BONUS, "def": ItemDefinition_586.DEFENSE_BONUS}


class ItemDefinition_587:
    ITEM_ID = "item_587"
    NAME = "Hyperion Legendary Artifact #587"
    TYPE = "Weapon" if 587 % 2 == 0 else "Armor"
    RARITY = "Epic" if 587 % 5 == 0 else "Legendary"
    BASE_VALUE = 29350
    ATTACK_BONUS = 1761
    DEFENSE_BONUS = 1174
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 587."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_587.ITEM_ID, "name": ItemDefinition_587.NAME, "atk": ItemDefinition_587.ATTACK_BONUS, "def": ItemDefinition_587.DEFENSE_BONUS}


class ItemDefinition_588:
    ITEM_ID = "item_588"
    NAME = "Hyperion Legendary Artifact #588"
    TYPE = "Weapon" if 588 % 2 == 0 else "Armor"
    RARITY = "Epic" if 588 % 5 == 0 else "Legendary"
    BASE_VALUE = 29400
    ATTACK_BONUS = 1764
    DEFENSE_BONUS = 1176
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 588."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_588.ITEM_ID, "name": ItemDefinition_588.NAME, "atk": ItemDefinition_588.ATTACK_BONUS, "def": ItemDefinition_588.DEFENSE_BONUS}


class ItemDefinition_589:
    ITEM_ID = "item_589"
    NAME = "Hyperion Legendary Artifact #589"
    TYPE = "Weapon" if 589 % 2 == 0 else "Armor"
    RARITY = "Epic" if 589 % 5 == 0 else "Legendary"
    BASE_VALUE = 29450
    ATTACK_BONUS = 1767
    DEFENSE_BONUS = 1178
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 589."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_589.ITEM_ID, "name": ItemDefinition_589.NAME, "atk": ItemDefinition_589.ATTACK_BONUS, "def": ItemDefinition_589.DEFENSE_BONUS}


class ItemDefinition_590:
    ITEM_ID = "item_590"
    NAME = "Hyperion Legendary Artifact #590"
    TYPE = "Weapon" if 590 % 2 == 0 else "Armor"
    RARITY = "Epic" if 590 % 5 == 0 else "Legendary"
    BASE_VALUE = 29500
    ATTACK_BONUS = 1770
    DEFENSE_BONUS = 1180
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 590."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_590.ITEM_ID, "name": ItemDefinition_590.NAME, "atk": ItemDefinition_590.ATTACK_BONUS, "def": ItemDefinition_590.DEFENSE_BONUS}


class ItemDefinition_591:
    ITEM_ID = "item_591"
    NAME = "Hyperion Legendary Artifact #591"
    TYPE = "Weapon" if 591 % 2 == 0 else "Armor"
    RARITY = "Epic" if 591 % 5 == 0 else "Legendary"
    BASE_VALUE = 29550
    ATTACK_BONUS = 1773
    DEFENSE_BONUS = 1182
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 591."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_591.ITEM_ID, "name": ItemDefinition_591.NAME, "atk": ItemDefinition_591.ATTACK_BONUS, "def": ItemDefinition_591.DEFENSE_BONUS}


class ItemDefinition_592:
    ITEM_ID = "item_592"
    NAME = "Hyperion Legendary Artifact #592"
    TYPE = "Weapon" if 592 % 2 == 0 else "Armor"
    RARITY = "Epic" if 592 % 5 == 0 else "Legendary"
    BASE_VALUE = 29600
    ATTACK_BONUS = 1776
    DEFENSE_BONUS = 1184
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 592."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_592.ITEM_ID, "name": ItemDefinition_592.NAME, "atk": ItemDefinition_592.ATTACK_BONUS, "def": ItemDefinition_592.DEFENSE_BONUS}


class ItemDefinition_593:
    ITEM_ID = "item_593"
    NAME = "Hyperion Legendary Artifact #593"
    TYPE = "Weapon" if 593 % 2 == 0 else "Armor"
    RARITY = "Epic" if 593 % 5 == 0 else "Legendary"
    BASE_VALUE = 29650
    ATTACK_BONUS = 1779
    DEFENSE_BONUS = 1186
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 593."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_593.ITEM_ID, "name": ItemDefinition_593.NAME, "atk": ItemDefinition_593.ATTACK_BONUS, "def": ItemDefinition_593.DEFENSE_BONUS}


class ItemDefinition_594:
    ITEM_ID = "item_594"
    NAME = "Hyperion Legendary Artifact #594"
    TYPE = "Weapon" if 594 % 2 == 0 else "Armor"
    RARITY = "Epic" if 594 % 5 == 0 else "Legendary"
    BASE_VALUE = 29700
    ATTACK_BONUS = 1782
    DEFENSE_BONUS = 1188
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 594."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_594.ITEM_ID, "name": ItemDefinition_594.NAME, "atk": ItemDefinition_594.ATTACK_BONUS, "def": ItemDefinition_594.DEFENSE_BONUS}


class ItemDefinition_595:
    ITEM_ID = "item_595"
    NAME = "Hyperion Legendary Artifact #595"
    TYPE = "Weapon" if 595 % 2 == 0 else "Armor"
    RARITY = "Epic" if 595 % 5 == 0 else "Legendary"
    BASE_VALUE = 29750
    ATTACK_BONUS = 1785
    DEFENSE_BONUS = 1190
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 595."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_595.ITEM_ID, "name": ItemDefinition_595.NAME, "atk": ItemDefinition_595.ATTACK_BONUS, "def": ItemDefinition_595.DEFENSE_BONUS}


class ItemDefinition_596:
    ITEM_ID = "item_596"
    NAME = "Hyperion Legendary Artifact #596"
    TYPE = "Weapon" if 596 % 2 == 0 else "Armor"
    RARITY = "Epic" if 596 % 5 == 0 else "Legendary"
    BASE_VALUE = 29800
    ATTACK_BONUS = 1788
    DEFENSE_BONUS = 1192
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 596."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_596.ITEM_ID, "name": ItemDefinition_596.NAME, "atk": ItemDefinition_596.ATTACK_BONUS, "def": ItemDefinition_596.DEFENSE_BONUS}


class ItemDefinition_597:
    ITEM_ID = "item_597"
    NAME = "Hyperion Legendary Artifact #597"
    TYPE = "Weapon" if 597 % 2 == 0 else "Armor"
    RARITY = "Epic" if 597 % 5 == 0 else "Legendary"
    BASE_VALUE = 29850
    ATTACK_BONUS = 1791
    DEFENSE_BONUS = 1194
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 597."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_597.ITEM_ID, "name": ItemDefinition_597.NAME, "atk": ItemDefinition_597.ATTACK_BONUS, "def": ItemDefinition_597.DEFENSE_BONUS}


class ItemDefinition_598:
    ITEM_ID = "item_598"
    NAME = "Hyperion Legendary Artifact #598"
    TYPE = "Weapon" if 598 % 2 == 0 else "Armor"
    RARITY = "Epic" if 598 % 5 == 0 else "Legendary"
    BASE_VALUE = 29900
    ATTACK_BONUS = 1794
    DEFENSE_BONUS = 1196
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 598."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_598.ITEM_ID, "name": ItemDefinition_598.NAME, "atk": ItemDefinition_598.ATTACK_BONUS, "def": ItemDefinition_598.DEFENSE_BONUS}


class ItemDefinition_599:
    ITEM_ID = "item_599"
    NAME = "Hyperion Legendary Artifact #599"
    TYPE = "Weapon" if 599 % 2 == 0 else "Armor"
    RARITY = "Epic" if 599 % 5 == 0 else "Legendary"
    BASE_VALUE = 29950
    ATTACK_BONUS = 1797
    DEFENSE_BONUS = 1198
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 599."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_599.ITEM_ID, "name": ItemDefinition_599.NAME, "atk": ItemDefinition_599.ATTACK_BONUS, "def": ItemDefinition_599.DEFENSE_BONUS}


class ItemDefinition_600:
    ITEM_ID = "item_600"
    NAME = "Hyperion Legendary Artifact #600"
    TYPE = "Weapon" if 600 % 2 == 0 else "Armor"
    RARITY = "Epic" if 600 % 5 == 0 else "Legendary"
    BASE_VALUE = 30000
    ATTACK_BONUS = 1800
    DEFENSE_BONUS = 1200
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 600."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_600.ITEM_ID, "name": ItemDefinition_600.NAME, "atk": ItemDefinition_600.ATTACK_BONUS, "def": ItemDefinition_600.DEFENSE_BONUS}


class ItemDefinition_601:
    ITEM_ID = "item_601"
    NAME = "Hyperion Legendary Artifact #601"
    TYPE = "Weapon" if 601 % 2 == 0 else "Armor"
    RARITY = "Epic" if 601 % 5 == 0 else "Legendary"
    BASE_VALUE = 30050
    ATTACK_BONUS = 1803
    DEFENSE_BONUS = 1202
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 601."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_601.ITEM_ID, "name": ItemDefinition_601.NAME, "atk": ItemDefinition_601.ATTACK_BONUS, "def": ItemDefinition_601.DEFENSE_BONUS}


class ItemDefinition_602:
    ITEM_ID = "item_602"
    NAME = "Hyperion Legendary Artifact #602"
    TYPE = "Weapon" if 602 % 2 == 0 else "Armor"
    RARITY = "Epic" if 602 % 5 == 0 else "Legendary"
    BASE_VALUE = 30100
    ATTACK_BONUS = 1806
    DEFENSE_BONUS = 1204
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 602."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_602.ITEM_ID, "name": ItemDefinition_602.NAME, "atk": ItemDefinition_602.ATTACK_BONUS, "def": ItemDefinition_602.DEFENSE_BONUS}


class ItemDefinition_603:
    ITEM_ID = "item_603"
    NAME = "Hyperion Legendary Artifact #603"
    TYPE = "Weapon" if 603 % 2 == 0 else "Armor"
    RARITY = "Epic" if 603 % 5 == 0 else "Legendary"
    BASE_VALUE = 30150
    ATTACK_BONUS = 1809
    DEFENSE_BONUS = 1206
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 603."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_603.ITEM_ID, "name": ItemDefinition_603.NAME, "atk": ItemDefinition_603.ATTACK_BONUS, "def": ItemDefinition_603.DEFENSE_BONUS}


class ItemDefinition_604:
    ITEM_ID = "item_604"
    NAME = "Hyperion Legendary Artifact #604"
    TYPE = "Weapon" if 604 % 2 == 0 else "Armor"
    RARITY = "Epic" if 604 % 5 == 0 else "Legendary"
    BASE_VALUE = 30200
    ATTACK_BONUS = 1812
    DEFENSE_BONUS = 1208
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 604."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_604.ITEM_ID, "name": ItemDefinition_604.NAME, "atk": ItemDefinition_604.ATTACK_BONUS, "def": ItemDefinition_604.DEFENSE_BONUS}


class ItemDefinition_605:
    ITEM_ID = "item_605"
    NAME = "Hyperion Legendary Artifact #605"
    TYPE = "Weapon" if 605 % 2 == 0 else "Armor"
    RARITY = "Epic" if 605 % 5 == 0 else "Legendary"
    BASE_VALUE = 30250
    ATTACK_BONUS = 1815
    DEFENSE_BONUS = 1210
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 605."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_605.ITEM_ID, "name": ItemDefinition_605.NAME, "atk": ItemDefinition_605.ATTACK_BONUS, "def": ItemDefinition_605.DEFENSE_BONUS}


class ItemDefinition_606:
    ITEM_ID = "item_606"
    NAME = "Hyperion Legendary Artifact #606"
    TYPE = "Weapon" if 606 % 2 == 0 else "Armor"
    RARITY = "Epic" if 606 % 5 == 0 else "Legendary"
    BASE_VALUE = 30300
    ATTACK_BONUS = 1818
    DEFENSE_BONUS = 1212
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 606."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_606.ITEM_ID, "name": ItemDefinition_606.NAME, "atk": ItemDefinition_606.ATTACK_BONUS, "def": ItemDefinition_606.DEFENSE_BONUS}


class ItemDefinition_607:
    ITEM_ID = "item_607"
    NAME = "Hyperion Legendary Artifact #607"
    TYPE = "Weapon" if 607 % 2 == 0 else "Armor"
    RARITY = "Epic" if 607 % 5 == 0 else "Legendary"
    BASE_VALUE = 30350
    ATTACK_BONUS = 1821
    DEFENSE_BONUS = 1214
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 607."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_607.ITEM_ID, "name": ItemDefinition_607.NAME, "atk": ItemDefinition_607.ATTACK_BONUS, "def": ItemDefinition_607.DEFENSE_BONUS}


class ItemDefinition_608:
    ITEM_ID = "item_608"
    NAME = "Hyperion Legendary Artifact #608"
    TYPE = "Weapon" if 608 % 2 == 0 else "Armor"
    RARITY = "Epic" if 608 % 5 == 0 else "Legendary"
    BASE_VALUE = 30400
    ATTACK_BONUS = 1824
    DEFENSE_BONUS = 1216
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 608."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_608.ITEM_ID, "name": ItemDefinition_608.NAME, "atk": ItemDefinition_608.ATTACK_BONUS, "def": ItemDefinition_608.DEFENSE_BONUS}


class ItemDefinition_609:
    ITEM_ID = "item_609"
    NAME = "Hyperion Legendary Artifact #609"
    TYPE = "Weapon" if 609 % 2 == 0 else "Armor"
    RARITY = "Epic" if 609 % 5 == 0 else "Legendary"
    BASE_VALUE = 30450
    ATTACK_BONUS = 1827
    DEFENSE_BONUS = 1218
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 609."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_609.ITEM_ID, "name": ItemDefinition_609.NAME, "atk": ItemDefinition_609.ATTACK_BONUS, "def": ItemDefinition_609.DEFENSE_BONUS}


class ItemDefinition_610:
    ITEM_ID = "item_610"
    NAME = "Hyperion Legendary Artifact #610"
    TYPE = "Weapon" if 610 % 2 == 0 else "Armor"
    RARITY = "Epic" if 610 % 5 == 0 else "Legendary"
    BASE_VALUE = 30500
    ATTACK_BONUS = 1830
    DEFENSE_BONUS = 1220
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 610."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_610.ITEM_ID, "name": ItemDefinition_610.NAME, "atk": ItemDefinition_610.ATTACK_BONUS, "def": ItemDefinition_610.DEFENSE_BONUS}


class ItemDefinition_611:
    ITEM_ID = "item_611"
    NAME = "Hyperion Legendary Artifact #611"
    TYPE = "Weapon" if 611 % 2 == 0 else "Armor"
    RARITY = "Epic" if 611 % 5 == 0 else "Legendary"
    BASE_VALUE = 30550
    ATTACK_BONUS = 1833
    DEFENSE_BONUS = 1222
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 611."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_611.ITEM_ID, "name": ItemDefinition_611.NAME, "atk": ItemDefinition_611.ATTACK_BONUS, "def": ItemDefinition_611.DEFENSE_BONUS}


class ItemDefinition_612:
    ITEM_ID = "item_612"
    NAME = "Hyperion Legendary Artifact #612"
    TYPE = "Weapon" if 612 % 2 == 0 else "Armor"
    RARITY = "Epic" if 612 % 5 == 0 else "Legendary"
    BASE_VALUE = 30600
    ATTACK_BONUS = 1836
    DEFENSE_BONUS = 1224
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 612."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_612.ITEM_ID, "name": ItemDefinition_612.NAME, "atk": ItemDefinition_612.ATTACK_BONUS, "def": ItemDefinition_612.DEFENSE_BONUS}


class ItemDefinition_613:
    ITEM_ID = "item_613"
    NAME = "Hyperion Legendary Artifact #613"
    TYPE = "Weapon" if 613 % 2 == 0 else "Armor"
    RARITY = "Epic" if 613 % 5 == 0 else "Legendary"
    BASE_VALUE = 30650
    ATTACK_BONUS = 1839
    DEFENSE_BONUS = 1226
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 613."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_613.ITEM_ID, "name": ItemDefinition_613.NAME, "atk": ItemDefinition_613.ATTACK_BONUS, "def": ItemDefinition_613.DEFENSE_BONUS}


class ItemDefinition_614:
    ITEM_ID = "item_614"
    NAME = "Hyperion Legendary Artifact #614"
    TYPE = "Weapon" if 614 % 2 == 0 else "Armor"
    RARITY = "Epic" if 614 % 5 == 0 else "Legendary"
    BASE_VALUE = 30700
    ATTACK_BONUS = 1842
    DEFENSE_BONUS = 1228
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 614."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_614.ITEM_ID, "name": ItemDefinition_614.NAME, "atk": ItemDefinition_614.ATTACK_BONUS, "def": ItemDefinition_614.DEFENSE_BONUS}


class ItemDefinition_615:
    ITEM_ID = "item_615"
    NAME = "Hyperion Legendary Artifact #615"
    TYPE = "Weapon" if 615 % 2 == 0 else "Armor"
    RARITY = "Epic" if 615 % 5 == 0 else "Legendary"
    BASE_VALUE = 30750
    ATTACK_BONUS = 1845
    DEFENSE_BONUS = 1230
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 615."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_615.ITEM_ID, "name": ItemDefinition_615.NAME, "atk": ItemDefinition_615.ATTACK_BONUS, "def": ItemDefinition_615.DEFENSE_BONUS}


class ItemDefinition_616:
    ITEM_ID = "item_616"
    NAME = "Hyperion Legendary Artifact #616"
    TYPE = "Weapon" if 616 % 2 == 0 else "Armor"
    RARITY = "Epic" if 616 % 5 == 0 else "Legendary"
    BASE_VALUE = 30800
    ATTACK_BONUS = 1848
    DEFENSE_BONUS = 1232
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 616."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_616.ITEM_ID, "name": ItemDefinition_616.NAME, "atk": ItemDefinition_616.ATTACK_BONUS, "def": ItemDefinition_616.DEFENSE_BONUS}


class ItemDefinition_617:
    ITEM_ID = "item_617"
    NAME = "Hyperion Legendary Artifact #617"
    TYPE = "Weapon" if 617 % 2 == 0 else "Armor"
    RARITY = "Epic" if 617 % 5 == 0 else "Legendary"
    BASE_VALUE = 30850
    ATTACK_BONUS = 1851
    DEFENSE_BONUS = 1234
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 617."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_617.ITEM_ID, "name": ItemDefinition_617.NAME, "atk": ItemDefinition_617.ATTACK_BONUS, "def": ItemDefinition_617.DEFENSE_BONUS}


class ItemDefinition_618:
    ITEM_ID = "item_618"
    NAME = "Hyperion Legendary Artifact #618"
    TYPE = "Weapon" if 618 % 2 == 0 else "Armor"
    RARITY = "Epic" if 618 % 5 == 0 else "Legendary"
    BASE_VALUE = 30900
    ATTACK_BONUS = 1854
    DEFENSE_BONUS = 1236
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 618."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_618.ITEM_ID, "name": ItemDefinition_618.NAME, "atk": ItemDefinition_618.ATTACK_BONUS, "def": ItemDefinition_618.DEFENSE_BONUS}


class ItemDefinition_619:
    ITEM_ID = "item_619"
    NAME = "Hyperion Legendary Artifact #619"
    TYPE = "Weapon" if 619 % 2 == 0 else "Armor"
    RARITY = "Epic" if 619 % 5 == 0 else "Legendary"
    BASE_VALUE = 30950
    ATTACK_BONUS = 1857
    DEFENSE_BONUS = 1238
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 619."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_619.ITEM_ID, "name": ItemDefinition_619.NAME, "atk": ItemDefinition_619.ATTACK_BONUS, "def": ItemDefinition_619.DEFENSE_BONUS}


class ItemDefinition_620:
    ITEM_ID = "item_620"
    NAME = "Hyperion Legendary Artifact #620"
    TYPE = "Weapon" if 620 % 2 == 0 else "Armor"
    RARITY = "Epic" if 620 % 5 == 0 else "Legendary"
    BASE_VALUE = 31000
    ATTACK_BONUS = 1860
    DEFENSE_BONUS = 1240
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 620."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_620.ITEM_ID, "name": ItemDefinition_620.NAME, "atk": ItemDefinition_620.ATTACK_BONUS, "def": ItemDefinition_620.DEFENSE_BONUS}


class ItemDefinition_621:
    ITEM_ID = "item_621"
    NAME = "Hyperion Legendary Artifact #621"
    TYPE = "Weapon" if 621 % 2 == 0 else "Armor"
    RARITY = "Epic" if 621 % 5 == 0 else "Legendary"
    BASE_VALUE = 31050
    ATTACK_BONUS = 1863
    DEFENSE_BONUS = 1242
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 621."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_621.ITEM_ID, "name": ItemDefinition_621.NAME, "atk": ItemDefinition_621.ATTACK_BONUS, "def": ItemDefinition_621.DEFENSE_BONUS}


class ItemDefinition_622:
    ITEM_ID = "item_622"
    NAME = "Hyperion Legendary Artifact #622"
    TYPE = "Weapon" if 622 % 2 == 0 else "Armor"
    RARITY = "Epic" if 622 % 5 == 0 else "Legendary"
    BASE_VALUE = 31100
    ATTACK_BONUS = 1866
    DEFENSE_BONUS = 1244
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 622."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_622.ITEM_ID, "name": ItemDefinition_622.NAME, "atk": ItemDefinition_622.ATTACK_BONUS, "def": ItemDefinition_622.DEFENSE_BONUS}


class ItemDefinition_623:
    ITEM_ID = "item_623"
    NAME = "Hyperion Legendary Artifact #623"
    TYPE = "Weapon" if 623 % 2 == 0 else "Armor"
    RARITY = "Epic" if 623 % 5 == 0 else "Legendary"
    BASE_VALUE = 31150
    ATTACK_BONUS = 1869
    DEFENSE_BONUS = 1246
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 623."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_623.ITEM_ID, "name": ItemDefinition_623.NAME, "atk": ItemDefinition_623.ATTACK_BONUS, "def": ItemDefinition_623.DEFENSE_BONUS}


class ItemDefinition_624:
    ITEM_ID = "item_624"
    NAME = "Hyperion Legendary Artifact #624"
    TYPE = "Weapon" if 624 % 2 == 0 else "Armor"
    RARITY = "Epic" if 624 % 5 == 0 else "Legendary"
    BASE_VALUE = 31200
    ATTACK_BONUS = 1872
    DEFENSE_BONUS = 1248
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 624."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_624.ITEM_ID, "name": ItemDefinition_624.NAME, "atk": ItemDefinition_624.ATTACK_BONUS, "def": ItemDefinition_624.DEFENSE_BONUS}


class ItemDefinition_625:
    ITEM_ID = "item_625"
    NAME = "Hyperion Legendary Artifact #625"
    TYPE = "Weapon" if 625 % 2 == 0 else "Armor"
    RARITY = "Epic" if 625 % 5 == 0 else "Legendary"
    BASE_VALUE = 31250
    ATTACK_BONUS = 1875
    DEFENSE_BONUS = 1250
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 625."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_625.ITEM_ID, "name": ItemDefinition_625.NAME, "atk": ItemDefinition_625.ATTACK_BONUS, "def": ItemDefinition_625.DEFENSE_BONUS}


class ItemDefinition_626:
    ITEM_ID = "item_626"
    NAME = "Hyperion Legendary Artifact #626"
    TYPE = "Weapon" if 626 % 2 == 0 else "Armor"
    RARITY = "Epic" if 626 % 5 == 0 else "Legendary"
    BASE_VALUE = 31300
    ATTACK_BONUS = 1878
    DEFENSE_BONUS = 1252
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 626."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_626.ITEM_ID, "name": ItemDefinition_626.NAME, "atk": ItemDefinition_626.ATTACK_BONUS, "def": ItemDefinition_626.DEFENSE_BONUS}


class ItemDefinition_627:
    ITEM_ID = "item_627"
    NAME = "Hyperion Legendary Artifact #627"
    TYPE = "Weapon" if 627 % 2 == 0 else "Armor"
    RARITY = "Epic" if 627 % 5 == 0 else "Legendary"
    BASE_VALUE = 31350
    ATTACK_BONUS = 1881
    DEFENSE_BONUS = 1254
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 627."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_627.ITEM_ID, "name": ItemDefinition_627.NAME, "atk": ItemDefinition_627.ATTACK_BONUS, "def": ItemDefinition_627.DEFENSE_BONUS}


class ItemDefinition_628:
    ITEM_ID = "item_628"
    NAME = "Hyperion Legendary Artifact #628"
    TYPE = "Weapon" if 628 % 2 == 0 else "Armor"
    RARITY = "Epic" if 628 % 5 == 0 else "Legendary"
    BASE_VALUE = 31400
    ATTACK_BONUS = 1884
    DEFENSE_BONUS = 1256
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 628."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_628.ITEM_ID, "name": ItemDefinition_628.NAME, "atk": ItemDefinition_628.ATTACK_BONUS, "def": ItemDefinition_628.DEFENSE_BONUS}


class ItemDefinition_629:
    ITEM_ID = "item_629"
    NAME = "Hyperion Legendary Artifact #629"
    TYPE = "Weapon" if 629 % 2 == 0 else "Armor"
    RARITY = "Epic" if 629 % 5 == 0 else "Legendary"
    BASE_VALUE = 31450
    ATTACK_BONUS = 1887
    DEFENSE_BONUS = 1258
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 629."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_629.ITEM_ID, "name": ItemDefinition_629.NAME, "atk": ItemDefinition_629.ATTACK_BONUS, "def": ItemDefinition_629.DEFENSE_BONUS}


class ItemDefinition_630:
    ITEM_ID = "item_630"
    NAME = "Hyperion Legendary Artifact #630"
    TYPE = "Weapon" if 630 % 2 == 0 else "Armor"
    RARITY = "Epic" if 630 % 5 == 0 else "Legendary"
    BASE_VALUE = 31500
    ATTACK_BONUS = 1890
    DEFENSE_BONUS = 1260
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 630."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_630.ITEM_ID, "name": ItemDefinition_630.NAME, "atk": ItemDefinition_630.ATTACK_BONUS, "def": ItemDefinition_630.DEFENSE_BONUS}


class ItemDefinition_631:
    ITEM_ID = "item_631"
    NAME = "Hyperion Legendary Artifact #631"
    TYPE = "Weapon" if 631 % 2 == 0 else "Armor"
    RARITY = "Epic" if 631 % 5 == 0 else "Legendary"
    BASE_VALUE = 31550
    ATTACK_BONUS = 1893
    DEFENSE_BONUS = 1262
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 631."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_631.ITEM_ID, "name": ItemDefinition_631.NAME, "atk": ItemDefinition_631.ATTACK_BONUS, "def": ItemDefinition_631.DEFENSE_BONUS}


class ItemDefinition_632:
    ITEM_ID = "item_632"
    NAME = "Hyperion Legendary Artifact #632"
    TYPE = "Weapon" if 632 % 2 == 0 else "Armor"
    RARITY = "Epic" if 632 % 5 == 0 else "Legendary"
    BASE_VALUE = 31600
    ATTACK_BONUS = 1896
    DEFENSE_BONUS = 1264
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 632."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_632.ITEM_ID, "name": ItemDefinition_632.NAME, "atk": ItemDefinition_632.ATTACK_BONUS, "def": ItemDefinition_632.DEFENSE_BONUS}


class ItemDefinition_633:
    ITEM_ID = "item_633"
    NAME = "Hyperion Legendary Artifact #633"
    TYPE = "Weapon" if 633 % 2 == 0 else "Armor"
    RARITY = "Epic" if 633 % 5 == 0 else "Legendary"
    BASE_VALUE = 31650
    ATTACK_BONUS = 1899
    DEFENSE_BONUS = 1266
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 633."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_633.ITEM_ID, "name": ItemDefinition_633.NAME, "atk": ItemDefinition_633.ATTACK_BONUS, "def": ItemDefinition_633.DEFENSE_BONUS}


class ItemDefinition_634:
    ITEM_ID = "item_634"
    NAME = "Hyperion Legendary Artifact #634"
    TYPE = "Weapon" if 634 % 2 == 0 else "Armor"
    RARITY = "Epic" if 634 % 5 == 0 else "Legendary"
    BASE_VALUE = 31700
    ATTACK_BONUS = 1902
    DEFENSE_BONUS = 1268
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 634."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_634.ITEM_ID, "name": ItemDefinition_634.NAME, "atk": ItemDefinition_634.ATTACK_BONUS, "def": ItemDefinition_634.DEFENSE_BONUS}


class ItemDefinition_635:
    ITEM_ID = "item_635"
    NAME = "Hyperion Legendary Artifact #635"
    TYPE = "Weapon" if 635 % 2 == 0 else "Armor"
    RARITY = "Epic" if 635 % 5 == 0 else "Legendary"
    BASE_VALUE = 31750
    ATTACK_BONUS = 1905
    DEFENSE_BONUS = 1270
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 635."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_635.ITEM_ID, "name": ItemDefinition_635.NAME, "atk": ItemDefinition_635.ATTACK_BONUS, "def": ItemDefinition_635.DEFENSE_BONUS}


class ItemDefinition_636:
    ITEM_ID = "item_636"
    NAME = "Hyperion Legendary Artifact #636"
    TYPE = "Weapon" if 636 % 2 == 0 else "Armor"
    RARITY = "Epic" if 636 % 5 == 0 else "Legendary"
    BASE_VALUE = 31800
    ATTACK_BONUS = 1908
    DEFENSE_BONUS = 1272
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 636."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_636.ITEM_ID, "name": ItemDefinition_636.NAME, "atk": ItemDefinition_636.ATTACK_BONUS, "def": ItemDefinition_636.DEFENSE_BONUS}


class ItemDefinition_637:
    ITEM_ID = "item_637"
    NAME = "Hyperion Legendary Artifact #637"
    TYPE = "Weapon" if 637 % 2 == 0 else "Armor"
    RARITY = "Epic" if 637 % 5 == 0 else "Legendary"
    BASE_VALUE = 31850
    ATTACK_BONUS = 1911
    DEFENSE_BONUS = 1274
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 637."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_637.ITEM_ID, "name": ItemDefinition_637.NAME, "atk": ItemDefinition_637.ATTACK_BONUS, "def": ItemDefinition_637.DEFENSE_BONUS}


class ItemDefinition_638:
    ITEM_ID = "item_638"
    NAME = "Hyperion Legendary Artifact #638"
    TYPE = "Weapon" if 638 % 2 == 0 else "Armor"
    RARITY = "Epic" if 638 % 5 == 0 else "Legendary"
    BASE_VALUE = 31900
    ATTACK_BONUS = 1914
    DEFENSE_BONUS = 1276
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 638."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_638.ITEM_ID, "name": ItemDefinition_638.NAME, "atk": ItemDefinition_638.ATTACK_BONUS, "def": ItemDefinition_638.DEFENSE_BONUS}


class ItemDefinition_639:
    ITEM_ID = "item_639"
    NAME = "Hyperion Legendary Artifact #639"
    TYPE = "Weapon" if 639 % 2 == 0 else "Armor"
    RARITY = "Epic" if 639 % 5 == 0 else "Legendary"
    BASE_VALUE = 31950
    ATTACK_BONUS = 1917
    DEFENSE_BONUS = 1278
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 639."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_639.ITEM_ID, "name": ItemDefinition_639.NAME, "atk": ItemDefinition_639.ATTACK_BONUS, "def": ItemDefinition_639.DEFENSE_BONUS}


class ItemDefinition_640:
    ITEM_ID = "item_640"
    NAME = "Hyperion Legendary Artifact #640"
    TYPE = "Weapon" if 640 % 2 == 0 else "Armor"
    RARITY = "Epic" if 640 % 5 == 0 else "Legendary"
    BASE_VALUE = 32000
    ATTACK_BONUS = 1920
    DEFENSE_BONUS = 1280
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 640."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_640.ITEM_ID, "name": ItemDefinition_640.NAME, "atk": ItemDefinition_640.ATTACK_BONUS, "def": ItemDefinition_640.DEFENSE_BONUS}


class ItemDefinition_641:
    ITEM_ID = "item_641"
    NAME = "Hyperion Legendary Artifact #641"
    TYPE = "Weapon" if 641 % 2 == 0 else "Armor"
    RARITY = "Epic" if 641 % 5 == 0 else "Legendary"
    BASE_VALUE = 32050
    ATTACK_BONUS = 1923
    DEFENSE_BONUS = 1282
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 641."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_641.ITEM_ID, "name": ItemDefinition_641.NAME, "atk": ItemDefinition_641.ATTACK_BONUS, "def": ItemDefinition_641.DEFENSE_BONUS}


class ItemDefinition_642:
    ITEM_ID = "item_642"
    NAME = "Hyperion Legendary Artifact #642"
    TYPE = "Weapon" if 642 % 2 == 0 else "Armor"
    RARITY = "Epic" if 642 % 5 == 0 else "Legendary"
    BASE_VALUE = 32100
    ATTACK_BONUS = 1926
    DEFENSE_BONUS = 1284
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 642."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_642.ITEM_ID, "name": ItemDefinition_642.NAME, "atk": ItemDefinition_642.ATTACK_BONUS, "def": ItemDefinition_642.DEFENSE_BONUS}


class ItemDefinition_643:
    ITEM_ID = "item_643"
    NAME = "Hyperion Legendary Artifact #643"
    TYPE = "Weapon" if 643 % 2 == 0 else "Armor"
    RARITY = "Epic" if 643 % 5 == 0 else "Legendary"
    BASE_VALUE = 32150
    ATTACK_BONUS = 1929
    DEFENSE_BONUS = 1286
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 643."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_643.ITEM_ID, "name": ItemDefinition_643.NAME, "atk": ItemDefinition_643.ATTACK_BONUS, "def": ItemDefinition_643.DEFENSE_BONUS}


class ItemDefinition_644:
    ITEM_ID = "item_644"
    NAME = "Hyperion Legendary Artifact #644"
    TYPE = "Weapon" if 644 % 2 == 0 else "Armor"
    RARITY = "Epic" if 644 % 5 == 0 else "Legendary"
    BASE_VALUE = 32200
    ATTACK_BONUS = 1932
    DEFENSE_BONUS = 1288
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 644."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_644.ITEM_ID, "name": ItemDefinition_644.NAME, "atk": ItemDefinition_644.ATTACK_BONUS, "def": ItemDefinition_644.DEFENSE_BONUS}


class ItemDefinition_645:
    ITEM_ID = "item_645"
    NAME = "Hyperion Legendary Artifact #645"
    TYPE = "Weapon" if 645 % 2 == 0 else "Armor"
    RARITY = "Epic" if 645 % 5 == 0 else "Legendary"
    BASE_VALUE = 32250
    ATTACK_BONUS = 1935
    DEFENSE_BONUS = 1290
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 645."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_645.ITEM_ID, "name": ItemDefinition_645.NAME, "atk": ItemDefinition_645.ATTACK_BONUS, "def": ItemDefinition_645.DEFENSE_BONUS}


class ItemDefinition_646:
    ITEM_ID = "item_646"
    NAME = "Hyperion Legendary Artifact #646"
    TYPE = "Weapon" if 646 % 2 == 0 else "Armor"
    RARITY = "Epic" if 646 % 5 == 0 else "Legendary"
    BASE_VALUE = 32300
    ATTACK_BONUS = 1938
    DEFENSE_BONUS = 1292
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 646."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_646.ITEM_ID, "name": ItemDefinition_646.NAME, "atk": ItemDefinition_646.ATTACK_BONUS, "def": ItemDefinition_646.DEFENSE_BONUS}


class ItemDefinition_647:
    ITEM_ID = "item_647"
    NAME = "Hyperion Legendary Artifact #647"
    TYPE = "Weapon" if 647 % 2 == 0 else "Armor"
    RARITY = "Epic" if 647 % 5 == 0 else "Legendary"
    BASE_VALUE = 32350
    ATTACK_BONUS = 1941
    DEFENSE_BONUS = 1294
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 647."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_647.ITEM_ID, "name": ItemDefinition_647.NAME, "atk": ItemDefinition_647.ATTACK_BONUS, "def": ItemDefinition_647.DEFENSE_BONUS}


class ItemDefinition_648:
    ITEM_ID = "item_648"
    NAME = "Hyperion Legendary Artifact #648"
    TYPE = "Weapon" if 648 % 2 == 0 else "Armor"
    RARITY = "Epic" if 648 % 5 == 0 else "Legendary"
    BASE_VALUE = 32400
    ATTACK_BONUS = 1944
    DEFENSE_BONUS = 1296
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 648."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_648.ITEM_ID, "name": ItemDefinition_648.NAME, "atk": ItemDefinition_648.ATTACK_BONUS, "def": ItemDefinition_648.DEFENSE_BONUS}


class ItemDefinition_649:
    ITEM_ID = "item_649"
    NAME = "Hyperion Legendary Artifact #649"
    TYPE = "Weapon" if 649 % 2 == 0 else "Armor"
    RARITY = "Epic" if 649 % 5 == 0 else "Legendary"
    BASE_VALUE = 32450
    ATTACK_BONUS = 1947
    DEFENSE_BONUS = 1298
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 649."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_649.ITEM_ID, "name": ItemDefinition_649.NAME, "atk": ItemDefinition_649.ATTACK_BONUS, "def": ItemDefinition_649.DEFENSE_BONUS}


class ItemDefinition_650:
    ITEM_ID = "item_650"
    NAME = "Hyperion Legendary Artifact #650"
    TYPE = "Weapon" if 650 % 2 == 0 else "Armor"
    RARITY = "Epic" if 650 % 5 == 0 else "Legendary"
    BASE_VALUE = 32500
    ATTACK_BONUS = 1950
    DEFENSE_BONUS = 1300
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 650."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_650.ITEM_ID, "name": ItemDefinition_650.NAME, "atk": ItemDefinition_650.ATTACK_BONUS, "def": ItemDefinition_650.DEFENSE_BONUS}


class ItemDefinition_651:
    ITEM_ID = "item_651"
    NAME = "Hyperion Legendary Artifact #651"
    TYPE = "Weapon" if 651 % 2 == 0 else "Armor"
    RARITY = "Epic" if 651 % 5 == 0 else "Legendary"
    BASE_VALUE = 32550
    ATTACK_BONUS = 1953
    DEFENSE_BONUS = 1302
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 651."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_651.ITEM_ID, "name": ItemDefinition_651.NAME, "atk": ItemDefinition_651.ATTACK_BONUS, "def": ItemDefinition_651.DEFENSE_BONUS}


class ItemDefinition_652:
    ITEM_ID = "item_652"
    NAME = "Hyperion Legendary Artifact #652"
    TYPE = "Weapon" if 652 % 2 == 0 else "Armor"
    RARITY = "Epic" if 652 % 5 == 0 else "Legendary"
    BASE_VALUE = 32600
    ATTACK_BONUS = 1956
    DEFENSE_BONUS = 1304
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 652."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_652.ITEM_ID, "name": ItemDefinition_652.NAME, "atk": ItemDefinition_652.ATTACK_BONUS, "def": ItemDefinition_652.DEFENSE_BONUS}


class ItemDefinition_653:
    ITEM_ID = "item_653"
    NAME = "Hyperion Legendary Artifact #653"
    TYPE = "Weapon" if 653 % 2 == 0 else "Armor"
    RARITY = "Epic" if 653 % 5 == 0 else "Legendary"
    BASE_VALUE = 32650
    ATTACK_BONUS = 1959
    DEFENSE_BONUS = 1306
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 653."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_653.ITEM_ID, "name": ItemDefinition_653.NAME, "atk": ItemDefinition_653.ATTACK_BONUS, "def": ItemDefinition_653.DEFENSE_BONUS}


class ItemDefinition_654:
    ITEM_ID = "item_654"
    NAME = "Hyperion Legendary Artifact #654"
    TYPE = "Weapon" if 654 % 2 == 0 else "Armor"
    RARITY = "Epic" if 654 % 5 == 0 else "Legendary"
    BASE_VALUE = 32700
    ATTACK_BONUS = 1962
    DEFENSE_BONUS = 1308
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 654."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_654.ITEM_ID, "name": ItemDefinition_654.NAME, "atk": ItemDefinition_654.ATTACK_BONUS, "def": ItemDefinition_654.DEFENSE_BONUS}


class ItemDefinition_655:
    ITEM_ID = "item_655"
    NAME = "Hyperion Legendary Artifact #655"
    TYPE = "Weapon" if 655 % 2 == 0 else "Armor"
    RARITY = "Epic" if 655 % 5 == 0 else "Legendary"
    BASE_VALUE = 32750
    ATTACK_BONUS = 1965
    DEFENSE_BONUS = 1310
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 655."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_655.ITEM_ID, "name": ItemDefinition_655.NAME, "atk": ItemDefinition_655.ATTACK_BONUS, "def": ItemDefinition_655.DEFENSE_BONUS}


class ItemDefinition_656:
    ITEM_ID = "item_656"
    NAME = "Hyperion Legendary Artifact #656"
    TYPE = "Weapon" if 656 % 2 == 0 else "Armor"
    RARITY = "Epic" if 656 % 5 == 0 else "Legendary"
    BASE_VALUE = 32800
    ATTACK_BONUS = 1968
    DEFENSE_BONUS = 1312
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 656."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_656.ITEM_ID, "name": ItemDefinition_656.NAME, "atk": ItemDefinition_656.ATTACK_BONUS, "def": ItemDefinition_656.DEFENSE_BONUS}


class ItemDefinition_657:
    ITEM_ID = "item_657"
    NAME = "Hyperion Legendary Artifact #657"
    TYPE = "Weapon" if 657 % 2 == 0 else "Armor"
    RARITY = "Epic" if 657 % 5 == 0 else "Legendary"
    BASE_VALUE = 32850
    ATTACK_BONUS = 1971
    DEFENSE_BONUS = 1314
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 657."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_657.ITEM_ID, "name": ItemDefinition_657.NAME, "atk": ItemDefinition_657.ATTACK_BONUS, "def": ItemDefinition_657.DEFENSE_BONUS}


class ItemDefinition_658:
    ITEM_ID = "item_658"
    NAME = "Hyperion Legendary Artifact #658"
    TYPE = "Weapon" if 658 % 2 == 0 else "Armor"
    RARITY = "Epic" if 658 % 5 == 0 else "Legendary"
    BASE_VALUE = 32900
    ATTACK_BONUS = 1974
    DEFENSE_BONUS = 1316
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 658."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_658.ITEM_ID, "name": ItemDefinition_658.NAME, "atk": ItemDefinition_658.ATTACK_BONUS, "def": ItemDefinition_658.DEFENSE_BONUS}


class ItemDefinition_659:
    ITEM_ID = "item_659"
    NAME = "Hyperion Legendary Artifact #659"
    TYPE = "Weapon" if 659 % 2 == 0 else "Armor"
    RARITY = "Epic" if 659 % 5 == 0 else "Legendary"
    BASE_VALUE = 32950
    ATTACK_BONUS = 1977
    DEFENSE_BONUS = 1318
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 659."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_659.ITEM_ID, "name": ItemDefinition_659.NAME, "atk": ItemDefinition_659.ATTACK_BONUS, "def": ItemDefinition_659.DEFENSE_BONUS}


class ItemDefinition_660:
    ITEM_ID = "item_660"
    NAME = "Hyperion Legendary Artifact #660"
    TYPE = "Weapon" if 660 % 2 == 0 else "Armor"
    RARITY = "Epic" if 660 % 5 == 0 else "Legendary"
    BASE_VALUE = 33000
    ATTACK_BONUS = 1980
    DEFENSE_BONUS = 1320
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 660."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_660.ITEM_ID, "name": ItemDefinition_660.NAME, "atk": ItemDefinition_660.ATTACK_BONUS, "def": ItemDefinition_660.DEFENSE_BONUS}


class ItemDefinition_661:
    ITEM_ID = "item_661"
    NAME = "Hyperion Legendary Artifact #661"
    TYPE = "Weapon" if 661 % 2 == 0 else "Armor"
    RARITY = "Epic" if 661 % 5 == 0 else "Legendary"
    BASE_VALUE = 33050
    ATTACK_BONUS = 1983
    DEFENSE_BONUS = 1322
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 661."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_661.ITEM_ID, "name": ItemDefinition_661.NAME, "atk": ItemDefinition_661.ATTACK_BONUS, "def": ItemDefinition_661.DEFENSE_BONUS}


class ItemDefinition_662:
    ITEM_ID = "item_662"
    NAME = "Hyperion Legendary Artifact #662"
    TYPE = "Weapon" if 662 % 2 == 0 else "Armor"
    RARITY = "Epic" if 662 % 5 == 0 else "Legendary"
    BASE_VALUE = 33100
    ATTACK_BONUS = 1986
    DEFENSE_BONUS = 1324
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 662."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_662.ITEM_ID, "name": ItemDefinition_662.NAME, "atk": ItemDefinition_662.ATTACK_BONUS, "def": ItemDefinition_662.DEFENSE_BONUS}


class ItemDefinition_663:
    ITEM_ID = "item_663"
    NAME = "Hyperion Legendary Artifact #663"
    TYPE = "Weapon" if 663 % 2 == 0 else "Armor"
    RARITY = "Epic" if 663 % 5 == 0 else "Legendary"
    BASE_VALUE = 33150
    ATTACK_BONUS = 1989
    DEFENSE_BONUS = 1326
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 663."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_663.ITEM_ID, "name": ItemDefinition_663.NAME, "atk": ItemDefinition_663.ATTACK_BONUS, "def": ItemDefinition_663.DEFENSE_BONUS}


class ItemDefinition_664:
    ITEM_ID = "item_664"
    NAME = "Hyperion Legendary Artifact #664"
    TYPE = "Weapon" if 664 % 2 == 0 else "Armor"
    RARITY = "Epic" if 664 % 5 == 0 else "Legendary"
    BASE_VALUE = 33200
    ATTACK_BONUS = 1992
    DEFENSE_BONUS = 1328
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 664."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_664.ITEM_ID, "name": ItemDefinition_664.NAME, "atk": ItemDefinition_664.ATTACK_BONUS, "def": ItemDefinition_664.DEFENSE_BONUS}


class ItemDefinition_665:
    ITEM_ID = "item_665"
    NAME = "Hyperion Legendary Artifact #665"
    TYPE = "Weapon" if 665 % 2 == 0 else "Armor"
    RARITY = "Epic" if 665 % 5 == 0 else "Legendary"
    BASE_VALUE = 33250
    ATTACK_BONUS = 1995
    DEFENSE_BONUS = 1330
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 665."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_665.ITEM_ID, "name": ItemDefinition_665.NAME, "atk": ItemDefinition_665.ATTACK_BONUS, "def": ItemDefinition_665.DEFENSE_BONUS}


class ItemDefinition_666:
    ITEM_ID = "item_666"
    NAME = "Hyperion Legendary Artifact #666"
    TYPE = "Weapon" if 666 % 2 == 0 else "Armor"
    RARITY = "Epic" if 666 % 5 == 0 else "Legendary"
    BASE_VALUE = 33300
    ATTACK_BONUS = 1998
    DEFENSE_BONUS = 1332
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 666."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_666.ITEM_ID, "name": ItemDefinition_666.NAME, "atk": ItemDefinition_666.ATTACK_BONUS, "def": ItemDefinition_666.DEFENSE_BONUS}


class ItemDefinition_667:
    ITEM_ID = "item_667"
    NAME = "Hyperion Legendary Artifact #667"
    TYPE = "Weapon" if 667 % 2 == 0 else "Armor"
    RARITY = "Epic" if 667 % 5 == 0 else "Legendary"
    BASE_VALUE = 33350
    ATTACK_BONUS = 2001
    DEFENSE_BONUS = 1334
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 667."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_667.ITEM_ID, "name": ItemDefinition_667.NAME, "atk": ItemDefinition_667.ATTACK_BONUS, "def": ItemDefinition_667.DEFENSE_BONUS}


class ItemDefinition_668:
    ITEM_ID = "item_668"
    NAME = "Hyperion Legendary Artifact #668"
    TYPE = "Weapon" if 668 % 2 == 0 else "Armor"
    RARITY = "Epic" if 668 % 5 == 0 else "Legendary"
    BASE_VALUE = 33400
    ATTACK_BONUS = 2004
    DEFENSE_BONUS = 1336
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 668."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_668.ITEM_ID, "name": ItemDefinition_668.NAME, "atk": ItemDefinition_668.ATTACK_BONUS, "def": ItemDefinition_668.DEFENSE_BONUS}


class ItemDefinition_669:
    ITEM_ID = "item_669"
    NAME = "Hyperion Legendary Artifact #669"
    TYPE = "Weapon" if 669 % 2 == 0 else "Armor"
    RARITY = "Epic" if 669 % 5 == 0 else "Legendary"
    BASE_VALUE = 33450
    ATTACK_BONUS = 2007
    DEFENSE_BONUS = 1338
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 669."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_669.ITEM_ID, "name": ItemDefinition_669.NAME, "atk": ItemDefinition_669.ATTACK_BONUS, "def": ItemDefinition_669.DEFENSE_BONUS}


class ItemDefinition_670:
    ITEM_ID = "item_670"
    NAME = "Hyperion Legendary Artifact #670"
    TYPE = "Weapon" if 670 % 2 == 0 else "Armor"
    RARITY = "Epic" if 670 % 5 == 0 else "Legendary"
    BASE_VALUE = 33500
    ATTACK_BONUS = 2010
    DEFENSE_BONUS = 1340
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 670."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_670.ITEM_ID, "name": ItemDefinition_670.NAME, "atk": ItemDefinition_670.ATTACK_BONUS, "def": ItemDefinition_670.DEFENSE_BONUS}


class ItemDefinition_671:
    ITEM_ID = "item_671"
    NAME = "Hyperion Legendary Artifact #671"
    TYPE = "Weapon" if 671 % 2 == 0 else "Armor"
    RARITY = "Epic" if 671 % 5 == 0 else "Legendary"
    BASE_VALUE = 33550
    ATTACK_BONUS = 2013
    DEFENSE_BONUS = 1342
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 671."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_671.ITEM_ID, "name": ItemDefinition_671.NAME, "atk": ItemDefinition_671.ATTACK_BONUS, "def": ItemDefinition_671.DEFENSE_BONUS}


class ItemDefinition_672:
    ITEM_ID = "item_672"
    NAME = "Hyperion Legendary Artifact #672"
    TYPE = "Weapon" if 672 % 2 == 0 else "Armor"
    RARITY = "Epic" if 672 % 5 == 0 else "Legendary"
    BASE_VALUE = 33600
    ATTACK_BONUS = 2016
    DEFENSE_BONUS = 1344
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 672."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_672.ITEM_ID, "name": ItemDefinition_672.NAME, "atk": ItemDefinition_672.ATTACK_BONUS, "def": ItemDefinition_672.DEFENSE_BONUS}


class ItemDefinition_673:
    ITEM_ID = "item_673"
    NAME = "Hyperion Legendary Artifact #673"
    TYPE = "Weapon" if 673 % 2 == 0 else "Armor"
    RARITY = "Epic" if 673 % 5 == 0 else "Legendary"
    BASE_VALUE = 33650
    ATTACK_BONUS = 2019
    DEFENSE_BONUS = 1346
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 673."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_673.ITEM_ID, "name": ItemDefinition_673.NAME, "atk": ItemDefinition_673.ATTACK_BONUS, "def": ItemDefinition_673.DEFENSE_BONUS}


class ItemDefinition_674:
    ITEM_ID = "item_674"
    NAME = "Hyperion Legendary Artifact #674"
    TYPE = "Weapon" if 674 % 2 == 0 else "Armor"
    RARITY = "Epic" if 674 % 5 == 0 else "Legendary"
    BASE_VALUE = 33700
    ATTACK_BONUS = 2022
    DEFENSE_BONUS = 1348
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 674."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_674.ITEM_ID, "name": ItemDefinition_674.NAME, "atk": ItemDefinition_674.ATTACK_BONUS, "def": ItemDefinition_674.DEFENSE_BONUS}


class ItemDefinition_675:
    ITEM_ID = "item_675"
    NAME = "Hyperion Legendary Artifact #675"
    TYPE = "Weapon" if 675 % 2 == 0 else "Armor"
    RARITY = "Epic" if 675 % 5 == 0 else "Legendary"
    BASE_VALUE = 33750
    ATTACK_BONUS = 2025
    DEFENSE_BONUS = 1350
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 675."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_675.ITEM_ID, "name": ItemDefinition_675.NAME, "atk": ItemDefinition_675.ATTACK_BONUS, "def": ItemDefinition_675.DEFENSE_BONUS}


class ItemDefinition_676:
    ITEM_ID = "item_676"
    NAME = "Hyperion Legendary Artifact #676"
    TYPE = "Weapon" if 676 % 2 == 0 else "Armor"
    RARITY = "Epic" if 676 % 5 == 0 else "Legendary"
    BASE_VALUE = 33800
    ATTACK_BONUS = 2028
    DEFENSE_BONUS = 1352
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 676."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_676.ITEM_ID, "name": ItemDefinition_676.NAME, "atk": ItemDefinition_676.ATTACK_BONUS, "def": ItemDefinition_676.DEFENSE_BONUS}


class ItemDefinition_677:
    ITEM_ID = "item_677"
    NAME = "Hyperion Legendary Artifact #677"
    TYPE = "Weapon" if 677 % 2 == 0 else "Armor"
    RARITY = "Epic" if 677 % 5 == 0 else "Legendary"
    BASE_VALUE = 33850
    ATTACK_BONUS = 2031
    DEFENSE_BONUS = 1354
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 677."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_677.ITEM_ID, "name": ItemDefinition_677.NAME, "atk": ItemDefinition_677.ATTACK_BONUS, "def": ItemDefinition_677.DEFENSE_BONUS}


class ItemDefinition_678:
    ITEM_ID = "item_678"
    NAME = "Hyperion Legendary Artifact #678"
    TYPE = "Weapon" if 678 % 2 == 0 else "Armor"
    RARITY = "Epic" if 678 % 5 == 0 else "Legendary"
    BASE_VALUE = 33900
    ATTACK_BONUS = 2034
    DEFENSE_BONUS = 1356
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 678."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_678.ITEM_ID, "name": ItemDefinition_678.NAME, "atk": ItemDefinition_678.ATTACK_BONUS, "def": ItemDefinition_678.DEFENSE_BONUS}


class ItemDefinition_679:
    ITEM_ID = "item_679"
    NAME = "Hyperion Legendary Artifact #679"
    TYPE = "Weapon" if 679 % 2 == 0 else "Armor"
    RARITY = "Epic" if 679 % 5 == 0 else "Legendary"
    BASE_VALUE = 33950
    ATTACK_BONUS = 2037
    DEFENSE_BONUS = 1358
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 679."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_679.ITEM_ID, "name": ItemDefinition_679.NAME, "atk": ItemDefinition_679.ATTACK_BONUS, "def": ItemDefinition_679.DEFENSE_BONUS}


class ItemDefinition_680:
    ITEM_ID = "item_680"
    NAME = "Hyperion Legendary Artifact #680"
    TYPE = "Weapon" if 680 % 2 == 0 else "Armor"
    RARITY = "Epic" if 680 % 5 == 0 else "Legendary"
    BASE_VALUE = 34000
    ATTACK_BONUS = 2040
    DEFENSE_BONUS = 1360
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 680."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_680.ITEM_ID, "name": ItemDefinition_680.NAME, "atk": ItemDefinition_680.ATTACK_BONUS, "def": ItemDefinition_680.DEFENSE_BONUS}


class ItemDefinition_681:
    ITEM_ID = "item_681"
    NAME = "Hyperion Legendary Artifact #681"
    TYPE = "Weapon" if 681 % 2 == 0 else "Armor"
    RARITY = "Epic" if 681 % 5 == 0 else "Legendary"
    BASE_VALUE = 34050
    ATTACK_BONUS = 2043
    DEFENSE_BONUS = 1362
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 681."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_681.ITEM_ID, "name": ItemDefinition_681.NAME, "atk": ItemDefinition_681.ATTACK_BONUS, "def": ItemDefinition_681.DEFENSE_BONUS}


class ItemDefinition_682:
    ITEM_ID = "item_682"
    NAME = "Hyperion Legendary Artifact #682"
    TYPE = "Weapon" if 682 % 2 == 0 else "Armor"
    RARITY = "Epic" if 682 % 5 == 0 else "Legendary"
    BASE_VALUE = 34100
    ATTACK_BONUS = 2046
    DEFENSE_BONUS = 1364
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 682."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_682.ITEM_ID, "name": ItemDefinition_682.NAME, "atk": ItemDefinition_682.ATTACK_BONUS, "def": ItemDefinition_682.DEFENSE_BONUS}


class ItemDefinition_683:
    ITEM_ID = "item_683"
    NAME = "Hyperion Legendary Artifact #683"
    TYPE = "Weapon" if 683 % 2 == 0 else "Armor"
    RARITY = "Epic" if 683 % 5 == 0 else "Legendary"
    BASE_VALUE = 34150
    ATTACK_BONUS = 2049
    DEFENSE_BONUS = 1366
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 683."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_683.ITEM_ID, "name": ItemDefinition_683.NAME, "atk": ItemDefinition_683.ATTACK_BONUS, "def": ItemDefinition_683.DEFENSE_BONUS}


class ItemDefinition_684:
    ITEM_ID = "item_684"
    NAME = "Hyperion Legendary Artifact #684"
    TYPE = "Weapon" if 684 % 2 == 0 else "Armor"
    RARITY = "Epic" if 684 % 5 == 0 else "Legendary"
    BASE_VALUE = 34200
    ATTACK_BONUS = 2052
    DEFENSE_BONUS = 1368
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 684."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_684.ITEM_ID, "name": ItemDefinition_684.NAME, "atk": ItemDefinition_684.ATTACK_BONUS, "def": ItemDefinition_684.DEFENSE_BONUS}


class ItemDefinition_685:
    ITEM_ID = "item_685"
    NAME = "Hyperion Legendary Artifact #685"
    TYPE = "Weapon" if 685 % 2 == 0 else "Armor"
    RARITY = "Epic" if 685 % 5 == 0 else "Legendary"
    BASE_VALUE = 34250
    ATTACK_BONUS = 2055
    DEFENSE_BONUS = 1370
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 685."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_685.ITEM_ID, "name": ItemDefinition_685.NAME, "atk": ItemDefinition_685.ATTACK_BONUS, "def": ItemDefinition_685.DEFENSE_BONUS}


class ItemDefinition_686:
    ITEM_ID = "item_686"
    NAME = "Hyperion Legendary Artifact #686"
    TYPE = "Weapon" if 686 % 2 == 0 else "Armor"
    RARITY = "Epic" if 686 % 5 == 0 else "Legendary"
    BASE_VALUE = 34300
    ATTACK_BONUS = 2058
    DEFENSE_BONUS = 1372
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 686."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_686.ITEM_ID, "name": ItemDefinition_686.NAME, "atk": ItemDefinition_686.ATTACK_BONUS, "def": ItemDefinition_686.DEFENSE_BONUS}


class ItemDefinition_687:
    ITEM_ID = "item_687"
    NAME = "Hyperion Legendary Artifact #687"
    TYPE = "Weapon" if 687 % 2 == 0 else "Armor"
    RARITY = "Epic" if 687 % 5 == 0 else "Legendary"
    BASE_VALUE = 34350
    ATTACK_BONUS = 2061
    DEFENSE_BONUS = 1374
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 687."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_687.ITEM_ID, "name": ItemDefinition_687.NAME, "atk": ItemDefinition_687.ATTACK_BONUS, "def": ItemDefinition_687.DEFENSE_BONUS}


class ItemDefinition_688:
    ITEM_ID = "item_688"
    NAME = "Hyperion Legendary Artifact #688"
    TYPE = "Weapon" if 688 % 2 == 0 else "Armor"
    RARITY = "Epic" if 688 % 5 == 0 else "Legendary"
    BASE_VALUE = 34400
    ATTACK_BONUS = 2064
    DEFENSE_BONUS = 1376
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 688."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_688.ITEM_ID, "name": ItemDefinition_688.NAME, "atk": ItemDefinition_688.ATTACK_BONUS, "def": ItemDefinition_688.DEFENSE_BONUS}


class ItemDefinition_689:
    ITEM_ID = "item_689"
    NAME = "Hyperion Legendary Artifact #689"
    TYPE = "Weapon" if 689 % 2 == 0 else "Armor"
    RARITY = "Epic" if 689 % 5 == 0 else "Legendary"
    BASE_VALUE = 34450
    ATTACK_BONUS = 2067
    DEFENSE_BONUS = 1378
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 689."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_689.ITEM_ID, "name": ItemDefinition_689.NAME, "atk": ItemDefinition_689.ATTACK_BONUS, "def": ItemDefinition_689.DEFENSE_BONUS}


class ItemDefinition_690:
    ITEM_ID = "item_690"
    NAME = "Hyperion Legendary Artifact #690"
    TYPE = "Weapon" if 690 % 2 == 0 else "Armor"
    RARITY = "Epic" if 690 % 5 == 0 else "Legendary"
    BASE_VALUE = 34500
    ATTACK_BONUS = 2070
    DEFENSE_BONUS = 1380
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 690."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_690.ITEM_ID, "name": ItemDefinition_690.NAME, "atk": ItemDefinition_690.ATTACK_BONUS, "def": ItemDefinition_690.DEFENSE_BONUS}


class ItemDefinition_691:
    ITEM_ID = "item_691"
    NAME = "Hyperion Legendary Artifact #691"
    TYPE = "Weapon" if 691 % 2 == 0 else "Armor"
    RARITY = "Epic" if 691 % 5 == 0 else "Legendary"
    BASE_VALUE = 34550
    ATTACK_BONUS = 2073
    DEFENSE_BONUS = 1382
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 691."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_691.ITEM_ID, "name": ItemDefinition_691.NAME, "atk": ItemDefinition_691.ATTACK_BONUS, "def": ItemDefinition_691.DEFENSE_BONUS}


class ItemDefinition_692:
    ITEM_ID = "item_692"
    NAME = "Hyperion Legendary Artifact #692"
    TYPE = "Weapon" if 692 % 2 == 0 else "Armor"
    RARITY = "Epic" if 692 % 5 == 0 else "Legendary"
    BASE_VALUE = 34600
    ATTACK_BONUS = 2076
    DEFENSE_BONUS = 1384
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 692."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_692.ITEM_ID, "name": ItemDefinition_692.NAME, "atk": ItemDefinition_692.ATTACK_BONUS, "def": ItemDefinition_692.DEFENSE_BONUS}


class ItemDefinition_693:
    ITEM_ID = "item_693"
    NAME = "Hyperion Legendary Artifact #693"
    TYPE = "Weapon" if 693 % 2 == 0 else "Armor"
    RARITY = "Epic" if 693 % 5 == 0 else "Legendary"
    BASE_VALUE = 34650
    ATTACK_BONUS = 2079
    DEFENSE_BONUS = 1386
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 693."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_693.ITEM_ID, "name": ItemDefinition_693.NAME, "atk": ItemDefinition_693.ATTACK_BONUS, "def": ItemDefinition_693.DEFENSE_BONUS}


class ItemDefinition_694:
    ITEM_ID = "item_694"
    NAME = "Hyperion Legendary Artifact #694"
    TYPE = "Weapon" if 694 % 2 == 0 else "Armor"
    RARITY = "Epic" if 694 % 5 == 0 else "Legendary"
    BASE_VALUE = 34700
    ATTACK_BONUS = 2082
    DEFENSE_BONUS = 1388
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 694."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_694.ITEM_ID, "name": ItemDefinition_694.NAME, "atk": ItemDefinition_694.ATTACK_BONUS, "def": ItemDefinition_694.DEFENSE_BONUS}


class ItemDefinition_695:
    ITEM_ID = "item_695"
    NAME = "Hyperion Legendary Artifact #695"
    TYPE = "Weapon" if 695 % 2 == 0 else "Armor"
    RARITY = "Epic" if 695 % 5 == 0 else "Legendary"
    BASE_VALUE = 34750
    ATTACK_BONUS = 2085
    DEFENSE_BONUS = 1390
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 695."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_695.ITEM_ID, "name": ItemDefinition_695.NAME, "atk": ItemDefinition_695.ATTACK_BONUS, "def": ItemDefinition_695.DEFENSE_BONUS}


class ItemDefinition_696:
    ITEM_ID = "item_696"
    NAME = "Hyperion Legendary Artifact #696"
    TYPE = "Weapon" if 696 % 2 == 0 else "Armor"
    RARITY = "Epic" if 696 % 5 == 0 else "Legendary"
    BASE_VALUE = 34800
    ATTACK_BONUS = 2088
    DEFENSE_BONUS = 1392
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 696."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_696.ITEM_ID, "name": ItemDefinition_696.NAME, "atk": ItemDefinition_696.ATTACK_BONUS, "def": ItemDefinition_696.DEFENSE_BONUS}


class ItemDefinition_697:
    ITEM_ID = "item_697"
    NAME = "Hyperion Legendary Artifact #697"
    TYPE = "Weapon" if 697 % 2 == 0 else "Armor"
    RARITY = "Epic" if 697 % 5 == 0 else "Legendary"
    BASE_VALUE = 34850
    ATTACK_BONUS = 2091
    DEFENSE_BONUS = 1394
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 697."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_697.ITEM_ID, "name": ItemDefinition_697.NAME, "atk": ItemDefinition_697.ATTACK_BONUS, "def": ItemDefinition_697.DEFENSE_BONUS}


class ItemDefinition_698:
    ITEM_ID = "item_698"
    NAME = "Hyperion Legendary Artifact #698"
    TYPE = "Weapon" if 698 % 2 == 0 else "Armor"
    RARITY = "Epic" if 698 % 5 == 0 else "Legendary"
    BASE_VALUE = 34900
    ATTACK_BONUS = 2094
    DEFENSE_BONUS = 1396
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 698."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_698.ITEM_ID, "name": ItemDefinition_698.NAME, "atk": ItemDefinition_698.ATTACK_BONUS, "def": ItemDefinition_698.DEFENSE_BONUS}


class ItemDefinition_699:
    ITEM_ID = "item_699"
    NAME = "Hyperion Legendary Artifact #699"
    TYPE = "Weapon" if 699 % 2 == 0 else "Armor"
    RARITY = "Epic" if 699 % 5 == 0 else "Legendary"
    BASE_VALUE = 34950
    ATTACK_BONUS = 2097
    DEFENSE_BONUS = 1398
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 699."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_699.ITEM_ID, "name": ItemDefinition_699.NAME, "atk": ItemDefinition_699.ATTACK_BONUS, "def": ItemDefinition_699.DEFENSE_BONUS}


class ItemDefinition_700:
    ITEM_ID = "item_700"
    NAME = "Hyperion Legendary Artifact #700"
    TYPE = "Weapon" if 700 % 2 == 0 else "Armor"
    RARITY = "Epic" if 700 % 5 == 0 else "Legendary"
    BASE_VALUE = 35000
    ATTACK_BONUS = 2100
    DEFENSE_BONUS = 1400
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 700."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_700.ITEM_ID, "name": ItemDefinition_700.NAME, "atk": ItemDefinition_700.ATTACK_BONUS, "def": ItemDefinition_700.DEFENSE_BONUS}


class ItemDefinition_701:
    ITEM_ID = "item_701"
    NAME = "Hyperion Legendary Artifact #701"
    TYPE = "Weapon" if 701 % 2 == 0 else "Armor"
    RARITY = "Epic" if 701 % 5 == 0 else "Legendary"
    BASE_VALUE = 35050
    ATTACK_BONUS = 2103
    DEFENSE_BONUS = 1402
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 701."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_701.ITEM_ID, "name": ItemDefinition_701.NAME, "atk": ItemDefinition_701.ATTACK_BONUS, "def": ItemDefinition_701.DEFENSE_BONUS}


class ItemDefinition_702:
    ITEM_ID = "item_702"
    NAME = "Hyperion Legendary Artifact #702"
    TYPE = "Weapon" if 702 % 2 == 0 else "Armor"
    RARITY = "Epic" if 702 % 5 == 0 else "Legendary"
    BASE_VALUE = 35100
    ATTACK_BONUS = 2106
    DEFENSE_BONUS = 1404
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 702."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_702.ITEM_ID, "name": ItemDefinition_702.NAME, "atk": ItemDefinition_702.ATTACK_BONUS, "def": ItemDefinition_702.DEFENSE_BONUS}


class ItemDefinition_703:
    ITEM_ID = "item_703"
    NAME = "Hyperion Legendary Artifact #703"
    TYPE = "Weapon" if 703 % 2 == 0 else "Armor"
    RARITY = "Epic" if 703 % 5 == 0 else "Legendary"
    BASE_VALUE = 35150
    ATTACK_BONUS = 2109
    DEFENSE_BONUS = 1406
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 703."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_703.ITEM_ID, "name": ItemDefinition_703.NAME, "atk": ItemDefinition_703.ATTACK_BONUS, "def": ItemDefinition_703.DEFENSE_BONUS}


class ItemDefinition_704:
    ITEM_ID = "item_704"
    NAME = "Hyperion Legendary Artifact #704"
    TYPE = "Weapon" if 704 % 2 == 0 else "Armor"
    RARITY = "Epic" if 704 % 5 == 0 else "Legendary"
    BASE_VALUE = 35200
    ATTACK_BONUS = 2112
    DEFENSE_BONUS = 1408
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 704."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_704.ITEM_ID, "name": ItemDefinition_704.NAME, "atk": ItemDefinition_704.ATTACK_BONUS, "def": ItemDefinition_704.DEFENSE_BONUS}


class ItemDefinition_705:
    ITEM_ID = "item_705"
    NAME = "Hyperion Legendary Artifact #705"
    TYPE = "Weapon" if 705 % 2 == 0 else "Armor"
    RARITY = "Epic" if 705 % 5 == 0 else "Legendary"
    BASE_VALUE = 35250
    ATTACK_BONUS = 2115
    DEFENSE_BONUS = 1410
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 705."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_705.ITEM_ID, "name": ItemDefinition_705.NAME, "atk": ItemDefinition_705.ATTACK_BONUS, "def": ItemDefinition_705.DEFENSE_BONUS}


class ItemDefinition_706:
    ITEM_ID = "item_706"
    NAME = "Hyperion Legendary Artifact #706"
    TYPE = "Weapon" if 706 % 2 == 0 else "Armor"
    RARITY = "Epic" if 706 % 5 == 0 else "Legendary"
    BASE_VALUE = 35300
    ATTACK_BONUS = 2118
    DEFENSE_BONUS = 1412
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 706."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_706.ITEM_ID, "name": ItemDefinition_706.NAME, "atk": ItemDefinition_706.ATTACK_BONUS, "def": ItemDefinition_706.DEFENSE_BONUS}


class ItemDefinition_707:
    ITEM_ID = "item_707"
    NAME = "Hyperion Legendary Artifact #707"
    TYPE = "Weapon" if 707 % 2 == 0 else "Armor"
    RARITY = "Epic" if 707 % 5 == 0 else "Legendary"
    BASE_VALUE = 35350
    ATTACK_BONUS = 2121
    DEFENSE_BONUS = 1414
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 707."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_707.ITEM_ID, "name": ItemDefinition_707.NAME, "atk": ItemDefinition_707.ATTACK_BONUS, "def": ItemDefinition_707.DEFENSE_BONUS}


class ItemDefinition_708:
    ITEM_ID = "item_708"
    NAME = "Hyperion Legendary Artifact #708"
    TYPE = "Weapon" if 708 % 2 == 0 else "Armor"
    RARITY = "Epic" if 708 % 5 == 0 else "Legendary"
    BASE_VALUE = 35400
    ATTACK_BONUS = 2124
    DEFENSE_BONUS = 1416
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 708."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_708.ITEM_ID, "name": ItemDefinition_708.NAME, "atk": ItemDefinition_708.ATTACK_BONUS, "def": ItemDefinition_708.DEFENSE_BONUS}


class ItemDefinition_709:
    ITEM_ID = "item_709"
    NAME = "Hyperion Legendary Artifact #709"
    TYPE = "Weapon" if 709 % 2 == 0 else "Armor"
    RARITY = "Epic" if 709 % 5 == 0 else "Legendary"
    BASE_VALUE = 35450
    ATTACK_BONUS = 2127
    DEFENSE_BONUS = 1418
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 709."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_709.ITEM_ID, "name": ItemDefinition_709.NAME, "atk": ItemDefinition_709.ATTACK_BONUS, "def": ItemDefinition_709.DEFENSE_BONUS}


class ItemDefinition_710:
    ITEM_ID = "item_710"
    NAME = "Hyperion Legendary Artifact #710"
    TYPE = "Weapon" if 710 % 2 == 0 else "Armor"
    RARITY = "Epic" if 710 % 5 == 0 else "Legendary"
    BASE_VALUE = 35500
    ATTACK_BONUS = 2130
    DEFENSE_BONUS = 1420
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 710."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_710.ITEM_ID, "name": ItemDefinition_710.NAME, "atk": ItemDefinition_710.ATTACK_BONUS, "def": ItemDefinition_710.DEFENSE_BONUS}


class ItemDefinition_711:
    ITEM_ID = "item_711"
    NAME = "Hyperion Legendary Artifact #711"
    TYPE = "Weapon" if 711 % 2 == 0 else "Armor"
    RARITY = "Epic" if 711 % 5 == 0 else "Legendary"
    BASE_VALUE = 35550
    ATTACK_BONUS = 2133
    DEFENSE_BONUS = 1422
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 711."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_711.ITEM_ID, "name": ItemDefinition_711.NAME, "atk": ItemDefinition_711.ATTACK_BONUS, "def": ItemDefinition_711.DEFENSE_BONUS}


class ItemDefinition_712:
    ITEM_ID = "item_712"
    NAME = "Hyperion Legendary Artifact #712"
    TYPE = "Weapon" if 712 % 2 == 0 else "Armor"
    RARITY = "Epic" if 712 % 5 == 0 else "Legendary"
    BASE_VALUE = 35600
    ATTACK_BONUS = 2136
    DEFENSE_BONUS = 1424
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 712."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_712.ITEM_ID, "name": ItemDefinition_712.NAME, "atk": ItemDefinition_712.ATTACK_BONUS, "def": ItemDefinition_712.DEFENSE_BONUS}


class ItemDefinition_713:
    ITEM_ID = "item_713"
    NAME = "Hyperion Legendary Artifact #713"
    TYPE = "Weapon" if 713 % 2 == 0 else "Armor"
    RARITY = "Epic" if 713 % 5 == 0 else "Legendary"
    BASE_VALUE = 35650
    ATTACK_BONUS = 2139
    DEFENSE_BONUS = 1426
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 713."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_713.ITEM_ID, "name": ItemDefinition_713.NAME, "atk": ItemDefinition_713.ATTACK_BONUS, "def": ItemDefinition_713.DEFENSE_BONUS}


class ItemDefinition_714:
    ITEM_ID = "item_714"
    NAME = "Hyperion Legendary Artifact #714"
    TYPE = "Weapon" if 714 % 2 == 0 else "Armor"
    RARITY = "Epic" if 714 % 5 == 0 else "Legendary"
    BASE_VALUE = 35700
    ATTACK_BONUS = 2142
    DEFENSE_BONUS = 1428
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 714."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_714.ITEM_ID, "name": ItemDefinition_714.NAME, "atk": ItemDefinition_714.ATTACK_BONUS, "def": ItemDefinition_714.DEFENSE_BONUS}


class ItemDefinition_715:
    ITEM_ID = "item_715"
    NAME = "Hyperion Legendary Artifact #715"
    TYPE = "Weapon" if 715 % 2 == 0 else "Armor"
    RARITY = "Epic" if 715 % 5 == 0 else "Legendary"
    BASE_VALUE = 35750
    ATTACK_BONUS = 2145
    DEFENSE_BONUS = 1430
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 715."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_715.ITEM_ID, "name": ItemDefinition_715.NAME, "atk": ItemDefinition_715.ATTACK_BONUS, "def": ItemDefinition_715.DEFENSE_BONUS}


class ItemDefinition_716:
    ITEM_ID = "item_716"
    NAME = "Hyperion Legendary Artifact #716"
    TYPE = "Weapon" if 716 % 2 == 0 else "Armor"
    RARITY = "Epic" if 716 % 5 == 0 else "Legendary"
    BASE_VALUE = 35800
    ATTACK_BONUS = 2148
    DEFENSE_BONUS = 1432
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 716."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_716.ITEM_ID, "name": ItemDefinition_716.NAME, "atk": ItemDefinition_716.ATTACK_BONUS, "def": ItemDefinition_716.DEFENSE_BONUS}


class ItemDefinition_717:
    ITEM_ID = "item_717"
    NAME = "Hyperion Legendary Artifact #717"
    TYPE = "Weapon" if 717 % 2 == 0 else "Armor"
    RARITY = "Epic" if 717 % 5 == 0 else "Legendary"
    BASE_VALUE = 35850
    ATTACK_BONUS = 2151
    DEFENSE_BONUS = 1434
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 717."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_717.ITEM_ID, "name": ItemDefinition_717.NAME, "atk": ItemDefinition_717.ATTACK_BONUS, "def": ItemDefinition_717.DEFENSE_BONUS}


class ItemDefinition_718:
    ITEM_ID = "item_718"
    NAME = "Hyperion Legendary Artifact #718"
    TYPE = "Weapon" if 718 % 2 == 0 else "Armor"
    RARITY = "Epic" if 718 % 5 == 0 else "Legendary"
    BASE_VALUE = 35900
    ATTACK_BONUS = 2154
    DEFENSE_BONUS = 1436
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 718."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_718.ITEM_ID, "name": ItemDefinition_718.NAME, "atk": ItemDefinition_718.ATTACK_BONUS, "def": ItemDefinition_718.DEFENSE_BONUS}


class ItemDefinition_719:
    ITEM_ID = "item_719"
    NAME = "Hyperion Legendary Artifact #719"
    TYPE = "Weapon" if 719 % 2 == 0 else "Armor"
    RARITY = "Epic" if 719 % 5 == 0 else "Legendary"
    BASE_VALUE = 35950
    ATTACK_BONUS = 2157
    DEFENSE_BONUS = 1438
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 719."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_719.ITEM_ID, "name": ItemDefinition_719.NAME, "atk": ItemDefinition_719.ATTACK_BONUS, "def": ItemDefinition_719.DEFENSE_BONUS}


class ItemDefinition_720:
    ITEM_ID = "item_720"
    NAME = "Hyperion Legendary Artifact #720"
    TYPE = "Weapon" if 720 % 2 == 0 else "Armor"
    RARITY = "Epic" if 720 % 5 == 0 else "Legendary"
    BASE_VALUE = 36000
    ATTACK_BONUS = 2160
    DEFENSE_BONUS = 1440
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 720."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_720.ITEM_ID, "name": ItemDefinition_720.NAME, "atk": ItemDefinition_720.ATTACK_BONUS, "def": ItemDefinition_720.DEFENSE_BONUS}


class ItemDefinition_721:
    ITEM_ID = "item_721"
    NAME = "Hyperion Legendary Artifact #721"
    TYPE = "Weapon" if 721 % 2 == 0 else "Armor"
    RARITY = "Epic" if 721 % 5 == 0 else "Legendary"
    BASE_VALUE = 36050
    ATTACK_BONUS = 2163
    DEFENSE_BONUS = 1442
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 721."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_721.ITEM_ID, "name": ItemDefinition_721.NAME, "atk": ItemDefinition_721.ATTACK_BONUS, "def": ItemDefinition_721.DEFENSE_BONUS}


class ItemDefinition_722:
    ITEM_ID = "item_722"
    NAME = "Hyperion Legendary Artifact #722"
    TYPE = "Weapon" if 722 % 2 == 0 else "Armor"
    RARITY = "Epic" if 722 % 5 == 0 else "Legendary"
    BASE_VALUE = 36100
    ATTACK_BONUS = 2166
    DEFENSE_BONUS = 1444
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 722."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_722.ITEM_ID, "name": ItemDefinition_722.NAME, "atk": ItemDefinition_722.ATTACK_BONUS, "def": ItemDefinition_722.DEFENSE_BONUS}


class ItemDefinition_723:
    ITEM_ID = "item_723"
    NAME = "Hyperion Legendary Artifact #723"
    TYPE = "Weapon" if 723 % 2 == 0 else "Armor"
    RARITY = "Epic" if 723 % 5 == 0 else "Legendary"
    BASE_VALUE = 36150
    ATTACK_BONUS = 2169
    DEFENSE_BONUS = 1446
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 723."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_723.ITEM_ID, "name": ItemDefinition_723.NAME, "atk": ItemDefinition_723.ATTACK_BONUS, "def": ItemDefinition_723.DEFENSE_BONUS}


class ItemDefinition_724:
    ITEM_ID = "item_724"
    NAME = "Hyperion Legendary Artifact #724"
    TYPE = "Weapon" if 724 % 2 == 0 else "Armor"
    RARITY = "Epic" if 724 % 5 == 0 else "Legendary"
    BASE_VALUE = 36200
    ATTACK_BONUS = 2172
    DEFENSE_BONUS = 1448
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 724."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_724.ITEM_ID, "name": ItemDefinition_724.NAME, "atk": ItemDefinition_724.ATTACK_BONUS, "def": ItemDefinition_724.DEFENSE_BONUS}


class ItemDefinition_725:
    ITEM_ID = "item_725"
    NAME = "Hyperion Legendary Artifact #725"
    TYPE = "Weapon" if 725 % 2 == 0 else "Armor"
    RARITY = "Epic" if 725 % 5 == 0 else "Legendary"
    BASE_VALUE = 36250
    ATTACK_BONUS = 2175
    DEFENSE_BONUS = 1450
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 725."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_725.ITEM_ID, "name": ItemDefinition_725.NAME, "atk": ItemDefinition_725.ATTACK_BONUS, "def": ItemDefinition_725.DEFENSE_BONUS}


class ItemDefinition_726:
    ITEM_ID = "item_726"
    NAME = "Hyperion Legendary Artifact #726"
    TYPE = "Weapon" if 726 % 2 == 0 else "Armor"
    RARITY = "Epic" if 726 % 5 == 0 else "Legendary"
    BASE_VALUE = 36300
    ATTACK_BONUS = 2178
    DEFENSE_BONUS = 1452
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 726."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_726.ITEM_ID, "name": ItemDefinition_726.NAME, "atk": ItemDefinition_726.ATTACK_BONUS, "def": ItemDefinition_726.DEFENSE_BONUS}


class ItemDefinition_727:
    ITEM_ID = "item_727"
    NAME = "Hyperion Legendary Artifact #727"
    TYPE = "Weapon" if 727 % 2 == 0 else "Armor"
    RARITY = "Epic" if 727 % 5 == 0 else "Legendary"
    BASE_VALUE = 36350
    ATTACK_BONUS = 2181
    DEFENSE_BONUS = 1454
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 727."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_727.ITEM_ID, "name": ItemDefinition_727.NAME, "atk": ItemDefinition_727.ATTACK_BONUS, "def": ItemDefinition_727.DEFENSE_BONUS}


class ItemDefinition_728:
    ITEM_ID = "item_728"
    NAME = "Hyperion Legendary Artifact #728"
    TYPE = "Weapon" if 728 % 2 == 0 else "Armor"
    RARITY = "Epic" if 728 % 5 == 0 else "Legendary"
    BASE_VALUE = 36400
    ATTACK_BONUS = 2184
    DEFENSE_BONUS = 1456
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 728."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_728.ITEM_ID, "name": ItemDefinition_728.NAME, "atk": ItemDefinition_728.ATTACK_BONUS, "def": ItemDefinition_728.DEFENSE_BONUS}


class ItemDefinition_729:
    ITEM_ID = "item_729"
    NAME = "Hyperion Legendary Artifact #729"
    TYPE = "Weapon" if 729 % 2 == 0 else "Armor"
    RARITY = "Epic" if 729 % 5 == 0 else "Legendary"
    BASE_VALUE = 36450
    ATTACK_BONUS = 2187
    DEFENSE_BONUS = 1458
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 729."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_729.ITEM_ID, "name": ItemDefinition_729.NAME, "atk": ItemDefinition_729.ATTACK_BONUS, "def": ItemDefinition_729.DEFENSE_BONUS}


class ItemDefinition_730:
    ITEM_ID = "item_730"
    NAME = "Hyperion Legendary Artifact #730"
    TYPE = "Weapon" if 730 % 2 == 0 else "Armor"
    RARITY = "Epic" if 730 % 5 == 0 else "Legendary"
    BASE_VALUE = 36500
    ATTACK_BONUS = 2190
    DEFENSE_BONUS = 1460
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 730."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_730.ITEM_ID, "name": ItemDefinition_730.NAME, "atk": ItemDefinition_730.ATTACK_BONUS, "def": ItemDefinition_730.DEFENSE_BONUS}


class ItemDefinition_731:
    ITEM_ID = "item_731"
    NAME = "Hyperion Legendary Artifact #731"
    TYPE = "Weapon" if 731 % 2 == 0 else "Armor"
    RARITY = "Epic" if 731 % 5 == 0 else "Legendary"
    BASE_VALUE = 36550
    ATTACK_BONUS = 2193
    DEFENSE_BONUS = 1462
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 731."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_731.ITEM_ID, "name": ItemDefinition_731.NAME, "atk": ItemDefinition_731.ATTACK_BONUS, "def": ItemDefinition_731.DEFENSE_BONUS}


class ItemDefinition_732:
    ITEM_ID = "item_732"
    NAME = "Hyperion Legendary Artifact #732"
    TYPE = "Weapon" if 732 % 2 == 0 else "Armor"
    RARITY = "Epic" if 732 % 5 == 0 else "Legendary"
    BASE_VALUE = 36600
    ATTACK_BONUS = 2196
    DEFENSE_BONUS = 1464
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 732."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_732.ITEM_ID, "name": ItemDefinition_732.NAME, "atk": ItemDefinition_732.ATTACK_BONUS, "def": ItemDefinition_732.DEFENSE_BONUS}


class ItemDefinition_733:
    ITEM_ID = "item_733"
    NAME = "Hyperion Legendary Artifact #733"
    TYPE = "Weapon" if 733 % 2 == 0 else "Armor"
    RARITY = "Epic" if 733 % 5 == 0 else "Legendary"
    BASE_VALUE = 36650
    ATTACK_BONUS = 2199
    DEFENSE_BONUS = 1466
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 733."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_733.ITEM_ID, "name": ItemDefinition_733.NAME, "atk": ItemDefinition_733.ATTACK_BONUS, "def": ItemDefinition_733.DEFENSE_BONUS}


class ItemDefinition_734:
    ITEM_ID = "item_734"
    NAME = "Hyperion Legendary Artifact #734"
    TYPE = "Weapon" if 734 % 2 == 0 else "Armor"
    RARITY = "Epic" if 734 % 5 == 0 else "Legendary"
    BASE_VALUE = 36700
    ATTACK_BONUS = 2202
    DEFENSE_BONUS = 1468
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 734."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_734.ITEM_ID, "name": ItemDefinition_734.NAME, "atk": ItemDefinition_734.ATTACK_BONUS, "def": ItemDefinition_734.DEFENSE_BONUS}


class ItemDefinition_735:
    ITEM_ID = "item_735"
    NAME = "Hyperion Legendary Artifact #735"
    TYPE = "Weapon" if 735 % 2 == 0 else "Armor"
    RARITY = "Epic" if 735 % 5 == 0 else "Legendary"
    BASE_VALUE = 36750
    ATTACK_BONUS = 2205
    DEFENSE_BONUS = 1470
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 735."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_735.ITEM_ID, "name": ItemDefinition_735.NAME, "atk": ItemDefinition_735.ATTACK_BONUS, "def": ItemDefinition_735.DEFENSE_BONUS}


class ItemDefinition_736:
    ITEM_ID = "item_736"
    NAME = "Hyperion Legendary Artifact #736"
    TYPE = "Weapon" if 736 % 2 == 0 else "Armor"
    RARITY = "Epic" if 736 % 5 == 0 else "Legendary"
    BASE_VALUE = 36800
    ATTACK_BONUS = 2208
    DEFENSE_BONUS = 1472
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 736."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_736.ITEM_ID, "name": ItemDefinition_736.NAME, "atk": ItemDefinition_736.ATTACK_BONUS, "def": ItemDefinition_736.DEFENSE_BONUS}


class ItemDefinition_737:
    ITEM_ID = "item_737"
    NAME = "Hyperion Legendary Artifact #737"
    TYPE = "Weapon" if 737 % 2 == 0 else "Armor"
    RARITY = "Epic" if 737 % 5 == 0 else "Legendary"
    BASE_VALUE = 36850
    ATTACK_BONUS = 2211
    DEFENSE_BONUS = 1474
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 737."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_737.ITEM_ID, "name": ItemDefinition_737.NAME, "atk": ItemDefinition_737.ATTACK_BONUS, "def": ItemDefinition_737.DEFENSE_BONUS}


class ItemDefinition_738:
    ITEM_ID = "item_738"
    NAME = "Hyperion Legendary Artifact #738"
    TYPE = "Weapon" if 738 % 2 == 0 else "Armor"
    RARITY = "Epic" if 738 % 5 == 0 else "Legendary"
    BASE_VALUE = 36900
    ATTACK_BONUS = 2214
    DEFENSE_BONUS = 1476
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 738."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_738.ITEM_ID, "name": ItemDefinition_738.NAME, "atk": ItemDefinition_738.ATTACK_BONUS, "def": ItemDefinition_738.DEFENSE_BONUS}


class ItemDefinition_739:
    ITEM_ID = "item_739"
    NAME = "Hyperion Legendary Artifact #739"
    TYPE = "Weapon" if 739 % 2 == 0 else "Armor"
    RARITY = "Epic" if 739 % 5 == 0 else "Legendary"
    BASE_VALUE = 36950
    ATTACK_BONUS = 2217
    DEFENSE_BONUS = 1478
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 739."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_739.ITEM_ID, "name": ItemDefinition_739.NAME, "atk": ItemDefinition_739.ATTACK_BONUS, "def": ItemDefinition_739.DEFENSE_BONUS}


class ItemDefinition_740:
    ITEM_ID = "item_740"
    NAME = "Hyperion Legendary Artifact #740"
    TYPE = "Weapon" if 740 % 2 == 0 else "Armor"
    RARITY = "Epic" if 740 % 5 == 0 else "Legendary"
    BASE_VALUE = 37000
    ATTACK_BONUS = 2220
    DEFENSE_BONUS = 1480
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 740."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_740.ITEM_ID, "name": ItemDefinition_740.NAME, "atk": ItemDefinition_740.ATTACK_BONUS, "def": ItemDefinition_740.DEFENSE_BONUS}


class ItemDefinition_741:
    ITEM_ID = "item_741"
    NAME = "Hyperion Legendary Artifact #741"
    TYPE = "Weapon" if 741 % 2 == 0 else "Armor"
    RARITY = "Epic" if 741 % 5 == 0 else "Legendary"
    BASE_VALUE = 37050
    ATTACK_BONUS = 2223
    DEFENSE_BONUS = 1482
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 741."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_741.ITEM_ID, "name": ItemDefinition_741.NAME, "atk": ItemDefinition_741.ATTACK_BONUS, "def": ItemDefinition_741.DEFENSE_BONUS}


class ItemDefinition_742:
    ITEM_ID = "item_742"
    NAME = "Hyperion Legendary Artifact #742"
    TYPE = "Weapon" if 742 % 2 == 0 else "Armor"
    RARITY = "Epic" if 742 % 5 == 0 else "Legendary"
    BASE_VALUE = 37100
    ATTACK_BONUS = 2226
    DEFENSE_BONUS = 1484
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 742."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_742.ITEM_ID, "name": ItemDefinition_742.NAME, "atk": ItemDefinition_742.ATTACK_BONUS, "def": ItemDefinition_742.DEFENSE_BONUS}


class ItemDefinition_743:
    ITEM_ID = "item_743"
    NAME = "Hyperion Legendary Artifact #743"
    TYPE = "Weapon" if 743 % 2 == 0 else "Armor"
    RARITY = "Epic" if 743 % 5 == 0 else "Legendary"
    BASE_VALUE = 37150
    ATTACK_BONUS = 2229
    DEFENSE_BONUS = 1486
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 743."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_743.ITEM_ID, "name": ItemDefinition_743.NAME, "atk": ItemDefinition_743.ATTACK_BONUS, "def": ItemDefinition_743.DEFENSE_BONUS}


class ItemDefinition_744:
    ITEM_ID = "item_744"
    NAME = "Hyperion Legendary Artifact #744"
    TYPE = "Weapon" if 744 % 2 == 0 else "Armor"
    RARITY = "Epic" if 744 % 5 == 0 else "Legendary"
    BASE_VALUE = 37200
    ATTACK_BONUS = 2232
    DEFENSE_BONUS = 1488
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 744."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_744.ITEM_ID, "name": ItemDefinition_744.NAME, "atk": ItemDefinition_744.ATTACK_BONUS, "def": ItemDefinition_744.DEFENSE_BONUS}


class ItemDefinition_745:
    ITEM_ID = "item_745"
    NAME = "Hyperion Legendary Artifact #745"
    TYPE = "Weapon" if 745 % 2 == 0 else "Armor"
    RARITY = "Epic" if 745 % 5 == 0 else "Legendary"
    BASE_VALUE = 37250
    ATTACK_BONUS = 2235
    DEFENSE_BONUS = 1490
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 745."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_745.ITEM_ID, "name": ItemDefinition_745.NAME, "atk": ItemDefinition_745.ATTACK_BONUS, "def": ItemDefinition_745.DEFENSE_BONUS}


class ItemDefinition_746:
    ITEM_ID = "item_746"
    NAME = "Hyperion Legendary Artifact #746"
    TYPE = "Weapon" if 746 % 2 == 0 else "Armor"
    RARITY = "Epic" if 746 % 5 == 0 else "Legendary"
    BASE_VALUE = 37300
    ATTACK_BONUS = 2238
    DEFENSE_BONUS = 1492
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 746."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_746.ITEM_ID, "name": ItemDefinition_746.NAME, "atk": ItemDefinition_746.ATTACK_BONUS, "def": ItemDefinition_746.DEFENSE_BONUS}


class ItemDefinition_747:
    ITEM_ID = "item_747"
    NAME = "Hyperion Legendary Artifact #747"
    TYPE = "Weapon" if 747 % 2 == 0 else "Armor"
    RARITY = "Epic" if 747 % 5 == 0 else "Legendary"
    BASE_VALUE = 37350
    ATTACK_BONUS = 2241
    DEFENSE_BONUS = 1494
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 747."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_747.ITEM_ID, "name": ItemDefinition_747.NAME, "atk": ItemDefinition_747.ATTACK_BONUS, "def": ItemDefinition_747.DEFENSE_BONUS}


class ItemDefinition_748:
    ITEM_ID = "item_748"
    NAME = "Hyperion Legendary Artifact #748"
    TYPE = "Weapon" if 748 % 2 == 0 else "Armor"
    RARITY = "Epic" if 748 % 5 == 0 else "Legendary"
    BASE_VALUE = 37400
    ATTACK_BONUS = 2244
    DEFENSE_BONUS = 1496
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 748."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_748.ITEM_ID, "name": ItemDefinition_748.NAME, "atk": ItemDefinition_748.ATTACK_BONUS, "def": ItemDefinition_748.DEFENSE_BONUS}


class ItemDefinition_749:
    ITEM_ID = "item_749"
    NAME = "Hyperion Legendary Artifact #749"
    TYPE = "Weapon" if 749 % 2 == 0 else "Armor"
    RARITY = "Epic" if 749 % 5 == 0 else "Legendary"
    BASE_VALUE = 37450
    ATTACK_BONUS = 2247
    DEFENSE_BONUS = 1498
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 749."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_749.ITEM_ID, "name": ItemDefinition_749.NAME, "atk": ItemDefinition_749.ATTACK_BONUS, "def": ItemDefinition_749.DEFENSE_BONUS}


class ItemDefinition_750:
    ITEM_ID = "item_750"
    NAME = "Hyperion Legendary Artifact #750"
    TYPE = "Weapon" if 750 % 2 == 0 else "Armor"
    RARITY = "Epic" if 750 % 5 == 0 else "Legendary"
    BASE_VALUE = 37500
    ATTACK_BONUS = 2250
    DEFENSE_BONUS = 1500
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 750."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_750.ITEM_ID, "name": ItemDefinition_750.NAME, "atk": ItemDefinition_750.ATTACK_BONUS, "def": ItemDefinition_750.DEFENSE_BONUS}


class ItemDefinition_751:
    ITEM_ID = "item_751"
    NAME = "Hyperion Legendary Artifact #751"
    TYPE = "Weapon" if 751 % 2 == 0 else "Armor"
    RARITY = "Epic" if 751 % 5 == 0 else "Legendary"
    BASE_VALUE = 37550
    ATTACK_BONUS = 2253
    DEFENSE_BONUS = 1502
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 751."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_751.ITEM_ID, "name": ItemDefinition_751.NAME, "atk": ItemDefinition_751.ATTACK_BONUS, "def": ItemDefinition_751.DEFENSE_BONUS}


class ItemDefinition_752:
    ITEM_ID = "item_752"
    NAME = "Hyperion Legendary Artifact #752"
    TYPE = "Weapon" if 752 % 2 == 0 else "Armor"
    RARITY = "Epic" if 752 % 5 == 0 else "Legendary"
    BASE_VALUE = 37600
    ATTACK_BONUS = 2256
    DEFENSE_BONUS = 1504
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 752."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_752.ITEM_ID, "name": ItemDefinition_752.NAME, "atk": ItemDefinition_752.ATTACK_BONUS, "def": ItemDefinition_752.DEFENSE_BONUS}


class ItemDefinition_753:
    ITEM_ID = "item_753"
    NAME = "Hyperion Legendary Artifact #753"
    TYPE = "Weapon" if 753 % 2 == 0 else "Armor"
    RARITY = "Epic" if 753 % 5 == 0 else "Legendary"
    BASE_VALUE = 37650
    ATTACK_BONUS = 2259
    DEFENSE_BONUS = 1506
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 753."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_753.ITEM_ID, "name": ItemDefinition_753.NAME, "atk": ItemDefinition_753.ATTACK_BONUS, "def": ItemDefinition_753.DEFENSE_BONUS}


class ItemDefinition_754:
    ITEM_ID = "item_754"
    NAME = "Hyperion Legendary Artifact #754"
    TYPE = "Weapon" if 754 % 2 == 0 else "Armor"
    RARITY = "Epic" if 754 % 5 == 0 else "Legendary"
    BASE_VALUE = 37700
    ATTACK_BONUS = 2262
    DEFENSE_BONUS = 1508
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 754."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_754.ITEM_ID, "name": ItemDefinition_754.NAME, "atk": ItemDefinition_754.ATTACK_BONUS, "def": ItemDefinition_754.DEFENSE_BONUS}


class ItemDefinition_755:
    ITEM_ID = "item_755"
    NAME = "Hyperion Legendary Artifact #755"
    TYPE = "Weapon" if 755 % 2 == 0 else "Armor"
    RARITY = "Epic" if 755 % 5 == 0 else "Legendary"
    BASE_VALUE = 37750
    ATTACK_BONUS = 2265
    DEFENSE_BONUS = 1510
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 755."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_755.ITEM_ID, "name": ItemDefinition_755.NAME, "atk": ItemDefinition_755.ATTACK_BONUS, "def": ItemDefinition_755.DEFENSE_BONUS}


class ItemDefinition_756:
    ITEM_ID = "item_756"
    NAME = "Hyperion Legendary Artifact #756"
    TYPE = "Weapon" if 756 % 2 == 0 else "Armor"
    RARITY = "Epic" if 756 % 5 == 0 else "Legendary"
    BASE_VALUE = 37800
    ATTACK_BONUS = 2268
    DEFENSE_BONUS = 1512
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 756."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_756.ITEM_ID, "name": ItemDefinition_756.NAME, "atk": ItemDefinition_756.ATTACK_BONUS, "def": ItemDefinition_756.DEFENSE_BONUS}


class ItemDefinition_757:
    ITEM_ID = "item_757"
    NAME = "Hyperion Legendary Artifact #757"
    TYPE = "Weapon" if 757 % 2 == 0 else "Armor"
    RARITY = "Epic" if 757 % 5 == 0 else "Legendary"
    BASE_VALUE = 37850
    ATTACK_BONUS = 2271
    DEFENSE_BONUS = 1514
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 757."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_757.ITEM_ID, "name": ItemDefinition_757.NAME, "atk": ItemDefinition_757.ATTACK_BONUS, "def": ItemDefinition_757.DEFENSE_BONUS}


class ItemDefinition_758:
    ITEM_ID = "item_758"
    NAME = "Hyperion Legendary Artifact #758"
    TYPE = "Weapon" if 758 % 2 == 0 else "Armor"
    RARITY = "Epic" if 758 % 5 == 0 else "Legendary"
    BASE_VALUE = 37900
    ATTACK_BONUS = 2274
    DEFENSE_BONUS = 1516
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 758."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_758.ITEM_ID, "name": ItemDefinition_758.NAME, "atk": ItemDefinition_758.ATTACK_BONUS, "def": ItemDefinition_758.DEFENSE_BONUS}


class ItemDefinition_759:
    ITEM_ID = "item_759"
    NAME = "Hyperion Legendary Artifact #759"
    TYPE = "Weapon" if 759 % 2 == 0 else "Armor"
    RARITY = "Epic" if 759 % 5 == 0 else "Legendary"
    BASE_VALUE = 37950
    ATTACK_BONUS = 2277
    DEFENSE_BONUS = 1518
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 759."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_759.ITEM_ID, "name": ItemDefinition_759.NAME, "atk": ItemDefinition_759.ATTACK_BONUS, "def": ItemDefinition_759.DEFENSE_BONUS}


class ItemDefinition_760:
    ITEM_ID = "item_760"
    NAME = "Hyperion Legendary Artifact #760"
    TYPE = "Weapon" if 760 % 2 == 0 else "Armor"
    RARITY = "Epic" if 760 % 5 == 0 else "Legendary"
    BASE_VALUE = 38000
    ATTACK_BONUS = 2280
    DEFENSE_BONUS = 1520
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 760."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_760.ITEM_ID, "name": ItemDefinition_760.NAME, "atk": ItemDefinition_760.ATTACK_BONUS, "def": ItemDefinition_760.DEFENSE_BONUS}


class ItemDefinition_761:
    ITEM_ID = "item_761"
    NAME = "Hyperion Legendary Artifact #761"
    TYPE = "Weapon" if 761 % 2 == 0 else "Armor"
    RARITY = "Epic" if 761 % 5 == 0 else "Legendary"
    BASE_VALUE = 38050
    ATTACK_BONUS = 2283
    DEFENSE_BONUS = 1522
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 761."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_761.ITEM_ID, "name": ItemDefinition_761.NAME, "atk": ItemDefinition_761.ATTACK_BONUS, "def": ItemDefinition_761.DEFENSE_BONUS}


class ItemDefinition_762:
    ITEM_ID = "item_762"
    NAME = "Hyperion Legendary Artifact #762"
    TYPE = "Weapon" if 762 % 2 == 0 else "Armor"
    RARITY = "Epic" if 762 % 5 == 0 else "Legendary"
    BASE_VALUE = 38100
    ATTACK_BONUS = 2286
    DEFENSE_BONUS = 1524
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 762."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_762.ITEM_ID, "name": ItemDefinition_762.NAME, "atk": ItemDefinition_762.ATTACK_BONUS, "def": ItemDefinition_762.DEFENSE_BONUS}


class ItemDefinition_763:
    ITEM_ID = "item_763"
    NAME = "Hyperion Legendary Artifact #763"
    TYPE = "Weapon" if 763 % 2 == 0 else "Armor"
    RARITY = "Epic" if 763 % 5 == 0 else "Legendary"
    BASE_VALUE = 38150
    ATTACK_BONUS = 2289
    DEFENSE_BONUS = 1526
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 763."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_763.ITEM_ID, "name": ItemDefinition_763.NAME, "atk": ItemDefinition_763.ATTACK_BONUS, "def": ItemDefinition_763.DEFENSE_BONUS}


class ItemDefinition_764:
    ITEM_ID = "item_764"
    NAME = "Hyperion Legendary Artifact #764"
    TYPE = "Weapon" if 764 % 2 == 0 else "Armor"
    RARITY = "Epic" if 764 % 5 == 0 else "Legendary"
    BASE_VALUE = 38200
    ATTACK_BONUS = 2292
    DEFENSE_BONUS = 1528
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 764."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_764.ITEM_ID, "name": ItemDefinition_764.NAME, "atk": ItemDefinition_764.ATTACK_BONUS, "def": ItemDefinition_764.DEFENSE_BONUS}


class ItemDefinition_765:
    ITEM_ID = "item_765"
    NAME = "Hyperion Legendary Artifact #765"
    TYPE = "Weapon" if 765 % 2 == 0 else "Armor"
    RARITY = "Epic" if 765 % 5 == 0 else "Legendary"
    BASE_VALUE = 38250
    ATTACK_BONUS = 2295
    DEFENSE_BONUS = 1530
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 765."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_765.ITEM_ID, "name": ItemDefinition_765.NAME, "atk": ItemDefinition_765.ATTACK_BONUS, "def": ItemDefinition_765.DEFENSE_BONUS}


class ItemDefinition_766:
    ITEM_ID = "item_766"
    NAME = "Hyperion Legendary Artifact #766"
    TYPE = "Weapon" if 766 % 2 == 0 else "Armor"
    RARITY = "Epic" if 766 % 5 == 0 else "Legendary"
    BASE_VALUE = 38300
    ATTACK_BONUS = 2298
    DEFENSE_BONUS = 1532
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 766."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_766.ITEM_ID, "name": ItemDefinition_766.NAME, "atk": ItemDefinition_766.ATTACK_BONUS, "def": ItemDefinition_766.DEFENSE_BONUS}


class ItemDefinition_767:
    ITEM_ID = "item_767"
    NAME = "Hyperion Legendary Artifact #767"
    TYPE = "Weapon" if 767 % 2 == 0 else "Armor"
    RARITY = "Epic" if 767 % 5 == 0 else "Legendary"
    BASE_VALUE = 38350
    ATTACK_BONUS = 2301
    DEFENSE_BONUS = 1534
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 767."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_767.ITEM_ID, "name": ItemDefinition_767.NAME, "atk": ItemDefinition_767.ATTACK_BONUS, "def": ItemDefinition_767.DEFENSE_BONUS}


class ItemDefinition_768:
    ITEM_ID = "item_768"
    NAME = "Hyperion Legendary Artifact #768"
    TYPE = "Weapon" if 768 % 2 == 0 else "Armor"
    RARITY = "Epic" if 768 % 5 == 0 else "Legendary"
    BASE_VALUE = 38400
    ATTACK_BONUS = 2304
    DEFENSE_BONUS = 1536
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 768."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_768.ITEM_ID, "name": ItemDefinition_768.NAME, "atk": ItemDefinition_768.ATTACK_BONUS, "def": ItemDefinition_768.DEFENSE_BONUS}


class ItemDefinition_769:
    ITEM_ID = "item_769"
    NAME = "Hyperion Legendary Artifact #769"
    TYPE = "Weapon" if 769 % 2 == 0 else "Armor"
    RARITY = "Epic" if 769 % 5 == 0 else "Legendary"
    BASE_VALUE = 38450
    ATTACK_BONUS = 2307
    DEFENSE_BONUS = 1538
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 769."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_769.ITEM_ID, "name": ItemDefinition_769.NAME, "atk": ItemDefinition_769.ATTACK_BONUS, "def": ItemDefinition_769.DEFENSE_BONUS}


class ItemDefinition_770:
    ITEM_ID = "item_770"
    NAME = "Hyperion Legendary Artifact #770"
    TYPE = "Weapon" if 770 % 2 == 0 else "Armor"
    RARITY = "Epic" if 770 % 5 == 0 else "Legendary"
    BASE_VALUE = 38500
    ATTACK_BONUS = 2310
    DEFENSE_BONUS = 1540
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 770."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_770.ITEM_ID, "name": ItemDefinition_770.NAME, "atk": ItemDefinition_770.ATTACK_BONUS, "def": ItemDefinition_770.DEFENSE_BONUS}


class ItemDefinition_771:
    ITEM_ID = "item_771"
    NAME = "Hyperion Legendary Artifact #771"
    TYPE = "Weapon" if 771 % 2 == 0 else "Armor"
    RARITY = "Epic" if 771 % 5 == 0 else "Legendary"
    BASE_VALUE = 38550
    ATTACK_BONUS = 2313
    DEFENSE_BONUS = 1542
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 771."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_771.ITEM_ID, "name": ItemDefinition_771.NAME, "atk": ItemDefinition_771.ATTACK_BONUS, "def": ItemDefinition_771.DEFENSE_BONUS}


class ItemDefinition_772:
    ITEM_ID = "item_772"
    NAME = "Hyperion Legendary Artifact #772"
    TYPE = "Weapon" if 772 % 2 == 0 else "Armor"
    RARITY = "Epic" if 772 % 5 == 0 else "Legendary"
    BASE_VALUE = 38600
    ATTACK_BONUS = 2316
    DEFENSE_BONUS = 1544
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 772."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_772.ITEM_ID, "name": ItemDefinition_772.NAME, "atk": ItemDefinition_772.ATTACK_BONUS, "def": ItemDefinition_772.DEFENSE_BONUS}


class ItemDefinition_773:
    ITEM_ID = "item_773"
    NAME = "Hyperion Legendary Artifact #773"
    TYPE = "Weapon" if 773 % 2 == 0 else "Armor"
    RARITY = "Epic" if 773 % 5 == 0 else "Legendary"
    BASE_VALUE = 38650
    ATTACK_BONUS = 2319
    DEFENSE_BONUS = 1546
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 773."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_773.ITEM_ID, "name": ItemDefinition_773.NAME, "atk": ItemDefinition_773.ATTACK_BONUS, "def": ItemDefinition_773.DEFENSE_BONUS}


class ItemDefinition_774:
    ITEM_ID = "item_774"
    NAME = "Hyperion Legendary Artifact #774"
    TYPE = "Weapon" if 774 % 2 == 0 else "Armor"
    RARITY = "Epic" if 774 % 5 == 0 else "Legendary"
    BASE_VALUE = 38700
    ATTACK_BONUS = 2322
    DEFENSE_BONUS = 1548
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 774."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_774.ITEM_ID, "name": ItemDefinition_774.NAME, "atk": ItemDefinition_774.ATTACK_BONUS, "def": ItemDefinition_774.DEFENSE_BONUS}


class ItemDefinition_775:
    ITEM_ID = "item_775"
    NAME = "Hyperion Legendary Artifact #775"
    TYPE = "Weapon" if 775 % 2 == 0 else "Armor"
    RARITY = "Epic" if 775 % 5 == 0 else "Legendary"
    BASE_VALUE = 38750
    ATTACK_BONUS = 2325
    DEFENSE_BONUS = 1550
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 775."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_775.ITEM_ID, "name": ItemDefinition_775.NAME, "atk": ItemDefinition_775.ATTACK_BONUS, "def": ItemDefinition_775.DEFENSE_BONUS}


class ItemDefinition_776:
    ITEM_ID = "item_776"
    NAME = "Hyperion Legendary Artifact #776"
    TYPE = "Weapon" if 776 % 2 == 0 else "Armor"
    RARITY = "Epic" if 776 % 5 == 0 else "Legendary"
    BASE_VALUE = 38800
    ATTACK_BONUS = 2328
    DEFENSE_BONUS = 1552
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 776."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_776.ITEM_ID, "name": ItemDefinition_776.NAME, "atk": ItemDefinition_776.ATTACK_BONUS, "def": ItemDefinition_776.DEFENSE_BONUS}


class ItemDefinition_777:
    ITEM_ID = "item_777"
    NAME = "Hyperion Legendary Artifact #777"
    TYPE = "Weapon" if 777 % 2 == 0 else "Armor"
    RARITY = "Epic" if 777 % 5 == 0 else "Legendary"
    BASE_VALUE = 38850
    ATTACK_BONUS = 2331
    DEFENSE_BONUS = 1554
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 777."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_777.ITEM_ID, "name": ItemDefinition_777.NAME, "atk": ItemDefinition_777.ATTACK_BONUS, "def": ItemDefinition_777.DEFENSE_BONUS}


class ItemDefinition_778:
    ITEM_ID = "item_778"
    NAME = "Hyperion Legendary Artifact #778"
    TYPE = "Weapon" if 778 % 2 == 0 else "Armor"
    RARITY = "Epic" if 778 % 5 == 0 else "Legendary"
    BASE_VALUE = 38900
    ATTACK_BONUS = 2334
    DEFENSE_BONUS = 1556
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 778."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_778.ITEM_ID, "name": ItemDefinition_778.NAME, "atk": ItemDefinition_778.ATTACK_BONUS, "def": ItemDefinition_778.DEFENSE_BONUS}


class ItemDefinition_779:
    ITEM_ID = "item_779"
    NAME = "Hyperion Legendary Artifact #779"
    TYPE = "Weapon" if 779 % 2 == 0 else "Armor"
    RARITY = "Epic" if 779 % 5 == 0 else "Legendary"
    BASE_VALUE = 38950
    ATTACK_BONUS = 2337
    DEFENSE_BONUS = 1558
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 779."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_779.ITEM_ID, "name": ItemDefinition_779.NAME, "atk": ItemDefinition_779.ATTACK_BONUS, "def": ItemDefinition_779.DEFENSE_BONUS}


class ItemDefinition_780:
    ITEM_ID = "item_780"
    NAME = "Hyperion Legendary Artifact #780"
    TYPE = "Weapon" if 780 % 2 == 0 else "Armor"
    RARITY = "Epic" if 780 % 5 == 0 else "Legendary"
    BASE_VALUE = 39000
    ATTACK_BONUS = 2340
    DEFENSE_BONUS = 1560
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 780."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_780.ITEM_ID, "name": ItemDefinition_780.NAME, "atk": ItemDefinition_780.ATTACK_BONUS, "def": ItemDefinition_780.DEFENSE_BONUS}


class ItemDefinition_781:
    ITEM_ID = "item_781"
    NAME = "Hyperion Legendary Artifact #781"
    TYPE = "Weapon" if 781 % 2 == 0 else "Armor"
    RARITY = "Epic" if 781 % 5 == 0 else "Legendary"
    BASE_VALUE = 39050
    ATTACK_BONUS = 2343
    DEFENSE_BONUS = 1562
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 781."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_781.ITEM_ID, "name": ItemDefinition_781.NAME, "atk": ItemDefinition_781.ATTACK_BONUS, "def": ItemDefinition_781.DEFENSE_BONUS}


class ItemDefinition_782:
    ITEM_ID = "item_782"
    NAME = "Hyperion Legendary Artifact #782"
    TYPE = "Weapon" if 782 % 2 == 0 else "Armor"
    RARITY = "Epic" if 782 % 5 == 0 else "Legendary"
    BASE_VALUE = 39100
    ATTACK_BONUS = 2346
    DEFENSE_BONUS = 1564
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 782."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_782.ITEM_ID, "name": ItemDefinition_782.NAME, "atk": ItemDefinition_782.ATTACK_BONUS, "def": ItemDefinition_782.DEFENSE_BONUS}


class ItemDefinition_783:
    ITEM_ID = "item_783"
    NAME = "Hyperion Legendary Artifact #783"
    TYPE = "Weapon" if 783 % 2 == 0 else "Armor"
    RARITY = "Epic" if 783 % 5 == 0 else "Legendary"
    BASE_VALUE = 39150
    ATTACK_BONUS = 2349
    DEFENSE_BONUS = 1566
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 783."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_783.ITEM_ID, "name": ItemDefinition_783.NAME, "atk": ItemDefinition_783.ATTACK_BONUS, "def": ItemDefinition_783.DEFENSE_BONUS}


class ItemDefinition_784:
    ITEM_ID = "item_784"
    NAME = "Hyperion Legendary Artifact #784"
    TYPE = "Weapon" if 784 % 2 == 0 else "Armor"
    RARITY = "Epic" if 784 % 5 == 0 else "Legendary"
    BASE_VALUE = 39200
    ATTACK_BONUS = 2352
    DEFENSE_BONUS = 1568
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 784."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_784.ITEM_ID, "name": ItemDefinition_784.NAME, "atk": ItemDefinition_784.ATTACK_BONUS, "def": ItemDefinition_784.DEFENSE_BONUS}


class ItemDefinition_785:
    ITEM_ID = "item_785"
    NAME = "Hyperion Legendary Artifact #785"
    TYPE = "Weapon" if 785 % 2 == 0 else "Armor"
    RARITY = "Epic" if 785 % 5 == 0 else "Legendary"
    BASE_VALUE = 39250
    ATTACK_BONUS = 2355
    DEFENSE_BONUS = 1570
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 785."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_785.ITEM_ID, "name": ItemDefinition_785.NAME, "atk": ItemDefinition_785.ATTACK_BONUS, "def": ItemDefinition_785.DEFENSE_BONUS}


class ItemDefinition_786:
    ITEM_ID = "item_786"
    NAME = "Hyperion Legendary Artifact #786"
    TYPE = "Weapon" if 786 % 2 == 0 else "Armor"
    RARITY = "Epic" if 786 % 5 == 0 else "Legendary"
    BASE_VALUE = 39300
    ATTACK_BONUS = 2358
    DEFENSE_BONUS = 1572
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 786."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_786.ITEM_ID, "name": ItemDefinition_786.NAME, "atk": ItemDefinition_786.ATTACK_BONUS, "def": ItemDefinition_786.DEFENSE_BONUS}


class ItemDefinition_787:
    ITEM_ID = "item_787"
    NAME = "Hyperion Legendary Artifact #787"
    TYPE = "Weapon" if 787 % 2 == 0 else "Armor"
    RARITY = "Epic" if 787 % 5 == 0 else "Legendary"
    BASE_VALUE = 39350
    ATTACK_BONUS = 2361
    DEFENSE_BONUS = 1574
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 787."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_787.ITEM_ID, "name": ItemDefinition_787.NAME, "atk": ItemDefinition_787.ATTACK_BONUS, "def": ItemDefinition_787.DEFENSE_BONUS}


class ItemDefinition_788:
    ITEM_ID = "item_788"
    NAME = "Hyperion Legendary Artifact #788"
    TYPE = "Weapon" if 788 % 2 == 0 else "Armor"
    RARITY = "Epic" if 788 % 5 == 0 else "Legendary"
    BASE_VALUE = 39400
    ATTACK_BONUS = 2364
    DEFENSE_BONUS = 1576
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 788."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_788.ITEM_ID, "name": ItemDefinition_788.NAME, "atk": ItemDefinition_788.ATTACK_BONUS, "def": ItemDefinition_788.DEFENSE_BONUS}


class ItemDefinition_789:
    ITEM_ID = "item_789"
    NAME = "Hyperion Legendary Artifact #789"
    TYPE = "Weapon" if 789 % 2 == 0 else "Armor"
    RARITY = "Epic" if 789 % 5 == 0 else "Legendary"
    BASE_VALUE = 39450
    ATTACK_BONUS = 2367
    DEFENSE_BONUS = 1578
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 789."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_789.ITEM_ID, "name": ItemDefinition_789.NAME, "atk": ItemDefinition_789.ATTACK_BONUS, "def": ItemDefinition_789.DEFENSE_BONUS}


class ItemDefinition_790:
    ITEM_ID = "item_790"
    NAME = "Hyperion Legendary Artifact #790"
    TYPE = "Weapon" if 790 % 2 == 0 else "Armor"
    RARITY = "Epic" if 790 % 5 == 0 else "Legendary"
    BASE_VALUE = 39500
    ATTACK_BONUS = 2370
    DEFENSE_BONUS = 1580
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 790."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_790.ITEM_ID, "name": ItemDefinition_790.NAME, "atk": ItemDefinition_790.ATTACK_BONUS, "def": ItemDefinition_790.DEFENSE_BONUS}


class ItemDefinition_791:
    ITEM_ID = "item_791"
    NAME = "Hyperion Legendary Artifact #791"
    TYPE = "Weapon" if 791 % 2 == 0 else "Armor"
    RARITY = "Epic" if 791 % 5 == 0 else "Legendary"
    BASE_VALUE = 39550
    ATTACK_BONUS = 2373
    DEFENSE_BONUS = 1582
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 791."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_791.ITEM_ID, "name": ItemDefinition_791.NAME, "atk": ItemDefinition_791.ATTACK_BONUS, "def": ItemDefinition_791.DEFENSE_BONUS}


class ItemDefinition_792:
    ITEM_ID = "item_792"
    NAME = "Hyperion Legendary Artifact #792"
    TYPE = "Weapon" if 792 % 2 == 0 else "Armor"
    RARITY = "Epic" if 792 % 5 == 0 else "Legendary"
    BASE_VALUE = 39600
    ATTACK_BONUS = 2376
    DEFENSE_BONUS = 1584
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 792."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_792.ITEM_ID, "name": ItemDefinition_792.NAME, "atk": ItemDefinition_792.ATTACK_BONUS, "def": ItemDefinition_792.DEFENSE_BONUS}


class ItemDefinition_793:
    ITEM_ID = "item_793"
    NAME = "Hyperion Legendary Artifact #793"
    TYPE = "Weapon" if 793 % 2 == 0 else "Armor"
    RARITY = "Epic" if 793 % 5 == 0 else "Legendary"
    BASE_VALUE = 39650
    ATTACK_BONUS = 2379
    DEFENSE_BONUS = 1586
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 793."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_793.ITEM_ID, "name": ItemDefinition_793.NAME, "atk": ItemDefinition_793.ATTACK_BONUS, "def": ItemDefinition_793.DEFENSE_BONUS}


class ItemDefinition_794:
    ITEM_ID = "item_794"
    NAME = "Hyperion Legendary Artifact #794"
    TYPE = "Weapon" if 794 % 2 == 0 else "Armor"
    RARITY = "Epic" if 794 % 5 == 0 else "Legendary"
    BASE_VALUE = 39700
    ATTACK_BONUS = 2382
    DEFENSE_BONUS = 1588
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 794."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_794.ITEM_ID, "name": ItemDefinition_794.NAME, "atk": ItemDefinition_794.ATTACK_BONUS, "def": ItemDefinition_794.DEFENSE_BONUS}


class ItemDefinition_795:
    ITEM_ID = "item_795"
    NAME = "Hyperion Legendary Artifact #795"
    TYPE = "Weapon" if 795 % 2 == 0 else "Armor"
    RARITY = "Epic" if 795 % 5 == 0 else "Legendary"
    BASE_VALUE = 39750
    ATTACK_BONUS = 2385
    DEFENSE_BONUS = 1590
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 795."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_795.ITEM_ID, "name": ItemDefinition_795.NAME, "atk": ItemDefinition_795.ATTACK_BONUS, "def": ItemDefinition_795.DEFENSE_BONUS}


class ItemDefinition_796:
    ITEM_ID = "item_796"
    NAME = "Hyperion Legendary Artifact #796"
    TYPE = "Weapon" if 796 % 2 == 0 else "Armor"
    RARITY = "Epic" if 796 % 5 == 0 else "Legendary"
    BASE_VALUE = 39800
    ATTACK_BONUS = 2388
    DEFENSE_BONUS = 1592
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 796."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_796.ITEM_ID, "name": ItemDefinition_796.NAME, "atk": ItemDefinition_796.ATTACK_BONUS, "def": ItemDefinition_796.DEFENSE_BONUS}


class ItemDefinition_797:
    ITEM_ID = "item_797"
    NAME = "Hyperion Legendary Artifact #797"
    TYPE = "Weapon" if 797 % 2 == 0 else "Armor"
    RARITY = "Epic" if 797 % 5 == 0 else "Legendary"
    BASE_VALUE = 39850
    ATTACK_BONUS = 2391
    DEFENSE_BONUS = 1594
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 797."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_797.ITEM_ID, "name": ItemDefinition_797.NAME, "atk": ItemDefinition_797.ATTACK_BONUS, "def": ItemDefinition_797.DEFENSE_BONUS}


class ItemDefinition_798:
    ITEM_ID = "item_798"
    NAME = "Hyperion Legendary Artifact #798"
    TYPE = "Weapon" if 798 % 2 == 0 else "Armor"
    RARITY = "Epic" if 798 % 5 == 0 else "Legendary"
    BASE_VALUE = 39900
    ATTACK_BONUS = 2394
    DEFENSE_BONUS = 1596
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 798."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_798.ITEM_ID, "name": ItemDefinition_798.NAME, "atk": ItemDefinition_798.ATTACK_BONUS, "def": ItemDefinition_798.DEFENSE_BONUS}


class ItemDefinition_799:
    ITEM_ID = "item_799"
    NAME = "Hyperion Legendary Artifact #799"
    TYPE = "Weapon" if 799 % 2 == 0 else "Armor"
    RARITY = "Epic" if 799 % 5 == 0 else "Legendary"
    BASE_VALUE = 39950
    ATTACK_BONUS = 2397
    DEFENSE_BONUS = 1598
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 799."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_799.ITEM_ID, "name": ItemDefinition_799.NAME, "atk": ItemDefinition_799.ATTACK_BONUS, "def": ItemDefinition_799.DEFENSE_BONUS}


class ItemDefinition_800:
    ITEM_ID = "item_800"
    NAME = "Hyperion Legendary Artifact #800"
    TYPE = "Weapon" if 800 % 2 == 0 else "Armor"
    RARITY = "Epic" if 800 % 5 == 0 else "Legendary"
    BASE_VALUE = 40000
    ATTACK_BONUS = 2400
    DEFENSE_BONUS = 1600
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 800."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_800.ITEM_ID, "name": ItemDefinition_800.NAME, "atk": ItemDefinition_800.ATTACK_BONUS, "def": ItemDefinition_800.DEFENSE_BONUS}


class ItemDefinition_801:
    ITEM_ID = "item_801"
    NAME = "Hyperion Legendary Artifact #801"
    TYPE = "Weapon" if 801 % 2 == 0 else "Armor"
    RARITY = "Epic" if 801 % 5 == 0 else "Legendary"
    BASE_VALUE = 40050
    ATTACK_BONUS = 2403
    DEFENSE_BONUS = 1602
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 801."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_801.ITEM_ID, "name": ItemDefinition_801.NAME, "atk": ItemDefinition_801.ATTACK_BONUS, "def": ItemDefinition_801.DEFENSE_BONUS}


class ItemDefinition_802:
    ITEM_ID = "item_802"
    NAME = "Hyperion Legendary Artifact #802"
    TYPE = "Weapon" if 802 % 2 == 0 else "Armor"
    RARITY = "Epic" if 802 % 5 == 0 else "Legendary"
    BASE_VALUE = 40100
    ATTACK_BONUS = 2406
    DEFENSE_BONUS = 1604
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 802."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_802.ITEM_ID, "name": ItemDefinition_802.NAME, "atk": ItemDefinition_802.ATTACK_BONUS, "def": ItemDefinition_802.DEFENSE_BONUS}


class ItemDefinition_803:
    ITEM_ID = "item_803"
    NAME = "Hyperion Legendary Artifact #803"
    TYPE = "Weapon" if 803 % 2 == 0 else "Armor"
    RARITY = "Epic" if 803 % 5 == 0 else "Legendary"
    BASE_VALUE = 40150
    ATTACK_BONUS = 2409
    DEFENSE_BONUS = 1606
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 803."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_803.ITEM_ID, "name": ItemDefinition_803.NAME, "atk": ItemDefinition_803.ATTACK_BONUS, "def": ItemDefinition_803.DEFENSE_BONUS}


class ItemDefinition_804:
    ITEM_ID = "item_804"
    NAME = "Hyperion Legendary Artifact #804"
    TYPE = "Weapon" if 804 % 2 == 0 else "Armor"
    RARITY = "Epic" if 804 % 5 == 0 else "Legendary"
    BASE_VALUE = 40200
    ATTACK_BONUS = 2412
    DEFENSE_BONUS = 1608
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 804."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_804.ITEM_ID, "name": ItemDefinition_804.NAME, "atk": ItemDefinition_804.ATTACK_BONUS, "def": ItemDefinition_804.DEFENSE_BONUS}


class ItemDefinition_805:
    ITEM_ID = "item_805"
    NAME = "Hyperion Legendary Artifact #805"
    TYPE = "Weapon" if 805 % 2 == 0 else "Armor"
    RARITY = "Epic" if 805 % 5 == 0 else "Legendary"
    BASE_VALUE = 40250
    ATTACK_BONUS = 2415
    DEFENSE_BONUS = 1610
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 805."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_805.ITEM_ID, "name": ItemDefinition_805.NAME, "atk": ItemDefinition_805.ATTACK_BONUS, "def": ItemDefinition_805.DEFENSE_BONUS}


class ItemDefinition_806:
    ITEM_ID = "item_806"
    NAME = "Hyperion Legendary Artifact #806"
    TYPE = "Weapon" if 806 % 2 == 0 else "Armor"
    RARITY = "Epic" if 806 % 5 == 0 else "Legendary"
    BASE_VALUE = 40300
    ATTACK_BONUS = 2418
    DEFENSE_BONUS = 1612
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 806."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_806.ITEM_ID, "name": ItemDefinition_806.NAME, "atk": ItemDefinition_806.ATTACK_BONUS, "def": ItemDefinition_806.DEFENSE_BONUS}


class ItemDefinition_807:
    ITEM_ID = "item_807"
    NAME = "Hyperion Legendary Artifact #807"
    TYPE = "Weapon" if 807 % 2 == 0 else "Armor"
    RARITY = "Epic" if 807 % 5 == 0 else "Legendary"
    BASE_VALUE = 40350
    ATTACK_BONUS = 2421
    DEFENSE_BONUS = 1614
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 807."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_807.ITEM_ID, "name": ItemDefinition_807.NAME, "atk": ItemDefinition_807.ATTACK_BONUS, "def": ItemDefinition_807.DEFENSE_BONUS}


class ItemDefinition_808:
    ITEM_ID = "item_808"
    NAME = "Hyperion Legendary Artifact #808"
    TYPE = "Weapon" if 808 % 2 == 0 else "Armor"
    RARITY = "Epic" if 808 % 5 == 0 else "Legendary"
    BASE_VALUE = 40400
    ATTACK_BONUS = 2424
    DEFENSE_BONUS = 1616
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 808."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_808.ITEM_ID, "name": ItemDefinition_808.NAME, "atk": ItemDefinition_808.ATTACK_BONUS, "def": ItemDefinition_808.DEFENSE_BONUS}


class ItemDefinition_809:
    ITEM_ID = "item_809"
    NAME = "Hyperion Legendary Artifact #809"
    TYPE = "Weapon" if 809 % 2 == 0 else "Armor"
    RARITY = "Epic" if 809 % 5 == 0 else "Legendary"
    BASE_VALUE = 40450
    ATTACK_BONUS = 2427
    DEFENSE_BONUS = 1618
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 809."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_809.ITEM_ID, "name": ItemDefinition_809.NAME, "atk": ItemDefinition_809.ATTACK_BONUS, "def": ItemDefinition_809.DEFENSE_BONUS}


class ItemDefinition_810:
    ITEM_ID = "item_810"
    NAME = "Hyperion Legendary Artifact #810"
    TYPE = "Weapon" if 810 % 2 == 0 else "Armor"
    RARITY = "Epic" if 810 % 5 == 0 else "Legendary"
    BASE_VALUE = 40500
    ATTACK_BONUS = 2430
    DEFENSE_BONUS = 1620
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 810."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_810.ITEM_ID, "name": ItemDefinition_810.NAME, "atk": ItemDefinition_810.ATTACK_BONUS, "def": ItemDefinition_810.DEFENSE_BONUS}


class ItemDefinition_811:
    ITEM_ID = "item_811"
    NAME = "Hyperion Legendary Artifact #811"
    TYPE = "Weapon" if 811 % 2 == 0 else "Armor"
    RARITY = "Epic" if 811 % 5 == 0 else "Legendary"
    BASE_VALUE = 40550
    ATTACK_BONUS = 2433
    DEFENSE_BONUS = 1622
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 811."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_811.ITEM_ID, "name": ItemDefinition_811.NAME, "atk": ItemDefinition_811.ATTACK_BONUS, "def": ItemDefinition_811.DEFENSE_BONUS}


class ItemDefinition_812:
    ITEM_ID = "item_812"
    NAME = "Hyperion Legendary Artifact #812"
    TYPE = "Weapon" if 812 % 2 == 0 else "Armor"
    RARITY = "Epic" if 812 % 5 == 0 else "Legendary"
    BASE_VALUE = 40600
    ATTACK_BONUS = 2436
    DEFENSE_BONUS = 1624
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 812."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_812.ITEM_ID, "name": ItemDefinition_812.NAME, "atk": ItemDefinition_812.ATTACK_BONUS, "def": ItemDefinition_812.DEFENSE_BONUS}


class ItemDefinition_813:
    ITEM_ID = "item_813"
    NAME = "Hyperion Legendary Artifact #813"
    TYPE = "Weapon" if 813 % 2 == 0 else "Armor"
    RARITY = "Epic" if 813 % 5 == 0 else "Legendary"
    BASE_VALUE = 40650
    ATTACK_BONUS = 2439
    DEFENSE_BONUS = 1626
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 813."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_813.ITEM_ID, "name": ItemDefinition_813.NAME, "atk": ItemDefinition_813.ATTACK_BONUS, "def": ItemDefinition_813.DEFENSE_BONUS}


class ItemDefinition_814:
    ITEM_ID = "item_814"
    NAME = "Hyperion Legendary Artifact #814"
    TYPE = "Weapon" if 814 % 2 == 0 else "Armor"
    RARITY = "Epic" if 814 % 5 == 0 else "Legendary"
    BASE_VALUE = 40700
    ATTACK_BONUS = 2442
    DEFENSE_BONUS = 1628
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 814."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_814.ITEM_ID, "name": ItemDefinition_814.NAME, "atk": ItemDefinition_814.ATTACK_BONUS, "def": ItemDefinition_814.DEFENSE_BONUS}


class ItemDefinition_815:
    ITEM_ID = "item_815"
    NAME = "Hyperion Legendary Artifact #815"
    TYPE = "Weapon" if 815 % 2 == 0 else "Armor"
    RARITY = "Epic" if 815 % 5 == 0 else "Legendary"
    BASE_VALUE = 40750
    ATTACK_BONUS = 2445
    DEFENSE_BONUS = 1630
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 815."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_815.ITEM_ID, "name": ItemDefinition_815.NAME, "atk": ItemDefinition_815.ATTACK_BONUS, "def": ItemDefinition_815.DEFENSE_BONUS}


class ItemDefinition_816:
    ITEM_ID = "item_816"
    NAME = "Hyperion Legendary Artifact #816"
    TYPE = "Weapon" if 816 % 2 == 0 else "Armor"
    RARITY = "Epic" if 816 % 5 == 0 else "Legendary"
    BASE_VALUE = 40800
    ATTACK_BONUS = 2448
    DEFENSE_BONUS = 1632
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 816."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_816.ITEM_ID, "name": ItemDefinition_816.NAME, "atk": ItemDefinition_816.ATTACK_BONUS, "def": ItemDefinition_816.DEFENSE_BONUS}


class ItemDefinition_817:
    ITEM_ID = "item_817"
    NAME = "Hyperion Legendary Artifact #817"
    TYPE = "Weapon" if 817 % 2 == 0 else "Armor"
    RARITY = "Epic" if 817 % 5 == 0 else "Legendary"
    BASE_VALUE = 40850
    ATTACK_BONUS = 2451
    DEFENSE_BONUS = 1634
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 817."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_817.ITEM_ID, "name": ItemDefinition_817.NAME, "atk": ItemDefinition_817.ATTACK_BONUS, "def": ItemDefinition_817.DEFENSE_BONUS}


class ItemDefinition_818:
    ITEM_ID = "item_818"
    NAME = "Hyperion Legendary Artifact #818"
    TYPE = "Weapon" if 818 % 2 == 0 else "Armor"
    RARITY = "Epic" if 818 % 5 == 0 else "Legendary"
    BASE_VALUE = 40900
    ATTACK_BONUS = 2454
    DEFENSE_BONUS = 1636
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 818."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_818.ITEM_ID, "name": ItemDefinition_818.NAME, "atk": ItemDefinition_818.ATTACK_BONUS, "def": ItemDefinition_818.DEFENSE_BONUS}


class ItemDefinition_819:
    ITEM_ID = "item_819"
    NAME = "Hyperion Legendary Artifact #819"
    TYPE = "Weapon" if 819 % 2 == 0 else "Armor"
    RARITY = "Epic" if 819 % 5 == 0 else "Legendary"
    BASE_VALUE = 40950
    ATTACK_BONUS = 2457
    DEFENSE_BONUS = 1638
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 819."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_819.ITEM_ID, "name": ItemDefinition_819.NAME, "atk": ItemDefinition_819.ATTACK_BONUS, "def": ItemDefinition_819.DEFENSE_BONUS}


class ItemDefinition_820:
    ITEM_ID = "item_820"
    NAME = "Hyperion Legendary Artifact #820"
    TYPE = "Weapon" if 820 % 2 == 0 else "Armor"
    RARITY = "Epic" if 820 % 5 == 0 else "Legendary"
    BASE_VALUE = 41000
    ATTACK_BONUS = 2460
    DEFENSE_BONUS = 1640
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 820."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_820.ITEM_ID, "name": ItemDefinition_820.NAME, "atk": ItemDefinition_820.ATTACK_BONUS, "def": ItemDefinition_820.DEFENSE_BONUS}


class ItemDefinition_821:
    ITEM_ID = "item_821"
    NAME = "Hyperion Legendary Artifact #821"
    TYPE = "Weapon" if 821 % 2 == 0 else "Armor"
    RARITY = "Epic" if 821 % 5 == 0 else "Legendary"
    BASE_VALUE = 41050
    ATTACK_BONUS = 2463
    DEFENSE_BONUS = 1642
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 821."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_821.ITEM_ID, "name": ItemDefinition_821.NAME, "atk": ItemDefinition_821.ATTACK_BONUS, "def": ItemDefinition_821.DEFENSE_BONUS}


class ItemDefinition_822:
    ITEM_ID = "item_822"
    NAME = "Hyperion Legendary Artifact #822"
    TYPE = "Weapon" if 822 % 2 == 0 else "Armor"
    RARITY = "Epic" if 822 % 5 == 0 else "Legendary"
    BASE_VALUE = 41100
    ATTACK_BONUS = 2466
    DEFENSE_BONUS = 1644
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 822."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_822.ITEM_ID, "name": ItemDefinition_822.NAME, "atk": ItemDefinition_822.ATTACK_BONUS, "def": ItemDefinition_822.DEFENSE_BONUS}


class ItemDefinition_823:
    ITEM_ID = "item_823"
    NAME = "Hyperion Legendary Artifact #823"
    TYPE = "Weapon" if 823 % 2 == 0 else "Armor"
    RARITY = "Epic" if 823 % 5 == 0 else "Legendary"
    BASE_VALUE = 41150
    ATTACK_BONUS = 2469
    DEFENSE_BONUS = 1646
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 823."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_823.ITEM_ID, "name": ItemDefinition_823.NAME, "atk": ItemDefinition_823.ATTACK_BONUS, "def": ItemDefinition_823.DEFENSE_BONUS}


class ItemDefinition_824:
    ITEM_ID = "item_824"
    NAME = "Hyperion Legendary Artifact #824"
    TYPE = "Weapon" if 824 % 2 == 0 else "Armor"
    RARITY = "Epic" if 824 % 5 == 0 else "Legendary"
    BASE_VALUE = 41200
    ATTACK_BONUS = 2472
    DEFENSE_BONUS = 1648
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 824."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_824.ITEM_ID, "name": ItemDefinition_824.NAME, "atk": ItemDefinition_824.ATTACK_BONUS, "def": ItemDefinition_824.DEFENSE_BONUS}


class ItemDefinition_825:
    ITEM_ID = "item_825"
    NAME = "Hyperion Legendary Artifact #825"
    TYPE = "Weapon" if 825 % 2 == 0 else "Armor"
    RARITY = "Epic" if 825 % 5 == 0 else "Legendary"
    BASE_VALUE = 41250
    ATTACK_BONUS = 2475
    DEFENSE_BONUS = 1650
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 825."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_825.ITEM_ID, "name": ItemDefinition_825.NAME, "atk": ItemDefinition_825.ATTACK_BONUS, "def": ItemDefinition_825.DEFENSE_BONUS}


class ItemDefinition_826:
    ITEM_ID = "item_826"
    NAME = "Hyperion Legendary Artifact #826"
    TYPE = "Weapon" if 826 % 2 == 0 else "Armor"
    RARITY = "Epic" if 826 % 5 == 0 else "Legendary"
    BASE_VALUE = 41300
    ATTACK_BONUS = 2478
    DEFENSE_BONUS = 1652
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 826."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_826.ITEM_ID, "name": ItemDefinition_826.NAME, "atk": ItemDefinition_826.ATTACK_BONUS, "def": ItemDefinition_826.DEFENSE_BONUS}


class ItemDefinition_827:
    ITEM_ID = "item_827"
    NAME = "Hyperion Legendary Artifact #827"
    TYPE = "Weapon" if 827 % 2 == 0 else "Armor"
    RARITY = "Epic" if 827 % 5 == 0 else "Legendary"
    BASE_VALUE = 41350
    ATTACK_BONUS = 2481
    DEFENSE_BONUS = 1654
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 827."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_827.ITEM_ID, "name": ItemDefinition_827.NAME, "atk": ItemDefinition_827.ATTACK_BONUS, "def": ItemDefinition_827.DEFENSE_BONUS}


class ItemDefinition_828:
    ITEM_ID = "item_828"
    NAME = "Hyperion Legendary Artifact #828"
    TYPE = "Weapon" if 828 % 2 == 0 else "Armor"
    RARITY = "Epic" if 828 % 5 == 0 else "Legendary"
    BASE_VALUE = 41400
    ATTACK_BONUS = 2484
    DEFENSE_BONUS = 1656
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 828."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_828.ITEM_ID, "name": ItemDefinition_828.NAME, "atk": ItemDefinition_828.ATTACK_BONUS, "def": ItemDefinition_828.DEFENSE_BONUS}


class ItemDefinition_829:
    ITEM_ID = "item_829"
    NAME = "Hyperion Legendary Artifact #829"
    TYPE = "Weapon" if 829 % 2 == 0 else "Armor"
    RARITY = "Epic" if 829 % 5 == 0 else "Legendary"
    BASE_VALUE = 41450
    ATTACK_BONUS = 2487
    DEFENSE_BONUS = 1658
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 829."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_829.ITEM_ID, "name": ItemDefinition_829.NAME, "atk": ItemDefinition_829.ATTACK_BONUS, "def": ItemDefinition_829.DEFENSE_BONUS}


class ItemDefinition_830:
    ITEM_ID = "item_830"
    NAME = "Hyperion Legendary Artifact #830"
    TYPE = "Weapon" if 830 % 2 == 0 else "Armor"
    RARITY = "Epic" if 830 % 5 == 0 else "Legendary"
    BASE_VALUE = 41500
    ATTACK_BONUS = 2490
    DEFENSE_BONUS = 1660
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 830."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_830.ITEM_ID, "name": ItemDefinition_830.NAME, "atk": ItemDefinition_830.ATTACK_BONUS, "def": ItemDefinition_830.DEFENSE_BONUS}


class ItemDefinition_831:
    ITEM_ID = "item_831"
    NAME = "Hyperion Legendary Artifact #831"
    TYPE = "Weapon" if 831 % 2 == 0 else "Armor"
    RARITY = "Epic" if 831 % 5 == 0 else "Legendary"
    BASE_VALUE = 41550
    ATTACK_BONUS = 2493
    DEFENSE_BONUS = 1662
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 831."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_831.ITEM_ID, "name": ItemDefinition_831.NAME, "atk": ItemDefinition_831.ATTACK_BONUS, "def": ItemDefinition_831.DEFENSE_BONUS}


class ItemDefinition_832:
    ITEM_ID = "item_832"
    NAME = "Hyperion Legendary Artifact #832"
    TYPE = "Weapon" if 832 % 2 == 0 else "Armor"
    RARITY = "Epic" if 832 % 5 == 0 else "Legendary"
    BASE_VALUE = 41600
    ATTACK_BONUS = 2496
    DEFENSE_BONUS = 1664
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 832."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_832.ITEM_ID, "name": ItemDefinition_832.NAME, "atk": ItemDefinition_832.ATTACK_BONUS, "def": ItemDefinition_832.DEFENSE_BONUS}


class ItemDefinition_833:
    ITEM_ID = "item_833"
    NAME = "Hyperion Legendary Artifact #833"
    TYPE = "Weapon" if 833 % 2 == 0 else "Armor"
    RARITY = "Epic" if 833 % 5 == 0 else "Legendary"
    BASE_VALUE = 41650
    ATTACK_BONUS = 2499
    DEFENSE_BONUS = 1666
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 833."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_833.ITEM_ID, "name": ItemDefinition_833.NAME, "atk": ItemDefinition_833.ATTACK_BONUS, "def": ItemDefinition_833.DEFENSE_BONUS}


class ItemDefinition_834:
    ITEM_ID = "item_834"
    NAME = "Hyperion Legendary Artifact #834"
    TYPE = "Weapon" if 834 % 2 == 0 else "Armor"
    RARITY = "Epic" if 834 % 5 == 0 else "Legendary"
    BASE_VALUE = 41700
    ATTACK_BONUS = 2502
    DEFENSE_BONUS = 1668
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 834."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_834.ITEM_ID, "name": ItemDefinition_834.NAME, "atk": ItemDefinition_834.ATTACK_BONUS, "def": ItemDefinition_834.DEFENSE_BONUS}


class ItemDefinition_835:
    ITEM_ID = "item_835"
    NAME = "Hyperion Legendary Artifact #835"
    TYPE = "Weapon" if 835 % 2 == 0 else "Armor"
    RARITY = "Epic" if 835 % 5 == 0 else "Legendary"
    BASE_VALUE = 41750
    ATTACK_BONUS = 2505
    DEFENSE_BONUS = 1670
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 835."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_835.ITEM_ID, "name": ItemDefinition_835.NAME, "atk": ItemDefinition_835.ATTACK_BONUS, "def": ItemDefinition_835.DEFENSE_BONUS}


class ItemDefinition_836:
    ITEM_ID = "item_836"
    NAME = "Hyperion Legendary Artifact #836"
    TYPE = "Weapon" if 836 % 2 == 0 else "Armor"
    RARITY = "Epic" if 836 % 5 == 0 else "Legendary"
    BASE_VALUE = 41800
    ATTACK_BONUS = 2508
    DEFENSE_BONUS = 1672
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 836."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_836.ITEM_ID, "name": ItemDefinition_836.NAME, "atk": ItemDefinition_836.ATTACK_BONUS, "def": ItemDefinition_836.DEFENSE_BONUS}


class ItemDefinition_837:
    ITEM_ID = "item_837"
    NAME = "Hyperion Legendary Artifact #837"
    TYPE = "Weapon" if 837 % 2 == 0 else "Armor"
    RARITY = "Epic" if 837 % 5 == 0 else "Legendary"
    BASE_VALUE = 41850
    ATTACK_BONUS = 2511
    DEFENSE_BONUS = 1674
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 837."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_837.ITEM_ID, "name": ItemDefinition_837.NAME, "atk": ItemDefinition_837.ATTACK_BONUS, "def": ItemDefinition_837.DEFENSE_BONUS}


class ItemDefinition_838:
    ITEM_ID = "item_838"
    NAME = "Hyperion Legendary Artifact #838"
    TYPE = "Weapon" if 838 % 2 == 0 else "Armor"
    RARITY = "Epic" if 838 % 5 == 0 else "Legendary"
    BASE_VALUE = 41900
    ATTACK_BONUS = 2514
    DEFENSE_BONUS = 1676
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 838."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_838.ITEM_ID, "name": ItemDefinition_838.NAME, "atk": ItemDefinition_838.ATTACK_BONUS, "def": ItemDefinition_838.DEFENSE_BONUS}


class ItemDefinition_839:
    ITEM_ID = "item_839"
    NAME = "Hyperion Legendary Artifact #839"
    TYPE = "Weapon" if 839 % 2 == 0 else "Armor"
    RARITY = "Epic" if 839 % 5 == 0 else "Legendary"
    BASE_VALUE = 41950
    ATTACK_BONUS = 2517
    DEFENSE_BONUS = 1678
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 839."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_839.ITEM_ID, "name": ItemDefinition_839.NAME, "atk": ItemDefinition_839.ATTACK_BONUS, "def": ItemDefinition_839.DEFENSE_BONUS}


class ItemDefinition_840:
    ITEM_ID = "item_840"
    NAME = "Hyperion Legendary Artifact #840"
    TYPE = "Weapon" if 840 % 2 == 0 else "Armor"
    RARITY = "Epic" if 840 % 5 == 0 else "Legendary"
    BASE_VALUE = 42000
    ATTACK_BONUS = 2520
    DEFENSE_BONUS = 1680
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 840."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_840.ITEM_ID, "name": ItemDefinition_840.NAME, "atk": ItemDefinition_840.ATTACK_BONUS, "def": ItemDefinition_840.DEFENSE_BONUS}


class ItemDefinition_841:
    ITEM_ID = "item_841"
    NAME = "Hyperion Legendary Artifact #841"
    TYPE = "Weapon" if 841 % 2 == 0 else "Armor"
    RARITY = "Epic" if 841 % 5 == 0 else "Legendary"
    BASE_VALUE = 42050
    ATTACK_BONUS = 2523
    DEFENSE_BONUS = 1682
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 841."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_841.ITEM_ID, "name": ItemDefinition_841.NAME, "atk": ItemDefinition_841.ATTACK_BONUS, "def": ItemDefinition_841.DEFENSE_BONUS}


class ItemDefinition_842:
    ITEM_ID = "item_842"
    NAME = "Hyperion Legendary Artifact #842"
    TYPE = "Weapon" if 842 % 2 == 0 else "Armor"
    RARITY = "Epic" if 842 % 5 == 0 else "Legendary"
    BASE_VALUE = 42100
    ATTACK_BONUS = 2526
    DEFENSE_BONUS = 1684
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 842."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_842.ITEM_ID, "name": ItemDefinition_842.NAME, "atk": ItemDefinition_842.ATTACK_BONUS, "def": ItemDefinition_842.DEFENSE_BONUS}


class ItemDefinition_843:
    ITEM_ID = "item_843"
    NAME = "Hyperion Legendary Artifact #843"
    TYPE = "Weapon" if 843 % 2 == 0 else "Armor"
    RARITY = "Epic" if 843 % 5 == 0 else "Legendary"
    BASE_VALUE = 42150
    ATTACK_BONUS = 2529
    DEFENSE_BONUS = 1686
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 843."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_843.ITEM_ID, "name": ItemDefinition_843.NAME, "atk": ItemDefinition_843.ATTACK_BONUS, "def": ItemDefinition_843.DEFENSE_BONUS}


class ItemDefinition_844:
    ITEM_ID = "item_844"
    NAME = "Hyperion Legendary Artifact #844"
    TYPE = "Weapon" if 844 % 2 == 0 else "Armor"
    RARITY = "Epic" if 844 % 5 == 0 else "Legendary"
    BASE_VALUE = 42200
    ATTACK_BONUS = 2532
    DEFENSE_BONUS = 1688
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 844."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_844.ITEM_ID, "name": ItemDefinition_844.NAME, "atk": ItemDefinition_844.ATTACK_BONUS, "def": ItemDefinition_844.DEFENSE_BONUS}


class ItemDefinition_845:
    ITEM_ID = "item_845"
    NAME = "Hyperion Legendary Artifact #845"
    TYPE = "Weapon" if 845 % 2 == 0 else "Armor"
    RARITY = "Epic" if 845 % 5 == 0 else "Legendary"
    BASE_VALUE = 42250
    ATTACK_BONUS = 2535
    DEFENSE_BONUS = 1690
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 845."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_845.ITEM_ID, "name": ItemDefinition_845.NAME, "atk": ItemDefinition_845.ATTACK_BONUS, "def": ItemDefinition_845.DEFENSE_BONUS}


class ItemDefinition_846:
    ITEM_ID = "item_846"
    NAME = "Hyperion Legendary Artifact #846"
    TYPE = "Weapon" if 846 % 2 == 0 else "Armor"
    RARITY = "Epic" if 846 % 5 == 0 else "Legendary"
    BASE_VALUE = 42300
    ATTACK_BONUS = 2538
    DEFENSE_BONUS = 1692
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 846."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_846.ITEM_ID, "name": ItemDefinition_846.NAME, "atk": ItemDefinition_846.ATTACK_BONUS, "def": ItemDefinition_846.DEFENSE_BONUS}


class ItemDefinition_847:
    ITEM_ID = "item_847"
    NAME = "Hyperion Legendary Artifact #847"
    TYPE = "Weapon" if 847 % 2 == 0 else "Armor"
    RARITY = "Epic" if 847 % 5 == 0 else "Legendary"
    BASE_VALUE = 42350
    ATTACK_BONUS = 2541
    DEFENSE_BONUS = 1694
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 847."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_847.ITEM_ID, "name": ItemDefinition_847.NAME, "atk": ItemDefinition_847.ATTACK_BONUS, "def": ItemDefinition_847.DEFENSE_BONUS}


class ItemDefinition_848:
    ITEM_ID = "item_848"
    NAME = "Hyperion Legendary Artifact #848"
    TYPE = "Weapon" if 848 % 2 == 0 else "Armor"
    RARITY = "Epic" if 848 % 5 == 0 else "Legendary"
    BASE_VALUE = 42400
    ATTACK_BONUS = 2544
    DEFENSE_BONUS = 1696
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 848."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_848.ITEM_ID, "name": ItemDefinition_848.NAME, "atk": ItemDefinition_848.ATTACK_BONUS, "def": ItemDefinition_848.DEFENSE_BONUS}


class ItemDefinition_849:
    ITEM_ID = "item_849"
    NAME = "Hyperion Legendary Artifact #849"
    TYPE = "Weapon" if 849 % 2 == 0 else "Armor"
    RARITY = "Epic" if 849 % 5 == 0 else "Legendary"
    BASE_VALUE = 42450
    ATTACK_BONUS = 2547
    DEFENSE_BONUS = 1698
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 849."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_849.ITEM_ID, "name": ItemDefinition_849.NAME, "atk": ItemDefinition_849.ATTACK_BONUS, "def": ItemDefinition_849.DEFENSE_BONUS}


class ItemDefinition_850:
    ITEM_ID = "item_850"
    NAME = "Hyperion Legendary Artifact #850"
    TYPE = "Weapon" if 850 % 2 == 0 else "Armor"
    RARITY = "Epic" if 850 % 5 == 0 else "Legendary"
    BASE_VALUE = 42500
    ATTACK_BONUS = 2550
    DEFENSE_BONUS = 1700
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 850."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_850.ITEM_ID, "name": ItemDefinition_850.NAME, "atk": ItemDefinition_850.ATTACK_BONUS, "def": ItemDefinition_850.DEFENSE_BONUS}


class ItemDefinition_851:
    ITEM_ID = "item_851"
    NAME = "Hyperion Legendary Artifact #851"
    TYPE = "Weapon" if 851 % 2 == 0 else "Armor"
    RARITY = "Epic" if 851 % 5 == 0 else "Legendary"
    BASE_VALUE = 42550
    ATTACK_BONUS = 2553
    DEFENSE_BONUS = 1702
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 851."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_851.ITEM_ID, "name": ItemDefinition_851.NAME, "atk": ItemDefinition_851.ATTACK_BONUS, "def": ItemDefinition_851.DEFENSE_BONUS}


class ItemDefinition_852:
    ITEM_ID = "item_852"
    NAME = "Hyperion Legendary Artifact #852"
    TYPE = "Weapon" if 852 % 2 == 0 else "Armor"
    RARITY = "Epic" if 852 % 5 == 0 else "Legendary"
    BASE_VALUE = 42600
    ATTACK_BONUS = 2556
    DEFENSE_BONUS = 1704
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 852."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_852.ITEM_ID, "name": ItemDefinition_852.NAME, "atk": ItemDefinition_852.ATTACK_BONUS, "def": ItemDefinition_852.DEFENSE_BONUS}


class ItemDefinition_853:
    ITEM_ID = "item_853"
    NAME = "Hyperion Legendary Artifact #853"
    TYPE = "Weapon" if 853 % 2 == 0 else "Armor"
    RARITY = "Epic" if 853 % 5 == 0 else "Legendary"
    BASE_VALUE = 42650
    ATTACK_BONUS = 2559
    DEFENSE_BONUS = 1706
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 853."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_853.ITEM_ID, "name": ItemDefinition_853.NAME, "atk": ItemDefinition_853.ATTACK_BONUS, "def": ItemDefinition_853.DEFENSE_BONUS}


class ItemDefinition_854:
    ITEM_ID = "item_854"
    NAME = "Hyperion Legendary Artifact #854"
    TYPE = "Weapon" if 854 % 2 == 0 else "Armor"
    RARITY = "Epic" if 854 % 5 == 0 else "Legendary"
    BASE_VALUE = 42700
    ATTACK_BONUS = 2562
    DEFENSE_BONUS = 1708
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 854."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_854.ITEM_ID, "name": ItemDefinition_854.NAME, "atk": ItemDefinition_854.ATTACK_BONUS, "def": ItemDefinition_854.DEFENSE_BONUS}


class ItemDefinition_855:
    ITEM_ID = "item_855"
    NAME = "Hyperion Legendary Artifact #855"
    TYPE = "Weapon" if 855 % 2 == 0 else "Armor"
    RARITY = "Epic" if 855 % 5 == 0 else "Legendary"
    BASE_VALUE = 42750
    ATTACK_BONUS = 2565
    DEFENSE_BONUS = 1710
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 855."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_855.ITEM_ID, "name": ItemDefinition_855.NAME, "atk": ItemDefinition_855.ATTACK_BONUS, "def": ItemDefinition_855.DEFENSE_BONUS}


class ItemDefinition_856:
    ITEM_ID = "item_856"
    NAME = "Hyperion Legendary Artifact #856"
    TYPE = "Weapon" if 856 % 2 == 0 else "Armor"
    RARITY = "Epic" if 856 % 5 == 0 else "Legendary"
    BASE_VALUE = 42800
    ATTACK_BONUS = 2568
    DEFENSE_BONUS = 1712
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 856."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_856.ITEM_ID, "name": ItemDefinition_856.NAME, "atk": ItemDefinition_856.ATTACK_BONUS, "def": ItemDefinition_856.DEFENSE_BONUS}


class ItemDefinition_857:
    ITEM_ID = "item_857"
    NAME = "Hyperion Legendary Artifact #857"
    TYPE = "Weapon" if 857 % 2 == 0 else "Armor"
    RARITY = "Epic" if 857 % 5 == 0 else "Legendary"
    BASE_VALUE = 42850
    ATTACK_BONUS = 2571
    DEFENSE_BONUS = 1714
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 857."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_857.ITEM_ID, "name": ItemDefinition_857.NAME, "atk": ItemDefinition_857.ATTACK_BONUS, "def": ItemDefinition_857.DEFENSE_BONUS}


class ItemDefinition_858:
    ITEM_ID = "item_858"
    NAME = "Hyperion Legendary Artifact #858"
    TYPE = "Weapon" if 858 % 2 == 0 else "Armor"
    RARITY = "Epic" if 858 % 5 == 0 else "Legendary"
    BASE_VALUE = 42900
    ATTACK_BONUS = 2574
    DEFENSE_BONUS = 1716
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 858."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_858.ITEM_ID, "name": ItemDefinition_858.NAME, "atk": ItemDefinition_858.ATTACK_BONUS, "def": ItemDefinition_858.DEFENSE_BONUS}


class ItemDefinition_859:
    ITEM_ID = "item_859"
    NAME = "Hyperion Legendary Artifact #859"
    TYPE = "Weapon" if 859 % 2 == 0 else "Armor"
    RARITY = "Epic" if 859 % 5 == 0 else "Legendary"
    BASE_VALUE = 42950
    ATTACK_BONUS = 2577
    DEFENSE_BONUS = 1718
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 859."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_859.ITEM_ID, "name": ItemDefinition_859.NAME, "atk": ItemDefinition_859.ATTACK_BONUS, "def": ItemDefinition_859.DEFENSE_BONUS}


class ItemDefinition_860:
    ITEM_ID = "item_860"
    NAME = "Hyperion Legendary Artifact #860"
    TYPE = "Weapon" if 860 % 2 == 0 else "Armor"
    RARITY = "Epic" if 860 % 5 == 0 else "Legendary"
    BASE_VALUE = 43000
    ATTACK_BONUS = 2580
    DEFENSE_BONUS = 1720
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 860."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_860.ITEM_ID, "name": ItemDefinition_860.NAME, "atk": ItemDefinition_860.ATTACK_BONUS, "def": ItemDefinition_860.DEFENSE_BONUS}


class ItemDefinition_861:
    ITEM_ID = "item_861"
    NAME = "Hyperion Legendary Artifact #861"
    TYPE = "Weapon" if 861 % 2 == 0 else "Armor"
    RARITY = "Epic" if 861 % 5 == 0 else "Legendary"
    BASE_VALUE = 43050
    ATTACK_BONUS = 2583
    DEFENSE_BONUS = 1722
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 861."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_861.ITEM_ID, "name": ItemDefinition_861.NAME, "atk": ItemDefinition_861.ATTACK_BONUS, "def": ItemDefinition_861.DEFENSE_BONUS}


class ItemDefinition_862:
    ITEM_ID = "item_862"
    NAME = "Hyperion Legendary Artifact #862"
    TYPE = "Weapon" if 862 % 2 == 0 else "Armor"
    RARITY = "Epic" if 862 % 5 == 0 else "Legendary"
    BASE_VALUE = 43100
    ATTACK_BONUS = 2586
    DEFENSE_BONUS = 1724
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 862."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_862.ITEM_ID, "name": ItemDefinition_862.NAME, "atk": ItemDefinition_862.ATTACK_BONUS, "def": ItemDefinition_862.DEFENSE_BONUS}


class ItemDefinition_863:
    ITEM_ID = "item_863"
    NAME = "Hyperion Legendary Artifact #863"
    TYPE = "Weapon" if 863 % 2 == 0 else "Armor"
    RARITY = "Epic" if 863 % 5 == 0 else "Legendary"
    BASE_VALUE = 43150
    ATTACK_BONUS = 2589
    DEFENSE_BONUS = 1726
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 863."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_863.ITEM_ID, "name": ItemDefinition_863.NAME, "atk": ItemDefinition_863.ATTACK_BONUS, "def": ItemDefinition_863.DEFENSE_BONUS}


class ItemDefinition_864:
    ITEM_ID = "item_864"
    NAME = "Hyperion Legendary Artifact #864"
    TYPE = "Weapon" if 864 % 2 == 0 else "Armor"
    RARITY = "Epic" if 864 % 5 == 0 else "Legendary"
    BASE_VALUE = 43200
    ATTACK_BONUS = 2592
    DEFENSE_BONUS = 1728
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 864."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_864.ITEM_ID, "name": ItemDefinition_864.NAME, "atk": ItemDefinition_864.ATTACK_BONUS, "def": ItemDefinition_864.DEFENSE_BONUS}


class ItemDefinition_865:
    ITEM_ID = "item_865"
    NAME = "Hyperion Legendary Artifact #865"
    TYPE = "Weapon" if 865 % 2 == 0 else "Armor"
    RARITY = "Epic" if 865 % 5 == 0 else "Legendary"
    BASE_VALUE = 43250
    ATTACK_BONUS = 2595
    DEFENSE_BONUS = 1730
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 865."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_865.ITEM_ID, "name": ItemDefinition_865.NAME, "atk": ItemDefinition_865.ATTACK_BONUS, "def": ItemDefinition_865.DEFENSE_BONUS}


class ItemDefinition_866:
    ITEM_ID = "item_866"
    NAME = "Hyperion Legendary Artifact #866"
    TYPE = "Weapon" if 866 % 2 == 0 else "Armor"
    RARITY = "Epic" if 866 % 5 == 0 else "Legendary"
    BASE_VALUE = 43300
    ATTACK_BONUS = 2598
    DEFENSE_BONUS = 1732
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 866."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_866.ITEM_ID, "name": ItemDefinition_866.NAME, "atk": ItemDefinition_866.ATTACK_BONUS, "def": ItemDefinition_866.DEFENSE_BONUS}


class ItemDefinition_867:
    ITEM_ID = "item_867"
    NAME = "Hyperion Legendary Artifact #867"
    TYPE = "Weapon" if 867 % 2 == 0 else "Armor"
    RARITY = "Epic" if 867 % 5 == 0 else "Legendary"
    BASE_VALUE = 43350
    ATTACK_BONUS = 2601
    DEFENSE_BONUS = 1734
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 867."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_867.ITEM_ID, "name": ItemDefinition_867.NAME, "atk": ItemDefinition_867.ATTACK_BONUS, "def": ItemDefinition_867.DEFENSE_BONUS}


class ItemDefinition_868:
    ITEM_ID = "item_868"
    NAME = "Hyperion Legendary Artifact #868"
    TYPE = "Weapon" if 868 % 2 == 0 else "Armor"
    RARITY = "Epic" if 868 % 5 == 0 else "Legendary"
    BASE_VALUE = 43400
    ATTACK_BONUS = 2604
    DEFENSE_BONUS = 1736
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 868."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_868.ITEM_ID, "name": ItemDefinition_868.NAME, "atk": ItemDefinition_868.ATTACK_BONUS, "def": ItemDefinition_868.DEFENSE_BONUS}


class ItemDefinition_869:
    ITEM_ID = "item_869"
    NAME = "Hyperion Legendary Artifact #869"
    TYPE = "Weapon" if 869 % 2 == 0 else "Armor"
    RARITY = "Epic" if 869 % 5 == 0 else "Legendary"
    BASE_VALUE = 43450
    ATTACK_BONUS = 2607
    DEFENSE_BONUS = 1738
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 869."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_869.ITEM_ID, "name": ItemDefinition_869.NAME, "atk": ItemDefinition_869.ATTACK_BONUS, "def": ItemDefinition_869.DEFENSE_BONUS}


class ItemDefinition_870:
    ITEM_ID = "item_870"
    NAME = "Hyperion Legendary Artifact #870"
    TYPE = "Weapon" if 870 % 2 == 0 else "Armor"
    RARITY = "Epic" if 870 % 5 == 0 else "Legendary"
    BASE_VALUE = 43500
    ATTACK_BONUS = 2610
    DEFENSE_BONUS = 1740
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 870."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_870.ITEM_ID, "name": ItemDefinition_870.NAME, "atk": ItemDefinition_870.ATTACK_BONUS, "def": ItemDefinition_870.DEFENSE_BONUS}


class ItemDefinition_871:
    ITEM_ID = "item_871"
    NAME = "Hyperion Legendary Artifact #871"
    TYPE = "Weapon" if 871 % 2 == 0 else "Armor"
    RARITY = "Epic" if 871 % 5 == 0 else "Legendary"
    BASE_VALUE = 43550
    ATTACK_BONUS = 2613
    DEFENSE_BONUS = 1742
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 871."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_871.ITEM_ID, "name": ItemDefinition_871.NAME, "atk": ItemDefinition_871.ATTACK_BONUS, "def": ItemDefinition_871.DEFENSE_BONUS}


class ItemDefinition_872:
    ITEM_ID = "item_872"
    NAME = "Hyperion Legendary Artifact #872"
    TYPE = "Weapon" if 872 % 2 == 0 else "Armor"
    RARITY = "Epic" if 872 % 5 == 0 else "Legendary"
    BASE_VALUE = 43600
    ATTACK_BONUS = 2616
    DEFENSE_BONUS = 1744
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 872."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_872.ITEM_ID, "name": ItemDefinition_872.NAME, "atk": ItemDefinition_872.ATTACK_BONUS, "def": ItemDefinition_872.DEFENSE_BONUS}


class ItemDefinition_873:
    ITEM_ID = "item_873"
    NAME = "Hyperion Legendary Artifact #873"
    TYPE = "Weapon" if 873 % 2 == 0 else "Armor"
    RARITY = "Epic" if 873 % 5 == 0 else "Legendary"
    BASE_VALUE = 43650
    ATTACK_BONUS = 2619
    DEFENSE_BONUS = 1746
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 873."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_873.ITEM_ID, "name": ItemDefinition_873.NAME, "atk": ItemDefinition_873.ATTACK_BONUS, "def": ItemDefinition_873.DEFENSE_BONUS}


class ItemDefinition_874:
    ITEM_ID = "item_874"
    NAME = "Hyperion Legendary Artifact #874"
    TYPE = "Weapon" if 874 % 2 == 0 else "Armor"
    RARITY = "Epic" if 874 % 5 == 0 else "Legendary"
    BASE_VALUE = 43700
    ATTACK_BONUS = 2622
    DEFENSE_BONUS = 1748
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 874."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_874.ITEM_ID, "name": ItemDefinition_874.NAME, "atk": ItemDefinition_874.ATTACK_BONUS, "def": ItemDefinition_874.DEFENSE_BONUS}


class ItemDefinition_875:
    ITEM_ID = "item_875"
    NAME = "Hyperion Legendary Artifact #875"
    TYPE = "Weapon" if 875 % 2 == 0 else "Armor"
    RARITY = "Epic" if 875 % 5 == 0 else "Legendary"
    BASE_VALUE = 43750
    ATTACK_BONUS = 2625
    DEFENSE_BONUS = 1750
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 875."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_875.ITEM_ID, "name": ItemDefinition_875.NAME, "atk": ItemDefinition_875.ATTACK_BONUS, "def": ItemDefinition_875.DEFENSE_BONUS}


class ItemDefinition_876:
    ITEM_ID = "item_876"
    NAME = "Hyperion Legendary Artifact #876"
    TYPE = "Weapon" if 876 % 2 == 0 else "Armor"
    RARITY = "Epic" if 876 % 5 == 0 else "Legendary"
    BASE_VALUE = 43800
    ATTACK_BONUS = 2628
    DEFENSE_BONUS = 1752
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 876."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_876.ITEM_ID, "name": ItemDefinition_876.NAME, "atk": ItemDefinition_876.ATTACK_BONUS, "def": ItemDefinition_876.DEFENSE_BONUS}


class ItemDefinition_877:
    ITEM_ID = "item_877"
    NAME = "Hyperion Legendary Artifact #877"
    TYPE = "Weapon" if 877 % 2 == 0 else "Armor"
    RARITY = "Epic" if 877 % 5 == 0 else "Legendary"
    BASE_VALUE = 43850
    ATTACK_BONUS = 2631
    DEFENSE_BONUS = 1754
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 877."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_877.ITEM_ID, "name": ItemDefinition_877.NAME, "atk": ItemDefinition_877.ATTACK_BONUS, "def": ItemDefinition_877.DEFENSE_BONUS}


class ItemDefinition_878:
    ITEM_ID = "item_878"
    NAME = "Hyperion Legendary Artifact #878"
    TYPE = "Weapon" if 878 % 2 == 0 else "Armor"
    RARITY = "Epic" if 878 % 5 == 0 else "Legendary"
    BASE_VALUE = 43900
    ATTACK_BONUS = 2634
    DEFENSE_BONUS = 1756
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 878."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_878.ITEM_ID, "name": ItemDefinition_878.NAME, "atk": ItemDefinition_878.ATTACK_BONUS, "def": ItemDefinition_878.DEFENSE_BONUS}


class ItemDefinition_879:
    ITEM_ID = "item_879"
    NAME = "Hyperion Legendary Artifact #879"
    TYPE = "Weapon" if 879 % 2 == 0 else "Armor"
    RARITY = "Epic" if 879 % 5 == 0 else "Legendary"
    BASE_VALUE = 43950
    ATTACK_BONUS = 2637
    DEFENSE_BONUS = 1758
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 879."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_879.ITEM_ID, "name": ItemDefinition_879.NAME, "atk": ItemDefinition_879.ATTACK_BONUS, "def": ItemDefinition_879.DEFENSE_BONUS}


class ItemDefinition_880:
    ITEM_ID = "item_880"
    NAME = "Hyperion Legendary Artifact #880"
    TYPE = "Weapon" if 880 % 2 == 0 else "Armor"
    RARITY = "Epic" if 880 % 5 == 0 else "Legendary"
    BASE_VALUE = 44000
    ATTACK_BONUS = 2640
    DEFENSE_BONUS = 1760
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 880."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_880.ITEM_ID, "name": ItemDefinition_880.NAME, "atk": ItemDefinition_880.ATTACK_BONUS, "def": ItemDefinition_880.DEFENSE_BONUS}


class ItemDefinition_881:
    ITEM_ID = "item_881"
    NAME = "Hyperion Legendary Artifact #881"
    TYPE = "Weapon" if 881 % 2 == 0 else "Armor"
    RARITY = "Epic" if 881 % 5 == 0 else "Legendary"
    BASE_VALUE = 44050
    ATTACK_BONUS = 2643
    DEFENSE_BONUS = 1762
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 881."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_881.ITEM_ID, "name": ItemDefinition_881.NAME, "atk": ItemDefinition_881.ATTACK_BONUS, "def": ItemDefinition_881.DEFENSE_BONUS}


class ItemDefinition_882:
    ITEM_ID = "item_882"
    NAME = "Hyperion Legendary Artifact #882"
    TYPE = "Weapon" if 882 % 2 == 0 else "Armor"
    RARITY = "Epic" if 882 % 5 == 0 else "Legendary"
    BASE_VALUE = 44100
    ATTACK_BONUS = 2646
    DEFENSE_BONUS = 1764
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 882."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_882.ITEM_ID, "name": ItemDefinition_882.NAME, "atk": ItemDefinition_882.ATTACK_BONUS, "def": ItemDefinition_882.DEFENSE_BONUS}


class ItemDefinition_883:
    ITEM_ID = "item_883"
    NAME = "Hyperion Legendary Artifact #883"
    TYPE = "Weapon" if 883 % 2 == 0 else "Armor"
    RARITY = "Epic" if 883 % 5 == 0 else "Legendary"
    BASE_VALUE = 44150
    ATTACK_BONUS = 2649
    DEFENSE_BONUS = 1766
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 883."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_883.ITEM_ID, "name": ItemDefinition_883.NAME, "atk": ItemDefinition_883.ATTACK_BONUS, "def": ItemDefinition_883.DEFENSE_BONUS}


class ItemDefinition_884:
    ITEM_ID = "item_884"
    NAME = "Hyperion Legendary Artifact #884"
    TYPE = "Weapon" if 884 % 2 == 0 else "Armor"
    RARITY = "Epic" if 884 % 5 == 0 else "Legendary"
    BASE_VALUE = 44200
    ATTACK_BONUS = 2652
    DEFENSE_BONUS = 1768
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 884."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_884.ITEM_ID, "name": ItemDefinition_884.NAME, "atk": ItemDefinition_884.ATTACK_BONUS, "def": ItemDefinition_884.DEFENSE_BONUS}


class ItemDefinition_885:
    ITEM_ID = "item_885"
    NAME = "Hyperion Legendary Artifact #885"
    TYPE = "Weapon" if 885 % 2 == 0 else "Armor"
    RARITY = "Epic" if 885 % 5 == 0 else "Legendary"
    BASE_VALUE = 44250
    ATTACK_BONUS = 2655
    DEFENSE_BONUS = 1770
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 885."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_885.ITEM_ID, "name": ItemDefinition_885.NAME, "atk": ItemDefinition_885.ATTACK_BONUS, "def": ItemDefinition_885.DEFENSE_BONUS}


class ItemDefinition_886:
    ITEM_ID = "item_886"
    NAME = "Hyperion Legendary Artifact #886"
    TYPE = "Weapon" if 886 % 2 == 0 else "Armor"
    RARITY = "Epic" if 886 % 5 == 0 else "Legendary"
    BASE_VALUE = 44300
    ATTACK_BONUS = 2658
    DEFENSE_BONUS = 1772
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 886."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_886.ITEM_ID, "name": ItemDefinition_886.NAME, "atk": ItemDefinition_886.ATTACK_BONUS, "def": ItemDefinition_886.DEFENSE_BONUS}


class ItemDefinition_887:
    ITEM_ID = "item_887"
    NAME = "Hyperion Legendary Artifact #887"
    TYPE = "Weapon" if 887 % 2 == 0 else "Armor"
    RARITY = "Epic" if 887 % 5 == 0 else "Legendary"
    BASE_VALUE = 44350
    ATTACK_BONUS = 2661
    DEFENSE_BONUS = 1774
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 887."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_887.ITEM_ID, "name": ItemDefinition_887.NAME, "atk": ItemDefinition_887.ATTACK_BONUS, "def": ItemDefinition_887.DEFENSE_BONUS}


class ItemDefinition_888:
    ITEM_ID = "item_888"
    NAME = "Hyperion Legendary Artifact #888"
    TYPE = "Weapon" if 888 % 2 == 0 else "Armor"
    RARITY = "Epic" if 888 % 5 == 0 else "Legendary"
    BASE_VALUE = 44400
    ATTACK_BONUS = 2664
    DEFENSE_BONUS = 1776
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 888."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_888.ITEM_ID, "name": ItemDefinition_888.NAME, "atk": ItemDefinition_888.ATTACK_BONUS, "def": ItemDefinition_888.DEFENSE_BONUS}


class ItemDefinition_889:
    ITEM_ID = "item_889"
    NAME = "Hyperion Legendary Artifact #889"
    TYPE = "Weapon" if 889 % 2 == 0 else "Armor"
    RARITY = "Epic" if 889 % 5 == 0 else "Legendary"
    BASE_VALUE = 44450
    ATTACK_BONUS = 2667
    DEFENSE_BONUS = 1778
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 889."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_889.ITEM_ID, "name": ItemDefinition_889.NAME, "atk": ItemDefinition_889.ATTACK_BONUS, "def": ItemDefinition_889.DEFENSE_BONUS}


class ItemDefinition_890:
    ITEM_ID = "item_890"
    NAME = "Hyperion Legendary Artifact #890"
    TYPE = "Weapon" if 890 % 2 == 0 else "Armor"
    RARITY = "Epic" if 890 % 5 == 0 else "Legendary"
    BASE_VALUE = 44500
    ATTACK_BONUS = 2670
    DEFENSE_BONUS = 1780
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 890."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_890.ITEM_ID, "name": ItemDefinition_890.NAME, "atk": ItemDefinition_890.ATTACK_BONUS, "def": ItemDefinition_890.DEFENSE_BONUS}


class ItemDefinition_891:
    ITEM_ID = "item_891"
    NAME = "Hyperion Legendary Artifact #891"
    TYPE = "Weapon" if 891 % 2 == 0 else "Armor"
    RARITY = "Epic" if 891 % 5 == 0 else "Legendary"
    BASE_VALUE = 44550
    ATTACK_BONUS = 2673
    DEFENSE_BONUS = 1782
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 891."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_891.ITEM_ID, "name": ItemDefinition_891.NAME, "atk": ItemDefinition_891.ATTACK_BONUS, "def": ItemDefinition_891.DEFENSE_BONUS}


class ItemDefinition_892:
    ITEM_ID = "item_892"
    NAME = "Hyperion Legendary Artifact #892"
    TYPE = "Weapon" if 892 % 2 == 0 else "Armor"
    RARITY = "Epic" if 892 % 5 == 0 else "Legendary"
    BASE_VALUE = 44600
    ATTACK_BONUS = 2676
    DEFENSE_BONUS = 1784
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 892."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_892.ITEM_ID, "name": ItemDefinition_892.NAME, "atk": ItemDefinition_892.ATTACK_BONUS, "def": ItemDefinition_892.DEFENSE_BONUS}


class ItemDefinition_893:
    ITEM_ID = "item_893"
    NAME = "Hyperion Legendary Artifact #893"
    TYPE = "Weapon" if 893 % 2 == 0 else "Armor"
    RARITY = "Epic" if 893 % 5 == 0 else "Legendary"
    BASE_VALUE = 44650
    ATTACK_BONUS = 2679
    DEFENSE_BONUS = 1786
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 893."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_893.ITEM_ID, "name": ItemDefinition_893.NAME, "atk": ItemDefinition_893.ATTACK_BONUS, "def": ItemDefinition_893.DEFENSE_BONUS}


class ItemDefinition_894:
    ITEM_ID = "item_894"
    NAME = "Hyperion Legendary Artifact #894"
    TYPE = "Weapon" if 894 % 2 == 0 else "Armor"
    RARITY = "Epic" if 894 % 5 == 0 else "Legendary"
    BASE_VALUE = 44700
    ATTACK_BONUS = 2682
    DEFENSE_BONUS = 1788
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 894."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_894.ITEM_ID, "name": ItemDefinition_894.NAME, "atk": ItemDefinition_894.ATTACK_BONUS, "def": ItemDefinition_894.DEFENSE_BONUS}


class ItemDefinition_895:
    ITEM_ID = "item_895"
    NAME = "Hyperion Legendary Artifact #895"
    TYPE = "Weapon" if 895 % 2 == 0 else "Armor"
    RARITY = "Epic" if 895 % 5 == 0 else "Legendary"
    BASE_VALUE = 44750
    ATTACK_BONUS = 2685
    DEFENSE_BONUS = 1790
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 895."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_895.ITEM_ID, "name": ItemDefinition_895.NAME, "atk": ItemDefinition_895.ATTACK_BONUS, "def": ItemDefinition_895.DEFENSE_BONUS}


class ItemDefinition_896:
    ITEM_ID = "item_896"
    NAME = "Hyperion Legendary Artifact #896"
    TYPE = "Weapon" if 896 % 2 == 0 else "Armor"
    RARITY = "Epic" if 896 % 5 == 0 else "Legendary"
    BASE_VALUE = 44800
    ATTACK_BONUS = 2688
    DEFENSE_BONUS = 1792
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 896."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_896.ITEM_ID, "name": ItemDefinition_896.NAME, "atk": ItemDefinition_896.ATTACK_BONUS, "def": ItemDefinition_896.DEFENSE_BONUS}


class ItemDefinition_897:
    ITEM_ID = "item_897"
    NAME = "Hyperion Legendary Artifact #897"
    TYPE = "Weapon" if 897 % 2 == 0 else "Armor"
    RARITY = "Epic" if 897 % 5 == 0 else "Legendary"
    BASE_VALUE = 44850
    ATTACK_BONUS = 2691
    DEFENSE_BONUS = 1794
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 897."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_897.ITEM_ID, "name": ItemDefinition_897.NAME, "atk": ItemDefinition_897.ATTACK_BONUS, "def": ItemDefinition_897.DEFENSE_BONUS}


class ItemDefinition_898:
    ITEM_ID = "item_898"
    NAME = "Hyperion Legendary Artifact #898"
    TYPE = "Weapon" if 898 % 2 == 0 else "Armor"
    RARITY = "Epic" if 898 % 5 == 0 else "Legendary"
    BASE_VALUE = 44900
    ATTACK_BONUS = 2694
    DEFENSE_BONUS = 1796
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 898."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_898.ITEM_ID, "name": ItemDefinition_898.NAME, "atk": ItemDefinition_898.ATTACK_BONUS, "def": ItemDefinition_898.DEFENSE_BONUS}


class ItemDefinition_899:
    ITEM_ID = "item_899"
    NAME = "Hyperion Legendary Artifact #899"
    TYPE = "Weapon" if 899 % 2 == 0 else "Armor"
    RARITY = "Epic" if 899 % 5 == 0 else "Legendary"
    BASE_VALUE = 44950
    ATTACK_BONUS = 2697
    DEFENSE_BONUS = 1798
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 899."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_899.ITEM_ID, "name": ItemDefinition_899.NAME, "atk": ItemDefinition_899.ATTACK_BONUS, "def": ItemDefinition_899.DEFENSE_BONUS}


class ItemDefinition_900:
    ITEM_ID = "item_900"
    NAME = "Hyperion Legendary Artifact #900"
    TYPE = "Weapon" if 900 % 2 == 0 else "Armor"
    RARITY = "Epic" if 900 % 5 == 0 else "Legendary"
    BASE_VALUE = 45000
    ATTACK_BONUS = 2700
    DEFENSE_BONUS = 1800
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 900."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_900.ITEM_ID, "name": ItemDefinition_900.NAME, "atk": ItemDefinition_900.ATTACK_BONUS, "def": ItemDefinition_900.DEFENSE_BONUS}


class ItemDefinition_901:
    ITEM_ID = "item_901"
    NAME = "Hyperion Legendary Artifact #901"
    TYPE = "Weapon" if 901 % 2 == 0 else "Armor"
    RARITY = "Epic" if 901 % 5 == 0 else "Legendary"
    BASE_VALUE = 45050
    ATTACK_BONUS = 2703
    DEFENSE_BONUS = 1802
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 901."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_901.ITEM_ID, "name": ItemDefinition_901.NAME, "atk": ItemDefinition_901.ATTACK_BONUS, "def": ItemDefinition_901.DEFENSE_BONUS}


class ItemDefinition_902:
    ITEM_ID = "item_902"
    NAME = "Hyperion Legendary Artifact #902"
    TYPE = "Weapon" if 902 % 2 == 0 else "Armor"
    RARITY = "Epic" if 902 % 5 == 0 else "Legendary"
    BASE_VALUE = 45100
    ATTACK_BONUS = 2706
    DEFENSE_BONUS = 1804
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 902."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_902.ITEM_ID, "name": ItemDefinition_902.NAME, "atk": ItemDefinition_902.ATTACK_BONUS, "def": ItemDefinition_902.DEFENSE_BONUS}


class ItemDefinition_903:
    ITEM_ID = "item_903"
    NAME = "Hyperion Legendary Artifact #903"
    TYPE = "Weapon" if 903 % 2 == 0 else "Armor"
    RARITY = "Epic" if 903 % 5 == 0 else "Legendary"
    BASE_VALUE = 45150
    ATTACK_BONUS = 2709
    DEFENSE_BONUS = 1806
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 903."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_903.ITEM_ID, "name": ItemDefinition_903.NAME, "atk": ItemDefinition_903.ATTACK_BONUS, "def": ItemDefinition_903.DEFENSE_BONUS}


class ItemDefinition_904:
    ITEM_ID = "item_904"
    NAME = "Hyperion Legendary Artifact #904"
    TYPE = "Weapon" if 904 % 2 == 0 else "Armor"
    RARITY = "Epic" if 904 % 5 == 0 else "Legendary"
    BASE_VALUE = 45200
    ATTACK_BONUS = 2712
    DEFENSE_BONUS = 1808
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 904."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_904.ITEM_ID, "name": ItemDefinition_904.NAME, "atk": ItemDefinition_904.ATTACK_BONUS, "def": ItemDefinition_904.DEFENSE_BONUS}


class ItemDefinition_905:
    ITEM_ID = "item_905"
    NAME = "Hyperion Legendary Artifact #905"
    TYPE = "Weapon" if 905 % 2 == 0 else "Armor"
    RARITY = "Epic" if 905 % 5 == 0 else "Legendary"
    BASE_VALUE = 45250
    ATTACK_BONUS = 2715
    DEFENSE_BONUS = 1810
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 905."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_905.ITEM_ID, "name": ItemDefinition_905.NAME, "atk": ItemDefinition_905.ATTACK_BONUS, "def": ItemDefinition_905.DEFENSE_BONUS}


class ItemDefinition_906:
    ITEM_ID = "item_906"
    NAME = "Hyperion Legendary Artifact #906"
    TYPE = "Weapon" if 906 % 2 == 0 else "Armor"
    RARITY = "Epic" if 906 % 5 == 0 else "Legendary"
    BASE_VALUE = 45300
    ATTACK_BONUS = 2718
    DEFENSE_BONUS = 1812
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 906."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_906.ITEM_ID, "name": ItemDefinition_906.NAME, "atk": ItemDefinition_906.ATTACK_BONUS, "def": ItemDefinition_906.DEFENSE_BONUS}


class ItemDefinition_907:
    ITEM_ID = "item_907"
    NAME = "Hyperion Legendary Artifact #907"
    TYPE = "Weapon" if 907 % 2 == 0 else "Armor"
    RARITY = "Epic" if 907 % 5 == 0 else "Legendary"
    BASE_VALUE = 45350
    ATTACK_BONUS = 2721
    DEFENSE_BONUS = 1814
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 907."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_907.ITEM_ID, "name": ItemDefinition_907.NAME, "atk": ItemDefinition_907.ATTACK_BONUS, "def": ItemDefinition_907.DEFENSE_BONUS}


class ItemDefinition_908:
    ITEM_ID = "item_908"
    NAME = "Hyperion Legendary Artifact #908"
    TYPE = "Weapon" if 908 % 2 == 0 else "Armor"
    RARITY = "Epic" if 908 % 5 == 0 else "Legendary"
    BASE_VALUE = 45400
    ATTACK_BONUS = 2724
    DEFENSE_BONUS = 1816
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 908."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_908.ITEM_ID, "name": ItemDefinition_908.NAME, "atk": ItemDefinition_908.ATTACK_BONUS, "def": ItemDefinition_908.DEFENSE_BONUS}


class ItemDefinition_909:
    ITEM_ID = "item_909"
    NAME = "Hyperion Legendary Artifact #909"
    TYPE = "Weapon" if 909 % 2 == 0 else "Armor"
    RARITY = "Epic" if 909 % 5 == 0 else "Legendary"
    BASE_VALUE = 45450
    ATTACK_BONUS = 2727
    DEFENSE_BONUS = 1818
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 909."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_909.ITEM_ID, "name": ItemDefinition_909.NAME, "atk": ItemDefinition_909.ATTACK_BONUS, "def": ItemDefinition_909.DEFENSE_BONUS}


class ItemDefinition_910:
    ITEM_ID = "item_910"
    NAME = "Hyperion Legendary Artifact #910"
    TYPE = "Weapon" if 910 % 2 == 0 else "Armor"
    RARITY = "Epic" if 910 % 5 == 0 else "Legendary"
    BASE_VALUE = 45500
    ATTACK_BONUS = 2730
    DEFENSE_BONUS = 1820
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 910."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_910.ITEM_ID, "name": ItemDefinition_910.NAME, "atk": ItemDefinition_910.ATTACK_BONUS, "def": ItemDefinition_910.DEFENSE_BONUS}


class ItemDefinition_911:
    ITEM_ID = "item_911"
    NAME = "Hyperion Legendary Artifact #911"
    TYPE = "Weapon" if 911 % 2 == 0 else "Armor"
    RARITY = "Epic" if 911 % 5 == 0 else "Legendary"
    BASE_VALUE = 45550
    ATTACK_BONUS = 2733
    DEFENSE_BONUS = 1822
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 911."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_911.ITEM_ID, "name": ItemDefinition_911.NAME, "atk": ItemDefinition_911.ATTACK_BONUS, "def": ItemDefinition_911.DEFENSE_BONUS}


class ItemDefinition_912:
    ITEM_ID = "item_912"
    NAME = "Hyperion Legendary Artifact #912"
    TYPE = "Weapon" if 912 % 2 == 0 else "Armor"
    RARITY = "Epic" if 912 % 5 == 0 else "Legendary"
    BASE_VALUE = 45600
    ATTACK_BONUS = 2736
    DEFENSE_BONUS = 1824
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 912."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_912.ITEM_ID, "name": ItemDefinition_912.NAME, "atk": ItemDefinition_912.ATTACK_BONUS, "def": ItemDefinition_912.DEFENSE_BONUS}


class ItemDefinition_913:
    ITEM_ID = "item_913"
    NAME = "Hyperion Legendary Artifact #913"
    TYPE = "Weapon" if 913 % 2 == 0 else "Armor"
    RARITY = "Epic" if 913 % 5 == 0 else "Legendary"
    BASE_VALUE = 45650
    ATTACK_BONUS = 2739
    DEFENSE_BONUS = 1826
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 913."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_913.ITEM_ID, "name": ItemDefinition_913.NAME, "atk": ItemDefinition_913.ATTACK_BONUS, "def": ItemDefinition_913.DEFENSE_BONUS}


class ItemDefinition_914:
    ITEM_ID = "item_914"
    NAME = "Hyperion Legendary Artifact #914"
    TYPE = "Weapon" if 914 % 2 == 0 else "Armor"
    RARITY = "Epic" if 914 % 5 == 0 else "Legendary"
    BASE_VALUE = 45700
    ATTACK_BONUS = 2742
    DEFENSE_BONUS = 1828
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 914."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_914.ITEM_ID, "name": ItemDefinition_914.NAME, "atk": ItemDefinition_914.ATTACK_BONUS, "def": ItemDefinition_914.DEFENSE_BONUS}


class ItemDefinition_915:
    ITEM_ID = "item_915"
    NAME = "Hyperion Legendary Artifact #915"
    TYPE = "Weapon" if 915 % 2 == 0 else "Armor"
    RARITY = "Epic" if 915 % 5 == 0 else "Legendary"
    BASE_VALUE = 45750
    ATTACK_BONUS = 2745
    DEFENSE_BONUS = 1830
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 915."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_915.ITEM_ID, "name": ItemDefinition_915.NAME, "atk": ItemDefinition_915.ATTACK_BONUS, "def": ItemDefinition_915.DEFENSE_BONUS}


class ItemDefinition_916:
    ITEM_ID = "item_916"
    NAME = "Hyperion Legendary Artifact #916"
    TYPE = "Weapon" if 916 % 2 == 0 else "Armor"
    RARITY = "Epic" if 916 % 5 == 0 else "Legendary"
    BASE_VALUE = 45800
    ATTACK_BONUS = 2748
    DEFENSE_BONUS = 1832
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 916."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_916.ITEM_ID, "name": ItemDefinition_916.NAME, "atk": ItemDefinition_916.ATTACK_BONUS, "def": ItemDefinition_916.DEFENSE_BONUS}


class ItemDefinition_917:
    ITEM_ID = "item_917"
    NAME = "Hyperion Legendary Artifact #917"
    TYPE = "Weapon" if 917 % 2 == 0 else "Armor"
    RARITY = "Epic" if 917 % 5 == 0 else "Legendary"
    BASE_VALUE = 45850
    ATTACK_BONUS = 2751
    DEFENSE_BONUS = 1834
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 917."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_917.ITEM_ID, "name": ItemDefinition_917.NAME, "atk": ItemDefinition_917.ATTACK_BONUS, "def": ItemDefinition_917.DEFENSE_BONUS}


class ItemDefinition_918:
    ITEM_ID = "item_918"
    NAME = "Hyperion Legendary Artifact #918"
    TYPE = "Weapon" if 918 % 2 == 0 else "Armor"
    RARITY = "Epic" if 918 % 5 == 0 else "Legendary"
    BASE_VALUE = 45900
    ATTACK_BONUS = 2754
    DEFENSE_BONUS = 1836
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 918."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_918.ITEM_ID, "name": ItemDefinition_918.NAME, "atk": ItemDefinition_918.ATTACK_BONUS, "def": ItemDefinition_918.DEFENSE_BONUS}


class ItemDefinition_919:
    ITEM_ID = "item_919"
    NAME = "Hyperion Legendary Artifact #919"
    TYPE = "Weapon" if 919 % 2 == 0 else "Armor"
    RARITY = "Epic" if 919 % 5 == 0 else "Legendary"
    BASE_VALUE = 45950
    ATTACK_BONUS = 2757
    DEFENSE_BONUS = 1838
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 919."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_919.ITEM_ID, "name": ItemDefinition_919.NAME, "atk": ItemDefinition_919.ATTACK_BONUS, "def": ItemDefinition_919.DEFENSE_BONUS}


class ItemDefinition_920:
    ITEM_ID = "item_920"
    NAME = "Hyperion Legendary Artifact #920"
    TYPE = "Weapon" if 920 % 2 == 0 else "Armor"
    RARITY = "Epic" if 920 % 5 == 0 else "Legendary"
    BASE_VALUE = 46000
    ATTACK_BONUS = 2760
    DEFENSE_BONUS = 1840
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 920."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_920.ITEM_ID, "name": ItemDefinition_920.NAME, "atk": ItemDefinition_920.ATTACK_BONUS, "def": ItemDefinition_920.DEFENSE_BONUS}


class ItemDefinition_921:
    ITEM_ID = "item_921"
    NAME = "Hyperion Legendary Artifact #921"
    TYPE = "Weapon" if 921 % 2 == 0 else "Armor"
    RARITY = "Epic" if 921 % 5 == 0 else "Legendary"
    BASE_VALUE = 46050
    ATTACK_BONUS = 2763
    DEFENSE_BONUS = 1842
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 921."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_921.ITEM_ID, "name": ItemDefinition_921.NAME, "atk": ItemDefinition_921.ATTACK_BONUS, "def": ItemDefinition_921.DEFENSE_BONUS}


class ItemDefinition_922:
    ITEM_ID = "item_922"
    NAME = "Hyperion Legendary Artifact #922"
    TYPE = "Weapon" if 922 % 2 == 0 else "Armor"
    RARITY = "Epic" if 922 % 5 == 0 else "Legendary"
    BASE_VALUE = 46100
    ATTACK_BONUS = 2766
    DEFENSE_BONUS = 1844
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 922."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_922.ITEM_ID, "name": ItemDefinition_922.NAME, "atk": ItemDefinition_922.ATTACK_BONUS, "def": ItemDefinition_922.DEFENSE_BONUS}


class ItemDefinition_923:
    ITEM_ID = "item_923"
    NAME = "Hyperion Legendary Artifact #923"
    TYPE = "Weapon" if 923 % 2 == 0 else "Armor"
    RARITY = "Epic" if 923 % 5 == 0 else "Legendary"
    BASE_VALUE = 46150
    ATTACK_BONUS = 2769
    DEFENSE_BONUS = 1846
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 923."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_923.ITEM_ID, "name": ItemDefinition_923.NAME, "atk": ItemDefinition_923.ATTACK_BONUS, "def": ItemDefinition_923.DEFENSE_BONUS}


class ItemDefinition_924:
    ITEM_ID = "item_924"
    NAME = "Hyperion Legendary Artifact #924"
    TYPE = "Weapon" if 924 % 2 == 0 else "Armor"
    RARITY = "Epic" if 924 % 5 == 0 else "Legendary"
    BASE_VALUE = 46200
    ATTACK_BONUS = 2772
    DEFENSE_BONUS = 1848
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 924."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_924.ITEM_ID, "name": ItemDefinition_924.NAME, "atk": ItemDefinition_924.ATTACK_BONUS, "def": ItemDefinition_924.DEFENSE_BONUS}


class ItemDefinition_925:
    ITEM_ID = "item_925"
    NAME = "Hyperion Legendary Artifact #925"
    TYPE = "Weapon" if 925 % 2 == 0 else "Armor"
    RARITY = "Epic" if 925 % 5 == 0 else "Legendary"
    BASE_VALUE = 46250
    ATTACK_BONUS = 2775
    DEFENSE_BONUS = 1850
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 925."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_925.ITEM_ID, "name": ItemDefinition_925.NAME, "atk": ItemDefinition_925.ATTACK_BONUS, "def": ItemDefinition_925.DEFENSE_BONUS}


class ItemDefinition_926:
    ITEM_ID = "item_926"
    NAME = "Hyperion Legendary Artifact #926"
    TYPE = "Weapon" if 926 % 2 == 0 else "Armor"
    RARITY = "Epic" if 926 % 5 == 0 else "Legendary"
    BASE_VALUE = 46300
    ATTACK_BONUS = 2778
    DEFENSE_BONUS = 1852
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 926."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_926.ITEM_ID, "name": ItemDefinition_926.NAME, "atk": ItemDefinition_926.ATTACK_BONUS, "def": ItemDefinition_926.DEFENSE_BONUS}


class ItemDefinition_927:
    ITEM_ID = "item_927"
    NAME = "Hyperion Legendary Artifact #927"
    TYPE = "Weapon" if 927 % 2 == 0 else "Armor"
    RARITY = "Epic" if 927 % 5 == 0 else "Legendary"
    BASE_VALUE = 46350
    ATTACK_BONUS = 2781
    DEFENSE_BONUS = 1854
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 927."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_927.ITEM_ID, "name": ItemDefinition_927.NAME, "atk": ItemDefinition_927.ATTACK_BONUS, "def": ItemDefinition_927.DEFENSE_BONUS}


class ItemDefinition_928:
    ITEM_ID = "item_928"
    NAME = "Hyperion Legendary Artifact #928"
    TYPE = "Weapon" if 928 % 2 == 0 else "Armor"
    RARITY = "Epic" if 928 % 5 == 0 else "Legendary"
    BASE_VALUE = 46400
    ATTACK_BONUS = 2784
    DEFENSE_BONUS = 1856
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 928."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_928.ITEM_ID, "name": ItemDefinition_928.NAME, "atk": ItemDefinition_928.ATTACK_BONUS, "def": ItemDefinition_928.DEFENSE_BONUS}


class ItemDefinition_929:
    ITEM_ID = "item_929"
    NAME = "Hyperion Legendary Artifact #929"
    TYPE = "Weapon" if 929 % 2 == 0 else "Armor"
    RARITY = "Epic" if 929 % 5 == 0 else "Legendary"
    BASE_VALUE = 46450
    ATTACK_BONUS = 2787
    DEFENSE_BONUS = 1858
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 929."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_929.ITEM_ID, "name": ItemDefinition_929.NAME, "atk": ItemDefinition_929.ATTACK_BONUS, "def": ItemDefinition_929.DEFENSE_BONUS}


class ItemDefinition_930:
    ITEM_ID = "item_930"
    NAME = "Hyperion Legendary Artifact #930"
    TYPE = "Weapon" if 930 % 2 == 0 else "Armor"
    RARITY = "Epic" if 930 % 5 == 0 else "Legendary"
    BASE_VALUE = 46500
    ATTACK_BONUS = 2790
    DEFENSE_BONUS = 1860
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 930."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_930.ITEM_ID, "name": ItemDefinition_930.NAME, "atk": ItemDefinition_930.ATTACK_BONUS, "def": ItemDefinition_930.DEFENSE_BONUS}


class ItemDefinition_931:
    ITEM_ID = "item_931"
    NAME = "Hyperion Legendary Artifact #931"
    TYPE = "Weapon" if 931 % 2 == 0 else "Armor"
    RARITY = "Epic" if 931 % 5 == 0 else "Legendary"
    BASE_VALUE = 46550
    ATTACK_BONUS = 2793
    DEFENSE_BONUS = 1862
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 931."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_931.ITEM_ID, "name": ItemDefinition_931.NAME, "atk": ItemDefinition_931.ATTACK_BONUS, "def": ItemDefinition_931.DEFENSE_BONUS}


class ItemDefinition_932:
    ITEM_ID = "item_932"
    NAME = "Hyperion Legendary Artifact #932"
    TYPE = "Weapon" if 932 % 2 == 0 else "Armor"
    RARITY = "Epic" if 932 % 5 == 0 else "Legendary"
    BASE_VALUE = 46600
    ATTACK_BONUS = 2796
    DEFENSE_BONUS = 1864
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 932."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_932.ITEM_ID, "name": ItemDefinition_932.NAME, "atk": ItemDefinition_932.ATTACK_BONUS, "def": ItemDefinition_932.DEFENSE_BONUS}


class ItemDefinition_933:
    ITEM_ID = "item_933"
    NAME = "Hyperion Legendary Artifact #933"
    TYPE = "Weapon" if 933 % 2 == 0 else "Armor"
    RARITY = "Epic" if 933 % 5 == 0 else "Legendary"
    BASE_VALUE = 46650
    ATTACK_BONUS = 2799
    DEFENSE_BONUS = 1866
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 933."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_933.ITEM_ID, "name": ItemDefinition_933.NAME, "atk": ItemDefinition_933.ATTACK_BONUS, "def": ItemDefinition_933.DEFENSE_BONUS}


class ItemDefinition_934:
    ITEM_ID = "item_934"
    NAME = "Hyperion Legendary Artifact #934"
    TYPE = "Weapon" if 934 % 2 == 0 else "Armor"
    RARITY = "Epic" if 934 % 5 == 0 else "Legendary"
    BASE_VALUE = 46700
    ATTACK_BONUS = 2802
    DEFENSE_BONUS = 1868
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 934."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_934.ITEM_ID, "name": ItemDefinition_934.NAME, "atk": ItemDefinition_934.ATTACK_BONUS, "def": ItemDefinition_934.DEFENSE_BONUS}


class ItemDefinition_935:
    ITEM_ID = "item_935"
    NAME = "Hyperion Legendary Artifact #935"
    TYPE = "Weapon" if 935 % 2 == 0 else "Armor"
    RARITY = "Epic" if 935 % 5 == 0 else "Legendary"
    BASE_VALUE = 46750
    ATTACK_BONUS = 2805
    DEFENSE_BONUS = 1870
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 935."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_935.ITEM_ID, "name": ItemDefinition_935.NAME, "atk": ItemDefinition_935.ATTACK_BONUS, "def": ItemDefinition_935.DEFENSE_BONUS}


class ItemDefinition_936:
    ITEM_ID = "item_936"
    NAME = "Hyperion Legendary Artifact #936"
    TYPE = "Weapon" if 936 % 2 == 0 else "Armor"
    RARITY = "Epic" if 936 % 5 == 0 else "Legendary"
    BASE_VALUE = 46800
    ATTACK_BONUS = 2808
    DEFENSE_BONUS = 1872
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 936."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_936.ITEM_ID, "name": ItemDefinition_936.NAME, "atk": ItemDefinition_936.ATTACK_BONUS, "def": ItemDefinition_936.DEFENSE_BONUS}


class ItemDefinition_937:
    ITEM_ID = "item_937"
    NAME = "Hyperion Legendary Artifact #937"
    TYPE = "Weapon" if 937 % 2 == 0 else "Armor"
    RARITY = "Epic" if 937 % 5 == 0 else "Legendary"
    BASE_VALUE = 46850
    ATTACK_BONUS = 2811
    DEFENSE_BONUS = 1874
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 937."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_937.ITEM_ID, "name": ItemDefinition_937.NAME, "atk": ItemDefinition_937.ATTACK_BONUS, "def": ItemDefinition_937.DEFENSE_BONUS}


class ItemDefinition_938:
    ITEM_ID = "item_938"
    NAME = "Hyperion Legendary Artifact #938"
    TYPE = "Weapon" if 938 % 2 == 0 else "Armor"
    RARITY = "Epic" if 938 % 5 == 0 else "Legendary"
    BASE_VALUE = 46900
    ATTACK_BONUS = 2814
    DEFENSE_BONUS = 1876
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 938."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_938.ITEM_ID, "name": ItemDefinition_938.NAME, "atk": ItemDefinition_938.ATTACK_BONUS, "def": ItemDefinition_938.DEFENSE_BONUS}


class ItemDefinition_939:
    ITEM_ID = "item_939"
    NAME = "Hyperion Legendary Artifact #939"
    TYPE = "Weapon" if 939 % 2 == 0 else "Armor"
    RARITY = "Epic" if 939 % 5 == 0 else "Legendary"
    BASE_VALUE = 46950
    ATTACK_BONUS = 2817
    DEFENSE_BONUS = 1878
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 939."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_939.ITEM_ID, "name": ItemDefinition_939.NAME, "atk": ItemDefinition_939.ATTACK_BONUS, "def": ItemDefinition_939.DEFENSE_BONUS}


class ItemDefinition_940:
    ITEM_ID = "item_940"
    NAME = "Hyperion Legendary Artifact #940"
    TYPE = "Weapon" if 940 % 2 == 0 else "Armor"
    RARITY = "Epic" if 940 % 5 == 0 else "Legendary"
    BASE_VALUE = 47000
    ATTACK_BONUS = 2820
    DEFENSE_BONUS = 1880
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 940."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_940.ITEM_ID, "name": ItemDefinition_940.NAME, "atk": ItemDefinition_940.ATTACK_BONUS, "def": ItemDefinition_940.DEFENSE_BONUS}


class ItemDefinition_941:
    ITEM_ID = "item_941"
    NAME = "Hyperion Legendary Artifact #941"
    TYPE = "Weapon" if 941 % 2 == 0 else "Armor"
    RARITY = "Epic" if 941 % 5 == 0 else "Legendary"
    BASE_VALUE = 47050
    ATTACK_BONUS = 2823
    DEFENSE_BONUS = 1882
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 941."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_941.ITEM_ID, "name": ItemDefinition_941.NAME, "atk": ItemDefinition_941.ATTACK_BONUS, "def": ItemDefinition_941.DEFENSE_BONUS}


class ItemDefinition_942:
    ITEM_ID = "item_942"
    NAME = "Hyperion Legendary Artifact #942"
    TYPE = "Weapon" if 942 % 2 == 0 else "Armor"
    RARITY = "Epic" if 942 % 5 == 0 else "Legendary"
    BASE_VALUE = 47100
    ATTACK_BONUS = 2826
    DEFENSE_BONUS = 1884
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 942."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_942.ITEM_ID, "name": ItemDefinition_942.NAME, "atk": ItemDefinition_942.ATTACK_BONUS, "def": ItemDefinition_942.DEFENSE_BONUS}


class ItemDefinition_943:
    ITEM_ID = "item_943"
    NAME = "Hyperion Legendary Artifact #943"
    TYPE = "Weapon" if 943 % 2 == 0 else "Armor"
    RARITY = "Epic" if 943 % 5 == 0 else "Legendary"
    BASE_VALUE = 47150
    ATTACK_BONUS = 2829
    DEFENSE_BONUS = 1886
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 943."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_943.ITEM_ID, "name": ItemDefinition_943.NAME, "atk": ItemDefinition_943.ATTACK_BONUS, "def": ItemDefinition_943.DEFENSE_BONUS}


class ItemDefinition_944:
    ITEM_ID = "item_944"
    NAME = "Hyperion Legendary Artifact #944"
    TYPE = "Weapon" if 944 % 2 == 0 else "Armor"
    RARITY = "Epic" if 944 % 5 == 0 else "Legendary"
    BASE_VALUE = 47200
    ATTACK_BONUS = 2832
    DEFENSE_BONUS = 1888
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 944."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_944.ITEM_ID, "name": ItemDefinition_944.NAME, "atk": ItemDefinition_944.ATTACK_BONUS, "def": ItemDefinition_944.DEFENSE_BONUS}


class ItemDefinition_945:
    ITEM_ID = "item_945"
    NAME = "Hyperion Legendary Artifact #945"
    TYPE = "Weapon" if 945 % 2 == 0 else "Armor"
    RARITY = "Epic" if 945 % 5 == 0 else "Legendary"
    BASE_VALUE = 47250
    ATTACK_BONUS = 2835
    DEFENSE_BONUS = 1890
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 945."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_945.ITEM_ID, "name": ItemDefinition_945.NAME, "atk": ItemDefinition_945.ATTACK_BONUS, "def": ItemDefinition_945.DEFENSE_BONUS}


class ItemDefinition_946:
    ITEM_ID = "item_946"
    NAME = "Hyperion Legendary Artifact #946"
    TYPE = "Weapon" if 946 % 2 == 0 else "Armor"
    RARITY = "Epic" if 946 % 5 == 0 else "Legendary"
    BASE_VALUE = 47300
    ATTACK_BONUS = 2838
    DEFENSE_BONUS = 1892
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 946."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_946.ITEM_ID, "name": ItemDefinition_946.NAME, "atk": ItemDefinition_946.ATTACK_BONUS, "def": ItemDefinition_946.DEFENSE_BONUS}


class ItemDefinition_947:
    ITEM_ID = "item_947"
    NAME = "Hyperion Legendary Artifact #947"
    TYPE = "Weapon" if 947 % 2 == 0 else "Armor"
    RARITY = "Epic" if 947 % 5 == 0 else "Legendary"
    BASE_VALUE = 47350
    ATTACK_BONUS = 2841
    DEFENSE_BONUS = 1894
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 947."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_947.ITEM_ID, "name": ItemDefinition_947.NAME, "atk": ItemDefinition_947.ATTACK_BONUS, "def": ItemDefinition_947.DEFENSE_BONUS}


class ItemDefinition_948:
    ITEM_ID = "item_948"
    NAME = "Hyperion Legendary Artifact #948"
    TYPE = "Weapon" if 948 % 2 == 0 else "Armor"
    RARITY = "Epic" if 948 % 5 == 0 else "Legendary"
    BASE_VALUE = 47400
    ATTACK_BONUS = 2844
    DEFENSE_BONUS = 1896
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 948."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_948.ITEM_ID, "name": ItemDefinition_948.NAME, "atk": ItemDefinition_948.ATTACK_BONUS, "def": ItemDefinition_948.DEFENSE_BONUS}


class ItemDefinition_949:
    ITEM_ID = "item_949"
    NAME = "Hyperion Legendary Artifact #949"
    TYPE = "Weapon" if 949 % 2 == 0 else "Armor"
    RARITY = "Epic" if 949 % 5 == 0 else "Legendary"
    BASE_VALUE = 47450
    ATTACK_BONUS = 2847
    DEFENSE_BONUS = 1898
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 949."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_949.ITEM_ID, "name": ItemDefinition_949.NAME, "atk": ItemDefinition_949.ATTACK_BONUS, "def": ItemDefinition_949.DEFENSE_BONUS}


class ItemDefinition_950:
    ITEM_ID = "item_950"
    NAME = "Hyperion Legendary Artifact #950"
    TYPE = "Weapon" if 950 % 2 == 0 else "Armor"
    RARITY = "Epic" if 950 % 5 == 0 else "Legendary"
    BASE_VALUE = 47500
    ATTACK_BONUS = 2850
    DEFENSE_BONUS = 1900
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 950."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_950.ITEM_ID, "name": ItemDefinition_950.NAME, "atk": ItemDefinition_950.ATTACK_BONUS, "def": ItemDefinition_950.DEFENSE_BONUS}


class ItemDefinition_951:
    ITEM_ID = "item_951"
    NAME = "Hyperion Legendary Artifact #951"
    TYPE = "Weapon" if 951 % 2 == 0 else "Armor"
    RARITY = "Epic" if 951 % 5 == 0 else "Legendary"
    BASE_VALUE = 47550
    ATTACK_BONUS = 2853
    DEFENSE_BONUS = 1902
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 951."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_951.ITEM_ID, "name": ItemDefinition_951.NAME, "atk": ItemDefinition_951.ATTACK_BONUS, "def": ItemDefinition_951.DEFENSE_BONUS}


class ItemDefinition_952:
    ITEM_ID = "item_952"
    NAME = "Hyperion Legendary Artifact #952"
    TYPE = "Weapon" if 952 % 2 == 0 else "Armor"
    RARITY = "Epic" if 952 % 5 == 0 else "Legendary"
    BASE_VALUE = 47600
    ATTACK_BONUS = 2856
    DEFENSE_BONUS = 1904
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 952."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_952.ITEM_ID, "name": ItemDefinition_952.NAME, "atk": ItemDefinition_952.ATTACK_BONUS, "def": ItemDefinition_952.DEFENSE_BONUS}


class ItemDefinition_953:
    ITEM_ID = "item_953"
    NAME = "Hyperion Legendary Artifact #953"
    TYPE = "Weapon" if 953 % 2 == 0 else "Armor"
    RARITY = "Epic" if 953 % 5 == 0 else "Legendary"
    BASE_VALUE = 47650
    ATTACK_BONUS = 2859
    DEFENSE_BONUS = 1906
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 953."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_953.ITEM_ID, "name": ItemDefinition_953.NAME, "atk": ItemDefinition_953.ATTACK_BONUS, "def": ItemDefinition_953.DEFENSE_BONUS}


class ItemDefinition_954:
    ITEM_ID = "item_954"
    NAME = "Hyperion Legendary Artifact #954"
    TYPE = "Weapon" if 954 % 2 == 0 else "Armor"
    RARITY = "Epic" if 954 % 5 == 0 else "Legendary"
    BASE_VALUE = 47700
    ATTACK_BONUS = 2862
    DEFENSE_BONUS = 1908
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 954."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_954.ITEM_ID, "name": ItemDefinition_954.NAME, "atk": ItemDefinition_954.ATTACK_BONUS, "def": ItemDefinition_954.DEFENSE_BONUS}


class ItemDefinition_955:
    ITEM_ID = "item_955"
    NAME = "Hyperion Legendary Artifact #955"
    TYPE = "Weapon" if 955 % 2 == 0 else "Armor"
    RARITY = "Epic" if 955 % 5 == 0 else "Legendary"
    BASE_VALUE = 47750
    ATTACK_BONUS = 2865
    DEFENSE_BONUS = 1910
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 955."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_955.ITEM_ID, "name": ItemDefinition_955.NAME, "atk": ItemDefinition_955.ATTACK_BONUS, "def": ItemDefinition_955.DEFENSE_BONUS}


class ItemDefinition_956:
    ITEM_ID = "item_956"
    NAME = "Hyperion Legendary Artifact #956"
    TYPE = "Weapon" if 956 % 2 == 0 else "Armor"
    RARITY = "Epic" if 956 % 5 == 0 else "Legendary"
    BASE_VALUE = 47800
    ATTACK_BONUS = 2868
    DEFENSE_BONUS = 1912
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 956."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_956.ITEM_ID, "name": ItemDefinition_956.NAME, "atk": ItemDefinition_956.ATTACK_BONUS, "def": ItemDefinition_956.DEFENSE_BONUS}


class ItemDefinition_957:
    ITEM_ID = "item_957"
    NAME = "Hyperion Legendary Artifact #957"
    TYPE = "Weapon" if 957 % 2 == 0 else "Armor"
    RARITY = "Epic" if 957 % 5 == 0 else "Legendary"
    BASE_VALUE = 47850
    ATTACK_BONUS = 2871
    DEFENSE_BONUS = 1914
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 957."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_957.ITEM_ID, "name": ItemDefinition_957.NAME, "atk": ItemDefinition_957.ATTACK_BONUS, "def": ItemDefinition_957.DEFENSE_BONUS}


class ItemDefinition_958:
    ITEM_ID = "item_958"
    NAME = "Hyperion Legendary Artifact #958"
    TYPE = "Weapon" if 958 % 2 == 0 else "Armor"
    RARITY = "Epic" if 958 % 5 == 0 else "Legendary"
    BASE_VALUE = 47900
    ATTACK_BONUS = 2874
    DEFENSE_BONUS = 1916
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 958."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_958.ITEM_ID, "name": ItemDefinition_958.NAME, "atk": ItemDefinition_958.ATTACK_BONUS, "def": ItemDefinition_958.DEFENSE_BONUS}


class ItemDefinition_959:
    ITEM_ID = "item_959"
    NAME = "Hyperion Legendary Artifact #959"
    TYPE = "Weapon" if 959 % 2 == 0 else "Armor"
    RARITY = "Epic" if 959 % 5 == 0 else "Legendary"
    BASE_VALUE = 47950
    ATTACK_BONUS = 2877
    DEFENSE_BONUS = 1918
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 959."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_959.ITEM_ID, "name": ItemDefinition_959.NAME, "atk": ItemDefinition_959.ATTACK_BONUS, "def": ItemDefinition_959.DEFENSE_BONUS}


class ItemDefinition_960:
    ITEM_ID = "item_960"
    NAME = "Hyperion Legendary Artifact #960"
    TYPE = "Weapon" if 960 % 2 == 0 else "Armor"
    RARITY = "Epic" if 960 % 5 == 0 else "Legendary"
    BASE_VALUE = 48000
    ATTACK_BONUS = 2880
    DEFENSE_BONUS = 1920
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 960."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_960.ITEM_ID, "name": ItemDefinition_960.NAME, "atk": ItemDefinition_960.ATTACK_BONUS, "def": ItemDefinition_960.DEFENSE_BONUS}


class ItemDefinition_961:
    ITEM_ID = "item_961"
    NAME = "Hyperion Legendary Artifact #961"
    TYPE = "Weapon" if 961 % 2 == 0 else "Armor"
    RARITY = "Epic" if 961 % 5 == 0 else "Legendary"
    BASE_VALUE = 48050
    ATTACK_BONUS = 2883
    DEFENSE_BONUS = 1922
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 961."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_961.ITEM_ID, "name": ItemDefinition_961.NAME, "atk": ItemDefinition_961.ATTACK_BONUS, "def": ItemDefinition_961.DEFENSE_BONUS}


class ItemDefinition_962:
    ITEM_ID = "item_962"
    NAME = "Hyperion Legendary Artifact #962"
    TYPE = "Weapon" if 962 % 2 == 0 else "Armor"
    RARITY = "Epic" if 962 % 5 == 0 else "Legendary"
    BASE_VALUE = 48100
    ATTACK_BONUS = 2886
    DEFENSE_BONUS = 1924
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 962."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_962.ITEM_ID, "name": ItemDefinition_962.NAME, "atk": ItemDefinition_962.ATTACK_BONUS, "def": ItemDefinition_962.DEFENSE_BONUS}


class ItemDefinition_963:
    ITEM_ID = "item_963"
    NAME = "Hyperion Legendary Artifact #963"
    TYPE = "Weapon" if 963 % 2 == 0 else "Armor"
    RARITY = "Epic" if 963 % 5 == 0 else "Legendary"
    BASE_VALUE = 48150
    ATTACK_BONUS = 2889
    DEFENSE_BONUS = 1926
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 963."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_963.ITEM_ID, "name": ItemDefinition_963.NAME, "atk": ItemDefinition_963.ATTACK_BONUS, "def": ItemDefinition_963.DEFENSE_BONUS}


class ItemDefinition_964:
    ITEM_ID = "item_964"
    NAME = "Hyperion Legendary Artifact #964"
    TYPE = "Weapon" if 964 % 2 == 0 else "Armor"
    RARITY = "Epic" if 964 % 5 == 0 else "Legendary"
    BASE_VALUE = 48200
    ATTACK_BONUS = 2892
    DEFENSE_BONUS = 1928
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 964."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_964.ITEM_ID, "name": ItemDefinition_964.NAME, "atk": ItemDefinition_964.ATTACK_BONUS, "def": ItemDefinition_964.DEFENSE_BONUS}


class ItemDefinition_965:
    ITEM_ID = "item_965"
    NAME = "Hyperion Legendary Artifact #965"
    TYPE = "Weapon" if 965 % 2 == 0 else "Armor"
    RARITY = "Epic" if 965 % 5 == 0 else "Legendary"
    BASE_VALUE = 48250
    ATTACK_BONUS = 2895
    DEFENSE_BONUS = 1930
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 965."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_965.ITEM_ID, "name": ItemDefinition_965.NAME, "atk": ItemDefinition_965.ATTACK_BONUS, "def": ItemDefinition_965.DEFENSE_BONUS}


class ItemDefinition_966:
    ITEM_ID = "item_966"
    NAME = "Hyperion Legendary Artifact #966"
    TYPE = "Weapon" if 966 % 2 == 0 else "Armor"
    RARITY = "Epic" if 966 % 5 == 0 else "Legendary"
    BASE_VALUE = 48300
    ATTACK_BONUS = 2898
    DEFENSE_BONUS = 1932
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 966."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_966.ITEM_ID, "name": ItemDefinition_966.NAME, "atk": ItemDefinition_966.ATTACK_BONUS, "def": ItemDefinition_966.DEFENSE_BONUS}


class ItemDefinition_967:
    ITEM_ID = "item_967"
    NAME = "Hyperion Legendary Artifact #967"
    TYPE = "Weapon" if 967 % 2 == 0 else "Armor"
    RARITY = "Epic" if 967 % 5 == 0 else "Legendary"
    BASE_VALUE = 48350
    ATTACK_BONUS = 2901
    DEFENSE_BONUS = 1934
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 967."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_967.ITEM_ID, "name": ItemDefinition_967.NAME, "atk": ItemDefinition_967.ATTACK_BONUS, "def": ItemDefinition_967.DEFENSE_BONUS}


class ItemDefinition_968:
    ITEM_ID = "item_968"
    NAME = "Hyperion Legendary Artifact #968"
    TYPE = "Weapon" if 968 % 2 == 0 else "Armor"
    RARITY = "Epic" if 968 % 5 == 0 else "Legendary"
    BASE_VALUE = 48400
    ATTACK_BONUS = 2904
    DEFENSE_BONUS = 1936
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 968."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_968.ITEM_ID, "name": ItemDefinition_968.NAME, "atk": ItemDefinition_968.ATTACK_BONUS, "def": ItemDefinition_968.DEFENSE_BONUS}


class ItemDefinition_969:
    ITEM_ID = "item_969"
    NAME = "Hyperion Legendary Artifact #969"
    TYPE = "Weapon" if 969 % 2 == 0 else "Armor"
    RARITY = "Epic" if 969 % 5 == 0 else "Legendary"
    BASE_VALUE = 48450
    ATTACK_BONUS = 2907
    DEFENSE_BONUS = 1938
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 969."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_969.ITEM_ID, "name": ItemDefinition_969.NAME, "atk": ItemDefinition_969.ATTACK_BONUS, "def": ItemDefinition_969.DEFENSE_BONUS}


class ItemDefinition_970:
    ITEM_ID = "item_970"
    NAME = "Hyperion Legendary Artifact #970"
    TYPE = "Weapon" if 970 % 2 == 0 else "Armor"
    RARITY = "Epic" if 970 % 5 == 0 else "Legendary"
    BASE_VALUE = 48500
    ATTACK_BONUS = 2910
    DEFENSE_BONUS = 1940
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 970."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_970.ITEM_ID, "name": ItemDefinition_970.NAME, "atk": ItemDefinition_970.ATTACK_BONUS, "def": ItemDefinition_970.DEFENSE_BONUS}


class ItemDefinition_971:
    ITEM_ID = "item_971"
    NAME = "Hyperion Legendary Artifact #971"
    TYPE = "Weapon" if 971 % 2 == 0 else "Armor"
    RARITY = "Epic" if 971 % 5 == 0 else "Legendary"
    BASE_VALUE = 48550
    ATTACK_BONUS = 2913
    DEFENSE_BONUS = 1942
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 971."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_971.ITEM_ID, "name": ItemDefinition_971.NAME, "atk": ItemDefinition_971.ATTACK_BONUS, "def": ItemDefinition_971.DEFENSE_BONUS}


class ItemDefinition_972:
    ITEM_ID = "item_972"
    NAME = "Hyperion Legendary Artifact #972"
    TYPE = "Weapon" if 972 % 2 == 0 else "Armor"
    RARITY = "Epic" if 972 % 5 == 0 else "Legendary"
    BASE_VALUE = 48600
    ATTACK_BONUS = 2916
    DEFENSE_BONUS = 1944
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 972."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_972.ITEM_ID, "name": ItemDefinition_972.NAME, "atk": ItemDefinition_972.ATTACK_BONUS, "def": ItemDefinition_972.DEFENSE_BONUS}


class ItemDefinition_973:
    ITEM_ID = "item_973"
    NAME = "Hyperion Legendary Artifact #973"
    TYPE = "Weapon" if 973 % 2 == 0 else "Armor"
    RARITY = "Epic" if 973 % 5 == 0 else "Legendary"
    BASE_VALUE = 48650
    ATTACK_BONUS = 2919
    DEFENSE_BONUS = 1946
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 973."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_973.ITEM_ID, "name": ItemDefinition_973.NAME, "atk": ItemDefinition_973.ATTACK_BONUS, "def": ItemDefinition_973.DEFENSE_BONUS}


class ItemDefinition_974:
    ITEM_ID = "item_974"
    NAME = "Hyperion Legendary Artifact #974"
    TYPE = "Weapon" if 974 % 2 == 0 else "Armor"
    RARITY = "Epic" if 974 % 5 == 0 else "Legendary"
    BASE_VALUE = 48700
    ATTACK_BONUS = 2922
    DEFENSE_BONUS = 1948
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 974."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_974.ITEM_ID, "name": ItemDefinition_974.NAME, "atk": ItemDefinition_974.ATTACK_BONUS, "def": ItemDefinition_974.DEFENSE_BONUS}


class ItemDefinition_975:
    ITEM_ID = "item_975"
    NAME = "Hyperion Legendary Artifact #975"
    TYPE = "Weapon" if 975 % 2 == 0 else "Armor"
    RARITY = "Epic" if 975 % 5 == 0 else "Legendary"
    BASE_VALUE = 48750
    ATTACK_BONUS = 2925
    DEFENSE_BONUS = 1950
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 975."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_975.ITEM_ID, "name": ItemDefinition_975.NAME, "atk": ItemDefinition_975.ATTACK_BONUS, "def": ItemDefinition_975.DEFENSE_BONUS}


class ItemDefinition_976:
    ITEM_ID = "item_976"
    NAME = "Hyperion Legendary Artifact #976"
    TYPE = "Weapon" if 976 % 2 == 0 else "Armor"
    RARITY = "Epic" if 976 % 5 == 0 else "Legendary"
    BASE_VALUE = 48800
    ATTACK_BONUS = 2928
    DEFENSE_BONUS = 1952
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 976."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_976.ITEM_ID, "name": ItemDefinition_976.NAME, "atk": ItemDefinition_976.ATTACK_BONUS, "def": ItemDefinition_976.DEFENSE_BONUS}


class ItemDefinition_977:
    ITEM_ID = "item_977"
    NAME = "Hyperion Legendary Artifact #977"
    TYPE = "Weapon" if 977 % 2 == 0 else "Armor"
    RARITY = "Epic" if 977 % 5 == 0 else "Legendary"
    BASE_VALUE = 48850
    ATTACK_BONUS = 2931
    DEFENSE_BONUS = 1954
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 977."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_977.ITEM_ID, "name": ItemDefinition_977.NAME, "atk": ItemDefinition_977.ATTACK_BONUS, "def": ItemDefinition_977.DEFENSE_BONUS}


class ItemDefinition_978:
    ITEM_ID = "item_978"
    NAME = "Hyperion Legendary Artifact #978"
    TYPE = "Weapon" if 978 % 2 == 0 else "Armor"
    RARITY = "Epic" if 978 % 5 == 0 else "Legendary"
    BASE_VALUE = 48900
    ATTACK_BONUS = 2934
    DEFENSE_BONUS = 1956
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 978."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_978.ITEM_ID, "name": ItemDefinition_978.NAME, "atk": ItemDefinition_978.ATTACK_BONUS, "def": ItemDefinition_978.DEFENSE_BONUS}


class ItemDefinition_979:
    ITEM_ID = "item_979"
    NAME = "Hyperion Legendary Artifact #979"
    TYPE = "Weapon" if 979 % 2 == 0 else "Armor"
    RARITY = "Epic" if 979 % 5 == 0 else "Legendary"
    BASE_VALUE = 48950
    ATTACK_BONUS = 2937
    DEFENSE_BONUS = 1958
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 979."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_979.ITEM_ID, "name": ItemDefinition_979.NAME, "atk": ItemDefinition_979.ATTACK_BONUS, "def": ItemDefinition_979.DEFENSE_BONUS}


class ItemDefinition_980:
    ITEM_ID = "item_980"
    NAME = "Hyperion Legendary Artifact #980"
    TYPE = "Weapon" if 980 % 2 == 0 else "Armor"
    RARITY = "Epic" if 980 % 5 == 0 else "Legendary"
    BASE_VALUE = 49000
    ATTACK_BONUS = 2940
    DEFENSE_BONUS = 1960
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 980."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_980.ITEM_ID, "name": ItemDefinition_980.NAME, "atk": ItemDefinition_980.ATTACK_BONUS, "def": ItemDefinition_980.DEFENSE_BONUS}


class ItemDefinition_981:
    ITEM_ID = "item_981"
    NAME = "Hyperion Legendary Artifact #981"
    TYPE = "Weapon" if 981 % 2 == 0 else "Armor"
    RARITY = "Epic" if 981 % 5 == 0 else "Legendary"
    BASE_VALUE = 49050
    ATTACK_BONUS = 2943
    DEFENSE_BONUS = 1962
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 981."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_981.ITEM_ID, "name": ItemDefinition_981.NAME, "atk": ItemDefinition_981.ATTACK_BONUS, "def": ItemDefinition_981.DEFENSE_BONUS}


class ItemDefinition_982:
    ITEM_ID = "item_982"
    NAME = "Hyperion Legendary Artifact #982"
    TYPE = "Weapon" if 982 % 2 == 0 else "Armor"
    RARITY = "Epic" if 982 % 5 == 0 else "Legendary"
    BASE_VALUE = 49100
    ATTACK_BONUS = 2946
    DEFENSE_BONUS = 1964
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 982."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_982.ITEM_ID, "name": ItemDefinition_982.NAME, "atk": ItemDefinition_982.ATTACK_BONUS, "def": ItemDefinition_982.DEFENSE_BONUS}


class ItemDefinition_983:
    ITEM_ID = "item_983"
    NAME = "Hyperion Legendary Artifact #983"
    TYPE = "Weapon" if 983 % 2 == 0 else "Armor"
    RARITY = "Epic" if 983 % 5 == 0 else "Legendary"
    BASE_VALUE = 49150
    ATTACK_BONUS = 2949
    DEFENSE_BONUS = 1966
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 983."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_983.ITEM_ID, "name": ItemDefinition_983.NAME, "atk": ItemDefinition_983.ATTACK_BONUS, "def": ItemDefinition_983.DEFENSE_BONUS}


class ItemDefinition_984:
    ITEM_ID = "item_984"
    NAME = "Hyperion Legendary Artifact #984"
    TYPE = "Weapon" if 984 % 2 == 0 else "Armor"
    RARITY = "Epic" if 984 % 5 == 0 else "Legendary"
    BASE_VALUE = 49200
    ATTACK_BONUS = 2952
    DEFENSE_BONUS = 1968
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 984."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_984.ITEM_ID, "name": ItemDefinition_984.NAME, "atk": ItemDefinition_984.ATTACK_BONUS, "def": ItemDefinition_984.DEFENSE_BONUS}


class ItemDefinition_985:
    ITEM_ID = "item_985"
    NAME = "Hyperion Legendary Artifact #985"
    TYPE = "Weapon" if 985 % 2 == 0 else "Armor"
    RARITY = "Epic" if 985 % 5 == 0 else "Legendary"
    BASE_VALUE = 49250
    ATTACK_BONUS = 2955
    DEFENSE_BONUS = 1970
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 985."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_985.ITEM_ID, "name": ItemDefinition_985.NAME, "atk": ItemDefinition_985.ATTACK_BONUS, "def": ItemDefinition_985.DEFENSE_BONUS}


class ItemDefinition_986:
    ITEM_ID = "item_986"
    NAME = "Hyperion Legendary Artifact #986"
    TYPE = "Weapon" if 986 % 2 == 0 else "Armor"
    RARITY = "Epic" if 986 % 5 == 0 else "Legendary"
    BASE_VALUE = 49300
    ATTACK_BONUS = 2958
    DEFENSE_BONUS = 1972
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 986."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_986.ITEM_ID, "name": ItemDefinition_986.NAME, "atk": ItemDefinition_986.ATTACK_BONUS, "def": ItemDefinition_986.DEFENSE_BONUS}


class ItemDefinition_987:
    ITEM_ID = "item_987"
    NAME = "Hyperion Legendary Artifact #987"
    TYPE = "Weapon" if 987 % 2 == 0 else "Armor"
    RARITY = "Epic" if 987 % 5 == 0 else "Legendary"
    BASE_VALUE = 49350
    ATTACK_BONUS = 2961
    DEFENSE_BONUS = 1974
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 987."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_987.ITEM_ID, "name": ItemDefinition_987.NAME, "atk": ItemDefinition_987.ATTACK_BONUS, "def": ItemDefinition_987.DEFENSE_BONUS}


class ItemDefinition_988:
    ITEM_ID = "item_988"
    NAME = "Hyperion Legendary Artifact #988"
    TYPE = "Weapon" if 988 % 2 == 0 else "Armor"
    RARITY = "Epic" if 988 % 5 == 0 else "Legendary"
    BASE_VALUE = 49400
    ATTACK_BONUS = 2964
    DEFENSE_BONUS = 1976
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 988."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_988.ITEM_ID, "name": ItemDefinition_988.NAME, "atk": ItemDefinition_988.ATTACK_BONUS, "def": ItemDefinition_988.DEFENSE_BONUS}


class ItemDefinition_989:
    ITEM_ID = "item_989"
    NAME = "Hyperion Legendary Artifact #989"
    TYPE = "Weapon" if 989 % 2 == 0 else "Armor"
    RARITY = "Epic" if 989 % 5 == 0 else "Legendary"
    BASE_VALUE = 49450
    ATTACK_BONUS = 2967
    DEFENSE_BONUS = 1978
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 989."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_989.ITEM_ID, "name": ItemDefinition_989.NAME, "atk": ItemDefinition_989.ATTACK_BONUS, "def": ItemDefinition_989.DEFENSE_BONUS}


class ItemDefinition_990:
    ITEM_ID = "item_990"
    NAME = "Hyperion Legendary Artifact #990"
    TYPE = "Weapon" if 990 % 2 == 0 else "Armor"
    RARITY = "Epic" if 990 % 5 == 0 else "Legendary"
    BASE_VALUE = 49500
    ATTACK_BONUS = 2970
    DEFENSE_BONUS = 1980
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 990."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_990.ITEM_ID, "name": ItemDefinition_990.NAME, "atk": ItemDefinition_990.ATTACK_BONUS, "def": ItemDefinition_990.DEFENSE_BONUS}


class ItemDefinition_991:
    ITEM_ID = "item_991"
    NAME = "Hyperion Legendary Artifact #991"
    TYPE = "Weapon" if 991 % 2 == 0 else "Armor"
    RARITY = "Epic" if 991 % 5 == 0 else "Legendary"
    BASE_VALUE = 49550
    ATTACK_BONUS = 2973
    DEFENSE_BONUS = 1982
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 991."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_991.ITEM_ID, "name": ItemDefinition_991.NAME, "atk": ItemDefinition_991.ATTACK_BONUS, "def": ItemDefinition_991.DEFENSE_BONUS}


class ItemDefinition_992:
    ITEM_ID = "item_992"
    NAME = "Hyperion Legendary Artifact #992"
    TYPE = "Weapon" if 992 % 2 == 0 else "Armor"
    RARITY = "Epic" if 992 % 5 == 0 else "Legendary"
    BASE_VALUE = 49600
    ATTACK_BONUS = 2976
    DEFENSE_BONUS = 1984
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 992."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_992.ITEM_ID, "name": ItemDefinition_992.NAME, "atk": ItemDefinition_992.ATTACK_BONUS, "def": ItemDefinition_992.DEFENSE_BONUS}


class ItemDefinition_993:
    ITEM_ID = "item_993"
    NAME = "Hyperion Legendary Artifact #993"
    TYPE = "Weapon" if 993 % 2 == 0 else "Armor"
    RARITY = "Epic" if 993 % 5 == 0 else "Legendary"
    BASE_VALUE = 49650
    ATTACK_BONUS = 2979
    DEFENSE_BONUS = 1986
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 993."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_993.ITEM_ID, "name": ItemDefinition_993.NAME, "atk": ItemDefinition_993.ATTACK_BONUS, "def": ItemDefinition_993.DEFENSE_BONUS}


class ItemDefinition_994:
    ITEM_ID = "item_994"
    NAME = "Hyperion Legendary Artifact #994"
    TYPE = "Weapon" if 994 % 2 == 0 else "Armor"
    RARITY = "Epic" if 994 % 5 == 0 else "Legendary"
    BASE_VALUE = 49700
    ATTACK_BONUS = 2982
    DEFENSE_BONUS = 1988
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 994."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_994.ITEM_ID, "name": ItemDefinition_994.NAME, "atk": ItemDefinition_994.ATTACK_BONUS, "def": ItemDefinition_994.DEFENSE_BONUS}


class ItemDefinition_995:
    ITEM_ID = "item_995"
    NAME = "Hyperion Legendary Artifact #995"
    TYPE = "Weapon" if 995 % 2 == 0 else "Armor"
    RARITY = "Epic" if 995 % 5 == 0 else "Legendary"
    BASE_VALUE = 49750
    ATTACK_BONUS = 2985
    DEFENSE_BONUS = 1990
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 995."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_995.ITEM_ID, "name": ItemDefinition_995.NAME, "atk": ItemDefinition_995.ATTACK_BONUS, "def": ItemDefinition_995.DEFENSE_BONUS}


class ItemDefinition_996:
    ITEM_ID = "item_996"
    NAME = "Hyperion Legendary Artifact #996"
    TYPE = "Weapon" if 996 % 2 == 0 else "Armor"
    RARITY = "Epic" if 996 % 5 == 0 else "Legendary"
    BASE_VALUE = 49800
    ATTACK_BONUS = 2988
    DEFENSE_BONUS = 1992
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 996."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_996.ITEM_ID, "name": ItemDefinition_996.NAME, "atk": ItemDefinition_996.ATTACK_BONUS, "def": ItemDefinition_996.DEFENSE_BONUS}


class ItemDefinition_997:
    ITEM_ID = "item_997"
    NAME = "Hyperion Legendary Artifact #997"
    TYPE = "Weapon" if 997 % 2 == 0 else "Armor"
    RARITY = "Epic" if 997 % 5 == 0 else "Legendary"
    BASE_VALUE = 49850
    ATTACK_BONUS = 2991
    DEFENSE_BONUS = 1994
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 997."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_997.ITEM_ID, "name": ItemDefinition_997.NAME, "atk": ItemDefinition_997.ATTACK_BONUS, "def": ItemDefinition_997.DEFENSE_BONUS}


class ItemDefinition_998:
    ITEM_ID = "item_998"
    NAME = "Hyperion Legendary Artifact #998"
    TYPE = "Weapon" if 998 % 2 == 0 else "Armor"
    RARITY = "Epic" if 998 % 5 == 0 else "Legendary"
    BASE_VALUE = 49900
    ATTACK_BONUS = 2994
    DEFENSE_BONUS = 1996
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 998."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_998.ITEM_ID, "name": ItemDefinition_998.NAME, "atk": ItemDefinition_998.ATTACK_BONUS, "def": ItemDefinition_998.DEFENSE_BONUS}


class ItemDefinition_999:
    ITEM_ID = "item_999"
    NAME = "Hyperion Legendary Artifact #999"
    TYPE = "Weapon" if 999 % 2 == 0 else "Armor"
    RARITY = "Epic" if 999 % 5 == 0 else "Legendary"
    BASE_VALUE = 49950
    ATTACK_BONUS = 2997
    DEFENSE_BONUS = 1998
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 999."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_999.ITEM_ID, "name": ItemDefinition_999.NAME, "atk": ItemDefinition_999.ATTACK_BONUS, "def": ItemDefinition_999.DEFENSE_BONUS}


class ItemDefinition_1000:
    ITEM_ID = "item_1000"
    NAME = "Hyperion Legendary Artifact #1000"
    TYPE = "Weapon" if 1000 % 2 == 0 else "Armor"
    RARITY = "Epic" if 1000 % 5 == 0 else "Legendary"
    BASE_VALUE = 50000
    ATTACK_BONUS = 3000
    DEFENSE_BONUS = 2000
    DESCRIPTION = "A ancient forged artifact from the primordial hyperion age tier 1000."

    @staticmethod
    def get_stats():
        return {"id": ItemDefinition_1000.ITEM_ID, "name": ItemDefinition_1000.NAME, "atk": ItemDefinition_1000.ATTACK_BONUS, "def": ItemDefinition_1000.DEFENSE_BONUS}
