"""
Gameplay Engine - Expanded Item Registry & Equipment Prefabs
Contains extended items, legendary gear, consumable presets, and crafting schemas.
"""


class ExpandedItemPrefab_1001:
    PREFAB_ID = "item_prefab_1001"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1001"
    EQUIPMENT_SLOT = "Head" if 1001 % 4 == 0 else ("Chest" if 1001 % 4 == 1 else ("Weapon" if 1001 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 12012
    REQUIRE_LEVEL = 21
    SELL_PRICE = 100100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1002:
    PREFAB_ID = "item_prefab_1002"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1002"
    EQUIPMENT_SLOT = "Head" if 1002 % 4 == 0 else ("Chest" if 1002 % 4 == 1 else ("Weapon" if 1002 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 12024
    REQUIRE_LEVEL = 21
    SELL_PRICE = 100200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1003:
    PREFAB_ID = "item_prefab_1003"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1003"
    EQUIPMENT_SLOT = "Head" if 1003 % 4 == 0 else ("Chest" if 1003 % 4 == 1 else ("Weapon" if 1003 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 12036
    REQUIRE_LEVEL = 21
    SELL_PRICE = 100300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1004:
    PREFAB_ID = "item_prefab_1004"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1004"
    EQUIPMENT_SLOT = "Head" if 1004 % 4 == 0 else ("Chest" if 1004 % 4 == 1 else ("Weapon" if 1004 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 12048
    REQUIRE_LEVEL = 21
    SELL_PRICE = 100400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1005:
    PREFAB_ID = "item_prefab_1005"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1005"
    EQUIPMENT_SLOT = "Head" if 1005 % 4 == 0 else ("Chest" if 1005 % 4 == 1 else ("Weapon" if 1005 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 12060
    REQUIRE_LEVEL = 21
    SELL_PRICE = 100500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1006:
    PREFAB_ID = "item_prefab_1006"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1006"
    EQUIPMENT_SLOT = "Head" if 1006 % 4 == 0 else ("Chest" if 1006 % 4 == 1 else ("Weapon" if 1006 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 12072
    REQUIRE_LEVEL = 21
    SELL_PRICE = 100600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1007:
    PREFAB_ID = "item_prefab_1007"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1007"
    EQUIPMENT_SLOT = "Head" if 1007 % 4 == 0 else ("Chest" if 1007 % 4 == 1 else ("Weapon" if 1007 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 12084
    REQUIRE_LEVEL = 21
    SELL_PRICE = 100700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1008:
    PREFAB_ID = "item_prefab_1008"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1008"
    EQUIPMENT_SLOT = "Head" if 1008 % 4 == 0 else ("Chest" if 1008 % 4 == 1 else ("Weapon" if 1008 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 12096
    REQUIRE_LEVEL = 21
    SELL_PRICE = 100800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1009:
    PREFAB_ID = "item_prefab_1009"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1009"
    EQUIPMENT_SLOT = "Head" if 1009 % 4 == 0 else ("Chest" if 1009 % 4 == 1 else ("Weapon" if 1009 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 12108
    REQUIRE_LEVEL = 21
    SELL_PRICE = 100900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1010:
    PREFAB_ID = "item_prefab_1010"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1010"
    EQUIPMENT_SLOT = "Head" if 1010 % 4 == 0 else ("Chest" if 1010 % 4 == 1 else ("Weapon" if 1010 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 12120
    REQUIRE_LEVEL = 21
    SELL_PRICE = 101000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1011:
    PREFAB_ID = "item_prefab_1011"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1011"
    EQUIPMENT_SLOT = "Head" if 1011 % 4 == 0 else ("Chest" if 1011 % 4 == 1 else ("Weapon" if 1011 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 12132
    REQUIRE_LEVEL = 21
    SELL_PRICE = 101100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1012:
    PREFAB_ID = "item_prefab_1012"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1012"
    EQUIPMENT_SLOT = "Head" if 1012 % 4 == 0 else ("Chest" if 1012 % 4 == 1 else ("Weapon" if 1012 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 12144
    REQUIRE_LEVEL = 21
    SELL_PRICE = 101200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1013:
    PREFAB_ID = "item_prefab_1013"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1013"
    EQUIPMENT_SLOT = "Head" if 1013 % 4 == 0 else ("Chest" if 1013 % 4 == 1 else ("Weapon" if 1013 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 12156
    REQUIRE_LEVEL = 21
    SELL_PRICE = 101300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1014:
    PREFAB_ID = "item_prefab_1014"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1014"
    EQUIPMENT_SLOT = "Head" if 1014 % 4 == 0 else ("Chest" if 1014 % 4 == 1 else ("Weapon" if 1014 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 12168
    REQUIRE_LEVEL = 21
    SELL_PRICE = 101400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1015:
    PREFAB_ID = "item_prefab_1015"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1015"
    EQUIPMENT_SLOT = "Head" if 1015 % 4 == 0 else ("Chest" if 1015 % 4 == 1 else ("Weapon" if 1015 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 12180
    REQUIRE_LEVEL = 21
    SELL_PRICE = 101500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1016:
    PREFAB_ID = "item_prefab_1016"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1016"
    EQUIPMENT_SLOT = "Head" if 1016 % 4 == 0 else ("Chest" if 1016 % 4 == 1 else ("Weapon" if 1016 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 12192
    REQUIRE_LEVEL = 21
    SELL_PRICE = 101600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1017:
    PREFAB_ID = "item_prefab_1017"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1017"
    EQUIPMENT_SLOT = "Head" if 1017 % 4 == 0 else ("Chest" if 1017 % 4 == 1 else ("Weapon" if 1017 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 12204
    REQUIRE_LEVEL = 21
    SELL_PRICE = 101700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1018:
    PREFAB_ID = "item_prefab_1018"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1018"
    EQUIPMENT_SLOT = "Head" if 1018 % 4 == 0 else ("Chest" if 1018 % 4 == 1 else ("Weapon" if 1018 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 12216
    REQUIRE_LEVEL = 21
    SELL_PRICE = 101800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1019:
    PREFAB_ID = "item_prefab_1019"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1019"
    EQUIPMENT_SLOT = "Head" if 1019 % 4 == 0 else ("Chest" if 1019 % 4 == 1 else ("Weapon" if 1019 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 12228
    REQUIRE_LEVEL = 21
    SELL_PRICE = 101900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1020:
    PREFAB_ID = "item_prefab_1020"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1020"
    EQUIPMENT_SLOT = "Head" if 1020 % 4 == 0 else ("Chest" if 1020 % 4 == 1 else ("Weapon" if 1020 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 12240
    REQUIRE_LEVEL = 21
    SELL_PRICE = 102000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1021:
    PREFAB_ID = "item_prefab_1021"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1021"
    EQUIPMENT_SLOT = "Head" if 1021 % 4 == 0 else ("Chest" if 1021 % 4 == 1 else ("Weapon" if 1021 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 12252
    REQUIRE_LEVEL = 21
    SELL_PRICE = 102100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1022:
    PREFAB_ID = "item_prefab_1022"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1022"
    EQUIPMENT_SLOT = "Head" if 1022 % 4 == 0 else ("Chest" if 1022 % 4 == 1 else ("Weapon" if 1022 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 12264
    REQUIRE_LEVEL = 21
    SELL_PRICE = 102200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1023:
    PREFAB_ID = "item_prefab_1023"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1023"
    EQUIPMENT_SLOT = "Head" if 1023 % 4 == 0 else ("Chest" if 1023 % 4 == 1 else ("Weapon" if 1023 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 12276
    REQUIRE_LEVEL = 21
    SELL_PRICE = 102300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1024:
    PREFAB_ID = "item_prefab_1024"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1024"
    EQUIPMENT_SLOT = "Head" if 1024 % 4 == 0 else ("Chest" if 1024 % 4 == 1 else ("Weapon" if 1024 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 12288
    REQUIRE_LEVEL = 21
    SELL_PRICE = 102400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1025:
    PREFAB_ID = "item_prefab_1025"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1025"
    EQUIPMENT_SLOT = "Head" if 1025 % 4 == 0 else ("Chest" if 1025 % 4 == 1 else ("Weapon" if 1025 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 12300
    REQUIRE_LEVEL = 21
    SELL_PRICE = 102500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1026:
    PREFAB_ID = "item_prefab_1026"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1026"
    EQUIPMENT_SLOT = "Head" if 1026 % 4 == 0 else ("Chest" if 1026 % 4 == 1 else ("Weapon" if 1026 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 12312
    REQUIRE_LEVEL = 21
    SELL_PRICE = 102600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1027:
    PREFAB_ID = "item_prefab_1027"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1027"
    EQUIPMENT_SLOT = "Head" if 1027 % 4 == 0 else ("Chest" if 1027 % 4 == 1 else ("Weapon" if 1027 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 12324
    REQUIRE_LEVEL = 21
    SELL_PRICE = 102700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1028:
    PREFAB_ID = "item_prefab_1028"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1028"
    EQUIPMENT_SLOT = "Head" if 1028 % 4 == 0 else ("Chest" if 1028 % 4 == 1 else ("Weapon" if 1028 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 12336
    REQUIRE_LEVEL = 21
    SELL_PRICE = 102800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1029:
    PREFAB_ID = "item_prefab_1029"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1029"
    EQUIPMENT_SLOT = "Head" if 1029 % 4 == 0 else ("Chest" if 1029 % 4 == 1 else ("Weapon" if 1029 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 12348
    REQUIRE_LEVEL = 21
    SELL_PRICE = 102900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1030:
    PREFAB_ID = "item_prefab_1030"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1030"
    EQUIPMENT_SLOT = "Head" if 1030 % 4 == 0 else ("Chest" if 1030 % 4 == 1 else ("Weapon" if 1030 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 12360
    REQUIRE_LEVEL = 21
    SELL_PRICE = 103000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1031:
    PREFAB_ID = "item_prefab_1031"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1031"
    EQUIPMENT_SLOT = "Head" if 1031 % 4 == 0 else ("Chest" if 1031 % 4 == 1 else ("Weapon" if 1031 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 12372
    REQUIRE_LEVEL = 21
    SELL_PRICE = 103100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1032:
    PREFAB_ID = "item_prefab_1032"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1032"
    EQUIPMENT_SLOT = "Head" if 1032 % 4 == 0 else ("Chest" if 1032 % 4 == 1 else ("Weapon" if 1032 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 12384
    REQUIRE_LEVEL = 21
    SELL_PRICE = 103200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1033:
    PREFAB_ID = "item_prefab_1033"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1033"
    EQUIPMENT_SLOT = "Head" if 1033 % 4 == 0 else ("Chest" if 1033 % 4 == 1 else ("Weapon" if 1033 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 12396
    REQUIRE_LEVEL = 21
    SELL_PRICE = 103300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1034:
    PREFAB_ID = "item_prefab_1034"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1034"
    EQUIPMENT_SLOT = "Head" if 1034 % 4 == 0 else ("Chest" if 1034 % 4 == 1 else ("Weapon" if 1034 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 12408
    REQUIRE_LEVEL = 21
    SELL_PRICE = 103400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1035:
    PREFAB_ID = "item_prefab_1035"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1035"
    EQUIPMENT_SLOT = "Head" if 1035 % 4 == 0 else ("Chest" if 1035 % 4 == 1 else ("Weapon" if 1035 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 12420
    REQUIRE_LEVEL = 21
    SELL_PRICE = 103500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1036:
    PREFAB_ID = "item_prefab_1036"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1036"
    EQUIPMENT_SLOT = "Head" if 1036 % 4 == 0 else ("Chest" if 1036 % 4 == 1 else ("Weapon" if 1036 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 12432
    REQUIRE_LEVEL = 21
    SELL_PRICE = 103600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1037:
    PREFAB_ID = "item_prefab_1037"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1037"
    EQUIPMENT_SLOT = "Head" if 1037 % 4 == 0 else ("Chest" if 1037 % 4 == 1 else ("Weapon" if 1037 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 12444
    REQUIRE_LEVEL = 21
    SELL_PRICE = 103700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1038:
    PREFAB_ID = "item_prefab_1038"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1038"
    EQUIPMENT_SLOT = "Head" if 1038 % 4 == 0 else ("Chest" if 1038 % 4 == 1 else ("Weapon" if 1038 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 12456
    REQUIRE_LEVEL = 21
    SELL_PRICE = 103800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1039:
    PREFAB_ID = "item_prefab_1039"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1039"
    EQUIPMENT_SLOT = "Head" if 1039 % 4 == 0 else ("Chest" if 1039 % 4 == 1 else ("Weapon" if 1039 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 12468
    REQUIRE_LEVEL = 21
    SELL_PRICE = 103900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1040:
    PREFAB_ID = "item_prefab_1040"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1040"
    EQUIPMENT_SLOT = "Head" if 1040 % 4 == 0 else ("Chest" if 1040 % 4 == 1 else ("Weapon" if 1040 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 12480
    REQUIRE_LEVEL = 21
    SELL_PRICE = 104000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1041:
    PREFAB_ID = "item_prefab_1041"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1041"
    EQUIPMENT_SLOT = "Head" if 1041 % 4 == 0 else ("Chest" if 1041 % 4 == 1 else ("Weapon" if 1041 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 12492
    REQUIRE_LEVEL = 21
    SELL_PRICE = 104100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1042:
    PREFAB_ID = "item_prefab_1042"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1042"
    EQUIPMENT_SLOT = "Head" if 1042 % 4 == 0 else ("Chest" if 1042 % 4 == 1 else ("Weapon" if 1042 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 12504
    REQUIRE_LEVEL = 21
    SELL_PRICE = 104200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1043:
    PREFAB_ID = "item_prefab_1043"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1043"
    EQUIPMENT_SLOT = "Head" if 1043 % 4 == 0 else ("Chest" if 1043 % 4 == 1 else ("Weapon" if 1043 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 12516
    REQUIRE_LEVEL = 21
    SELL_PRICE = 104300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1044:
    PREFAB_ID = "item_prefab_1044"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1044"
    EQUIPMENT_SLOT = "Head" if 1044 % 4 == 0 else ("Chest" if 1044 % 4 == 1 else ("Weapon" if 1044 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 12528
    REQUIRE_LEVEL = 21
    SELL_PRICE = 104400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1045:
    PREFAB_ID = "item_prefab_1045"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1045"
    EQUIPMENT_SLOT = "Head" if 1045 % 4 == 0 else ("Chest" if 1045 % 4 == 1 else ("Weapon" if 1045 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 12540
    REQUIRE_LEVEL = 21
    SELL_PRICE = 104500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1046:
    PREFAB_ID = "item_prefab_1046"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1046"
    EQUIPMENT_SLOT = "Head" if 1046 % 4 == 0 else ("Chest" if 1046 % 4 == 1 else ("Weapon" if 1046 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 12552
    REQUIRE_LEVEL = 21
    SELL_PRICE = 104600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1047:
    PREFAB_ID = "item_prefab_1047"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1047"
    EQUIPMENT_SLOT = "Head" if 1047 % 4 == 0 else ("Chest" if 1047 % 4 == 1 else ("Weapon" if 1047 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 12564
    REQUIRE_LEVEL = 21
    SELL_PRICE = 104700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1048:
    PREFAB_ID = "item_prefab_1048"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1048"
    EQUIPMENT_SLOT = "Head" if 1048 % 4 == 0 else ("Chest" if 1048 % 4 == 1 else ("Weapon" if 1048 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 12576
    REQUIRE_LEVEL = 21
    SELL_PRICE = 104800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1049:
    PREFAB_ID = "item_prefab_1049"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1049"
    EQUIPMENT_SLOT = "Head" if 1049 % 4 == 0 else ("Chest" if 1049 % 4 == 1 else ("Weapon" if 1049 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 12588
    REQUIRE_LEVEL = 21
    SELL_PRICE = 104900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1050:
    PREFAB_ID = "item_prefab_1050"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1050"
    EQUIPMENT_SLOT = "Head" if 1050 % 4 == 0 else ("Chest" if 1050 % 4 == 1 else ("Weapon" if 1050 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 12600
    REQUIRE_LEVEL = 22
    SELL_PRICE = 105000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1051:
    PREFAB_ID = "item_prefab_1051"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1051"
    EQUIPMENT_SLOT = "Head" if 1051 % 4 == 0 else ("Chest" if 1051 % 4 == 1 else ("Weapon" if 1051 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 12612
    REQUIRE_LEVEL = 22
    SELL_PRICE = 105100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1052:
    PREFAB_ID = "item_prefab_1052"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1052"
    EQUIPMENT_SLOT = "Head" if 1052 % 4 == 0 else ("Chest" if 1052 % 4 == 1 else ("Weapon" if 1052 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 12624
    REQUIRE_LEVEL = 22
    SELL_PRICE = 105200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1053:
    PREFAB_ID = "item_prefab_1053"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1053"
    EQUIPMENT_SLOT = "Head" if 1053 % 4 == 0 else ("Chest" if 1053 % 4 == 1 else ("Weapon" if 1053 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 12636
    REQUIRE_LEVEL = 22
    SELL_PRICE = 105300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1054:
    PREFAB_ID = "item_prefab_1054"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1054"
    EQUIPMENT_SLOT = "Head" if 1054 % 4 == 0 else ("Chest" if 1054 % 4 == 1 else ("Weapon" if 1054 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 12648
    REQUIRE_LEVEL = 22
    SELL_PRICE = 105400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1055:
    PREFAB_ID = "item_prefab_1055"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1055"
    EQUIPMENT_SLOT = "Head" if 1055 % 4 == 0 else ("Chest" if 1055 % 4 == 1 else ("Weapon" if 1055 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 12660
    REQUIRE_LEVEL = 22
    SELL_PRICE = 105500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1056:
    PREFAB_ID = "item_prefab_1056"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1056"
    EQUIPMENT_SLOT = "Head" if 1056 % 4 == 0 else ("Chest" if 1056 % 4 == 1 else ("Weapon" if 1056 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 12672
    REQUIRE_LEVEL = 22
    SELL_PRICE = 105600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1057:
    PREFAB_ID = "item_prefab_1057"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1057"
    EQUIPMENT_SLOT = "Head" if 1057 % 4 == 0 else ("Chest" if 1057 % 4 == 1 else ("Weapon" if 1057 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 12684
    REQUIRE_LEVEL = 22
    SELL_PRICE = 105700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1058:
    PREFAB_ID = "item_prefab_1058"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1058"
    EQUIPMENT_SLOT = "Head" if 1058 % 4 == 0 else ("Chest" if 1058 % 4 == 1 else ("Weapon" if 1058 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 12696
    REQUIRE_LEVEL = 22
    SELL_PRICE = 105800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1059:
    PREFAB_ID = "item_prefab_1059"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1059"
    EQUIPMENT_SLOT = "Head" if 1059 % 4 == 0 else ("Chest" if 1059 % 4 == 1 else ("Weapon" if 1059 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 12708
    REQUIRE_LEVEL = 22
    SELL_PRICE = 105900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1060:
    PREFAB_ID = "item_prefab_1060"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1060"
    EQUIPMENT_SLOT = "Head" if 1060 % 4 == 0 else ("Chest" if 1060 % 4 == 1 else ("Weapon" if 1060 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 12720
    REQUIRE_LEVEL = 22
    SELL_PRICE = 106000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1061:
    PREFAB_ID = "item_prefab_1061"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1061"
    EQUIPMENT_SLOT = "Head" if 1061 % 4 == 0 else ("Chest" if 1061 % 4 == 1 else ("Weapon" if 1061 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 12732
    REQUIRE_LEVEL = 22
    SELL_PRICE = 106100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1062:
    PREFAB_ID = "item_prefab_1062"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1062"
    EQUIPMENT_SLOT = "Head" if 1062 % 4 == 0 else ("Chest" if 1062 % 4 == 1 else ("Weapon" if 1062 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 12744
    REQUIRE_LEVEL = 22
    SELL_PRICE = 106200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1063:
    PREFAB_ID = "item_prefab_1063"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1063"
    EQUIPMENT_SLOT = "Head" if 1063 % 4 == 0 else ("Chest" if 1063 % 4 == 1 else ("Weapon" if 1063 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 12756
    REQUIRE_LEVEL = 22
    SELL_PRICE = 106300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1064:
    PREFAB_ID = "item_prefab_1064"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1064"
    EQUIPMENT_SLOT = "Head" if 1064 % 4 == 0 else ("Chest" if 1064 % 4 == 1 else ("Weapon" if 1064 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 12768
    REQUIRE_LEVEL = 22
    SELL_PRICE = 106400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1065:
    PREFAB_ID = "item_prefab_1065"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1065"
    EQUIPMENT_SLOT = "Head" if 1065 % 4 == 0 else ("Chest" if 1065 % 4 == 1 else ("Weapon" if 1065 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 12780
    REQUIRE_LEVEL = 22
    SELL_PRICE = 106500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1066:
    PREFAB_ID = "item_prefab_1066"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1066"
    EQUIPMENT_SLOT = "Head" if 1066 % 4 == 0 else ("Chest" if 1066 % 4 == 1 else ("Weapon" if 1066 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 12792
    REQUIRE_LEVEL = 22
    SELL_PRICE = 106600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1067:
    PREFAB_ID = "item_prefab_1067"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1067"
    EQUIPMENT_SLOT = "Head" if 1067 % 4 == 0 else ("Chest" if 1067 % 4 == 1 else ("Weapon" if 1067 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 12804
    REQUIRE_LEVEL = 22
    SELL_PRICE = 106700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1068:
    PREFAB_ID = "item_prefab_1068"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1068"
    EQUIPMENT_SLOT = "Head" if 1068 % 4 == 0 else ("Chest" if 1068 % 4 == 1 else ("Weapon" if 1068 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 12816
    REQUIRE_LEVEL = 22
    SELL_PRICE = 106800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1069:
    PREFAB_ID = "item_prefab_1069"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1069"
    EQUIPMENT_SLOT = "Head" if 1069 % 4 == 0 else ("Chest" if 1069 % 4 == 1 else ("Weapon" if 1069 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 12828
    REQUIRE_LEVEL = 22
    SELL_PRICE = 106900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1070:
    PREFAB_ID = "item_prefab_1070"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1070"
    EQUIPMENT_SLOT = "Head" if 1070 % 4 == 0 else ("Chest" if 1070 % 4 == 1 else ("Weapon" if 1070 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 12840
    REQUIRE_LEVEL = 22
    SELL_PRICE = 107000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1071:
    PREFAB_ID = "item_prefab_1071"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1071"
    EQUIPMENT_SLOT = "Head" if 1071 % 4 == 0 else ("Chest" if 1071 % 4 == 1 else ("Weapon" if 1071 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 12852
    REQUIRE_LEVEL = 22
    SELL_PRICE = 107100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1072:
    PREFAB_ID = "item_prefab_1072"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1072"
    EQUIPMENT_SLOT = "Head" if 1072 % 4 == 0 else ("Chest" if 1072 % 4 == 1 else ("Weapon" if 1072 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 12864
    REQUIRE_LEVEL = 22
    SELL_PRICE = 107200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1073:
    PREFAB_ID = "item_prefab_1073"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1073"
    EQUIPMENT_SLOT = "Head" if 1073 % 4 == 0 else ("Chest" if 1073 % 4 == 1 else ("Weapon" if 1073 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 12876
    REQUIRE_LEVEL = 22
    SELL_PRICE = 107300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1074:
    PREFAB_ID = "item_prefab_1074"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1074"
    EQUIPMENT_SLOT = "Head" if 1074 % 4 == 0 else ("Chest" if 1074 % 4 == 1 else ("Weapon" if 1074 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 12888
    REQUIRE_LEVEL = 22
    SELL_PRICE = 107400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1075:
    PREFAB_ID = "item_prefab_1075"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1075"
    EQUIPMENT_SLOT = "Head" if 1075 % 4 == 0 else ("Chest" if 1075 % 4 == 1 else ("Weapon" if 1075 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 12900
    REQUIRE_LEVEL = 22
    SELL_PRICE = 107500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1076:
    PREFAB_ID = "item_prefab_1076"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1076"
    EQUIPMENT_SLOT = "Head" if 1076 % 4 == 0 else ("Chest" if 1076 % 4 == 1 else ("Weapon" if 1076 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 12912
    REQUIRE_LEVEL = 22
    SELL_PRICE = 107600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1077:
    PREFAB_ID = "item_prefab_1077"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1077"
    EQUIPMENT_SLOT = "Head" if 1077 % 4 == 0 else ("Chest" if 1077 % 4 == 1 else ("Weapon" if 1077 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 12924
    REQUIRE_LEVEL = 22
    SELL_PRICE = 107700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1078:
    PREFAB_ID = "item_prefab_1078"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1078"
    EQUIPMENT_SLOT = "Head" if 1078 % 4 == 0 else ("Chest" if 1078 % 4 == 1 else ("Weapon" if 1078 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 12936
    REQUIRE_LEVEL = 22
    SELL_PRICE = 107800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1079:
    PREFAB_ID = "item_prefab_1079"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1079"
    EQUIPMENT_SLOT = "Head" if 1079 % 4 == 0 else ("Chest" if 1079 % 4 == 1 else ("Weapon" if 1079 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 12948
    REQUIRE_LEVEL = 22
    SELL_PRICE = 107900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1080:
    PREFAB_ID = "item_prefab_1080"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1080"
    EQUIPMENT_SLOT = "Head" if 1080 % 4 == 0 else ("Chest" if 1080 % 4 == 1 else ("Weapon" if 1080 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 12960
    REQUIRE_LEVEL = 22
    SELL_PRICE = 108000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1081:
    PREFAB_ID = "item_prefab_1081"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1081"
    EQUIPMENT_SLOT = "Head" if 1081 % 4 == 0 else ("Chest" if 1081 % 4 == 1 else ("Weapon" if 1081 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 12972
    REQUIRE_LEVEL = 22
    SELL_PRICE = 108100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1082:
    PREFAB_ID = "item_prefab_1082"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1082"
    EQUIPMENT_SLOT = "Head" if 1082 % 4 == 0 else ("Chest" if 1082 % 4 == 1 else ("Weapon" if 1082 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 12984
    REQUIRE_LEVEL = 22
    SELL_PRICE = 108200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1083:
    PREFAB_ID = "item_prefab_1083"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1083"
    EQUIPMENT_SLOT = "Head" if 1083 % 4 == 0 else ("Chest" if 1083 % 4 == 1 else ("Weapon" if 1083 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 12996
    REQUIRE_LEVEL = 22
    SELL_PRICE = 108300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1084:
    PREFAB_ID = "item_prefab_1084"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1084"
    EQUIPMENT_SLOT = "Head" if 1084 % 4 == 0 else ("Chest" if 1084 % 4 == 1 else ("Weapon" if 1084 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 13008
    REQUIRE_LEVEL = 22
    SELL_PRICE = 108400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1085:
    PREFAB_ID = "item_prefab_1085"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1085"
    EQUIPMENT_SLOT = "Head" if 1085 % 4 == 0 else ("Chest" if 1085 % 4 == 1 else ("Weapon" if 1085 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 13020
    REQUIRE_LEVEL = 22
    SELL_PRICE = 108500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1086:
    PREFAB_ID = "item_prefab_1086"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1086"
    EQUIPMENT_SLOT = "Head" if 1086 % 4 == 0 else ("Chest" if 1086 % 4 == 1 else ("Weapon" if 1086 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 13032
    REQUIRE_LEVEL = 22
    SELL_PRICE = 108600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1087:
    PREFAB_ID = "item_prefab_1087"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1087"
    EQUIPMENT_SLOT = "Head" if 1087 % 4 == 0 else ("Chest" if 1087 % 4 == 1 else ("Weapon" if 1087 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 13044
    REQUIRE_LEVEL = 22
    SELL_PRICE = 108700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1088:
    PREFAB_ID = "item_prefab_1088"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1088"
    EQUIPMENT_SLOT = "Head" if 1088 % 4 == 0 else ("Chest" if 1088 % 4 == 1 else ("Weapon" if 1088 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 13056
    REQUIRE_LEVEL = 22
    SELL_PRICE = 108800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1089:
    PREFAB_ID = "item_prefab_1089"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1089"
    EQUIPMENT_SLOT = "Head" if 1089 % 4 == 0 else ("Chest" if 1089 % 4 == 1 else ("Weapon" if 1089 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 13068
    REQUIRE_LEVEL = 22
    SELL_PRICE = 108900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1090:
    PREFAB_ID = "item_prefab_1090"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1090"
    EQUIPMENT_SLOT = "Head" if 1090 % 4 == 0 else ("Chest" if 1090 % 4 == 1 else ("Weapon" if 1090 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 13080
    REQUIRE_LEVEL = 22
    SELL_PRICE = 109000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1091:
    PREFAB_ID = "item_prefab_1091"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1091"
    EQUIPMENT_SLOT = "Head" if 1091 % 4 == 0 else ("Chest" if 1091 % 4 == 1 else ("Weapon" if 1091 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 13092
    REQUIRE_LEVEL = 22
    SELL_PRICE = 109100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1092:
    PREFAB_ID = "item_prefab_1092"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1092"
    EQUIPMENT_SLOT = "Head" if 1092 % 4 == 0 else ("Chest" if 1092 % 4 == 1 else ("Weapon" if 1092 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 13104
    REQUIRE_LEVEL = 22
    SELL_PRICE = 109200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1093:
    PREFAB_ID = "item_prefab_1093"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1093"
    EQUIPMENT_SLOT = "Head" if 1093 % 4 == 0 else ("Chest" if 1093 % 4 == 1 else ("Weapon" if 1093 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 13116
    REQUIRE_LEVEL = 22
    SELL_PRICE = 109300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1094:
    PREFAB_ID = "item_prefab_1094"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1094"
    EQUIPMENT_SLOT = "Head" if 1094 % 4 == 0 else ("Chest" if 1094 % 4 == 1 else ("Weapon" if 1094 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 13128
    REQUIRE_LEVEL = 22
    SELL_PRICE = 109400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1095:
    PREFAB_ID = "item_prefab_1095"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1095"
    EQUIPMENT_SLOT = "Head" if 1095 % 4 == 0 else ("Chest" if 1095 % 4 == 1 else ("Weapon" if 1095 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 13140
    REQUIRE_LEVEL = 22
    SELL_PRICE = 109500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1096:
    PREFAB_ID = "item_prefab_1096"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1096"
    EQUIPMENT_SLOT = "Head" if 1096 % 4 == 0 else ("Chest" if 1096 % 4 == 1 else ("Weapon" if 1096 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 13152
    REQUIRE_LEVEL = 22
    SELL_PRICE = 109600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1097:
    PREFAB_ID = "item_prefab_1097"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1097"
    EQUIPMENT_SLOT = "Head" if 1097 % 4 == 0 else ("Chest" if 1097 % 4 == 1 else ("Weapon" if 1097 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 13164
    REQUIRE_LEVEL = 22
    SELL_PRICE = 109700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1098:
    PREFAB_ID = "item_prefab_1098"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1098"
    EQUIPMENT_SLOT = "Head" if 1098 % 4 == 0 else ("Chest" if 1098 % 4 == 1 else ("Weapon" if 1098 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 13176
    REQUIRE_LEVEL = 22
    SELL_PRICE = 109800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1099:
    PREFAB_ID = "item_prefab_1099"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1099"
    EQUIPMENT_SLOT = "Head" if 1099 % 4 == 0 else ("Chest" if 1099 % 4 == 1 else ("Weapon" if 1099 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 13188
    REQUIRE_LEVEL = 22
    SELL_PRICE = 109900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1100:
    PREFAB_ID = "item_prefab_1100"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1100"
    EQUIPMENT_SLOT = "Head" if 1100 % 4 == 0 else ("Chest" if 1100 % 4 == 1 else ("Weapon" if 1100 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 13200
    REQUIRE_LEVEL = 23
    SELL_PRICE = 110000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1101:
    PREFAB_ID = "item_prefab_1101"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1101"
    EQUIPMENT_SLOT = "Head" if 1101 % 4 == 0 else ("Chest" if 1101 % 4 == 1 else ("Weapon" if 1101 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 13212
    REQUIRE_LEVEL = 23
    SELL_PRICE = 110100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1102:
    PREFAB_ID = "item_prefab_1102"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1102"
    EQUIPMENT_SLOT = "Head" if 1102 % 4 == 0 else ("Chest" if 1102 % 4 == 1 else ("Weapon" if 1102 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 13224
    REQUIRE_LEVEL = 23
    SELL_PRICE = 110200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1103:
    PREFAB_ID = "item_prefab_1103"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1103"
    EQUIPMENT_SLOT = "Head" if 1103 % 4 == 0 else ("Chest" if 1103 % 4 == 1 else ("Weapon" if 1103 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 13236
    REQUIRE_LEVEL = 23
    SELL_PRICE = 110300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1104:
    PREFAB_ID = "item_prefab_1104"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1104"
    EQUIPMENT_SLOT = "Head" if 1104 % 4 == 0 else ("Chest" if 1104 % 4 == 1 else ("Weapon" if 1104 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 13248
    REQUIRE_LEVEL = 23
    SELL_PRICE = 110400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1105:
    PREFAB_ID = "item_prefab_1105"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1105"
    EQUIPMENT_SLOT = "Head" if 1105 % 4 == 0 else ("Chest" if 1105 % 4 == 1 else ("Weapon" if 1105 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 13260
    REQUIRE_LEVEL = 23
    SELL_PRICE = 110500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1106:
    PREFAB_ID = "item_prefab_1106"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1106"
    EQUIPMENT_SLOT = "Head" if 1106 % 4 == 0 else ("Chest" if 1106 % 4 == 1 else ("Weapon" if 1106 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 13272
    REQUIRE_LEVEL = 23
    SELL_PRICE = 110600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1107:
    PREFAB_ID = "item_prefab_1107"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1107"
    EQUIPMENT_SLOT = "Head" if 1107 % 4 == 0 else ("Chest" if 1107 % 4 == 1 else ("Weapon" if 1107 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 13284
    REQUIRE_LEVEL = 23
    SELL_PRICE = 110700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1108:
    PREFAB_ID = "item_prefab_1108"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1108"
    EQUIPMENT_SLOT = "Head" if 1108 % 4 == 0 else ("Chest" if 1108 % 4 == 1 else ("Weapon" if 1108 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 13296
    REQUIRE_LEVEL = 23
    SELL_PRICE = 110800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1109:
    PREFAB_ID = "item_prefab_1109"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1109"
    EQUIPMENT_SLOT = "Head" if 1109 % 4 == 0 else ("Chest" if 1109 % 4 == 1 else ("Weapon" if 1109 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 13308
    REQUIRE_LEVEL = 23
    SELL_PRICE = 110900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1110:
    PREFAB_ID = "item_prefab_1110"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1110"
    EQUIPMENT_SLOT = "Head" if 1110 % 4 == 0 else ("Chest" if 1110 % 4 == 1 else ("Weapon" if 1110 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 13320
    REQUIRE_LEVEL = 23
    SELL_PRICE = 111000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1111:
    PREFAB_ID = "item_prefab_1111"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1111"
    EQUIPMENT_SLOT = "Head" if 1111 % 4 == 0 else ("Chest" if 1111 % 4 == 1 else ("Weapon" if 1111 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 13332
    REQUIRE_LEVEL = 23
    SELL_PRICE = 111100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1112:
    PREFAB_ID = "item_prefab_1112"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1112"
    EQUIPMENT_SLOT = "Head" if 1112 % 4 == 0 else ("Chest" if 1112 % 4 == 1 else ("Weapon" if 1112 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 13344
    REQUIRE_LEVEL = 23
    SELL_PRICE = 111200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1113:
    PREFAB_ID = "item_prefab_1113"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1113"
    EQUIPMENT_SLOT = "Head" if 1113 % 4 == 0 else ("Chest" if 1113 % 4 == 1 else ("Weapon" if 1113 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 13356
    REQUIRE_LEVEL = 23
    SELL_PRICE = 111300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1114:
    PREFAB_ID = "item_prefab_1114"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1114"
    EQUIPMENT_SLOT = "Head" if 1114 % 4 == 0 else ("Chest" if 1114 % 4 == 1 else ("Weapon" if 1114 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 13368
    REQUIRE_LEVEL = 23
    SELL_PRICE = 111400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1115:
    PREFAB_ID = "item_prefab_1115"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1115"
    EQUIPMENT_SLOT = "Head" if 1115 % 4 == 0 else ("Chest" if 1115 % 4 == 1 else ("Weapon" if 1115 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 13380
    REQUIRE_LEVEL = 23
    SELL_PRICE = 111500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1116:
    PREFAB_ID = "item_prefab_1116"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1116"
    EQUIPMENT_SLOT = "Head" if 1116 % 4 == 0 else ("Chest" if 1116 % 4 == 1 else ("Weapon" if 1116 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 13392
    REQUIRE_LEVEL = 23
    SELL_PRICE = 111600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1117:
    PREFAB_ID = "item_prefab_1117"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1117"
    EQUIPMENT_SLOT = "Head" if 1117 % 4 == 0 else ("Chest" if 1117 % 4 == 1 else ("Weapon" if 1117 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 13404
    REQUIRE_LEVEL = 23
    SELL_PRICE = 111700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1118:
    PREFAB_ID = "item_prefab_1118"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1118"
    EQUIPMENT_SLOT = "Head" if 1118 % 4 == 0 else ("Chest" if 1118 % 4 == 1 else ("Weapon" if 1118 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 13416
    REQUIRE_LEVEL = 23
    SELL_PRICE = 111800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1119:
    PREFAB_ID = "item_prefab_1119"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1119"
    EQUIPMENT_SLOT = "Head" if 1119 % 4 == 0 else ("Chest" if 1119 % 4 == 1 else ("Weapon" if 1119 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 13428
    REQUIRE_LEVEL = 23
    SELL_PRICE = 111900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1120:
    PREFAB_ID = "item_prefab_1120"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1120"
    EQUIPMENT_SLOT = "Head" if 1120 % 4 == 0 else ("Chest" if 1120 % 4 == 1 else ("Weapon" if 1120 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 13440
    REQUIRE_LEVEL = 23
    SELL_PRICE = 112000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1121:
    PREFAB_ID = "item_prefab_1121"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1121"
    EQUIPMENT_SLOT = "Head" if 1121 % 4 == 0 else ("Chest" if 1121 % 4 == 1 else ("Weapon" if 1121 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 13452
    REQUIRE_LEVEL = 23
    SELL_PRICE = 112100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1122:
    PREFAB_ID = "item_prefab_1122"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1122"
    EQUIPMENT_SLOT = "Head" if 1122 % 4 == 0 else ("Chest" if 1122 % 4 == 1 else ("Weapon" if 1122 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 13464
    REQUIRE_LEVEL = 23
    SELL_PRICE = 112200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1123:
    PREFAB_ID = "item_prefab_1123"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1123"
    EQUIPMENT_SLOT = "Head" if 1123 % 4 == 0 else ("Chest" if 1123 % 4 == 1 else ("Weapon" if 1123 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 13476
    REQUIRE_LEVEL = 23
    SELL_PRICE = 112300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1124:
    PREFAB_ID = "item_prefab_1124"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1124"
    EQUIPMENT_SLOT = "Head" if 1124 % 4 == 0 else ("Chest" if 1124 % 4 == 1 else ("Weapon" if 1124 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 13488
    REQUIRE_LEVEL = 23
    SELL_PRICE = 112400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1125:
    PREFAB_ID = "item_prefab_1125"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1125"
    EQUIPMENT_SLOT = "Head" if 1125 % 4 == 0 else ("Chest" if 1125 % 4 == 1 else ("Weapon" if 1125 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 13500
    REQUIRE_LEVEL = 23
    SELL_PRICE = 112500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1126:
    PREFAB_ID = "item_prefab_1126"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1126"
    EQUIPMENT_SLOT = "Head" if 1126 % 4 == 0 else ("Chest" if 1126 % 4 == 1 else ("Weapon" if 1126 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 13512
    REQUIRE_LEVEL = 23
    SELL_PRICE = 112600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1127:
    PREFAB_ID = "item_prefab_1127"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1127"
    EQUIPMENT_SLOT = "Head" if 1127 % 4 == 0 else ("Chest" if 1127 % 4 == 1 else ("Weapon" if 1127 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 13524
    REQUIRE_LEVEL = 23
    SELL_PRICE = 112700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1128:
    PREFAB_ID = "item_prefab_1128"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1128"
    EQUIPMENT_SLOT = "Head" if 1128 % 4 == 0 else ("Chest" if 1128 % 4 == 1 else ("Weapon" if 1128 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 13536
    REQUIRE_LEVEL = 23
    SELL_PRICE = 112800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1129:
    PREFAB_ID = "item_prefab_1129"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1129"
    EQUIPMENT_SLOT = "Head" if 1129 % 4 == 0 else ("Chest" if 1129 % 4 == 1 else ("Weapon" if 1129 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 13548
    REQUIRE_LEVEL = 23
    SELL_PRICE = 112900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1130:
    PREFAB_ID = "item_prefab_1130"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1130"
    EQUIPMENT_SLOT = "Head" if 1130 % 4 == 0 else ("Chest" if 1130 % 4 == 1 else ("Weapon" if 1130 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 13560
    REQUIRE_LEVEL = 23
    SELL_PRICE = 113000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1131:
    PREFAB_ID = "item_prefab_1131"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1131"
    EQUIPMENT_SLOT = "Head" if 1131 % 4 == 0 else ("Chest" if 1131 % 4 == 1 else ("Weapon" if 1131 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 13572
    REQUIRE_LEVEL = 23
    SELL_PRICE = 113100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1132:
    PREFAB_ID = "item_prefab_1132"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1132"
    EQUIPMENT_SLOT = "Head" if 1132 % 4 == 0 else ("Chest" if 1132 % 4 == 1 else ("Weapon" if 1132 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 13584
    REQUIRE_LEVEL = 23
    SELL_PRICE = 113200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1133:
    PREFAB_ID = "item_prefab_1133"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1133"
    EQUIPMENT_SLOT = "Head" if 1133 % 4 == 0 else ("Chest" if 1133 % 4 == 1 else ("Weapon" if 1133 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 13596
    REQUIRE_LEVEL = 23
    SELL_PRICE = 113300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1134:
    PREFAB_ID = "item_prefab_1134"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1134"
    EQUIPMENT_SLOT = "Head" if 1134 % 4 == 0 else ("Chest" if 1134 % 4 == 1 else ("Weapon" if 1134 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 13608
    REQUIRE_LEVEL = 23
    SELL_PRICE = 113400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1135:
    PREFAB_ID = "item_prefab_1135"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1135"
    EQUIPMENT_SLOT = "Head" if 1135 % 4 == 0 else ("Chest" if 1135 % 4 == 1 else ("Weapon" if 1135 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 13620
    REQUIRE_LEVEL = 23
    SELL_PRICE = 113500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1136:
    PREFAB_ID = "item_prefab_1136"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1136"
    EQUIPMENT_SLOT = "Head" if 1136 % 4 == 0 else ("Chest" if 1136 % 4 == 1 else ("Weapon" if 1136 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 13632
    REQUIRE_LEVEL = 23
    SELL_PRICE = 113600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1137:
    PREFAB_ID = "item_prefab_1137"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1137"
    EQUIPMENT_SLOT = "Head" if 1137 % 4 == 0 else ("Chest" if 1137 % 4 == 1 else ("Weapon" if 1137 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 13644
    REQUIRE_LEVEL = 23
    SELL_PRICE = 113700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1138:
    PREFAB_ID = "item_prefab_1138"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1138"
    EQUIPMENT_SLOT = "Head" if 1138 % 4 == 0 else ("Chest" if 1138 % 4 == 1 else ("Weapon" if 1138 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 13656
    REQUIRE_LEVEL = 23
    SELL_PRICE = 113800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1139:
    PREFAB_ID = "item_prefab_1139"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1139"
    EQUIPMENT_SLOT = "Head" if 1139 % 4 == 0 else ("Chest" if 1139 % 4 == 1 else ("Weapon" if 1139 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 13668
    REQUIRE_LEVEL = 23
    SELL_PRICE = 113900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1140:
    PREFAB_ID = "item_prefab_1140"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1140"
    EQUIPMENT_SLOT = "Head" if 1140 % 4 == 0 else ("Chest" if 1140 % 4 == 1 else ("Weapon" if 1140 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 13680
    REQUIRE_LEVEL = 23
    SELL_PRICE = 114000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1141:
    PREFAB_ID = "item_prefab_1141"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1141"
    EQUIPMENT_SLOT = "Head" if 1141 % 4 == 0 else ("Chest" if 1141 % 4 == 1 else ("Weapon" if 1141 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 13692
    REQUIRE_LEVEL = 23
    SELL_PRICE = 114100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1142:
    PREFAB_ID = "item_prefab_1142"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1142"
    EQUIPMENT_SLOT = "Head" if 1142 % 4 == 0 else ("Chest" if 1142 % 4 == 1 else ("Weapon" if 1142 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 13704
    REQUIRE_LEVEL = 23
    SELL_PRICE = 114200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1143:
    PREFAB_ID = "item_prefab_1143"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1143"
    EQUIPMENT_SLOT = "Head" if 1143 % 4 == 0 else ("Chest" if 1143 % 4 == 1 else ("Weapon" if 1143 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 13716
    REQUIRE_LEVEL = 23
    SELL_PRICE = 114300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1144:
    PREFAB_ID = "item_prefab_1144"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1144"
    EQUIPMENT_SLOT = "Head" if 1144 % 4 == 0 else ("Chest" if 1144 % 4 == 1 else ("Weapon" if 1144 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 13728
    REQUIRE_LEVEL = 23
    SELL_PRICE = 114400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1145:
    PREFAB_ID = "item_prefab_1145"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1145"
    EQUIPMENT_SLOT = "Head" if 1145 % 4 == 0 else ("Chest" if 1145 % 4 == 1 else ("Weapon" if 1145 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 13740
    REQUIRE_LEVEL = 23
    SELL_PRICE = 114500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1146:
    PREFAB_ID = "item_prefab_1146"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1146"
    EQUIPMENT_SLOT = "Head" if 1146 % 4 == 0 else ("Chest" if 1146 % 4 == 1 else ("Weapon" if 1146 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 13752
    REQUIRE_LEVEL = 23
    SELL_PRICE = 114600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1147:
    PREFAB_ID = "item_prefab_1147"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1147"
    EQUIPMENT_SLOT = "Head" if 1147 % 4 == 0 else ("Chest" if 1147 % 4 == 1 else ("Weapon" if 1147 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 13764
    REQUIRE_LEVEL = 23
    SELL_PRICE = 114700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1148:
    PREFAB_ID = "item_prefab_1148"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1148"
    EQUIPMENT_SLOT = "Head" if 1148 % 4 == 0 else ("Chest" if 1148 % 4 == 1 else ("Weapon" if 1148 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 13776
    REQUIRE_LEVEL = 23
    SELL_PRICE = 114800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1149:
    PREFAB_ID = "item_prefab_1149"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1149"
    EQUIPMENT_SLOT = "Head" if 1149 % 4 == 0 else ("Chest" if 1149 % 4 == 1 else ("Weapon" if 1149 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 13788
    REQUIRE_LEVEL = 23
    SELL_PRICE = 114900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1150:
    PREFAB_ID = "item_prefab_1150"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1150"
    EQUIPMENT_SLOT = "Head" if 1150 % 4 == 0 else ("Chest" if 1150 % 4 == 1 else ("Weapon" if 1150 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 13800
    REQUIRE_LEVEL = 24
    SELL_PRICE = 115000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1151:
    PREFAB_ID = "item_prefab_1151"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1151"
    EQUIPMENT_SLOT = "Head" if 1151 % 4 == 0 else ("Chest" if 1151 % 4 == 1 else ("Weapon" if 1151 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 13812
    REQUIRE_LEVEL = 24
    SELL_PRICE = 115100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1152:
    PREFAB_ID = "item_prefab_1152"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1152"
    EQUIPMENT_SLOT = "Head" if 1152 % 4 == 0 else ("Chest" if 1152 % 4 == 1 else ("Weapon" if 1152 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 13824
    REQUIRE_LEVEL = 24
    SELL_PRICE = 115200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1153:
    PREFAB_ID = "item_prefab_1153"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1153"
    EQUIPMENT_SLOT = "Head" if 1153 % 4 == 0 else ("Chest" if 1153 % 4 == 1 else ("Weapon" if 1153 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 13836
    REQUIRE_LEVEL = 24
    SELL_PRICE = 115300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1154:
    PREFAB_ID = "item_prefab_1154"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1154"
    EQUIPMENT_SLOT = "Head" if 1154 % 4 == 0 else ("Chest" if 1154 % 4 == 1 else ("Weapon" if 1154 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 13848
    REQUIRE_LEVEL = 24
    SELL_PRICE = 115400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1155:
    PREFAB_ID = "item_prefab_1155"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1155"
    EQUIPMENT_SLOT = "Head" if 1155 % 4 == 0 else ("Chest" if 1155 % 4 == 1 else ("Weapon" if 1155 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 13860
    REQUIRE_LEVEL = 24
    SELL_PRICE = 115500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1156:
    PREFAB_ID = "item_prefab_1156"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1156"
    EQUIPMENT_SLOT = "Head" if 1156 % 4 == 0 else ("Chest" if 1156 % 4 == 1 else ("Weapon" if 1156 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 13872
    REQUIRE_LEVEL = 24
    SELL_PRICE = 115600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1157:
    PREFAB_ID = "item_prefab_1157"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1157"
    EQUIPMENT_SLOT = "Head" if 1157 % 4 == 0 else ("Chest" if 1157 % 4 == 1 else ("Weapon" if 1157 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 13884
    REQUIRE_LEVEL = 24
    SELL_PRICE = 115700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1158:
    PREFAB_ID = "item_prefab_1158"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1158"
    EQUIPMENT_SLOT = "Head" if 1158 % 4 == 0 else ("Chest" if 1158 % 4 == 1 else ("Weapon" if 1158 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 13896
    REQUIRE_LEVEL = 24
    SELL_PRICE = 115800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1159:
    PREFAB_ID = "item_prefab_1159"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1159"
    EQUIPMENT_SLOT = "Head" if 1159 % 4 == 0 else ("Chest" if 1159 % 4 == 1 else ("Weapon" if 1159 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 13908
    REQUIRE_LEVEL = 24
    SELL_PRICE = 115900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1160:
    PREFAB_ID = "item_prefab_1160"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1160"
    EQUIPMENT_SLOT = "Head" if 1160 % 4 == 0 else ("Chest" if 1160 % 4 == 1 else ("Weapon" if 1160 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 13920
    REQUIRE_LEVEL = 24
    SELL_PRICE = 116000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1161:
    PREFAB_ID = "item_prefab_1161"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1161"
    EQUIPMENT_SLOT = "Head" if 1161 % 4 == 0 else ("Chest" if 1161 % 4 == 1 else ("Weapon" if 1161 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 13932
    REQUIRE_LEVEL = 24
    SELL_PRICE = 116100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1162:
    PREFAB_ID = "item_prefab_1162"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1162"
    EQUIPMENT_SLOT = "Head" if 1162 % 4 == 0 else ("Chest" if 1162 % 4 == 1 else ("Weapon" if 1162 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 13944
    REQUIRE_LEVEL = 24
    SELL_PRICE = 116200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1163:
    PREFAB_ID = "item_prefab_1163"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1163"
    EQUIPMENT_SLOT = "Head" if 1163 % 4 == 0 else ("Chest" if 1163 % 4 == 1 else ("Weapon" if 1163 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 13956
    REQUIRE_LEVEL = 24
    SELL_PRICE = 116300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1164:
    PREFAB_ID = "item_prefab_1164"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1164"
    EQUIPMENT_SLOT = "Head" if 1164 % 4 == 0 else ("Chest" if 1164 % 4 == 1 else ("Weapon" if 1164 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 13968
    REQUIRE_LEVEL = 24
    SELL_PRICE = 116400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1165:
    PREFAB_ID = "item_prefab_1165"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1165"
    EQUIPMENT_SLOT = "Head" if 1165 % 4 == 0 else ("Chest" if 1165 % 4 == 1 else ("Weapon" if 1165 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 13980
    REQUIRE_LEVEL = 24
    SELL_PRICE = 116500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1166:
    PREFAB_ID = "item_prefab_1166"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1166"
    EQUIPMENT_SLOT = "Head" if 1166 % 4 == 0 else ("Chest" if 1166 % 4 == 1 else ("Weapon" if 1166 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 13992
    REQUIRE_LEVEL = 24
    SELL_PRICE = 116600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1167:
    PREFAB_ID = "item_prefab_1167"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1167"
    EQUIPMENT_SLOT = "Head" if 1167 % 4 == 0 else ("Chest" if 1167 % 4 == 1 else ("Weapon" if 1167 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 14004
    REQUIRE_LEVEL = 24
    SELL_PRICE = 116700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1168:
    PREFAB_ID = "item_prefab_1168"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1168"
    EQUIPMENT_SLOT = "Head" if 1168 % 4 == 0 else ("Chest" if 1168 % 4 == 1 else ("Weapon" if 1168 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 14016
    REQUIRE_LEVEL = 24
    SELL_PRICE = 116800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1169:
    PREFAB_ID = "item_prefab_1169"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1169"
    EQUIPMENT_SLOT = "Head" if 1169 % 4 == 0 else ("Chest" if 1169 % 4 == 1 else ("Weapon" if 1169 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 14028
    REQUIRE_LEVEL = 24
    SELL_PRICE = 116900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1170:
    PREFAB_ID = "item_prefab_1170"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1170"
    EQUIPMENT_SLOT = "Head" if 1170 % 4 == 0 else ("Chest" if 1170 % 4 == 1 else ("Weapon" if 1170 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 14040
    REQUIRE_LEVEL = 24
    SELL_PRICE = 117000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1171:
    PREFAB_ID = "item_prefab_1171"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1171"
    EQUIPMENT_SLOT = "Head" if 1171 % 4 == 0 else ("Chest" if 1171 % 4 == 1 else ("Weapon" if 1171 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 14052
    REQUIRE_LEVEL = 24
    SELL_PRICE = 117100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1172:
    PREFAB_ID = "item_prefab_1172"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1172"
    EQUIPMENT_SLOT = "Head" if 1172 % 4 == 0 else ("Chest" if 1172 % 4 == 1 else ("Weapon" if 1172 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 14064
    REQUIRE_LEVEL = 24
    SELL_PRICE = 117200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1173:
    PREFAB_ID = "item_prefab_1173"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1173"
    EQUIPMENT_SLOT = "Head" if 1173 % 4 == 0 else ("Chest" if 1173 % 4 == 1 else ("Weapon" if 1173 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 14076
    REQUIRE_LEVEL = 24
    SELL_PRICE = 117300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1174:
    PREFAB_ID = "item_prefab_1174"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1174"
    EQUIPMENT_SLOT = "Head" if 1174 % 4 == 0 else ("Chest" if 1174 % 4 == 1 else ("Weapon" if 1174 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 14088
    REQUIRE_LEVEL = 24
    SELL_PRICE = 117400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1175:
    PREFAB_ID = "item_prefab_1175"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1175"
    EQUIPMENT_SLOT = "Head" if 1175 % 4 == 0 else ("Chest" if 1175 % 4 == 1 else ("Weapon" if 1175 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 14100
    REQUIRE_LEVEL = 24
    SELL_PRICE = 117500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1176:
    PREFAB_ID = "item_prefab_1176"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1176"
    EQUIPMENT_SLOT = "Head" if 1176 % 4 == 0 else ("Chest" if 1176 % 4 == 1 else ("Weapon" if 1176 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 14112
    REQUIRE_LEVEL = 24
    SELL_PRICE = 117600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1177:
    PREFAB_ID = "item_prefab_1177"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1177"
    EQUIPMENT_SLOT = "Head" if 1177 % 4 == 0 else ("Chest" if 1177 % 4 == 1 else ("Weapon" if 1177 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 14124
    REQUIRE_LEVEL = 24
    SELL_PRICE = 117700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1178:
    PREFAB_ID = "item_prefab_1178"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1178"
    EQUIPMENT_SLOT = "Head" if 1178 % 4 == 0 else ("Chest" if 1178 % 4 == 1 else ("Weapon" if 1178 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 14136
    REQUIRE_LEVEL = 24
    SELL_PRICE = 117800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1179:
    PREFAB_ID = "item_prefab_1179"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1179"
    EQUIPMENT_SLOT = "Head" if 1179 % 4 == 0 else ("Chest" if 1179 % 4 == 1 else ("Weapon" if 1179 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 14148
    REQUIRE_LEVEL = 24
    SELL_PRICE = 117900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1180:
    PREFAB_ID = "item_prefab_1180"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1180"
    EQUIPMENT_SLOT = "Head" if 1180 % 4 == 0 else ("Chest" if 1180 % 4 == 1 else ("Weapon" if 1180 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 14160
    REQUIRE_LEVEL = 24
    SELL_PRICE = 118000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1181:
    PREFAB_ID = "item_prefab_1181"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1181"
    EQUIPMENT_SLOT = "Head" if 1181 % 4 == 0 else ("Chest" if 1181 % 4 == 1 else ("Weapon" if 1181 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 14172
    REQUIRE_LEVEL = 24
    SELL_PRICE = 118100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1182:
    PREFAB_ID = "item_prefab_1182"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1182"
    EQUIPMENT_SLOT = "Head" if 1182 % 4 == 0 else ("Chest" if 1182 % 4 == 1 else ("Weapon" if 1182 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 14184
    REQUIRE_LEVEL = 24
    SELL_PRICE = 118200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1183:
    PREFAB_ID = "item_prefab_1183"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1183"
    EQUIPMENT_SLOT = "Head" if 1183 % 4 == 0 else ("Chest" if 1183 % 4 == 1 else ("Weapon" if 1183 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 14196
    REQUIRE_LEVEL = 24
    SELL_PRICE = 118300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1184:
    PREFAB_ID = "item_prefab_1184"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1184"
    EQUIPMENT_SLOT = "Head" if 1184 % 4 == 0 else ("Chest" if 1184 % 4 == 1 else ("Weapon" if 1184 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 14208
    REQUIRE_LEVEL = 24
    SELL_PRICE = 118400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1185:
    PREFAB_ID = "item_prefab_1185"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1185"
    EQUIPMENT_SLOT = "Head" if 1185 % 4 == 0 else ("Chest" if 1185 % 4 == 1 else ("Weapon" if 1185 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 14220
    REQUIRE_LEVEL = 24
    SELL_PRICE = 118500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1186:
    PREFAB_ID = "item_prefab_1186"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1186"
    EQUIPMENT_SLOT = "Head" if 1186 % 4 == 0 else ("Chest" if 1186 % 4 == 1 else ("Weapon" if 1186 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 14232
    REQUIRE_LEVEL = 24
    SELL_PRICE = 118600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1187:
    PREFAB_ID = "item_prefab_1187"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1187"
    EQUIPMENT_SLOT = "Head" if 1187 % 4 == 0 else ("Chest" if 1187 % 4 == 1 else ("Weapon" if 1187 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 14244
    REQUIRE_LEVEL = 24
    SELL_PRICE = 118700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1188:
    PREFAB_ID = "item_prefab_1188"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1188"
    EQUIPMENT_SLOT = "Head" if 1188 % 4 == 0 else ("Chest" if 1188 % 4 == 1 else ("Weapon" if 1188 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 14256
    REQUIRE_LEVEL = 24
    SELL_PRICE = 118800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1189:
    PREFAB_ID = "item_prefab_1189"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1189"
    EQUIPMENT_SLOT = "Head" if 1189 % 4 == 0 else ("Chest" if 1189 % 4 == 1 else ("Weapon" if 1189 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 14268
    REQUIRE_LEVEL = 24
    SELL_PRICE = 118900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1190:
    PREFAB_ID = "item_prefab_1190"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1190"
    EQUIPMENT_SLOT = "Head" if 1190 % 4 == 0 else ("Chest" if 1190 % 4 == 1 else ("Weapon" if 1190 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 14280
    REQUIRE_LEVEL = 24
    SELL_PRICE = 119000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1191:
    PREFAB_ID = "item_prefab_1191"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1191"
    EQUIPMENT_SLOT = "Head" if 1191 % 4 == 0 else ("Chest" if 1191 % 4 == 1 else ("Weapon" if 1191 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 14292
    REQUIRE_LEVEL = 24
    SELL_PRICE = 119100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1192:
    PREFAB_ID = "item_prefab_1192"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1192"
    EQUIPMENT_SLOT = "Head" if 1192 % 4 == 0 else ("Chest" if 1192 % 4 == 1 else ("Weapon" if 1192 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 14304
    REQUIRE_LEVEL = 24
    SELL_PRICE = 119200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1193:
    PREFAB_ID = "item_prefab_1193"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1193"
    EQUIPMENT_SLOT = "Head" if 1193 % 4 == 0 else ("Chest" if 1193 % 4 == 1 else ("Weapon" if 1193 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 14316
    REQUIRE_LEVEL = 24
    SELL_PRICE = 119300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1194:
    PREFAB_ID = "item_prefab_1194"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1194"
    EQUIPMENT_SLOT = "Head" if 1194 % 4 == 0 else ("Chest" if 1194 % 4 == 1 else ("Weapon" if 1194 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 14328
    REQUIRE_LEVEL = 24
    SELL_PRICE = 119400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1195:
    PREFAB_ID = "item_prefab_1195"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1195"
    EQUIPMENT_SLOT = "Head" if 1195 % 4 == 0 else ("Chest" if 1195 % 4 == 1 else ("Weapon" if 1195 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 14340
    REQUIRE_LEVEL = 24
    SELL_PRICE = 119500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1196:
    PREFAB_ID = "item_prefab_1196"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1196"
    EQUIPMENT_SLOT = "Head" if 1196 % 4 == 0 else ("Chest" if 1196 % 4 == 1 else ("Weapon" if 1196 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 14352
    REQUIRE_LEVEL = 24
    SELL_PRICE = 119600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1197:
    PREFAB_ID = "item_prefab_1197"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1197"
    EQUIPMENT_SLOT = "Head" if 1197 % 4 == 0 else ("Chest" if 1197 % 4 == 1 else ("Weapon" if 1197 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 14364
    REQUIRE_LEVEL = 24
    SELL_PRICE = 119700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1198:
    PREFAB_ID = "item_prefab_1198"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1198"
    EQUIPMENT_SLOT = "Head" if 1198 % 4 == 0 else ("Chest" if 1198 % 4 == 1 else ("Weapon" if 1198 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 14376
    REQUIRE_LEVEL = 24
    SELL_PRICE = 119800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1199:
    PREFAB_ID = "item_prefab_1199"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1199"
    EQUIPMENT_SLOT = "Head" if 1199 % 4 == 0 else ("Chest" if 1199 % 4 == 1 else ("Weapon" if 1199 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 14388
    REQUIRE_LEVEL = 24
    SELL_PRICE = 119900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1200:
    PREFAB_ID = "item_prefab_1200"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1200"
    EQUIPMENT_SLOT = "Head" if 1200 % 4 == 0 else ("Chest" if 1200 % 4 == 1 else ("Weapon" if 1200 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 14400
    REQUIRE_LEVEL = 25
    SELL_PRICE = 120000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1201:
    PREFAB_ID = "item_prefab_1201"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1201"
    EQUIPMENT_SLOT = "Head" if 1201 % 4 == 0 else ("Chest" if 1201 % 4 == 1 else ("Weapon" if 1201 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 14412
    REQUIRE_LEVEL = 25
    SELL_PRICE = 120100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1202:
    PREFAB_ID = "item_prefab_1202"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1202"
    EQUIPMENT_SLOT = "Head" if 1202 % 4 == 0 else ("Chest" if 1202 % 4 == 1 else ("Weapon" if 1202 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 14424
    REQUIRE_LEVEL = 25
    SELL_PRICE = 120200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1203:
    PREFAB_ID = "item_prefab_1203"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1203"
    EQUIPMENT_SLOT = "Head" if 1203 % 4 == 0 else ("Chest" if 1203 % 4 == 1 else ("Weapon" if 1203 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 14436
    REQUIRE_LEVEL = 25
    SELL_PRICE = 120300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1204:
    PREFAB_ID = "item_prefab_1204"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1204"
    EQUIPMENT_SLOT = "Head" if 1204 % 4 == 0 else ("Chest" if 1204 % 4 == 1 else ("Weapon" if 1204 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 14448
    REQUIRE_LEVEL = 25
    SELL_PRICE = 120400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1205:
    PREFAB_ID = "item_prefab_1205"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1205"
    EQUIPMENT_SLOT = "Head" if 1205 % 4 == 0 else ("Chest" if 1205 % 4 == 1 else ("Weapon" if 1205 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 14460
    REQUIRE_LEVEL = 25
    SELL_PRICE = 120500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1206:
    PREFAB_ID = "item_prefab_1206"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1206"
    EQUIPMENT_SLOT = "Head" if 1206 % 4 == 0 else ("Chest" if 1206 % 4 == 1 else ("Weapon" if 1206 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 14472
    REQUIRE_LEVEL = 25
    SELL_PRICE = 120600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1207:
    PREFAB_ID = "item_prefab_1207"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1207"
    EQUIPMENT_SLOT = "Head" if 1207 % 4 == 0 else ("Chest" if 1207 % 4 == 1 else ("Weapon" if 1207 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 14484
    REQUIRE_LEVEL = 25
    SELL_PRICE = 120700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1208:
    PREFAB_ID = "item_prefab_1208"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1208"
    EQUIPMENT_SLOT = "Head" if 1208 % 4 == 0 else ("Chest" if 1208 % 4 == 1 else ("Weapon" if 1208 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 14496
    REQUIRE_LEVEL = 25
    SELL_PRICE = 120800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1209:
    PREFAB_ID = "item_prefab_1209"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1209"
    EQUIPMENT_SLOT = "Head" if 1209 % 4 == 0 else ("Chest" if 1209 % 4 == 1 else ("Weapon" if 1209 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 14508
    REQUIRE_LEVEL = 25
    SELL_PRICE = 120900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1210:
    PREFAB_ID = "item_prefab_1210"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1210"
    EQUIPMENT_SLOT = "Head" if 1210 % 4 == 0 else ("Chest" if 1210 % 4 == 1 else ("Weapon" if 1210 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 14520
    REQUIRE_LEVEL = 25
    SELL_PRICE = 121000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1211:
    PREFAB_ID = "item_prefab_1211"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1211"
    EQUIPMENT_SLOT = "Head" if 1211 % 4 == 0 else ("Chest" if 1211 % 4 == 1 else ("Weapon" if 1211 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 14532
    REQUIRE_LEVEL = 25
    SELL_PRICE = 121100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1212:
    PREFAB_ID = "item_prefab_1212"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1212"
    EQUIPMENT_SLOT = "Head" if 1212 % 4 == 0 else ("Chest" if 1212 % 4 == 1 else ("Weapon" if 1212 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 14544
    REQUIRE_LEVEL = 25
    SELL_PRICE = 121200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1213:
    PREFAB_ID = "item_prefab_1213"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1213"
    EQUIPMENT_SLOT = "Head" if 1213 % 4 == 0 else ("Chest" if 1213 % 4 == 1 else ("Weapon" if 1213 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 14556
    REQUIRE_LEVEL = 25
    SELL_PRICE = 121300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1214:
    PREFAB_ID = "item_prefab_1214"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1214"
    EQUIPMENT_SLOT = "Head" if 1214 % 4 == 0 else ("Chest" if 1214 % 4 == 1 else ("Weapon" if 1214 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 14568
    REQUIRE_LEVEL = 25
    SELL_PRICE = 121400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1215:
    PREFAB_ID = "item_prefab_1215"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1215"
    EQUIPMENT_SLOT = "Head" if 1215 % 4 == 0 else ("Chest" if 1215 % 4 == 1 else ("Weapon" if 1215 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 14580
    REQUIRE_LEVEL = 25
    SELL_PRICE = 121500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1216:
    PREFAB_ID = "item_prefab_1216"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1216"
    EQUIPMENT_SLOT = "Head" if 1216 % 4 == 0 else ("Chest" if 1216 % 4 == 1 else ("Weapon" if 1216 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 14592
    REQUIRE_LEVEL = 25
    SELL_PRICE = 121600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1217:
    PREFAB_ID = "item_prefab_1217"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1217"
    EQUIPMENT_SLOT = "Head" if 1217 % 4 == 0 else ("Chest" if 1217 % 4 == 1 else ("Weapon" if 1217 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 14604
    REQUIRE_LEVEL = 25
    SELL_PRICE = 121700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1218:
    PREFAB_ID = "item_prefab_1218"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1218"
    EQUIPMENT_SLOT = "Head" if 1218 % 4 == 0 else ("Chest" if 1218 % 4 == 1 else ("Weapon" if 1218 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 14616
    REQUIRE_LEVEL = 25
    SELL_PRICE = 121800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1219:
    PREFAB_ID = "item_prefab_1219"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1219"
    EQUIPMENT_SLOT = "Head" if 1219 % 4 == 0 else ("Chest" if 1219 % 4 == 1 else ("Weapon" if 1219 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 14628
    REQUIRE_LEVEL = 25
    SELL_PRICE = 121900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1220:
    PREFAB_ID = "item_prefab_1220"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1220"
    EQUIPMENT_SLOT = "Head" if 1220 % 4 == 0 else ("Chest" if 1220 % 4 == 1 else ("Weapon" if 1220 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 14640
    REQUIRE_LEVEL = 25
    SELL_PRICE = 122000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1221:
    PREFAB_ID = "item_prefab_1221"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1221"
    EQUIPMENT_SLOT = "Head" if 1221 % 4 == 0 else ("Chest" if 1221 % 4 == 1 else ("Weapon" if 1221 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 14652
    REQUIRE_LEVEL = 25
    SELL_PRICE = 122100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1222:
    PREFAB_ID = "item_prefab_1222"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1222"
    EQUIPMENT_SLOT = "Head" if 1222 % 4 == 0 else ("Chest" if 1222 % 4 == 1 else ("Weapon" if 1222 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 14664
    REQUIRE_LEVEL = 25
    SELL_PRICE = 122200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1223:
    PREFAB_ID = "item_prefab_1223"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1223"
    EQUIPMENT_SLOT = "Head" if 1223 % 4 == 0 else ("Chest" if 1223 % 4 == 1 else ("Weapon" if 1223 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 14676
    REQUIRE_LEVEL = 25
    SELL_PRICE = 122300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1224:
    PREFAB_ID = "item_prefab_1224"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1224"
    EQUIPMENT_SLOT = "Head" if 1224 % 4 == 0 else ("Chest" if 1224 % 4 == 1 else ("Weapon" if 1224 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 14688
    REQUIRE_LEVEL = 25
    SELL_PRICE = 122400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1225:
    PREFAB_ID = "item_prefab_1225"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1225"
    EQUIPMENT_SLOT = "Head" if 1225 % 4 == 0 else ("Chest" if 1225 % 4 == 1 else ("Weapon" if 1225 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 14700
    REQUIRE_LEVEL = 25
    SELL_PRICE = 122500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1226:
    PREFAB_ID = "item_prefab_1226"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1226"
    EQUIPMENT_SLOT = "Head" if 1226 % 4 == 0 else ("Chest" if 1226 % 4 == 1 else ("Weapon" if 1226 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 14712
    REQUIRE_LEVEL = 25
    SELL_PRICE = 122600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1227:
    PREFAB_ID = "item_prefab_1227"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1227"
    EQUIPMENT_SLOT = "Head" if 1227 % 4 == 0 else ("Chest" if 1227 % 4 == 1 else ("Weapon" if 1227 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 14724
    REQUIRE_LEVEL = 25
    SELL_PRICE = 122700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1228:
    PREFAB_ID = "item_prefab_1228"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1228"
    EQUIPMENT_SLOT = "Head" if 1228 % 4 == 0 else ("Chest" if 1228 % 4 == 1 else ("Weapon" if 1228 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 14736
    REQUIRE_LEVEL = 25
    SELL_PRICE = 122800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1229:
    PREFAB_ID = "item_prefab_1229"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1229"
    EQUIPMENT_SLOT = "Head" if 1229 % 4 == 0 else ("Chest" if 1229 % 4 == 1 else ("Weapon" if 1229 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 14748
    REQUIRE_LEVEL = 25
    SELL_PRICE = 122900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1230:
    PREFAB_ID = "item_prefab_1230"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1230"
    EQUIPMENT_SLOT = "Head" if 1230 % 4 == 0 else ("Chest" if 1230 % 4 == 1 else ("Weapon" if 1230 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 14760
    REQUIRE_LEVEL = 25
    SELL_PRICE = 123000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1231:
    PREFAB_ID = "item_prefab_1231"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1231"
    EQUIPMENT_SLOT = "Head" if 1231 % 4 == 0 else ("Chest" if 1231 % 4 == 1 else ("Weapon" if 1231 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 14772
    REQUIRE_LEVEL = 25
    SELL_PRICE = 123100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1232:
    PREFAB_ID = "item_prefab_1232"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1232"
    EQUIPMENT_SLOT = "Head" if 1232 % 4 == 0 else ("Chest" if 1232 % 4 == 1 else ("Weapon" if 1232 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 14784
    REQUIRE_LEVEL = 25
    SELL_PRICE = 123200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1233:
    PREFAB_ID = "item_prefab_1233"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1233"
    EQUIPMENT_SLOT = "Head" if 1233 % 4 == 0 else ("Chest" if 1233 % 4 == 1 else ("Weapon" if 1233 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 14796
    REQUIRE_LEVEL = 25
    SELL_PRICE = 123300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1234:
    PREFAB_ID = "item_prefab_1234"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1234"
    EQUIPMENT_SLOT = "Head" if 1234 % 4 == 0 else ("Chest" if 1234 % 4 == 1 else ("Weapon" if 1234 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 14808
    REQUIRE_LEVEL = 25
    SELL_PRICE = 123400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1235:
    PREFAB_ID = "item_prefab_1235"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1235"
    EQUIPMENT_SLOT = "Head" if 1235 % 4 == 0 else ("Chest" if 1235 % 4 == 1 else ("Weapon" if 1235 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 14820
    REQUIRE_LEVEL = 25
    SELL_PRICE = 123500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1236:
    PREFAB_ID = "item_prefab_1236"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1236"
    EQUIPMENT_SLOT = "Head" if 1236 % 4 == 0 else ("Chest" if 1236 % 4 == 1 else ("Weapon" if 1236 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 14832
    REQUIRE_LEVEL = 25
    SELL_PRICE = 123600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1237:
    PREFAB_ID = "item_prefab_1237"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1237"
    EQUIPMENT_SLOT = "Head" if 1237 % 4 == 0 else ("Chest" if 1237 % 4 == 1 else ("Weapon" if 1237 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 14844
    REQUIRE_LEVEL = 25
    SELL_PRICE = 123700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1238:
    PREFAB_ID = "item_prefab_1238"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1238"
    EQUIPMENT_SLOT = "Head" if 1238 % 4 == 0 else ("Chest" if 1238 % 4 == 1 else ("Weapon" if 1238 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 14856
    REQUIRE_LEVEL = 25
    SELL_PRICE = 123800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1239:
    PREFAB_ID = "item_prefab_1239"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1239"
    EQUIPMENT_SLOT = "Head" if 1239 % 4 == 0 else ("Chest" if 1239 % 4 == 1 else ("Weapon" if 1239 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 14868
    REQUIRE_LEVEL = 25
    SELL_PRICE = 123900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1240:
    PREFAB_ID = "item_prefab_1240"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1240"
    EQUIPMENT_SLOT = "Head" if 1240 % 4 == 0 else ("Chest" if 1240 % 4 == 1 else ("Weapon" if 1240 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 14880
    REQUIRE_LEVEL = 25
    SELL_PRICE = 124000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1241:
    PREFAB_ID = "item_prefab_1241"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1241"
    EQUIPMENT_SLOT = "Head" if 1241 % 4 == 0 else ("Chest" if 1241 % 4 == 1 else ("Weapon" if 1241 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 14892
    REQUIRE_LEVEL = 25
    SELL_PRICE = 124100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1242:
    PREFAB_ID = "item_prefab_1242"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1242"
    EQUIPMENT_SLOT = "Head" if 1242 % 4 == 0 else ("Chest" if 1242 % 4 == 1 else ("Weapon" if 1242 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 14904
    REQUIRE_LEVEL = 25
    SELL_PRICE = 124200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1243:
    PREFAB_ID = "item_prefab_1243"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1243"
    EQUIPMENT_SLOT = "Head" if 1243 % 4 == 0 else ("Chest" if 1243 % 4 == 1 else ("Weapon" if 1243 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 14916
    REQUIRE_LEVEL = 25
    SELL_PRICE = 124300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1244:
    PREFAB_ID = "item_prefab_1244"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1244"
    EQUIPMENT_SLOT = "Head" if 1244 % 4 == 0 else ("Chest" if 1244 % 4 == 1 else ("Weapon" if 1244 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 14928
    REQUIRE_LEVEL = 25
    SELL_PRICE = 124400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1245:
    PREFAB_ID = "item_prefab_1245"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1245"
    EQUIPMENT_SLOT = "Head" if 1245 % 4 == 0 else ("Chest" if 1245 % 4 == 1 else ("Weapon" if 1245 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 14940
    REQUIRE_LEVEL = 25
    SELL_PRICE = 124500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1246:
    PREFAB_ID = "item_prefab_1246"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1246"
    EQUIPMENT_SLOT = "Head" if 1246 % 4 == 0 else ("Chest" if 1246 % 4 == 1 else ("Weapon" if 1246 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 14952
    REQUIRE_LEVEL = 25
    SELL_PRICE = 124600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1247:
    PREFAB_ID = "item_prefab_1247"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1247"
    EQUIPMENT_SLOT = "Head" if 1247 % 4 == 0 else ("Chest" if 1247 % 4 == 1 else ("Weapon" if 1247 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 14964
    REQUIRE_LEVEL = 25
    SELL_PRICE = 124700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1248:
    PREFAB_ID = "item_prefab_1248"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1248"
    EQUIPMENT_SLOT = "Head" if 1248 % 4 == 0 else ("Chest" if 1248 % 4 == 1 else ("Weapon" if 1248 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 14976
    REQUIRE_LEVEL = 25
    SELL_PRICE = 124800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1249:
    PREFAB_ID = "item_prefab_1249"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1249"
    EQUIPMENT_SLOT = "Head" if 1249 % 4 == 0 else ("Chest" if 1249 % 4 == 1 else ("Weapon" if 1249 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 14988
    REQUIRE_LEVEL = 25
    SELL_PRICE = 124900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1250:
    PREFAB_ID = "item_prefab_1250"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1250"
    EQUIPMENT_SLOT = "Head" if 1250 % 4 == 0 else ("Chest" if 1250 % 4 == 1 else ("Weapon" if 1250 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 15000
    REQUIRE_LEVEL = 26
    SELL_PRICE = 125000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1251:
    PREFAB_ID = "item_prefab_1251"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1251"
    EQUIPMENT_SLOT = "Head" if 1251 % 4 == 0 else ("Chest" if 1251 % 4 == 1 else ("Weapon" if 1251 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 15012
    REQUIRE_LEVEL = 26
    SELL_PRICE = 125100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1252:
    PREFAB_ID = "item_prefab_1252"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1252"
    EQUIPMENT_SLOT = "Head" if 1252 % 4 == 0 else ("Chest" if 1252 % 4 == 1 else ("Weapon" if 1252 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 15024
    REQUIRE_LEVEL = 26
    SELL_PRICE = 125200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1253:
    PREFAB_ID = "item_prefab_1253"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1253"
    EQUIPMENT_SLOT = "Head" if 1253 % 4 == 0 else ("Chest" if 1253 % 4 == 1 else ("Weapon" if 1253 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 15036
    REQUIRE_LEVEL = 26
    SELL_PRICE = 125300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1254:
    PREFAB_ID = "item_prefab_1254"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1254"
    EQUIPMENT_SLOT = "Head" if 1254 % 4 == 0 else ("Chest" if 1254 % 4 == 1 else ("Weapon" if 1254 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 15048
    REQUIRE_LEVEL = 26
    SELL_PRICE = 125400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1255:
    PREFAB_ID = "item_prefab_1255"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1255"
    EQUIPMENT_SLOT = "Head" if 1255 % 4 == 0 else ("Chest" if 1255 % 4 == 1 else ("Weapon" if 1255 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 15060
    REQUIRE_LEVEL = 26
    SELL_PRICE = 125500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1256:
    PREFAB_ID = "item_prefab_1256"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1256"
    EQUIPMENT_SLOT = "Head" if 1256 % 4 == 0 else ("Chest" if 1256 % 4 == 1 else ("Weapon" if 1256 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 15072
    REQUIRE_LEVEL = 26
    SELL_PRICE = 125600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1257:
    PREFAB_ID = "item_prefab_1257"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1257"
    EQUIPMENT_SLOT = "Head" if 1257 % 4 == 0 else ("Chest" if 1257 % 4 == 1 else ("Weapon" if 1257 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 15084
    REQUIRE_LEVEL = 26
    SELL_PRICE = 125700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1258:
    PREFAB_ID = "item_prefab_1258"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1258"
    EQUIPMENT_SLOT = "Head" if 1258 % 4 == 0 else ("Chest" if 1258 % 4 == 1 else ("Weapon" if 1258 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 15096
    REQUIRE_LEVEL = 26
    SELL_PRICE = 125800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1259:
    PREFAB_ID = "item_prefab_1259"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1259"
    EQUIPMENT_SLOT = "Head" if 1259 % 4 == 0 else ("Chest" if 1259 % 4 == 1 else ("Weapon" if 1259 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 15108
    REQUIRE_LEVEL = 26
    SELL_PRICE = 125900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1260:
    PREFAB_ID = "item_prefab_1260"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1260"
    EQUIPMENT_SLOT = "Head" if 1260 % 4 == 0 else ("Chest" if 1260 % 4 == 1 else ("Weapon" if 1260 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 15120
    REQUIRE_LEVEL = 26
    SELL_PRICE = 126000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1261:
    PREFAB_ID = "item_prefab_1261"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1261"
    EQUIPMENT_SLOT = "Head" if 1261 % 4 == 0 else ("Chest" if 1261 % 4 == 1 else ("Weapon" if 1261 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 15132
    REQUIRE_LEVEL = 26
    SELL_PRICE = 126100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1262:
    PREFAB_ID = "item_prefab_1262"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1262"
    EQUIPMENT_SLOT = "Head" if 1262 % 4 == 0 else ("Chest" if 1262 % 4 == 1 else ("Weapon" if 1262 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 15144
    REQUIRE_LEVEL = 26
    SELL_PRICE = 126200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1263:
    PREFAB_ID = "item_prefab_1263"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1263"
    EQUIPMENT_SLOT = "Head" if 1263 % 4 == 0 else ("Chest" if 1263 % 4 == 1 else ("Weapon" if 1263 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 15156
    REQUIRE_LEVEL = 26
    SELL_PRICE = 126300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1264:
    PREFAB_ID = "item_prefab_1264"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1264"
    EQUIPMENT_SLOT = "Head" if 1264 % 4 == 0 else ("Chest" if 1264 % 4 == 1 else ("Weapon" if 1264 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 15168
    REQUIRE_LEVEL = 26
    SELL_PRICE = 126400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1265:
    PREFAB_ID = "item_prefab_1265"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1265"
    EQUIPMENT_SLOT = "Head" if 1265 % 4 == 0 else ("Chest" if 1265 % 4 == 1 else ("Weapon" if 1265 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 15180
    REQUIRE_LEVEL = 26
    SELL_PRICE = 126500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1266:
    PREFAB_ID = "item_prefab_1266"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1266"
    EQUIPMENT_SLOT = "Head" if 1266 % 4 == 0 else ("Chest" if 1266 % 4 == 1 else ("Weapon" if 1266 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 15192
    REQUIRE_LEVEL = 26
    SELL_PRICE = 126600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1267:
    PREFAB_ID = "item_prefab_1267"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1267"
    EQUIPMENT_SLOT = "Head" if 1267 % 4 == 0 else ("Chest" if 1267 % 4 == 1 else ("Weapon" if 1267 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 15204
    REQUIRE_LEVEL = 26
    SELL_PRICE = 126700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1268:
    PREFAB_ID = "item_prefab_1268"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1268"
    EQUIPMENT_SLOT = "Head" if 1268 % 4 == 0 else ("Chest" if 1268 % 4 == 1 else ("Weapon" if 1268 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 15216
    REQUIRE_LEVEL = 26
    SELL_PRICE = 126800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1269:
    PREFAB_ID = "item_prefab_1269"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1269"
    EQUIPMENT_SLOT = "Head" if 1269 % 4 == 0 else ("Chest" if 1269 % 4 == 1 else ("Weapon" if 1269 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 15228
    REQUIRE_LEVEL = 26
    SELL_PRICE = 126900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1270:
    PREFAB_ID = "item_prefab_1270"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1270"
    EQUIPMENT_SLOT = "Head" if 1270 % 4 == 0 else ("Chest" if 1270 % 4 == 1 else ("Weapon" if 1270 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 15240
    REQUIRE_LEVEL = 26
    SELL_PRICE = 127000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1271:
    PREFAB_ID = "item_prefab_1271"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1271"
    EQUIPMENT_SLOT = "Head" if 1271 % 4 == 0 else ("Chest" if 1271 % 4 == 1 else ("Weapon" if 1271 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 15252
    REQUIRE_LEVEL = 26
    SELL_PRICE = 127100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1272:
    PREFAB_ID = "item_prefab_1272"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1272"
    EQUIPMENT_SLOT = "Head" if 1272 % 4 == 0 else ("Chest" if 1272 % 4 == 1 else ("Weapon" if 1272 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 15264
    REQUIRE_LEVEL = 26
    SELL_PRICE = 127200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1273:
    PREFAB_ID = "item_prefab_1273"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1273"
    EQUIPMENT_SLOT = "Head" if 1273 % 4 == 0 else ("Chest" if 1273 % 4 == 1 else ("Weapon" if 1273 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 15276
    REQUIRE_LEVEL = 26
    SELL_PRICE = 127300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1274:
    PREFAB_ID = "item_prefab_1274"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1274"
    EQUIPMENT_SLOT = "Head" if 1274 % 4 == 0 else ("Chest" if 1274 % 4 == 1 else ("Weapon" if 1274 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 15288
    REQUIRE_LEVEL = 26
    SELL_PRICE = 127400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1275:
    PREFAB_ID = "item_prefab_1275"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1275"
    EQUIPMENT_SLOT = "Head" if 1275 % 4 == 0 else ("Chest" if 1275 % 4 == 1 else ("Weapon" if 1275 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 15300
    REQUIRE_LEVEL = 26
    SELL_PRICE = 127500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1276:
    PREFAB_ID = "item_prefab_1276"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1276"
    EQUIPMENT_SLOT = "Head" if 1276 % 4 == 0 else ("Chest" if 1276 % 4 == 1 else ("Weapon" if 1276 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 15312
    REQUIRE_LEVEL = 26
    SELL_PRICE = 127600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1277:
    PREFAB_ID = "item_prefab_1277"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1277"
    EQUIPMENT_SLOT = "Head" if 1277 % 4 == 0 else ("Chest" if 1277 % 4 == 1 else ("Weapon" if 1277 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 15324
    REQUIRE_LEVEL = 26
    SELL_PRICE = 127700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1278:
    PREFAB_ID = "item_prefab_1278"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1278"
    EQUIPMENT_SLOT = "Head" if 1278 % 4 == 0 else ("Chest" if 1278 % 4 == 1 else ("Weapon" if 1278 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 15336
    REQUIRE_LEVEL = 26
    SELL_PRICE = 127800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1279:
    PREFAB_ID = "item_prefab_1279"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1279"
    EQUIPMENT_SLOT = "Head" if 1279 % 4 == 0 else ("Chest" if 1279 % 4 == 1 else ("Weapon" if 1279 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 15348
    REQUIRE_LEVEL = 26
    SELL_PRICE = 127900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1280:
    PREFAB_ID = "item_prefab_1280"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1280"
    EQUIPMENT_SLOT = "Head" if 1280 % 4 == 0 else ("Chest" if 1280 % 4 == 1 else ("Weapon" if 1280 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 15360
    REQUIRE_LEVEL = 26
    SELL_PRICE = 128000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1281:
    PREFAB_ID = "item_prefab_1281"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1281"
    EQUIPMENT_SLOT = "Head" if 1281 % 4 == 0 else ("Chest" if 1281 % 4 == 1 else ("Weapon" if 1281 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 15372
    REQUIRE_LEVEL = 26
    SELL_PRICE = 128100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1282:
    PREFAB_ID = "item_prefab_1282"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1282"
    EQUIPMENT_SLOT = "Head" if 1282 % 4 == 0 else ("Chest" if 1282 % 4 == 1 else ("Weapon" if 1282 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 15384
    REQUIRE_LEVEL = 26
    SELL_PRICE = 128200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1283:
    PREFAB_ID = "item_prefab_1283"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1283"
    EQUIPMENT_SLOT = "Head" if 1283 % 4 == 0 else ("Chest" if 1283 % 4 == 1 else ("Weapon" if 1283 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 15396
    REQUIRE_LEVEL = 26
    SELL_PRICE = 128300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1284:
    PREFAB_ID = "item_prefab_1284"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1284"
    EQUIPMENT_SLOT = "Head" if 1284 % 4 == 0 else ("Chest" if 1284 % 4 == 1 else ("Weapon" if 1284 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 15408
    REQUIRE_LEVEL = 26
    SELL_PRICE = 128400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1285:
    PREFAB_ID = "item_prefab_1285"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1285"
    EQUIPMENT_SLOT = "Head" if 1285 % 4 == 0 else ("Chest" if 1285 % 4 == 1 else ("Weapon" if 1285 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 15420
    REQUIRE_LEVEL = 26
    SELL_PRICE = 128500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1286:
    PREFAB_ID = "item_prefab_1286"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1286"
    EQUIPMENT_SLOT = "Head" if 1286 % 4 == 0 else ("Chest" if 1286 % 4 == 1 else ("Weapon" if 1286 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 15432
    REQUIRE_LEVEL = 26
    SELL_PRICE = 128600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1287:
    PREFAB_ID = "item_prefab_1287"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1287"
    EQUIPMENT_SLOT = "Head" if 1287 % 4 == 0 else ("Chest" if 1287 % 4 == 1 else ("Weapon" if 1287 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 15444
    REQUIRE_LEVEL = 26
    SELL_PRICE = 128700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1288:
    PREFAB_ID = "item_prefab_1288"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1288"
    EQUIPMENT_SLOT = "Head" if 1288 % 4 == 0 else ("Chest" if 1288 % 4 == 1 else ("Weapon" if 1288 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 15456
    REQUIRE_LEVEL = 26
    SELL_PRICE = 128800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1289:
    PREFAB_ID = "item_prefab_1289"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1289"
    EQUIPMENT_SLOT = "Head" if 1289 % 4 == 0 else ("Chest" if 1289 % 4 == 1 else ("Weapon" if 1289 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 15468
    REQUIRE_LEVEL = 26
    SELL_PRICE = 128900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1290:
    PREFAB_ID = "item_prefab_1290"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1290"
    EQUIPMENT_SLOT = "Head" if 1290 % 4 == 0 else ("Chest" if 1290 % 4 == 1 else ("Weapon" if 1290 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 15480
    REQUIRE_LEVEL = 26
    SELL_PRICE = 129000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1291:
    PREFAB_ID = "item_prefab_1291"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1291"
    EQUIPMENT_SLOT = "Head" if 1291 % 4 == 0 else ("Chest" if 1291 % 4 == 1 else ("Weapon" if 1291 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 15492
    REQUIRE_LEVEL = 26
    SELL_PRICE = 129100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1292:
    PREFAB_ID = "item_prefab_1292"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1292"
    EQUIPMENT_SLOT = "Head" if 1292 % 4 == 0 else ("Chest" if 1292 % 4 == 1 else ("Weapon" if 1292 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 15504
    REQUIRE_LEVEL = 26
    SELL_PRICE = 129200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1293:
    PREFAB_ID = "item_prefab_1293"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1293"
    EQUIPMENT_SLOT = "Head" if 1293 % 4 == 0 else ("Chest" if 1293 % 4 == 1 else ("Weapon" if 1293 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 15516
    REQUIRE_LEVEL = 26
    SELL_PRICE = 129300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1294:
    PREFAB_ID = "item_prefab_1294"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1294"
    EQUIPMENT_SLOT = "Head" if 1294 % 4 == 0 else ("Chest" if 1294 % 4 == 1 else ("Weapon" if 1294 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 15528
    REQUIRE_LEVEL = 26
    SELL_PRICE = 129400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1295:
    PREFAB_ID = "item_prefab_1295"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1295"
    EQUIPMENT_SLOT = "Head" if 1295 % 4 == 0 else ("Chest" if 1295 % 4 == 1 else ("Weapon" if 1295 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 15540
    REQUIRE_LEVEL = 26
    SELL_PRICE = 129500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1296:
    PREFAB_ID = "item_prefab_1296"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1296"
    EQUIPMENT_SLOT = "Head" if 1296 % 4 == 0 else ("Chest" if 1296 % 4 == 1 else ("Weapon" if 1296 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 15552
    REQUIRE_LEVEL = 26
    SELL_PRICE = 129600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1297:
    PREFAB_ID = "item_prefab_1297"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1297"
    EQUIPMENT_SLOT = "Head" if 1297 % 4 == 0 else ("Chest" if 1297 % 4 == 1 else ("Weapon" if 1297 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 15564
    REQUIRE_LEVEL = 26
    SELL_PRICE = 129700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1298:
    PREFAB_ID = "item_prefab_1298"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1298"
    EQUIPMENT_SLOT = "Head" if 1298 % 4 == 0 else ("Chest" if 1298 % 4 == 1 else ("Weapon" if 1298 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 15576
    REQUIRE_LEVEL = 26
    SELL_PRICE = 129800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1299:
    PREFAB_ID = "item_prefab_1299"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1299"
    EQUIPMENT_SLOT = "Head" if 1299 % 4 == 0 else ("Chest" if 1299 % 4 == 1 else ("Weapon" if 1299 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 15588
    REQUIRE_LEVEL = 26
    SELL_PRICE = 129900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1300:
    PREFAB_ID = "item_prefab_1300"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1300"
    EQUIPMENT_SLOT = "Head" if 1300 % 4 == 0 else ("Chest" if 1300 % 4 == 1 else ("Weapon" if 1300 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 15600
    REQUIRE_LEVEL = 27
    SELL_PRICE = 130000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1301:
    PREFAB_ID = "item_prefab_1301"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1301"
    EQUIPMENT_SLOT = "Head" if 1301 % 4 == 0 else ("Chest" if 1301 % 4 == 1 else ("Weapon" if 1301 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 15612
    REQUIRE_LEVEL = 27
    SELL_PRICE = 130100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1302:
    PREFAB_ID = "item_prefab_1302"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1302"
    EQUIPMENT_SLOT = "Head" if 1302 % 4 == 0 else ("Chest" if 1302 % 4 == 1 else ("Weapon" if 1302 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 15624
    REQUIRE_LEVEL = 27
    SELL_PRICE = 130200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1303:
    PREFAB_ID = "item_prefab_1303"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1303"
    EQUIPMENT_SLOT = "Head" if 1303 % 4 == 0 else ("Chest" if 1303 % 4 == 1 else ("Weapon" if 1303 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 15636
    REQUIRE_LEVEL = 27
    SELL_PRICE = 130300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1304:
    PREFAB_ID = "item_prefab_1304"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1304"
    EQUIPMENT_SLOT = "Head" if 1304 % 4 == 0 else ("Chest" if 1304 % 4 == 1 else ("Weapon" if 1304 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 15648
    REQUIRE_LEVEL = 27
    SELL_PRICE = 130400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1305:
    PREFAB_ID = "item_prefab_1305"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1305"
    EQUIPMENT_SLOT = "Head" if 1305 % 4 == 0 else ("Chest" if 1305 % 4 == 1 else ("Weapon" if 1305 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 15660
    REQUIRE_LEVEL = 27
    SELL_PRICE = 130500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1306:
    PREFAB_ID = "item_prefab_1306"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1306"
    EQUIPMENT_SLOT = "Head" if 1306 % 4 == 0 else ("Chest" if 1306 % 4 == 1 else ("Weapon" if 1306 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 15672
    REQUIRE_LEVEL = 27
    SELL_PRICE = 130600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1307:
    PREFAB_ID = "item_prefab_1307"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1307"
    EQUIPMENT_SLOT = "Head" if 1307 % 4 == 0 else ("Chest" if 1307 % 4 == 1 else ("Weapon" if 1307 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 15684
    REQUIRE_LEVEL = 27
    SELL_PRICE = 130700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1308:
    PREFAB_ID = "item_prefab_1308"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1308"
    EQUIPMENT_SLOT = "Head" if 1308 % 4 == 0 else ("Chest" if 1308 % 4 == 1 else ("Weapon" if 1308 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 15696
    REQUIRE_LEVEL = 27
    SELL_PRICE = 130800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1309:
    PREFAB_ID = "item_prefab_1309"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1309"
    EQUIPMENT_SLOT = "Head" if 1309 % 4 == 0 else ("Chest" if 1309 % 4 == 1 else ("Weapon" if 1309 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 15708
    REQUIRE_LEVEL = 27
    SELL_PRICE = 130900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1310:
    PREFAB_ID = "item_prefab_1310"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1310"
    EQUIPMENT_SLOT = "Head" if 1310 % 4 == 0 else ("Chest" if 1310 % 4 == 1 else ("Weapon" if 1310 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 15720
    REQUIRE_LEVEL = 27
    SELL_PRICE = 131000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1311:
    PREFAB_ID = "item_prefab_1311"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1311"
    EQUIPMENT_SLOT = "Head" if 1311 % 4 == 0 else ("Chest" if 1311 % 4 == 1 else ("Weapon" if 1311 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 15732
    REQUIRE_LEVEL = 27
    SELL_PRICE = 131100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1312:
    PREFAB_ID = "item_prefab_1312"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1312"
    EQUIPMENT_SLOT = "Head" if 1312 % 4 == 0 else ("Chest" if 1312 % 4 == 1 else ("Weapon" if 1312 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 15744
    REQUIRE_LEVEL = 27
    SELL_PRICE = 131200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1313:
    PREFAB_ID = "item_prefab_1313"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1313"
    EQUIPMENT_SLOT = "Head" if 1313 % 4 == 0 else ("Chest" if 1313 % 4 == 1 else ("Weapon" if 1313 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 15756
    REQUIRE_LEVEL = 27
    SELL_PRICE = 131300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1314:
    PREFAB_ID = "item_prefab_1314"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1314"
    EQUIPMENT_SLOT = "Head" if 1314 % 4 == 0 else ("Chest" if 1314 % 4 == 1 else ("Weapon" if 1314 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 15768
    REQUIRE_LEVEL = 27
    SELL_PRICE = 131400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1315:
    PREFAB_ID = "item_prefab_1315"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1315"
    EQUIPMENT_SLOT = "Head" if 1315 % 4 == 0 else ("Chest" if 1315 % 4 == 1 else ("Weapon" if 1315 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 15780
    REQUIRE_LEVEL = 27
    SELL_PRICE = 131500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1316:
    PREFAB_ID = "item_prefab_1316"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1316"
    EQUIPMENT_SLOT = "Head" if 1316 % 4 == 0 else ("Chest" if 1316 % 4 == 1 else ("Weapon" if 1316 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 15792
    REQUIRE_LEVEL = 27
    SELL_PRICE = 131600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1317:
    PREFAB_ID = "item_prefab_1317"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1317"
    EQUIPMENT_SLOT = "Head" if 1317 % 4 == 0 else ("Chest" if 1317 % 4 == 1 else ("Weapon" if 1317 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 15804
    REQUIRE_LEVEL = 27
    SELL_PRICE = 131700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1318:
    PREFAB_ID = "item_prefab_1318"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1318"
    EQUIPMENT_SLOT = "Head" if 1318 % 4 == 0 else ("Chest" if 1318 % 4 == 1 else ("Weapon" if 1318 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 15816
    REQUIRE_LEVEL = 27
    SELL_PRICE = 131800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1319:
    PREFAB_ID = "item_prefab_1319"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1319"
    EQUIPMENT_SLOT = "Head" if 1319 % 4 == 0 else ("Chest" if 1319 % 4 == 1 else ("Weapon" if 1319 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 15828
    REQUIRE_LEVEL = 27
    SELL_PRICE = 131900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1320:
    PREFAB_ID = "item_prefab_1320"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1320"
    EQUIPMENT_SLOT = "Head" if 1320 % 4 == 0 else ("Chest" if 1320 % 4 == 1 else ("Weapon" if 1320 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 15840
    REQUIRE_LEVEL = 27
    SELL_PRICE = 132000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1321:
    PREFAB_ID = "item_prefab_1321"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1321"
    EQUIPMENT_SLOT = "Head" if 1321 % 4 == 0 else ("Chest" if 1321 % 4 == 1 else ("Weapon" if 1321 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 15852
    REQUIRE_LEVEL = 27
    SELL_PRICE = 132100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1322:
    PREFAB_ID = "item_prefab_1322"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1322"
    EQUIPMENT_SLOT = "Head" if 1322 % 4 == 0 else ("Chest" if 1322 % 4 == 1 else ("Weapon" if 1322 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 15864
    REQUIRE_LEVEL = 27
    SELL_PRICE = 132200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1323:
    PREFAB_ID = "item_prefab_1323"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1323"
    EQUIPMENT_SLOT = "Head" if 1323 % 4 == 0 else ("Chest" if 1323 % 4 == 1 else ("Weapon" if 1323 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 15876
    REQUIRE_LEVEL = 27
    SELL_PRICE = 132300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1324:
    PREFAB_ID = "item_prefab_1324"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1324"
    EQUIPMENT_SLOT = "Head" if 1324 % 4 == 0 else ("Chest" if 1324 % 4 == 1 else ("Weapon" if 1324 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 15888
    REQUIRE_LEVEL = 27
    SELL_PRICE = 132400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1325:
    PREFAB_ID = "item_prefab_1325"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1325"
    EQUIPMENT_SLOT = "Head" if 1325 % 4 == 0 else ("Chest" if 1325 % 4 == 1 else ("Weapon" if 1325 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 15900
    REQUIRE_LEVEL = 27
    SELL_PRICE = 132500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1326:
    PREFAB_ID = "item_prefab_1326"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1326"
    EQUIPMENT_SLOT = "Head" if 1326 % 4 == 0 else ("Chest" if 1326 % 4 == 1 else ("Weapon" if 1326 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 15912
    REQUIRE_LEVEL = 27
    SELL_PRICE = 132600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1327:
    PREFAB_ID = "item_prefab_1327"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1327"
    EQUIPMENT_SLOT = "Head" if 1327 % 4 == 0 else ("Chest" if 1327 % 4 == 1 else ("Weapon" if 1327 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 15924
    REQUIRE_LEVEL = 27
    SELL_PRICE = 132700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1328:
    PREFAB_ID = "item_prefab_1328"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1328"
    EQUIPMENT_SLOT = "Head" if 1328 % 4 == 0 else ("Chest" if 1328 % 4 == 1 else ("Weapon" if 1328 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 15936
    REQUIRE_LEVEL = 27
    SELL_PRICE = 132800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1329:
    PREFAB_ID = "item_prefab_1329"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1329"
    EQUIPMENT_SLOT = "Head" if 1329 % 4 == 0 else ("Chest" if 1329 % 4 == 1 else ("Weapon" if 1329 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 15948
    REQUIRE_LEVEL = 27
    SELL_PRICE = 132900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1330:
    PREFAB_ID = "item_prefab_1330"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1330"
    EQUIPMENT_SLOT = "Head" if 1330 % 4 == 0 else ("Chest" if 1330 % 4 == 1 else ("Weapon" if 1330 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 15960
    REQUIRE_LEVEL = 27
    SELL_PRICE = 133000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1331:
    PREFAB_ID = "item_prefab_1331"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1331"
    EQUIPMENT_SLOT = "Head" if 1331 % 4 == 0 else ("Chest" if 1331 % 4 == 1 else ("Weapon" if 1331 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 15972
    REQUIRE_LEVEL = 27
    SELL_PRICE = 133100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1332:
    PREFAB_ID = "item_prefab_1332"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1332"
    EQUIPMENT_SLOT = "Head" if 1332 % 4 == 0 else ("Chest" if 1332 % 4 == 1 else ("Weapon" if 1332 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 15984
    REQUIRE_LEVEL = 27
    SELL_PRICE = 133200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1333:
    PREFAB_ID = "item_prefab_1333"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1333"
    EQUIPMENT_SLOT = "Head" if 1333 % 4 == 0 else ("Chest" if 1333 % 4 == 1 else ("Weapon" if 1333 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 15996
    REQUIRE_LEVEL = 27
    SELL_PRICE = 133300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1334:
    PREFAB_ID = "item_prefab_1334"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1334"
    EQUIPMENT_SLOT = "Head" if 1334 % 4 == 0 else ("Chest" if 1334 % 4 == 1 else ("Weapon" if 1334 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 16008
    REQUIRE_LEVEL = 27
    SELL_PRICE = 133400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1335:
    PREFAB_ID = "item_prefab_1335"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1335"
    EQUIPMENT_SLOT = "Head" if 1335 % 4 == 0 else ("Chest" if 1335 % 4 == 1 else ("Weapon" if 1335 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 16020
    REQUIRE_LEVEL = 27
    SELL_PRICE = 133500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1336:
    PREFAB_ID = "item_prefab_1336"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1336"
    EQUIPMENT_SLOT = "Head" if 1336 % 4 == 0 else ("Chest" if 1336 % 4 == 1 else ("Weapon" if 1336 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 16032
    REQUIRE_LEVEL = 27
    SELL_PRICE = 133600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1337:
    PREFAB_ID = "item_prefab_1337"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1337"
    EQUIPMENT_SLOT = "Head" if 1337 % 4 == 0 else ("Chest" if 1337 % 4 == 1 else ("Weapon" if 1337 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 16044
    REQUIRE_LEVEL = 27
    SELL_PRICE = 133700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1338:
    PREFAB_ID = "item_prefab_1338"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1338"
    EQUIPMENT_SLOT = "Head" if 1338 % 4 == 0 else ("Chest" if 1338 % 4 == 1 else ("Weapon" if 1338 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 16056
    REQUIRE_LEVEL = 27
    SELL_PRICE = 133800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1339:
    PREFAB_ID = "item_prefab_1339"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1339"
    EQUIPMENT_SLOT = "Head" if 1339 % 4 == 0 else ("Chest" if 1339 % 4 == 1 else ("Weapon" if 1339 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 16068
    REQUIRE_LEVEL = 27
    SELL_PRICE = 133900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1340:
    PREFAB_ID = "item_prefab_1340"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1340"
    EQUIPMENT_SLOT = "Head" if 1340 % 4 == 0 else ("Chest" if 1340 % 4 == 1 else ("Weapon" if 1340 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 16080
    REQUIRE_LEVEL = 27
    SELL_PRICE = 134000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1341:
    PREFAB_ID = "item_prefab_1341"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1341"
    EQUIPMENT_SLOT = "Head" if 1341 % 4 == 0 else ("Chest" if 1341 % 4 == 1 else ("Weapon" if 1341 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 16092
    REQUIRE_LEVEL = 27
    SELL_PRICE = 134100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1342:
    PREFAB_ID = "item_prefab_1342"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1342"
    EQUIPMENT_SLOT = "Head" if 1342 % 4 == 0 else ("Chest" if 1342 % 4 == 1 else ("Weapon" if 1342 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 16104
    REQUIRE_LEVEL = 27
    SELL_PRICE = 134200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1343:
    PREFAB_ID = "item_prefab_1343"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1343"
    EQUIPMENT_SLOT = "Head" if 1343 % 4 == 0 else ("Chest" if 1343 % 4 == 1 else ("Weapon" if 1343 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 16116
    REQUIRE_LEVEL = 27
    SELL_PRICE = 134300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1344:
    PREFAB_ID = "item_prefab_1344"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1344"
    EQUIPMENT_SLOT = "Head" if 1344 % 4 == 0 else ("Chest" if 1344 % 4 == 1 else ("Weapon" if 1344 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 16128
    REQUIRE_LEVEL = 27
    SELL_PRICE = 134400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1345:
    PREFAB_ID = "item_prefab_1345"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1345"
    EQUIPMENT_SLOT = "Head" if 1345 % 4 == 0 else ("Chest" if 1345 % 4 == 1 else ("Weapon" if 1345 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 16140
    REQUIRE_LEVEL = 27
    SELL_PRICE = 134500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1346:
    PREFAB_ID = "item_prefab_1346"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1346"
    EQUIPMENT_SLOT = "Head" if 1346 % 4 == 0 else ("Chest" if 1346 % 4 == 1 else ("Weapon" if 1346 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 16152
    REQUIRE_LEVEL = 27
    SELL_PRICE = 134600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1347:
    PREFAB_ID = "item_prefab_1347"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1347"
    EQUIPMENT_SLOT = "Head" if 1347 % 4 == 0 else ("Chest" if 1347 % 4 == 1 else ("Weapon" if 1347 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 16164
    REQUIRE_LEVEL = 27
    SELL_PRICE = 134700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1348:
    PREFAB_ID = "item_prefab_1348"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1348"
    EQUIPMENT_SLOT = "Head" if 1348 % 4 == 0 else ("Chest" if 1348 % 4 == 1 else ("Weapon" if 1348 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 16176
    REQUIRE_LEVEL = 27
    SELL_PRICE = 134800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1349:
    PREFAB_ID = "item_prefab_1349"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1349"
    EQUIPMENT_SLOT = "Head" if 1349 % 4 == 0 else ("Chest" if 1349 % 4 == 1 else ("Weapon" if 1349 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 16188
    REQUIRE_LEVEL = 27
    SELL_PRICE = 134900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1350:
    PREFAB_ID = "item_prefab_1350"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1350"
    EQUIPMENT_SLOT = "Head" if 1350 % 4 == 0 else ("Chest" if 1350 % 4 == 1 else ("Weapon" if 1350 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 16200
    REQUIRE_LEVEL = 28
    SELL_PRICE = 135000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1351:
    PREFAB_ID = "item_prefab_1351"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1351"
    EQUIPMENT_SLOT = "Head" if 1351 % 4 == 0 else ("Chest" if 1351 % 4 == 1 else ("Weapon" if 1351 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 16212
    REQUIRE_LEVEL = 28
    SELL_PRICE = 135100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1352:
    PREFAB_ID = "item_prefab_1352"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1352"
    EQUIPMENT_SLOT = "Head" if 1352 % 4 == 0 else ("Chest" if 1352 % 4 == 1 else ("Weapon" if 1352 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 16224
    REQUIRE_LEVEL = 28
    SELL_PRICE = 135200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1353:
    PREFAB_ID = "item_prefab_1353"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1353"
    EQUIPMENT_SLOT = "Head" if 1353 % 4 == 0 else ("Chest" if 1353 % 4 == 1 else ("Weapon" if 1353 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 16236
    REQUIRE_LEVEL = 28
    SELL_PRICE = 135300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1354:
    PREFAB_ID = "item_prefab_1354"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1354"
    EQUIPMENT_SLOT = "Head" if 1354 % 4 == 0 else ("Chest" if 1354 % 4 == 1 else ("Weapon" if 1354 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 16248
    REQUIRE_LEVEL = 28
    SELL_PRICE = 135400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1355:
    PREFAB_ID = "item_prefab_1355"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1355"
    EQUIPMENT_SLOT = "Head" if 1355 % 4 == 0 else ("Chest" if 1355 % 4 == 1 else ("Weapon" if 1355 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 16260
    REQUIRE_LEVEL = 28
    SELL_PRICE = 135500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1356:
    PREFAB_ID = "item_prefab_1356"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1356"
    EQUIPMENT_SLOT = "Head" if 1356 % 4 == 0 else ("Chest" if 1356 % 4 == 1 else ("Weapon" if 1356 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 16272
    REQUIRE_LEVEL = 28
    SELL_PRICE = 135600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1357:
    PREFAB_ID = "item_prefab_1357"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1357"
    EQUIPMENT_SLOT = "Head" if 1357 % 4 == 0 else ("Chest" if 1357 % 4 == 1 else ("Weapon" if 1357 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 16284
    REQUIRE_LEVEL = 28
    SELL_PRICE = 135700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1358:
    PREFAB_ID = "item_prefab_1358"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1358"
    EQUIPMENT_SLOT = "Head" if 1358 % 4 == 0 else ("Chest" if 1358 % 4 == 1 else ("Weapon" if 1358 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 16296
    REQUIRE_LEVEL = 28
    SELL_PRICE = 135800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1359:
    PREFAB_ID = "item_prefab_1359"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1359"
    EQUIPMENT_SLOT = "Head" if 1359 % 4 == 0 else ("Chest" if 1359 % 4 == 1 else ("Weapon" if 1359 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 16308
    REQUIRE_LEVEL = 28
    SELL_PRICE = 135900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1360:
    PREFAB_ID = "item_prefab_1360"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1360"
    EQUIPMENT_SLOT = "Head" if 1360 % 4 == 0 else ("Chest" if 1360 % 4 == 1 else ("Weapon" if 1360 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 16320
    REQUIRE_LEVEL = 28
    SELL_PRICE = 136000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1361:
    PREFAB_ID = "item_prefab_1361"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1361"
    EQUIPMENT_SLOT = "Head" if 1361 % 4 == 0 else ("Chest" if 1361 % 4 == 1 else ("Weapon" if 1361 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 16332
    REQUIRE_LEVEL = 28
    SELL_PRICE = 136100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1362:
    PREFAB_ID = "item_prefab_1362"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1362"
    EQUIPMENT_SLOT = "Head" if 1362 % 4 == 0 else ("Chest" if 1362 % 4 == 1 else ("Weapon" if 1362 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 16344
    REQUIRE_LEVEL = 28
    SELL_PRICE = 136200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1363:
    PREFAB_ID = "item_prefab_1363"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1363"
    EQUIPMENT_SLOT = "Head" if 1363 % 4 == 0 else ("Chest" if 1363 % 4 == 1 else ("Weapon" if 1363 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 16356
    REQUIRE_LEVEL = 28
    SELL_PRICE = 136300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1364:
    PREFAB_ID = "item_prefab_1364"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1364"
    EQUIPMENT_SLOT = "Head" if 1364 % 4 == 0 else ("Chest" if 1364 % 4 == 1 else ("Weapon" if 1364 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 16368
    REQUIRE_LEVEL = 28
    SELL_PRICE = 136400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1365:
    PREFAB_ID = "item_prefab_1365"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1365"
    EQUIPMENT_SLOT = "Head" if 1365 % 4 == 0 else ("Chest" if 1365 % 4 == 1 else ("Weapon" if 1365 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 16380
    REQUIRE_LEVEL = 28
    SELL_PRICE = 136500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1366:
    PREFAB_ID = "item_prefab_1366"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1366"
    EQUIPMENT_SLOT = "Head" if 1366 % 4 == 0 else ("Chest" if 1366 % 4 == 1 else ("Weapon" if 1366 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 16392
    REQUIRE_LEVEL = 28
    SELL_PRICE = 136600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1367:
    PREFAB_ID = "item_prefab_1367"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1367"
    EQUIPMENT_SLOT = "Head" if 1367 % 4 == 0 else ("Chest" if 1367 % 4 == 1 else ("Weapon" if 1367 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 16404
    REQUIRE_LEVEL = 28
    SELL_PRICE = 136700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1368:
    PREFAB_ID = "item_prefab_1368"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1368"
    EQUIPMENT_SLOT = "Head" if 1368 % 4 == 0 else ("Chest" if 1368 % 4 == 1 else ("Weapon" if 1368 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 16416
    REQUIRE_LEVEL = 28
    SELL_PRICE = 136800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1369:
    PREFAB_ID = "item_prefab_1369"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1369"
    EQUIPMENT_SLOT = "Head" if 1369 % 4 == 0 else ("Chest" if 1369 % 4 == 1 else ("Weapon" if 1369 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 16428
    REQUIRE_LEVEL = 28
    SELL_PRICE = 136900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1370:
    PREFAB_ID = "item_prefab_1370"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1370"
    EQUIPMENT_SLOT = "Head" if 1370 % 4 == 0 else ("Chest" if 1370 % 4 == 1 else ("Weapon" if 1370 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 16440
    REQUIRE_LEVEL = 28
    SELL_PRICE = 137000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1371:
    PREFAB_ID = "item_prefab_1371"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1371"
    EQUIPMENT_SLOT = "Head" if 1371 % 4 == 0 else ("Chest" if 1371 % 4 == 1 else ("Weapon" if 1371 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 16452
    REQUIRE_LEVEL = 28
    SELL_PRICE = 137100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1372:
    PREFAB_ID = "item_prefab_1372"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1372"
    EQUIPMENT_SLOT = "Head" if 1372 % 4 == 0 else ("Chest" if 1372 % 4 == 1 else ("Weapon" if 1372 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 16464
    REQUIRE_LEVEL = 28
    SELL_PRICE = 137200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1373:
    PREFAB_ID = "item_prefab_1373"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1373"
    EQUIPMENT_SLOT = "Head" if 1373 % 4 == 0 else ("Chest" if 1373 % 4 == 1 else ("Weapon" if 1373 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 16476
    REQUIRE_LEVEL = 28
    SELL_PRICE = 137300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1374:
    PREFAB_ID = "item_prefab_1374"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1374"
    EQUIPMENT_SLOT = "Head" if 1374 % 4 == 0 else ("Chest" if 1374 % 4 == 1 else ("Weapon" if 1374 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 16488
    REQUIRE_LEVEL = 28
    SELL_PRICE = 137400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1375:
    PREFAB_ID = "item_prefab_1375"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1375"
    EQUIPMENT_SLOT = "Head" if 1375 % 4 == 0 else ("Chest" if 1375 % 4 == 1 else ("Weapon" if 1375 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 16500
    REQUIRE_LEVEL = 28
    SELL_PRICE = 137500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1376:
    PREFAB_ID = "item_prefab_1376"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1376"
    EQUIPMENT_SLOT = "Head" if 1376 % 4 == 0 else ("Chest" if 1376 % 4 == 1 else ("Weapon" if 1376 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 16512
    REQUIRE_LEVEL = 28
    SELL_PRICE = 137600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1377:
    PREFAB_ID = "item_prefab_1377"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1377"
    EQUIPMENT_SLOT = "Head" if 1377 % 4 == 0 else ("Chest" if 1377 % 4 == 1 else ("Weapon" if 1377 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 16524
    REQUIRE_LEVEL = 28
    SELL_PRICE = 137700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1378:
    PREFAB_ID = "item_prefab_1378"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1378"
    EQUIPMENT_SLOT = "Head" if 1378 % 4 == 0 else ("Chest" if 1378 % 4 == 1 else ("Weapon" if 1378 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 16536
    REQUIRE_LEVEL = 28
    SELL_PRICE = 137800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1379:
    PREFAB_ID = "item_prefab_1379"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1379"
    EQUIPMENT_SLOT = "Head" if 1379 % 4 == 0 else ("Chest" if 1379 % 4 == 1 else ("Weapon" if 1379 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 16548
    REQUIRE_LEVEL = 28
    SELL_PRICE = 137900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1380:
    PREFAB_ID = "item_prefab_1380"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1380"
    EQUIPMENT_SLOT = "Head" if 1380 % 4 == 0 else ("Chest" if 1380 % 4 == 1 else ("Weapon" if 1380 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 16560
    REQUIRE_LEVEL = 28
    SELL_PRICE = 138000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1381:
    PREFAB_ID = "item_prefab_1381"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1381"
    EQUIPMENT_SLOT = "Head" if 1381 % 4 == 0 else ("Chest" if 1381 % 4 == 1 else ("Weapon" if 1381 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 16572
    REQUIRE_LEVEL = 28
    SELL_PRICE = 138100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1382:
    PREFAB_ID = "item_prefab_1382"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1382"
    EQUIPMENT_SLOT = "Head" if 1382 % 4 == 0 else ("Chest" if 1382 % 4 == 1 else ("Weapon" if 1382 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 16584
    REQUIRE_LEVEL = 28
    SELL_PRICE = 138200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1383:
    PREFAB_ID = "item_prefab_1383"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1383"
    EQUIPMENT_SLOT = "Head" if 1383 % 4 == 0 else ("Chest" if 1383 % 4 == 1 else ("Weapon" if 1383 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 16596
    REQUIRE_LEVEL = 28
    SELL_PRICE = 138300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1384:
    PREFAB_ID = "item_prefab_1384"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1384"
    EQUIPMENT_SLOT = "Head" if 1384 % 4 == 0 else ("Chest" if 1384 % 4 == 1 else ("Weapon" if 1384 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 16608
    REQUIRE_LEVEL = 28
    SELL_PRICE = 138400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1385:
    PREFAB_ID = "item_prefab_1385"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1385"
    EQUIPMENT_SLOT = "Head" if 1385 % 4 == 0 else ("Chest" if 1385 % 4 == 1 else ("Weapon" if 1385 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 16620
    REQUIRE_LEVEL = 28
    SELL_PRICE = 138500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1386:
    PREFAB_ID = "item_prefab_1386"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1386"
    EQUIPMENT_SLOT = "Head" if 1386 % 4 == 0 else ("Chest" if 1386 % 4 == 1 else ("Weapon" if 1386 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 16632
    REQUIRE_LEVEL = 28
    SELL_PRICE = 138600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1387:
    PREFAB_ID = "item_prefab_1387"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1387"
    EQUIPMENT_SLOT = "Head" if 1387 % 4 == 0 else ("Chest" if 1387 % 4 == 1 else ("Weapon" if 1387 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 16644
    REQUIRE_LEVEL = 28
    SELL_PRICE = 138700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1388:
    PREFAB_ID = "item_prefab_1388"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1388"
    EQUIPMENT_SLOT = "Head" if 1388 % 4 == 0 else ("Chest" if 1388 % 4 == 1 else ("Weapon" if 1388 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 16656
    REQUIRE_LEVEL = 28
    SELL_PRICE = 138800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1389:
    PREFAB_ID = "item_prefab_1389"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1389"
    EQUIPMENT_SLOT = "Head" if 1389 % 4 == 0 else ("Chest" if 1389 % 4 == 1 else ("Weapon" if 1389 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 16668
    REQUIRE_LEVEL = 28
    SELL_PRICE = 138900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1390:
    PREFAB_ID = "item_prefab_1390"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1390"
    EQUIPMENT_SLOT = "Head" if 1390 % 4 == 0 else ("Chest" if 1390 % 4 == 1 else ("Weapon" if 1390 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 16680
    REQUIRE_LEVEL = 28
    SELL_PRICE = 139000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1391:
    PREFAB_ID = "item_prefab_1391"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1391"
    EQUIPMENT_SLOT = "Head" if 1391 % 4 == 0 else ("Chest" if 1391 % 4 == 1 else ("Weapon" if 1391 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 16692
    REQUIRE_LEVEL = 28
    SELL_PRICE = 139100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1392:
    PREFAB_ID = "item_prefab_1392"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1392"
    EQUIPMENT_SLOT = "Head" if 1392 % 4 == 0 else ("Chest" if 1392 % 4 == 1 else ("Weapon" if 1392 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 16704
    REQUIRE_LEVEL = 28
    SELL_PRICE = 139200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1393:
    PREFAB_ID = "item_prefab_1393"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1393"
    EQUIPMENT_SLOT = "Head" if 1393 % 4 == 0 else ("Chest" if 1393 % 4 == 1 else ("Weapon" if 1393 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 16716
    REQUIRE_LEVEL = 28
    SELL_PRICE = 139300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1394:
    PREFAB_ID = "item_prefab_1394"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1394"
    EQUIPMENT_SLOT = "Head" if 1394 % 4 == 0 else ("Chest" if 1394 % 4 == 1 else ("Weapon" if 1394 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 16728
    REQUIRE_LEVEL = 28
    SELL_PRICE = 139400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1395:
    PREFAB_ID = "item_prefab_1395"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1395"
    EQUIPMENT_SLOT = "Head" if 1395 % 4 == 0 else ("Chest" if 1395 % 4 == 1 else ("Weapon" if 1395 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 16740
    REQUIRE_LEVEL = 28
    SELL_PRICE = 139500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1396:
    PREFAB_ID = "item_prefab_1396"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1396"
    EQUIPMENT_SLOT = "Head" if 1396 % 4 == 0 else ("Chest" if 1396 % 4 == 1 else ("Weapon" if 1396 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 16752
    REQUIRE_LEVEL = 28
    SELL_PRICE = 139600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1397:
    PREFAB_ID = "item_prefab_1397"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1397"
    EQUIPMENT_SLOT = "Head" if 1397 % 4 == 0 else ("Chest" if 1397 % 4 == 1 else ("Weapon" if 1397 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 16764
    REQUIRE_LEVEL = 28
    SELL_PRICE = 139700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1398:
    PREFAB_ID = "item_prefab_1398"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1398"
    EQUIPMENT_SLOT = "Head" if 1398 % 4 == 0 else ("Chest" if 1398 % 4 == 1 else ("Weapon" if 1398 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 16776
    REQUIRE_LEVEL = 28
    SELL_PRICE = 139800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1399:
    PREFAB_ID = "item_prefab_1399"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1399"
    EQUIPMENT_SLOT = "Head" if 1399 % 4 == 0 else ("Chest" if 1399 % 4 == 1 else ("Weapon" if 1399 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 16788
    REQUIRE_LEVEL = 28
    SELL_PRICE = 139900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1400:
    PREFAB_ID = "item_prefab_1400"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1400"
    EQUIPMENT_SLOT = "Head" if 1400 % 4 == 0 else ("Chest" if 1400 % 4 == 1 else ("Weapon" if 1400 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 16800
    REQUIRE_LEVEL = 29
    SELL_PRICE = 140000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1401:
    PREFAB_ID = "item_prefab_1401"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1401"
    EQUIPMENT_SLOT = "Head" if 1401 % 4 == 0 else ("Chest" if 1401 % 4 == 1 else ("Weapon" if 1401 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 16812
    REQUIRE_LEVEL = 29
    SELL_PRICE = 140100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1402:
    PREFAB_ID = "item_prefab_1402"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1402"
    EQUIPMENT_SLOT = "Head" if 1402 % 4 == 0 else ("Chest" if 1402 % 4 == 1 else ("Weapon" if 1402 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 16824
    REQUIRE_LEVEL = 29
    SELL_PRICE = 140200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1403:
    PREFAB_ID = "item_prefab_1403"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1403"
    EQUIPMENT_SLOT = "Head" if 1403 % 4 == 0 else ("Chest" if 1403 % 4 == 1 else ("Weapon" if 1403 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 16836
    REQUIRE_LEVEL = 29
    SELL_PRICE = 140300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1404:
    PREFAB_ID = "item_prefab_1404"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1404"
    EQUIPMENT_SLOT = "Head" if 1404 % 4 == 0 else ("Chest" if 1404 % 4 == 1 else ("Weapon" if 1404 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 16848
    REQUIRE_LEVEL = 29
    SELL_PRICE = 140400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1405:
    PREFAB_ID = "item_prefab_1405"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1405"
    EQUIPMENT_SLOT = "Head" if 1405 % 4 == 0 else ("Chest" if 1405 % 4 == 1 else ("Weapon" if 1405 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 16860
    REQUIRE_LEVEL = 29
    SELL_PRICE = 140500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1406:
    PREFAB_ID = "item_prefab_1406"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1406"
    EQUIPMENT_SLOT = "Head" if 1406 % 4 == 0 else ("Chest" if 1406 % 4 == 1 else ("Weapon" if 1406 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 16872
    REQUIRE_LEVEL = 29
    SELL_PRICE = 140600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1407:
    PREFAB_ID = "item_prefab_1407"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1407"
    EQUIPMENT_SLOT = "Head" if 1407 % 4 == 0 else ("Chest" if 1407 % 4 == 1 else ("Weapon" if 1407 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 16884
    REQUIRE_LEVEL = 29
    SELL_PRICE = 140700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1408:
    PREFAB_ID = "item_prefab_1408"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1408"
    EQUIPMENT_SLOT = "Head" if 1408 % 4 == 0 else ("Chest" if 1408 % 4 == 1 else ("Weapon" if 1408 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 16896
    REQUIRE_LEVEL = 29
    SELL_PRICE = 140800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1409:
    PREFAB_ID = "item_prefab_1409"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1409"
    EQUIPMENT_SLOT = "Head" if 1409 % 4 == 0 else ("Chest" if 1409 % 4 == 1 else ("Weapon" if 1409 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 16908
    REQUIRE_LEVEL = 29
    SELL_PRICE = 140900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1410:
    PREFAB_ID = "item_prefab_1410"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1410"
    EQUIPMENT_SLOT = "Head" if 1410 % 4 == 0 else ("Chest" if 1410 % 4 == 1 else ("Weapon" if 1410 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 16920
    REQUIRE_LEVEL = 29
    SELL_PRICE = 141000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1411:
    PREFAB_ID = "item_prefab_1411"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1411"
    EQUIPMENT_SLOT = "Head" if 1411 % 4 == 0 else ("Chest" if 1411 % 4 == 1 else ("Weapon" if 1411 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 16932
    REQUIRE_LEVEL = 29
    SELL_PRICE = 141100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1412:
    PREFAB_ID = "item_prefab_1412"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1412"
    EQUIPMENT_SLOT = "Head" if 1412 % 4 == 0 else ("Chest" if 1412 % 4 == 1 else ("Weapon" if 1412 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 16944
    REQUIRE_LEVEL = 29
    SELL_PRICE = 141200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1413:
    PREFAB_ID = "item_prefab_1413"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1413"
    EQUIPMENT_SLOT = "Head" if 1413 % 4 == 0 else ("Chest" if 1413 % 4 == 1 else ("Weapon" if 1413 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 16956
    REQUIRE_LEVEL = 29
    SELL_PRICE = 141300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1414:
    PREFAB_ID = "item_prefab_1414"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1414"
    EQUIPMENT_SLOT = "Head" if 1414 % 4 == 0 else ("Chest" if 1414 % 4 == 1 else ("Weapon" if 1414 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 16968
    REQUIRE_LEVEL = 29
    SELL_PRICE = 141400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1415:
    PREFAB_ID = "item_prefab_1415"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1415"
    EQUIPMENT_SLOT = "Head" if 1415 % 4 == 0 else ("Chest" if 1415 % 4 == 1 else ("Weapon" if 1415 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 16980
    REQUIRE_LEVEL = 29
    SELL_PRICE = 141500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1416:
    PREFAB_ID = "item_prefab_1416"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1416"
    EQUIPMENT_SLOT = "Head" if 1416 % 4 == 0 else ("Chest" if 1416 % 4 == 1 else ("Weapon" if 1416 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 16992
    REQUIRE_LEVEL = 29
    SELL_PRICE = 141600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1417:
    PREFAB_ID = "item_prefab_1417"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1417"
    EQUIPMENT_SLOT = "Head" if 1417 % 4 == 0 else ("Chest" if 1417 % 4 == 1 else ("Weapon" if 1417 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 17004
    REQUIRE_LEVEL = 29
    SELL_PRICE = 141700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1418:
    PREFAB_ID = "item_prefab_1418"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1418"
    EQUIPMENT_SLOT = "Head" if 1418 % 4 == 0 else ("Chest" if 1418 % 4 == 1 else ("Weapon" if 1418 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 17016
    REQUIRE_LEVEL = 29
    SELL_PRICE = 141800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1419:
    PREFAB_ID = "item_prefab_1419"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1419"
    EQUIPMENT_SLOT = "Head" if 1419 % 4 == 0 else ("Chest" if 1419 % 4 == 1 else ("Weapon" if 1419 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 17028
    REQUIRE_LEVEL = 29
    SELL_PRICE = 141900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1420:
    PREFAB_ID = "item_prefab_1420"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1420"
    EQUIPMENT_SLOT = "Head" if 1420 % 4 == 0 else ("Chest" if 1420 % 4 == 1 else ("Weapon" if 1420 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 17040
    REQUIRE_LEVEL = 29
    SELL_PRICE = 142000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1421:
    PREFAB_ID = "item_prefab_1421"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1421"
    EQUIPMENT_SLOT = "Head" if 1421 % 4 == 0 else ("Chest" if 1421 % 4 == 1 else ("Weapon" if 1421 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 17052
    REQUIRE_LEVEL = 29
    SELL_PRICE = 142100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1422:
    PREFAB_ID = "item_prefab_1422"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1422"
    EQUIPMENT_SLOT = "Head" if 1422 % 4 == 0 else ("Chest" if 1422 % 4 == 1 else ("Weapon" if 1422 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 17064
    REQUIRE_LEVEL = 29
    SELL_PRICE = 142200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1423:
    PREFAB_ID = "item_prefab_1423"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1423"
    EQUIPMENT_SLOT = "Head" if 1423 % 4 == 0 else ("Chest" if 1423 % 4 == 1 else ("Weapon" if 1423 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 17076
    REQUIRE_LEVEL = 29
    SELL_PRICE = 142300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1424:
    PREFAB_ID = "item_prefab_1424"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1424"
    EQUIPMENT_SLOT = "Head" if 1424 % 4 == 0 else ("Chest" if 1424 % 4 == 1 else ("Weapon" if 1424 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 17088
    REQUIRE_LEVEL = 29
    SELL_PRICE = 142400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1425:
    PREFAB_ID = "item_prefab_1425"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1425"
    EQUIPMENT_SLOT = "Head" if 1425 % 4 == 0 else ("Chest" if 1425 % 4 == 1 else ("Weapon" if 1425 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 17100
    REQUIRE_LEVEL = 29
    SELL_PRICE = 142500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1426:
    PREFAB_ID = "item_prefab_1426"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1426"
    EQUIPMENT_SLOT = "Head" if 1426 % 4 == 0 else ("Chest" if 1426 % 4 == 1 else ("Weapon" if 1426 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 17112
    REQUIRE_LEVEL = 29
    SELL_PRICE = 142600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1427:
    PREFAB_ID = "item_prefab_1427"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1427"
    EQUIPMENT_SLOT = "Head" if 1427 % 4 == 0 else ("Chest" if 1427 % 4 == 1 else ("Weapon" if 1427 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 17124
    REQUIRE_LEVEL = 29
    SELL_PRICE = 142700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1428:
    PREFAB_ID = "item_prefab_1428"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1428"
    EQUIPMENT_SLOT = "Head" if 1428 % 4 == 0 else ("Chest" if 1428 % 4 == 1 else ("Weapon" if 1428 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 17136
    REQUIRE_LEVEL = 29
    SELL_PRICE = 142800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1429:
    PREFAB_ID = "item_prefab_1429"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1429"
    EQUIPMENT_SLOT = "Head" if 1429 % 4 == 0 else ("Chest" if 1429 % 4 == 1 else ("Weapon" if 1429 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 17148
    REQUIRE_LEVEL = 29
    SELL_PRICE = 142900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1430:
    PREFAB_ID = "item_prefab_1430"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1430"
    EQUIPMENT_SLOT = "Head" if 1430 % 4 == 0 else ("Chest" if 1430 % 4 == 1 else ("Weapon" if 1430 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 17160
    REQUIRE_LEVEL = 29
    SELL_PRICE = 143000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1431:
    PREFAB_ID = "item_prefab_1431"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1431"
    EQUIPMENT_SLOT = "Head" if 1431 % 4 == 0 else ("Chest" if 1431 % 4 == 1 else ("Weapon" if 1431 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 17172
    REQUIRE_LEVEL = 29
    SELL_PRICE = 143100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1432:
    PREFAB_ID = "item_prefab_1432"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1432"
    EQUIPMENT_SLOT = "Head" if 1432 % 4 == 0 else ("Chest" if 1432 % 4 == 1 else ("Weapon" if 1432 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 17184
    REQUIRE_LEVEL = 29
    SELL_PRICE = 143200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1433:
    PREFAB_ID = "item_prefab_1433"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1433"
    EQUIPMENT_SLOT = "Head" if 1433 % 4 == 0 else ("Chest" if 1433 % 4 == 1 else ("Weapon" if 1433 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 17196
    REQUIRE_LEVEL = 29
    SELL_PRICE = 143300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1434:
    PREFAB_ID = "item_prefab_1434"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1434"
    EQUIPMENT_SLOT = "Head" if 1434 % 4 == 0 else ("Chest" if 1434 % 4 == 1 else ("Weapon" if 1434 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 17208
    REQUIRE_LEVEL = 29
    SELL_PRICE = 143400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1435:
    PREFAB_ID = "item_prefab_1435"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1435"
    EQUIPMENT_SLOT = "Head" if 1435 % 4 == 0 else ("Chest" if 1435 % 4 == 1 else ("Weapon" if 1435 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 17220
    REQUIRE_LEVEL = 29
    SELL_PRICE = 143500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1436:
    PREFAB_ID = "item_prefab_1436"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1436"
    EQUIPMENT_SLOT = "Head" if 1436 % 4 == 0 else ("Chest" if 1436 % 4 == 1 else ("Weapon" if 1436 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 17232
    REQUIRE_LEVEL = 29
    SELL_PRICE = 143600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1437:
    PREFAB_ID = "item_prefab_1437"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1437"
    EQUIPMENT_SLOT = "Head" if 1437 % 4 == 0 else ("Chest" if 1437 % 4 == 1 else ("Weapon" if 1437 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 17244
    REQUIRE_LEVEL = 29
    SELL_PRICE = 143700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1438:
    PREFAB_ID = "item_prefab_1438"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1438"
    EQUIPMENT_SLOT = "Head" if 1438 % 4 == 0 else ("Chest" if 1438 % 4 == 1 else ("Weapon" if 1438 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 17256
    REQUIRE_LEVEL = 29
    SELL_PRICE = 143800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1439:
    PREFAB_ID = "item_prefab_1439"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1439"
    EQUIPMENT_SLOT = "Head" if 1439 % 4 == 0 else ("Chest" if 1439 % 4 == 1 else ("Weapon" if 1439 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 17268
    REQUIRE_LEVEL = 29
    SELL_PRICE = 143900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1440:
    PREFAB_ID = "item_prefab_1440"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1440"
    EQUIPMENT_SLOT = "Head" if 1440 % 4 == 0 else ("Chest" if 1440 % 4 == 1 else ("Weapon" if 1440 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 17280
    REQUIRE_LEVEL = 29
    SELL_PRICE = 144000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1441:
    PREFAB_ID = "item_prefab_1441"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1441"
    EQUIPMENT_SLOT = "Head" if 1441 % 4 == 0 else ("Chest" if 1441 % 4 == 1 else ("Weapon" if 1441 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 17292
    REQUIRE_LEVEL = 29
    SELL_PRICE = 144100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1442:
    PREFAB_ID = "item_prefab_1442"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1442"
    EQUIPMENT_SLOT = "Head" if 1442 % 4 == 0 else ("Chest" if 1442 % 4 == 1 else ("Weapon" if 1442 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 17304
    REQUIRE_LEVEL = 29
    SELL_PRICE = 144200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1443:
    PREFAB_ID = "item_prefab_1443"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1443"
    EQUIPMENT_SLOT = "Head" if 1443 % 4 == 0 else ("Chest" if 1443 % 4 == 1 else ("Weapon" if 1443 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 17316
    REQUIRE_LEVEL = 29
    SELL_PRICE = 144300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1444:
    PREFAB_ID = "item_prefab_1444"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1444"
    EQUIPMENT_SLOT = "Head" if 1444 % 4 == 0 else ("Chest" if 1444 % 4 == 1 else ("Weapon" if 1444 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 17328
    REQUIRE_LEVEL = 29
    SELL_PRICE = 144400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1445:
    PREFAB_ID = "item_prefab_1445"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1445"
    EQUIPMENT_SLOT = "Head" if 1445 % 4 == 0 else ("Chest" if 1445 % 4 == 1 else ("Weapon" if 1445 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 17340
    REQUIRE_LEVEL = 29
    SELL_PRICE = 144500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1446:
    PREFAB_ID = "item_prefab_1446"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1446"
    EQUIPMENT_SLOT = "Head" if 1446 % 4 == 0 else ("Chest" if 1446 % 4 == 1 else ("Weapon" if 1446 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 17352
    REQUIRE_LEVEL = 29
    SELL_PRICE = 144600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1447:
    PREFAB_ID = "item_prefab_1447"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1447"
    EQUIPMENT_SLOT = "Head" if 1447 % 4 == 0 else ("Chest" if 1447 % 4 == 1 else ("Weapon" if 1447 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 17364
    REQUIRE_LEVEL = 29
    SELL_PRICE = 144700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1448:
    PREFAB_ID = "item_prefab_1448"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1448"
    EQUIPMENT_SLOT = "Head" if 1448 % 4 == 0 else ("Chest" if 1448 % 4 == 1 else ("Weapon" if 1448 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 17376
    REQUIRE_LEVEL = 29
    SELL_PRICE = 144800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1449:
    PREFAB_ID = "item_prefab_1449"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1449"
    EQUIPMENT_SLOT = "Head" if 1449 % 4 == 0 else ("Chest" if 1449 % 4 == 1 else ("Weapon" if 1449 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 17388
    REQUIRE_LEVEL = 29
    SELL_PRICE = 144900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1450:
    PREFAB_ID = "item_prefab_1450"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1450"
    EQUIPMENT_SLOT = "Head" if 1450 % 4 == 0 else ("Chest" if 1450 % 4 == 1 else ("Weapon" if 1450 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 17400
    REQUIRE_LEVEL = 30
    SELL_PRICE = 145000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1451:
    PREFAB_ID = "item_prefab_1451"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1451"
    EQUIPMENT_SLOT = "Head" if 1451 % 4 == 0 else ("Chest" if 1451 % 4 == 1 else ("Weapon" if 1451 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 17412
    REQUIRE_LEVEL = 30
    SELL_PRICE = 145100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1452:
    PREFAB_ID = "item_prefab_1452"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1452"
    EQUIPMENT_SLOT = "Head" if 1452 % 4 == 0 else ("Chest" if 1452 % 4 == 1 else ("Weapon" if 1452 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 17424
    REQUIRE_LEVEL = 30
    SELL_PRICE = 145200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1453:
    PREFAB_ID = "item_prefab_1453"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1453"
    EQUIPMENT_SLOT = "Head" if 1453 % 4 == 0 else ("Chest" if 1453 % 4 == 1 else ("Weapon" if 1453 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 17436
    REQUIRE_LEVEL = 30
    SELL_PRICE = 145300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1454:
    PREFAB_ID = "item_prefab_1454"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1454"
    EQUIPMENT_SLOT = "Head" if 1454 % 4 == 0 else ("Chest" if 1454 % 4 == 1 else ("Weapon" if 1454 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 17448
    REQUIRE_LEVEL = 30
    SELL_PRICE = 145400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1455:
    PREFAB_ID = "item_prefab_1455"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1455"
    EQUIPMENT_SLOT = "Head" if 1455 % 4 == 0 else ("Chest" if 1455 % 4 == 1 else ("Weapon" if 1455 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 17460
    REQUIRE_LEVEL = 30
    SELL_PRICE = 145500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1456:
    PREFAB_ID = "item_prefab_1456"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1456"
    EQUIPMENT_SLOT = "Head" if 1456 % 4 == 0 else ("Chest" if 1456 % 4 == 1 else ("Weapon" if 1456 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 17472
    REQUIRE_LEVEL = 30
    SELL_PRICE = 145600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1457:
    PREFAB_ID = "item_prefab_1457"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1457"
    EQUIPMENT_SLOT = "Head" if 1457 % 4 == 0 else ("Chest" if 1457 % 4 == 1 else ("Weapon" if 1457 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 17484
    REQUIRE_LEVEL = 30
    SELL_PRICE = 145700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1458:
    PREFAB_ID = "item_prefab_1458"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1458"
    EQUIPMENT_SLOT = "Head" if 1458 % 4 == 0 else ("Chest" if 1458 % 4 == 1 else ("Weapon" if 1458 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 17496
    REQUIRE_LEVEL = 30
    SELL_PRICE = 145800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1459:
    PREFAB_ID = "item_prefab_1459"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1459"
    EQUIPMENT_SLOT = "Head" if 1459 % 4 == 0 else ("Chest" if 1459 % 4 == 1 else ("Weapon" if 1459 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 17508
    REQUIRE_LEVEL = 30
    SELL_PRICE = 145900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1460:
    PREFAB_ID = "item_prefab_1460"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1460"
    EQUIPMENT_SLOT = "Head" if 1460 % 4 == 0 else ("Chest" if 1460 % 4 == 1 else ("Weapon" if 1460 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 17520
    REQUIRE_LEVEL = 30
    SELL_PRICE = 146000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1461:
    PREFAB_ID = "item_prefab_1461"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1461"
    EQUIPMENT_SLOT = "Head" if 1461 % 4 == 0 else ("Chest" if 1461 % 4 == 1 else ("Weapon" if 1461 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 17532
    REQUIRE_LEVEL = 30
    SELL_PRICE = 146100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1462:
    PREFAB_ID = "item_prefab_1462"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1462"
    EQUIPMENT_SLOT = "Head" if 1462 % 4 == 0 else ("Chest" if 1462 % 4 == 1 else ("Weapon" if 1462 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 17544
    REQUIRE_LEVEL = 30
    SELL_PRICE = 146200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1463:
    PREFAB_ID = "item_prefab_1463"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1463"
    EQUIPMENT_SLOT = "Head" if 1463 % 4 == 0 else ("Chest" if 1463 % 4 == 1 else ("Weapon" if 1463 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 17556
    REQUIRE_LEVEL = 30
    SELL_PRICE = 146300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1464:
    PREFAB_ID = "item_prefab_1464"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1464"
    EQUIPMENT_SLOT = "Head" if 1464 % 4 == 0 else ("Chest" if 1464 % 4 == 1 else ("Weapon" if 1464 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 17568
    REQUIRE_LEVEL = 30
    SELL_PRICE = 146400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1465:
    PREFAB_ID = "item_prefab_1465"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1465"
    EQUIPMENT_SLOT = "Head" if 1465 % 4 == 0 else ("Chest" if 1465 % 4 == 1 else ("Weapon" if 1465 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 17580
    REQUIRE_LEVEL = 30
    SELL_PRICE = 146500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1466:
    PREFAB_ID = "item_prefab_1466"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1466"
    EQUIPMENT_SLOT = "Head" if 1466 % 4 == 0 else ("Chest" if 1466 % 4 == 1 else ("Weapon" if 1466 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 17592
    REQUIRE_LEVEL = 30
    SELL_PRICE = 146600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1467:
    PREFAB_ID = "item_prefab_1467"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1467"
    EQUIPMENT_SLOT = "Head" if 1467 % 4 == 0 else ("Chest" if 1467 % 4 == 1 else ("Weapon" if 1467 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 17604
    REQUIRE_LEVEL = 30
    SELL_PRICE = 146700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1468:
    PREFAB_ID = "item_prefab_1468"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1468"
    EQUIPMENT_SLOT = "Head" if 1468 % 4 == 0 else ("Chest" if 1468 % 4 == 1 else ("Weapon" if 1468 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 17616
    REQUIRE_LEVEL = 30
    SELL_PRICE = 146800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1469:
    PREFAB_ID = "item_prefab_1469"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1469"
    EQUIPMENT_SLOT = "Head" if 1469 % 4 == 0 else ("Chest" if 1469 % 4 == 1 else ("Weapon" if 1469 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 17628
    REQUIRE_LEVEL = 30
    SELL_PRICE = 146900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1470:
    PREFAB_ID = "item_prefab_1470"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1470"
    EQUIPMENT_SLOT = "Head" if 1470 % 4 == 0 else ("Chest" if 1470 % 4 == 1 else ("Weapon" if 1470 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 17640
    REQUIRE_LEVEL = 30
    SELL_PRICE = 147000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1471:
    PREFAB_ID = "item_prefab_1471"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1471"
    EQUIPMENT_SLOT = "Head" if 1471 % 4 == 0 else ("Chest" if 1471 % 4 == 1 else ("Weapon" if 1471 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 17652
    REQUIRE_LEVEL = 30
    SELL_PRICE = 147100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1472:
    PREFAB_ID = "item_prefab_1472"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1472"
    EQUIPMENT_SLOT = "Head" if 1472 % 4 == 0 else ("Chest" if 1472 % 4 == 1 else ("Weapon" if 1472 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 17664
    REQUIRE_LEVEL = 30
    SELL_PRICE = 147200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1473:
    PREFAB_ID = "item_prefab_1473"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1473"
    EQUIPMENT_SLOT = "Head" if 1473 % 4 == 0 else ("Chest" if 1473 % 4 == 1 else ("Weapon" if 1473 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 17676
    REQUIRE_LEVEL = 30
    SELL_PRICE = 147300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1474:
    PREFAB_ID = "item_prefab_1474"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1474"
    EQUIPMENT_SLOT = "Head" if 1474 % 4 == 0 else ("Chest" if 1474 % 4 == 1 else ("Weapon" if 1474 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 17688
    REQUIRE_LEVEL = 30
    SELL_PRICE = 147400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1475:
    PREFAB_ID = "item_prefab_1475"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1475"
    EQUIPMENT_SLOT = "Head" if 1475 % 4 == 0 else ("Chest" if 1475 % 4 == 1 else ("Weapon" if 1475 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 17700
    REQUIRE_LEVEL = 30
    SELL_PRICE = 147500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1476:
    PREFAB_ID = "item_prefab_1476"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1476"
    EQUIPMENT_SLOT = "Head" if 1476 % 4 == 0 else ("Chest" if 1476 % 4 == 1 else ("Weapon" if 1476 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 17712
    REQUIRE_LEVEL = 30
    SELL_PRICE = 147600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1477:
    PREFAB_ID = "item_prefab_1477"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1477"
    EQUIPMENT_SLOT = "Head" if 1477 % 4 == 0 else ("Chest" if 1477 % 4 == 1 else ("Weapon" if 1477 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 17724
    REQUIRE_LEVEL = 30
    SELL_PRICE = 147700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1478:
    PREFAB_ID = "item_prefab_1478"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1478"
    EQUIPMENT_SLOT = "Head" if 1478 % 4 == 0 else ("Chest" if 1478 % 4 == 1 else ("Weapon" if 1478 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 17736
    REQUIRE_LEVEL = 30
    SELL_PRICE = 147800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1479:
    PREFAB_ID = "item_prefab_1479"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1479"
    EQUIPMENT_SLOT = "Head" if 1479 % 4 == 0 else ("Chest" if 1479 % 4 == 1 else ("Weapon" if 1479 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 17748
    REQUIRE_LEVEL = 30
    SELL_PRICE = 147900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1480:
    PREFAB_ID = "item_prefab_1480"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1480"
    EQUIPMENT_SLOT = "Head" if 1480 % 4 == 0 else ("Chest" if 1480 % 4 == 1 else ("Weapon" if 1480 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 17760
    REQUIRE_LEVEL = 30
    SELL_PRICE = 148000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1481:
    PREFAB_ID = "item_prefab_1481"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1481"
    EQUIPMENT_SLOT = "Head" if 1481 % 4 == 0 else ("Chest" if 1481 % 4 == 1 else ("Weapon" if 1481 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 17772
    REQUIRE_LEVEL = 30
    SELL_PRICE = 148100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1482:
    PREFAB_ID = "item_prefab_1482"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1482"
    EQUIPMENT_SLOT = "Head" if 1482 % 4 == 0 else ("Chest" if 1482 % 4 == 1 else ("Weapon" if 1482 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 17784
    REQUIRE_LEVEL = 30
    SELL_PRICE = 148200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1483:
    PREFAB_ID = "item_prefab_1483"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1483"
    EQUIPMENT_SLOT = "Head" if 1483 % 4 == 0 else ("Chest" if 1483 % 4 == 1 else ("Weapon" if 1483 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 17796
    REQUIRE_LEVEL = 30
    SELL_PRICE = 148300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1484:
    PREFAB_ID = "item_prefab_1484"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1484"
    EQUIPMENT_SLOT = "Head" if 1484 % 4 == 0 else ("Chest" if 1484 % 4 == 1 else ("Weapon" if 1484 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 17808
    REQUIRE_LEVEL = 30
    SELL_PRICE = 148400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1485:
    PREFAB_ID = "item_prefab_1485"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1485"
    EQUIPMENT_SLOT = "Head" if 1485 % 4 == 0 else ("Chest" if 1485 % 4 == 1 else ("Weapon" if 1485 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 17820
    REQUIRE_LEVEL = 30
    SELL_PRICE = 148500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1486:
    PREFAB_ID = "item_prefab_1486"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1486"
    EQUIPMENT_SLOT = "Head" if 1486 % 4 == 0 else ("Chest" if 1486 % 4 == 1 else ("Weapon" if 1486 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 17832
    REQUIRE_LEVEL = 30
    SELL_PRICE = 148600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1487:
    PREFAB_ID = "item_prefab_1487"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1487"
    EQUIPMENT_SLOT = "Head" if 1487 % 4 == 0 else ("Chest" if 1487 % 4 == 1 else ("Weapon" if 1487 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 17844
    REQUIRE_LEVEL = 30
    SELL_PRICE = 148700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1488:
    PREFAB_ID = "item_prefab_1488"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1488"
    EQUIPMENT_SLOT = "Head" if 1488 % 4 == 0 else ("Chest" if 1488 % 4 == 1 else ("Weapon" if 1488 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 17856
    REQUIRE_LEVEL = 30
    SELL_PRICE = 148800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1489:
    PREFAB_ID = "item_prefab_1489"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1489"
    EQUIPMENT_SLOT = "Head" if 1489 % 4 == 0 else ("Chest" if 1489 % 4 == 1 else ("Weapon" if 1489 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 17868
    REQUIRE_LEVEL = 30
    SELL_PRICE = 148900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1490:
    PREFAB_ID = "item_prefab_1490"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1490"
    EQUIPMENT_SLOT = "Head" if 1490 % 4 == 0 else ("Chest" if 1490 % 4 == 1 else ("Weapon" if 1490 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 17880
    REQUIRE_LEVEL = 30
    SELL_PRICE = 149000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1491:
    PREFAB_ID = "item_prefab_1491"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1491"
    EQUIPMENT_SLOT = "Head" if 1491 % 4 == 0 else ("Chest" if 1491 % 4 == 1 else ("Weapon" if 1491 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 17892
    REQUIRE_LEVEL = 30
    SELL_PRICE = 149100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1492:
    PREFAB_ID = "item_prefab_1492"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1492"
    EQUIPMENT_SLOT = "Head" if 1492 % 4 == 0 else ("Chest" if 1492 % 4 == 1 else ("Weapon" if 1492 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 17904
    REQUIRE_LEVEL = 30
    SELL_PRICE = 149200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1493:
    PREFAB_ID = "item_prefab_1493"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1493"
    EQUIPMENT_SLOT = "Head" if 1493 % 4 == 0 else ("Chest" if 1493 % 4 == 1 else ("Weapon" if 1493 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 17916
    REQUIRE_LEVEL = 30
    SELL_PRICE = 149300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1494:
    PREFAB_ID = "item_prefab_1494"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1494"
    EQUIPMENT_SLOT = "Head" if 1494 % 4 == 0 else ("Chest" if 1494 % 4 == 1 else ("Weapon" if 1494 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 17928
    REQUIRE_LEVEL = 30
    SELL_PRICE = 149400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1495:
    PREFAB_ID = "item_prefab_1495"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1495"
    EQUIPMENT_SLOT = "Head" if 1495 % 4 == 0 else ("Chest" if 1495 % 4 == 1 else ("Weapon" if 1495 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 17940
    REQUIRE_LEVEL = 30
    SELL_PRICE = 149500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1496:
    PREFAB_ID = "item_prefab_1496"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1496"
    EQUIPMENT_SLOT = "Head" if 1496 % 4 == 0 else ("Chest" if 1496 % 4 == 1 else ("Weapon" if 1496 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 17952
    REQUIRE_LEVEL = 30
    SELL_PRICE = 149600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1497:
    PREFAB_ID = "item_prefab_1497"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1497"
    EQUIPMENT_SLOT = "Head" if 1497 % 4 == 0 else ("Chest" if 1497 % 4 == 1 else ("Weapon" if 1497 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 17964
    REQUIRE_LEVEL = 30
    SELL_PRICE = 149700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1498:
    PREFAB_ID = "item_prefab_1498"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1498"
    EQUIPMENT_SLOT = "Head" if 1498 % 4 == 0 else ("Chest" if 1498 % 4 == 1 else ("Weapon" if 1498 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 17976
    REQUIRE_LEVEL = 30
    SELL_PRICE = 149800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1499:
    PREFAB_ID = "item_prefab_1499"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1499"
    EQUIPMENT_SLOT = "Head" if 1499 % 4 == 0 else ("Chest" if 1499 % 4 == 1 else ("Weapon" if 1499 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 17988
    REQUIRE_LEVEL = 30
    SELL_PRICE = 149900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1500:
    PREFAB_ID = "item_prefab_1500"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1500"
    EQUIPMENT_SLOT = "Head" if 1500 % 4 == 0 else ("Chest" if 1500 % 4 == 1 else ("Weapon" if 1500 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 18000
    REQUIRE_LEVEL = 31
    SELL_PRICE = 150000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1501:
    PREFAB_ID = "item_prefab_1501"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1501"
    EQUIPMENT_SLOT = "Head" if 1501 % 4 == 0 else ("Chest" if 1501 % 4 == 1 else ("Weapon" if 1501 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 18012
    REQUIRE_LEVEL = 31
    SELL_PRICE = 150100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1502:
    PREFAB_ID = "item_prefab_1502"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1502"
    EQUIPMENT_SLOT = "Head" if 1502 % 4 == 0 else ("Chest" if 1502 % 4 == 1 else ("Weapon" if 1502 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 18024
    REQUIRE_LEVEL = 31
    SELL_PRICE = 150200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1503:
    PREFAB_ID = "item_prefab_1503"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1503"
    EQUIPMENT_SLOT = "Head" if 1503 % 4 == 0 else ("Chest" if 1503 % 4 == 1 else ("Weapon" if 1503 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 18036
    REQUIRE_LEVEL = 31
    SELL_PRICE = 150300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1504:
    PREFAB_ID = "item_prefab_1504"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1504"
    EQUIPMENT_SLOT = "Head" if 1504 % 4 == 0 else ("Chest" if 1504 % 4 == 1 else ("Weapon" if 1504 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 18048
    REQUIRE_LEVEL = 31
    SELL_PRICE = 150400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1505:
    PREFAB_ID = "item_prefab_1505"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1505"
    EQUIPMENT_SLOT = "Head" if 1505 % 4 == 0 else ("Chest" if 1505 % 4 == 1 else ("Weapon" if 1505 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 18060
    REQUIRE_LEVEL = 31
    SELL_PRICE = 150500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1506:
    PREFAB_ID = "item_prefab_1506"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1506"
    EQUIPMENT_SLOT = "Head" if 1506 % 4 == 0 else ("Chest" if 1506 % 4 == 1 else ("Weapon" if 1506 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 18072
    REQUIRE_LEVEL = 31
    SELL_PRICE = 150600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1507:
    PREFAB_ID = "item_prefab_1507"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1507"
    EQUIPMENT_SLOT = "Head" if 1507 % 4 == 0 else ("Chest" if 1507 % 4 == 1 else ("Weapon" if 1507 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 18084
    REQUIRE_LEVEL = 31
    SELL_PRICE = 150700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1508:
    PREFAB_ID = "item_prefab_1508"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1508"
    EQUIPMENT_SLOT = "Head" if 1508 % 4 == 0 else ("Chest" if 1508 % 4 == 1 else ("Weapon" if 1508 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 18096
    REQUIRE_LEVEL = 31
    SELL_PRICE = 150800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1509:
    PREFAB_ID = "item_prefab_1509"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1509"
    EQUIPMENT_SLOT = "Head" if 1509 % 4 == 0 else ("Chest" if 1509 % 4 == 1 else ("Weapon" if 1509 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 18108
    REQUIRE_LEVEL = 31
    SELL_PRICE = 150900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1510:
    PREFAB_ID = "item_prefab_1510"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1510"
    EQUIPMENT_SLOT = "Head" if 1510 % 4 == 0 else ("Chest" if 1510 % 4 == 1 else ("Weapon" if 1510 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 18120
    REQUIRE_LEVEL = 31
    SELL_PRICE = 151000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1511:
    PREFAB_ID = "item_prefab_1511"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1511"
    EQUIPMENT_SLOT = "Head" if 1511 % 4 == 0 else ("Chest" if 1511 % 4 == 1 else ("Weapon" if 1511 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 18132
    REQUIRE_LEVEL = 31
    SELL_PRICE = 151100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1512:
    PREFAB_ID = "item_prefab_1512"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1512"
    EQUIPMENT_SLOT = "Head" if 1512 % 4 == 0 else ("Chest" if 1512 % 4 == 1 else ("Weapon" if 1512 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 18144
    REQUIRE_LEVEL = 31
    SELL_PRICE = 151200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1513:
    PREFAB_ID = "item_prefab_1513"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1513"
    EQUIPMENT_SLOT = "Head" if 1513 % 4 == 0 else ("Chest" if 1513 % 4 == 1 else ("Weapon" if 1513 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 18156
    REQUIRE_LEVEL = 31
    SELL_PRICE = 151300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1514:
    PREFAB_ID = "item_prefab_1514"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1514"
    EQUIPMENT_SLOT = "Head" if 1514 % 4 == 0 else ("Chest" if 1514 % 4 == 1 else ("Weapon" if 1514 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 18168
    REQUIRE_LEVEL = 31
    SELL_PRICE = 151400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1515:
    PREFAB_ID = "item_prefab_1515"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1515"
    EQUIPMENT_SLOT = "Head" if 1515 % 4 == 0 else ("Chest" if 1515 % 4 == 1 else ("Weapon" if 1515 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 18180
    REQUIRE_LEVEL = 31
    SELL_PRICE = 151500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1516:
    PREFAB_ID = "item_prefab_1516"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1516"
    EQUIPMENT_SLOT = "Head" if 1516 % 4 == 0 else ("Chest" if 1516 % 4 == 1 else ("Weapon" if 1516 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 18192
    REQUIRE_LEVEL = 31
    SELL_PRICE = 151600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1517:
    PREFAB_ID = "item_prefab_1517"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1517"
    EQUIPMENT_SLOT = "Head" if 1517 % 4 == 0 else ("Chest" if 1517 % 4 == 1 else ("Weapon" if 1517 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 18204
    REQUIRE_LEVEL = 31
    SELL_PRICE = 151700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1518:
    PREFAB_ID = "item_prefab_1518"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1518"
    EQUIPMENT_SLOT = "Head" if 1518 % 4 == 0 else ("Chest" if 1518 % 4 == 1 else ("Weapon" if 1518 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 18216
    REQUIRE_LEVEL = 31
    SELL_PRICE = 151800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1519:
    PREFAB_ID = "item_prefab_1519"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1519"
    EQUIPMENT_SLOT = "Head" if 1519 % 4 == 0 else ("Chest" if 1519 % 4 == 1 else ("Weapon" if 1519 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 18228
    REQUIRE_LEVEL = 31
    SELL_PRICE = 151900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1520:
    PREFAB_ID = "item_prefab_1520"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1520"
    EQUIPMENT_SLOT = "Head" if 1520 % 4 == 0 else ("Chest" if 1520 % 4 == 1 else ("Weapon" if 1520 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 18240
    REQUIRE_LEVEL = 31
    SELL_PRICE = 152000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1521:
    PREFAB_ID = "item_prefab_1521"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1521"
    EQUIPMENT_SLOT = "Head" if 1521 % 4 == 0 else ("Chest" if 1521 % 4 == 1 else ("Weapon" if 1521 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 18252
    REQUIRE_LEVEL = 31
    SELL_PRICE = 152100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1522:
    PREFAB_ID = "item_prefab_1522"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1522"
    EQUIPMENT_SLOT = "Head" if 1522 % 4 == 0 else ("Chest" if 1522 % 4 == 1 else ("Weapon" if 1522 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 18264
    REQUIRE_LEVEL = 31
    SELL_PRICE = 152200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1523:
    PREFAB_ID = "item_prefab_1523"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1523"
    EQUIPMENT_SLOT = "Head" if 1523 % 4 == 0 else ("Chest" if 1523 % 4 == 1 else ("Weapon" if 1523 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 18276
    REQUIRE_LEVEL = 31
    SELL_PRICE = 152300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1524:
    PREFAB_ID = "item_prefab_1524"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1524"
    EQUIPMENT_SLOT = "Head" if 1524 % 4 == 0 else ("Chest" if 1524 % 4 == 1 else ("Weapon" if 1524 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 18288
    REQUIRE_LEVEL = 31
    SELL_PRICE = 152400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1525:
    PREFAB_ID = "item_prefab_1525"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1525"
    EQUIPMENT_SLOT = "Head" if 1525 % 4 == 0 else ("Chest" if 1525 % 4 == 1 else ("Weapon" if 1525 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 18300
    REQUIRE_LEVEL = 31
    SELL_PRICE = 152500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1526:
    PREFAB_ID = "item_prefab_1526"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1526"
    EQUIPMENT_SLOT = "Head" if 1526 % 4 == 0 else ("Chest" if 1526 % 4 == 1 else ("Weapon" if 1526 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 18312
    REQUIRE_LEVEL = 31
    SELL_PRICE = 152600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1527:
    PREFAB_ID = "item_prefab_1527"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1527"
    EQUIPMENT_SLOT = "Head" if 1527 % 4 == 0 else ("Chest" if 1527 % 4 == 1 else ("Weapon" if 1527 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 18324
    REQUIRE_LEVEL = 31
    SELL_PRICE = 152700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1528:
    PREFAB_ID = "item_prefab_1528"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1528"
    EQUIPMENT_SLOT = "Head" if 1528 % 4 == 0 else ("Chest" if 1528 % 4 == 1 else ("Weapon" if 1528 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 18336
    REQUIRE_LEVEL = 31
    SELL_PRICE = 152800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1529:
    PREFAB_ID = "item_prefab_1529"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1529"
    EQUIPMENT_SLOT = "Head" if 1529 % 4 == 0 else ("Chest" if 1529 % 4 == 1 else ("Weapon" if 1529 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 18348
    REQUIRE_LEVEL = 31
    SELL_PRICE = 152900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1530:
    PREFAB_ID = "item_prefab_1530"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1530"
    EQUIPMENT_SLOT = "Head" if 1530 % 4 == 0 else ("Chest" if 1530 % 4 == 1 else ("Weapon" if 1530 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 18360
    REQUIRE_LEVEL = 31
    SELL_PRICE = 153000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1531:
    PREFAB_ID = "item_prefab_1531"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1531"
    EQUIPMENT_SLOT = "Head" if 1531 % 4 == 0 else ("Chest" if 1531 % 4 == 1 else ("Weapon" if 1531 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 18372
    REQUIRE_LEVEL = 31
    SELL_PRICE = 153100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1532:
    PREFAB_ID = "item_prefab_1532"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1532"
    EQUIPMENT_SLOT = "Head" if 1532 % 4 == 0 else ("Chest" if 1532 % 4 == 1 else ("Weapon" if 1532 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 18384
    REQUIRE_LEVEL = 31
    SELL_PRICE = 153200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1533:
    PREFAB_ID = "item_prefab_1533"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1533"
    EQUIPMENT_SLOT = "Head" if 1533 % 4 == 0 else ("Chest" if 1533 % 4 == 1 else ("Weapon" if 1533 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 18396
    REQUIRE_LEVEL = 31
    SELL_PRICE = 153300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1534:
    PREFAB_ID = "item_prefab_1534"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1534"
    EQUIPMENT_SLOT = "Head" if 1534 % 4 == 0 else ("Chest" if 1534 % 4 == 1 else ("Weapon" if 1534 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 18408
    REQUIRE_LEVEL = 31
    SELL_PRICE = 153400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1535:
    PREFAB_ID = "item_prefab_1535"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1535"
    EQUIPMENT_SLOT = "Head" if 1535 % 4 == 0 else ("Chest" if 1535 % 4 == 1 else ("Weapon" if 1535 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 18420
    REQUIRE_LEVEL = 31
    SELL_PRICE = 153500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1536:
    PREFAB_ID = "item_prefab_1536"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1536"
    EQUIPMENT_SLOT = "Head" if 1536 % 4 == 0 else ("Chest" if 1536 % 4 == 1 else ("Weapon" if 1536 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 18432
    REQUIRE_LEVEL = 31
    SELL_PRICE = 153600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1537:
    PREFAB_ID = "item_prefab_1537"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1537"
    EQUIPMENT_SLOT = "Head" if 1537 % 4 == 0 else ("Chest" if 1537 % 4 == 1 else ("Weapon" if 1537 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 18444
    REQUIRE_LEVEL = 31
    SELL_PRICE = 153700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1538:
    PREFAB_ID = "item_prefab_1538"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1538"
    EQUIPMENT_SLOT = "Head" if 1538 % 4 == 0 else ("Chest" if 1538 % 4 == 1 else ("Weapon" if 1538 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 18456
    REQUIRE_LEVEL = 31
    SELL_PRICE = 153800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1539:
    PREFAB_ID = "item_prefab_1539"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1539"
    EQUIPMENT_SLOT = "Head" if 1539 % 4 == 0 else ("Chest" if 1539 % 4 == 1 else ("Weapon" if 1539 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 18468
    REQUIRE_LEVEL = 31
    SELL_PRICE = 153900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1540:
    PREFAB_ID = "item_prefab_1540"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1540"
    EQUIPMENT_SLOT = "Head" if 1540 % 4 == 0 else ("Chest" if 1540 % 4 == 1 else ("Weapon" if 1540 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 18480
    REQUIRE_LEVEL = 31
    SELL_PRICE = 154000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1541:
    PREFAB_ID = "item_prefab_1541"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1541"
    EQUIPMENT_SLOT = "Head" if 1541 % 4 == 0 else ("Chest" if 1541 % 4 == 1 else ("Weapon" if 1541 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 18492
    REQUIRE_LEVEL = 31
    SELL_PRICE = 154100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1542:
    PREFAB_ID = "item_prefab_1542"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1542"
    EQUIPMENT_SLOT = "Head" if 1542 % 4 == 0 else ("Chest" if 1542 % 4 == 1 else ("Weapon" if 1542 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 18504
    REQUIRE_LEVEL = 31
    SELL_PRICE = 154200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1543:
    PREFAB_ID = "item_prefab_1543"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1543"
    EQUIPMENT_SLOT = "Head" if 1543 % 4 == 0 else ("Chest" if 1543 % 4 == 1 else ("Weapon" if 1543 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 18516
    REQUIRE_LEVEL = 31
    SELL_PRICE = 154300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1544:
    PREFAB_ID = "item_prefab_1544"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1544"
    EQUIPMENT_SLOT = "Head" if 1544 % 4 == 0 else ("Chest" if 1544 % 4 == 1 else ("Weapon" if 1544 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 18528
    REQUIRE_LEVEL = 31
    SELL_PRICE = 154400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1545:
    PREFAB_ID = "item_prefab_1545"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1545"
    EQUIPMENT_SLOT = "Head" if 1545 % 4 == 0 else ("Chest" if 1545 % 4 == 1 else ("Weapon" if 1545 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 18540
    REQUIRE_LEVEL = 31
    SELL_PRICE = 154500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1546:
    PREFAB_ID = "item_prefab_1546"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1546"
    EQUIPMENT_SLOT = "Head" if 1546 % 4 == 0 else ("Chest" if 1546 % 4 == 1 else ("Weapon" if 1546 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 18552
    REQUIRE_LEVEL = 31
    SELL_PRICE = 154600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1547:
    PREFAB_ID = "item_prefab_1547"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1547"
    EQUIPMENT_SLOT = "Head" if 1547 % 4 == 0 else ("Chest" if 1547 % 4 == 1 else ("Weapon" if 1547 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 18564
    REQUIRE_LEVEL = 31
    SELL_PRICE = 154700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1548:
    PREFAB_ID = "item_prefab_1548"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1548"
    EQUIPMENT_SLOT = "Head" if 1548 % 4 == 0 else ("Chest" if 1548 % 4 == 1 else ("Weapon" if 1548 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 18576
    REQUIRE_LEVEL = 31
    SELL_PRICE = 154800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1549:
    PREFAB_ID = "item_prefab_1549"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1549"
    EQUIPMENT_SLOT = "Head" if 1549 % 4 == 0 else ("Chest" if 1549 % 4 == 1 else ("Weapon" if 1549 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 18588
    REQUIRE_LEVEL = 31
    SELL_PRICE = 154900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1550:
    PREFAB_ID = "item_prefab_1550"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1550"
    EQUIPMENT_SLOT = "Head" if 1550 % 4 == 0 else ("Chest" if 1550 % 4 == 1 else ("Weapon" if 1550 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 18600
    REQUIRE_LEVEL = 32
    SELL_PRICE = 155000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1551:
    PREFAB_ID = "item_prefab_1551"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1551"
    EQUIPMENT_SLOT = "Head" if 1551 % 4 == 0 else ("Chest" if 1551 % 4 == 1 else ("Weapon" if 1551 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 18612
    REQUIRE_LEVEL = 32
    SELL_PRICE = 155100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1552:
    PREFAB_ID = "item_prefab_1552"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1552"
    EQUIPMENT_SLOT = "Head" if 1552 % 4 == 0 else ("Chest" if 1552 % 4 == 1 else ("Weapon" if 1552 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 18624
    REQUIRE_LEVEL = 32
    SELL_PRICE = 155200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1553:
    PREFAB_ID = "item_prefab_1553"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1553"
    EQUIPMENT_SLOT = "Head" if 1553 % 4 == 0 else ("Chest" if 1553 % 4 == 1 else ("Weapon" if 1553 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 18636
    REQUIRE_LEVEL = 32
    SELL_PRICE = 155300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1554:
    PREFAB_ID = "item_prefab_1554"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1554"
    EQUIPMENT_SLOT = "Head" if 1554 % 4 == 0 else ("Chest" if 1554 % 4 == 1 else ("Weapon" if 1554 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 18648
    REQUIRE_LEVEL = 32
    SELL_PRICE = 155400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1555:
    PREFAB_ID = "item_prefab_1555"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1555"
    EQUIPMENT_SLOT = "Head" if 1555 % 4 == 0 else ("Chest" if 1555 % 4 == 1 else ("Weapon" if 1555 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 18660
    REQUIRE_LEVEL = 32
    SELL_PRICE = 155500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1556:
    PREFAB_ID = "item_prefab_1556"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1556"
    EQUIPMENT_SLOT = "Head" if 1556 % 4 == 0 else ("Chest" if 1556 % 4 == 1 else ("Weapon" if 1556 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 18672
    REQUIRE_LEVEL = 32
    SELL_PRICE = 155600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1557:
    PREFAB_ID = "item_prefab_1557"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1557"
    EQUIPMENT_SLOT = "Head" if 1557 % 4 == 0 else ("Chest" if 1557 % 4 == 1 else ("Weapon" if 1557 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 18684
    REQUIRE_LEVEL = 32
    SELL_PRICE = 155700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1558:
    PREFAB_ID = "item_prefab_1558"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1558"
    EQUIPMENT_SLOT = "Head" if 1558 % 4 == 0 else ("Chest" if 1558 % 4 == 1 else ("Weapon" if 1558 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 18696
    REQUIRE_LEVEL = 32
    SELL_PRICE = 155800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1559:
    PREFAB_ID = "item_prefab_1559"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1559"
    EQUIPMENT_SLOT = "Head" if 1559 % 4 == 0 else ("Chest" if 1559 % 4 == 1 else ("Weapon" if 1559 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 18708
    REQUIRE_LEVEL = 32
    SELL_PRICE = 155900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1560:
    PREFAB_ID = "item_prefab_1560"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1560"
    EQUIPMENT_SLOT = "Head" if 1560 % 4 == 0 else ("Chest" if 1560 % 4 == 1 else ("Weapon" if 1560 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 18720
    REQUIRE_LEVEL = 32
    SELL_PRICE = 156000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1561:
    PREFAB_ID = "item_prefab_1561"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1561"
    EQUIPMENT_SLOT = "Head" if 1561 % 4 == 0 else ("Chest" if 1561 % 4 == 1 else ("Weapon" if 1561 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 18732
    REQUIRE_LEVEL = 32
    SELL_PRICE = 156100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1562:
    PREFAB_ID = "item_prefab_1562"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1562"
    EQUIPMENT_SLOT = "Head" if 1562 % 4 == 0 else ("Chest" if 1562 % 4 == 1 else ("Weapon" if 1562 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 18744
    REQUIRE_LEVEL = 32
    SELL_PRICE = 156200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1563:
    PREFAB_ID = "item_prefab_1563"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1563"
    EQUIPMENT_SLOT = "Head" if 1563 % 4 == 0 else ("Chest" if 1563 % 4 == 1 else ("Weapon" if 1563 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 18756
    REQUIRE_LEVEL = 32
    SELL_PRICE = 156300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1564:
    PREFAB_ID = "item_prefab_1564"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1564"
    EQUIPMENT_SLOT = "Head" if 1564 % 4 == 0 else ("Chest" if 1564 % 4 == 1 else ("Weapon" if 1564 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 18768
    REQUIRE_LEVEL = 32
    SELL_PRICE = 156400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1565:
    PREFAB_ID = "item_prefab_1565"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1565"
    EQUIPMENT_SLOT = "Head" if 1565 % 4 == 0 else ("Chest" if 1565 % 4 == 1 else ("Weapon" if 1565 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 18780
    REQUIRE_LEVEL = 32
    SELL_PRICE = 156500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1566:
    PREFAB_ID = "item_prefab_1566"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1566"
    EQUIPMENT_SLOT = "Head" if 1566 % 4 == 0 else ("Chest" if 1566 % 4 == 1 else ("Weapon" if 1566 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 18792
    REQUIRE_LEVEL = 32
    SELL_PRICE = 156600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1567:
    PREFAB_ID = "item_prefab_1567"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1567"
    EQUIPMENT_SLOT = "Head" if 1567 % 4 == 0 else ("Chest" if 1567 % 4 == 1 else ("Weapon" if 1567 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 18804
    REQUIRE_LEVEL = 32
    SELL_PRICE = 156700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1568:
    PREFAB_ID = "item_prefab_1568"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1568"
    EQUIPMENT_SLOT = "Head" if 1568 % 4 == 0 else ("Chest" if 1568 % 4 == 1 else ("Weapon" if 1568 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 18816
    REQUIRE_LEVEL = 32
    SELL_PRICE = 156800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1569:
    PREFAB_ID = "item_prefab_1569"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1569"
    EQUIPMENT_SLOT = "Head" if 1569 % 4 == 0 else ("Chest" if 1569 % 4 == 1 else ("Weapon" if 1569 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 18828
    REQUIRE_LEVEL = 32
    SELL_PRICE = 156900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1570:
    PREFAB_ID = "item_prefab_1570"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1570"
    EQUIPMENT_SLOT = "Head" if 1570 % 4 == 0 else ("Chest" if 1570 % 4 == 1 else ("Weapon" if 1570 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 18840
    REQUIRE_LEVEL = 32
    SELL_PRICE = 157000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1571:
    PREFAB_ID = "item_prefab_1571"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1571"
    EQUIPMENT_SLOT = "Head" if 1571 % 4 == 0 else ("Chest" if 1571 % 4 == 1 else ("Weapon" if 1571 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 18852
    REQUIRE_LEVEL = 32
    SELL_PRICE = 157100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1572:
    PREFAB_ID = "item_prefab_1572"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1572"
    EQUIPMENT_SLOT = "Head" if 1572 % 4 == 0 else ("Chest" if 1572 % 4 == 1 else ("Weapon" if 1572 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 18864
    REQUIRE_LEVEL = 32
    SELL_PRICE = 157200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1573:
    PREFAB_ID = "item_prefab_1573"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1573"
    EQUIPMENT_SLOT = "Head" if 1573 % 4 == 0 else ("Chest" if 1573 % 4 == 1 else ("Weapon" if 1573 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 18876
    REQUIRE_LEVEL = 32
    SELL_PRICE = 157300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1574:
    PREFAB_ID = "item_prefab_1574"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1574"
    EQUIPMENT_SLOT = "Head" if 1574 % 4 == 0 else ("Chest" if 1574 % 4 == 1 else ("Weapon" if 1574 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 18888
    REQUIRE_LEVEL = 32
    SELL_PRICE = 157400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1575:
    PREFAB_ID = "item_prefab_1575"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1575"
    EQUIPMENT_SLOT = "Head" if 1575 % 4 == 0 else ("Chest" if 1575 % 4 == 1 else ("Weapon" if 1575 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 18900
    REQUIRE_LEVEL = 32
    SELL_PRICE = 157500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1576:
    PREFAB_ID = "item_prefab_1576"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1576"
    EQUIPMENT_SLOT = "Head" if 1576 % 4 == 0 else ("Chest" if 1576 % 4 == 1 else ("Weapon" if 1576 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 18912
    REQUIRE_LEVEL = 32
    SELL_PRICE = 157600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1577:
    PREFAB_ID = "item_prefab_1577"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1577"
    EQUIPMENT_SLOT = "Head" if 1577 % 4 == 0 else ("Chest" if 1577 % 4 == 1 else ("Weapon" if 1577 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 18924
    REQUIRE_LEVEL = 32
    SELL_PRICE = 157700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1578:
    PREFAB_ID = "item_prefab_1578"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1578"
    EQUIPMENT_SLOT = "Head" if 1578 % 4 == 0 else ("Chest" if 1578 % 4 == 1 else ("Weapon" if 1578 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 18936
    REQUIRE_LEVEL = 32
    SELL_PRICE = 157800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1579:
    PREFAB_ID = "item_prefab_1579"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1579"
    EQUIPMENT_SLOT = "Head" if 1579 % 4 == 0 else ("Chest" if 1579 % 4 == 1 else ("Weapon" if 1579 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 18948
    REQUIRE_LEVEL = 32
    SELL_PRICE = 157900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1580:
    PREFAB_ID = "item_prefab_1580"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1580"
    EQUIPMENT_SLOT = "Head" if 1580 % 4 == 0 else ("Chest" if 1580 % 4 == 1 else ("Weapon" if 1580 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 18960
    REQUIRE_LEVEL = 32
    SELL_PRICE = 158000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1581:
    PREFAB_ID = "item_prefab_1581"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1581"
    EQUIPMENT_SLOT = "Head" if 1581 % 4 == 0 else ("Chest" if 1581 % 4 == 1 else ("Weapon" if 1581 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 18972
    REQUIRE_LEVEL = 32
    SELL_PRICE = 158100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1582:
    PREFAB_ID = "item_prefab_1582"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1582"
    EQUIPMENT_SLOT = "Head" if 1582 % 4 == 0 else ("Chest" if 1582 % 4 == 1 else ("Weapon" if 1582 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 18984
    REQUIRE_LEVEL = 32
    SELL_PRICE = 158200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1583:
    PREFAB_ID = "item_prefab_1583"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1583"
    EQUIPMENT_SLOT = "Head" if 1583 % 4 == 0 else ("Chest" if 1583 % 4 == 1 else ("Weapon" if 1583 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 18996
    REQUIRE_LEVEL = 32
    SELL_PRICE = 158300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1584:
    PREFAB_ID = "item_prefab_1584"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1584"
    EQUIPMENT_SLOT = "Head" if 1584 % 4 == 0 else ("Chest" if 1584 % 4 == 1 else ("Weapon" if 1584 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 19008
    REQUIRE_LEVEL = 32
    SELL_PRICE = 158400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1585:
    PREFAB_ID = "item_prefab_1585"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1585"
    EQUIPMENT_SLOT = "Head" if 1585 % 4 == 0 else ("Chest" if 1585 % 4 == 1 else ("Weapon" if 1585 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 19020
    REQUIRE_LEVEL = 32
    SELL_PRICE = 158500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1586:
    PREFAB_ID = "item_prefab_1586"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1586"
    EQUIPMENT_SLOT = "Head" if 1586 % 4 == 0 else ("Chest" if 1586 % 4 == 1 else ("Weapon" if 1586 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 19032
    REQUIRE_LEVEL = 32
    SELL_PRICE = 158600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1587:
    PREFAB_ID = "item_prefab_1587"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1587"
    EQUIPMENT_SLOT = "Head" if 1587 % 4 == 0 else ("Chest" if 1587 % 4 == 1 else ("Weapon" if 1587 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 19044
    REQUIRE_LEVEL = 32
    SELL_PRICE = 158700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1588:
    PREFAB_ID = "item_prefab_1588"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1588"
    EQUIPMENT_SLOT = "Head" if 1588 % 4 == 0 else ("Chest" if 1588 % 4 == 1 else ("Weapon" if 1588 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 19056
    REQUIRE_LEVEL = 32
    SELL_PRICE = 158800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1589:
    PREFAB_ID = "item_prefab_1589"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1589"
    EQUIPMENT_SLOT = "Head" if 1589 % 4 == 0 else ("Chest" if 1589 % 4 == 1 else ("Weapon" if 1589 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 19068
    REQUIRE_LEVEL = 32
    SELL_PRICE = 158900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1590:
    PREFAB_ID = "item_prefab_1590"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1590"
    EQUIPMENT_SLOT = "Head" if 1590 % 4 == 0 else ("Chest" if 1590 % 4 == 1 else ("Weapon" if 1590 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 19080
    REQUIRE_LEVEL = 32
    SELL_PRICE = 159000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1591:
    PREFAB_ID = "item_prefab_1591"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1591"
    EQUIPMENT_SLOT = "Head" if 1591 % 4 == 0 else ("Chest" if 1591 % 4 == 1 else ("Weapon" if 1591 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 19092
    REQUIRE_LEVEL = 32
    SELL_PRICE = 159100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1592:
    PREFAB_ID = "item_prefab_1592"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1592"
    EQUIPMENT_SLOT = "Head" if 1592 % 4 == 0 else ("Chest" if 1592 % 4 == 1 else ("Weapon" if 1592 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 19104
    REQUIRE_LEVEL = 32
    SELL_PRICE = 159200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1593:
    PREFAB_ID = "item_prefab_1593"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1593"
    EQUIPMENT_SLOT = "Head" if 1593 % 4 == 0 else ("Chest" if 1593 % 4 == 1 else ("Weapon" if 1593 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 19116
    REQUIRE_LEVEL = 32
    SELL_PRICE = 159300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1594:
    PREFAB_ID = "item_prefab_1594"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1594"
    EQUIPMENT_SLOT = "Head" if 1594 % 4 == 0 else ("Chest" if 1594 % 4 == 1 else ("Weapon" if 1594 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 19128
    REQUIRE_LEVEL = 32
    SELL_PRICE = 159400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1595:
    PREFAB_ID = "item_prefab_1595"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1595"
    EQUIPMENT_SLOT = "Head" if 1595 % 4 == 0 else ("Chest" if 1595 % 4 == 1 else ("Weapon" if 1595 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 19140
    REQUIRE_LEVEL = 32
    SELL_PRICE = 159500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1596:
    PREFAB_ID = "item_prefab_1596"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1596"
    EQUIPMENT_SLOT = "Head" if 1596 % 4 == 0 else ("Chest" if 1596 % 4 == 1 else ("Weapon" if 1596 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 19152
    REQUIRE_LEVEL = 32
    SELL_PRICE = 159600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1597:
    PREFAB_ID = "item_prefab_1597"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1597"
    EQUIPMENT_SLOT = "Head" if 1597 % 4 == 0 else ("Chest" if 1597 % 4 == 1 else ("Weapon" if 1597 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 19164
    REQUIRE_LEVEL = 32
    SELL_PRICE = 159700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1598:
    PREFAB_ID = "item_prefab_1598"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1598"
    EQUIPMENT_SLOT = "Head" if 1598 % 4 == 0 else ("Chest" if 1598 % 4 == 1 else ("Weapon" if 1598 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 19176
    REQUIRE_LEVEL = 32
    SELL_PRICE = 159800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1599:
    PREFAB_ID = "item_prefab_1599"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1599"
    EQUIPMENT_SLOT = "Head" if 1599 % 4 == 0 else ("Chest" if 1599 % 4 == 1 else ("Weapon" if 1599 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 19188
    REQUIRE_LEVEL = 32
    SELL_PRICE = 159900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1600:
    PREFAB_ID = "item_prefab_1600"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1600"
    EQUIPMENT_SLOT = "Head" if 1600 % 4 == 0 else ("Chest" if 1600 % 4 == 1 else ("Weapon" if 1600 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 19200
    REQUIRE_LEVEL = 33
    SELL_PRICE = 160000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1601:
    PREFAB_ID = "item_prefab_1601"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1601"
    EQUIPMENT_SLOT = "Head" if 1601 % 4 == 0 else ("Chest" if 1601 % 4 == 1 else ("Weapon" if 1601 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 19212
    REQUIRE_LEVEL = 33
    SELL_PRICE = 160100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1602:
    PREFAB_ID = "item_prefab_1602"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1602"
    EQUIPMENT_SLOT = "Head" if 1602 % 4 == 0 else ("Chest" if 1602 % 4 == 1 else ("Weapon" if 1602 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 19224
    REQUIRE_LEVEL = 33
    SELL_PRICE = 160200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1603:
    PREFAB_ID = "item_prefab_1603"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1603"
    EQUIPMENT_SLOT = "Head" if 1603 % 4 == 0 else ("Chest" if 1603 % 4 == 1 else ("Weapon" if 1603 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 19236
    REQUIRE_LEVEL = 33
    SELL_PRICE = 160300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1604:
    PREFAB_ID = "item_prefab_1604"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1604"
    EQUIPMENT_SLOT = "Head" if 1604 % 4 == 0 else ("Chest" if 1604 % 4 == 1 else ("Weapon" if 1604 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 19248
    REQUIRE_LEVEL = 33
    SELL_PRICE = 160400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1605:
    PREFAB_ID = "item_prefab_1605"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1605"
    EQUIPMENT_SLOT = "Head" if 1605 % 4 == 0 else ("Chest" if 1605 % 4 == 1 else ("Weapon" if 1605 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 19260
    REQUIRE_LEVEL = 33
    SELL_PRICE = 160500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1606:
    PREFAB_ID = "item_prefab_1606"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1606"
    EQUIPMENT_SLOT = "Head" if 1606 % 4 == 0 else ("Chest" if 1606 % 4 == 1 else ("Weapon" if 1606 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 19272
    REQUIRE_LEVEL = 33
    SELL_PRICE = 160600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1607:
    PREFAB_ID = "item_prefab_1607"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1607"
    EQUIPMENT_SLOT = "Head" if 1607 % 4 == 0 else ("Chest" if 1607 % 4 == 1 else ("Weapon" if 1607 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 19284
    REQUIRE_LEVEL = 33
    SELL_PRICE = 160700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1608:
    PREFAB_ID = "item_prefab_1608"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1608"
    EQUIPMENT_SLOT = "Head" if 1608 % 4 == 0 else ("Chest" if 1608 % 4 == 1 else ("Weapon" if 1608 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 19296
    REQUIRE_LEVEL = 33
    SELL_PRICE = 160800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1609:
    PREFAB_ID = "item_prefab_1609"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1609"
    EQUIPMENT_SLOT = "Head" if 1609 % 4 == 0 else ("Chest" if 1609 % 4 == 1 else ("Weapon" if 1609 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 19308
    REQUIRE_LEVEL = 33
    SELL_PRICE = 160900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1610:
    PREFAB_ID = "item_prefab_1610"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1610"
    EQUIPMENT_SLOT = "Head" if 1610 % 4 == 0 else ("Chest" if 1610 % 4 == 1 else ("Weapon" if 1610 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 19320
    REQUIRE_LEVEL = 33
    SELL_PRICE = 161000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1611:
    PREFAB_ID = "item_prefab_1611"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1611"
    EQUIPMENT_SLOT = "Head" if 1611 % 4 == 0 else ("Chest" if 1611 % 4 == 1 else ("Weapon" if 1611 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 19332
    REQUIRE_LEVEL = 33
    SELL_PRICE = 161100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1612:
    PREFAB_ID = "item_prefab_1612"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1612"
    EQUIPMENT_SLOT = "Head" if 1612 % 4 == 0 else ("Chest" if 1612 % 4 == 1 else ("Weapon" if 1612 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 19344
    REQUIRE_LEVEL = 33
    SELL_PRICE = 161200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1613:
    PREFAB_ID = "item_prefab_1613"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1613"
    EQUIPMENT_SLOT = "Head" if 1613 % 4 == 0 else ("Chest" if 1613 % 4 == 1 else ("Weapon" if 1613 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 19356
    REQUIRE_LEVEL = 33
    SELL_PRICE = 161300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1614:
    PREFAB_ID = "item_prefab_1614"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1614"
    EQUIPMENT_SLOT = "Head" if 1614 % 4 == 0 else ("Chest" if 1614 % 4 == 1 else ("Weapon" if 1614 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 19368
    REQUIRE_LEVEL = 33
    SELL_PRICE = 161400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1615:
    PREFAB_ID = "item_prefab_1615"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1615"
    EQUIPMENT_SLOT = "Head" if 1615 % 4 == 0 else ("Chest" if 1615 % 4 == 1 else ("Weapon" if 1615 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 19380
    REQUIRE_LEVEL = 33
    SELL_PRICE = 161500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1616:
    PREFAB_ID = "item_prefab_1616"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1616"
    EQUIPMENT_SLOT = "Head" if 1616 % 4 == 0 else ("Chest" if 1616 % 4 == 1 else ("Weapon" if 1616 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 19392
    REQUIRE_LEVEL = 33
    SELL_PRICE = 161600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1617:
    PREFAB_ID = "item_prefab_1617"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1617"
    EQUIPMENT_SLOT = "Head" if 1617 % 4 == 0 else ("Chest" if 1617 % 4 == 1 else ("Weapon" if 1617 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 19404
    REQUIRE_LEVEL = 33
    SELL_PRICE = 161700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1618:
    PREFAB_ID = "item_prefab_1618"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1618"
    EQUIPMENT_SLOT = "Head" if 1618 % 4 == 0 else ("Chest" if 1618 % 4 == 1 else ("Weapon" if 1618 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 19416
    REQUIRE_LEVEL = 33
    SELL_PRICE = 161800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1619:
    PREFAB_ID = "item_prefab_1619"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1619"
    EQUIPMENT_SLOT = "Head" if 1619 % 4 == 0 else ("Chest" if 1619 % 4 == 1 else ("Weapon" if 1619 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 19428
    REQUIRE_LEVEL = 33
    SELL_PRICE = 161900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1620:
    PREFAB_ID = "item_prefab_1620"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1620"
    EQUIPMENT_SLOT = "Head" if 1620 % 4 == 0 else ("Chest" if 1620 % 4 == 1 else ("Weapon" if 1620 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 19440
    REQUIRE_LEVEL = 33
    SELL_PRICE = 162000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1621:
    PREFAB_ID = "item_prefab_1621"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1621"
    EQUIPMENT_SLOT = "Head" if 1621 % 4 == 0 else ("Chest" if 1621 % 4 == 1 else ("Weapon" if 1621 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 19452
    REQUIRE_LEVEL = 33
    SELL_PRICE = 162100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1622:
    PREFAB_ID = "item_prefab_1622"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1622"
    EQUIPMENT_SLOT = "Head" if 1622 % 4 == 0 else ("Chest" if 1622 % 4 == 1 else ("Weapon" if 1622 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 19464
    REQUIRE_LEVEL = 33
    SELL_PRICE = 162200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1623:
    PREFAB_ID = "item_prefab_1623"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1623"
    EQUIPMENT_SLOT = "Head" if 1623 % 4 == 0 else ("Chest" if 1623 % 4 == 1 else ("Weapon" if 1623 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 19476
    REQUIRE_LEVEL = 33
    SELL_PRICE = 162300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1624:
    PREFAB_ID = "item_prefab_1624"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1624"
    EQUIPMENT_SLOT = "Head" if 1624 % 4 == 0 else ("Chest" if 1624 % 4 == 1 else ("Weapon" if 1624 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 19488
    REQUIRE_LEVEL = 33
    SELL_PRICE = 162400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1625:
    PREFAB_ID = "item_prefab_1625"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1625"
    EQUIPMENT_SLOT = "Head" if 1625 % 4 == 0 else ("Chest" if 1625 % 4 == 1 else ("Weapon" if 1625 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 19500
    REQUIRE_LEVEL = 33
    SELL_PRICE = 162500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1626:
    PREFAB_ID = "item_prefab_1626"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1626"
    EQUIPMENT_SLOT = "Head" if 1626 % 4 == 0 else ("Chest" if 1626 % 4 == 1 else ("Weapon" if 1626 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 19512
    REQUIRE_LEVEL = 33
    SELL_PRICE = 162600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1627:
    PREFAB_ID = "item_prefab_1627"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1627"
    EQUIPMENT_SLOT = "Head" if 1627 % 4 == 0 else ("Chest" if 1627 % 4 == 1 else ("Weapon" if 1627 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 19524
    REQUIRE_LEVEL = 33
    SELL_PRICE = 162700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1628:
    PREFAB_ID = "item_prefab_1628"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1628"
    EQUIPMENT_SLOT = "Head" if 1628 % 4 == 0 else ("Chest" if 1628 % 4 == 1 else ("Weapon" if 1628 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 19536
    REQUIRE_LEVEL = 33
    SELL_PRICE = 162800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1629:
    PREFAB_ID = "item_prefab_1629"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1629"
    EQUIPMENT_SLOT = "Head" if 1629 % 4 == 0 else ("Chest" if 1629 % 4 == 1 else ("Weapon" if 1629 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 19548
    REQUIRE_LEVEL = 33
    SELL_PRICE = 162900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1630:
    PREFAB_ID = "item_prefab_1630"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1630"
    EQUIPMENT_SLOT = "Head" if 1630 % 4 == 0 else ("Chest" if 1630 % 4 == 1 else ("Weapon" if 1630 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 19560
    REQUIRE_LEVEL = 33
    SELL_PRICE = 163000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1631:
    PREFAB_ID = "item_prefab_1631"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1631"
    EQUIPMENT_SLOT = "Head" if 1631 % 4 == 0 else ("Chest" if 1631 % 4 == 1 else ("Weapon" if 1631 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 19572
    REQUIRE_LEVEL = 33
    SELL_PRICE = 163100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1632:
    PREFAB_ID = "item_prefab_1632"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1632"
    EQUIPMENT_SLOT = "Head" if 1632 % 4 == 0 else ("Chest" if 1632 % 4 == 1 else ("Weapon" if 1632 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 19584
    REQUIRE_LEVEL = 33
    SELL_PRICE = 163200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1633:
    PREFAB_ID = "item_prefab_1633"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1633"
    EQUIPMENT_SLOT = "Head" if 1633 % 4 == 0 else ("Chest" if 1633 % 4 == 1 else ("Weapon" if 1633 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 19596
    REQUIRE_LEVEL = 33
    SELL_PRICE = 163300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1634:
    PREFAB_ID = "item_prefab_1634"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1634"
    EQUIPMENT_SLOT = "Head" if 1634 % 4 == 0 else ("Chest" if 1634 % 4 == 1 else ("Weapon" if 1634 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 19608
    REQUIRE_LEVEL = 33
    SELL_PRICE = 163400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1635:
    PREFAB_ID = "item_prefab_1635"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1635"
    EQUIPMENT_SLOT = "Head" if 1635 % 4 == 0 else ("Chest" if 1635 % 4 == 1 else ("Weapon" if 1635 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 19620
    REQUIRE_LEVEL = 33
    SELL_PRICE = 163500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1636:
    PREFAB_ID = "item_prefab_1636"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1636"
    EQUIPMENT_SLOT = "Head" if 1636 % 4 == 0 else ("Chest" if 1636 % 4 == 1 else ("Weapon" if 1636 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 19632
    REQUIRE_LEVEL = 33
    SELL_PRICE = 163600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1637:
    PREFAB_ID = "item_prefab_1637"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1637"
    EQUIPMENT_SLOT = "Head" if 1637 % 4 == 0 else ("Chest" if 1637 % 4 == 1 else ("Weapon" if 1637 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 19644
    REQUIRE_LEVEL = 33
    SELL_PRICE = 163700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1638:
    PREFAB_ID = "item_prefab_1638"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1638"
    EQUIPMENT_SLOT = "Head" if 1638 % 4 == 0 else ("Chest" if 1638 % 4 == 1 else ("Weapon" if 1638 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 19656
    REQUIRE_LEVEL = 33
    SELL_PRICE = 163800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1639:
    PREFAB_ID = "item_prefab_1639"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1639"
    EQUIPMENT_SLOT = "Head" if 1639 % 4 == 0 else ("Chest" if 1639 % 4 == 1 else ("Weapon" if 1639 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 19668
    REQUIRE_LEVEL = 33
    SELL_PRICE = 163900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1640:
    PREFAB_ID = "item_prefab_1640"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1640"
    EQUIPMENT_SLOT = "Head" if 1640 % 4 == 0 else ("Chest" if 1640 % 4 == 1 else ("Weapon" if 1640 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 19680
    REQUIRE_LEVEL = 33
    SELL_PRICE = 164000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1641:
    PREFAB_ID = "item_prefab_1641"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1641"
    EQUIPMENT_SLOT = "Head" if 1641 % 4 == 0 else ("Chest" if 1641 % 4 == 1 else ("Weapon" if 1641 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 19692
    REQUIRE_LEVEL = 33
    SELL_PRICE = 164100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1642:
    PREFAB_ID = "item_prefab_1642"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1642"
    EQUIPMENT_SLOT = "Head" if 1642 % 4 == 0 else ("Chest" if 1642 % 4 == 1 else ("Weapon" if 1642 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 19704
    REQUIRE_LEVEL = 33
    SELL_PRICE = 164200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1643:
    PREFAB_ID = "item_prefab_1643"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1643"
    EQUIPMENT_SLOT = "Head" if 1643 % 4 == 0 else ("Chest" if 1643 % 4 == 1 else ("Weapon" if 1643 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 19716
    REQUIRE_LEVEL = 33
    SELL_PRICE = 164300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1644:
    PREFAB_ID = "item_prefab_1644"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1644"
    EQUIPMENT_SLOT = "Head" if 1644 % 4 == 0 else ("Chest" if 1644 % 4 == 1 else ("Weapon" if 1644 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 19728
    REQUIRE_LEVEL = 33
    SELL_PRICE = 164400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1645:
    PREFAB_ID = "item_prefab_1645"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1645"
    EQUIPMENT_SLOT = "Head" if 1645 % 4 == 0 else ("Chest" if 1645 % 4 == 1 else ("Weapon" if 1645 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 19740
    REQUIRE_LEVEL = 33
    SELL_PRICE = 164500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1646:
    PREFAB_ID = "item_prefab_1646"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1646"
    EQUIPMENT_SLOT = "Head" if 1646 % 4 == 0 else ("Chest" if 1646 % 4 == 1 else ("Weapon" if 1646 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 19752
    REQUIRE_LEVEL = 33
    SELL_PRICE = 164600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1647:
    PREFAB_ID = "item_prefab_1647"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1647"
    EQUIPMENT_SLOT = "Head" if 1647 % 4 == 0 else ("Chest" if 1647 % 4 == 1 else ("Weapon" if 1647 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 19764
    REQUIRE_LEVEL = 33
    SELL_PRICE = 164700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1648:
    PREFAB_ID = "item_prefab_1648"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1648"
    EQUIPMENT_SLOT = "Head" if 1648 % 4 == 0 else ("Chest" if 1648 % 4 == 1 else ("Weapon" if 1648 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 19776
    REQUIRE_LEVEL = 33
    SELL_PRICE = 164800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1649:
    PREFAB_ID = "item_prefab_1649"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1649"
    EQUIPMENT_SLOT = "Head" if 1649 % 4 == 0 else ("Chest" if 1649 % 4 == 1 else ("Weapon" if 1649 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 19788
    REQUIRE_LEVEL = 33
    SELL_PRICE = 164900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1650:
    PREFAB_ID = "item_prefab_1650"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1650"
    EQUIPMENT_SLOT = "Head" if 1650 % 4 == 0 else ("Chest" if 1650 % 4 == 1 else ("Weapon" if 1650 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 19800
    REQUIRE_LEVEL = 34
    SELL_PRICE = 165000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1651:
    PREFAB_ID = "item_prefab_1651"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1651"
    EQUIPMENT_SLOT = "Head" if 1651 % 4 == 0 else ("Chest" if 1651 % 4 == 1 else ("Weapon" if 1651 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 19812
    REQUIRE_LEVEL = 34
    SELL_PRICE = 165100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1652:
    PREFAB_ID = "item_prefab_1652"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1652"
    EQUIPMENT_SLOT = "Head" if 1652 % 4 == 0 else ("Chest" if 1652 % 4 == 1 else ("Weapon" if 1652 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 19824
    REQUIRE_LEVEL = 34
    SELL_PRICE = 165200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1653:
    PREFAB_ID = "item_prefab_1653"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1653"
    EQUIPMENT_SLOT = "Head" if 1653 % 4 == 0 else ("Chest" if 1653 % 4 == 1 else ("Weapon" if 1653 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 19836
    REQUIRE_LEVEL = 34
    SELL_PRICE = 165300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1654:
    PREFAB_ID = "item_prefab_1654"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1654"
    EQUIPMENT_SLOT = "Head" if 1654 % 4 == 0 else ("Chest" if 1654 % 4 == 1 else ("Weapon" if 1654 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 19848
    REQUIRE_LEVEL = 34
    SELL_PRICE = 165400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1655:
    PREFAB_ID = "item_prefab_1655"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1655"
    EQUIPMENT_SLOT = "Head" if 1655 % 4 == 0 else ("Chest" if 1655 % 4 == 1 else ("Weapon" if 1655 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 19860
    REQUIRE_LEVEL = 34
    SELL_PRICE = 165500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1656:
    PREFAB_ID = "item_prefab_1656"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1656"
    EQUIPMENT_SLOT = "Head" if 1656 % 4 == 0 else ("Chest" if 1656 % 4 == 1 else ("Weapon" if 1656 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 19872
    REQUIRE_LEVEL = 34
    SELL_PRICE = 165600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1657:
    PREFAB_ID = "item_prefab_1657"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1657"
    EQUIPMENT_SLOT = "Head" if 1657 % 4 == 0 else ("Chest" if 1657 % 4 == 1 else ("Weapon" if 1657 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 19884
    REQUIRE_LEVEL = 34
    SELL_PRICE = 165700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1658:
    PREFAB_ID = "item_prefab_1658"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1658"
    EQUIPMENT_SLOT = "Head" if 1658 % 4 == 0 else ("Chest" if 1658 % 4 == 1 else ("Weapon" if 1658 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 19896
    REQUIRE_LEVEL = 34
    SELL_PRICE = 165800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1659:
    PREFAB_ID = "item_prefab_1659"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1659"
    EQUIPMENT_SLOT = "Head" if 1659 % 4 == 0 else ("Chest" if 1659 % 4 == 1 else ("Weapon" if 1659 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 19908
    REQUIRE_LEVEL = 34
    SELL_PRICE = 165900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1660:
    PREFAB_ID = "item_prefab_1660"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1660"
    EQUIPMENT_SLOT = "Head" if 1660 % 4 == 0 else ("Chest" if 1660 % 4 == 1 else ("Weapon" if 1660 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 19920
    REQUIRE_LEVEL = 34
    SELL_PRICE = 166000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1661:
    PREFAB_ID = "item_prefab_1661"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1661"
    EQUIPMENT_SLOT = "Head" if 1661 % 4 == 0 else ("Chest" if 1661 % 4 == 1 else ("Weapon" if 1661 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 19932
    REQUIRE_LEVEL = 34
    SELL_PRICE = 166100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1662:
    PREFAB_ID = "item_prefab_1662"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1662"
    EQUIPMENT_SLOT = "Head" if 1662 % 4 == 0 else ("Chest" if 1662 % 4 == 1 else ("Weapon" if 1662 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 19944
    REQUIRE_LEVEL = 34
    SELL_PRICE = 166200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1663:
    PREFAB_ID = "item_prefab_1663"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1663"
    EQUIPMENT_SLOT = "Head" if 1663 % 4 == 0 else ("Chest" if 1663 % 4 == 1 else ("Weapon" if 1663 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 19956
    REQUIRE_LEVEL = 34
    SELL_PRICE = 166300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1664:
    PREFAB_ID = "item_prefab_1664"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1664"
    EQUIPMENT_SLOT = "Head" if 1664 % 4 == 0 else ("Chest" if 1664 % 4 == 1 else ("Weapon" if 1664 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 19968
    REQUIRE_LEVEL = 34
    SELL_PRICE = 166400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1665:
    PREFAB_ID = "item_prefab_1665"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1665"
    EQUIPMENT_SLOT = "Head" if 1665 % 4 == 0 else ("Chest" if 1665 % 4 == 1 else ("Weapon" if 1665 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 19980
    REQUIRE_LEVEL = 34
    SELL_PRICE = 166500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1666:
    PREFAB_ID = "item_prefab_1666"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1666"
    EQUIPMENT_SLOT = "Head" if 1666 % 4 == 0 else ("Chest" if 1666 % 4 == 1 else ("Weapon" if 1666 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 19992
    REQUIRE_LEVEL = 34
    SELL_PRICE = 166600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1667:
    PREFAB_ID = "item_prefab_1667"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1667"
    EQUIPMENT_SLOT = "Head" if 1667 % 4 == 0 else ("Chest" if 1667 % 4 == 1 else ("Weapon" if 1667 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 20004
    REQUIRE_LEVEL = 34
    SELL_PRICE = 166700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1668:
    PREFAB_ID = "item_prefab_1668"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1668"
    EQUIPMENT_SLOT = "Head" if 1668 % 4 == 0 else ("Chest" if 1668 % 4 == 1 else ("Weapon" if 1668 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 20016
    REQUIRE_LEVEL = 34
    SELL_PRICE = 166800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1669:
    PREFAB_ID = "item_prefab_1669"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1669"
    EQUIPMENT_SLOT = "Head" if 1669 % 4 == 0 else ("Chest" if 1669 % 4 == 1 else ("Weapon" if 1669 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 20028
    REQUIRE_LEVEL = 34
    SELL_PRICE = 166900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1670:
    PREFAB_ID = "item_prefab_1670"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1670"
    EQUIPMENT_SLOT = "Head" if 1670 % 4 == 0 else ("Chest" if 1670 % 4 == 1 else ("Weapon" if 1670 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 20040
    REQUIRE_LEVEL = 34
    SELL_PRICE = 167000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1671:
    PREFAB_ID = "item_prefab_1671"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1671"
    EQUIPMENT_SLOT = "Head" if 1671 % 4 == 0 else ("Chest" if 1671 % 4 == 1 else ("Weapon" if 1671 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 20052
    REQUIRE_LEVEL = 34
    SELL_PRICE = 167100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1672:
    PREFAB_ID = "item_prefab_1672"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1672"
    EQUIPMENT_SLOT = "Head" if 1672 % 4 == 0 else ("Chest" if 1672 % 4 == 1 else ("Weapon" if 1672 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 20064
    REQUIRE_LEVEL = 34
    SELL_PRICE = 167200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1673:
    PREFAB_ID = "item_prefab_1673"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1673"
    EQUIPMENT_SLOT = "Head" if 1673 % 4 == 0 else ("Chest" if 1673 % 4 == 1 else ("Weapon" if 1673 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 20076
    REQUIRE_LEVEL = 34
    SELL_PRICE = 167300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1674:
    PREFAB_ID = "item_prefab_1674"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1674"
    EQUIPMENT_SLOT = "Head" if 1674 % 4 == 0 else ("Chest" if 1674 % 4 == 1 else ("Weapon" if 1674 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 20088
    REQUIRE_LEVEL = 34
    SELL_PRICE = 167400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1675:
    PREFAB_ID = "item_prefab_1675"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1675"
    EQUIPMENT_SLOT = "Head" if 1675 % 4 == 0 else ("Chest" if 1675 % 4 == 1 else ("Weapon" if 1675 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 20100
    REQUIRE_LEVEL = 34
    SELL_PRICE = 167500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1676:
    PREFAB_ID = "item_prefab_1676"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1676"
    EQUIPMENT_SLOT = "Head" if 1676 % 4 == 0 else ("Chest" if 1676 % 4 == 1 else ("Weapon" if 1676 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 20112
    REQUIRE_LEVEL = 34
    SELL_PRICE = 167600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1677:
    PREFAB_ID = "item_prefab_1677"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1677"
    EQUIPMENT_SLOT = "Head" if 1677 % 4 == 0 else ("Chest" if 1677 % 4 == 1 else ("Weapon" if 1677 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 20124
    REQUIRE_LEVEL = 34
    SELL_PRICE = 167700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1678:
    PREFAB_ID = "item_prefab_1678"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1678"
    EQUIPMENT_SLOT = "Head" if 1678 % 4 == 0 else ("Chest" if 1678 % 4 == 1 else ("Weapon" if 1678 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 20136
    REQUIRE_LEVEL = 34
    SELL_PRICE = 167800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1679:
    PREFAB_ID = "item_prefab_1679"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1679"
    EQUIPMENT_SLOT = "Head" if 1679 % 4 == 0 else ("Chest" if 1679 % 4 == 1 else ("Weapon" if 1679 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 20148
    REQUIRE_LEVEL = 34
    SELL_PRICE = 167900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1680:
    PREFAB_ID = "item_prefab_1680"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1680"
    EQUIPMENT_SLOT = "Head" if 1680 % 4 == 0 else ("Chest" if 1680 % 4 == 1 else ("Weapon" if 1680 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 20160
    REQUIRE_LEVEL = 34
    SELL_PRICE = 168000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1681:
    PREFAB_ID = "item_prefab_1681"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1681"
    EQUIPMENT_SLOT = "Head" if 1681 % 4 == 0 else ("Chest" if 1681 % 4 == 1 else ("Weapon" if 1681 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 20172
    REQUIRE_LEVEL = 34
    SELL_PRICE = 168100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1682:
    PREFAB_ID = "item_prefab_1682"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1682"
    EQUIPMENT_SLOT = "Head" if 1682 % 4 == 0 else ("Chest" if 1682 % 4 == 1 else ("Weapon" if 1682 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 20184
    REQUIRE_LEVEL = 34
    SELL_PRICE = 168200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1683:
    PREFAB_ID = "item_prefab_1683"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1683"
    EQUIPMENT_SLOT = "Head" if 1683 % 4 == 0 else ("Chest" if 1683 % 4 == 1 else ("Weapon" if 1683 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 20196
    REQUIRE_LEVEL = 34
    SELL_PRICE = 168300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1684:
    PREFAB_ID = "item_prefab_1684"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1684"
    EQUIPMENT_SLOT = "Head" if 1684 % 4 == 0 else ("Chest" if 1684 % 4 == 1 else ("Weapon" if 1684 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 20208
    REQUIRE_LEVEL = 34
    SELL_PRICE = 168400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1685:
    PREFAB_ID = "item_prefab_1685"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1685"
    EQUIPMENT_SLOT = "Head" if 1685 % 4 == 0 else ("Chest" if 1685 % 4 == 1 else ("Weapon" if 1685 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 20220
    REQUIRE_LEVEL = 34
    SELL_PRICE = 168500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1686:
    PREFAB_ID = "item_prefab_1686"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1686"
    EQUIPMENT_SLOT = "Head" if 1686 % 4 == 0 else ("Chest" if 1686 % 4 == 1 else ("Weapon" if 1686 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 20232
    REQUIRE_LEVEL = 34
    SELL_PRICE = 168600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1687:
    PREFAB_ID = "item_prefab_1687"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1687"
    EQUIPMENT_SLOT = "Head" if 1687 % 4 == 0 else ("Chest" if 1687 % 4 == 1 else ("Weapon" if 1687 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 20244
    REQUIRE_LEVEL = 34
    SELL_PRICE = 168700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1688:
    PREFAB_ID = "item_prefab_1688"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1688"
    EQUIPMENT_SLOT = "Head" if 1688 % 4 == 0 else ("Chest" if 1688 % 4 == 1 else ("Weapon" if 1688 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 20256
    REQUIRE_LEVEL = 34
    SELL_PRICE = 168800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1689:
    PREFAB_ID = "item_prefab_1689"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1689"
    EQUIPMENT_SLOT = "Head" if 1689 % 4 == 0 else ("Chest" if 1689 % 4 == 1 else ("Weapon" if 1689 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 20268
    REQUIRE_LEVEL = 34
    SELL_PRICE = 168900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1690:
    PREFAB_ID = "item_prefab_1690"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1690"
    EQUIPMENT_SLOT = "Head" if 1690 % 4 == 0 else ("Chest" if 1690 % 4 == 1 else ("Weapon" if 1690 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 20280
    REQUIRE_LEVEL = 34
    SELL_PRICE = 169000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1691:
    PREFAB_ID = "item_prefab_1691"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1691"
    EQUIPMENT_SLOT = "Head" if 1691 % 4 == 0 else ("Chest" if 1691 % 4 == 1 else ("Weapon" if 1691 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 20292
    REQUIRE_LEVEL = 34
    SELL_PRICE = 169100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1692:
    PREFAB_ID = "item_prefab_1692"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1692"
    EQUIPMENT_SLOT = "Head" if 1692 % 4 == 0 else ("Chest" if 1692 % 4 == 1 else ("Weapon" if 1692 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 20304
    REQUIRE_LEVEL = 34
    SELL_PRICE = 169200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1693:
    PREFAB_ID = "item_prefab_1693"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1693"
    EQUIPMENT_SLOT = "Head" if 1693 % 4 == 0 else ("Chest" if 1693 % 4 == 1 else ("Weapon" if 1693 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 20316
    REQUIRE_LEVEL = 34
    SELL_PRICE = 169300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1694:
    PREFAB_ID = "item_prefab_1694"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1694"
    EQUIPMENT_SLOT = "Head" if 1694 % 4 == 0 else ("Chest" if 1694 % 4 == 1 else ("Weapon" if 1694 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 20328
    REQUIRE_LEVEL = 34
    SELL_PRICE = 169400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1695:
    PREFAB_ID = "item_prefab_1695"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1695"
    EQUIPMENT_SLOT = "Head" if 1695 % 4 == 0 else ("Chest" if 1695 % 4 == 1 else ("Weapon" if 1695 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 20340
    REQUIRE_LEVEL = 34
    SELL_PRICE = 169500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1696:
    PREFAB_ID = "item_prefab_1696"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1696"
    EQUIPMENT_SLOT = "Head" if 1696 % 4 == 0 else ("Chest" if 1696 % 4 == 1 else ("Weapon" if 1696 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 20352
    REQUIRE_LEVEL = 34
    SELL_PRICE = 169600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1697:
    PREFAB_ID = "item_prefab_1697"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1697"
    EQUIPMENT_SLOT = "Head" if 1697 % 4 == 0 else ("Chest" if 1697 % 4 == 1 else ("Weapon" if 1697 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 20364
    REQUIRE_LEVEL = 34
    SELL_PRICE = 169700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1698:
    PREFAB_ID = "item_prefab_1698"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1698"
    EQUIPMENT_SLOT = "Head" if 1698 % 4 == 0 else ("Chest" if 1698 % 4 == 1 else ("Weapon" if 1698 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 20376
    REQUIRE_LEVEL = 34
    SELL_PRICE = 169800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1699:
    PREFAB_ID = "item_prefab_1699"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1699"
    EQUIPMENT_SLOT = "Head" if 1699 % 4 == 0 else ("Chest" if 1699 % 4 == 1 else ("Weapon" if 1699 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 20388
    REQUIRE_LEVEL = 34
    SELL_PRICE = 169900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1700:
    PREFAB_ID = "item_prefab_1700"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1700"
    EQUIPMENT_SLOT = "Head" if 1700 % 4 == 0 else ("Chest" if 1700 % 4 == 1 else ("Weapon" if 1700 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 20400
    REQUIRE_LEVEL = 35
    SELL_PRICE = 170000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1701:
    PREFAB_ID = "item_prefab_1701"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1701"
    EQUIPMENT_SLOT = "Head" if 1701 % 4 == 0 else ("Chest" if 1701 % 4 == 1 else ("Weapon" if 1701 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 20412
    REQUIRE_LEVEL = 35
    SELL_PRICE = 170100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1702:
    PREFAB_ID = "item_prefab_1702"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1702"
    EQUIPMENT_SLOT = "Head" if 1702 % 4 == 0 else ("Chest" if 1702 % 4 == 1 else ("Weapon" if 1702 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 20424
    REQUIRE_LEVEL = 35
    SELL_PRICE = 170200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1703:
    PREFAB_ID = "item_prefab_1703"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1703"
    EQUIPMENT_SLOT = "Head" if 1703 % 4 == 0 else ("Chest" if 1703 % 4 == 1 else ("Weapon" if 1703 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 20436
    REQUIRE_LEVEL = 35
    SELL_PRICE = 170300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1704:
    PREFAB_ID = "item_prefab_1704"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1704"
    EQUIPMENT_SLOT = "Head" if 1704 % 4 == 0 else ("Chest" if 1704 % 4 == 1 else ("Weapon" if 1704 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 20448
    REQUIRE_LEVEL = 35
    SELL_PRICE = 170400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1705:
    PREFAB_ID = "item_prefab_1705"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1705"
    EQUIPMENT_SLOT = "Head" if 1705 % 4 == 0 else ("Chest" if 1705 % 4 == 1 else ("Weapon" if 1705 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 20460
    REQUIRE_LEVEL = 35
    SELL_PRICE = 170500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1706:
    PREFAB_ID = "item_prefab_1706"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1706"
    EQUIPMENT_SLOT = "Head" if 1706 % 4 == 0 else ("Chest" if 1706 % 4 == 1 else ("Weapon" if 1706 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 20472
    REQUIRE_LEVEL = 35
    SELL_PRICE = 170600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1707:
    PREFAB_ID = "item_prefab_1707"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1707"
    EQUIPMENT_SLOT = "Head" if 1707 % 4 == 0 else ("Chest" if 1707 % 4 == 1 else ("Weapon" if 1707 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 20484
    REQUIRE_LEVEL = 35
    SELL_PRICE = 170700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1708:
    PREFAB_ID = "item_prefab_1708"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1708"
    EQUIPMENT_SLOT = "Head" if 1708 % 4 == 0 else ("Chest" if 1708 % 4 == 1 else ("Weapon" if 1708 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 20496
    REQUIRE_LEVEL = 35
    SELL_PRICE = 170800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1709:
    PREFAB_ID = "item_prefab_1709"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1709"
    EQUIPMENT_SLOT = "Head" if 1709 % 4 == 0 else ("Chest" if 1709 % 4 == 1 else ("Weapon" if 1709 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 20508
    REQUIRE_LEVEL = 35
    SELL_PRICE = 170900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1710:
    PREFAB_ID = "item_prefab_1710"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1710"
    EQUIPMENT_SLOT = "Head" if 1710 % 4 == 0 else ("Chest" if 1710 % 4 == 1 else ("Weapon" if 1710 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 20520
    REQUIRE_LEVEL = 35
    SELL_PRICE = 171000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1711:
    PREFAB_ID = "item_prefab_1711"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1711"
    EQUIPMENT_SLOT = "Head" if 1711 % 4 == 0 else ("Chest" if 1711 % 4 == 1 else ("Weapon" if 1711 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 20532
    REQUIRE_LEVEL = 35
    SELL_PRICE = 171100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1712:
    PREFAB_ID = "item_prefab_1712"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1712"
    EQUIPMENT_SLOT = "Head" if 1712 % 4 == 0 else ("Chest" if 1712 % 4 == 1 else ("Weapon" if 1712 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 20544
    REQUIRE_LEVEL = 35
    SELL_PRICE = 171200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1713:
    PREFAB_ID = "item_prefab_1713"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1713"
    EQUIPMENT_SLOT = "Head" if 1713 % 4 == 0 else ("Chest" if 1713 % 4 == 1 else ("Weapon" if 1713 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 20556
    REQUIRE_LEVEL = 35
    SELL_PRICE = 171300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1714:
    PREFAB_ID = "item_prefab_1714"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1714"
    EQUIPMENT_SLOT = "Head" if 1714 % 4 == 0 else ("Chest" if 1714 % 4 == 1 else ("Weapon" if 1714 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 20568
    REQUIRE_LEVEL = 35
    SELL_PRICE = 171400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1715:
    PREFAB_ID = "item_prefab_1715"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1715"
    EQUIPMENT_SLOT = "Head" if 1715 % 4 == 0 else ("Chest" if 1715 % 4 == 1 else ("Weapon" if 1715 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 20580
    REQUIRE_LEVEL = 35
    SELL_PRICE = 171500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1716:
    PREFAB_ID = "item_prefab_1716"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1716"
    EQUIPMENT_SLOT = "Head" if 1716 % 4 == 0 else ("Chest" if 1716 % 4 == 1 else ("Weapon" if 1716 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 20592
    REQUIRE_LEVEL = 35
    SELL_PRICE = 171600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1717:
    PREFAB_ID = "item_prefab_1717"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1717"
    EQUIPMENT_SLOT = "Head" if 1717 % 4 == 0 else ("Chest" if 1717 % 4 == 1 else ("Weapon" if 1717 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 20604
    REQUIRE_LEVEL = 35
    SELL_PRICE = 171700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1718:
    PREFAB_ID = "item_prefab_1718"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1718"
    EQUIPMENT_SLOT = "Head" if 1718 % 4 == 0 else ("Chest" if 1718 % 4 == 1 else ("Weapon" if 1718 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 20616
    REQUIRE_LEVEL = 35
    SELL_PRICE = 171800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1719:
    PREFAB_ID = "item_prefab_1719"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1719"
    EQUIPMENT_SLOT = "Head" if 1719 % 4 == 0 else ("Chest" if 1719 % 4 == 1 else ("Weapon" if 1719 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 20628
    REQUIRE_LEVEL = 35
    SELL_PRICE = 171900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1720:
    PREFAB_ID = "item_prefab_1720"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1720"
    EQUIPMENT_SLOT = "Head" if 1720 % 4 == 0 else ("Chest" if 1720 % 4 == 1 else ("Weapon" if 1720 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 20640
    REQUIRE_LEVEL = 35
    SELL_PRICE = 172000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1721:
    PREFAB_ID = "item_prefab_1721"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1721"
    EQUIPMENT_SLOT = "Head" if 1721 % 4 == 0 else ("Chest" if 1721 % 4 == 1 else ("Weapon" if 1721 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 20652
    REQUIRE_LEVEL = 35
    SELL_PRICE = 172100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1722:
    PREFAB_ID = "item_prefab_1722"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1722"
    EQUIPMENT_SLOT = "Head" if 1722 % 4 == 0 else ("Chest" if 1722 % 4 == 1 else ("Weapon" if 1722 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 20664
    REQUIRE_LEVEL = 35
    SELL_PRICE = 172200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1723:
    PREFAB_ID = "item_prefab_1723"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1723"
    EQUIPMENT_SLOT = "Head" if 1723 % 4 == 0 else ("Chest" if 1723 % 4 == 1 else ("Weapon" if 1723 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 20676
    REQUIRE_LEVEL = 35
    SELL_PRICE = 172300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1724:
    PREFAB_ID = "item_prefab_1724"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1724"
    EQUIPMENT_SLOT = "Head" if 1724 % 4 == 0 else ("Chest" if 1724 % 4 == 1 else ("Weapon" if 1724 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 20688
    REQUIRE_LEVEL = 35
    SELL_PRICE = 172400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1725:
    PREFAB_ID = "item_prefab_1725"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1725"
    EQUIPMENT_SLOT = "Head" if 1725 % 4 == 0 else ("Chest" if 1725 % 4 == 1 else ("Weapon" if 1725 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 20700
    REQUIRE_LEVEL = 35
    SELL_PRICE = 172500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1726:
    PREFAB_ID = "item_prefab_1726"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1726"
    EQUIPMENT_SLOT = "Head" if 1726 % 4 == 0 else ("Chest" if 1726 % 4 == 1 else ("Weapon" if 1726 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 20712
    REQUIRE_LEVEL = 35
    SELL_PRICE = 172600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1727:
    PREFAB_ID = "item_prefab_1727"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1727"
    EQUIPMENT_SLOT = "Head" if 1727 % 4 == 0 else ("Chest" if 1727 % 4 == 1 else ("Weapon" if 1727 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 20724
    REQUIRE_LEVEL = 35
    SELL_PRICE = 172700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1728:
    PREFAB_ID = "item_prefab_1728"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1728"
    EQUIPMENT_SLOT = "Head" if 1728 % 4 == 0 else ("Chest" if 1728 % 4 == 1 else ("Weapon" if 1728 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 20736
    REQUIRE_LEVEL = 35
    SELL_PRICE = 172800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1729:
    PREFAB_ID = "item_prefab_1729"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1729"
    EQUIPMENT_SLOT = "Head" if 1729 % 4 == 0 else ("Chest" if 1729 % 4 == 1 else ("Weapon" if 1729 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 20748
    REQUIRE_LEVEL = 35
    SELL_PRICE = 172900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1730:
    PREFAB_ID = "item_prefab_1730"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1730"
    EQUIPMENT_SLOT = "Head" if 1730 % 4 == 0 else ("Chest" if 1730 % 4 == 1 else ("Weapon" if 1730 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 20760
    REQUIRE_LEVEL = 35
    SELL_PRICE = 173000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1731:
    PREFAB_ID = "item_prefab_1731"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1731"
    EQUIPMENT_SLOT = "Head" if 1731 % 4 == 0 else ("Chest" if 1731 % 4 == 1 else ("Weapon" if 1731 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 20772
    REQUIRE_LEVEL = 35
    SELL_PRICE = 173100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1732:
    PREFAB_ID = "item_prefab_1732"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1732"
    EQUIPMENT_SLOT = "Head" if 1732 % 4 == 0 else ("Chest" if 1732 % 4 == 1 else ("Weapon" if 1732 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 20784
    REQUIRE_LEVEL = 35
    SELL_PRICE = 173200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1733:
    PREFAB_ID = "item_prefab_1733"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1733"
    EQUIPMENT_SLOT = "Head" if 1733 % 4 == 0 else ("Chest" if 1733 % 4 == 1 else ("Weapon" if 1733 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 20796
    REQUIRE_LEVEL = 35
    SELL_PRICE = 173300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1734:
    PREFAB_ID = "item_prefab_1734"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1734"
    EQUIPMENT_SLOT = "Head" if 1734 % 4 == 0 else ("Chest" if 1734 % 4 == 1 else ("Weapon" if 1734 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 20808
    REQUIRE_LEVEL = 35
    SELL_PRICE = 173400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1735:
    PREFAB_ID = "item_prefab_1735"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1735"
    EQUIPMENT_SLOT = "Head" if 1735 % 4 == 0 else ("Chest" if 1735 % 4 == 1 else ("Weapon" if 1735 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 20820
    REQUIRE_LEVEL = 35
    SELL_PRICE = 173500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1736:
    PREFAB_ID = "item_prefab_1736"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1736"
    EQUIPMENT_SLOT = "Head" if 1736 % 4 == 0 else ("Chest" if 1736 % 4 == 1 else ("Weapon" if 1736 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 20832
    REQUIRE_LEVEL = 35
    SELL_PRICE = 173600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1737:
    PREFAB_ID = "item_prefab_1737"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1737"
    EQUIPMENT_SLOT = "Head" if 1737 % 4 == 0 else ("Chest" if 1737 % 4 == 1 else ("Weapon" if 1737 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 20844
    REQUIRE_LEVEL = 35
    SELL_PRICE = 173700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1738:
    PREFAB_ID = "item_prefab_1738"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1738"
    EQUIPMENT_SLOT = "Head" if 1738 % 4 == 0 else ("Chest" if 1738 % 4 == 1 else ("Weapon" if 1738 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 20856
    REQUIRE_LEVEL = 35
    SELL_PRICE = 173800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1739:
    PREFAB_ID = "item_prefab_1739"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1739"
    EQUIPMENT_SLOT = "Head" if 1739 % 4 == 0 else ("Chest" if 1739 % 4 == 1 else ("Weapon" if 1739 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 20868
    REQUIRE_LEVEL = 35
    SELL_PRICE = 173900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1740:
    PREFAB_ID = "item_prefab_1740"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1740"
    EQUIPMENT_SLOT = "Head" if 1740 % 4 == 0 else ("Chest" if 1740 % 4 == 1 else ("Weapon" if 1740 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 20880
    REQUIRE_LEVEL = 35
    SELL_PRICE = 174000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1741:
    PREFAB_ID = "item_prefab_1741"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1741"
    EQUIPMENT_SLOT = "Head" if 1741 % 4 == 0 else ("Chest" if 1741 % 4 == 1 else ("Weapon" if 1741 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 20892
    REQUIRE_LEVEL = 35
    SELL_PRICE = 174100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1742:
    PREFAB_ID = "item_prefab_1742"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1742"
    EQUIPMENT_SLOT = "Head" if 1742 % 4 == 0 else ("Chest" if 1742 % 4 == 1 else ("Weapon" if 1742 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 20904
    REQUIRE_LEVEL = 35
    SELL_PRICE = 174200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1743:
    PREFAB_ID = "item_prefab_1743"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1743"
    EQUIPMENT_SLOT = "Head" if 1743 % 4 == 0 else ("Chest" if 1743 % 4 == 1 else ("Weapon" if 1743 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 20916
    REQUIRE_LEVEL = 35
    SELL_PRICE = 174300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1744:
    PREFAB_ID = "item_prefab_1744"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1744"
    EQUIPMENT_SLOT = "Head" if 1744 % 4 == 0 else ("Chest" if 1744 % 4 == 1 else ("Weapon" if 1744 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 20928
    REQUIRE_LEVEL = 35
    SELL_PRICE = 174400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1745:
    PREFAB_ID = "item_prefab_1745"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1745"
    EQUIPMENT_SLOT = "Head" if 1745 % 4 == 0 else ("Chest" if 1745 % 4 == 1 else ("Weapon" if 1745 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 20940
    REQUIRE_LEVEL = 35
    SELL_PRICE = 174500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1746:
    PREFAB_ID = "item_prefab_1746"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1746"
    EQUIPMENT_SLOT = "Head" if 1746 % 4 == 0 else ("Chest" if 1746 % 4 == 1 else ("Weapon" if 1746 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 20952
    REQUIRE_LEVEL = 35
    SELL_PRICE = 174600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1747:
    PREFAB_ID = "item_prefab_1747"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1747"
    EQUIPMENT_SLOT = "Head" if 1747 % 4 == 0 else ("Chest" if 1747 % 4 == 1 else ("Weapon" if 1747 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 20964
    REQUIRE_LEVEL = 35
    SELL_PRICE = 174700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1748:
    PREFAB_ID = "item_prefab_1748"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1748"
    EQUIPMENT_SLOT = "Head" if 1748 % 4 == 0 else ("Chest" if 1748 % 4 == 1 else ("Weapon" if 1748 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 20976
    REQUIRE_LEVEL = 35
    SELL_PRICE = 174800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1749:
    PREFAB_ID = "item_prefab_1749"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1749"
    EQUIPMENT_SLOT = "Head" if 1749 % 4 == 0 else ("Chest" if 1749 % 4 == 1 else ("Weapon" if 1749 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 20988
    REQUIRE_LEVEL = 35
    SELL_PRICE = 174900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1750:
    PREFAB_ID = "item_prefab_1750"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1750"
    EQUIPMENT_SLOT = "Head" if 1750 % 4 == 0 else ("Chest" if 1750 % 4 == 1 else ("Weapon" if 1750 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 21000
    REQUIRE_LEVEL = 36
    SELL_PRICE = 175000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1751:
    PREFAB_ID = "item_prefab_1751"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1751"
    EQUIPMENT_SLOT = "Head" if 1751 % 4 == 0 else ("Chest" if 1751 % 4 == 1 else ("Weapon" if 1751 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 21012
    REQUIRE_LEVEL = 36
    SELL_PRICE = 175100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1752:
    PREFAB_ID = "item_prefab_1752"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1752"
    EQUIPMENT_SLOT = "Head" if 1752 % 4 == 0 else ("Chest" if 1752 % 4 == 1 else ("Weapon" if 1752 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 21024
    REQUIRE_LEVEL = 36
    SELL_PRICE = 175200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1753:
    PREFAB_ID = "item_prefab_1753"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1753"
    EQUIPMENT_SLOT = "Head" if 1753 % 4 == 0 else ("Chest" if 1753 % 4 == 1 else ("Weapon" if 1753 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 21036
    REQUIRE_LEVEL = 36
    SELL_PRICE = 175300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1754:
    PREFAB_ID = "item_prefab_1754"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1754"
    EQUIPMENT_SLOT = "Head" if 1754 % 4 == 0 else ("Chest" if 1754 % 4 == 1 else ("Weapon" if 1754 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 21048
    REQUIRE_LEVEL = 36
    SELL_PRICE = 175400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1755:
    PREFAB_ID = "item_prefab_1755"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1755"
    EQUIPMENT_SLOT = "Head" if 1755 % 4 == 0 else ("Chest" if 1755 % 4 == 1 else ("Weapon" if 1755 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 21060
    REQUIRE_LEVEL = 36
    SELL_PRICE = 175500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1756:
    PREFAB_ID = "item_prefab_1756"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1756"
    EQUIPMENT_SLOT = "Head" if 1756 % 4 == 0 else ("Chest" if 1756 % 4 == 1 else ("Weapon" if 1756 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 21072
    REQUIRE_LEVEL = 36
    SELL_PRICE = 175600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1757:
    PREFAB_ID = "item_prefab_1757"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1757"
    EQUIPMENT_SLOT = "Head" if 1757 % 4 == 0 else ("Chest" if 1757 % 4 == 1 else ("Weapon" if 1757 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 21084
    REQUIRE_LEVEL = 36
    SELL_PRICE = 175700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1758:
    PREFAB_ID = "item_prefab_1758"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1758"
    EQUIPMENT_SLOT = "Head" if 1758 % 4 == 0 else ("Chest" if 1758 % 4 == 1 else ("Weapon" if 1758 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 21096
    REQUIRE_LEVEL = 36
    SELL_PRICE = 175800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1759:
    PREFAB_ID = "item_prefab_1759"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1759"
    EQUIPMENT_SLOT = "Head" if 1759 % 4 == 0 else ("Chest" if 1759 % 4 == 1 else ("Weapon" if 1759 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 21108
    REQUIRE_LEVEL = 36
    SELL_PRICE = 175900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1760:
    PREFAB_ID = "item_prefab_1760"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1760"
    EQUIPMENT_SLOT = "Head" if 1760 % 4 == 0 else ("Chest" if 1760 % 4 == 1 else ("Weapon" if 1760 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 21120
    REQUIRE_LEVEL = 36
    SELL_PRICE = 176000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1761:
    PREFAB_ID = "item_prefab_1761"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1761"
    EQUIPMENT_SLOT = "Head" if 1761 % 4 == 0 else ("Chest" if 1761 % 4 == 1 else ("Weapon" if 1761 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 21132
    REQUIRE_LEVEL = 36
    SELL_PRICE = 176100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1762:
    PREFAB_ID = "item_prefab_1762"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1762"
    EQUIPMENT_SLOT = "Head" if 1762 % 4 == 0 else ("Chest" if 1762 % 4 == 1 else ("Weapon" if 1762 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 21144
    REQUIRE_LEVEL = 36
    SELL_PRICE = 176200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1763:
    PREFAB_ID = "item_prefab_1763"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1763"
    EQUIPMENT_SLOT = "Head" if 1763 % 4 == 0 else ("Chest" if 1763 % 4 == 1 else ("Weapon" if 1763 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 21156
    REQUIRE_LEVEL = 36
    SELL_PRICE = 176300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1764:
    PREFAB_ID = "item_prefab_1764"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1764"
    EQUIPMENT_SLOT = "Head" if 1764 % 4 == 0 else ("Chest" if 1764 % 4 == 1 else ("Weapon" if 1764 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 21168
    REQUIRE_LEVEL = 36
    SELL_PRICE = 176400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1765:
    PREFAB_ID = "item_prefab_1765"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1765"
    EQUIPMENT_SLOT = "Head" if 1765 % 4 == 0 else ("Chest" if 1765 % 4 == 1 else ("Weapon" if 1765 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 21180
    REQUIRE_LEVEL = 36
    SELL_PRICE = 176500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1766:
    PREFAB_ID = "item_prefab_1766"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1766"
    EQUIPMENT_SLOT = "Head" if 1766 % 4 == 0 else ("Chest" if 1766 % 4 == 1 else ("Weapon" if 1766 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 21192
    REQUIRE_LEVEL = 36
    SELL_PRICE = 176600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1767:
    PREFAB_ID = "item_prefab_1767"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1767"
    EQUIPMENT_SLOT = "Head" if 1767 % 4 == 0 else ("Chest" if 1767 % 4 == 1 else ("Weapon" if 1767 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 21204
    REQUIRE_LEVEL = 36
    SELL_PRICE = 176700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1768:
    PREFAB_ID = "item_prefab_1768"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1768"
    EQUIPMENT_SLOT = "Head" if 1768 % 4 == 0 else ("Chest" if 1768 % 4 == 1 else ("Weapon" if 1768 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 21216
    REQUIRE_LEVEL = 36
    SELL_PRICE = 176800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1769:
    PREFAB_ID = "item_prefab_1769"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1769"
    EQUIPMENT_SLOT = "Head" if 1769 % 4 == 0 else ("Chest" if 1769 % 4 == 1 else ("Weapon" if 1769 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 21228
    REQUIRE_LEVEL = 36
    SELL_PRICE = 176900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1770:
    PREFAB_ID = "item_prefab_1770"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1770"
    EQUIPMENT_SLOT = "Head" if 1770 % 4 == 0 else ("Chest" if 1770 % 4 == 1 else ("Weapon" if 1770 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 21240
    REQUIRE_LEVEL = 36
    SELL_PRICE = 177000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1771:
    PREFAB_ID = "item_prefab_1771"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1771"
    EQUIPMENT_SLOT = "Head" if 1771 % 4 == 0 else ("Chest" if 1771 % 4 == 1 else ("Weapon" if 1771 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 21252
    REQUIRE_LEVEL = 36
    SELL_PRICE = 177100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1772:
    PREFAB_ID = "item_prefab_1772"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1772"
    EQUIPMENT_SLOT = "Head" if 1772 % 4 == 0 else ("Chest" if 1772 % 4 == 1 else ("Weapon" if 1772 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 21264
    REQUIRE_LEVEL = 36
    SELL_PRICE = 177200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1773:
    PREFAB_ID = "item_prefab_1773"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1773"
    EQUIPMENT_SLOT = "Head" if 1773 % 4 == 0 else ("Chest" if 1773 % 4 == 1 else ("Weapon" if 1773 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 21276
    REQUIRE_LEVEL = 36
    SELL_PRICE = 177300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1774:
    PREFAB_ID = "item_prefab_1774"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1774"
    EQUIPMENT_SLOT = "Head" if 1774 % 4 == 0 else ("Chest" if 1774 % 4 == 1 else ("Weapon" if 1774 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 21288
    REQUIRE_LEVEL = 36
    SELL_PRICE = 177400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1775:
    PREFAB_ID = "item_prefab_1775"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1775"
    EQUIPMENT_SLOT = "Head" if 1775 % 4 == 0 else ("Chest" if 1775 % 4 == 1 else ("Weapon" if 1775 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 21300
    REQUIRE_LEVEL = 36
    SELL_PRICE = 177500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1776:
    PREFAB_ID = "item_prefab_1776"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1776"
    EQUIPMENT_SLOT = "Head" if 1776 % 4 == 0 else ("Chest" if 1776 % 4 == 1 else ("Weapon" if 1776 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 21312
    REQUIRE_LEVEL = 36
    SELL_PRICE = 177600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1777:
    PREFAB_ID = "item_prefab_1777"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1777"
    EQUIPMENT_SLOT = "Head" if 1777 % 4 == 0 else ("Chest" if 1777 % 4 == 1 else ("Weapon" if 1777 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 21324
    REQUIRE_LEVEL = 36
    SELL_PRICE = 177700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1778:
    PREFAB_ID = "item_prefab_1778"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1778"
    EQUIPMENT_SLOT = "Head" if 1778 % 4 == 0 else ("Chest" if 1778 % 4 == 1 else ("Weapon" if 1778 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 21336
    REQUIRE_LEVEL = 36
    SELL_PRICE = 177800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1779:
    PREFAB_ID = "item_prefab_1779"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1779"
    EQUIPMENT_SLOT = "Head" if 1779 % 4 == 0 else ("Chest" if 1779 % 4 == 1 else ("Weapon" if 1779 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 21348
    REQUIRE_LEVEL = 36
    SELL_PRICE = 177900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1780:
    PREFAB_ID = "item_prefab_1780"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1780"
    EQUIPMENT_SLOT = "Head" if 1780 % 4 == 0 else ("Chest" if 1780 % 4 == 1 else ("Weapon" if 1780 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 21360
    REQUIRE_LEVEL = 36
    SELL_PRICE = 178000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1781:
    PREFAB_ID = "item_prefab_1781"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1781"
    EQUIPMENT_SLOT = "Head" if 1781 % 4 == 0 else ("Chest" if 1781 % 4 == 1 else ("Weapon" if 1781 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 21372
    REQUIRE_LEVEL = 36
    SELL_PRICE = 178100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1782:
    PREFAB_ID = "item_prefab_1782"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1782"
    EQUIPMENT_SLOT = "Head" if 1782 % 4 == 0 else ("Chest" if 1782 % 4 == 1 else ("Weapon" if 1782 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 21384
    REQUIRE_LEVEL = 36
    SELL_PRICE = 178200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1783:
    PREFAB_ID = "item_prefab_1783"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1783"
    EQUIPMENT_SLOT = "Head" if 1783 % 4 == 0 else ("Chest" if 1783 % 4 == 1 else ("Weapon" if 1783 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 21396
    REQUIRE_LEVEL = 36
    SELL_PRICE = 178300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1784:
    PREFAB_ID = "item_prefab_1784"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1784"
    EQUIPMENT_SLOT = "Head" if 1784 % 4 == 0 else ("Chest" if 1784 % 4 == 1 else ("Weapon" if 1784 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 21408
    REQUIRE_LEVEL = 36
    SELL_PRICE = 178400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1785:
    PREFAB_ID = "item_prefab_1785"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1785"
    EQUIPMENT_SLOT = "Head" if 1785 % 4 == 0 else ("Chest" if 1785 % 4 == 1 else ("Weapon" if 1785 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 21420
    REQUIRE_LEVEL = 36
    SELL_PRICE = 178500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1786:
    PREFAB_ID = "item_prefab_1786"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1786"
    EQUIPMENT_SLOT = "Head" if 1786 % 4 == 0 else ("Chest" if 1786 % 4 == 1 else ("Weapon" if 1786 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 21432
    REQUIRE_LEVEL = 36
    SELL_PRICE = 178600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1787:
    PREFAB_ID = "item_prefab_1787"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1787"
    EQUIPMENT_SLOT = "Head" if 1787 % 4 == 0 else ("Chest" if 1787 % 4 == 1 else ("Weapon" if 1787 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 21444
    REQUIRE_LEVEL = 36
    SELL_PRICE = 178700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1788:
    PREFAB_ID = "item_prefab_1788"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1788"
    EQUIPMENT_SLOT = "Head" if 1788 % 4 == 0 else ("Chest" if 1788 % 4 == 1 else ("Weapon" if 1788 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 21456
    REQUIRE_LEVEL = 36
    SELL_PRICE = 178800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1789:
    PREFAB_ID = "item_prefab_1789"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1789"
    EQUIPMENT_SLOT = "Head" if 1789 % 4 == 0 else ("Chest" if 1789 % 4 == 1 else ("Weapon" if 1789 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 21468
    REQUIRE_LEVEL = 36
    SELL_PRICE = 178900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1790:
    PREFAB_ID = "item_prefab_1790"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1790"
    EQUIPMENT_SLOT = "Head" if 1790 % 4 == 0 else ("Chest" if 1790 % 4 == 1 else ("Weapon" if 1790 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 21480
    REQUIRE_LEVEL = 36
    SELL_PRICE = 179000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1791:
    PREFAB_ID = "item_prefab_1791"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1791"
    EQUIPMENT_SLOT = "Head" if 1791 % 4 == 0 else ("Chest" if 1791 % 4 == 1 else ("Weapon" if 1791 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 21492
    REQUIRE_LEVEL = 36
    SELL_PRICE = 179100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1792:
    PREFAB_ID = "item_prefab_1792"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1792"
    EQUIPMENT_SLOT = "Head" if 1792 % 4 == 0 else ("Chest" if 1792 % 4 == 1 else ("Weapon" if 1792 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 21504
    REQUIRE_LEVEL = 36
    SELL_PRICE = 179200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1793:
    PREFAB_ID = "item_prefab_1793"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1793"
    EQUIPMENT_SLOT = "Head" if 1793 % 4 == 0 else ("Chest" if 1793 % 4 == 1 else ("Weapon" if 1793 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 21516
    REQUIRE_LEVEL = 36
    SELL_PRICE = 179300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1794:
    PREFAB_ID = "item_prefab_1794"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1794"
    EQUIPMENT_SLOT = "Head" if 1794 % 4 == 0 else ("Chest" if 1794 % 4 == 1 else ("Weapon" if 1794 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 21528
    REQUIRE_LEVEL = 36
    SELL_PRICE = 179400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1795:
    PREFAB_ID = "item_prefab_1795"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1795"
    EQUIPMENT_SLOT = "Head" if 1795 % 4 == 0 else ("Chest" if 1795 % 4 == 1 else ("Weapon" if 1795 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 21540
    REQUIRE_LEVEL = 36
    SELL_PRICE = 179500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1796:
    PREFAB_ID = "item_prefab_1796"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1796"
    EQUIPMENT_SLOT = "Head" if 1796 % 4 == 0 else ("Chest" if 1796 % 4 == 1 else ("Weapon" if 1796 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 21552
    REQUIRE_LEVEL = 36
    SELL_PRICE = 179600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1797:
    PREFAB_ID = "item_prefab_1797"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1797"
    EQUIPMENT_SLOT = "Head" if 1797 % 4 == 0 else ("Chest" if 1797 % 4 == 1 else ("Weapon" if 1797 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 21564
    REQUIRE_LEVEL = 36
    SELL_PRICE = 179700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1798:
    PREFAB_ID = "item_prefab_1798"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1798"
    EQUIPMENT_SLOT = "Head" if 1798 % 4 == 0 else ("Chest" if 1798 % 4 == 1 else ("Weapon" if 1798 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 21576
    REQUIRE_LEVEL = 36
    SELL_PRICE = 179800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1799:
    PREFAB_ID = "item_prefab_1799"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1799"
    EQUIPMENT_SLOT = "Head" if 1799 % 4 == 0 else ("Chest" if 1799 % 4 == 1 else ("Weapon" if 1799 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 21588
    REQUIRE_LEVEL = 36
    SELL_PRICE = 179900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1800:
    PREFAB_ID = "item_prefab_1800"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1800"
    EQUIPMENT_SLOT = "Head" if 1800 % 4 == 0 else ("Chest" if 1800 % 4 == 1 else ("Weapon" if 1800 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 21600
    REQUIRE_LEVEL = 37
    SELL_PRICE = 180000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1801:
    PREFAB_ID = "item_prefab_1801"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1801"
    EQUIPMENT_SLOT = "Head" if 1801 % 4 == 0 else ("Chest" if 1801 % 4 == 1 else ("Weapon" if 1801 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 21612
    REQUIRE_LEVEL = 37
    SELL_PRICE = 180100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1802:
    PREFAB_ID = "item_prefab_1802"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1802"
    EQUIPMENT_SLOT = "Head" if 1802 % 4 == 0 else ("Chest" if 1802 % 4 == 1 else ("Weapon" if 1802 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 21624
    REQUIRE_LEVEL = 37
    SELL_PRICE = 180200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1803:
    PREFAB_ID = "item_prefab_1803"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1803"
    EQUIPMENT_SLOT = "Head" if 1803 % 4 == 0 else ("Chest" if 1803 % 4 == 1 else ("Weapon" if 1803 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 21636
    REQUIRE_LEVEL = 37
    SELL_PRICE = 180300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1804:
    PREFAB_ID = "item_prefab_1804"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1804"
    EQUIPMENT_SLOT = "Head" if 1804 % 4 == 0 else ("Chest" if 1804 % 4 == 1 else ("Weapon" if 1804 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 21648
    REQUIRE_LEVEL = 37
    SELL_PRICE = 180400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1805:
    PREFAB_ID = "item_prefab_1805"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1805"
    EQUIPMENT_SLOT = "Head" if 1805 % 4 == 0 else ("Chest" if 1805 % 4 == 1 else ("Weapon" if 1805 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 21660
    REQUIRE_LEVEL = 37
    SELL_PRICE = 180500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1806:
    PREFAB_ID = "item_prefab_1806"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1806"
    EQUIPMENT_SLOT = "Head" if 1806 % 4 == 0 else ("Chest" if 1806 % 4 == 1 else ("Weapon" if 1806 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 21672
    REQUIRE_LEVEL = 37
    SELL_PRICE = 180600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1807:
    PREFAB_ID = "item_prefab_1807"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1807"
    EQUIPMENT_SLOT = "Head" if 1807 % 4 == 0 else ("Chest" if 1807 % 4 == 1 else ("Weapon" if 1807 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 21684
    REQUIRE_LEVEL = 37
    SELL_PRICE = 180700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1808:
    PREFAB_ID = "item_prefab_1808"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1808"
    EQUIPMENT_SLOT = "Head" if 1808 % 4 == 0 else ("Chest" if 1808 % 4 == 1 else ("Weapon" if 1808 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 21696
    REQUIRE_LEVEL = 37
    SELL_PRICE = 180800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1809:
    PREFAB_ID = "item_prefab_1809"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1809"
    EQUIPMENT_SLOT = "Head" if 1809 % 4 == 0 else ("Chest" if 1809 % 4 == 1 else ("Weapon" if 1809 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 21708
    REQUIRE_LEVEL = 37
    SELL_PRICE = 180900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1810:
    PREFAB_ID = "item_prefab_1810"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1810"
    EQUIPMENT_SLOT = "Head" if 1810 % 4 == 0 else ("Chest" if 1810 % 4 == 1 else ("Weapon" if 1810 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 21720
    REQUIRE_LEVEL = 37
    SELL_PRICE = 181000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1811:
    PREFAB_ID = "item_prefab_1811"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1811"
    EQUIPMENT_SLOT = "Head" if 1811 % 4 == 0 else ("Chest" if 1811 % 4 == 1 else ("Weapon" if 1811 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 21732
    REQUIRE_LEVEL = 37
    SELL_PRICE = 181100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1812:
    PREFAB_ID = "item_prefab_1812"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1812"
    EQUIPMENT_SLOT = "Head" if 1812 % 4 == 0 else ("Chest" if 1812 % 4 == 1 else ("Weapon" if 1812 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 21744
    REQUIRE_LEVEL = 37
    SELL_PRICE = 181200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1813:
    PREFAB_ID = "item_prefab_1813"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1813"
    EQUIPMENT_SLOT = "Head" if 1813 % 4 == 0 else ("Chest" if 1813 % 4 == 1 else ("Weapon" if 1813 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 21756
    REQUIRE_LEVEL = 37
    SELL_PRICE = 181300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1814:
    PREFAB_ID = "item_prefab_1814"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1814"
    EQUIPMENT_SLOT = "Head" if 1814 % 4 == 0 else ("Chest" if 1814 % 4 == 1 else ("Weapon" if 1814 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 21768
    REQUIRE_LEVEL = 37
    SELL_PRICE = 181400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1815:
    PREFAB_ID = "item_prefab_1815"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1815"
    EQUIPMENT_SLOT = "Head" if 1815 % 4 == 0 else ("Chest" if 1815 % 4 == 1 else ("Weapon" if 1815 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 21780
    REQUIRE_LEVEL = 37
    SELL_PRICE = 181500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1816:
    PREFAB_ID = "item_prefab_1816"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1816"
    EQUIPMENT_SLOT = "Head" if 1816 % 4 == 0 else ("Chest" if 1816 % 4 == 1 else ("Weapon" if 1816 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 21792
    REQUIRE_LEVEL = 37
    SELL_PRICE = 181600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1817:
    PREFAB_ID = "item_prefab_1817"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1817"
    EQUIPMENT_SLOT = "Head" if 1817 % 4 == 0 else ("Chest" if 1817 % 4 == 1 else ("Weapon" if 1817 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 21804
    REQUIRE_LEVEL = 37
    SELL_PRICE = 181700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1818:
    PREFAB_ID = "item_prefab_1818"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1818"
    EQUIPMENT_SLOT = "Head" if 1818 % 4 == 0 else ("Chest" if 1818 % 4 == 1 else ("Weapon" if 1818 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 21816
    REQUIRE_LEVEL = 37
    SELL_PRICE = 181800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1819:
    PREFAB_ID = "item_prefab_1819"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1819"
    EQUIPMENT_SLOT = "Head" if 1819 % 4 == 0 else ("Chest" if 1819 % 4 == 1 else ("Weapon" if 1819 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 21828
    REQUIRE_LEVEL = 37
    SELL_PRICE = 181900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1820:
    PREFAB_ID = "item_prefab_1820"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1820"
    EQUIPMENT_SLOT = "Head" if 1820 % 4 == 0 else ("Chest" if 1820 % 4 == 1 else ("Weapon" if 1820 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 21840
    REQUIRE_LEVEL = 37
    SELL_PRICE = 182000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1821:
    PREFAB_ID = "item_prefab_1821"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1821"
    EQUIPMENT_SLOT = "Head" if 1821 % 4 == 0 else ("Chest" if 1821 % 4 == 1 else ("Weapon" if 1821 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 21852
    REQUIRE_LEVEL = 37
    SELL_PRICE = 182100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1822:
    PREFAB_ID = "item_prefab_1822"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1822"
    EQUIPMENT_SLOT = "Head" if 1822 % 4 == 0 else ("Chest" if 1822 % 4 == 1 else ("Weapon" if 1822 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 21864
    REQUIRE_LEVEL = 37
    SELL_PRICE = 182200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1823:
    PREFAB_ID = "item_prefab_1823"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1823"
    EQUIPMENT_SLOT = "Head" if 1823 % 4 == 0 else ("Chest" if 1823 % 4 == 1 else ("Weapon" if 1823 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 21876
    REQUIRE_LEVEL = 37
    SELL_PRICE = 182300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1824:
    PREFAB_ID = "item_prefab_1824"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1824"
    EQUIPMENT_SLOT = "Head" if 1824 % 4 == 0 else ("Chest" if 1824 % 4 == 1 else ("Weapon" if 1824 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 21888
    REQUIRE_LEVEL = 37
    SELL_PRICE = 182400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1825:
    PREFAB_ID = "item_prefab_1825"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1825"
    EQUIPMENT_SLOT = "Head" if 1825 % 4 == 0 else ("Chest" if 1825 % 4 == 1 else ("Weapon" if 1825 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 21900
    REQUIRE_LEVEL = 37
    SELL_PRICE = 182500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1826:
    PREFAB_ID = "item_prefab_1826"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1826"
    EQUIPMENT_SLOT = "Head" if 1826 % 4 == 0 else ("Chest" if 1826 % 4 == 1 else ("Weapon" if 1826 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 21912
    REQUIRE_LEVEL = 37
    SELL_PRICE = 182600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1827:
    PREFAB_ID = "item_prefab_1827"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1827"
    EQUIPMENT_SLOT = "Head" if 1827 % 4 == 0 else ("Chest" if 1827 % 4 == 1 else ("Weapon" if 1827 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 21924
    REQUIRE_LEVEL = 37
    SELL_PRICE = 182700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1828:
    PREFAB_ID = "item_prefab_1828"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1828"
    EQUIPMENT_SLOT = "Head" if 1828 % 4 == 0 else ("Chest" if 1828 % 4 == 1 else ("Weapon" if 1828 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 21936
    REQUIRE_LEVEL = 37
    SELL_PRICE = 182800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1829:
    PREFAB_ID = "item_prefab_1829"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1829"
    EQUIPMENT_SLOT = "Head" if 1829 % 4 == 0 else ("Chest" if 1829 % 4 == 1 else ("Weapon" if 1829 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 21948
    REQUIRE_LEVEL = 37
    SELL_PRICE = 182900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1830:
    PREFAB_ID = "item_prefab_1830"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1830"
    EQUIPMENT_SLOT = "Head" if 1830 % 4 == 0 else ("Chest" if 1830 % 4 == 1 else ("Weapon" if 1830 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 21960
    REQUIRE_LEVEL = 37
    SELL_PRICE = 183000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1831:
    PREFAB_ID = "item_prefab_1831"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1831"
    EQUIPMENT_SLOT = "Head" if 1831 % 4 == 0 else ("Chest" if 1831 % 4 == 1 else ("Weapon" if 1831 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 21972
    REQUIRE_LEVEL = 37
    SELL_PRICE = 183100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1832:
    PREFAB_ID = "item_prefab_1832"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1832"
    EQUIPMENT_SLOT = "Head" if 1832 % 4 == 0 else ("Chest" if 1832 % 4 == 1 else ("Weapon" if 1832 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 21984
    REQUIRE_LEVEL = 37
    SELL_PRICE = 183200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1833:
    PREFAB_ID = "item_prefab_1833"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1833"
    EQUIPMENT_SLOT = "Head" if 1833 % 4 == 0 else ("Chest" if 1833 % 4 == 1 else ("Weapon" if 1833 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 21996
    REQUIRE_LEVEL = 37
    SELL_PRICE = 183300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1834:
    PREFAB_ID = "item_prefab_1834"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1834"
    EQUIPMENT_SLOT = "Head" if 1834 % 4 == 0 else ("Chest" if 1834 % 4 == 1 else ("Weapon" if 1834 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 22008
    REQUIRE_LEVEL = 37
    SELL_PRICE = 183400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1835:
    PREFAB_ID = "item_prefab_1835"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1835"
    EQUIPMENT_SLOT = "Head" if 1835 % 4 == 0 else ("Chest" if 1835 % 4 == 1 else ("Weapon" if 1835 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 22020
    REQUIRE_LEVEL = 37
    SELL_PRICE = 183500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1836:
    PREFAB_ID = "item_prefab_1836"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1836"
    EQUIPMENT_SLOT = "Head" if 1836 % 4 == 0 else ("Chest" if 1836 % 4 == 1 else ("Weapon" if 1836 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 22032
    REQUIRE_LEVEL = 37
    SELL_PRICE = 183600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1837:
    PREFAB_ID = "item_prefab_1837"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1837"
    EQUIPMENT_SLOT = "Head" if 1837 % 4 == 0 else ("Chest" if 1837 % 4 == 1 else ("Weapon" if 1837 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 22044
    REQUIRE_LEVEL = 37
    SELL_PRICE = 183700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1838:
    PREFAB_ID = "item_prefab_1838"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1838"
    EQUIPMENT_SLOT = "Head" if 1838 % 4 == 0 else ("Chest" if 1838 % 4 == 1 else ("Weapon" if 1838 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 22056
    REQUIRE_LEVEL = 37
    SELL_PRICE = 183800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1839:
    PREFAB_ID = "item_prefab_1839"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1839"
    EQUIPMENT_SLOT = "Head" if 1839 % 4 == 0 else ("Chest" if 1839 % 4 == 1 else ("Weapon" if 1839 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 22068
    REQUIRE_LEVEL = 37
    SELL_PRICE = 183900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1840:
    PREFAB_ID = "item_prefab_1840"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1840"
    EQUIPMENT_SLOT = "Head" if 1840 % 4 == 0 else ("Chest" if 1840 % 4 == 1 else ("Weapon" if 1840 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 22080
    REQUIRE_LEVEL = 37
    SELL_PRICE = 184000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1841:
    PREFAB_ID = "item_prefab_1841"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1841"
    EQUIPMENT_SLOT = "Head" if 1841 % 4 == 0 else ("Chest" if 1841 % 4 == 1 else ("Weapon" if 1841 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 22092
    REQUIRE_LEVEL = 37
    SELL_PRICE = 184100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1842:
    PREFAB_ID = "item_prefab_1842"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1842"
    EQUIPMENT_SLOT = "Head" if 1842 % 4 == 0 else ("Chest" if 1842 % 4 == 1 else ("Weapon" if 1842 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 22104
    REQUIRE_LEVEL = 37
    SELL_PRICE = 184200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1843:
    PREFAB_ID = "item_prefab_1843"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1843"
    EQUIPMENT_SLOT = "Head" if 1843 % 4 == 0 else ("Chest" if 1843 % 4 == 1 else ("Weapon" if 1843 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 22116
    REQUIRE_LEVEL = 37
    SELL_PRICE = 184300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1844:
    PREFAB_ID = "item_prefab_1844"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1844"
    EQUIPMENT_SLOT = "Head" if 1844 % 4 == 0 else ("Chest" if 1844 % 4 == 1 else ("Weapon" if 1844 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 22128
    REQUIRE_LEVEL = 37
    SELL_PRICE = 184400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1845:
    PREFAB_ID = "item_prefab_1845"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1845"
    EQUIPMENT_SLOT = "Head" if 1845 % 4 == 0 else ("Chest" if 1845 % 4 == 1 else ("Weapon" if 1845 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 22140
    REQUIRE_LEVEL = 37
    SELL_PRICE = 184500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1846:
    PREFAB_ID = "item_prefab_1846"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1846"
    EQUIPMENT_SLOT = "Head" if 1846 % 4 == 0 else ("Chest" if 1846 % 4 == 1 else ("Weapon" if 1846 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 22152
    REQUIRE_LEVEL = 37
    SELL_PRICE = 184600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1847:
    PREFAB_ID = "item_prefab_1847"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1847"
    EQUIPMENT_SLOT = "Head" if 1847 % 4 == 0 else ("Chest" if 1847 % 4 == 1 else ("Weapon" if 1847 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 22164
    REQUIRE_LEVEL = 37
    SELL_PRICE = 184700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1848:
    PREFAB_ID = "item_prefab_1848"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1848"
    EQUIPMENT_SLOT = "Head" if 1848 % 4 == 0 else ("Chest" if 1848 % 4 == 1 else ("Weapon" if 1848 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 22176
    REQUIRE_LEVEL = 37
    SELL_PRICE = 184800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1849:
    PREFAB_ID = "item_prefab_1849"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1849"
    EQUIPMENT_SLOT = "Head" if 1849 % 4 == 0 else ("Chest" if 1849 % 4 == 1 else ("Weapon" if 1849 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 22188
    REQUIRE_LEVEL = 37
    SELL_PRICE = 184900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1850:
    PREFAB_ID = "item_prefab_1850"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1850"
    EQUIPMENT_SLOT = "Head" if 1850 % 4 == 0 else ("Chest" if 1850 % 4 == 1 else ("Weapon" if 1850 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 22200
    REQUIRE_LEVEL = 38
    SELL_PRICE = 185000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1851:
    PREFAB_ID = "item_prefab_1851"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1851"
    EQUIPMENT_SLOT = "Head" if 1851 % 4 == 0 else ("Chest" if 1851 % 4 == 1 else ("Weapon" if 1851 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 22212
    REQUIRE_LEVEL = 38
    SELL_PRICE = 185100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1852:
    PREFAB_ID = "item_prefab_1852"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1852"
    EQUIPMENT_SLOT = "Head" if 1852 % 4 == 0 else ("Chest" if 1852 % 4 == 1 else ("Weapon" if 1852 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 22224
    REQUIRE_LEVEL = 38
    SELL_PRICE = 185200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1853:
    PREFAB_ID = "item_prefab_1853"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1853"
    EQUIPMENT_SLOT = "Head" if 1853 % 4 == 0 else ("Chest" if 1853 % 4 == 1 else ("Weapon" if 1853 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 22236
    REQUIRE_LEVEL = 38
    SELL_PRICE = 185300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1854:
    PREFAB_ID = "item_prefab_1854"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1854"
    EQUIPMENT_SLOT = "Head" if 1854 % 4 == 0 else ("Chest" if 1854 % 4 == 1 else ("Weapon" if 1854 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 22248
    REQUIRE_LEVEL = 38
    SELL_PRICE = 185400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1855:
    PREFAB_ID = "item_prefab_1855"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1855"
    EQUIPMENT_SLOT = "Head" if 1855 % 4 == 0 else ("Chest" if 1855 % 4 == 1 else ("Weapon" if 1855 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 22260
    REQUIRE_LEVEL = 38
    SELL_PRICE = 185500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1856:
    PREFAB_ID = "item_prefab_1856"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1856"
    EQUIPMENT_SLOT = "Head" if 1856 % 4 == 0 else ("Chest" if 1856 % 4 == 1 else ("Weapon" if 1856 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 22272
    REQUIRE_LEVEL = 38
    SELL_PRICE = 185600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1857:
    PREFAB_ID = "item_prefab_1857"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1857"
    EQUIPMENT_SLOT = "Head" if 1857 % 4 == 0 else ("Chest" if 1857 % 4 == 1 else ("Weapon" if 1857 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 22284
    REQUIRE_LEVEL = 38
    SELL_PRICE = 185700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1858:
    PREFAB_ID = "item_prefab_1858"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1858"
    EQUIPMENT_SLOT = "Head" if 1858 % 4 == 0 else ("Chest" if 1858 % 4 == 1 else ("Weapon" if 1858 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 22296
    REQUIRE_LEVEL = 38
    SELL_PRICE = 185800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1859:
    PREFAB_ID = "item_prefab_1859"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1859"
    EQUIPMENT_SLOT = "Head" if 1859 % 4 == 0 else ("Chest" if 1859 % 4 == 1 else ("Weapon" if 1859 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 22308
    REQUIRE_LEVEL = 38
    SELL_PRICE = 185900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1860:
    PREFAB_ID = "item_prefab_1860"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1860"
    EQUIPMENT_SLOT = "Head" if 1860 % 4 == 0 else ("Chest" if 1860 % 4 == 1 else ("Weapon" if 1860 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 22320
    REQUIRE_LEVEL = 38
    SELL_PRICE = 186000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1861:
    PREFAB_ID = "item_prefab_1861"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1861"
    EQUIPMENT_SLOT = "Head" if 1861 % 4 == 0 else ("Chest" if 1861 % 4 == 1 else ("Weapon" if 1861 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 22332
    REQUIRE_LEVEL = 38
    SELL_PRICE = 186100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1862:
    PREFAB_ID = "item_prefab_1862"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1862"
    EQUIPMENT_SLOT = "Head" if 1862 % 4 == 0 else ("Chest" if 1862 % 4 == 1 else ("Weapon" if 1862 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 22344
    REQUIRE_LEVEL = 38
    SELL_PRICE = 186200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1863:
    PREFAB_ID = "item_prefab_1863"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1863"
    EQUIPMENT_SLOT = "Head" if 1863 % 4 == 0 else ("Chest" if 1863 % 4 == 1 else ("Weapon" if 1863 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 22356
    REQUIRE_LEVEL = 38
    SELL_PRICE = 186300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1864:
    PREFAB_ID = "item_prefab_1864"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1864"
    EQUIPMENT_SLOT = "Head" if 1864 % 4 == 0 else ("Chest" if 1864 % 4 == 1 else ("Weapon" if 1864 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 22368
    REQUIRE_LEVEL = 38
    SELL_PRICE = 186400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1865:
    PREFAB_ID = "item_prefab_1865"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1865"
    EQUIPMENT_SLOT = "Head" if 1865 % 4 == 0 else ("Chest" if 1865 % 4 == 1 else ("Weapon" if 1865 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 22380
    REQUIRE_LEVEL = 38
    SELL_PRICE = 186500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1866:
    PREFAB_ID = "item_prefab_1866"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1866"
    EQUIPMENT_SLOT = "Head" if 1866 % 4 == 0 else ("Chest" if 1866 % 4 == 1 else ("Weapon" if 1866 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 22392
    REQUIRE_LEVEL = 38
    SELL_PRICE = 186600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1867:
    PREFAB_ID = "item_prefab_1867"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1867"
    EQUIPMENT_SLOT = "Head" if 1867 % 4 == 0 else ("Chest" if 1867 % 4 == 1 else ("Weapon" if 1867 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 22404
    REQUIRE_LEVEL = 38
    SELL_PRICE = 186700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1868:
    PREFAB_ID = "item_prefab_1868"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1868"
    EQUIPMENT_SLOT = "Head" if 1868 % 4 == 0 else ("Chest" if 1868 % 4 == 1 else ("Weapon" if 1868 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 22416
    REQUIRE_LEVEL = 38
    SELL_PRICE = 186800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1869:
    PREFAB_ID = "item_prefab_1869"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1869"
    EQUIPMENT_SLOT = "Head" if 1869 % 4 == 0 else ("Chest" if 1869 % 4 == 1 else ("Weapon" if 1869 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 22428
    REQUIRE_LEVEL = 38
    SELL_PRICE = 186900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1870:
    PREFAB_ID = "item_prefab_1870"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1870"
    EQUIPMENT_SLOT = "Head" if 1870 % 4 == 0 else ("Chest" if 1870 % 4 == 1 else ("Weapon" if 1870 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 22440
    REQUIRE_LEVEL = 38
    SELL_PRICE = 187000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1871:
    PREFAB_ID = "item_prefab_1871"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1871"
    EQUIPMENT_SLOT = "Head" if 1871 % 4 == 0 else ("Chest" if 1871 % 4 == 1 else ("Weapon" if 1871 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 22452
    REQUIRE_LEVEL = 38
    SELL_PRICE = 187100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1872:
    PREFAB_ID = "item_prefab_1872"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1872"
    EQUIPMENT_SLOT = "Head" if 1872 % 4 == 0 else ("Chest" if 1872 % 4 == 1 else ("Weapon" if 1872 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 22464
    REQUIRE_LEVEL = 38
    SELL_PRICE = 187200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1873:
    PREFAB_ID = "item_prefab_1873"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1873"
    EQUIPMENT_SLOT = "Head" if 1873 % 4 == 0 else ("Chest" if 1873 % 4 == 1 else ("Weapon" if 1873 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 22476
    REQUIRE_LEVEL = 38
    SELL_PRICE = 187300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1874:
    PREFAB_ID = "item_prefab_1874"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1874"
    EQUIPMENT_SLOT = "Head" if 1874 % 4 == 0 else ("Chest" if 1874 % 4 == 1 else ("Weapon" if 1874 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 22488
    REQUIRE_LEVEL = 38
    SELL_PRICE = 187400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1875:
    PREFAB_ID = "item_prefab_1875"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1875"
    EQUIPMENT_SLOT = "Head" if 1875 % 4 == 0 else ("Chest" if 1875 % 4 == 1 else ("Weapon" if 1875 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 22500
    REQUIRE_LEVEL = 38
    SELL_PRICE = 187500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1876:
    PREFAB_ID = "item_prefab_1876"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1876"
    EQUIPMENT_SLOT = "Head" if 1876 % 4 == 0 else ("Chest" if 1876 % 4 == 1 else ("Weapon" if 1876 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 22512
    REQUIRE_LEVEL = 38
    SELL_PRICE = 187600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1877:
    PREFAB_ID = "item_prefab_1877"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1877"
    EQUIPMENT_SLOT = "Head" if 1877 % 4 == 0 else ("Chest" if 1877 % 4 == 1 else ("Weapon" if 1877 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 22524
    REQUIRE_LEVEL = 38
    SELL_PRICE = 187700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1878:
    PREFAB_ID = "item_prefab_1878"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1878"
    EQUIPMENT_SLOT = "Head" if 1878 % 4 == 0 else ("Chest" if 1878 % 4 == 1 else ("Weapon" if 1878 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 22536
    REQUIRE_LEVEL = 38
    SELL_PRICE = 187800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1879:
    PREFAB_ID = "item_prefab_1879"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1879"
    EQUIPMENT_SLOT = "Head" if 1879 % 4 == 0 else ("Chest" if 1879 % 4 == 1 else ("Weapon" if 1879 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 22548
    REQUIRE_LEVEL = 38
    SELL_PRICE = 187900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1880:
    PREFAB_ID = "item_prefab_1880"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1880"
    EQUIPMENT_SLOT = "Head" if 1880 % 4 == 0 else ("Chest" if 1880 % 4 == 1 else ("Weapon" if 1880 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 22560
    REQUIRE_LEVEL = 38
    SELL_PRICE = 188000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1881:
    PREFAB_ID = "item_prefab_1881"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1881"
    EQUIPMENT_SLOT = "Head" if 1881 % 4 == 0 else ("Chest" if 1881 % 4 == 1 else ("Weapon" if 1881 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 22572
    REQUIRE_LEVEL = 38
    SELL_PRICE = 188100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1882:
    PREFAB_ID = "item_prefab_1882"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1882"
    EQUIPMENT_SLOT = "Head" if 1882 % 4 == 0 else ("Chest" if 1882 % 4 == 1 else ("Weapon" if 1882 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 22584
    REQUIRE_LEVEL = 38
    SELL_PRICE = 188200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1883:
    PREFAB_ID = "item_prefab_1883"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1883"
    EQUIPMENT_SLOT = "Head" if 1883 % 4 == 0 else ("Chest" if 1883 % 4 == 1 else ("Weapon" if 1883 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 22596
    REQUIRE_LEVEL = 38
    SELL_PRICE = 188300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1884:
    PREFAB_ID = "item_prefab_1884"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1884"
    EQUIPMENT_SLOT = "Head" if 1884 % 4 == 0 else ("Chest" if 1884 % 4 == 1 else ("Weapon" if 1884 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 22608
    REQUIRE_LEVEL = 38
    SELL_PRICE = 188400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1885:
    PREFAB_ID = "item_prefab_1885"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1885"
    EQUIPMENT_SLOT = "Head" if 1885 % 4 == 0 else ("Chest" if 1885 % 4 == 1 else ("Weapon" if 1885 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 22620
    REQUIRE_LEVEL = 38
    SELL_PRICE = 188500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1886:
    PREFAB_ID = "item_prefab_1886"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1886"
    EQUIPMENT_SLOT = "Head" if 1886 % 4 == 0 else ("Chest" if 1886 % 4 == 1 else ("Weapon" if 1886 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 22632
    REQUIRE_LEVEL = 38
    SELL_PRICE = 188600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1887:
    PREFAB_ID = "item_prefab_1887"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1887"
    EQUIPMENT_SLOT = "Head" if 1887 % 4 == 0 else ("Chest" if 1887 % 4 == 1 else ("Weapon" if 1887 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 22644
    REQUIRE_LEVEL = 38
    SELL_PRICE = 188700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1888:
    PREFAB_ID = "item_prefab_1888"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1888"
    EQUIPMENT_SLOT = "Head" if 1888 % 4 == 0 else ("Chest" if 1888 % 4 == 1 else ("Weapon" if 1888 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 22656
    REQUIRE_LEVEL = 38
    SELL_PRICE = 188800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1889:
    PREFAB_ID = "item_prefab_1889"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1889"
    EQUIPMENT_SLOT = "Head" if 1889 % 4 == 0 else ("Chest" if 1889 % 4 == 1 else ("Weapon" if 1889 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 22668
    REQUIRE_LEVEL = 38
    SELL_PRICE = 188900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1890:
    PREFAB_ID = "item_prefab_1890"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1890"
    EQUIPMENT_SLOT = "Head" if 1890 % 4 == 0 else ("Chest" if 1890 % 4 == 1 else ("Weapon" if 1890 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 22680
    REQUIRE_LEVEL = 38
    SELL_PRICE = 189000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1891:
    PREFAB_ID = "item_prefab_1891"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1891"
    EQUIPMENT_SLOT = "Head" if 1891 % 4 == 0 else ("Chest" if 1891 % 4 == 1 else ("Weapon" if 1891 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 22692
    REQUIRE_LEVEL = 38
    SELL_PRICE = 189100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1892:
    PREFAB_ID = "item_prefab_1892"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1892"
    EQUIPMENT_SLOT = "Head" if 1892 % 4 == 0 else ("Chest" if 1892 % 4 == 1 else ("Weapon" if 1892 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 22704
    REQUIRE_LEVEL = 38
    SELL_PRICE = 189200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1893:
    PREFAB_ID = "item_prefab_1893"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1893"
    EQUIPMENT_SLOT = "Head" if 1893 % 4 == 0 else ("Chest" if 1893 % 4 == 1 else ("Weapon" if 1893 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 22716
    REQUIRE_LEVEL = 38
    SELL_PRICE = 189300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1894:
    PREFAB_ID = "item_prefab_1894"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1894"
    EQUIPMENT_SLOT = "Head" if 1894 % 4 == 0 else ("Chest" if 1894 % 4 == 1 else ("Weapon" if 1894 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 22728
    REQUIRE_LEVEL = 38
    SELL_PRICE = 189400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1895:
    PREFAB_ID = "item_prefab_1895"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1895"
    EQUIPMENT_SLOT = "Head" if 1895 % 4 == 0 else ("Chest" if 1895 % 4 == 1 else ("Weapon" if 1895 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 22740
    REQUIRE_LEVEL = 38
    SELL_PRICE = 189500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1896:
    PREFAB_ID = "item_prefab_1896"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1896"
    EQUIPMENT_SLOT = "Head" if 1896 % 4 == 0 else ("Chest" if 1896 % 4 == 1 else ("Weapon" if 1896 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 22752
    REQUIRE_LEVEL = 38
    SELL_PRICE = 189600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1897:
    PREFAB_ID = "item_prefab_1897"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1897"
    EQUIPMENT_SLOT = "Head" if 1897 % 4 == 0 else ("Chest" if 1897 % 4 == 1 else ("Weapon" if 1897 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 22764
    REQUIRE_LEVEL = 38
    SELL_PRICE = 189700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1898:
    PREFAB_ID = "item_prefab_1898"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1898"
    EQUIPMENT_SLOT = "Head" if 1898 % 4 == 0 else ("Chest" if 1898 % 4 == 1 else ("Weapon" if 1898 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 22776
    REQUIRE_LEVEL = 38
    SELL_PRICE = 189800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1899:
    PREFAB_ID = "item_prefab_1899"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1899"
    EQUIPMENT_SLOT = "Head" if 1899 % 4 == 0 else ("Chest" if 1899 % 4 == 1 else ("Weapon" if 1899 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 22788
    REQUIRE_LEVEL = 38
    SELL_PRICE = 189900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1900:
    PREFAB_ID = "item_prefab_1900"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1900"
    EQUIPMENT_SLOT = "Head" if 1900 % 4 == 0 else ("Chest" if 1900 % 4 == 1 else ("Weapon" if 1900 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 22800
    REQUIRE_LEVEL = 39
    SELL_PRICE = 190000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1901:
    PREFAB_ID = "item_prefab_1901"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1901"
    EQUIPMENT_SLOT = "Head" if 1901 % 4 == 0 else ("Chest" if 1901 % 4 == 1 else ("Weapon" if 1901 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 22812
    REQUIRE_LEVEL = 39
    SELL_PRICE = 190100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1902:
    PREFAB_ID = "item_prefab_1902"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1902"
    EQUIPMENT_SLOT = "Head" if 1902 % 4 == 0 else ("Chest" if 1902 % 4 == 1 else ("Weapon" if 1902 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 22824
    REQUIRE_LEVEL = 39
    SELL_PRICE = 190200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1903:
    PREFAB_ID = "item_prefab_1903"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1903"
    EQUIPMENT_SLOT = "Head" if 1903 % 4 == 0 else ("Chest" if 1903 % 4 == 1 else ("Weapon" if 1903 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 22836
    REQUIRE_LEVEL = 39
    SELL_PRICE = 190300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1904:
    PREFAB_ID = "item_prefab_1904"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1904"
    EQUIPMENT_SLOT = "Head" if 1904 % 4 == 0 else ("Chest" if 1904 % 4 == 1 else ("Weapon" if 1904 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 22848
    REQUIRE_LEVEL = 39
    SELL_PRICE = 190400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1905:
    PREFAB_ID = "item_prefab_1905"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1905"
    EQUIPMENT_SLOT = "Head" if 1905 % 4 == 0 else ("Chest" if 1905 % 4 == 1 else ("Weapon" if 1905 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 22860
    REQUIRE_LEVEL = 39
    SELL_PRICE = 190500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1906:
    PREFAB_ID = "item_prefab_1906"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1906"
    EQUIPMENT_SLOT = "Head" if 1906 % 4 == 0 else ("Chest" if 1906 % 4 == 1 else ("Weapon" if 1906 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 22872
    REQUIRE_LEVEL = 39
    SELL_PRICE = 190600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1907:
    PREFAB_ID = "item_prefab_1907"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1907"
    EQUIPMENT_SLOT = "Head" if 1907 % 4 == 0 else ("Chest" if 1907 % 4 == 1 else ("Weapon" if 1907 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 22884
    REQUIRE_LEVEL = 39
    SELL_PRICE = 190700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1908:
    PREFAB_ID = "item_prefab_1908"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1908"
    EQUIPMENT_SLOT = "Head" if 1908 % 4 == 0 else ("Chest" if 1908 % 4 == 1 else ("Weapon" if 1908 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 22896
    REQUIRE_LEVEL = 39
    SELL_PRICE = 190800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1909:
    PREFAB_ID = "item_prefab_1909"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1909"
    EQUIPMENT_SLOT = "Head" if 1909 % 4 == 0 else ("Chest" if 1909 % 4 == 1 else ("Weapon" if 1909 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 22908
    REQUIRE_LEVEL = 39
    SELL_PRICE = 190900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1910:
    PREFAB_ID = "item_prefab_1910"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1910"
    EQUIPMENT_SLOT = "Head" if 1910 % 4 == 0 else ("Chest" if 1910 % 4 == 1 else ("Weapon" if 1910 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 22920
    REQUIRE_LEVEL = 39
    SELL_PRICE = 191000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1911:
    PREFAB_ID = "item_prefab_1911"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1911"
    EQUIPMENT_SLOT = "Head" if 1911 % 4 == 0 else ("Chest" if 1911 % 4 == 1 else ("Weapon" if 1911 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 22932
    REQUIRE_LEVEL = 39
    SELL_PRICE = 191100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1912:
    PREFAB_ID = "item_prefab_1912"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1912"
    EQUIPMENT_SLOT = "Head" if 1912 % 4 == 0 else ("Chest" if 1912 % 4 == 1 else ("Weapon" if 1912 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 22944
    REQUIRE_LEVEL = 39
    SELL_PRICE = 191200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1913:
    PREFAB_ID = "item_prefab_1913"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1913"
    EQUIPMENT_SLOT = "Head" if 1913 % 4 == 0 else ("Chest" if 1913 % 4 == 1 else ("Weapon" if 1913 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 22956
    REQUIRE_LEVEL = 39
    SELL_PRICE = 191300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1914:
    PREFAB_ID = "item_prefab_1914"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1914"
    EQUIPMENT_SLOT = "Head" if 1914 % 4 == 0 else ("Chest" if 1914 % 4 == 1 else ("Weapon" if 1914 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 22968
    REQUIRE_LEVEL = 39
    SELL_PRICE = 191400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1915:
    PREFAB_ID = "item_prefab_1915"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1915"
    EQUIPMENT_SLOT = "Head" if 1915 % 4 == 0 else ("Chest" if 1915 % 4 == 1 else ("Weapon" if 1915 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 22980
    REQUIRE_LEVEL = 39
    SELL_PRICE = 191500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1916:
    PREFAB_ID = "item_prefab_1916"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1916"
    EQUIPMENT_SLOT = "Head" if 1916 % 4 == 0 else ("Chest" if 1916 % 4 == 1 else ("Weapon" if 1916 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 22992
    REQUIRE_LEVEL = 39
    SELL_PRICE = 191600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1917:
    PREFAB_ID = "item_prefab_1917"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1917"
    EQUIPMENT_SLOT = "Head" if 1917 % 4 == 0 else ("Chest" if 1917 % 4 == 1 else ("Weapon" if 1917 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 23004
    REQUIRE_LEVEL = 39
    SELL_PRICE = 191700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1918:
    PREFAB_ID = "item_prefab_1918"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1918"
    EQUIPMENT_SLOT = "Head" if 1918 % 4 == 0 else ("Chest" if 1918 % 4 == 1 else ("Weapon" if 1918 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 23016
    REQUIRE_LEVEL = 39
    SELL_PRICE = 191800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1919:
    PREFAB_ID = "item_prefab_1919"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1919"
    EQUIPMENT_SLOT = "Head" if 1919 % 4 == 0 else ("Chest" if 1919 % 4 == 1 else ("Weapon" if 1919 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 23028
    REQUIRE_LEVEL = 39
    SELL_PRICE = 191900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1920:
    PREFAB_ID = "item_prefab_1920"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1920"
    EQUIPMENT_SLOT = "Head" if 1920 % 4 == 0 else ("Chest" if 1920 % 4 == 1 else ("Weapon" if 1920 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 23040
    REQUIRE_LEVEL = 39
    SELL_PRICE = 192000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1921:
    PREFAB_ID = "item_prefab_1921"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1921"
    EQUIPMENT_SLOT = "Head" if 1921 % 4 == 0 else ("Chest" if 1921 % 4 == 1 else ("Weapon" if 1921 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 23052
    REQUIRE_LEVEL = 39
    SELL_PRICE = 192100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1922:
    PREFAB_ID = "item_prefab_1922"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1922"
    EQUIPMENT_SLOT = "Head" if 1922 % 4 == 0 else ("Chest" if 1922 % 4 == 1 else ("Weapon" if 1922 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 23064
    REQUIRE_LEVEL = 39
    SELL_PRICE = 192200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1923:
    PREFAB_ID = "item_prefab_1923"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1923"
    EQUIPMENT_SLOT = "Head" if 1923 % 4 == 0 else ("Chest" if 1923 % 4 == 1 else ("Weapon" if 1923 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 23076
    REQUIRE_LEVEL = 39
    SELL_PRICE = 192300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1924:
    PREFAB_ID = "item_prefab_1924"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1924"
    EQUIPMENT_SLOT = "Head" if 1924 % 4 == 0 else ("Chest" if 1924 % 4 == 1 else ("Weapon" if 1924 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 23088
    REQUIRE_LEVEL = 39
    SELL_PRICE = 192400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1925:
    PREFAB_ID = "item_prefab_1925"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1925"
    EQUIPMENT_SLOT = "Head" if 1925 % 4 == 0 else ("Chest" if 1925 % 4 == 1 else ("Weapon" if 1925 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 23100
    REQUIRE_LEVEL = 39
    SELL_PRICE = 192500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1926:
    PREFAB_ID = "item_prefab_1926"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1926"
    EQUIPMENT_SLOT = "Head" if 1926 % 4 == 0 else ("Chest" if 1926 % 4 == 1 else ("Weapon" if 1926 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 23112
    REQUIRE_LEVEL = 39
    SELL_PRICE = 192600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1927:
    PREFAB_ID = "item_prefab_1927"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1927"
    EQUIPMENT_SLOT = "Head" if 1927 % 4 == 0 else ("Chest" if 1927 % 4 == 1 else ("Weapon" if 1927 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 23124
    REQUIRE_LEVEL = 39
    SELL_PRICE = 192700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1928:
    PREFAB_ID = "item_prefab_1928"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1928"
    EQUIPMENT_SLOT = "Head" if 1928 % 4 == 0 else ("Chest" if 1928 % 4 == 1 else ("Weapon" if 1928 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 23136
    REQUIRE_LEVEL = 39
    SELL_PRICE = 192800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1929:
    PREFAB_ID = "item_prefab_1929"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1929"
    EQUIPMENT_SLOT = "Head" if 1929 % 4 == 0 else ("Chest" if 1929 % 4 == 1 else ("Weapon" if 1929 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 23148
    REQUIRE_LEVEL = 39
    SELL_PRICE = 192900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1930:
    PREFAB_ID = "item_prefab_1930"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1930"
    EQUIPMENT_SLOT = "Head" if 1930 % 4 == 0 else ("Chest" if 1930 % 4 == 1 else ("Weapon" if 1930 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 23160
    REQUIRE_LEVEL = 39
    SELL_PRICE = 193000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1931:
    PREFAB_ID = "item_prefab_1931"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1931"
    EQUIPMENT_SLOT = "Head" if 1931 % 4 == 0 else ("Chest" if 1931 % 4 == 1 else ("Weapon" if 1931 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 23172
    REQUIRE_LEVEL = 39
    SELL_PRICE = 193100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1932:
    PREFAB_ID = "item_prefab_1932"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1932"
    EQUIPMENT_SLOT = "Head" if 1932 % 4 == 0 else ("Chest" if 1932 % 4 == 1 else ("Weapon" if 1932 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 23184
    REQUIRE_LEVEL = 39
    SELL_PRICE = 193200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1933:
    PREFAB_ID = "item_prefab_1933"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1933"
    EQUIPMENT_SLOT = "Head" if 1933 % 4 == 0 else ("Chest" if 1933 % 4 == 1 else ("Weapon" if 1933 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 23196
    REQUIRE_LEVEL = 39
    SELL_PRICE = 193300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1934:
    PREFAB_ID = "item_prefab_1934"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1934"
    EQUIPMENT_SLOT = "Head" if 1934 % 4 == 0 else ("Chest" if 1934 % 4 == 1 else ("Weapon" if 1934 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 23208
    REQUIRE_LEVEL = 39
    SELL_PRICE = 193400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1935:
    PREFAB_ID = "item_prefab_1935"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1935"
    EQUIPMENT_SLOT = "Head" if 1935 % 4 == 0 else ("Chest" if 1935 % 4 == 1 else ("Weapon" if 1935 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 23220
    REQUIRE_LEVEL = 39
    SELL_PRICE = 193500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1936:
    PREFAB_ID = "item_prefab_1936"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1936"
    EQUIPMENT_SLOT = "Head" if 1936 % 4 == 0 else ("Chest" if 1936 % 4 == 1 else ("Weapon" if 1936 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 23232
    REQUIRE_LEVEL = 39
    SELL_PRICE = 193600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1937:
    PREFAB_ID = "item_prefab_1937"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1937"
    EQUIPMENT_SLOT = "Head" if 1937 % 4 == 0 else ("Chest" if 1937 % 4 == 1 else ("Weapon" if 1937 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 23244
    REQUIRE_LEVEL = 39
    SELL_PRICE = 193700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1938:
    PREFAB_ID = "item_prefab_1938"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1938"
    EQUIPMENT_SLOT = "Head" if 1938 % 4 == 0 else ("Chest" if 1938 % 4 == 1 else ("Weapon" if 1938 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 23256
    REQUIRE_LEVEL = 39
    SELL_PRICE = 193800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1939:
    PREFAB_ID = "item_prefab_1939"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1939"
    EQUIPMENT_SLOT = "Head" if 1939 % 4 == 0 else ("Chest" if 1939 % 4 == 1 else ("Weapon" if 1939 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 23268
    REQUIRE_LEVEL = 39
    SELL_PRICE = 193900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1940:
    PREFAB_ID = "item_prefab_1940"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1940"
    EQUIPMENT_SLOT = "Head" if 1940 % 4 == 0 else ("Chest" if 1940 % 4 == 1 else ("Weapon" if 1940 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 23280
    REQUIRE_LEVEL = 39
    SELL_PRICE = 194000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1941:
    PREFAB_ID = "item_prefab_1941"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1941"
    EQUIPMENT_SLOT = "Head" if 1941 % 4 == 0 else ("Chest" if 1941 % 4 == 1 else ("Weapon" if 1941 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 23292
    REQUIRE_LEVEL = 39
    SELL_PRICE = 194100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1942:
    PREFAB_ID = "item_prefab_1942"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1942"
    EQUIPMENT_SLOT = "Head" if 1942 % 4 == 0 else ("Chest" if 1942 % 4 == 1 else ("Weapon" if 1942 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 23304
    REQUIRE_LEVEL = 39
    SELL_PRICE = 194200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1943:
    PREFAB_ID = "item_prefab_1943"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1943"
    EQUIPMENT_SLOT = "Head" if 1943 % 4 == 0 else ("Chest" if 1943 % 4 == 1 else ("Weapon" if 1943 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 23316
    REQUIRE_LEVEL = 39
    SELL_PRICE = 194300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1944:
    PREFAB_ID = "item_prefab_1944"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1944"
    EQUIPMENT_SLOT = "Head" if 1944 % 4 == 0 else ("Chest" if 1944 % 4 == 1 else ("Weapon" if 1944 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 23328
    REQUIRE_LEVEL = 39
    SELL_PRICE = 194400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1945:
    PREFAB_ID = "item_prefab_1945"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1945"
    EQUIPMENT_SLOT = "Head" if 1945 % 4 == 0 else ("Chest" if 1945 % 4 == 1 else ("Weapon" if 1945 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 23340
    REQUIRE_LEVEL = 39
    SELL_PRICE = 194500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1946:
    PREFAB_ID = "item_prefab_1946"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1946"
    EQUIPMENT_SLOT = "Head" if 1946 % 4 == 0 else ("Chest" if 1946 % 4 == 1 else ("Weapon" if 1946 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 23352
    REQUIRE_LEVEL = 39
    SELL_PRICE = 194600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1947:
    PREFAB_ID = "item_prefab_1947"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1947"
    EQUIPMENT_SLOT = "Head" if 1947 % 4 == 0 else ("Chest" if 1947 % 4 == 1 else ("Weapon" if 1947 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 23364
    REQUIRE_LEVEL = 39
    SELL_PRICE = 194700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1948:
    PREFAB_ID = "item_prefab_1948"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1948"
    EQUIPMENT_SLOT = "Head" if 1948 % 4 == 0 else ("Chest" if 1948 % 4 == 1 else ("Weapon" if 1948 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 23376
    REQUIRE_LEVEL = 39
    SELL_PRICE = 194800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1949:
    PREFAB_ID = "item_prefab_1949"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1949"
    EQUIPMENT_SLOT = "Head" if 1949 % 4 == 0 else ("Chest" if 1949 % 4 == 1 else ("Weapon" if 1949 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 23388
    REQUIRE_LEVEL = 39
    SELL_PRICE = 194900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1950:
    PREFAB_ID = "item_prefab_1950"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1950"
    EQUIPMENT_SLOT = "Head" if 1950 % 4 == 0 else ("Chest" if 1950 % 4 == 1 else ("Weapon" if 1950 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 23400
    REQUIRE_LEVEL = 40
    SELL_PRICE = 195000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1951:
    PREFAB_ID = "item_prefab_1951"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1951"
    EQUIPMENT_SLOT = "Head" if 1951 % 4 == 0 else ("Chest" if 1951 % 4 == 1 else ("Weapon" if 1951 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 23412
    REQUIRE_LEVEL = 40
    SELL_PRICE = 195100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1952:
    PREFAB_ID = "item_prefab_1952"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1952"
    EQUIPMENT_SLOT = "Head" if 1952 % 4 == 0 else ("Chest" if 1952 % 4 == 1 else ("Weapon" if 1952 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 23424
    REQUIRE_LEVEL = 40
    SELL_PRICE = 195200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1953:
    PREFAB_ID = "item_prefab_1953"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1953"
    EQUIPMENT_SLOT = "Head" if 1953 % 4 == 0 else ("Chest" if 1953 % 4 == 1 else ("Weapon" if 1953 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 23436
    REQUIRE_LEVEL = 40
    SELL_PRICE = 195300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1954:
    PREFAB_ID = "item_prefab_1954"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1954"
    EQUIPMENT_SLOT = "Head" if 1954 % 4 == 0 else ("Chest" if 1954 % 4 == 1 else ("Weapon" if 1954 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 23448
    REQUIRE_LEVEL = 40
    SELL_PRICE = 195400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1955:
    PREFAB_ID = "item_prefab_1955"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1955"
    EQUIPMENT_SLOT = "Head" if 1955 % 4 == 0 else ("Chest" if 1955 % 4 == 1 else ("Weapon" if 1955 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 23460
    REQUIRE_LEVEL = 40
    SELL_PRICE = 195500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1956:
    PREFAB_ID = "item_prefab_1956"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1956"
    EQUIPMENT_SLOT = "Head" if 1956 % 4 == 0 else ("Chest" if 1956 % 4 == 1 else ("Weapon" if 1956 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 23472
    REQUIRE_LEVEL = 40
    SELL_PRICE = 195600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1957:
    PREFAB_ID = "item_prefab_1957"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1957"
    EQUIPMENT_SLOT = "Head" if 1957 % 4 == 0 else ("Chest" if 1957 % 4 == 1 else ("Weapon" if 1957 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 23484
    REQUIRE_LEVEL = 40
    SELL_PRICE = 195700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1958:
    PREFAB_ID = "item_prefab_1958"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1958"
    EQUIPMENT_SLOT = "Head" if 1958 % 4 == 0 else ("Chest" if 1958 % 4 == 1 else ("Weapon" if 1958 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 23496
    REQUIRE_LEVEL = 40
    SELL_PRICE = 195800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1959:
    PREFAB_ID = "item_prefab_1959"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1959"
    EQUIPMENT_SLOT = "Head" if 1959 % 4 == 0 else ("Chest" if 1959 % 4 == 1 else ("Weapon" if 1959 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 23508
    REQUIRE_LEVEL = 40
    SELL_PRICE = 195900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1960:
    PREFAB_ID = "item_prefab_1960"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1960"
    EQUIPMENT_SLOT = "Head" if 1960 % 4 == 0 else ("Chest" if 1960 % 4 == 1 else ("Weapon" if 1960 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 23520
    REQUIRE_LEVEL = 40
    SELL_PRICE = 196000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1961:
    PREFAB_ID = "item_prefab_1961"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1961"
    EQUIPMENT_SLOT = "Head" if 1961 % 4 == 0 else ("Chest" if 1961 % 4 == 1 else ("Weapon" if 1961 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 23532
    REQUIRE_LEVEL = 40
    SELL_PRICE = 196100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1962:
    PREFAB_ID = "item_prefab_1962"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1962"
    EQUIPMENT_SLOT = "Head" if 1962 % 4 == 0 else ("Chest" if 1962 % 4 == 1 else ("Weapon" if 1962 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 23544
    REQUIRE_LEVEL = 40
    SELL_PRICE = 196200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1963:
    PREFAB_ID = "item_prefab_1963"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1963"
    EQUIPMENT_SLOT = "Head" if 1963 % 4 == 0 else ("Chest" if 1963 % 4 == 1 else ("Weapon" if 1963 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 23556
    REQUIRE_LEVEL = 40
    SELL_PRICE = 196300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1964:
    PREFAB_ID = "item_prefab_1964"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1964"
    EQUIPMENT_SLOT = "Head" if 1964 % 4 == 0 else ("Chest" if 1964 % 4 == 1 else ("Weapon" if 1964 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 23568
    REQUIRE_LEVEL = 40
    SELL_PRICE = 196400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1965:
    PREFAB_ID = "item_prefab_1965"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1965"
    EQUIPMENT_SLOT = "Head" if 1965 % 4 == 0 else ("Chest" if 1965 % 4 == 1 else ("Weapon" if 1965 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 23580
    REQUIRE_LEVEL = 40
    SELL_PRICE = 196500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1966:
    PREFAB_ID = "item_prefab_1966"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1966"
    EQUIPMENT_SLOT = "Head" if 1966 % 4 == 0 else ("Chest" if 1966 % 4 == 1 else ("Weapon" if 1966 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 23592
    REQUIRE_LEVEL = 40
    SELL_PRICE = 196600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1967:
    PREFAB_ID = "item_prefab_1967"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1967"
    EQUIPMENT_SLOT = "Head" if 1967 % 4 == 0 else ("Chest" if 1967 % 4 == 1 else ("Weapon" if 1967 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 23604
    REQUIRE_LEVEL = 40
    SELL_PRICE = 196700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1968:
    PREFAB_ID = "item_prefab_1968"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1968"
    EQUIPMENT_SLOT = "Head" if 1968 % 4 == 0 else ("Chest" if 1968 % 4 == 1 else ("Weapon" if 1968 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 23616
    REQUIRE_LEVEL = 40
    SELL_PRICE = 196800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1969:
    PREFAB_ID = "item_prefab_1969"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1969"
    EQUIPMENT_SLOT = "Head" if 1969 % 4 == 0 else ("Chest" if 1969 % 4 == 1 else ("Weapon" if 1969 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 23628
    REQUIRE_LEVEL = 40
    SELL_PRICE = 196900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1970:
    PREFAB_ID = "item_prefab_1970"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1970"
    EQUIPMENT_SLOT = "Head" if 1970 % 4 == 0 else ("Chest" if 1970 % 4 == 1 else ("Weapon" if 1970 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 23640
    REQUIRE_LEVEL = 40
    SELL_PRICE = 197000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1971:
    PREFAB_ID = "item_prefab_1971"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1971"
    EQUIPMENT_SLOT = "Head" if 1971 % 4 == 0 else ("Chest" if 1971 % 4 == 1 else ("Weapon" if 1971 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 23652
    REQUIRE_LEVEL = 40
    SELL_PRICE = 197100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1972:
    PREFAB_ID = "item_prefab_1972"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1972"
    EQUIPMENT_SLOT = "Head" if 1972 % 4 == 0 else ("Chest" if 1972 % 4 == 1 else ("Weapon" if 1972 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 23664
    REQUIRE_LEVEL = 40
    SELL_PRICE = 197200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1973:
    PREFAB_ID = "item_prefab_1973"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1973"
    EQUIPMENT_SLOT = "Head" if 1973 % 4 == 0 else ("Chest" if 1973 % 4 == 1 else ("Weapon" if 1973 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 23676
    REQUIRE_LEVEL = 40
    SELL_PRICE = 197300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1974:
    PREFAB_ID = "item_prefab_1974"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1974"
    EQUIPMENT_SLOT = "Head" if 1974 % 4 == 0 else ("Chest" if 1974 % 4 == 1 else ("Weapon" if 1974 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 23688
    REQUIRE_LEVEL = 40
    SELL_PRICE = 197400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1975:
    PREFAB_ID = "item_prefab_1975"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1975"
    EQUIPMENT_SLOT = "Head" if 1975 % 4 == 0 else ("Chest" if 1975 % 4 == 1 else ("Weapon" if 1975 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 23700
    REQUIRE_LEVEL = 40
    SELL_PRICE = 197500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1976:
    PREFAB_ID = "item_prefab_1976"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1976"
    EQUIPMENT_SLOT = "Head" if 1976 % 4 == 0 else ("Chest" if 1976 % 4 == 1 else ("Weapon" if 1976 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 23712
    REQUIRE_LEVEL = 40
    SELL_PRICE = 197600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1977:
    PREFAB_ID = "item_prefab_1977"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1977"
    EQUIPMENT_SLOT = "Head" if 1977 % 4 == 0 else ("Chest" if 1977 % 4 == 1 else ("Weapon" if 1977 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 23724
    REQUIRE_LEVEL = 40
    SELL_PRICE = 197700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1978:
    PREFAB_ID = "item_prefab_1978"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1978"
    EQUIPMENT_SLOT = "Head" if 1978 % 4 == 0 else ("Chest" if 1978 % 4 == 1 else ("Weapon" if 1978 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 23736
    REQUIRE_LEVEL = 40
    SELL_PRICE = 197800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1979:
    PREFAB_ID = "item_prefab_1979"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1979"
    EQUIPMENT_SLOT = "Head" if 1979 % 4 == 0 else ("Chest" if 1979 % 4 == 1 else ("Weapon" if 1979 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 23748
    REQUIRE_LEVEL = 40
    SELL_PRICE = 197900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1980:
    PREFAB_ID = "item_prefab_1980"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1980"
    EQUIPMENT_SLOT = "Head" if 1980 % 4 == 0 else ("Chest" if 1980 % 4 == 1 else ("Weapon" if 1980 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 23760
    REQUIRE_LEVEL = 40
    SELL_PRICE = 198000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1981:
    PREFAB_ID = "item_prefab_1981"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1981"
    EQUIPMENT_SLOT = "Head" if 1981 % 4 == 0 else ("Chest" if 1981 % 4 == 1 else ("Weapon" if 1981 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 23772
    REQUIRE_LEVEL = 40
    SELL_PRICE = 198100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1982:
    PREFAB_ID = "item_prefab_1982"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1982"
    EQUIPMENT_SLOT = "Head" if 1982 % 4 == 0 else ("Chest" if 1982 % 4 == 1 else ("Weapon" if 1982 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 23784
    REQUIRE_LEVEL = 40
    SELL_PRICE = 198200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1983:
    PREFAB_ID = "item_prefab_1983"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1983"
    EQUIPMENT_SLOT = "Head" if 1983 % 4 == 0 else ("Chest" if 1983 % 4 == 1 else ("Weapon" if 1983 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 23796
    REQUIRE_LEVEL = 40
    SELL_PRICE = 198300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1984:
    PREFAB_ID = "item_prefab_1984"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1984"
    EQUIPMENT_SLOT = "Head" if 1984 % 4 == 0 else ("Chest" if 1984 % 4 == 1 else ("Weapon" if 1984 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 23808
    REQUIRE_LEVEL = 40
    SELL_PRICE = 198400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1985:
    PREFAB_ID = "item_prefab_1985"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1985"
    EQUIPMENT_SLOT = "Head" if 1985 % 4 == 0 else ("Chest" if 1985 % 4 == 1 else ("Weapon" if 1985 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 23820
    REQUIRE_LEVEL = 40
    SELL_PRICE = 198500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1986:
    PREFAB_ID = "item_prefab_1986"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1986"
    EQUIPMENT_SLOT = "Head" if 1986 % 4 == 0 else ("Chest" if 1986 % 4 == 1 else ("Weapon" if 1986 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 23832
    REQUIRE_LEVEL = 40
    SELL_PRICE = 198600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1987:
    PREFAB_ID = "item_prefab_1987"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1987"
    EQUIPMENT_SLOT = "Head" if 1987 % 4 == 0 else ("Chest" if 1987 % 4 == 1 else ("Weapon" if 1987 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 23844
    REQUIRE_LEVEL = 40
    SELL_PRICE = 198700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1988:
    PREFAB_ID = "item_prefab_1988"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1988"
    EQUIPMENT_SLOT = "Head" if 1988 % 4 == 0 else ("Chest" if 1988 % 4 == 1 else ("Weapon" if 1988 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 23856
    REQUIRE_LEVEL = 40
    SELL_PRICE = 198800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1989:
    PREFAB_ID = "item_prefab_1989"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1989"
    EQUIPMENT_SLOT = "Head" if 1989 % 4 == 0 else ("Chest" if 1989 % 4 == 1 else ("Weapon" if 1989 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 23868
    REQUIRE_LEVEL = 40
    SELL_PRICE = 198900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1990:
    PREFAB_ID = "item_prefab_1990"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1990"
    EQUIPMENT_SLOT = "Head" if 1990 % 4 == 0 else ("Chest" if 1990 % 4 == 1 else ("Weapon" if 1990 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 23880
    REQUIRE_LEVEL = 40
    SELL_PRICE = 199000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1991:
    PREFAB_ID = "item_prefab_1991"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1991"
    EQUIPMENT_SLOT = "Head" if 1991 % 4 == 0 else ("Chest" if 1991 % 4 == 1 else ("Weapon" if 1991 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 23892
    REQUIRE_LEVEL = 40
    SELL_PRICE = 199100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1992:
    PREFAB_ID = "item_prefab_1992"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1992"
    EQUIPMENT_SLOT = "Head" if 1992 % 4 == 0 else ("Chest" if 1992 % 4 == 1 else ("Weapon" if 1992 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 23904
    REQUIRE_LEVEL = 40
    SELL_PRICE = 199200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1993:
    PREFAB_ID = "item_prefab_1993"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1993"
    EQUIPMENT_SLOT = "Head" if 1993 % 4 == 0 else ("Chest" if 1993 % 4 == 1 else ("Weapon" if 1993 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 23916
    REQUIRE_LEVEL = 40
    SELL_PRICE = 199300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1994:
    PREFAB_ID = "item_prefab_1994"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1994"
    EQUIPMENT_SLOT = "Head" if 1994 % 4 == 0 else ("Chest" if 1994 % 4 == 1 else ("Weapon" if 1994 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 23928
    REQUIRE_LEVEL = 40
    SELL_PRICE = 199400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1995:
    PREFAB_ID = "item_prefab_1995"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1995"
    EQUIPMENT_SLOT = "Head" if 1995 % 4 == 0 else ("Chest" if 1995 % 4 == 1 else ("Weapon" if 1995 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 23940
    REQUIRE_LEVEL = 40
    SELL_PRICE = 199500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1996:
    PREFAB_ID = "item_prefab_1996"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1996"
    EQUIPMENT_SLOT = "Head" if 1996 % 4 == 0 else ("Chest" if 1996 % 4 == 1 else ("Weapon" if 1996 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 23952
    REQUIRE_LEVEL = 40
    SELL_PRICE = 199600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1997:
    PREFAB_ID = "item_prefab_1997"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1997"
    EQUIPMENT_SLOT = "Head" if 1997 % 4 == 0 else ("Chest" if 1997 % 4 == 1 else ("Weapon" if 1997 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 23964
    REQUIRE_LEVEL = 40
    SELL_PRICE = 199700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1998:
    PREFAB_ID = "item_prefab_1998"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1998"
    EQUIPMENT_SLOT = "Head" if 1998 % 4 == 0 else ("Chest" if 1998 % 4 == 1 else ("Weapon" if 1998 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 23976
    REQUIRE_LEVEL = 40
    SELL_PRICE = 199800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_1999:
    PREFAB_ID = "item_prefab_1999"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #1999"
    EQUIPMENT_SLOT = "Head" if 1999 % 4 == 0 else ("Chest" if 1999 % 4 == 1 else ("Weapon" if 1999 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 23988
    REQUIRE_LEVEL = 40
    SELL_PRICE = 199900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2000:
    PREFAB_ID = "item_prefab_2000"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2000"
    EQUIPMENT_SLOT = "Head" if 2000 % 4 == 0 else ("Chest" if 2000 % 4 == 1 else ("Weapon" if 2000 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 24000
    REQUIRE_LEVEL = 41
    SELL_PRICE = 200000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2001:
    PREFAB_ID = "item_prefab_2001"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2001"
    EQUIPMENT_SLOT = "Head" if 2001 % 4 == 0 else ("Chest" if 2001 % 4 == 1 else ("Weapon" if 2001 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 24012
    REQUIRE_LEVEL = 41
    SELL_PRICE = 200100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2002:
    PREFAB_ID = "item_prefab_2002"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2002"
    EQUIPMENT_SLOT = "Head" if 2002 % 4 == 0 else ("Chest" if 2002 % 4 == 1 else ("Weapon" if 2002 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 24024
    REQUIRE_LEVEL = 41
    SELL_PRICE = 200200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2003:
    PREFAB_ID = "item_prefab_2003"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2003"
    EQUIPMENT_SLOT = "Head" if 2003 % 4 == 0 else ("Chest" if 2003 % 4 == 1 else ("Weapon" if 2003 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 24036
    REQUIRE_LEVEL = 41
    SELL_PRICE = 200300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2004:
    PREFAB_ID = "item_prefab_2004"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2004"
    EQUIPMENT_SLOT = "Head" if 2004 % 4 == 0 else ("Chest" if 2004 % 4 == 1 else ("Weapon" if 2004 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 24048
    REQUIRE_LEVEL = 41
    SELL_PRICE = 200400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2005:
    PREFAB_ID = "item_prefab_2005"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2005"
    EQUIPMENT_SLOT = "Head" if 2005 % 4 == 0 else ("Chest" if 2005 % 4 == 1 else ("Weapon" if 2005 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 24060
    REQUIRE_LEVEL = 41
    SELL_PRICE = 200500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2006:
    PREFAB_ID = "item_prefab_2006"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2006"
    EQUIPMENT_SLOT = "Head" if 2006 % 4 == 0 else ("Chest" if 2006 % 4 == 1 else ("Weapon" if 2006 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 24072
    REQUIRE_LEVEL = 41
    SELL_PRICE = 200600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2007:
    PREFAB_ID = "item_prefab_2007"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2007"
    EQUIPMENT_SLOT = "Head" if 2007 % 4 == 0 else ("Chest" if 2007 % 4 == 1 else ("Weapon" if 2007 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 24084
    REQUIRE_LEVEL = 41
    SELL_PRICE = 200700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2008:
    PREFAB_ID = "item_prefab_2008"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2008"
    EQUIPMENT_SLOT = "Head" if 2008 % 4 == 0 else ("Chest" if 2008 % 4 == 1 else ("Weapon" if 2008 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 24096
    REQUIRE_LEVEL = 41
    SELL_PRICE = 200800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2009:
    PREFAB_ID = "item_prefab_2009"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2009"
    EQUIPMENT_SLOT = "Head" if 2009 % 4 == 0 else ("Chest" if 2009 % 4 == 1 else ("Weapon" if 2009 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 24108
    REQUIRE_LEVEL = 41
    SELL_PRICE = 200900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2010:
    PREFAB_ID = "item_prefab_2010"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2010"
    EQUIPMENT_SLOT = "Head" if 2010 % 4 == 0 else ("Chest" if 2010 % 4 == 1 else ("Weapon" if 2010 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 24120
    REQUIRE_LEVEL = 41
    SELL_PRICE = 201000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2011:
    PREFAB_ID = "item_prefab_2011"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2011"
    EQUIPMENT_SLOT = "Head" if 2011 % 4 == 0 else ("Chest" if 2011 % 4 == 1 else ("Weapon" if 2011 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 24132
    REQUIRE_LEVEL = 41
    SELL_PRICE = 201100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2012:
    PREFAB_ID = "item_prefab_2012"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2012"
    EQUIPMENT_SLOT = "Head" if 2012 % 4 == 0 else ("Chest" if 2012 % 4 == 1 else ("Weapon" if 2012 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 24144
    REQUIRE_LEVEL = 41
    SELL_PRICE = 201200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2013:
    PREFAB_ID = "item_prefab_2013"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2013"
    EQUIPMENT_SLOT = "Head" if 2013 % 4 == 0 else ("Chest" if 2013 % 4 == 1 else ("Weapon" if 2013 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 24156
    REQUIRE_LEVEL = 41
    SELL_PRICE = 201300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2014:
    PREFAB_ID = "item_prefab_2014"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2014"
    EQUIPMENT_SLOT = "Head" if 2014 % 4 == 0 else ("Chest" if 2014 % 4 == 1 else ("Weapon" if 2014 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 24168
    REQUIRE_LEVEL = 41
    SELL_PRICE = 201400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2015:
    PREFAB_ID = "item_prefab_2015"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2015"
    EQUIPMENT_SLOT = "Head" if 2015 % 4 == 0 else ("Chest" if 2015 % 4 == 1 else ("Weapon" if 2015 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 24180
    REQUIRE_LEVEL = 41
    SELL_PRICE = 201500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2016:
    PREFAB_ID = "item_prefab_2016"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2016"
    EQUIPMENT_SLOT = "Head" if 2016 % 4 == 0 else ("Chest" if 2016 % 4 == 1 else ("Weapon" if 2016 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 24192
    REQUIRE_LEVEL = 41
    SELL_PRICE = 201600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2017:
    PREFAB_ID = "item_prefab_2017"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2017"
    EQUIPMENT_SLOT = "Head" if 2017 % 4 == 0 else ("Chest" if 2017 % 4 == 1 else ("Weapon" if 2017 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 24204
    REQUIRE_LEVEL = 41
    SELL_PRICE = 201700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2018:
    PREFAB_ID = "item_prefab_2018"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2018"
    EQUIPMENT_SLOT = "Head" if 2018 % 4 == 0 else ("Chest" if 2018 % 4 == 1 else ("Weapon" if 2018 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 24216
    REQUIRE_LEVEL = 41
    SELL_PRICE = 201800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2019:
    PREFAB_ID = "item_prefab_2019"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2019"
    EQUIPMENT_SLOT = "Head" if 2019 % 4 == 0 else ("Chest" if 2019 % 4 == 1 else ("Weapon" if 2019 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 24228
    REQUIRE_LEVEL = 41
    SELL_PRICE = 201900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2020:
    PREFAB_ID = "item_prefab_2020"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2020"
    EQUIPMENT_SLOT = "Head" if 2020 % 4 == 0 else ("Chest" if 2020 % 4 == 1 else ("Weapon" if 2020 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 24240
    REQUIRE_LEVEL = 41
    SELL_PRICE = 202000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2021:
    PREFAB_ID = "item_prefab_2021"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2021"
    EQUIPMENT_SLOT = "Head" if 2021 % 4 == 0 else ("Chest" if 2021 % 4 == 1 else ("Weapon" if 2021 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 24252
    REQUIRE_LEVEL = 41
    SELL_PRICE = 202100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2022:
    PREFAB_ID = "item_prefab_2022"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2022"
    EQUIPMENT_SLOT = "Head" if 2022 % 4 == 0 else ("Chest" if 2022 % 4 == 1 else ("Weapon" if 2022 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 24264
    REQUIRE_LEVEL = 41
    SELL_PRICE = 202200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2023:
    PREFAB_ID = "item_prefab_2023"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2023"
    EQUIPMENT_SLOT = "Head" if 2023 % 4 == 0 else ("Chest" if 2023 % 4 == 1 else ("Weapon" if 2023 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 24276
    REQUIRE_LEVEL = 41
    SELL_PRICE = 202300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2024:
    PREFAB_ID = "item_prefab_2024"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2024"
    EQUIPMENT_SLOT = "Head" if 2024 % 4 == 0 else ("Chest" if 2024 % 4 == 1 else ("Weapon" if 2024 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 24288
    REQUIRE_LEVEL = 41
    SELL_PRICE = 202400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2025:
    PREFAB_ID = "item_prefab_2025"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2025"
    EQUIPMENT_SLOT = "Head" if 2025 % 4 == 0 else ("Chest" if 2025 % 4 == 1 else ("Weapon" if 2025 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 24300
    REQUIRE_LEVEL = 41
    SELL_PRICE = 202500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2026:
    PREFAB_ID = "item_prefab_2026"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2026"
    EQUIPMENT_SLOT = "Head" if 2026 % 4 == 0 else ("Chest" if 2026 % 4 == 1 else ("Weapon" if 2026 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 24312
    REQUIRE_LEVEL = 41
    SELL_PRICE = 202600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2027:
    PREFAB_ID = "item_prefab_2027"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2027"
    EQUIPMENT_SLOT = "Head" if 2027 % 4 == 0 else ("Chest" if 2027 % 4 == 1 else ("Weapon" if 2027 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 24324
    REQUIRE_LEVEL = 41
    SELL_PRICE = 202700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2028:
    PREFAB_ID = "item_prefab_2028"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2028"
    EQUIPMENT_SLOT = "Head" if 2028 % 4 == 0 else ("Chest" if 2028 % 4 == 1 else ("Weapon" if 2028 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 24336
    REQUIRE_LEVEL = 41
    SELL_PRICE = 202800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2029:
    PREFAB_ID = "item_prefab_2029"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2029"
    EQUIPMENT_SLOT = "Head" if 2029 % 4 == 0 else ("Chest" if 2029 % 4 == 1 else ("Weapon" if 2029 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 24348
    REQUIRE_LEVEL = 41
    SELL_PRICE = 202900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2030:
    PREFAB_ID = "item_prefab_2030"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2030"
    EQUIPMENT_SLOT = "Head" if 2030 % 4 == 0 else ("Chest" if 2030 % 4 == 1 else ("Weapon" if 2030 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 24360
    REQUIRE_LEVEL = 41
    SELL_PRICE = 203000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2031:
    PREFAB_ID = "item_prefab_2031"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2031"
    EQUIPMENT_SLOT = "Head" if 2031 % 4 == 0 else ("Chest" if 2031 % 4 == 1 else ("Weapon" if 2031 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 24372
    REQUIRE_LEVEL = 41
    SELL_PRICE = 203100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2032:
    PREFAB_ID = "item_prefab_2032"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2032"
    EQUIPMENT_SLOT = "Head" if 2032 % 4 == 0 else ("Chest" if 2032 % 4 == 1 else ("Weapon" if 2032 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 24384
    REQUIRE_LEVEL = 41
    SELL_PRICE = 203200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2033:
    PREFAB_ID = "item_prefab_2033"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2033"
    EQUIPMENT_SLOT = "Head" if 2033 % 4 == 0 else ("Chest" if 2033 % 4 == 1 else ("Weapon" if 2033 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 24396
    REQUIRE_LEVEL = 41
    SELL_PRICE = 203300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2034:
    PREFAB_ID = "item_prefab_2034"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2034"
    EQUIPMENT_SLOT = "Head" if 2034 % 4 == 0 else ("Chest" if 2034 % 4 == 1 else ("Weapon" if 2034 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 24408
    REQUIRE_LEVEL = 41
    SELL_PRICE = 203400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2035:
    PREFAB_ID = "item_prefab_2035"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2035"
    EQUIPMENT_SLOT = "Head" if 2035 % 4 == 0 else ("Chest" if 2035 % 4 == 1 else ("Weapon" if 2035 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 24420
    REQUIRE_LEVEL = 41
    SELL_PRICE = 203500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2036:
    PREFAB_ID = "item_prefab_2036"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2036"
    EQUIPMENT_SLOT = "Head" if 2036 % 4 == 0 else ("Chest" if 2036 % 4 == 1 else ("Weapon" if 2036 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 24432
    REQUIRE_LEVEL = 41
    SELL_PRICE = 203600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2037:
    PREFAB_ID = "item_prefab_2037"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2037"
    EQUIPMENT_SLOT = "Head" if 2037 % 4 == 0 else ("Chest" if 2037 % 4 == 1 else ("Weapon" if 2037 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 24444
    REQUIRE_LEVEL = 41
    SELL_PRICE = 203700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2038:
    PREFAB_ID = "item_prefab_2038"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2038"
    EQUIPMENT_SLOT = "Head" if 2038 % 4 == 0 else ("Chest" if 2038 % 4 == 1 else ("Weapon" if 2038 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 24456
    REQUIRE_LEVEL = 41
    SELL_PRICE = 203800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2039:
    PREFAB_ID = "item_prefab_2039"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2039"
    EQUIPMENT_SLOT = "Head" if 2039 % 4 == 0 else ("Chest" if 2039 % 4 == 1 else ("Weapon" if 2039 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 24468
    REQUIRE_LEVEL = 41
    SELL_PRICE = 203900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2040:
    PREFAB_ID = "item_prefab_2040"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2040"
    EQUIPMENT_SLOT = "Head" if 2040 % 4 == 0 else ("Chest" if 2040 % 4 == 1 else ("Weapon" if 2040 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 24480
    REQUIRE_LEVEL = 41
    SELL_PRICE = 204000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2041:
    PREFAB_ID = "item_prefab_2041"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2041"
    EQUIPMENT_SLOT = "Head" if 2041 % 4 == 0 else ("Chest" if 2041 % 4 == 1 else ("Weapon" if 2041 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 24492
    REQUIRE_LEVEL = 41
    SELL_PRICE = 204100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2042:
    PREFAB_ID = "item_prefab_2042"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2042"
    EQUIPMENT_SLOT = "Head" if 2042 % 4 == 0 else ("Chest" if 2042 % 4 == 1 else ("Weapon" if 2042 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 24504
    REQUIRE_LEVEL = 41
    SELL_PRICE = 204200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2043:
    PREFAB_ID = "item_prefab_2043"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2043"
    EQUIPMENT_SLOT = "Head" if 2043 % 4 == 0 else ("Chest" if 2043 % 4 == 1 else ("Weapon" if 2043 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 24516
    REQUIRE_LEVEL = 41
    SELL_PRICE = 204300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2044:
    PREFAB_ID = "item_prefab_2044"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2044"
    EQUIPMENT_SLOT = "Head" if 2044 % 4 == 0 else ("Chest" if 2044 % 4 == 1 else ("Weapon" if 2044 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 24528
    REQUIRE_LEVEL = 41
    SELL_PRICE = 204400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2045:
    PREFAB_ID = "item_prefab_2045"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2045"
    EQUIPMENT_SLOT = "Head" if 2045 % 4 == 0 else ("Chest" if 2045 % 4 == 1 else ("Weapon" if 2045 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 24540
    REQUIRE_LEVEL = 41
    SELL_PRICE = 204500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2046:
    PREFAB_ID = "item_prefab_2046"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2046"
    EQUIPMENT_SLOT = "Head" if 2046 % 4 == 0 else ("Chest" if 2046 % 4 == 1 else ("Weapon" if 2046 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 24552
    REQUIRE_LEVEL = 41
    SELL_PRICE = 204600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2047:
    PREFAB_ID = "item_prefab_2047"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2047"
    EQUIPMENT_SLOT = "Head" if 2047 % 4 == 0 else ("Chest" if 2047 % 4 == 1 else ("Weapon" if 2047 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 24564
    REQUIRE_LEVEL = 41
    SELL_PRICE = 204700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2048:
    PREFAB_ID = "item_prefab_2048"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2048"
    EQUIPMENT_SLOT = "Head" if 2048 % 4 == 0 else ("Chest" if 2048 % 4 == 1 else ("Weapon" if 2048 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 24576
    REQUIRE_LEVEL = 41
    SELL_PRICE = 204800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2049:
    PREFAB_ID = "item_prefab_2049"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2049"
    EQUIPMENT_SLOT = "Head" if 2049 % 4 == 0 else ("Chest" if 2049 % 4 == 1 else ("Weapon" if 2049 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 24588
    REQUIRE_LEVEL = 41
    SELL_PRICE = 204900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2050:
    PREFAB_ID = "item_prefab_2050"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2050"
    EQUIPMENT_SLOT = "Head" if 2050 % 4 == 0 else ("Chest" if 2050 % 4 == 1 else ("Weapon" if 2050 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 24600
    REQUIRE_LEVEL = 42
    SELL_PRICE = 205000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2051:
    PREFAB_ID = "item_prefab_2051"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2051"
    EQUIPMENT_SLOT = "Head" if 2051 % 4 == 0 else ("Chest" if 2051 % 4 == 1 else ("Weapon" if 2051 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 24612
    REQUIRE_LEVEL = 42
    SELL_PRICE = 205100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2052:
    PREFAB_ID = "item_prefab_2052"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2052"
    EQUIPMENT_SLOT = "Head" if 2052 % 4 == 0 else ("Chest" if 2052 % 4 == 1 else ("Weapon" if 2052 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 24624
    REQUIRE_LEVEL = 42
    SELL_PRICE = 205200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2053:
    PREFAB_ID = "item_prefab_2053"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2053"
    EQUIPMENT_SLOT = "Head" if 2053 % 4 == 0 else ("Chest" if 2053 % 4 == 1 else ("Weapon" if 2053 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 24636
    REQUIRE_LEVEL = 42
    SELL_PRICE = 205300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2054:
    PREFAB_ID = "item_prefab_2054"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2054"
    EQUIPMENT_SLOT = "Head" if 2054 % 4 == 0 else ("Chest" if 2054 % 4 == 1 else ("Weapon" if 2054 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 24648
    REQUIRE_LEVEL = 42
    SELL_PRICE = 205400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2055:
    PREFAB_ID = "item_prefab_2055"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2055"
    EQUIPMENT_SLOT = "Head" if 2055 % 4 == 0 else ("Chest" if 2055 % 4 == 1 else ("Weapon" if 2055 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 24660
    REQUIRE_LEVEL = 42
    SELL_PRICE = 205500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2056:
    PREFAB_ID = "item_prefab_2056"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2056"
    EQUIPMENT_SLOT = "Head" if 2056 % 4 == 0 else ("Chest" if 2056 % 4 == 1 else ("Weapon" if 2056 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 24672
    REQUIRE_LEVEL = 42
    SELL_PRICE = 205600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2057:
    PREFAB_ID = "item_prefab_2057"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2057"
    EQUIPMENT_SLOT = "Head" if 2057 % 4 == 0 else ("Chest" if 2057 % 4 == 1 else ("Weapon" if 2057 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 24684
    REQUIRE_LEVEL = 42
    SELL_PRICE = 205700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2058:
    PREFAB_ID = "item_prefab_2058"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2058"
    EQUIPMENT_SLOT = "Head" if 2058 % 4 == 0 else ("Chest" if 2058 % 4 == 1 else ("Weapon" if 2058 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 24696
    REQUIRE_LEVEL = 42
    SELL_PRICE = 205800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2059:
    PREFAB_ID = "item_prefab_2059"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2059"
    EQUIPMENT_SLOT = "Head" if 2059 % 4 == 0 else ("Chest" if 2059 % 4 == 1 else ("Weapon" if 2059 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 24708
    REQUIRE_LEVEL = 42
    SELL_PRICE = 205900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2060:
    PREFAB_ID = "item_prefab_2060"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2060"
    EQUIPMENT_SLOT = "Head" if 2060 % 4 == 0 else ("Chest" if 2060 % 4 == 1 else ("Weapon" if 2060 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 24720
    REQUIRE_LEVEL = 42
    SELL_PRICE = 206000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2061:
    PREFAB_ID = "item_prefab_2061"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2061"
    EQUIPMENT_SLOT = "Head" if 2061 % 4 == 0 else ("Chest" if 2061 % 4 == 1 else ("Weapon" if 2061 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 24732
    REQUIRE_LEVEL = 42
    SELL_PRICE = 206100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2062:
    PREFAB_ID = "item_prefab_2062"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2062"
    EQUIPMENT_SLOT = "Head" if 2062 % 4 == 0 else ("Chest" if 2062 % 4 == 1 else ("Weapon" if 2062 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 24744
    REQUIRE_LEVEL = 42
    SELL_PRICE = 206200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2063:
    PREFAB_ID = "item_prefab_2063"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2063"
    EQUIPMENT_SLOT = "Head" if 2063 % 4 == 0 else ("Chest" if 2063 % 4 == 1 else ("Weapon" if 2063 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 24756
    REQUIRE_LEVEL = 42
    SELL_PRICE = 206300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2064:
    PREFAB_ID = "item_prefab_2064"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2064"
    EQUIPMENT_SLOT = "Head" if 2064 % 4 == 0 else ("Chest" if 2064 % 4 == 1 else ("Weapon" if 2064 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 24768
    REQUIRE_LEVEL = 42
    SELL_PRICE = 206400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2065:
    PREFAB_ID = "item_prefab_2065"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2065"
    EQUIPMENT_SLOT = "Head" if 2065 % 4 == 0 else ("Chest" if 2065 % 4 == 1 else ("Weapon" if 2065 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 24780
    REQUIRE_LEVEL = 42
    SELL_PRICE = 206500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2066:
    PREFAB_ID = "item_prefab_2066"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2066"
    EQUIPMENT_SLOT = "Head" if 2066 % 4 == 0 else ("Chest" if 2066 % 4 == 1 else ("Weapon" if 2066 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 24792
    REQUIRE_LEVEL = 42
    SELL_PRICE = 206600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2067:
    PREFAB_ID = "item_prefab_2067"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2067"
    EQUIPMENT_SLOT = "Head" if 2067 % 4 == 0 else ("Chest" if 2067 % 4 == 1 else ("Weapon" if 2067 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 24804
    REQUIRE_LEVEL = 42
    SELL_PRICE = 206700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2068:
    PREFAB_ID = "item_prefab_2068"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2068"
    EQUIPMENT_SLOT = "Head" if 2068 % 4 == 0 else ("Chest" if 2068 % 4 == 1 else ("Weapon" if 2068 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 24816
    REQUIRE_LEVEL = 42
    SELL_PRICE = 206800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2069:
    PREFAB_ID = "item_prefab_2069"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2069"
    EQUIPMENT_SLOT = "Head" if 2069 % 4 == 0 else ("Chest" if 2069 % 4 == 1 else ("Weapon" if 2069 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 24828
    REQUIRE_LEVEL = 42
    SELL_PRICE = 206900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2070:
    PREFAB_ID = "item_prefab_2070"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2070"
    EQUIPMENT_SLOT = "Head" if 2070 % 4 == 0 else ("Chest" if 2070 % 4 == 1 else ("Weapon" if 2070 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 24840
    REQUIRE_LEVEL = 42
    SELL_PRICE = 207000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2071:
    PREFAB_ID = "item_prefab_2071"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2071"
    EQUIPMENT_SLOT = "Head" if 2071 % 4 == 0 else ("Chest" if 2071 % 4 == 1 else ("Weapon" if 2071 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 24852
    REQUIRE_LEVEL = 42
    SELL_PRICE = 207100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2072:
    PREFAB_ID = "item_prefab_2072"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2072"
    EQUIPMENT_SLOT = "Head" if 2072 % 4 == 0 else ("Chest" if 2072 % 4 == 1 else ("Weapon" if 2072 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 24864
    REQUIRE_LEVEL = 42
    SELL_PRICE = 207200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2073:
    PREFAB_ID = "item_prefab_2073"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2073"
    EQUIPMENT_SLOT = "Head" if 2073 % 4 == 0 else ("Chest" if 2073 % 4 == 1 else ("Weapon" if 2073 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 24876
    REQUIRE_LEVEL = 42
    SELL_PRICE = 207300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2074:
    PREFAB_ID = "item_prefab_2074"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2074"
    EQUIPMENT_SLOT = "Head" if 2074 % 4 == 0 else ("Chest" if 2074 % 4 == 1 else ("Weapon" if 2074 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 24888
    REQUIRE_LEVEL = 42
    SELL_PRICE = 207400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2075:
    PREFAB_ID = "item_prefab_2075"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2075"
    EQUIPMENT_SLOT = "Head" if 2075 % 4 == 0 else ("Chest" if 2075 % 4 == 1 else ("Weapon" if 2075 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 24900
    REQUIRE_LEVEL = 42
    SELL_PRICE = 207500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2076:
    PREFAB_ID = "item_prefab_2076"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2076"
    EQUIPMENT_SLOT = "Head" if 2076 % 4 == 0 else ("Chest" if 2076 % 4 == 1 else ("Weapon" if 2076 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 24912
    REQUIRE_LEVEL = 42
    SELL_PRICE = 207600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2077:
    PREFAB_ID = "item_prefab_2077"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2077"
    EQUIPMENT_SLOT = "Head" if 2077 % 4 == 0 else ("Chest" if 2077 % 4 == 1 else ("Weapon" if 2077 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 24924
    REQUIRE_LEVEL = 42
    SELL_PRICE = 207700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2078:
    PREFAB_ID = "item_prefab_2078"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2078"
    EQUIPMENT_SLOT = "Head" if 2078 % 4 == 0 else ("Chest" if 2078 % 4 == 1 else ("Weapon" if 2078 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 24936
    REQUIRE_LEVEL = 42
    SELL_PRICE = 207800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2079:
    PREFAB_ID = "item_prefab_2079"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2079"
    EQUIPMENT_SLOT = "Head" if 2079 % 4 == 0 else ("Chest" if 2079 % 4 == 1 else ("Weapon" if 2079 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 24948
    REQUIRE_LEVEL = 42
    SELL_PRICE = 207900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2080:
    PREFAB_ID = "item_prefab_2080"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2080"
    EQUIPMENT_SLOT = "Head" if 2080 % 4 == 0 else ("Chest" if 2080 % 4 == 1 else ("Weapon" if 2080 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 24960
    REQUIRE_LEVEL = 42
    SELL_PRICE = 208000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2081:
    PREFAB_ID = "item_prefab_2081"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2081"
    EQUIPMENT_SLOT = "Head" if 2081 % 4 == 0 else ("Chest" if 2081 % 4 == 1 else ("Weapon" if 2081 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 24972
    REQUIRE_LEVEL = 42
    SELL_PRICE = 208100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2082:
    PREFAB_ID = "item_prefab_2082"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2082"
    EQUIPMENT_SLOT = "Head" if 2082 % 4 == 0 else ("Chest" if 2082 % 4 == 1 else ("Weapon" if 2082 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 24984
    REQUIRE_LEVEL = 42
    SELL_PRICE = 208200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2083:
    PREFAB_ID = "item_prefab_2083"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2083"
    EQUIPMENT_SLOT = "Head" if 2083 % 4 == 0 else ("Chest" if 2083 % 4 == 1 else ("Weapon" if 2083 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 24996
    REQUIRE_LEVEL = 42
    SELL_PRICE = 208300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2084:
    PREFAB_ID = "item_prefab_2084"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2084"
    EQUIPMENT_SLOT = "Head" if 2084 % 4 == 0 else ("Chest" if 2084 % 4 == 1 else ("Weapon" if 2084 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 25008
    REQUIRE_LEVEL = 42
    SELL_PRICE = 208400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2085:
    PREFAB_ID = "item_prefab_2085"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2085"
    EQUIPMENT_SLOT = "Head" if 2085 % 4 == 0 else ("Chest" if 2085 % 4 == 1 else ("Weapon" if 2085 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 25020
    REQUIRE_LEVEL = 42
    SELL_PRICE = 208500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2086:
    PREFAB_ID = "item_prefab_2086"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2086"
    EQUIPMENT_SLOT = "Head" if 2086 % 4 == 0 else ("Chest" if 2086 % 4 == 1 else ("Weapon" if 2086 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 25032
    REQUIRE_LEVEL = 42
    SELL_PRICE = 208600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2087:
    PREFAB_ID = "item_prefab_2087"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2087"
    EQUIPMENT_SLOT = "Head" if 2087 % 4 == 0 else ("Chest" if 2087 % 4 == 1 else ("Weapon" if 2087 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 25044
    REQUIRE_LEVEL = 42
    SELL_PRICE = 208700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2088:
    PREFAB_ID = "item_prefab_2088"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2088"
    EQUIPMENT_SLOT = "Head" if 2088 % 4 == 0 else ("Chest" if 2088 % 4 == 1 else ("Weapon" if 2088 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 25056
    REQUIRE_LEVEL = 42
    SELL_PRICE = 208800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2089:
    PREFAB_ID = "item_prefab_2089"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2089"
    EQUIPMENT_SLOT = "Head" if 2089 % 4 == 0 else ("Chest" if 2089 % 4 == 1 else ("Weapon" if 2089 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 25068
    REQUIRE_LEVEL = 42
    SELL_PRICE = 208900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2090:
    PREFAB_ID = "item_prefab_2090"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2090"
    EQUIPMENT_SLOT = "Head" if 2090 % 4 == 0 else ("Chest" if 2090 % 4 == 1 else ("Weapon" if 2090 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 25080
    REQUIRE_LEVEL = 42
    SELL_PRICE = 209000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2091:
    PREFAB_ID = "item_prefab_2091"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2091"
    EQUIPMENT_SLOT = "Head" if 2091 % 4 == 0 else ("Chest" if 2091 % 4 == 1 else ("Weapon" if 2091 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 25092
    REQUIRE_LEVEL = 42
    SELL_PRICE = 209100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2092:
    PREFAB_ID = "item_prefab_2092"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2092"
    EQUIPMENT_SLOT = "Head" if 2092 % 4 == 0 else ("Chest" if 2092 % 4 == 1 else ("Weapon" if 2092 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 25104
    REQUIRE_LEVEL = 42
    SELL_PRICE = 209200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2093:
    PREFAB_ID = "item_prefab_2093"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2093"
    EQUIPMENT_SLOT = "Head" if 2093 % 4 == 0 else ("Chest" if 2093 % 4 == 1 else ("Weapon" if 2093 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 25116
    REQUIRE_LEVEL = 42
    SELL_PRICE = 209300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2094:
    PREFAB_ID = "item_prefab_2094"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2094"
    EQUIPMENT_SLOT = "Head" if 2094 % 4 == 0 else ("Chest" if 2094 % 4 == 1 else ("Weapon" if 2094 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 25128
    REQUIRE_LEVEL = 42
    SELL_PRICE = 209400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2095:
    PREFAB_ID = "item_prefab_2095"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2095"
    EQUIPMENT_SLOT = "Head" if 2095 % 4 == 0 else ("Chest" if 2095 % 4 == 1 else ("Weapon" if 2095 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 25140
    REQUIRE_LEVEL = 42
    SELL_PRICE = 209500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2096:
    PREFAB_ID = "item_prefab_2096"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2096"
    EQUIPMENT_SLOT = "Head" if 2096 % 4 == 0 else ("Chest" if 2096 % 4 == 1 else ("Weapon" if 2096 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 25152
    REQUIRE_LEVEL = 42
    SELL_PRICE = 209600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2097:
    PREFAB_ID = "item_prefab_2097"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2097"
    EQUIPMENT_SLOT = "Head" if 2097 % 4 == 0 else ("Chest" if 2097 % 4 == 1 else ("Weapon" if 2097 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 25164
    REQUIRE_LEVEL = 42
    SELL_PRICE = 209700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2098:
    PREFAB_ID = "item_prefab_2098"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2098"
    EQUIPMENT_SLOT = "Head" if 2098 % 4 == 0 else ("Chest" if 2098 % 4 == 1 else ("Weapon" if 2098 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 25176
    REQUIRE_LEVEL = 42
    SELL_PRICE = 209800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2099:
    PREFAB_ID = "item_prefab_2099"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2099"
    EQUIPMENT_SLOT = "Head" if 2099 % 4 == 0 else ("Chest" if 2099 % 4 == 1 else ("Weapon" if 2099 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 25188
    REQUIRE_LEVEL = 42
    SELL_PRICE = 209900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2100:
    PREFAB_ID = "item_prefab_2100"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2100"
    EQUIPMENT_SLOT = "Head" if 2100 % 4 == 0 else ("Chest" if 2100 % 4 == 1 else ("Weapon" if 2100 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 25200
    REQUIRE_LEVEL = 43
    SELL_PRICE = 210000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2101:
    PREFAB_ID = "item_prefab_2101"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2101"
    EQUIPMENT_SLOT = "Head" if 2101 % 4 == 0 else ("Chest" if 2101 % 4 == 1 else ("Weapon" if 2101 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 25212
    REQUIRE_LEVEL = 43
    SELL_PRICE = 210100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2102:
    PREFAB_ID = "item_prefab_2102"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2102"
    EQUIPMENT_SLOT = "Head" if 2102 % 4 == 0 else ("Chest" if 2102 % 4 == 1 else ("Weapon" if 2102 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 25224
    REQUIRE_LEVEL = 43
    SELL_PRICE = 210200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2103:
    PREFAB_ID = "item_prefab_2103"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2103"
    EQUIPMENT_SLOT = "Head" if 2103 % 4 == 0 else ("Chest" if 2103 % 4 == 1 else ("Weapon" if 2103 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 25236
    REQUIRE_LEVEL = 43
    SELL_PRICE = 210300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2104:
    PREFAB_ID = "item_prefab_2104"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2104"
    EQUIPMENT_SLOT = "Head" if 2104 % 4 == 0 else ("Chest" if 2104 % 4 == 1 else ("Weapon" if 2104 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 25248
    REQUIRE_LEVEL = 43
    SELL_PRICE = 210400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2105:
    PREFAB_ID = "item_prefab_2105"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2105"
    EQUIPMENT_SLOT = "Head" if 2105 % 4 == 0 else ("Chest" if 2105 % 4 == 1 else ("Weapon" if 2105 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 25260
    REQUIRE_LEVEL = 43
    SELL_PRICE = 210500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2106:
    PREFAB_ID = "item_prefab_2106"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2106"
    EQUIPMENT_SLOT = "Head" if 2106 % 4 == 0 else ("Chest" if 2106 % 4 == 1 else ("Weapon" if 2106 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 25272
    REQUIRE_LEVEL = 43
    SELL_PRICE = 210600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2107:
    PREFAB_ID = "item_prefab_2107"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2107"
    EQUIPMENT_SLOT = "Head" if 2107 % 4 == 0 else ("Chest" if 2107 % 4 == 1 else ("Weapon" if 2107 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 25284
    REQUIRE_LEVEL = 43
    SELL_PRICE = 210700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2108:
    PREFAB_ID = "item_prefab_2108"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2108"
    EQUIPMENT_SLOT = "Head" if 2108 % 4 == 0 else ("Chest" if 2108 % 4 == 1 else ("Weapon" if 2108 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 25296
    REQUIRE_LEVEL = 43
    SELL_PRICE = 210800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2109:
    PREFAB_ID = "item_prefab_2109"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2109"
    EQUIPMENT_SLOT = "Head" if 2109 % 4 == 0 else ("Chest" if 2109 % 4 == 1 else ("Weapon" if 2109 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 25308
    REQUIRE_LEVEL = 43
    SELL_PRICE = 210900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2110:
    PREFAB_ID = "item_prefab_2110"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2110"
    EQUIPMENT_SLOT = "Head" if 2110 % 4 == 0 else ("Chest" if 2110 % 4 == 1 else ("Weapon" if 2110 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 25320
    REQUIRE_LEVEL = 43
    SELL_PRICE = 211000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2111:
    PREFAB_ID = "item_prefab_2111"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2111"
    EQUIPMENT_SLOT = "Head" if 2111 % 4 == 0 else ("Chest" if 2111 % 4 == 1 else ("Weapon" if 2111 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 25332
    REQUIRE_LEVEL = 43
    SELL_PRICE = 211100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2112:
    PREFAB_ID = "item_prefab_2112"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2112"
    EQUIPMENT_SLOT = "Head" if 2112 % 4 == 0 else ("Chest" if 2112 % 4 == 1 else ("Weapon" if 2112 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 25344
    REQUIRE_LEVEL = 43
    SELL_PRICE = 211200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2113:
    PREFAB_ID = "item_prefab_2113"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2113"
    EQUIPMENT_SLOT = "Head" if 2113 % 4 == 0 else ("Chest" if 2113 % 4 == 1 else ("Weapon" if 2113 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 25356
    REQUIRE_LEVEL = 43
    SELL_PRICE = 211300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2114:
    PREFAB_ID = "item_prefab_2114"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2114"
    EQUIPMENT_SLOT = "Head" if 2114 % 4 == 0 else ("Chest" if 2114 % 4 == 1 else ("Weapon" if 2114 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 25368
    REQUIRE_LEVEL = 43
    SELL_PRICE = 211400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2115:
    PREFAB_ID = "item_prefab_2115"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2115"
    EQUIPMENT_SLOT = "Head" if 2115 % 4 == 0 else ("Chest" if 2115 % 4 == 1 else ("Weapon" if 2115 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 25380
    REQUIRE_LEVEL = 43
    SELL_PRICE = 211500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2116:
    PREFAB_ID = "item_prefab_2116"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2116"
    EQUIPMENT_SLOT = "Head" if 2116 % 4 == 0 else ("Chest" if 2116 % 4 == 1 else ("Weapon" if 2116 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 25392
    REQUIRE_LEVEL = 43
    SELL_PRICE = 211600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2117:
    PREFAB_ID = "item_prefab_2117"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2117"
    EQUIPMENT_SLOT = "Head" if 2117 % 4 == 0 else ("Chest" if 2117 % 4 == 1 else ("Weapon" if 2117 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 25404
    REQUIRE_LEVEL = 43
    SELL_PRICE = 211700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2118:
    PREFAB_ID = "item_prefab_2118"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2118"
    EQUIPMENT_SLOT = "Head" if 2118 % 4 == 0 else ("Chest" if 2118 % 4 == 1 else ("Weapon" if 2118 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 25416
    REQUIRE_LEVEL = 43
    SELL_PRICE = 211800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2119:
    PREFAB_ID = "item_prefab_2119"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2119"
    EQUIPMENT_SLOT = "Head" if 2119 % 4 == 0 else ("Chest" if 2119 % 4 == 1 else ("Weapon" if 2119 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 25428
    REQUIRE_LEVEL = 43
    SELL_PRICE = 211900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2120:
    PREFAB_ID = "item_prefab_2120"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2120"
    EQUIPMENT_SLOT = "Head" if 2120 % 4 == 0 else ("Chest" if 2120 % 4 == 1 else ("Weapon" if 2120 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 25440
    REQUIRE_LEVEL = 43
    SELL_PRICE = 212000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2121:
    PREFAB_ID = "item_prefab_2121"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2121"
    EQUIPMENT_SLOT = "Head" if 2121 % 4 == 0 else ("Chest" if 2121 % 4 == 1 else ("Weapon" if 2121 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 25452
    REQUIRE_LEVEL = 43
    SELL_PRICE = 212100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2122:
    PREFAB_ID = "item_prefab_2122"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2122"
    EQUIPMENT_SLOT = "Head" if 2122 % 4 == 0 else ("Chest" if 2122 % 4 == 1 else ("Weapon" if 2122 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 25464
    REQUIRE_LEVEL = 43
    SELL_PRICE = 212200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2123:
    PREFAB_ID = "item_prefab_2123"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2123"
    EQUIPMENT_SLOT = "Head" if 2123 % 4 == 0 else ("Chest" if 2123 % 4 == 1 else ("Weapon" if 2123 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 25476
    REQUIRE_LEVEL = 43
    SELL_PRICE = 212300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2124:
    PREFAB_ID = "item_prefab_2124"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2124"
    EQUIPMENT_SLOT = "Head" if 2124 % 4 == 0 else ("Chest" if 2124 % 4 == 1 else ("Weapon" if 2124 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 25488
    REQUIRE_LEVEL = 43
    SELL_PRICE = 212400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2125:
    PREFAB_ID = "item_prefab_2125"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2125"
    EQUIPMENT_SLOT = "Head" if 2125 % 4 == 0 else ("Chest" if 2125 % 4 == 1 else ("Weapon" if 2125 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 25500
    REQUIRE_LEVEL = 43
    SELL_PRICE = 212500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2126:
    PREFAB_ID = "item_prefab_2126"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2126"
    EQUIPMENT_SLOT = "Head" if 2126 % 4 == 0 else ("Chest" if 2126 % 4 == 1 else ("Weapon" if 2126 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 25512
    REQUIRE_LEVEL = 43
    SELL_PRICE = 212600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2127:
    PREFAB_ID = "item_prefab_2127"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2127"
    EQUIPMENT_SLOT = "Head" if 2127 % 4 == 0 else ("Chest" if 2127 % 4 == 1 else ("Weapon" if 2127 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 25524
    REQUIRE_LEVEL = 43
    SELL_PRICE = 212700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2128:
    PREFAB_ID = "item_prefab_2128"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2128"
    EQUIPMENT_SLOT = "Head" if 2128 % 4 == 0 else ("Chest" if 2128 % 4 == 1 else ("Weapon" if 2128 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 25536
    REQUIRE_LEVEL = 43
    SELL_PRICE = 212800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2129:
    PREFAB_ID = "item_prefab_2129"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2129"
    EQUIPMENT_SLOT = "Head" if 2129 % 4 == 0 else ("Chest" if 2129 % 4 == 1 else ("Weapon" if 2129 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 25548
    REQUIRE_LEVEL = 43
    SELL_PRICE = 212900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2130:
    PREFAB_ID = "item_prefab_2130"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2130"
    EQUIPMENT_SLOT = "Head" if 2130 % 4 == 0 else ("Chest" if 2130 % 4 == 1 else ("Weapon" if 2130 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 25560
    REQUIRE_LEVEL = 43
    SELL_PRICE = 213000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2131:
    PREFAB_ID = "item_prefab_2131"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2131"
    EQUIPMENT_SLOT = "Head" if 2131 % 4 == 0 else ("Chest" if 2131 % 4 == 1 else ("Weapon" if 2131 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 25572
    REQUIRE_LEVEL = 43
    SELL_PRICE = 213100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2132:
    PREFAB_ID = "item_prefab_2132"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2132"
    EQUIPMENT_SLOT = "Head" if 2132 % 4 == 0 else ("Chest" if 2132 % 4 == 1 else ("Weapon" if 2132 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 25584
    REQUIRE_LEVEL = 43
    SELL_PRICE = 213200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2133:
    PREFAB_ID = "item_prefab_2133"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2133"
    EQUIPMENT_SLOT = "Head" if 2133 % 4 == 0 else ("Chest" if 2133 % 4 == 1 else ("Weapon" if 2133 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 25596
    REQUIRE_LEVEL = 43
    SELL_PRICE = 213300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2134:
    PREFAB_ID = "item_prefab_2134"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2134"
    EQUIPMENT_SLOT = "Head" if 2134 % 4 == 0 else ("Chest" if 2134 % 4 == 1 else ("Weapon" if 2134 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 25608
    REQUIRE_LEVEL = 43
    SELL_PRICE = 213400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2135:
    PREFAB_ID = "item_prefab_2135"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2135"
    EQUIPMENT_SLOT = "Head" if 2135 % 4 == 0 else ("Chest" if 2135 % 4 == 1 else ("Weapon" if 2135 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 25620
    REQUIRE_LEVEL = 43
    SELL_PRICE = 213500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2136:
    PREFAB_ID = "item_prefab_2136"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2136"
    EQUIPMENT_SLOT = "Head" if 2136 % 4 == 0 else ("Chest" if 2136 % 4 == 1 else ("Weapon" if 2136 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 25632
    REQUIRE_LEVEL = 43
    SELL_PRICE = 213600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2137:
    PREFAB_ID = "item_prefab_2137"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2137"
    EQUIPMENT_SLOT = "Head" if 2137 % 4 == 0 else ("Chest" if 2137 % 4 == 1 else ("Weapon" if 2137 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 25644
    REQUIRE_LEVEL = 43
    SELL_PRICE = 213700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2138:
    PREFAB_ID = "item_prefab_2138"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2138"
    EQUIPMENT_SLOT = "Head" if 2138 % 4 == 0 else ("Chest" if 2138 % 4 == 1 else ("Weapon" if 2138 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 25656
    REQUIRE_LEVEL = 43
    SELL_PRICE = 213800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2139:
    PREFAB_ID = "item_prefab_2139"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2139"
    EQUIPMENT_SLOT = "Head" if 2139 % 4 == 0 else ("Chest" if 2139 % 4 == 1 else ("Weapon" if 2139 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 25668
    REQUIRE_LEVEL = 43
    SELL_PRICE = 213900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2140:
    PREFAB_ID = "item_prefab_2140"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2140"
    EQUIPMENT_SLOT = "Head" if 2140 % 4 == 0 else ("Chest" if 2140 % 4 == 1 else ("Weapon" if 2140 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 25680
    REQUIRE_LEVEL = 43
    SELL_PRICE = 214000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2141:
    PREFAB_ID = "item_prefab_2141"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2141"
    EQUIPMENT_SLOT = "Head" if 2141 % 4 == 0 else ("Chest" if 2141 % 4 == 1 else ("Weapon" if 2141 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 25692
    REQUIRE_LEVEL = 43
    SELL_PRICE = 214100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2142:
    PREFAB_ID = "item_prefab_2142"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2142"
    EQUIPMENT_SLOT = "Head" if 2142 % 4 == 0 else ("Chest" if 2142 % 4 == 1 else ("Weapon" if 2142 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 25704
    REQUIRE_LEVEL = 43
    SELL_PRICE = 214200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2143:
    PREFAB_ID = "item_prefab_2143"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2143"
    EQUIPMENT_SLOT = "Head" if 2143 % 4 == 0 else ("Chest" if 2143 % 4 == 1 else ("Weapon" if 2143 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 25716
    REQUIRE_LEVEL = 43
    SELL_PRICE = 214300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2144:
    PREFAB_ID = "item_prefab_2144"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2144"
    EQUIPMENT_SLOT = "Head" if 2144 % 4 == 0 else ("Chest" if 2144 % 4 == 1 else ("Weapon" if 2144 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 25728
    REQUIRE_LEVEL = 43
    SELL_PRICE = 214400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2145:
    PREFAB_ID = "item_prefab_2145"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2145"
    EQUIPMENT_SLOT = "Head" if 2145 % 4 == 0 else ("Chest" if 2145 % 4 == 1 else ("Weapon" if 2145 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 25740
    REQUIRE_LEVEL = 43
    SELL_PRICE = 214500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2146:
    PREFAB_ID = "item_prefab_2146"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2146"
    EQUIPMENT_SLOT = "Head" if 2146 % 4 == 0 else ("Chest" if 2146 % 4 == 1 else ("Weapon" if 2146 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 25752
    REQUIRE_LEVEL = 43
    SELL_PRICE = 214600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2147:
    PREFAB_ID = "item_prefab_2147"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2147"
    EQUIPMENT_SLOT = "Head" if 2147 % 4 == 0 else ("Chest" if 2147 % 4 == 1 else ("Weapon" if 2147 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 25764
    REQUIRE_LEVEL = 43
    SELL_PRICE = 214700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2148:
    PREFAB_ID = "item_prefab_2148"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2148"
    EQUIPMENT_SLOT = "Head" if 2148 % 4 == 0 else ("Chest" if 2148 % 4 == 1 else ("Weapon" if 2148 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 25776
    REQUIRE_LEVEL = 43
    SELL_PRICE = 214800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2149:
    PREFAB_ID = "item_prefab_2149"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2149"
    EQUIPMENT_SLOT = "Head" if 2149 % 4 == 0 else ("Chest" if 2149 % 4 == 1 else ("Weapon" if 2149 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 25788
    REQUIRE_LEVEL = 43
    SELL_PRICE = 214900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2150:
    PREFAB_ID = "item_prefab_2150"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2150"
    EQUIPMENT_SLOT = "Head" if 2150 % 4 == 0 else ("Chest" if 2150 % 4 == 1 else ("Weapon" if 2150 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 25800
    REQUIRE_LEVEL = 44
    SELL_PRICE = 215000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2151:
    PREFAB_ID = "item_prefab_2151"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2151"
    EQUIPMENT_SLOT = "Head" if 2151 % 4 == 0 else ("Chest" if 2151 % 4 == 1 else ("Weapon" if 2151 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 110
    STAT_POWER = 25812
    REQUIRE_LEVEL = 44
    SELL_PRICE = 215100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2152:
    PREFAB_ID = "item_prefab_2152"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2152"
    EQUIPMENT_SLOT = "Head" if 2152 % 4 == 0 else ("Chest" if 2152 % 4 == 1 else ("Weapon" if 2152 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 120
    STAT_POWER = 25824
    REQUIRE_LEVEL = 44
    SELL_PRICE = 215200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2153:
    PREFAB_ID = "item_prefab_2153"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2153"
    EQUIPMENT_SLOT = "Head" if 2153 % 4 == 0 else ("Chest" if 2153 % 4 == 1 else ("Weapon" if 2153 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 130
    STAT_POWER = 25836
    REQUIRE_LEVEL = 44
    SELL_PRICE = 215300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2154:
    PREFAB_ID = "item_prefab_2154"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2154"
    EQUIPMENT_SLOT = "Head" if 2154 % 4 == 0 else ("Chest" if 2154 % 4 == 1 else ("Weapon" if 2154 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 140
    STAT_POWER = 25848
    REQUIRE_LEVEL = 44
    SELL_PRICE = 215400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2155:
    PREFAB_ID = "item_prefab_2155"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2155"
    EQUIPMENT_SLOT = "Head" if 2155 % 4 == 0 else ("Chest" if 2155 % 4 == 1 else ("Weapon" if 2155 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 150
    STAT_POWER = 25860
    REQUIRE_LEVEL = 44
    SELL_PRICE = 215500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2156:
    PREFAB_ID = "item_prefab_2156"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2156"
    EQUIPMENT_SLOT = "Head" if 2156 % 4 == 0 else ("Chest" if 2156 % 4 == 1 else ("Weapon" if 2156 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 160
    STAT_POWER = 25872
    REQUIRE_LEVEL = 44
    SELL_PRICE = 215600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2157:
    PREFAB_ID = "item_prefab_2157"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2157"
    EQUIPMENT_SLOT = "Head" if 2157 % 4 == 0 else ("Chest" if 2157 % 4 == 1 else ("Weapon" if 2157 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 170
    STAT_POWER = 25884
    REQUIRE_LEVEL = 44
    SELL_PRICE = 215700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2158:
    PREFAB_ID = "item_prefab_2158"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2158"
    EQUIPMENT_SLOT = "Head" if 2158 % 4 == 0 else ("Chest" if 2158 % 4 == 1 else ("Weapon" if 2158 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 180
    STAT_POWER = 25896
    REQUIRE_LEVEL = 44
    SELL_PRICE = 215800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2159:
    PREFAB_ID = "item_prefab_2159"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2159"
    EQUIPMENT_SLOT = "Head" if 2159 % 4 == 0 else ("Chest" if 2159 % 4 == 1 else ("Weapon" if 2159 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 190
    STAT_POWER = 25908
    REQUIRE_LEVEL = 44
    SELL_PRICE = 215900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2160:
    PREFAB_ID = "item_prefab_2160"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2160"
    EQUIPMENT_SLOT = "Head" if 2160 % 4 == 0 else ("Chest" if 2160 % 4 == 1 else ("Weapon" if 2160 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 200
    STAT_POWER = 25920
    REQUIRE_LEVEL = 44
    SELL_PRICE = 216000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2161:
    PREFAB_ID = "item_prefab_2161"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2161"
    EQUIPMENT_SLOT = "Head" if 2161 % 4 == 0 else ("Chest" if 2161 % 4 == 1 else ("Weapon" if 2161 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 210
    STAT_POWER = 25932
    REQUIRE_LEVEL = 44
    SELL_PRICE = 216100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2162:
    PREFAB_ID = "item_prefab_2162"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2162"
    EQUIPMENT_SLOT = "Head" if 2162 % 4 == 0 else ("Chest" if 2162 % 4 == 1 else ("Weapon" if 2162 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 220
    STAT_POWER = 25944
    REQUIRE_LEVEL = 44
    SELL_PRICE = 216200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2163:
    PREFAB_ID = "item_prefab_2163"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2163"
    EQUIPMENT_SLOT = "Head" if 2163 % 4 == 0 else ("Chest" if 2163 % 4 == 1 else ("Weapon" if 2163 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 230
    STAT_POWER = 25956
    REQUIRE_LEVEL = 44
    SELL_PRICE = 216300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2164:
    PREFAB_ID = "item_prefab_2164"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2164"
    EQUIPMENT_SLOT = "Head" if 2164 % 4 == 0 else ("Chest" if 2164 % 4 == 1 else ("Weapon" if 2164 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 240
    STAT_POWER = 25968
    REQUIRE_LEVEL = 44
    SELL_PRICE = 216400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2165:
    PREFAB_ID = "item_prefab_2165"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2165"
    EQUIPMENT_SLOT = "Head" if 2165 % 4 == 0 else ("Chest" if 2165 % 4 == 1 else ("Weapon" if 2165 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 250
    STAT_POWER = 25980
    REQUIRE_LEVEL = 44
    SELL_PRICE = 216500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2166:
    PREFAB_ID = "item_prefab_2166"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2166"
    EQUIPMENT_SLOT = "Head" if 2166 % 4 == 0 else ("Chest" if 2166 % 4 == 1 else ("Weapon" if 2166 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 260
    STAT_POWER = 25992
    REQUIRE_LEVEL = 44
    SELL_PRICE = 216600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2167:
    PREFAB_ID = "item_prefab_2167"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2167"
    EQUIPMENT_SLOT = "Head" if 2167 % 4 == 0 else ("Chest" if 2167 % 4 == 1 else ("Weapon" if 2167 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 270
    STAT_POWER = 26004
    REQUIRE_LEVEL = 44
    SELL_PRICE = 216700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2168:
    PREFAB_ID = "item_prefab_2168"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2168"
    EQUIPMENT_SLOT = "Head" if 2168 % 4 == 0 else ("Chest" if 2168 % 4 == 1 else ("Weapon" if 2168 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 280
    STAT_POWER = 26016
    REQUIRE_LEVEL = 44
    SELL_PRICE = 216800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2169:
    PREFAB_ID = "item_prefab_2169"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2169"
    EQUIPMENT_SLOT = "Head" if 2169 % 4 == 0 else ("Chest" if 2169 % 4 == 1 else ("Weapon" if 2169 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 290
    STAT_POWER = 26028
    REQUIRE_LEVEL = 44
    SELL_PRICE = 216900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2170:
    PREFAB_ID = "item_prefab_2170"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2170"
    EQUIPMENT_SLOT = "Head" if 2170 % 4 == 0 else ("Chest" if 2170 % 4 == 1 else ("Weapon" if 2170 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 300
    STAT_POWER = 26040
    REQUIRE_LEVEL = 44
    SELL_PRICE = 217000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2171:
    PREFAB_ID = "item_prefab_2171"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2171"
    EQUIPMENT_SLOT = "Head" if 2171 % 4 == 0 else ("Chest" if 2171 % 4 == 1 else ("Weapon" if 2171 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 310
    STAT_POWER = 26052
    REQUIRE_LEVEL = 44
    SELL_PRICE = 217100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2172:
    PREFAB_ID = "item_prefab_2172"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2172"
    EQUIPMENT_SLOT = "Head" if 2172 % 4 == 0 else ("Chest" if 2172 % 4 == 1 else ("Weapon" if 2172 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 320
    STAT_POWER = 26064
    REQUIRE_LEVEL = 44
    SELL_PRICE = 217200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2173:
    PREFAB_ID = "item_prefab_2173"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2173"
    EQUIPMENT_SLOT = "Head" if 2173 % 4 == 0 else ("Chest" if 2173 % 4 == 1 else ("Weapon" if 2173 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 330
    STAT_POWER = 26076
    REQUIRE_LEVEL = 44
    SELL_PRICE = 217300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2174:
    PREFAB_ID = "item_prefab_2174"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2174"
    EQUIPMENT_SLOT = "Head" if 2174 % 4 == 0 else ("Chest" if 2174 % 4 == 1 else ("Weapon" if 2174 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 340
    STAT_POWER = 26088
    REQUIRE_LEVEL = 44
    SELL_PRICE = 217400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2175:
    PREFAB_ID = "item_prefab_2175"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2175"
    EQUIPMENT_SLOT = "Head" if 2175 % 4 == 0 else ("Chest" if 2175 % 4 == 1 else ("Weapon" if 2175 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 350
    STAT_POWER = 26100
    REQUIRE_LEVEL = 44
    SELL_PRICE = 217500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2176:
    PREFAB_ID = "item_prefab_2176"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2176"
    EQUIPMENT_SLOT = "Head" if 2176 % 4 == 0 else ("Chest" if 2176 % 4 == 1 else ("Weapon" if 2176 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 360
    STAT_POWER = 26112
    REQUIRE_LEVEL = 44
    SELL_PRICE = 217600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2177:
    PREFAB_ID = "item_prefab_2177"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2177"
    EQUIPMENT_SLOT = "Head" if 2177 % 4 == 0 else ("Chest" if 2177 % 4 == 1 else ("Weapon" if 2177 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 370
    STAT_POWER = 26124
    REQUIRE_LEVEL = 44
    SELL_PRICE = 217700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2178:
    PREFAB_ID = "item_prefab_2178"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2178"
    EQUIPMENT_SLOT = "Head" if 2178 % 4 == 0 else ("Chest" if 2178 % 4 == 1 else ("Weapon" if 2178 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 380
    STAT_POWER = 26136
    REQUIRE_LEVEL = 44
    SELL_PRICE = 217800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2179:
    PREFAB_ID = "item_prefab_2179"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2179"
    EQUIPMENT_SLOT = "Head" if 2179 % 4 == 0 else ("Chest" if 2179 % 4 == 1 else ("Weapon" if 2179 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 390
    STAT_POWER = 26148
    REQUIRE_LEVEL = 44
    SELL_PRICE = 217900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2180:
    PREFAB_ID = "item_prefab_2180"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2180"
    EQUIPMENT_SLOT = "Head" if 2180 % 4 == 0 else ("Chest" if 2180 % 4 == 1 else ("Weapon" if 2180 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 400
    STAT_POWER = 26160
    REQUIRE_LEVEL = 44
    SELL_PRICE = 218000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2181:
    PREFAB_ID = "item_prefab_2181"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2181"
    EQUIPMENT_SLOT = "Head" if 2181 % 4 == 0 else ("Chest" if 2181 % 4 == 1 else ("Weapon" if 2181 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 410
    STAT_POWER = 26172
    REQUIRE_LEVEL = 44
    SELL_PRICE = 218100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2182:
    PREFAB_ID = "item_prefab_2182"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2182"
    EQUIPMENT_SLOT = "Head" if 2182 % 4 == 0 else ("Chest" if 2182 % 4 == 1 else ("Weapon" if 2182 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 420
    STAT_POWER = 26184
    REQUIRE_LEVEL = 44
    SELL_PRICE = 218200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2183:
    PREFAB_ID = "item_prefab_2183"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2183"
    EQUIPMENT_SLOT = "Head" if 2183 % 4 == 0 else ("Chest" if 2183 % 4 == 1 else ("Weapon" if 2183 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 430
    STAT_POWER = 26196
    REQUIRE_LEVEL = 44
    SELL_PRICE = 218300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2184:
    PREFAB_ID = "item_prefab_2184"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2184"
    EQUIPMENT_SLOT = "Head" if 2184 % 4 == 0 else ("Chest" if 2184 % 4 == 1 else ("Weapon" if 2184 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 440
    STAT_POWER = 26208
    REQUIRE_LEVEL = 44
    SELL_PRICE = 218400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2185:
    PREFAB_ID = "item_prefab_2185"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2185"
    EQUIPMENT_SLOT = "Head" if 2185 % 4 == 0 else ("Chest" if 2185 % 4 == 1 else ("Weapon" if 2185 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 450
    STAT_POWER = 26220
    REQUIRE_LEVEL = 44
    SELL_PRICE = 218500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2186:
    PREFAB_ID = "item_prefab_2186"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2186"
    EQUIPMENT_SLOT = "Head" if 2186 % 4 == 0 else ("Chest" if 2186 % 4 == 1 else ("Weapon" if 2186 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 460
    STAT_POWER = 26232
    REQUIRE_LEVEL = 44
    SELL_PRICE = 218600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2187:
    PREFAB_ID = "item_prefab_2187"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2187"
    EQUIPMENT_SLOT = "Head" if 2187 % 4 == 0 else ("Chest" if 2187 % 4 == 1 else ("Weapon" if 2187 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 470
    STAT_POWER = 26244
    REQUIRE_LEVEL = 44
    SELL_PRICE = 218700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2188:
    PREFAB_ID = "item_prefab_2188"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2188"
    EQUIPMENT_SLOT = "Head" if 2188 % 4 == 0 else ("Chest" if 2188 % 4 == 1 else ("Weapon" if 2188 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 480
    STAT_POWER = 26256
    REQUIRE_LEVEL = 44
    SELL_PRICE = 218800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2189:
    PREFAB_ID = "item_prefab_2189"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2189"
    EQUIPMENT_SLOT = "Head" if 2189 % 4 == 0 else ("Chest" if 2189 % 4 == 1 else ("Weapon" if 2189 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 490
    STAT_POWER = 26268
    REQUIRE_LEVEL = 44
    SELL_PRICE = 218900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2190:
    PREFAB_ID = "item_prefab_2190"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2190"
    EQUIPMENT_SLOT = "Head" if 2190 % 4 == 0 else ("Chest" if 2190 % 4 == 1 else ("Weapon" if 2190 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 500
    STAT_POWER = 26280
    REQUIRE_LEVEL = 44
    SELL_PRICE = 219000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2191:
    PREFAB_ID = "item_prefab_2191"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2191"
    EQUIPMENT_SLOT = "Head" if 2191 % 4 == 0 else ("Chest" if 2191 % 4 == 1 else ("Weapon" if 2191 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 510
    STAT_POWER = 26292
    REQUIRE_LEVEL = 44
    SELL_PRICE = 219100

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2192:
    PREFAB_ID = "item_prefab_2192"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2192"
    EQUIPMENT_SLOT = "Head" if 2192 % 4 == 0 else ("Chest" if 2192 % 4 == 1 else ("Weapon" if 2192 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 520
    STAT_POWER = 26304
    REQUIRE_LEVEL = 44
    SELL_PRICE = 219200

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2193:
    PREFAB_ID = "item_prefab_2193"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2193"
    EQUIPMENT_SLOT = "Head" if 2193 % 4 == 0 else ("Chest" if 2193 % 4 == 1 else ("Weapon" if 2193 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 530
    STAT_POWER = 26316
    REQUIRE_LEVEL = 44
    SELL_PRICE = 219300

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2194:
    PREFAB_ID = "item_prefab_2194"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2194"
    EQUIPMENT_SLOT = "Head" if 2194 % 4 == 0 else ("Chest" if 2194 % 4 == 1 else ("Weapon" if 2194 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 540
    STAT_POWER = 26328
    REQUIRE_LEVEL = 44
    SELL_PRICE = 219400

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2195:
    PREFAB_ID = "item_prefab_2195"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2195"
    EQUIPMENT_SLOT = "Head" if 2195 % 4 == 0 else ("Chest" if 2195 % 4 == 1 else ("Weapon" if 2195 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 550
    STAT_POWER = 26340
    REQUIRE_LEVEL = 44
    SELL_PRICE = 219500

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2196:
    PREFAB_ID = "item_prefab_2196"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2196"
    EQUIPMENT_SLOT = "Head" if 2196 % 4 == 0 else ("Chest" if 2196 % 4 == 1 else ("Weapon" if 2196 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 560
    STAT_POWER = 26352
    REQUIRE_LEVEL = 44
    SELL_PRICE = 219600

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2197:
    PREFAB_ID = "item_prefab_2197"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2197"
    EQUIPMENT_SLOT = "Head" if 2197 % 4 == 0 else ("Chest" if 2197 % 4 == 1 else ("Weapon" if 2197 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 570
    STAT_POWER = 26364
    REQUIRE_LEVEL = 44
    SELL_PRICE = 219700

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2198:
    PREFAB_ID = "item_prefab_2198"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2198"
    EQUIPMENT_SLOT = "Head" if 2198 % 4 == 0 else ("Chest" if 2198 % 4 == 1 else ("Weapon" if 2198 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 580
    STAT_POWER = 26376
    REQUIRE_LEVEL = 44
    SELL_PRICE = 219800

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2199:
    PREFAB_ID = "item_prefab_2199"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2199"
    EQUIPMENT_SLOT = "Head" if 2199 % 4 == 0 else ("Chest" if 2199 % 4 == 1 else ("Weapon" if 2199 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 590
    STAT_POWER = 26388
    REQUIRE_LEVEL = 44
    SELL_PRICE = 219900

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }


class ExpandedItemPrefab_2200:
    PREFAB_ID = "item_prefab_2200"
    DISPLAY_NAME = "Hyperion Mythic Artifact Grade #2200"
    EQUIPMENT_SLOT = "Head" if 2200 % 4 == 0 else ("Chest" if 2200 % 4 == 1 else ("Weapon" if 2200 % 4 == 2 else "Ring"))
    DURABILITY_MAX = 100
    STAT_POWER = 26400
    REQUIRE_LEVEL = 45
    SELL_PRICE = 220000

    @classmethod
    def create_instance_dict(cls):
        return {
            "id": cls.PREFAB_ID,
            "name": cls.DISPLAY_NAME,
            "slot": cls.EQUIPMENT_SLOT,
            "durability": cls.DURABILITY_MAX,
            "power": cls.STAT_POWER,
            "req_level": cls.REQUIRE_LEVEL,
            "price": cls.SELL_PRICE
        }
