"""
World Engine - Procedural Map Templates & Tile Data Registry
Contains tile registries, biome map configurations, and level layout blueprints.
"""


class TileBlueprint_1:
    TILE_ID = 1
    NAME = "Biome Tile Pattern #1"
    WALKABLE = True if 1 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.01, 0.02)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_1.TILE_ID, "walkable": TileBlueprint_1.WALKABLE, "cost": TileBlueprint_1.MOVEMENT_COST}


class TileBlueprint_2:
    TILE_ID = 2
    NAME = "Biome Tile Pattern #2"
    WALKABLE = True if 2 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.02, 0.04)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_2.TILE_ID, "walkable": TileBlueprint_2.WALKABLE, "cost": TileBlueprint_2.MOVEMENT_COST}


class TileBlueprint_3:
    TILE_ID = 3
    NAME = "Biome Tile Pattern #3"
    WALKABLE = True if 3 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.03, 0.06)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_3.TILE_ID, "walkable": TileBlueprint_3.WALKABLE, "cost": TileBlueprint_3.MOVEMENT_COST}


class TileBlueprint_4:
    TILE_ID = 4
    NAME = "Biome Tile Pattern #4"
    WALKABLE = True if 4 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.04, 0.08)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_4.TILE_ID, "walkable": TileBlueprint_4.WALKABLE, "cost": TileBlueprint_4.MOVEMENT_COST}


class TileBlueprint_5:
    TILE_ID = 5
    NAME = "Biome Tile Pattern #5"
    WALKABLE = True if 5 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.05, 0.1)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_5.TILE_ID, "walkable": TileBlueprint_5.WALKABLE, "cost": TileBlueprint_5.MOVEMENT_COST}


class TileBlueprint_6:
    TILE_ID = 6
    NAME = "Biome Tile Pattern #6"
    WALKABLE = True if 6 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.06, 0.12)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_6.TILE_ID, "walkable": TileBlueprint_6.WALKABLE, "cost": TileBlueprint_6.MOVEMENT_COST}


class TileBlueprint_7:
    TILE_ID = 7
    NAME = "Biome Tile Pattern #7"
    WALKABLE = True if 7 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.07, 0.14)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_7.TILE_ID, "walkable": TileBlueprint_7.WALKABLE, "cost": TileBlueprint_7.MOVEMENT_COST}


class TileBlueprint_8:
    TILE_ID = 8
    NAME = "Biome Tile Pattern #8"
    WALKABLE = True if 8 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.08, 0.16)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_8.TILE_ID, "walkable": TileBlueprint_8.WALKABLE, "cost": TileBlueprint_8.MOVEMENT_COST}


class TileBlueprint_9:
    TILE_ID = 9
    NAME = "Biome Tile Pattern #9"
    WALKABLE = True if 9 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.09, 0.18)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_9.TILE_ID, "walkable": TileBlueprint_9.WALKABLE, "cost": TileBlueprint_9.MOVEMENT_COST}


class TileBlueprint_10:
    TILE_ID = 10
    NAME = "Biome Tile Pattern #10"
    WALKABLE = True if 10 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.1, 0.2)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_10.TILE_ID, "walkable": TileBlueprint_10.WALKABLE, "cost": TileBlueprint_10.MOVEMENT_COST}


class TileBlueprint_11:
    TILE_ID = 11
    NAME = "Biome Tile Pattern #11"
    WALKABLE = True if 11 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.11, 0.22)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_11.TILE_ID, "walkable": TileBlueprint_11.WALKABLE, "cost": TileBlueprint_11.MOVEMENT_COST}


class TileBlueprint_12:
    TILE_ID = 12
    NAME = "Biome Tile Pattern #12"
    WALKABLE = True if 12 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.12, 0.24)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_12.TILE_ID, "walkable": TileBlueprint_12.WALKABLE, "cost": TileBlueprint_12.MOVEMENT_COST}


class TileBlueprint_13:
    TILE_ID = 13
    NAME = "Biome Tile Pattern #13"
    WALKABLE = True if 13 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.13, 0.26)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_13.TILE_ID, "walkable": TileBlueprint_13.WALKABLE, "cost": TileBlueprint_13.MOVEMENT_COST}


class TileBlueprint_14:
    TILE_ID = 14
    NAME = "Biome Tile Pattern #14"
    WALKABLE = True if 14 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.14, 0.28)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_14.TILE_ID, "walkable": TileBlueprint_14.WALKABLE, "cost": TileBlueprint_14.MOVEMENT_COST}


class TileBlueprint_15:
    TILE_ID = 15
    NAME = "Biome Tile Pattern #15"
    WALKABLE = True if 15 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.15, 0.3)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_15.TILE_ID, "walkable": TileBlueprint_15.WALKABLE, "cost": TileBlueprint_15.MOVEMENT_COST}


class TileBlueprint_16:
    TILE_ID = 16
    NAME = "Biome Tile Pattern #16"
    WALKABLE = True if 16 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.16, 0.32)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_16.TILE_ID, "walkable": TileBlueprint_16.WALKABLE, "cost": TileBlueprint_16.MOVEMENT_COST}


class TileBlueprint_17:
    TILE_ID = 17
    NAME = "Biome Tile Pattern #17"
    WALKABLE = True if 17 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.17, 0.34)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_17.TILE_ID, "walkable": TileBlueprint_17.WALKABLE, "cost": TileBlueprint_17.MOVEMENT_COST}


class TileBlueprint_18:
    TILE_ID = 18
    NAME = "Biome Tile Pattern #18"
    WALKABLE = True if 18 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.18, 0.36)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_18.TILE_ID, "walkable": TileBlueprint_18.WALKABLE, "cost": TileBlueprint_18.MOVEMENT_COST}


class TileBlueprint_19:
    TILE_ID = 19
    NAME = "Biome Tile Pattern #19"
    WALKABLE = True if 19 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.19, 0.38)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_19.TILE_ID, "walkable": TileBlueprint_19.WALKABLE, "cost": TileBlueprint_19.MOVEMENT_COST}


class TileBlueprint_20:
    TILE_ID = 20
    NAME = "Biome Tile Pattern #20"
    WALKABLE = True if 20 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.2, 0.4)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_20.TILE_ID, "walkable": TileBlueprint_20.WALKABLE, "cost": TileBlueprint_20.MOVEMENT_COST}


class TileBlueprint_21:
    TILE_ID = 21
    NAME = "Biome Tile Pattern #21"
    WALKABLE = True if 21 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.21, 0.42)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_21.TILE_ID, "walkable": TileBlueprint_21.WALKABLE, "cost": TileBlueprint_21.MOVEMENT_COST}


class TileBlueprint_22:
    TILE_ID = 22
    NAME = "Biome Tile Pattern #22"
    WALKABLE = True if 22 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.22, 0.44)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_22.TILE_ID, "walkable": TileBlueprint_22.WALKABLE, "cost": TileBlueprint_22.MOVEMENT_COST}


class TileBlueprint_23:
    TILE_ID = 23
    NAME = "Biome Tile Pattern #23"
    WALKABLE = True if 23 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.23, 0.46)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_23.TILE_ID, "walkable": TileBlueprint_23.WALKABLE, "cost": TileBlueprint_23.MOVEMENT_COST}


class TileBlueprint_24:
    TILE_ID = 24
    NAME = "Biome Tile Pattern #24"
    WALKABLE = True if 24 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.24, 0.48)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_24.TILE_ID, "walkable": TileBlueprint_24.WALKABLE, "cost": TileBlueprint_24.MOVEMENT_COST}


class TileBlueprint_25:
    TILE_ID = 25
    NAME = "Biome Tile Pattern #25"
    WALKABLE = True if 25 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.25, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_25.TILE_ID, "walkable": TileBlueprint_25.WALKABLE, "cost": TileBlueprint_25.MOVEMENT_COST}


class TileBlueprint_26:
    TILE_ID = 26
    NAME = "Biome Tile Pattern #26"
    WALKABLE = True if 26 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.26, 0.52)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_26.TILE_ID, "walkable": TileBlueprint_26.WALKABLE, "cost": TileBlueprint_26.MOVEMENT_COST}


class TileBlueprint_27:
    TILE_ID = 27
    NAME = "Biome Tile Pattern #27"
    WALKABLE = True if 27 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.27, 0.54)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_27.TILE_ID, "walkable": TileBlueprint_27.WALKABLE, "cost": TileBlueprint_27.MOVEMENT_COST}


class TileBlueprint_28:
    TILE_ID = 28
    NAME = "Biome Tile Pattern #28"
    WALKABLE = True if 28 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.28, 0.56)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_28.TILE_ID, "walkable": TileBlueprint_28.WALKABLE, "cost": TileBlueprint_28.MOVEMENT_COST}


class TileBlueprint_29:
    TILE_ID = 29
    NAME = "Biome Tile Pattern #29"
    WALKABLE = True if 29 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.29, 0.58)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_29.TILE_ID, "walkable": TileBlueprint_29.WALKABLE, "cost": TileBlueprint_29.MOVEMENT_COST}


class TileBlueprint_30:
    TILE_ID = 30
    NAME = "Biome Tile Pattern #30"
    WALKABLE = True if 30 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.3, 0.6)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_30.TILE_ID, "walkable": TileBlueprint_30.WALKABLE, "cost": TileBlueprint_30.MOVEMENT_COST}


class TileBlueprint_31:
    TILE_ID = 31
    NAME = "Biome Tile Pattern #31"
    WALKABLE = True if 31 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.31, 0.62)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_31.TILE_ID, "walkable": TileBlueprint_31.WALKABLE, "cost": TileBlueprint_31.MOVEMENT_COST}


class TileBlueprint_32:
    TILE_ID = 32
    NAME = "Biome Tile Pattern #32"
    WALKABLE = True if 32 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.32, 0.64)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_32.TILE_ID, "walkable": TileBlueprint_32.WALKABLE, "cost": TileBlueprint_32.MOVEMENT_COST}


class TileBlueprint_33:
    TILE_ID = 33
    NAME = "Biome Tile Pattern #33"
    WALKABLE = True if 33 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.33, 0.66)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_33.TILE_ID, "walkable": TileBlueprint_33.WALKABLE, "cost": TileBlueprint_33.MOVEMENT_COST}


class TileBlueprint_34:
    TILE_ID = 34
    NAME = "Biome Tile Pattern #34"
    WALKABLE = True if 34 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.34, 0.68)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_34.TILE_ID, "walkable": TileBlueprint_34.WALKABLE, "cost": TileBlueprint_34.MOVEMENT_COST}


class TileBlueprint_35:
    TILE_ID = 35
    NAME = "Biome Tile Pattern #35"
    WALKABLE = True if 35 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.35000000000000003, 0.7000000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_35.TILE_ID, "walkable": TileBlueprint_35.WALKABLE, "cost": TileBlueprint_35.MOVEMENT_COST}


class TileBlueprint_36:
    TILE_ID = 36
    NAME = "Biome Tile Pattern #36"
    WALKABLE = True if 36 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.36, 0.72)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_36.TILE_ID, "walkable": TileBlueprint_36.WALKABLE, "cost": TileBlueprint_36.MOVEMENT_COST}


class TileBlueprint_37:
    TILE_ID = 37
    NAME = "Biome Tile Pattern #37"
    WALKABLE = True if 37 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.37, 0.74)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_37.TILE_ID, "walkable": TileBlueprint_37.WALKABLE, "cost": TileBlueprint_37.MOVEMENT_COST}


class TileBlueprint_38:
    TILE_ID = 38
    NAME = "Biome Tile Pattern #38"
    WALKABLE = True if 38 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.38, 0.76)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_38.TILE_ID, "walkable": TileBlueprint_38.WALKABLE, "cost": TileBlueprint_38.MOVEMENT_COST}


class TileBlueprint_39:
    TILE_ID = 39
    NAME = "Biome Tile Pattern #39"
    WALKABLE = True if 39 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.39, 0.78)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_39.TILE_ID, "walkable": TileBlueprint_39.WALKABLE, "cost": TileBlueprint_39.MOVEMENT_COST}


class TileBlueprint_40:
    TILE_ID = 40
    NAME = "Biome Tile Pattern #40"
    WALKABLE = True if 40 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.4, 0.8)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_40.TILE_ID, "walkable": TileBlueprint_40.WALKABLE, "cost": TileBlueprint_40.MOVEMENT_COST}


class TileBlueprint_41:
    TILE_ID = 41
    NAME = "Biome Tile Pattern #41"
    WALKABLE = True if 41 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.41000000000000003, 0.8200000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_41.TILE_ID, "walkable": TileBlueprint_41.WALKABLE, "cost": TileBlueprint_41.MOVEMENT_COST}


class TileBlueprint_42:
    TILE_ID = 42
    NAME = "Biome Tile Pattern #42"
    WALKABLE = True if 42 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.42, 0.84)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_42.TILE_ID, "walkable": TileBlueprint_42.WALKABLE, "cost": TileBlueprint_42.MOVEMENT_COST}


class TileBlueprint_43:
    TILE_ID = 43
    NAME = "Biome Tile Pattern #43"
    WALKABLE = True if 43 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.43, 0.86)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_43.TILE_ID, "walkable": TileBlueprint_43.WALKABLE, "cost": TileBlueprint_43.MOVEMENT_COST}


class TileBlueprint_44:
    TILE_ID = 44
    NAME = "Biome Tile Pattern #44"
    WALKABLE = True if 44 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.44, 0.88)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_44.TILE_ID, "walkable": TileBlueprint_44.WALKABLE, "cost": TileBlueprint_44.MOVEMENT_COST}


class TileBlueprint_45:
    TILE_ID = 45
    NAME = "Biome Tile Pattern #45"
    WALKABLE = True if 45 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.45, 0.9)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_45.TILE_ID, "walkable": TileBlueprint_45.WALKABLE, "cost": TileBlueprint_45.MOVEMENT_COST}


class TileBlueprint_46:
    TILE_ID = 46
    NAME = "Biome Tile Pattern #46"
    WALKABLE = True if 46 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.46, 0.92)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_46.TILE_ID, "walkable": TileBlueprint_46.WALKABLE, "cost": TileBlueprint_46.MOVEMENT_COST}


class TileBlueprint_47:
    TILE_ID = 47
    NAME = "Biome Tile Pattern #47"
    WALKABLE = True if 47 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.47000000000000003, 0.9400000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_47.TILE_ID, "walkable": TileBlueprint_47.WALKABLE, "cost": TileBlueprint_47.MOVEMENT_COST}


class TileBlueprint_48:
    TILE_ID = 48
    NAME = "Biome Tile Pattern #48"
    WALKABLE = True if 48 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.48, 0.96)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_48.TILE_ID, "walkable": TileBlueprint_48.WALKABLE, "cost": TileBlueprint_48.MOVEMENT_COST}


class TileBlueprint_49:
    TILE_ID = 49
    NAME = "Biome Tile Pattern #49"
    WALKABLE = True if 49 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.49, 0.98)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_49.TILE_ID, "walkable": TileBlueprint_49.WALKABLE, "cost": TileBlueprint_49.MOVEMENT_COST}


class TileBlueprint_50:
    TILE_ID = 50
    NAME = "Biome Tile Pattern #50"
    WALKABLE = True if 50 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.5, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_50.TILE_ID, "walkable": TileBlueprint_50.WALKABLE, "cost": TileBlueprint_50.MOVEMENT_COST}


class TileBlueprint_51:
    TILE_ID = 51
    NAME = "Biome Tile Pattern #51"
    WALKABLE = True if 51 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.51, 0.020000000000000018)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_51.TILE_ID, "walkable": TileBlueprint_51.WALKABLE, "cost": TileBlueprint_51.MOVEMENT_COST}


class TileBlueprint_52:
    TILE_ID = 52
    NAME = "Biome Tile Pattern #52"
    WALKABLE = True if 52 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.52, 0.040000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_52.TILE_ID, "walkable": TileBlueprint_52.WALKABLE, "cost": TileBlueprint_52.MOVEMENT_COST}


class TileBlueprint_53:
    TILE_ID = 53
    NAME = "Biome Tile Pattern #53"
    WALKABLE = True if 53 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.53, 0.06000000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_53.TILE_ID, "walkable": TileBlueprint_53.WALKABLE, "cost": TileBlueprint_53.MOVEMENT_COST}


class TileBlueprint_54:
    TILE_ID = 54
    NAME = "Biome Tile Pattern #54"
    WALKABLE = True if 54 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.54, 0.08000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_54.TILE_ID, "walkable": TileBlueprint_54.WALKABLE, "cost": TileBlueprint_54.MOVEMENT_COST}


class TileBlueprint_55:
    TILE_ID = 55
    NAME = "Biome Tile Pattern #55"
    WALKABLE = True if 55 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.55, 0.10000000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_55.TILE_ID, "walkable": TileBlueprint_55.WALKABLE, "cost": TileBlueprint_55.MOVEMENT_COST}


class TileBlueprint_56:
    TILE_ID = 56
    NAME = "Biome Tile Pattern #56"
    WALKABLE = True if 56 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.56, 0.1200000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_56.TILE_ID, "walkable": TileBlueprint_56.WALKABLE, "cost": TileBlueprint_56.MOVEMENT_COST}


class TileBlueprint_57:
    TILE_ID = 57
    NAME = "Biome Tile Pattern #57"
    WALKABLE = True if 57 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.5700000000000001, 0.14000000000000012)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_57.TILE_ID, "walkable": TileBlueprint_57.WALKABLE, "cost": TileBlueprint_57.MOVEMENT_COST}


class TileBlueprint_58:
    TILE_ID = 58
    NAME = "Biome Tile Pattern #58"
    WALKABLE = True if 58 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.58, 0.15999999999999992)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_58.TILE_ID, "walkable": TileBlueprint_58.WALKABLE, "cost": TileBlueprint_58.MOVEMENT_COST}


class TileBlueprint_59:
    TILE_ID = 59
    NAME = "Biome Tile Pattern #59"
    WALKABLE = True if 59 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.59, 0.17999999999999994)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_59.TILE_ID, "walkable": TileBlueprint_59.WALKABLE, "cost": TileBlueprint_59.MOVEMENT_COST}


class TileBlueprint_60:
    TILE_ID = 60
    NAME = "Biome Tile Pattern #60"
    WALKABLE = True if 60 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.6, 0.19999999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_60.TILE_ID, "walkable": TileBlueprint_60.WALKABLE, "cost": TileBlueprint_60.MOVEMENT_COST}


class TileBlueprint_61:
    TILE_ID = 61
    NAME = "Biome Tile Pattern #61"
    WALKABLE = True if 61 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.61, 0.21999999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_61.TILE_ID, "walkable": TileBlueprint_61.WALKABLE, "cost": TileBlueprint_61.MOVEMENT_COST}


class TileBlueprint_62:
    TILE_ID = 62
    NAME = "Biome Tile Pattern #62"
    WALKABLE = True if 62 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.62, 0.24)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_62.TILE_ID, "walkable": TileBlueprint_62.WALKABLE, "cost": TileBlueprint_62.MOVEMENT_COST}


class TileBlueprint_63:
    TILE_ID = 63
    NAME = "Biome Tile Pattern #63"
    WALKABLE = True if 63 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.63, 0.26)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_63.TILE_ID, "walkable": TileBlueprint_63.WALKABLE, "cost": TileBlueprint_63.MOVEMENT_COST}


class TileBlueprint_64:
    TILE_ID = 64
    NAME = "Biome Tile Pattern #64"
    WALKABLE = True if 64 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.64, 0.28)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_64.TILE_ID, "walkable": TileBlueprint_64.WALKABLE, "cost": TileBlueprint_64.MOVEMENT_COST}


class TileBlueprint_65:
    TILE_ID = 65
    NAME = "Biome Tile Pattern #65"
    WALKABLE = True if 65 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.65, 0.30000000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_65.TILE_ID, "walkable": TileBlueprint_65.WALKABLE, "cost": TileBlueprint_65.MOVEMENT_COST}


class TileBlueprint_66:
    TILE_ID = 66
    NAME = "Biome Tile Pattern #66"
    WALKABLE = True if 66 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.66, 0.32000000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_66.TILE_ID, "walkable": TileBlueprint_66.WALKABLE, "cost": TileBlueprint_66.MOVEMENT_COST}


class TileBlueprint_67:
    TILE_ID = 67
    NAME = "Biome Tile Pattern #67"
    WALKABLE = True if 67 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.67, 0.3400000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_67.TILE_ID, "walkable": TileBlueprint_67.WALKABLE, "cost": TileBlueprint_67.MOVEMENT_COST}


class TileBlueprint_68:
    TILE_ID = 68
    NAME = "Biome Tile Pattern #68"
    WALKABLE = True if 68 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.68, 0.3600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_68.TILE_ID, "walkable": TileBlueprint_68.WALKABLE, "cost": TileBlueprint_68.MOVEMENT_COST}


class TileBlueprint_69:
    TILE_ID = 69
    NAME = "Biome Tile Pattern #69"
    WALKABLE = True if 69 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.6900000000000001, 0.3800000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_69.TILE_ID, "walkable": TileBlueprint_69.WALKABLE, "cost": TileBlueprint_69.MOVEMENT_COST}


class TileBlueprint_70:
    TILE_ID = 70
    NAME = "Biome Tile Pattern #70"
    WALKABLE = True if 70 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.7000000000000001, 0.40000000000000013)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_70.TILE_ID, "walkable": TileBlueprint_70.WALKABLE, "cost": TileBlueprint_70.MOVEMENT_COST}


class TileBlueprint_71:
    TILE_ID = 71
    NAME = "Biome Tile Pattern #71"
    WALKABLE = True if 71 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.71, 0.41999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_71.TILE_ID, "walkable": TileBlueprint_71.WALKABLE, "cost": TileBlueprint_71.MOVEMENT_COST}


class TileBlueprint_72:
    TILE_ID = 72
    NAME = "Biome Tile Pattern #72"
    WALKABLE = True if 72 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.72, 0.43999999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_72.TILE_ID, "walkable": TileBlueprint_72.WALKABLE, "cost": TileBlueprint_72.MOVEMENT_COST}


class TileBlueprint_73:
    TILE_ID = 73
    NAME = "Biome Tile Pattern #73"
    WALKABLE = True if 73 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.73, 0.45999999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_73.TILE_ID, "walkable": TileBlueprint_73.WALKABLE, "cost": TileBlueprint_73.MOVEMENT_COST}


class TileBlueprint_74:
    TILE_ID = 74
    NAME = "Biome Tile Pattern #74"
    WALKABLE = True if 74 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.74, 0.48)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_74.TILE_ID, "walkable": TileBlueprint_74.WALKABLE, "cost": TileBlueprint_74.MOVEMENT_COST}


class TileBlueprint_75:
    TILE_ID = 75
    NAME = "Biome Tile Pattern #75"
    WALKABLE = True if 75 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.75, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_75.TILE_ID, "walkable": TileBlueprint_75.WALKABLE, "cost": TileBlueprint_75.MOVEMENT_COST}


class TileBlueprint_76:
    TILE_ID = 76
    NAME = "Biome Tile Pattern #76"
    WALKABLE = True if 76 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.76, 0.52)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_76.TILE_ID, "walkable": TileBlueprint_76.WALKABLE, "cost": TileBlueprint_76.MOVEMENT_COST}


class TileBlueprint_77:
    TILE_ID = 77
    NAME = "Biome Tile Pattern #77"
    WALKABLE = True if 77 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.77, 0.54)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_77.TILE_ID, "walkable": TileBlueprint_77.WALKABLE, "cost": TileBlueprint_77.MOVEMENT_COST}


class TileBlueprint_78:
    TILE_ID = 78
    NAME = "Biome Tile Pattern #78"
    WALKABLE = True if 78 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.78, 0.56)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_78.TILE_ID, "walkable": TileBlueprint_78.WALKABLE, "cost": TileBlueprint_78.MOVEMENT_COST}


class TileBlueprint_79:
    TILE_ID = 79
    NAME = "Biome Tile Pattern #79"
    WALKABLE = True if 79 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.79, 0.5800000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_79.TILE_ID, "walkable": TileBlueprint_79.WALKABLE, "cost": TileBlueprint_79.MOVEMENT_COST}


class TileBlueprint_80:
    TILE_ID = 80
    NAME = "Biome Tile Pattern #80"
    WALKABLE = True if 80 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.8, 0.6000000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_80.TILE_ID, "walkable": TileBlueprint_80.WALKABLE, "cost": TileBlueprint_80.MOVEMENT_COST}


class TileBlueprint_81:
    TILE_ID = 81
    NAME = "Biome Tile Pattern #81"
    WALKABLE = True if 81 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.81, 0.6200000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_81.TILE_ID, "walkable": TileBlueprint_81.WALKABLE, "cost": TileBlueprint_81.MOVEMENT_COST}


class TileBlueprint_82:
    TILE_ID = 82
    NAME = "Biome Tile Pattern #82"
    WALKABLE = True if 82 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.8200000000000001, 0.6400000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_82.TILE_ID, "walkable": TileBlueprint_82.WALKABLE, "cost": TileBlueprint_82.MOVEMENT_COST}


class TileBlueprint_83:
    TILE_ID = 83
    NAME = "Biome Tile Pattern #83"
    WALKABLE = True if 83 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.8300000000000001, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_83.TILE_ID, "walkable": TileBlueprint_83.WALKABLE, "cost": TileBlueprint_83.MOVEMENT_COST}


class TileBlueprint_84:
    TILE_ID = 84
    NAME = "Biome Tile Pattern #84"
    WALKABLE = True if 84 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.84, 0.6799999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_84.TILE_ID, "walkable": TileBlueprint_84.WALKABLE, "cost": TileBlueprint_84.MOVEMENT_COST}


class TileBlueprint_85:
    TILE_ID = 85
    NAME = "Biome Tile Pattern #85"
    WALKABLE = True if 85 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.85, 0.7)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_85.TILE_ID, "walkable": TileBlueprint_85.WALKABLE, "cost": TileBlueprint_85.MOVEMENT_COST}


class TileBlueprint_86:
    TILE_ID = 86
    NAME = "Biome Tile Pattern #86"
    WALKABLE = True if 86 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.86, 0.72)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_86.TILE_ID, "walkable": TileBlueprint_86.WALKABLE, "cost": TileBlueprint_86.MOVEMENT_COST}


class TileBlueprint_87:
    TILE_ID = 87
    NAME = "Biome Tile Pattern #87"
    WALKABLE = True if 87 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.87, 0.74)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_87.TILE_ID, "walkable": TileBlueprint_87.WALKABLE, "cost": TileBlueprint_87.MOVEMENT_COST}


class TileBlueprint_88:
    TILE_ID = 88
    NAME = "Biome Tile Pattern #88"
    WALKABLE = True if 88 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.88, 0.76)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_88.TILE_ID, "walkable": TileBlueprint_88.WALKABLE, "cost": TileBlueprint_88.MOVEMENT_COST}


class TileBlueprint_89:
    TILE_ID = 89
    NAME = "Biome Tile Pattern #89"
    WALKABLE = True if 89 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.89, 0.78)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_89.TILE_ID, "walkable": TileBlueprint_89.WALKABLE, "cost": TileBlueprint_89.MOVEMENT_COST}


class TileBlueprint_90:
    TILE_ID = 90
    NAME = "Biome Tile Pattern #90"
    WALKABLE = True if 90 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.9, 0.8)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_90.TILE_ID, "walkable": TileBlueprint_90.WALKABLE, "cost": TileBlueprint_90.MOVEMENT_COST}


class TileBlueprint_91:
    TILE_ID = 91
    NAME = "Biome Tile Pattern #91"
    WALKABLE = True if 91 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.91, 0.8200000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_91.TILE_ID, "walkable": TileBlueprint_91.WALKABLE, "cost": TileBlueprint_91.MOVEMENT_COST}


class TileBlueprint_92:
    TILE_ID = 92
    NAME = "Biome Tile Pattern #92"
    WALKABLE = True if 92 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.92, 0.8400000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_92.TILE_ID, "walkable": TileBlueprint_92.WALKABLE, "cost": TileBlueprint_92.MOVEMENT_COST}


class TileBlueprint_93:
    TILE_ID = 93
    NAME = "Biome Tile Pattern #93"
    WALKABLE = True if 93 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.93, 0.8600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_93.TILE_ID, "walkable": TileBlueprint_93.WALKABLE, "cost": TileBlueprint_93.MOVEMENT_COST}


class TileBlueprint_94:
    TILE_ID = 94
    NAME = "Biome Tile Pattern #94"
    WALKABLE = True if 94 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.9400000000000001, 0.8800000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_94.TILE_ID, "walkable": TileBlueprint_94.WALKABLE, "cost": TileBlueprint_94.MOVEMENT_COST}


class TileBlueprint_95:
    TILE_ID = 95
    NAME = "Biome Tile Pattern #95"
    WALKABLE = True if 95 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (0.9500000000000001, 0.9000000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_95.TILE_ID, "walkable": TileBlueprint_95.WALKABLE, "cost": TileBlueprint_95.MOVEMENT_COST}


class TileBlueprint_96:
    TILE_ID = 96
    NAME = "Biome Tile Pattern #96"
    WALKABLE = True if 96 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (0.96, 0.9199999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_96.TILE_ID, "walkable": TileBlueprint_96.WALKABLE, "cost": TileBlueprint_96.MOVEMENT_COST}


class TileBlueprint_97:
    TILE_ID = 97
    NAME = "Biome Tile Pattern #97"
    WALKABLE = True if 97 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (0.97, 0.94)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_97.TILE_ID, "walkable": TileBlueprint_97.WALKABLE, "cost": TileBlueprint_97.MOVEMENT_COST}


class TileBlueprint_98:
    TILE_ID = 98
    NAME = "Biome Tile Pattern #98"
    WALKABLE = True if 98 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (0.98, 0.96)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_98.TILE_ID, "walkable": TileBlueprint_98.WALKABLE, "cost": TileBlueprint_98.MOVEMENT_COST}


class TileBlueprint_99:
    TILE_ID = 99
    NAME = "Biome Tile Pattern #99"
    WALKABLE = True if 99 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (0.99, 0.98)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_99.TILE_ID, "walkable": TileBlueprint_99.WALKABLE, "cost": TileBlueprint_99.MOVEMENT_COST}


class TileBlueprint_100:
    TILE_ID = 100
    NAME = "Biome Tile Pattern #100"
    WALKABLE = True if 100 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.0, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_100.TILE_ID, "walkable": TileBlueprint_100.WALKABLE, "cost": TileBlueprint_100.MOVEMENT_COST}


class TileBlueprint_101:
    TILE_ID = 101
    NAME = "Biome Tile Pattern #101"
    WALKABLE = True if 101 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.01, 0.020000000000000018)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_101.TILE_ID, "walkable": TileBlueprint_101.WALKABLE, "cost": TileBlueprint_101.MOVEMENT_COST}


class TileBlueprint_102:
    TILE_ID = 102
    NAME = "Biome Tile Pattern #102"
    WALKABLE = True if 102 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.02, 0.040000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_102.TILE_ID, "walkable": TileBlueprint_102.WALKABLE, "cost": TileBlueprint_102.MOVEMENT_COST}


class TileBlueprint_103:
    TILE_ID = 103
    NAME = "Biome Tile Pattern #103"
    WALKABLE = True if 103 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.03, 0.06000000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_103.TILE_ID, "walkable": TileBlueprint_103.WALKABLE, "cost": TileBlueprint_103.MOVEMENT_COST}


class TileBlueprint_104:
    TILE_ID = 104
    NAME = "Biome Tile Pattern #104"
    WALKABLE = True if 104 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.04, 0.08000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_104.TILE_ID, "walkable": TileBlueprint_104.WALKABLE, "cost": TileBlueprint_104.MOVEMENT_COST}


class TileBlueprint_105:
    TILE_ID = 105
    NAME = "Biome Tile Pattern #105"
    WALKABLE = True if 105 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.05, 0.10000000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_105.TILE_ID, "walkable": TileBlueprint_105.WALKABLE, "cost": TileBlueprint_105.MOVEMENT_COST}


class TileBlueprint_106:
    TILE_ID = 106
    NAME = "Biome Tile Pattern #106"
    WALKABLE = True if 106 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.06, 0.1200000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_106.TILE_ID, "walkable": TileBlueprint_106.WALKABLE, "cost": TileBlueprint_106.MOVEMENT_COST}


class TileBlueprint_107:
    TILE_ID = 107
    NAME = "Biome Tile Pattern #107"
    WALKABLE = True if 107 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.07, 0.14000000000000012)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_107.TILE_ID, "walkable": TileBlueprint_107.WALKABLE, "cost": TileBlueprint_107.MOVEMENT_COST}


class TileBlueprint_108:
    TILE_ID = 108
    NAME = "Biome Tile Pattern #108"
    WALKABLE = True if 108 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.08, 0.16000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_108.TILE_ID, "walkable": TileBlueprint_108.WALKABLE, "cost": TileBlueprint_108.MOVEMENT_COST}


class TileBlueprint_109:
    TILE_ID = 109
    NAME = "Biome Tile Pattern #109"
    WALKABLE = True if 109 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.09, 0.18000000000000016)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_109.TILE_ID, "walkable": TileBlueprint_109.WALKABLE, "cost": TileBlueprint_109.MOVEMENT_COST}


class TileBlueprint_110:
    TILE_ID = 110
    NAME = "Biome Tile Pattern #110"
    WALKABLE = True if 110 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.1, 0.20000000000000018)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_110.TILE_ID, "walkable": TileBlueprint_110.WALKABLE, "cost": TileBlueprint_110.MOVEMENT_COST}


class TileBlueprint_111:
    TILE_ID = 111
    NAME = "Biome Tile Pattern #111"
    WALKABLE = True if 111 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.11, 0.2200000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_111.TILE_ID, "walkable": TileBlueprint_111.WALKABLE, "cost": TileBlueprint_111.MOVEMENT_COST}


class TileBlueprint_112:
    TILE_ID = 112
    NAME = "Biome Tile Pattern #112"
    WALKABLE = True if 112 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.12, 0.2400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_112.TILE_ID, "walkable": TileBlueprint_112.WALKABLE, "cost": TileBlueprint_112.MOVEMENT_COST}


class TileBlueprint_113:
    TILE_ID = 113
    NAME = "Biome Tile Pattern #113"
    WALKABLE = True if 113 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.1300000000000001, 0.26000000000000023)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_113.TILE_ID, "walkable": TileBlueprint_113.WALKABLE, "cost": TileBlueprint_113.MOVEMENT_COST}


class TileBlueprint_114:
    TILE_ID = 114
    NAME = "Biome Tile Pattern #114"
    WALKABLE = True if 114 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.1400000000000001, 0.28000000000000025)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_114.TILE_ID, "walkable": TileBlueprint_114.WALKABLE, "cost": TileBlueprint_114.MOVEMENT_COST}


class TileBlueprint_115:
    TILE_ID = 115
    NAME = "Biome Tile Pattern #115"
    WALKABLE = True if 115 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.1500000000000001, 0.30000000000000027)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_115.TILE_ID, "walkable": TileBlueprint_115.WALKABLE, "cost": TileBlueprint_115.MOVEMENT_COST}


class TileBlueprint_116:
    TILE_ID = 116
    NAME = "Biome Tile Pattern #116"
    WALKABLE = True if 116 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.16, 0.31999999999999984)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_116.TILE_ID, "walkable": TileBlueprint_116.WALKABLE, "cost": TileBlueprint_116.MOVEMENT_COST}


class TileBlueprint_117:
    TILE_ID = 117
    NAME = "Biome Tile Pattern #117"
    WALKABLE = True if 117 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.17, 0.33999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_117.TILE_ID, "walkable": TileBlueprint_117.WALKABLE, "cost": TileBlueprint_117.MOVEMENT_COST}


class TileBlueprint_118:
    TILE_ID = 118
    NAME = "Biome Tile Pattern #118"
    WALKABLE = True if 118 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.18, 0.3599999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_118.TILE_ID, "walkable": TileBlueprint_118.WALKABLE, "cost": TileBlueprint_118.MOVEMENT_COST}


class TileBlueprint_119:
    TILE_ID = 119
    NAME = "Biome Tile Pattern #119"
    WALKABLE = True if 119 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.19, 0.3799999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_119.TILE_ID, "walkable": TileBlueprint_119.WALKABLE, "cost": TileBlueprint_119.MOVEMENT_COST}


class TileBlueprint_120:
    TILE_ID = 120
    NAME = "Biome Tile Pattern #120"
    WALKABLE = True if 120 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.2, 0.3999999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_120.TILE_ID, "walkable": TileBlueprint_120.WALKABLE, "cost": TileBlueprint_120.MOVEMENT_COST}


class TileBlueprint_121:
    TILE_ID = 121
    NAME = "Biome Tile Pattern #121"
    WALKABLE = True if 121 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.21, 0.41999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_121.TILE_ID, "walkable": TileBlueprint_121.WALKABLE, "cost": TileBlueprint_121.MOVEMENT_COST}


class TileBlueprint_122:
    TILE_ID = 122
    NAME = "Biome Tile Pattern #122"
    WALKABLE = True if 122 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.22, 0.43999999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_122.TILE_ID, "walkable": TileBlueprint_122.WALKABLE, "cost": TileBlueprint_122.MOVEMENT_COST}


class TileBlueprint_123:
    TILE_ID = 123
    NAME = "Biome Tile Pattern #123"
    WALKABLE = True if 123 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.23, 0.45999999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_123.TILE_ID, "walkable": TileBlueprint_123.WALKABLE, "cost": TileBlueprint_123.MOVEMENT_COST}


class TileBlueprint_124:
    TILE_ID = 124
    NAME = "Biome Tile Pattern #124"
    WALKABLE = True if 124 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.24, 0.48)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_124.TILE_ID, "walkable": TileBlueprint_124.WALKABLE, "cost": TileBlueprint_124.MOVEMENT_COST}


class TileBlueprint_125:
    TILE_ID = 125
    NAME = "Biome Tile Pattern #125"
    WALKABLE = True if 125 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.25, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_125.TILE_ID, "walkable": TileBlueprint_125.WALKABLE, "cost": TileBlueprint_125.MOVEMENT_COST}


class TileBlueprint_126:
    TILE_ID = 126
    NAME = "Biome Tile Pattern #126"
    WALKABLE = True if 126 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.26, 0.52)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_126.TILE_ID, "walkable": TileBlueprint_126.WALKABLE, "cost": TileBlueprint_126.MOVEMENT_COST}


class TileBlueprint_127:
    TILE_ID = 127
    NAME = "Biome Tile Pattern #127"
    WALKABLE = True if 127 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.27, 0.54)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_127.TILE_ID, "walkable": TileBlueprint_127.WALKABLE, "cost": TileBlueprint_127.MOVEMENT_COST}


class TileBlueprint_128:
    TILE_ID = 128
    NAME = "Biome Tile Pattern #128"
    WALKABLE = True if 128 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.28, 0.56)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_128.TILE_ID, "walkable": TileBlueprint_128.WALKABLE, "cost": TileBlueprint_128.MOVEMENT_COST}


class TileBlueprint_129:
    TILE_ID = 129
    NAME = "Biome Tile Pattern #129"
    WALKABLE = True if 129 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.29, 0.5800000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_129.TILE_ID, "walkable": TileBlueprint_129.WALKABLE, "cost": TileBlueprint_129.MOVEMENT_COST}


class TileBlueprint_130:
    TILE_ID = 130
    NAME = "Biome Tile Pattern #130"
    WALKABLE = True if 130 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.3, 0.6000000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_130.TILE_ID, "walkable": TileBlueprint_130.WALKABLE, "cost": TileBlueprint_130.MOVEMENT_COST}


class TileBlueprint_131:
    TILE_ID = 131
    NAME = "Biome Tile Pattern #131"
    WALKABLE = True if 131 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.31, 0.6200000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_131.TILE_ID, "walkable": TileBlueprint_131.WALKABLE, "cost": TileBlueprint_131.MOVEMENT_COST}


class TileBlueprint_132:
    TILE_ID = 132
    NAME = "Biome Tile Pattern #132"
    WALKABLE = True if 132 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.32, 0.6400000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_132.TILE_ID, "walkable": TileBlueprint_132.WALKABLE, "cost": TileBlueprint_132.MOVEMENT_COST}


class TileBlueprint_133:
    TILE_ID = 133
    NAME = "Biome Tile Pattern #133"
    WALKABLE = True if 133 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.33, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_133.TILE_ID, "walkable": TileBlueprint_133.WALKABLE, "cost": TileBlueprint_133.MOVEMENT_COST}


class TileBlueprint_134:
    TILE_ID = 134
    NAME = "Biome Tile Pattern #134"
    WALKABLE = True if 134 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.34, 0.6800000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_134.TILE_ID, "walkable": TileBlueprint_134.WALKABLE, "cost": TileBlueprint_134.MOVEMENT_COST}


class TileBlueprint_135:
    TILE_ID = 135
    NAME = "Biome Tile Pattern #135"
    WALKABLE = True if 135 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.35, 0.7000000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_135.TILE_ID, "walkable": TileBlueprint_135.WALKABLE, "cost": TileBlueprint_135.MOVEMENT_COST}


class TileBlueprint_136:
    TILE_ID = 136
    NAME = "Biome Tile Pattern #136"
    WALKABLE = True if 136 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.36, 0.7200000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_136.TILE_ID, "walkable": TileBlueprint_136.WALKABLE, "cost": TileBlueprint_136.MOVEMENT_COST}


class TileBlueprint_137:
    TILE_ID = 137
    NAME = "Biome Tile Pattern #137"
    WALKABLE = True if 137 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.37, 0.7400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_137.TILE_ID, "walkable": TileBlueprint_137.WALKABLE, "cost": TileBlueprint_137.MOVEMENT_COST}


class TileBlueprint_138:
    TILE_ID = 138
    NAME = "Biome Tile Pattern #138"
    WALKABLE = True if 138 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.3800000000000001, 0.7600000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_138.TILE_ID, "walkable": TileBlueprint_138.WALKABLE, "cost": TileBlueprint_138.MOVEMENT_COST}


class TileBlueprint_139:
    TILE_ID = 139
    NAME = "Biome Tile Pattern #139"
    WALKABLE = True if 139 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.3900000000000001, 0.7800000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_139.TILE_ID, "walkable": TileBlueprint_139.WALKABLE, "cost": TileBlueprint_139.MOVEMENT_COST}


class TileBlueprint_140:
    TILE_ID = 140
    NAME = "Biome Tile Pattern #140"
    WALKABLE = True if 140 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.4000000000000001, 0.8000000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_140.TILE_ID, "walkable": TileBlueprint_140.WALKABLE, "cost": TileBlueprint_140.MOVEMENT_COST}


class TileBlueprint_141:
    TILE_ID = 141
    NAME = "Biome Tile Pattern #141"
    WALKABLE = True if 141 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.41, 0.8199999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_141.TILE_ID, "walkable": TileBlueprint_141.WALKABLE, "cost": TileBlueprint_141.MOVEMENT_COST}


class TileBlueprint_142:
    TILE_ID = 142
    NAME = "Biome Tile Pattern #142"
    WALKABLE = True if 142 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.42, 0.8399999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_142.TILE_ID, "walkable": TileBlueprint_142.WALKABLE, "cost": TileBlueprint_142.MOVEMENT_COST}


class TileBlueprint_143:
    TILE_ID = 143
    NAME = "Biome Tile Pattern #143"
    WALKABLE = True if 143 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.43, 0.8599999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_143.TILE_ID, "walkable": TileBlueprint_143.WALKABLE, "cost": TileBlueprint_143.MOVEMENT_COST}


class TileBlueprint_144:
    TILE_ID = 144
    NAME = "Biome Tile Pattern #144"
    WALKABLE = True if 144 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.44, 0.8799999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_144.TILE_ID, "walkable": TileBlueprint_144.WALKABLE, "cost": TileBlueprint_144.MOVEMENT_COST}


class TileBlueprint_145:
    TILE_ID = 145
    NAME = "Biome Tile Pattern #145"
    WALKABLE = True if 145 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.45, 0.8999999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_145.TILE_ID, "walkable": TileBlueprint_145.WALKABLE, "cost": TileBlueprint_145.MOVEMENT_COST}


class TileBlueprint_146:
    TILE_ID = 146
    NAME = "Biome Tile Pattern #146"
    WALKABLE = True if 146 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.46, 0.9199999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_146.TILE_ID, "walkable": TileBlueprint_146.WALKABLE, "cost": TileBlueprint_146.MOVEMENT_COST}


class TileBlueprint_147:
    TILE_ID = 147
    NAME = "Biome Tile Pattern #147"
    WALKABLE = True if 147 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.47, 0.94)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_147.TILE_ID, "walkable": TileBlueprint_147.WALKABLE, "cost": TileBlueprint_147.MOVEMENT_COST}


class TileBlueprint_148:
    TILE_ID = 148
    NAME = "Biome Tile Pattern #148"
    WALKABLE = True if 148 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.48, 0.96)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_148.TILE_ID, "walkable": TileBlueprint_148.WALKABLE, "cost": TileBlueprint_148.MOVEMENT_COST}


class TileBlueprint_149:
    TILE_ID = 149
    NAME = "Biome Tile Pattern #149"
    WALKABLE = True if 149 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.49, 0.98)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_149.TILE_ID, "walkable": TileBlueprint_149.WALKABLE, "cost": TileBlueprint_149.MOVEMENT_COST}


class TileBlueprint_150:
    TILE_ID = 150
    NAME = "Biome Tile Pattern #150"
    WALKABLE = True if 150 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.5, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_150.TILE_ID, "walkable": TileBlueprint_150.WALKABLE, "cost": TileBlueprint_150.MOVEMENT_COST}


class TileBlueprint_151:
    TILE_ID = 151
    NAME = "Biome Tile Pattern #151"
    WALKABLE = True if 151 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.51, 0.020000000000000018)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_151.TILE_ID, "walkable": TileBlueprint_151.WALKABLE, "cost": TileBlueprint_151.MOVEMENT_COST}


class TileBlueprint_152:
    TILE_ID = 152
    NAME = "Biome Tile Pattern #152"
    WALKABLE = True if 152 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.52, 0.040000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_152.TILE_ID, "walkable": TileBlueprint_152.WALKABLE, "cost": TileBlueprint_152.MOVEMENT_COST}


class TileBlueprint_153:
    TILE_ID = 153
    NAME = "Biome Tile Pattern #153"
    WALKABLE = True if 153 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.53, 0.06000000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_153.TILE_ID, "walkable": TileBlueprint_153.WALKABLE, "cost": TileBlueprint_153.MOVEMENT_COST}


class TileBlueprint_154:
    TILE_ID = 154
    NAME = "Biome Tile Pattern #154"
    WALKABLE = True if 154 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.54, 0.08000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_154.TILE_ID, "walkable": TileBlueprint_154.WALKABLE, "cost": TileBlueprint_154.MOVEMENT_COST}


class TileBlueprint_155:
    TILE_ID = 155
    NAME = "Biome Tile Pattern #155"
    WALKABLE = True if 155 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.55, 0.10000000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_155.TILE_ID, "walkable": TileBlueprint_155.WALKABLE, "cost": TileBlueprint_155.MOVEMENT_COST}


class TileBlueprint_156:
    TILE_ID = 156
    NAME = "Biome Tile Pattern #156"
    WALKABLE = True if 156 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.56, 0.1200000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_156.TILE_ID, "walkable": TileBlueprint_156.WALKABLE, "cost": TileBlueprint_156.MOVEMENT_COST}


class TileBlueprint_157:
    TILE_ID = 157
    NAME = "Biome Tile Pattern #157"
    WALKABLE = True if 157 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.57, 0.14000000000000012)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_157.TILE_ID, "walkable": TileBlueprint_157.WALKABLE, "cost": TileBlueprint_157.MOVEMENT_COST}


class TileBlueprint_158:
    TILE_ID = 158
    NAME = "Biome Tile Pattern #158"
    WALKABLE = True if 158 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.58, 0.16000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_158.TILE_ID, "walkable": TileBlueprint_158.WALKABLE, "cost": TileBlueprint_158.MOVEMENT_COST}


class TileBlueprint_159:
    TILE_ID = 159
    NAME = "Biome Tile Pattern #159"
    WALKABLE = True if 159 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.59, 0.18000000000000016)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_159.TILE_ID, "walkable": TileBlueprint_159.WALKABLE, "cost": TileBlueprint_159.MOVEMENT_COST}


class TileBlueprint_160:
    TILE_ID = 160
    NAME = "Biome Tile Pattern #160"
    WALKABLE = True if 160 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.6, 0.20000000000000018)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_160.TILE_ID, "walkable": TileBlueprint_160.WALKABLE, "cost": TileBlueprint_160.MOVEMENT_COST}


class TileBlueprint_161:
    TILE_ID = 161
    NAME = "Biome Tile Pattern #161"
    WALKABLE = True if 161 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.61, 0.2200000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_161.TILE_ID, "walkable": TileBlueprint_161.WALKABLE, "cost": TileBlueprint_161.MOVEMENT_COST}


class TileBlueprint_162:
    TILE_ID = 162
    NAME = "Biome Tile Pattern #162"
    WALKABLE = True if 162 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.62, 0.2400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_162.TILE_ID, "walkable": TileBlueprint_162.WALKABLE, "cost": TileBlueprint_162.MOVEMENT_COST}


class TileBlueprint_163:
    TILE_ID = 163
    NAME = "Biome Tile Pattern #163"
    WALKABLE = True if 163 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.6300000000000001, 0.26000000000000023)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_163.TILE_ID, "walkable": TileBlueprint_163.WALKABLE, "cost": TileBlueprint_163.MOVEMENT_COST}


class TileBlueprint_164:
    TILE_ID = 164
    NAME = "Biome Tile Pattern #164"
    WALKABLE = True if 164 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.6400000000000001, 0.28000000000000025)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_164.TILE_ID, "walkable": TileBlueprint_164.WALKABLE, "cost": TileBlueprint_164.MOVEMENT_COST}


class TileBlueprint_165:
    TILE_ID = 165
    NAME = "Biome Tile Pattern #165"
    WALKABLE = True if 165 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.6500000000000001, 0.30000000000000027)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_165.TILE_ID, "walkable": TileBlueprint_165.WALKABLE, "cost": TileBlueprint_165.MOVEMENT_COST}


class TileBlueprint_166:
    TILE_ID = 166
    NAME = "Biome Tile Pattern #166"
    WALKABLE = True if 166 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.6600000000000001, 0.3200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_166.TILE_ID, "walkable": TileBlueprint_166.WALKABLE, "cost": TileBlueprint_166.MOVEMENT_COST}


class TileBlueprint_167:
    TILE_ID = 167
    NAME = "Biome Tile Pattern #167"
    WALKABLE = True if 167 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.67, 0.33999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_167.TILE_ID, "walkable": TileBlueprint_167.WALKABLE, "cost": TileBlueprint_167.MOVEMENT_COST}


class TileBlueprint_168:
    TILE_ID = 168
    NAME = "Biome Tile Pattern #168"
    WALKABLE = True if 168 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.68, 0.3599999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_168.TILE_ID, "walkable": TileBlueprint_168.WALKABLE, "cost": TileBlueprint_168.MOVEMENT_COST}


class TileBlueprint_169:
    TILE_ID = 169
    NAME = "Biome Tile Pattern #169"
    WALKABLE = True if 169 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.69, 0.3799999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_169.TILE_ID, "walkable": TileBlueprint_169.WALKABLE, "cost": TileBlueprint_169.MOVEMENT_COST}


class TileBlueprint_170:
    TILE_ID = 170
    NAME = "Biome Tile Pattern #170"
    WALKABLE = True if 170 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.7, 0.3999999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_170.TILE_ID, "walkable": TileBlueprint_170.WALKABLE, "cost": TileBlueprint_170.MOVEMENT_COST}


class TileBlueprint_171:
    TILE_ID = 171
    NAME = "Biome Tile Pattern #171"
    WALKABLE = True if 171 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.71, 0.41999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_171.TILE_ID, "walkable": TileBlueprint_171.WALKABLE, "cost": TileBlueprint_171.MOVEMENT_COST}


class TileBlueprint_172:
    TILE_ID = 172
    NAME = "Biome Tile Pattern #172"
    WALKABLE = True if 172 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.72, 0.43999999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_172.TILE_ID, "walkable": TileBlueprint_172.WALKABLE, "cost": TileBlueprint_172.MOVEMENT_COST}


class TileBlueprint_173:
    TILE_ID = 173
    NAME = "Biome Tile Pattern #173"
    WALKABLE = True if 173 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.73, 0.45999999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_173.TILE_ID, "walkable": TileBlueprint_173.WALKABLE, "cost": TileBlueprint_173.MOVEMENT_COST}


class TileBlueprint_174:
    TILE_ID = 174
    NAME = "Biome Tile Pattern #174"
    WALKABLE = True if 174 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.74, 0.48)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_174.TILE_ID, "walkable": TileBlueprint_174.WALKABLE, "cost": TileBlueprint_174.MOVEMENT_COST}


class TileBlueprint_175:
    TILE_ID = 175
    NAME = "Biome Tile Pattern #175"
    WALKABLE = True if 175 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.75, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_175.TILE_ID, "walkable": TileBlueprint_175.WALKABLE, "cost": TileBlueprint_175.MOVEMENT_COST}


class TileBlueprint_176:
    TILE_ID = 176
    NAME = "Biome Tile Pattern #176"
    WALKABLE = True if 176 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.76, 0.52)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_176.TILE_ID, "walkable": TileBlueprint_176.WALKABLE, "cost": TileBlueprint_176.MOVEMENT_COST}


class TileBlueprint_177:
    TILE_ID = 177
    NAME = "Biome Tile Pattern #177"
    WALKABLE = True if 177 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.77, 0.54)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_177.TILE_ID, "walkable": TileBlueprint_177.WALKABLE, "cost": TileBlueprint_177.MOVEMENT_COST}


class TileBlueprint_178:
    TILE_ID = 178
    NAME = "Biome Tile Pattern #178"
    WALKABLE = True if 178 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.78, 0.56)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_178.TILE_ID, "walkable": TileBlueprint_178.WALKABLE, "cost": TileBlueprint_178.MOVEMENT_COST}


class TileBlueprint_179:
    TILE_ID = 179
    NAME = "Biome Tile Pattern #179"
    WALKABLE = True if 179 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.79, 0.5800000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_179.TILE_ID, "walkable": TileBlueprint_179.WALKABLE, "cost": TileBlueprint_179.MOVEMENT_COST}


class TileBlueprint_180:
    TILE_ID = 180
    NAME = "Biome Tile Pattern #180"
    WALKABLE = True if 180 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.8, 0.6000000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_180.TILE_ID, "walkable": TileBlueprint_180.WALKABLE, "cost": TileBlueprint_180.MOVEMENT_COST}


class TileBlueprint_181:
    TILE_ID = 181
    NAME = "Biome Tile Pattern #181"
    WALKABLE = True if 181 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.81, 0.6200000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_181.TILE_ID, "walkable": TileBlueprint_181.WALKABLE, "cost": TileBlueprint_181.MOVEMENT_COST}


class TileBlueprint_182:
    TILE_ID = 182
    NAME = "Biome Tile Pattern #182"
    WALKABLE = True if 182 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.82, 0.6400000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_182.TILE_ID, "walkable": TileBlueprint_182.WALKABLE, "cost": TileBlueprint_182.MOVEMENT_COST}


class TileBlueprint_183:
    TILE_ID = 183
    NAME = "Biome Tile Pattern #183"
    WALKABLE = True if 183 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.83, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_183.TILE_ID, "walkable": TileBlueprint_183.WALKABLE, "cost": TileBlueprint_183.MOVEMENT_COST}


class TileBlueprint_184:
    TILE_ID = 184
    NAME = "Biome Tile Pattern #184"
    WALKABLE = True if 184 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.84, 0.6800000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_184.TILE_ID, "walkable": TileBlueprint_184.WALKABLE, "cost": TileBlueprint_184.MOVEMENT_COST}


class TileBlueprint_185:
    TILE_ID = 185
    NAME = "Biome Tile Pattern #185"
    WALKABLE = True if 185 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.85, 0.7000000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_185.TILE_ID, "walkable": TileBlueprint_185.WALKABLE, "cost": TileBlueprint_185.MOVEMENT_COST}


class TileBlueprint_186:
    TILE_ID = 186
    NAME = "Biome Tile Pattern #186"
    WALKABLE = True if 186 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.86, 0.7200000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_186.TILE_ID, "walkable": TileBlueprint_186.WALKABLE, "cost": TileBlueprint_186.MOVEMENT_COST}


class TileBlueprint_187:
    TILE_ID = 187
    NAME = "Biome Tile Pattern #187"
    WALKABLE = True if 187 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.87, 0.7400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_187.TILE_ID, "walkable": TileBlueprint_187.WALKABLE, "cost": TileBlueprint_187.MOVEMENT_COST}


class TileBlueprint_188:
    TILE_ID = 188
    NAME = "Biome Tile Pattern #188"
    WALKABLE = True if 188 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.8800000000000001, 0.7600000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_188.TILE_ID, "walkable": TileBlueprint_188.WALKABLE, "cost": TileBlueprint_188.MOVEMENT_COST}


class TileBlueprint_189:
    TILE_ID = 189
    NAME = "Biome Tile Pattern #189"
    WALKABLE = True if 189 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.8900000000000001, 0.7800000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_189.TILE_ID, "walkable": TileBlueprint_189.WALKABLE, "cost": TileBlueprint_189.MOVEMENT_COST}


class TileBlueprint_190:
    TILE_ID = 190
    NAME = "Biome Tile Pattern #190"
    WALKABLE = True if 190 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.9000000000000001, 0.8000000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_190.TILE_ID, "walkable": TileBlueprint_190.WALKABLE, "cost": TileBlueprint_190.MOVEMENT_COST}


class TileBlueprint_191:
    TILE_ID = 191
    NAME = "Biome Tile Pattern #191"
    WALKABLE = True if 191 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.9100000000000001, 0.8200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_191.TILE_ID, "walkable": TileBlueprint_191.WALKABLE, "cost": TileBlueprint_191.MOVEMENT_COST}


class TileBlueprint_192:
    TILE_ID = 192
    NAME = "Biome Tile Pattern #192"
    WALKABLE = True if 192 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.92, 0.8399999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_192.TILE_ID, "walkable": TileBlueprint_192.WALKABLE, "cost": TileBlueprint_192.MOVEMENT_COST}


class TileBlueprint_193:
    TILE_ID = 193
    NAME = "Biome Tile Pattern #193"
    WALKABLE = True if 193 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.93, 0.8599999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_193.TILE_ID, "walkable": TileBlueprint_193.WALKABLE, "cost": TileBlueprint_193.MOVEMENT_COST}


class TileBlueprint_194:
    TILE_ID = 194
    NAME = "Biome Tile Pattern #194"
    WALKABLE = True if 194 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.94, 0.8799999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_194.TILE_ID, "walkable": TileBlueprint_194.WALKABLE, "cost": TileBlueprint_194.MOVEMENT_COST}


class TileBlueprint_195:
    TILE_ID = 195
    NAME = "Biome Tile Pattern #195"
    WALKABLE = True if 195 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (1.95, 0.8999999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_195.TILE_ID, "walkable": TileBlueprint_195.WALKABLE, "cost": TileBlueprint_195.MOVEMENT_COST}


class TileBlueprint_196:
    TILE_ID = 196
    NAME = "Biome Tile Pattern #196"
    WALKABLE = True if 196 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (1.96, 0.9199999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_196.TILE_ID, "walkable": TileBlueprint_196.WALKABLE, "cost": TileBlueprint_196.MOVEMENT_COST}


class TileBlueprint_197:
    TILE_ID = 197
    NAME = "Biome Tile Pattern #197"
    WALKABLE = True if 197 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (1.97, 0.94)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_197.TILE_ID, "walkable": TileBlueprint_197.WALKABLE, "cost": TileBlueprint_197.MOVEMENT_COST}


class TileBlueprint_198:
    TILE_ID = 198
    NAME = "Biome Tile Pattern #198"
    WALKABLE = True if 198 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (1.98, 0.96)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_198.TILE_ID, "walkable": TileBlueprint_198.WALKABLE, "cost": TileBlueprint_198.MOVEMENT_COST}


class TileBlueprint_199:
    TILE_ID = 199
    NAME = "Biome Tile Pattern #199"
    WALKABLE = True if 199 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (1.99, 0.98)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_199.TILE_ID, "walkable": TileBlueprint_199.WALKABLE, "cost": TileBlueprint_199.MOVEMENT_COST}


class TileBlueprint_200:
    TILE_ID = 200
    NAME = "Biome Tile Pattern #200"
    WALKABLE = True if 200 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.0, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_200.TILE_ID, "walkable": TileBlueprint_200.WALKABLE, "cost": TileBlueprint_200.MOVEMENT_COST}


class TileBlueprint_201:
    TILE_ID = 201
    NAME = "Biome Tile Pattern #201"
    WALKABLE = True if 201 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.0100000000000002, 0.020000000000000462)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_201.TILE_ID, "walkable": TileBlueprint_201.WALKABLE, "cost": TileBlueprint_201.MOVEMENT_COST}


class TileBlueprint_202:
    TILE_ID = 202
    NAME = "Biome Tile Pattern #202"
    WALKABLE = True if 202 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.02, 0.040000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_202.TILE_ID, "walkable": TileBlueprint_202.WALKABLE, "cost": TileBlueprint_202.MOVEMENT_COST}


class TileBlueprint_203:
    TILE_ID = 203
    NAME = "Biome Tile Pattern #203"
    WALKABLE = True if 203 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.0300000000000002, 0.0600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_203.TILE_ID, "walkable": TileBlueprint_203.WALKABLE, "cost": TileBlueprint_203.MOVEMENT_COST}


class TileBlueprint_204:
    TILE_ID = 204
    NAME = "Biome Tile Pattern #204"
    WALKABLE = True if 204 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.04, 0.08000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_204.TILE_ID, "walkable": TileBlueprint_204.WALKABLE, "cost": TileBlueprint_204.MOVEMENT_COST}


class TileBlueprint_205:
    TILE_ID = 205
    NAME = "Biome Tile Pattern #205"
    WALKABLE = True if 205 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.05, 0.09999999999999964)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_205.TILE_ID, "walkable": TileBlueprint_205.WALKABLE, "cost": TileBlueprint_205.MOVEMENT_COST}


class TileBlueprint_206:
    TILE_ID = 206
    NAME = "Biome Tile Pattern #206"
    WALKABLE = True if 206 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.06, 0.1200000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_206.TILE_ID, "walkable": TileBlueprint_206.WALKABLE, "cost": TileBlueprint_206.MOVEMENT_COST}


class TileBlueprint_207:
    TILE_ID = 207
    NAME = "Biome Tile Pattern #207"
    WALKABLE = True if 207 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.07, 0.13999999999999968)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_207.TILE_ID, "walkable": TileBlueprint_207.WALKABLE, "cost": TileBlueprint_207.MOVEMENT_COST}


class TileBlueprint_208:
    TILE_ID = 208
    NAME = "Biome Tile Pattern #208"
    WALKABLE = True if 208 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.08, 0.16000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_208.TILE_ID, "walkable": TileBlueprint_208.WALKABLE, "cost": TileBlueprint_208.MOVEMENT_COST}


class TileBlueprint_209:
    TILE_ID = 209
    NAME = "Biome Tile Pattern #209"
    WALKABLE = True if 209 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.09, 0.17999999999999972)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_209.TILE_ID, "walkable": TileBlueprint_209.WALKABLE, "cost": TileBlueprint_209.MOVEMENT_COST}


class TileBlueprint_210:
    TILE_ID = 210
    NAME = "Biome Tile Pattern #210"
    WALKABLE = True if 210 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.1, 0.20000000000000018)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_210.TILE_ID, "walkable": TileBlueprint_210.WALKABLE, "cost": TileBlueprint_210.MOVEMENT_COST}


class TileBlueprint_211:
    TILE_ID = 211
    NAME = "Biome Tile Pattern #211"
    WALKABLE = True if 211 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.11, 0.21999999999999975)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_211.TILE_ID, "walkable": TileBlueprint_211.WALKABLE, "cost": TileBlueprint_211.MOVEMENT_COST}


class TileBlueprint_212:
    TILE_ID = 212
    NAME = "Biome Tile Pattern #212"
    WALKABLE = True if 212 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.12, 0.2400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_212.TILE_ID, "walkable": TileBlueprint_212.WALKABLE, "cost": TileBlueprint_212.MOVEMENT_COST}


class TileBlueprint_213:
    TILE_ID = 213
    NAME = "Biome Tile Pattern #213"
    WALKABLE = True if 213 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.13, 0.2599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_213.TILE_ID, "walkable": TileBlueprint_213.WALKABLE, "cost": TileBlueprint_213.MOVEMENT_COST}


class TileBlueprint_214:
    TILE_ID = 214
    NAME = "Biome Tile Pattern #214"
    WALKABLE = True if 214 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.14, 0.28000000000000025)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_214.TILE_ID, "walkable": TileBlueprint_214.WALKABLE, "cost": TileBlueprint_214.MOVEMENT_COST}


class TileBlueprint_215:
    TILE_ID = 215
    NAME = "Biome Tile Pattern #215"
    WALKABLE = True if 215 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.15, 0.2999999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_215.TILE_ID, "walkable": TileBlueprint_215.WALKABLE, "cost": TileBlueprint_215.MOVEMENT_COST}


class TileBlueprint_216:
    TILE_ID = 216
    NAME = "Biome Tile Pattern #216"
    WALKABLE = True if 216 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.16, 0.3200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_216.TILE_ID, "walkable": TileBlueprint_216.WALKABLE, "cost": TileBlueprint_216.MOVEMENT_COST}


class TileBlueprint_217:
    TILE_ID = 217
    NAME = "Biome Tile Pattern #217"
    WALKABLE = True if 217 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.17, 0.33999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_217.TILE_ID, "walkable": TileBlueprint_217.WALKABLE, "cost": TileBlueprint_217.MOVEMENT_COST}


class TileBlueprint_218:
    TILE_ID = 218
    NAME = "Biome Tile Pattern #218"
    WALKABLE = True if 218 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.18, 0.3600000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_218.TILE_ID, "walkable": TileBlueprint_218.WALKABLE, "cost": TileBlueprint_218.MOVEMENT_COST}


class TileBlueprint_219:
    TILE_ID = 219
    NAME = "Biome Tile Pattern #219"
    WALKABLE = True if 219 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.19, 0.3799999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_219.TILE_ID, "walkable": TileBlueprint_219.WALKABLE, "cost": TileBlueprint_219.MOVEMENT_COST}


class TileBlueprint_220:
    TILE_ID = 220
    NAME = "Biome Tile Pattern #220"
    WALKABLE = True if 220 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.2, 0.40000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_220.TILE_ID, "walkable": TileBlueprint_220.WALKABLE, "cost": TileBlueprint_220.MOVEMENT_COST}


class TileBlueprint_221:
    TILE_ID = 221
    NAME = "Biome Tile Pattern #221"
    WALKABLE = True if 221 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.21, 0.41999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_221.TILE_ID, "walkable": TileBlueprint_221.WALKABLE, "cost": TileBlueprint_221.MOVEMENT_COST}


class TileBlueprint_222:
    TILE_ID = 222
    NAME = "Biome Tile Pattern #222"
    WALKABLE = True if 222 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.22, 0.4400000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_222.TILE_ID, "walkable": TileBlueprint_222.WALKABLE, "cost": TileBlueprint_222.MOVEMENT_COST}


class TileBlueprint_223:
    TILE_ID = 223
    NAME = "Biome Tile Pattern #223"
    WALKABLE = True if 223 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.23, 0.45999999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_223.TILE_ID, "walkable": TileBlueprint_223.WALKABLE, "cost": TileBlueprint_223.MOVEMENT_COST}


class TileBlueprint_224:
    TILE_ID = 224
    NAME = "Biome Tile Pattern #224"
    WALKABLE = True if 224 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.24, 0.4800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_224.TILE_ID, "walkable": TileBlueprint_224.WALKABLE, "cost": TileBlueprint_224.MOVEMENT_COST}


class TileBlueprint_225:
    TILE_ID = 225
    NAME = "Biome Tile Pattern #225"
    WALKABLE = True if 225 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.25, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_225.TILE_ID, "walkable": TileBlueprint_225.WALKABLE, "cost": TileBlueprint_225.MOVEMENT_COST}


class TileBlueprint_226:
    TILE_ID = 226
    NAME = "Biome Tile Pattern #226"
    WALKABLE = True if 226 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.2600000000000002, 0.5200000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_226.TILE_ID, "walkable": TileBlueprint_226.WALKABLE, "cost": TileBlueprint_226.MOVEMENT_COST}


class TileBlueprint_227:
    TILE_ID = 227
    NAME = "Biome Tile Pattern #227"
    WALKABLE = True if 227 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.27, 0.54)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_227.TILE_ID, "walkable": TileBlueprint_227.WALKABLE, "cost": TileBlueprint_227.MOVEMENT_COST}


class TileBlueprint_228:
    TILE_ID = 228
    NAME = "Biome Tile Pattern #228"
    WALKABLE = True if 228 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.2800000000000002, 0.5600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_228.TILE_ID, "walkable": TileBlueprint_228.WALKABLE, "cost": TileBlueprint_228.MOVEMENT_COST}


class TileBlueprint_229:
    TILE_ID = 229
    NAME = "Biome Tile Pattern #229"
    WALKABLE = True if 229 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.29, 0.5800000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_229.TILE_ID, "walkable": TileBlueprint_229.WALKABLE, "cost": TileBlueprint_229.MOVEMENT_COST}


class TileBlueprint_230:
    TILE_ID = 230
    NAME = "Biome Tile Pattern #230"
    WALKABLE = True if 230 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.3000000000000003, 0.6000000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_230.TILE_ID, "walkable": TileBlueprint_230.WALKABLE, "cost": TileBlueprint_230.MOVEMENT_COST}


class TileBlueprint_231:
    TILE_ID = 231
    NAME = "Biome Tile Pattern #231"
    WALKABLE = True if 231 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.31, 0.6200000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_231.TILE_ID, "walkable": TileBlueprint_231.WALKABLE, "cost": TileBlueprint_231.MOVEMENT_COST}


class TileBlueprint_232:
    TILE_ID = 232
    NAME = "Biome Tile Pattern #232"
    WALKABLE = True if 232 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.32, 0.6399999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_232.TILE_ID, "walkable": TileBlueprint_232.WALKABLE, "cost": TileBlueprint_232.MOVEMENT_COST}


class TileBlueprint_233:
    TILE_ID = 233
    NAME = "Biome Tile Pattern #233"
    WALKABLE = True if 233 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.33, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_233.TILE_ID, "walkable": TileBlueprint_233.WALKABLE, "cost": TileBlueprint_233.MOVEMENT_COST}


class TileBlueprint_234:
    TILE_ID = 234
    NAME = "Biome Tile Pattern #234"
    WALKABLE = True if 234 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.34, 0.6799999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_234.TILE_ID, "walkable": TileBlueprint_234.WALKABLE, "cost": TileBlueprint_234.MOVEMENT_COST}


class TileBlueprint_235:
    TILE_ID = 235
    NAME = "Biome Tile Pattern #235"
    WALKABLE = True if 235 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.35, 0.7000000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_235.TILE_ID, "walkable": TileBlueprint_235.WALKABLE, "cost": TileBlueprint_235.MOVEMENT_COST}


class TileBlueprint_236:
    TILE_ID = 236
    NAME = "Biome Tile Pattern #236"
    WALKABLE = True if 236 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.36, 0.7199999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_236.TILE_ID, "walkable": TileBlueprint_236.WALKABLE, "cost": TileBlueprint_236.MOVEMENT_COST}


class TileBlueprint_237:
    TILE_ID = 237
    NAME = "Biome Tile Pattern #237"
    WALKABLE = True if 237 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.37, 0.7400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_237.TILE_ID, "walkable": TileBlueprint_237.WALKABLE, "cost": TileBlueprint_237.MOVEMENT_COST}


class TileBlueprint_238:
    TILE_ID = 238
    NAME = "Biome Tile Pattern #238"
    WALKABLE = True if 238 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.38, 0.7599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_238.TILE_ID, "walkable": TileBlueprint_238.WALKABLE, "cost": TileBlueprint_238.MOVEMENT_COST}


class TileBlueprint_239:
    TILE_ID = 239
    NAME = "Biome Tile Pattern #239"
    WALKABLE = True if 239 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.39, 0.7800000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_239.TILE_ID, "walkable": TileBlueprint_239.WALKABLE, "cost": TileBlueprint_239.MOVEMENT_COST}


class TileBlueprint_240:
    TILE_ID = 240
    NAME = "Biome Tile Pattern #240"
    WALKABLE = True if 240 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.4, 0.7999999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_240.TILE_ID, "walkable": TileBlueprint_240.WALKABLE, "cost": TileBlueprint_240.MOVEMENT_COST}


class TileBlueprint_241:
    TILE_ID = 241
    NAME = "Biome Tile Pattern #241"
    WALKABLE = True if 241 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.41, 0.8200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_241.TILE_ID, "walkable": TileBlueprint_241.WALKABLE, "cost": TileBlueprint_241.MOVEMENT_COST}


class TileBlueprint_242:
    TILE_ID = 242
    NAME = "Biome Tile Pattern #242"
    WALKABLE = True if 242 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.42, 0.8399999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_242.TILE_ID, "walkable": TileBlueprint_242.WALKABLE, "cost": TileBlueprint_242.MOVEMENT_COST}


class TileBlueprint_243:
    TILE_ID = 243
    NAME = "Biome Tile Pattern #243"
    WALKABLE = True if 243 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.43, 0.8600000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_243.TILE_ID, "walkable": TileBlueprint_243.WALKABLE, "cost": TileBlueprint_243.MOVEMENT_COST}


class TileBlueprint_244:
    TILE_ID = 244
    NAME = "Biome Tile Pattern #244"
    WALKABLE = True if 244 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.44, 0.8799999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_244.TILE_ID, "walkable": TileBlueprint_244.WALKABLE, "cost": TileBlueprint_244.MOVEMENT_COST}


class TileBlueprint_245:
    TILE_ID = 245
    NAME = "Biome Tile Pattern #245"
    WALKABLE = True if 245 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.45, 0.9000000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_245.TILE_ID, "walkable": TileBlueprint_245.WALKABLE, "cost": TileBlueprint_245.MOVEMENT_COST}


class TileBlueprint_246:
    TILE_ID = 246
    NAME = "Biome Tile Pattern #246"
    WALKABLE = True if 246 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.46, 0.9199999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_246.TILE_ID, "walkable": TileBlueprint_246.WALKABLE, "cost": TileBlueprint_246.MOVEMENT_COST}


class TileBlueprint_247:
    TILE_ID = 247
    NAME = "Biome Tile Pattern #247"
    WALKABLE = True if 247 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.47, 0.9400000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_247.TILE_ID, "walkable": TileBlueprint_247.WALKABLE, "cost": TileBlueprint_247.MOVEMENT_COST}


class TileBlueprint_248:
    TILE_ID = 248
    NAME = "Biome Tile Pattern #248"
    WALKABLE = True if 248 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.48, 0.96)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_248.TILE_ID, "walkable": TileBlueprint_248.WALKABLE, "cost": TileBlueprint_248.MOVEMENT_COST}


class TileBlueprint_249:
    TILE_ID = 249
    NAME = "Biome Tile Pattern #249"
    WALKABLE = True if 249 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.49, 0.9800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_249.TILE_ID, "walkable": TileBlueprint_249.WALKABLE, "cost": TileBlueprint_249.MOVEMENT_COST}


class TileBlueprint_250:
    TILE_ID = 250
    NAME = "Biome Tile Pattern #250"
    WALKABLE = True if 250 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.5, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_250.TILE_ID, "walkable": TileBlueprint_250.WALKABLE, "cost": TileBlueprint_250.MOVEMENT_COST}


class TileBlueprint_251:
    TILE_ID = 251
    NAME = "Biome Tile Pattern #251"
    WALKABLE = True if 251 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.5100000000000002, 0.020000000000000462)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_251.TILE_ID, "walkable": TileBlueprint_251.WALKABLE, "cost": TileBlueprint_251.MOVEMENT_COST}


class TileBlueprint_252:
    TILE_ID = 252
    NAME = "Biome Tile Pattern #252"
    WALKABLE = True if 252 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.52, 0.040000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_252.TILE_ID, "walkable": TileBlueprint_252.WALKABLE, "cost": TileBlueprint_252.MOVEMENT_COST}


class TileBlueprint_253:
    TILE_ID = 253
    NAME = "Biome Tile Pattern #253"
    WALKABLE = True if 253 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.5300000000000002, 0.0600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_253.TILE_ID, "walkable": TileBlueprint_253.WALKABLE, "cost": TileBlueprint_253.MOVEMENT_COST}


class TileBlueprint_254:
    TILE_ID = 254
    NAME = "Biome Tile Pattern #254"
    WALKABLE = True if 254 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.54, 0.08000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_254.TILE_ID, "walkable": TileBlueprint_254.WALKABLE, "cost": TileBlueprint_254.MOVEMENT_COST}


class TileBlueprint_255:
    TILE_ID = 255
    NAME = "Biome Tile Pattern #255"
    WALKABLE = True if 255 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.5500000000000003, 0.10000000000000053)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_255.TILE_ID, "walkable": TileBlueprint_255.WALKABLE, "cost": TileBlueprint_255.MOVEMENT_COST}


class TileBlueprint_256:
    TILE_ID = 256
    NAME = "Biome Tile Pattern #256"
    WALKABLE = True if 256 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.56, 0.1200000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_256.TILE_ID, "walkable": TileBlueprint_256.WALKABLE, "cost": TileBlueprint_256.MOVEMENT_COST}


class TileBlueprint_257:
    TILE_ID = 257
    NAME = "Biome Tile Pattern #257"
    WALKABLE = True if 257 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.57, 0.13999999999999968)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_257.TILE_ID, "walkable": TileBlueprint_257.WALKABLE, "cost": TileBlueprint_257.MOVEMENT_COST}


class TileBlueprint_258:
    TILE_ID = 258
    NAME = "Biome Tile Pattern #258"
    WALKABLE = True if 258 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.58, 0.16000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_258.TILE_ID, "walkable": TileBlueprint_258.WALKABLE, "cost": TileBlueprint_258.MOVEMENT_COST}


class TileBlueprint_259:
    TILE_ID = 259
    NAME = "Biome Tile Pattern #259"
    WALKABLE = True if 259 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.59, 0.17999999999999972)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_259.TILE_ID, "walkable": TileBlueprint_259.WALKABLE, "cost": TileBlueprint_259.MOVEMENT_COST}


class TileBlueprint_260:
    TILE_ID = 260
    NAME = "Biome Tile Pattern #260"
    WALKABLE = True if 260 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.6, 0.20000000000000018)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_260.TILE_ID, "walkable": TileBlueprint_260.WALKABLE, "cost": TileBlueprint_260.MOVEMENT_COST}


class TileBlueprint_261:
    TILE_ID = 261
    NAME = "Biome Tile Pattern #261"
    WALKABLE = True if 261 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.61, 0.21999999999999975)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_261.TILE_ID, "walkable": TileBlueprint_261.WALKABLE, "cost": TileBlueprint_261.MOVEMENT_COST}


class TileBlueprint_262:
    TILE_ID = 262
    NAME = "Biome Tile Pattern #262"
    WALKABLE = True if 262 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.62, 0.2400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_262.TILE_ID, "walkable": TileBlueprint_262.WALKABLE, "cost": TileBlueprint_262.MOVEMENT_COST}


class TileBlueprint_263:
    TILE_ID = 263
    NAME = "Biome Tile Pattern #263"
    WALKABLE = True if 263 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.63, 0.2599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_263.TILE_ID, "walkable": TileBlueprint_263.WALKABLE, "cost": TileBlueprint_263.MOVEMENT_COST}


class TileBlueprint_264:
    TILE_ID = 264
    NAME = "Biome Tile Pattern #264"
    WALKABLE = True if 264 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.64, 0.28000000000000025)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_264.TILE_ID, "walkable": TileBlueprint_264.WALKABLE, "cost": TileBlueprint_264.MOVEMENT_COST}


class TileBlueprint_265:
    TILE_ID = 265
    NAME = "Biome Tile Pattern #265"
    WALKABLE = True if 265 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.65, 0.2999999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_265.TILE_ID, "walkable": TileBlueprint_265.WALKABLE, "cost": TileBlueprint_265.MOVEMENT_COST}


class TileBlueprint_266:
    TILE_ID = 266
    NAME = "Biome Tile Pattern #266"
    WALKABLE = True if 266 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.66, 0.3200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_266.TILE_ID, "walkable": TileBlueprint_266.WALKABLE, "cost": TileBlueprint_266.MOVEMENT_COST}


class TileBlueprint_267:
    TILE_ID = 267
    NAME = "Biome Tile Pattern #267"
    WALKABLE = True if 267 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.67, 0.33999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_267.TILE_ID, "walkable": TileBlueprint_267.WALKABLE, "cost": TileBlueprint_267.MOVEMENT_COST}


class TileBlueprint_268:
    TILE_ID = 268
    NAME = "Biome Tile Pattern #268"
    WALKABLE = True if 268 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.68, 0.3600000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_268.TILE_ID, "walkable": TileBlueprint_268.WALKABLE, "cost": TileBlueprint_268.MOVEMENT_COST}


class TileBlueprint_269:
    TILE_ID = 269
    NAME = "Biome Tile Pattern #269"
    WALKABLE = True if 269 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.69, 0.3799999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_269.TILE_ID, "walkable": TileBlueprint_269.WALKABLE, "cost": TileBlueprint_269.MOVEMENT_COST}


class TileBlueprint_270:
    TILE_ID = 270
    NAME = "Biome Tile Pattern #270"
    WALKABLE = True if 270 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.7, 0.40000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_270.TILE_ID, "walkable": TileBlueprint_270.WALKABLE, "cost": TileBlueprint_270.MOVEMENT_COST}


class TileBlueprint_271:
    TILE_ID = 271
    NAME = "Biome Tile Pattern #271"
    WALKABLE = True if 271 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.71, 0.41999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_271.TILE_ID, "walkable": TileBlueprint_271.WALKABLE, "cost": TileBlueprint_271.MOVEMENT_COST}


class TileBlueprint_272:
    TILE_ID = 272
    NAME = "Biome Tile Pattern #272"
    WALKABLE = True if 272 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.72, 0.4400000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_272.TILE_ID, "walkable": TileBlueprint_272.WALKABLE, "cost": TileBlueprint_272.MOVEMENT_COST}


class TileBlueprint_273:
    TILE_ID = 273
    NAME = "Biome Tile Pattern #273"
    WALKABLE = True if 273 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.73, 0.45999999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_273.TILE_ID, "walkable": TileBlueprint_273.WALKABLE, "cost": TileBlueprint_273.MOVEMENT_COST}


class TileBlueprint_274:
    TILE_ID = 274
    NAME = "Biome Tile Pattern #274"
    WALKABLE = True if 274 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.74, 0.4800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_274.TILE_ID, "walkable": TileBlueprint_274.WALKABLE, "cost": TileBlueprint_274.MOVEMENT_COST}


class TileBlueprint_275:
    TILE_ID = 275
    NAME = "Biome Tile Pattern #275"
    WALKABLE = True if 275 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.75, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_275.TILE_ID, "walkable": TileBlueprint_275.WALKABLE, "cost": TileBlueprint_275.MOVEMENT_COST}


class TileBlueprint_276:
    TILE_ID = 276
    NAME = "Biome Tile Pattern #276"
    WALKABLE = True if 276 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.7600000000000002, 0.5200000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_276.TILE_ID, "walkable": TileBlueprint_276.WALKABLE, "cost": TileBlueprint_276.MOVEMENT_COST}


class TileBlueprint_277:
    TILE_ID = 277
    NAME = "Biome Tile Pattern #277"
    WALKABLE = True if 277 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.77, 0.54)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_277.TILE_ID, "walkable": TileBlueprint_277.WALKABLE, "cost": TileBlueprint_277.MOVEMENT_COST}


class TileBlueprint_278:
    TILE_ID = 278
    NAME = "Biome Tile Pattern #278"
    WALKABLE = True if 278 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.7800000000000002, 0.5600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_278.TILE_ID, "walkable": TileBlueprint_278.WALKABLE, "cost": TileBlueprint_278.MOVEMENT_COST}


class TileBlueprint_279:
    TILE_ID = 279
    NAME = "Biome Tile Pattern #279"
    WALKABLE = True if 279 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.79, 0.5800000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_279.TILE_ID, "walkable": TileBlueprint_279.WALKABLE, "cost": TileBlueprint_279.MOVEMENT_COST}


class TileBlueprint_280:
    TILE_ID = 280
    NAME = "Biome Tile Pattern #280"
    WALKABLE = True if 280 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.8000000000000003, 0.6000000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_280.TILE_ID, "walkable": TileBlueprint_280.WALKABLE, "cost": TileBlueprint_280.MOVEMENT_COST}


class TileBlueprint_281:
    TILE_ID = 281
    NAME = "Biome Tile Pattern #281"
    WALKABLE = True if 281 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.81, 0.6200000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_281.TILE_ID, "walkable": TileBlueprint_281.WALKABLE, "cost": TileBlueprint_281.MOVEMENT_COST}


class TileBlueprint_282:
    TILE_ID = 282
    NAME = "Biome Tile Pattern #282"
    WALKABLE = True if 282 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.82, 0.6399999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_282.TILE_ID, "walkable": TileBlueprint_282.WALKABLE, "cost": TileBlueprint_282.MOVEMENT_COST}


class TileBlueprint_283:
    TILE_ID = 283
    NAME = "Biome Tile Pattern #283"
    WALKABLE = True if 283 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.83, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_283.TILE_ID, "walkable": TileBlueprint_283.WALKABLE, "cost": TileBlueprint_283.MOVEMENT_COST}


class TileBlueprint_284:
    TILE_ID = 284
    NAME = "Biome Tile Pattern #284"
    WALKABLE = True if 284 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.84, 0.6799999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_284.TILE_ID, "walkable": TileBlueprint_284.WALKABLE, "cost": TileBlueprint_284.MOVEMENT_COST}


class TileBlueprint_285:
    TILE_ID = 285
    NAME = "Biome Tile Pattern #285"
    WALKABLE = True if 285 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.85, 0.7000000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_285.TILE_ID, "walkable": TileBlueprint_285.WALKABLE, "cost": TileBlueprint_285.MOVEMENT_COST}


class TileBlueprint_286:
    TILE_ID = 286
    NAME = "Biome Tile Pattern #286"
    WALKABLE = True if 286 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.86, 0.7199999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_286.TILE_ID, "walkable": TileBlueprint_286.WALKABLE, "cost": TileBlueprint_286.MOVEMENT_COST}


class TileBlueprint_287:
    TILE_ID = 287
    NAME = "Biome Tile Pattern #287"
    WALKABLE = True if 287 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.87, 0.7400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_287.TILE_ID, "walkable": TileBlueprint_287.WALKABLE, "cost": TileBlueprint_287.MOVEMENT_COST}


class TileBlueprint_288:
    TILE_ID = 288
    NAME = "Biome Tile Pattern #288"
    WALKABLE = True if 288 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.88, 0.7599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_288.TILE_ID, "walkable": TileBlueprint_288.WALKABLE, "cost": TileBlueprint_288.MOVEMENT_COST}


class TileBlueprint_289:
    TILE_ID = 289
    NAME = "Biome Tile Pattern #289"
    WALKABLE = True if 289 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.89, 0.7800000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_289.TILE_ID, "walkable": TileBlueprint_289.WALKABLE, "cost": TileBlueprint_289.MOVEMENT_COST}


class TileBlueprint_290:
    TILE_ID = 290
    NAME = "Biome Tile Pattern #290"
    WALKABLE = True if 290 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.9, 0.7999999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_290.TILE_ID, "walkable": TileBlueprint_290.WALKABLE, "cost": TileBlueprint_290.MOVEMENT_COST}


class TileBlueprint_291:
    TILE_ID = 291
    NAME = "Biome Tile Pattern #291"
    WALKABLE = True if 291 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.91, 0.8200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_291.TILE_ID, "walkable": TileBlueprint_291.WALKABLE, "cost": TileBlueprint_291.MOVEMENT_COST}


class TileBlueprint_292:
    TILE_ID = 292
    NAME = "Biome Tile Pattern #292"
    WALKABLE = True if 292 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.92, 0.8399999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_292.TILE_ID, "walkable": TileBlueprint_292.WALKABLE, "cost": TileBlueprint_292.MOVEMENT_COST}


class TileBlueprint_293:
    TILE_ID = 293
    NAME = "Biome Tile Pattern #293"
    WALKABLE = True if 293 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.93, 0.8600000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_293.TILE_ID, "walkable": TileBlueprint_293.WALKABLE, "cost": TileBlueprint_293.MOVEMENT_COST}


class TileBlueprint_294:
    TILE_ID = 294
    NAME = "Biome Tile Pattern #294"
    WALKABLE = True if 294 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.94, 0.8799999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_294.TILE_ID, "walkable": TileBlueprint_294.WALKABLE, "cost": TileBlueprint_294.MOVEMENT_COST}


class TileBlueprint_295:
    TILE_ID = 295
    NAME = "Biome Tile Pattern #295"
    WALKABLE = True if 295 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (2.95, 0.9000000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_295.TILE_ID, "walkable": TileBlueprint_295.WALKABLE, "cost": TileBlueprint_295.MOVEMENT_COST}


class TileBlueprint_296:
    TILE_ID = 296
    NAME = "Biome Tile Pattern #296"
    WALKABLE = True if 296 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (2.96, 0.9199999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_296.TILE_ID, "walkable": TileBlueprint_296.WALKABLE, "cost": TileBlueprint_296.MOVEMENT_COST}


class TileBlueprint_297:
    TILE_ID = 297
    NAME = "Biome Tile Pattern #297"
    WALKABLE = True if 297 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (2.97, 0.9400000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_297.TILE_ID, "walkable": TileBlueprint_297.WALKABLE, "cost": TileBlueprint_297.MOVEMENT_COST}


class TileBlueprint_298:
    TILE_ID = 298
    NAME = "Biome Tile Pattern #298"
    WALKABLE = True if 298 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (2.98, 0.96)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_298.TILE_ID, "walkable": TileBlueprint_298.WALKABLE, "cost": TileBlueprint_298.MOVEMENT_COST}


class TileBlueprint_299:
    TILE_ID = 299
    NAME = "Biome Tile Pattern #299"
    WALKABLE = True if 299 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (2.99, 0.9800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_299.TILE_ID, "walkable": TileBlueprint_299.WALKABLE, "cost": TileBlueprint_299.MOVEMENT_COST}


class TileBlueprint_300:
    TILE_ID = 300
    NAME = "Biome Tile Pattern #300"
    WALKABLE = True if 300 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.0, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_300.TILE_ID, "walkable": TileBlueprint_300.WALKABLE, "cost": TileBlueprint_300.MOVEMENT_COST}


class TileBlueprint_301:
    TILE_ID = 301
    NAME = "Biome Tile Pattern #301"
    WALKABLE = True if 301 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.0100000000000002, 0.020000000000000462)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_301.TILE_ID, "walkable": TileBlueprint_301.WALKABLE, "cost": TileBlueprint_301.MOVEMENT_COST}


class TileBlueprint_302:
    TILE_ID = 302
    NAME = "Biome Tile Pattern #302"
    WALKABLE = True if 302 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.02, 0.040000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_302.TILE_ID, "walkable": TileBlueprint_302.WALKABLE, "cost": TileBlueprint_302.MOVEMENT_COST}


class TileBlueprint_303:
    TILE_ID = 303
    NAME = "Biome Tile Pattern #303"
    WALKABLE = True if 303 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.0300000000000002, 0.0600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_303.TILE_ID, "walkable": TileBlueprint_303.WALKABLE, "cost": TileBlueprint_303.MOVEMENT_COST}


class TileBlueprint_304:
    TILE_ID = 304
    NAME = "Biome Tile Pattern #304"
    WALKABLE = True if 304 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.04, 0.08000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_304.TILE_ID, "walkable": TileBlueprint_304.WALKABLE, "cost": TileBlueprint_304.MOVEMENT_COST}


class TileBlueprint_305:
    TILE_ID = 305
    NAME = "Biome Tile Pattern #305"
    WALKABLE = True if 305 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.0500000000000003, 0.10000000000000053)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_305.TILE_ID, "walkable": TileBlueprint_305.WALKABLE, "cost": TileBlueprint_305.MOVEMENT_COST}


class TileBlueprint_306:
    TILE_ID = 306
    NAME = "Biome Tile Pattern #306"
    WALKABLE = True if 306 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.06, 0.1200000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_306.TILE_ID, "walkable": TileBlueprint_306.WALKABLE, "cost": TileBlueprint_306.MOVEMENT_COST}


class TileBlueprint_307:
    TILE_ID = 307
    NAME = "Biome Tile Pattern #307"
    WALKABLE = True if 307 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.0700000000000003, 0.14000000000000057)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_307.TILE_ID, "walkable": TileBlueprint_307.WALKABLE, "cost": TileBlueprint_307.MOVEMENT_COST}


class TileBlueprint_308:
    TILE_ID = 308
    NAME = "Biome Tile Pattern #308"
    WALKABLE = True if 308 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.08, 0.16000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_308.TILE_ID, "walkable": TileBlueprint_308.WALKABLE, "cost": TileBlueprint_308.MOVEMENT_COST}


class TileBlueprint_309:
    TILE_ID = 309
    NAME = "Biome Tile Pattern #309"
    WALKABLE = True if 309 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.09, 0.17999999999999972)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_309.TILE_ID, "walkable": TileBlueprint_309.WALKABLE, "cost": TileBlueprint_309.MOVEMENT_COST}


class TileBlueprint_310:
    TILE_ID = 310
    NAME = "Biome Tile Pattern #310"
    WALKABLE = True if 310 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.1, 0.20000000000000018)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_310.TILE_ID, "walkable": TileBlueprint_310.WALKABLE, "cost": TileBlueprint_310.MOVEMENT_COST}


class TileBlueprint_311:
    TILE_ID = 311
    NAME = "Biome Tile Pattern #311"
    WALKABLE = True if 311 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.11, 0.21999999999999975)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_311.TILE_ID, "walkable": TileBlueprint_311.WALKABLE, "cost": TileBlueprint_311.MOVEMENT_COST}


class TileBlueprint_312:
    TILE_ID = 312
    NAME = "Biome Tile Pattern #312"
    WALKABLE = True if 312 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.12, 0.2400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_312.TILE_ID, "walkable": TileBlueprint_312.WALKABLE, "cost": TileBlueprint_312.MOVEMENT_COST}


class TileBlueprint_313:
    TILE_ID = 313
    NAME = "Biome Tile Pattern #313"
    WALKABLE = True if 313 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.13, 0.2599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_313.TILE_ID, "walkable": TileBlueprint_313.WALKABLE, "cost": TileBlueprint_313.MOVEMENT_COST}


class TileBlueprint_314:
    TILE_ID = 314
    NAME = "Biome Tile Pattern #314"
    WALKABLE = True if 314 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.14, 0.28000000000000025)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_314.TILE_ID, "walkable": TileBlueprint_314.WALKABLE, "cost": TileBlueprint_314.MOVEMENT_COST}


class TileBlueprint_315:
    TILE_ID = 315
    NAME = "Biome Tile Pattern #315"
    WALKABLE = True if 315 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.15, 0.2999999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_315.TILE_ID, "walkable": TileBlueprint_315.WALKABLE, "cost": TileBlueprint_315.MOVEMENT_COST}


class TileBlueprint_316:
    TILE_ID = 316
    NAME = "Biome Tile Pattern #316"
    WALKABLE = True if 316 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.16, 0.3200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_316.TILE_ID, "walkable": TileBlueprint_316.WALKABLE, "cost": TileBlueprint_316.MOVEMENT_COST}


class TileBlueprint_317:
    TILE_ID = 317
    NAME = "Biome Tile Pattern #317"
    WALKABLE = True if 317 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.17, 0.33999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_317.TILE_ID, "walkable": TileBlueprint_317.WALKABLE, "cost": TileBlueprint_317.MOVEMENT_COST}


class TileBlueprint_318:
    TILE_ID = 318
    NAME = "Biome Tile Pattern #318"
    WALKABLE = True if 318 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.18, 0.3600000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_318.TILE_ID, "walkable": TileBlueprint_318.WALKABLE, "cost": TileBlueprint_318.MOVEMENT_COST}


class TileBlueprint_319:
    TILE_ID = 319
    NAME = "Biome Tile Pattern #319"
    WALKABLE = True if 319 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.19, 0.3799999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_319.TILE_ID, "walkable": TileBlueprint_319.WALKABLE, "cost": TileBlueprint_319.MOVEMENT_COST}


class TileBlueprint_320:
    TILE_ID = 320
    NAME = "Biome Tile Pattern #320"
    WALKABLE = True if 320 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.2, 0.40000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_320.TILE_ID, "walkable": TileBlueprint_320.WALKABLE, "cost": TileBlueprint_320.MOVEMENT_COST}


class TileBlueprint_321:
    TILE_ID = 321
    NAME = "Biome Tile Pattern #321"
    WALKABLE = True if 321 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.21, 0.41999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_321.TILE_ID, "walkable": TileBlueprint_321.WALKABLE, "cost": TileBlueprint_321.MOVEMENT_COST}


class TileBlueprint_322:
    TILE_ID = 322
    NAME = "Biome Tile Pattern #322"
    WALKABLE = True if 322 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.22, 0.4400000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_322.TILE_ID, "walkable": TileBlueprint_322.WALKABLE, "cost": TileBlueprint_322.MOVEMENT_COST}


class TileBlueprint_323:
    TILE_ID = 323
    NAME = "Biome Tile Pattern #323"
    WALKABLE = True if 323 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.23, 0.45999999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_323.TILE_ID, "walkable": TileBlueprint_323.WALKABLE, "cost": TileBlueprint_323.MOVEMENT_COST}


class TileBlueprint_324:
    TILE_ID = 324
    NAME = "Biome Tile Pattern #324"
    WALKABLE = True if 324 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.24, 0.4800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_324.TILE_ID, "walkable": TileBlueprint_324.WALKABLE, "cost": TileBlueprint_324.MOVEMENT_COST}


class TileBlueprint_325:
    TILE_ID = 325
    NAME = "Biome Tile Pattern #325"
    WALKABLE = True if 325 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.25, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_325.TILE_ID, "walkable": TileBlueprint_325.WALKABLE, "cost": TileBlueprint_325.MOVEMENT_COST}


class TileBlueprint_326:
    TILE_ID = 326
    NAME = "Biome Tile Pattern #326"
    WALKABLE = True if 326 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.2600000000000002, 0.5200000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_326.TILE_ID, "walkable": TileBlueprint_326.WALKABLE, "cost": TileBlueprint_326.MOVEMENT_COST}


class TileBlueprint_327:
    TILE_ID = 327
    NAME = "Biome Tile Pattern #327"
    WALKABLE = True if 327 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.27, 0.54)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_327.TILE_ID, "walkable": TileBlueprint_327.WALKABLE, "cost": TileBlueprint_327.MOVEMENT_COST}


class TileBlueprint_328:
    TILE_ID = 328
    NAME = "Biome Tile Pattern #328"
    WALKABLE = True if 328 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.2800000000000002, 0.5600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_328.TILE_ID, "walkable": TileBlueprint_328.WALKABLE, "cost": TileBlueprint_328.MOVEMENT_COST}


class TileBlueprint_329:
    TILE_ID = 329
    NAME = "Biome Tile Pattern #329"
    WALKABLE = True if 329 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.29, 0.5800000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_329.TILE_ID, "walkable": TileBlueprint_329.WALKABLE, "cost": TileBlueprint_329.MOVEMENT_COST}


class TileBlueprint_330:
    TILE_ID = 330
    NAME = "Biome Tile Pattern #330"
    WALKABLE = True if 330 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.3000000000000003, 0.6000000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_330.TILE_ID, "walkable": TileBlueprint_330.WALKABLE, "cost": TileBlueprint_330.MOVEMENT_COST}


class TileBlueprint_331:
    TILE_ID = 331
    NAME = "Biome Tile Pattern #331"
    WALKABLE = True if 331 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.31, 0.6200000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_331.TILE_ID, "walkable": TileBlueprint_331.WALKABLE, "cost": TileBlueprint_331.MOVEMENT_COST}


class TileBlueprint_332:
    TILE_ID = 332
    NAME = "Biome Tile Pattern #332"
    WALKABLE = True if 332 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.3200000000000003, 0.6400000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_332.TILE_ID, "walkable": TileBlueprint_332.WALKABLE, "cost": TileBlueprint_332.MOVEMENT_COST}


class TileBlueprint_333:
    TILE_ID = 333
    NAME = "Biome Tile Pattern #333"
    WALKABLE = True if 333 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.33, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_333.TILE_ID, "walkable": TileBlueprint_333.WALKABLE, "cost": TileBlueprint_333.MOVEMENT_COST}


class TileBlueprint_334:
    TILE_ID = 334
    NAME = "Biome Tile Pattern #334"
    WALKABLE = True if 334 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.34, 0.6799999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_334.TILE_ID, "walkable": TileBlueprint_334.WALKABLE, "cost": TileBlueprint_334.MOVEMENT_COST}


class TileBlueprint_335:
    TILE_ID = 335
    NAME = "Biome Tile Pattern #335"
    WALKABLE = True if 335 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.35, 0.7000000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_335.TILE_ID, "walkable": TileBlueprint_335.WALKABLE, "cost": TileBlueprint_335.MOVEMENT_COST}


class TileBlueprint_336:
    TILE_ID = 336
    NAME = "Biome Tile Pattern #336"
    WALKABLE = True if 336 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.36, 0.7199999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_336.TILE_ID, "walkable": TileBlueprint_336.WALKABLE, "cost": TileBlueprint_336.MOVEMENT_COST}


class TileBlueprint_337:
    TILE_ID = 337
    NAME = "Biome Tile Pattern #337"
    WALKABLE = True if 337 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.37, 0.7400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_337.TILE_ID, "walkable": TileBlueprint_337.WALKABLE, "cost": TileBlueprint_337.MOVEMENT_COST}


class TileBlueprint_338:
    TILE_ID = 338
    NAME = "Biome Tile Pattern #338"
    WALKABLE = True if 338 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.38, 0.7599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_338.TILE_ID, "walkable": TileBlueprint_338.WALKABLE, "cost": TileBlueprint_338.MOVEMENT_COST}


class TileBlueprint_339:
    TILE_ID = 339
    NAME = "Biome Tile Pattern #339"
    WALKABLE = True if 339 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.39, 0.7800000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_339.TILE_ID, "walkable": TileBlueprint_339.WALKABLE, "cost": TileBlueprint_339.MOVEMENT_COST}


class TileBlueprint_340:
    TILE_ID = 340
    NAME = "Biome Tile Pattern #340"
    WALKABLE = True if 340 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.4, 0.7999999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_340.TILE_ID, "walkable": TileBlueprint_340.WALKABLE, "cost": TileBlueprint_340.MOVEMENT_COST}


class TileBlueprint_341:
    TILE_ID = 341
    NAME = "Biome Tile Pattern #341"
    WALKABLE = True if 341 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.41, 0.8200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_341.TILE_ID, "walkable": TileBlueprint_341.WALKABLE, "cost": TileBlueprint_341.MOVEMENT_COST}


class TileBlueprint_342:
    TILE_ID = 342
    NAME = "Biome Tile Pattern #342"
    WALKABLE = True if 342 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.42, 0.8399999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_342.TILE_ID, "walkable": TileBlueprint_342.WALKABLE, "cost": TileBlueprint_342.MOVEMENT_COST}


class TileBlueprint_343:
    TILE_ID = 343
    NAME = "Biome Tile Pattern #343"
    WALKABLE = True if 343 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.43, 0.8600000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_343.TILE_ID, "walkable": TileBlueprint_343.WALKABLE, "cost": TileBlueprint_343.MOVEMENT_COST}


class TileBlueprint_344:
    TILE_ID = 344
    NAME = "Biome Tile Pattern #344"
    WALKABLE = True if 344 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.44, 0.8799999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_344.TILE_ID, "walkable": TileBlueprint_344.WALKABLE, "cost": TileBlueprint_344.MOVEMENT_COST}


class TileBlueprint_345:
    TILE_ID = 345
    NAME = "Biome Tile Pattern #345"
    WALKABLE = True if 345 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.45, 0.9000000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_345.TILE_ID, "walkable": TileBlueprint_345.WALKABLE, "cost": TileBlueprint_345.MOVEMENT_COST}


class TileBlueprint_346:
    TILE_ID = 346
    NAME = "Biome Tile Pattern #346"
    WALKABLE = True if 346 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.46, 0.9199999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_346.TILE_ID, "walkable": TileBlueprint_346.WALKABLE, "cost": TileBlueprint_346.MOVEMENT_COST}


class TileBlueprint_347:
    TILE_ID = 347
    NAME = "Biome Tile Pattern #347"
    WALKABLE = True if 347 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.47, 0.9400000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_347.TILE_ID, "walkable": TileBlueprint_347.WALKABLE, "cost": TileBlueprint_347.MOVEMENT_COST}


class TileBlueprint_348:
    TILE_ID = 348
    NAME = "Biome Tile Pattern #348"
    WALKABLE = True if 348 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.48, 0.96)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_348.TILE_ID, "walkable": TileBlueprint_348.WALKABLE, "cost": TileBlueprint_348.MOVEMENT_COST}


class TileBlueprint_349:
    TILE_ID = 349
    NAME = "Biome Tile Pattern #349"
    WALKABLE = True if 349 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.49, 0.9800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_349.TILE_ID, "walkable": TileBlueprint_349.WALKABLE, "cost": TileBlueprint_349.MOVEMENT_COST}


class TileBlueprint_350:
    TILE_ID = 350
    NAME = "Biome Tile Pattern #350"
    WALKABLE = True if 350 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.5, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_350.TILE_ID, "walkable": TileBlueprint_350.WALKABLE, "cost": TileBlueprint_350.MOVEMENT_COST}


class TileBlueprint_351:
    TILE_ID = 351
    NAME = "Biome Tile Pattern #351"
    WALKABLE = True if 351 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.5100000000000002, 0.020000000000000462)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_351.TILE_ID, "walkable": TileBlueprint_351.WALKABLE, "cost": TileBlueprint_351.MOVEMENT_COST}


class TileBlueprint_352:
    TILE_ID = 352
    NAME = "Biome Tile Pattern #352"
    WALKABLE = True if 352 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.52, 0.040000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_352.TILE_ID, "walkable": TileBlueprint_352.WALKABLE, "cost": TileBlueprint_352.MOVEMENT_COST}


class TileBlueprint_353:
    TILE_ID = 353
    NAME = "Biome Tile Pattern #353"
    WALKABLE = True if 353 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.5300000000000002, 0.0600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_353.TILE_ID, "walkable": TileBlueprint_353.WALKABLE, "cost": TileBlueprint_353.MOVEMENT_COST}


class TileBlueprint_354:
    TILE_ID = 354
    NAME = "Biome Tile Pattern #354"
    WALKABLE = True if 354 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.54, 0.08000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_354.TILE_ID, "walkable": TileBlueprint_354.WALKABLE, "cost": TileBlueprint_354.MOVEMENT_COST}


class TileBlueprint_355:
    TILE_ID = 355
    NAME = "Biome Tile Pattern #355"
    WALKABLE = True if 355 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.5500000000000003, 0.10000000000000053)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_355.TILE_ID, "walkable": TileBlueprint_355.WALKABLE, "cost": TileBlueprint_355.MOVEMENT_COST}


class TileBlueprint_356:
    TILE_ID = 356
    NAME = "Biome Tile Pattern #356"
    WALKABLE = True if 356 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.56, 0.1200000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_356.TILE_ID, "walkable": TileBlueprint_356.WALKABLE, "cost": TileBlueprint_356.MOVEMENT_COST}


class TileBlueprint_357:
    TILE_ID = 357
    NAME = "Biome Tile Pattern #357"
    WALKABLE = True if 357 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.5700000000000003, 0.14000000000000057)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_357.TILE_ID, "walkable": TileBlueprint_357.WALKABLE, "cost": TileBlueprint_357.MOVEMENT_COST}


class TileBlueprint_358:
    TILE_ID = 358
    NAME = "Biome Tile Pattern #358"
    WALKABLE = True if 358 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.58, 0.16000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_358.TILE_ID, "walkable": TileBlueprint_358.WALKABLE, "cost": TileBlueprint_358.MOVEMENT_COST}


class TileBlueprint_359:
    TILE_ID = 359
    NAME = "Biome Tile Pattern #359"
    WALKABLE = True if 359 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.59, 0.17999999999999972)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_359.TILE_ID, "walkable": TileBlueprint_359.WALKABLE, "cost": TileBlueprint_359.MOVEMENT_COST}


class TileBlueprint_360:
    TILE_ID = 360
    NAME = "Biome Tile Pattern #360"
    WALKABLE = True if 360 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.6, 0.20000000000000018)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_360.TILE_ID, "walkable": TileBlueprint_360.WALKABLE, "cost": TileBlueprint_360.MOVEMENT_COST}


class TileBlueprint_361:
    TILE_ID = 361
    NAME = "Biome Tile Pattern #361"
    WALKABLE = True if 361 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.61, 0.21999999999999975)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_361.TILE_ID, "walkable": TileBlueprint_361.WALKABLE, "cost": TileBlueprint_361.MOVEMENT_COST}


class TileBlueprint_362:
    TILE_ID = 362
    NAME = "Biome Tile Pattern #362"
    WALKABLE = True if 362 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.62, 0.2400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_362.TILE_ID, "walkable": TileBlueprint_362.WALKABLE, "cost": TileBlueprint_362.MOVEMENT_COST}


class TileBlueprint_363:
    TILE_ID = 363
    NAME = "Biome Tile Pattern #363"
    WALKABLE = True if 363 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.63, 0.2599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_363.TILE_ID, "walkable": TileBlueprint_363.WALKABLE, "cost": TileBlueprint_363.MOVEMENT_COST}


class TileBlueprint_364:
    TILE_ID = 364
    NAME = "Biome Tile Pattern #364"
    WALKABLE = True if 364 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.64, 0.28000000000000025)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_364.TILE_ID, "walkable": TileBlueprint_364.WALKABLE, "cost": TileBlueprint_364.MOVEMENT_COST}


class TileBlueprint_365:
    TILE_ID = 365
    NAME = "Biome Tile Pattern #365"
    WALKABLE = True if 365 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.65, 0.2999999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_365.TILE_ID, "walkable": TileBlueprint_365.WALKABLE, "cost": TileBlueprint_365.MOVEMENT_COST}


class TileBlueprint_366:
    TILE_ID = 366
    NAME = "Biome Tile Pattern #366"
    WALKABLE = True if 366 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.66, 0.3200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_366.TILE_ID, "walkable": TileBlueprint_366.WALKABLE, "cost": TileBlueprint_366.MOVEMENT_COST}


class TileBlueprint_367:
    TILE_ID = 367
    NAME = "Biome Tile Pattern #367"
    WALKABLE = True if 367 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.67, 0.33999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_367.TILE_ID, "walkable": TileBlueprint_367.WALKABLE, "cost": TileBlueprint_367.MOVEMENT_COST}


class TileBlueprint_368:
    TILE_ID = 368
    NAME = "Biome Tile Pattern #368"
    WALKABLE = True if 368 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.68, 0.3600000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_368.TILE_ID, "walkable": TileBlueprint_368.WALKABLE, "cost": TileBlueprint_368.MOVEMENT_COST}


class TileBlueprint_369:
    TILE_ID = 369
    NAME = "Biome Tile Pattern #369"
    WALKABLE = True if 369 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.69, 0.3799999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_369.TILE_ID, "walkable": TileBlueprint_369.WALKABLE, "cost": TileBlueprint_369.MOVEMENT_COST}


class TileBlueprint_370:
    TILE_ID = 370
    NAME = "Biome Tile Pattern #370"
    WALKABLE = True if 370 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.7, 0.40000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_370.TILE_ID, "walkable": TileBlueprint_370.WALKABLE, "cost": TileBlueprint_370.MOVEMENT_COST}


class TileBlueprint_371:
    TILE_ID = 371
    NAME = "Biome Tile Pattern #371"
    WALKABLE = True if 371 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.71, 0.41999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_371.TILE_ID, "walkable": TileBlueprint_371.WALKABLE, "cost": TileBlueprint_371.MOVEMENT_COST}


class TileBlueprint_372:
    TILE_ID = 372
    NAME = "Biome Tile Pattern #372"
    WALKABLE = True if 372 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.72, 0.4400000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_372.TILE_ID, "walkable": TileBlueprint_372.WALKABLE, "cost": TileBlueprint_372.MOVEMENT_COST}


class TileBlueprint_373:
    TILE_ID = 373
    NAME = "Biome Tile Pattern #373"
    WALKABLE = True if 373 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.73, 0.45999999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_373.TILE_ID, "walkable": TileBlueprint_373.WALKABLE, "cost": TileBlueprint_373.MOVEMENT_COST}


class TileBlueprint_374:
    TILE_ID = 374
    NAME = "Biome Tile Pattern #374"
    WALKABLE = True if 374 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.74, 0.4800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_374.TILE_ID, "walkable": TileBlueprint_374.WALKABLE, "cost": TileBlueprint_374.MOVEMENT_COST}


class TileBlueprint_375:
    TILE_ID = 375
    NAME = "Biome Tile Pattern #375"
    WALKABLE = True if 375 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.75, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_375.TILE_ID, "walkable": TileBlueprint_375.WALKABLE, "cost": TileBlueprint_375.MOVEMENT_COST}


class TileBlueprint_376:
    TILE_ID = 376
    NAME = "Biome Tile Pattern #376"
    WALKABLE = True if 376 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.7600000000000002, 0.5200000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_376.TILE_ID, "walkable": TileBlueprint_376.WALKABLE, "cost": TileBlueprint_376.MOVEMENT_COST}


class TileBlueprint_377:
    TILE_ID = 377
    NAME = "Biome Tile Pattern #377"
    WALKABLE = True if 377 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.77, 0.54)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_377.TILE_ID, "walkable": TileBlueprint_377.WALKABLE, "cost": TileBlueprint_377.MOVEMENT_COST}


class TileBlueprint_378:
    TILE_ID = 378
    NAME = "Biome Tile Pattern #378"
    WALKABLE = True if 378 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.7800000000000002, 0.5600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_378.TILE_ID, "walkable": TileBlueprint_378.WALKABLE, "cost": TileBlueprint_378.MOVEMENT_COST}


class TileBlueprint_379:
    TILE_ID = 379
    NAME = "Biome Tile Pattern #379"
    WALKABLE = True if 379 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.79, 0.5800000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_379.TILE_ID, "walkable": TileBlueprint_379.WALKABLE, "cost": TileBlueprint_379.MOVEMENT_COST}


class TileBlueprint_380:
    TILE_ID = 380
    NAME = "Biome Tile Pattern #380"
    WALKABLE = True if 380 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.8000000000000003, 0.6000000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_380.TILE_ID, "walkable": TileBlueprint_380.WALKABLE, "cost": TileBlueprint_380.MOVEMENT_COST}


class TileBlueprint_381:
    TILE_ID = 381
    NAME = "Biome Tile Pattern #381"
    WALKABLE = True if 381 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.81, 0.6200000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_381.TILE_ID, "walkable": TileBlueprint_381.WALKABLE, "cost": TileBlueprint_381.MOVEMENT_COST}


class TileBlueprint_382:
    TILE_ID = 382
    NAME = "Biome Tile Pattern #382"
    WALKABLE = True if 382 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.8200000000000003, 0.6400000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_382.TILE_ID, "walkable": TileBlueprint_382.WALKABLE, "cost": TileBlueprint_382.MOVEMENT_COST}


class TileBlueprint_383:
    TILE_ID = 383
    NAME = "Biome Tile Pattern #383"
    WALKABLE = True if 383 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.83, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_383.TILE_ID, "walkable": TileBlueprint_383.WALKABLE, "cost": TileBlueprint_383.MOVEMENT_COST}


class TileBlueprint_384:
    TILE_ID = 384
    NAME = "Biome Tile Pattern #384"
    WALKABLE = True if 384 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.84, 0.6799999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_384.TILE_ID, "walkable": TileBlueprint_384.WALKABLE, "cost": TileBlueprint_384.MOVEMENT_COST}


class TileBlueprint_385:
    TILE_ID = 385
    NAME = "Biome Tile Pattern #385"
    WALKABLE = True if 385 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.85, 0.7000000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_385.TILE_ID, "walkable": TileBlueprint_385.WALKABLE, "cost": TileBlueprint_385.MOVEMENT_COST}


class TileBlueprint_386:
    TILE_ID = 386
    NAME = "Biome Tile Pattern #386"
    WALKABLE = True if 386 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.86, 0.7199999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_386.TILE_ID, "walkable": TileBlueprint_386.WALKABLE, "cost": TileBlueprint_386.MOVEMENT_COST}


class TileBlueprint_387:
    TILE_ID = 387
    NAME = "Biome Tile Pattern #387"
    WALKABLE = True if 387 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.87, 0.7400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_387.TILE_ID, "walkable": TileBlueprint_387.WALKABLE, "cost": TileBlueprint_387.MOVEMENT_COST}


class TileBlueprint_388:
    TILE_ID = 388
    NAME = "Biome Tile Pattern #388"
    WALKABLE = True if 388 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.88, 0.7599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_388.TILE_ID, "walkable": TileBlueprint_388.WALKABLE, "cost": TileBlueprint_388.MOVEMENT_COST}


class TileBlueprint_389:
    TILE_ID = 389
    NAME = "Biome Tile Pattern #389"
    WALKABLE = True if 389 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.89, 0.7800000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_389.TILE_ID, "walkable": TileBlueprint_389.WALKABLE, "cost": TileBlueprint_389.MOVEMENT_COST}


class TileBlueprint_390:
    TILE_ID = 390
    NAME = "Biome Tile Pattern #390"
    WALKABLE = True if 390 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.9, 0.7999999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_390.TILE_ID, "walkable": TileBlueprint_390.WALKABLE, "cost": TileBlueprint_390.MOVEMENT_COST}


class TileBlueprint_391:
    TILE_ID = 391
    NAME = "Biome Tile Pattern #391"
    WALKABLE = True if 391 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.91, 0.8200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_391.TILE_ID, "walkable": TileBlueprint_391.WALKABLE, "cost": TileBlueprint_391.MOVEMENT_COST}


class TileBlueprint_392:
    TILE_ID = 392
    NAME = "Biome Tile Pattern #392"
    WALKABLE = True if 392 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.92, 0.8399999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_392.TILE_ID, "walkable": TileBlueprint_392.WALKABLE, "cost": TileBlueprint_392.MOVEMENT_COST}


class TileBlueprint_393:
    TILE_ID = 393
    NAME = "Biome Tile Pattern #393"
    WALKABLE = True if 393 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.93, 0.8600000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_393.TILE_ID, "walkable": TileBlueprint_393.WALKABLE, "cost": TileBlueprint_393.MOVEMENT_COST}


class TileBlueprint_394:
    TILE_ID = 394
    NAME = "Biome Tile Pattern #394"
    WALKABLE = True if 394 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.94, 0.8799999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_394.TILE_ID, "walkable": TileBlueprint_394.WALKABLE, "cost": TileBlueprint_394.MOVEMENT_COST}


class TileBlueprint_395:
    TILE_ID = 395
    NAME = "Biome Tile Pattern #395"
    WALKABLE = True if 395 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (3.95, 0.9000000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_395.TILE_ID, "walkable": TileBlueprint_395.WALKABLE, "cost": TileBlueprint_395.MOVEMENT_COST}


class TileBlueprint_396:
    TILE_ID = 396
    NAME = "Biome Tile Pattern #396"
    WALKABLE = True if 396 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (3.96, 0.9199999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_396.TILE_ID, "walkable": TileBlueprint_396.WALKABLE, "cost": TileBlueprint_396.MOVEMENT_COST}


class TileBlueprint_397:
    TILE_ID = 397
    NAME = "Biome Tile Pattern #397"
    WALKABLE = True if 397 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (3.97, 0.9400000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_397.TILE_ID, "walkable": TileBlueprint_397.WALKABLE, "cost": TileBlueprint_397.MOVEMENT_COST}


class TileBlueprint_398:
    TILE_ID = 398
    NAME = "Biome Tile Pattern #398"
    WALKABLE = True if 398 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (3.98, 0.96)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_398.TILE_ID, "walkable": TileBlueprint_398.WALKABLE, "cost": TileBlueprint_398.MOVEMENT_COST}


class TileBlueprint_399:
    TILE_ID = 399
    NAME = "Biome Tile Pattern #399"
    WALKABLE = True if 399 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (3.99, 0.9800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_399.TILE_ID, "walkable": TileBlueprint_399.WALKABLE, "cost": TileBlueprint_399.MOVEMENT_COST}


class TileBlueprint_400:
    TILE_ID = 400
    NAME = "Biome Tile Pattern #400"
    WALKABLE = True if 400 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.0, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_400.TILE_ID, "walkable": TileBlueprint_400.WALKABLE, "cost": TileBlueprint_400.MOVEMENT_COST}


class TileBlueprint_401:
    TILE_ID = 401
    NAME = "Biome Tile Pattern #401"
    WALKABLE = True if 401 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.01, 0.019999999999999574)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_401.TILE_ID, "walkable": TileBlueprint_401.WALKABLE, "cost": TileBlueprint_401.MOVEMENT_COST}


class TileBlueprint_402:
    TILE_ID = 402
    NAME = "Biome Tile Pattern #402"
    WALKABLE = True if 402 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.0200000000000005, 0.040000000000000924)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_402.TILE_ID, "walkable": TileBlueprint_402.WALKABLE, "cost": TileBlueprint_402.MOVEMENT_COST}


class TileBlueprint_403:
    TILE_ID = 403
    NAME = "Biome Tile Pattern #403"
    WALKABLE = True if 403 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.03, 0.0600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_403.TILE_ID, "walkable": TileBlueprint_403.WALKABLE, "cost": TileBlueprint_403.MOVEMENT_COST}


class TileBlueprint_404:
    TILE_ID = 404
    NAME = "Biome Tile Pattern #404"
    WALKABLE = True if 404 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.04, 0.08000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_404.TILE_ID, "walkable": TileBlueprint_404.WALKABLE, "cost": TileBlueprint_404.MOVEMENT_COST}


class TileBlueprint_405:
    TILE_ID = 405
    NAME = "Biome Tile Pattern #405"
    WALKABLE = True if 405 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.05, 0.09999999999999964)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_405.TILE_ID, "walkable": TileBlueprint_405.WALKABLE, "cost": TileBlueprint_405.MOVEMENT_COST}


class TileBlueprint_406:
    TILE_ID = 406
    NAME = "Biome Tile Pattern #406"
    WALKABLE = True if 406 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.0600000000000005, 0.120000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_406.TILE_ID, "walkable": TileBlueprint_406.WALKABLE, "cost": TileBlueprint_406.MOVEMENT_COST}


class TileBlueprint_407:
    TILE_ID = 407
    NAME = "Biome Tile Pattern #407"
    WALKABLE = True if 407 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.07, 0.14000000000000057)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_407.TILE_ID, "walkable": TileBlueprint_407.WALKABLE, "cost": TileBlueprint_407.MOVEMENT_COST}


class TileBlueprint_408:
    TILE_ID = 408
    NAME = "Biome Tile Pattern #408"
    WALKABLE = True if 408 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.08, 0.16000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_408.TILE_ID, "walkable": TileBlueprint_408.WALKABLE, "cost": TileBlueprint_408.MOVEMENT_COST}


class TileBlueprint_409:
    TILE_ID = 409
    NAME = "Biome Tile Pattern #409"
    WALKABLE = True if 409 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.09, 0.17999999999999972)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_409.TILE_ID, "walkable": TileBlueprint_409.WALKABLE, "cost": TileBlueprint_409.MOVEMENT_COST}


class TileBlueprint_410:
    TILE_ID = 410
    NAME = "Biome Tile Pattern #410"
    WALKABLE = True if 410 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.1, 0.1999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_410.TILE_ID, "walkable": TileBlueprint_410.WALKABLE, "cost": TileBlueprint_410.MOVEMENT_COST}


class TileBlueprint_411:
    TILE_ID = 411
    NAME = "Biome Tile Pattern #411"
    WALKABLE = True if 411 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.11, 0.22000000000000064)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_411.TILE_ID, "walkable": TileBlueprint_411.WALKABLE, "cost": TileBlueprint_411.MOVEMENT_COST}


class TileBlueprint_412:
    TILE_ID = 412
    NAME = "Biome Tile Pattern #412"
    WALKABLE = True if 412 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.12, 0.2400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_412.TILE_ID, "walkable": TileBlueprint_412.WALKABLE, "cost": TileBlueprint_412.MOVEMENT_COST}


class TileBlueprint_413:
    TILE_ID = 413
    NAME = "Biome Tile Pattern #413"
    WALKABLE = True if 413 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.13, 0.2599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_413.TILE_ID, "walkable": TileBlueprint_413.WALKABLE, "cost": TileBlueprint_413.MOVEMENT_COST}


class TileBlueprint_414:
    TILE_ID = 414
    NAME = "Biome Tile Pattern #414"
    WALKABLE = True if 414 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.14, 0.27999999999999936)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_414.TILE_ID, "walkable": TileBlueprint_414.WALKABLE, "cost": TileBlueprint_414.MOVEMENT_COST}


class TileBlueprint_415:
    TILE_ID = 415
    NAME = "Biome Tile Pattern #415"
    WALKABLE = True if 415 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.15, 0.3000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_415.TILE_ID, "walkable": TileBlueprint_415.WALKABLE, "cost": TileBlueprint_415.MOVEMENT_COST}


class TileBlueprint_416:
    TILE_ID = 416
    NAME = "Biome Tile Pattern #416"
    WALKABLE = True if 416 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.16, 0.3200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_416.TILE_ID, "walkable": TileBlueprint_416.WALKABLE, "cost": TileBlueprint_416.MOVEMENT_COST}


class TileBlueprint_417:
    TILE_ID = 417
    NAME = "Biome Tile Pattern #417"
    WALKABLE = True if 417 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.17, 0.33999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_417.TILE_ID, "walkable": TileBlueprint_417.WALKABLE, "cost": TileBlueprint_417.MOVEMENT_COST}


class TileBlueprint_418:
    TILE_ID = 418
    NAME = "Biome Tile Pattern #418"
    WALKABLE = True if 418 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.18, 0.35999999999999943)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_418.TILE_ID, "walkable": TileBlueprint_418.WALKABLE, "cost": TileBlueprint_418.MOVEMENT_COST}


class TileBlueprint_419:
    TILE_ID = 419
    NAME = "Biome Tile Pattern #419"
    WALKABLE = True if 419 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.19, 0.3800000000000008)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_419.TILE_ID, "walkable": TileBlueprint_419.WALKABLE, "cost": TileBlueprint_419.MOVEMENT_COST}


class TileBlueprint_420:
    TILE_ID = 420
    NAME = "Biome Tile Pattern #420"
    WALKABLE = True if 420 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.2, 0.40000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_420.TILE_ID, "walkable": TileBlueprint_420.WALKABLE, "cost": TileBlueprint_420.MOVEMENT_COST}


class TileBlueprint_421:
    TILE_ID = 421
    NAME = "Biome Tile Pattern #421"
    WALKABLE = True if 421 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.21, 0.41999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_421.TILE_ID, "walkable": TileBlueprint_421.WALKABLE, "cost": TileBlueprint_421.MOVEMENT_COST}


class TileBlueprint_422:
    TILE_ID = 422
    NAME = "Biome Tile Pattern #422"
    WALKABLE = True if 422 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.22, 0.4399999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_422.TILE_ID, "walkable": TileBlueprint_422.WALKABLE, "cost": TileBlueprint_422.MOVEMENT_COST}


class TileBlueprint_423:
    TILE_ID = 423
    NAME = "Biome Tile Pattern #423"
    WALKABLE = True if 423 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.23, 0.46000000000000085)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_423.TILE_ID, "walkable": TileBlueprint_423.WALKABLE, "cost": TileBlueprint_423.MOVEMENT_COST}


class TileBlueprint_424:
    TILE_ID = 424
    NAME = "Biome Tile Pattern #424"
    WALKABLE = True if 424 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.24, 0.4800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_424.TILE_ID, "walkable": TileBlueprint_424.WALKABLE, "cost": TileBlueprint_424.MOVEMENT_COST}


class TileBlueprint_425:
    TILE_ID = 425
    NAME = "Biome Tile Pattern #425"
    WALKABLE = True if 425 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.25, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_425.TILE_ID, "walkable": TileBlueprint_425.WALKABLE, "cost": TileBlueprint_425.MOVEMENT_COST}


class TileBlueprint_426:
    TILE_ID = 426
    NAME = "Biome Tile Pattern #426"
    WALKABLE = True if 426 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.26, 0.5199999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_426.TILE_ID, "walkable": TileBlueprint_426.WALKABLE, "cost": TileBlueprint_426.MOVEMENT_COST}


class TileBlueprint_427:
    TILE_ID = 427
    NAME = "Biome Tile Pattern #427"
    WALKABLE = True if 427 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.2700000000000005, 0.5400000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_427.TILE_ID, "walkable": TileBlueprint_427.WALKABLE, "cost": TileBlueprint_427.MOVEMENT_COST}


class TileBlueprint_428:
    TILE_ID = 428
    NAME = "Biome Tile Pattern #428"
    WALKABLE = True if 428 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.28, 0.5600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_428.TILE_ID, "walkable": TileBlueprint_428.WALKABLE, "cost": TileBlueprint_428.MOVEMENT_COST}


class TileBlueprint_429:
    TILE_ID = 429
    NAME = "Biome Tile Pattern #429"
    WALKABLE = True if 429 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.29, 0.5800000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_429.TILE_ID, "walkable": TileBlueprint_429.WALKABLE, "cost": TileBlueprint_429.MOVEMENT_COST}


class TileBlueprint_430:
    TILE_ID = 430
    NAME = "Biome Tile Pattern #430"
    WALKABLE = True if 430 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.3, 0.5999999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_430.TILE_ID, "walkable": TileBlueprint_430.WALKABLE, "cost": TileBlueprint_430.MOVEMENT_COST}


class TileBlueprint_431:
    TILE_ID = 431
    NAME = "Biome Tile Pattern #431"
    WALKABLE = True if 431 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.3100000000000005, 0.620000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_431.TILE_ID, "walkable": TileBlueprint_431.WALKABLE, "cost": TileBlueprint_431.MOVEMENT_COST}


class TileBlueprint_432:
    TILE_ID = 432
    NAME = "Biome Tile Pattern #432"
    WALKABLE = True if 432 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.32, 0.6400000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_432.TILE_ID, "walkable": TileBlueprint_432.WALKABLE, "cost": TileBlueprint_432.MOVEMENT_COST}


class TileBlueprint_433:
    TILE_ID = 433
    NAME = "Biome Tile Pattern #433"
    WALKABLE = True if 433 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.33, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_433.TILE_ID, "walkable": TileBlueprint_433.WALKABLE, "cost": TileBlueprint_433.MOVEMENT_COST}


class TileBlueprint_434:
    TILE_ID = 434
    NAME = "Biome Tile Pattern #434"
    WALKABLE = True if 434 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.34, 0.6799999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_434.TILE_ID, "walkable": TileBlueprint_434.WALKABLE, "cost": TileBlueprint_434.MOVEMENT_COST}


class TileBlueprint_435:
    TILE_ID = 435
    NAME = "Biome Tile Pattern #435"
    WALKABLE = True if 435 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.3500000000000005, 0.7000000000000011)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_435.TILE_ID, "walkable": TileBlueprint_435.WALKABLE, "cost": TileBlueprint_435.MOVEMENT_COST}


class TileBlueprint_436:
    TILE_ID = 436
    NAME = "Biome Tile Pattern #436"
    WALKABLE = True if 436 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.36, 0.7200000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_436.TILE_ID, "walkable": TileBlueprint_436.WALKABLE, "cost": TileBlueprint_436.MOVEMENT_COST}


class TileBlueprint_437:
    TILE_ID = 437
    NAME = "Biome Tile Pattern #437"
    WALKABLE = True if 437 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.37, 0.7400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_437.TILE_ID, "walkable": TileBlueprint_437.WALKABLE, "cost": TileBlueprint_437.MOVEMENT_COST}


class TileBlueprint_438:
    TILE_ID = 438
    NAME = "Biome Tile Pattern #438"
    WALKABLE = True if 438 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.38, 0.7599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_438.TILE_ID, "walkable": TileBlueprint_438.WALKABLE, "cost": TileBlueprint_438.MOVEMENT_COST}


class TileBlueprint_439:
    TILE_ID = 439
    NAME = "Biome Tile Pattern #439"
    WALKABLE = True if 439 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.39, 0.7799999999999994)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_439.TILE_ID, "walkable": TileBlueprint_439.WALKABLE, "cost": TileBlueprint_439.MOVEMENT_COST}


class TileBlueprint_440:
    TILE_ID = 440
    NAME = "Biome Tile Pattern #440"
    WALKABLE = True if 440 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.4, 0.8000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_440.TILE_ID, "walkable": TileBlueprint_440.WALKABLE, "cost": TileBlueprint_440.MOVEMENT_COST}


class TileBlueprint_441:
    TILE_ID = 441
    NAME = "Biome Tile Pattern #441"
    WALKABLE = True if 441 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.41, 0.8200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_441.TILE_ID, "walkable": TileBlueprint_441.WALKABLE, "cost": TileBlueprint_441.MOVEMENT_COST}


class TileBlueprint_442:
    TILE_ID = 442
    NAME = "Biome Tile Pattern #442"
    WALKABLE = True if 442 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.42, 0.8399999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_442.TILE_ID, "walkable": TileBlueprint_442.WALKABLE, "cost": TileBlueprint_442.MOVEMENT_COST}


class TileBlueprint_443:
    TILE_ID = 443
    NAME = "Biome Tile Pattern #443"
    WALKABLE = True if 443 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.43, 0.8599999999999994)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_443.TILE_ID, "walkable": TileBlueprint_443.WALKABLE, "cost": TileBlueprint_443.MOVEMENT_COST}


class TileBlueprint_444:
    TILE_ID = 444
    NAME = "Biome Tile Pattern #444"
    WALKABLE = True if 444 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.44, 0.8800000000000008)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_444.TILE_ID, "walkable": TileBlueprint_444.WALKABLE, "cost": TileBlueprint_444.MOVEMENT_COST}


class TileBlueprint_445:
    TILE_ID = 445
    NAME = "Biome Tile Pattern #445"
    WALKABLE = True if 445 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.45, 0.9000000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_445.TILE_ID, "walkable": TileBlueprint_445.WALKABLE, "cost": TileBlueprint_445.MOVEMENT_COST}


class TileBlueprint_446:
    TILE_ID = 446
    NAME = "Biome Tile Pattern #446"
    WALKABLE = True if 446 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.46, 0.9199999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_446.TILE_ID, "walkable": TileBlueprint_446.WALKABLE, "cost": TileBlueprint_446.MOVEMENT_COST}


class TileBlueprint_447:
    TILE_ID = 447
    NAME = "Biome Tile Pattern #447"
    WALKABLE = True if 447 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.47, 0.9399999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_447.TILE_ID, "walkable": TileBlueprint_447.WALKABLE, "cost": TileBlueprint_447.MOVEMENT_COST}


class TileBlueprint_448:
    TILE_ID = 448
    NAME = "Biome Tile Pattern #448"
    WALKABLE = True if 448 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.48, 0.9600000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_448.TILE_ID, "walkable": TileBlueprint_448.WALKABLE, "cost": TileBlueprint_448.MOVEMENT_COST}


class TileBlueprint_449:
    TILE_ID = 449
    NAME = "Biome Tile Pattern #449"
    WALKABLE = True if 449 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.49, 0.9800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_449.TILE_ID, "walkable": TileBlueprint_449.WALKABLE, "cost": TileBlueprint_449.MOVEMENT_COST}


class TileBlueprint_450:
    TILE_ID = 450
    NAME = "Biome Tile Pattern #450"
    WALKABLE = True if 450 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.5, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_450.TILE_ID, "walkable": TileBlueprint_450.WALKABLE, "cost": TileBlueprint_450.MOVEMENT_COST}


class TileBlueprint_451:
    TILE_ID = 451
    NAME = "Biome Tile Pattern #451"
    WALKABLE = True if 451 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.51, 0.019999999999999574)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_451.TILE_ID, "walkable": TileBlueprint_451.WALKABLE, "cost": TileBlueprint_451.MOVEMENT_COST}


class TileBlueprint_452:
    TILE_ID = 452
    NAME = "Biome Tile Pattern #452"
    WALKABLE = True if 452 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.5200000000000005, 0.040000000000000924)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_452.TILE_ID, "walkable": TileBlueprint_452.WALKABLE, "cost": TileBlueprint_452.MOVEMENT_COST}


class TileBlueprint_453:
    TILE_ID = 453
    NAME = "Biome Tile Pattern #453"
    WALKABLE = True if 453 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.53, 0.0600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_453.TILE_ID, "walkable": TileBlueprint_453.WALKABLE, "cost": TileBlueprint_453.MOVEMENT_COST}


class TileBlueprint_454:
    TILE_ID = 454
    NAME = "Biome Tile Pattern #454"
    WALKABLE = True if 454 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.54, 0.08000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_454.TILE_ID, "walkable": TileBlueprint_454.WALKABLE, "cost": TileBlueprint_454.MOVEMENT_COST}


class TileBlueprint_455:
    TILE_ID = 455
    NAME = "Biome Tile Pattern #455"
    WALKABLE = True if 455 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.55, 0.09999999999999964)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_455.TILE_ID, "walkable": TileBlueprint_455.WALKABLE, "cost": TileBlueprint_455.MOVEMENT_COST}


class TileBlueprint_456:
    TILE_ID = 456
    NAME = "Biome Tile Pattern #456"
    WALKABLE = True if 456 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.5600000000000005, 0.120000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_456.TILE_ID, "walkable": TileBlueprint_456.WALKABLE, "cost": TileBlueprint_456.MOVEMENT_COST}


class TileBlueprint_457:
    TILE_ID = 457
    NAME = "Biome Tile Pattern #457"
    WALKABLE = True if 457 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.57, 0.14000000000000057)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_457.TILE_ID, "walkable": TileBlueprint_457.WALKABLE, "cost": TileBlueprint_457.MOVEMENT_COST}


class TileBlueprint_458:
    TILE_ID = 458
    NAME = "Biome Tile Pattern #458"
    WALKABLE = True if 458 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.58, 0.16000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_458.TILE_ID, "walkable": TileBlueprint_458.WALKABLE, "cost": TileBlueprint_458.MOVEMENT_COST}


class TileBlueprint_459:
    TILE_ID = 459
    NAME = "Biome Tile Pattern #459"
    WALKABLE = True if 459 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.59, 0.17999999999999972)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_459.TILE_ID, "walkable": TileBlueprint_459.WALKABLE, "cost": TileBlueprint_459.MOVEMENT_COST}


class TileBlueprint_460:
    TILE_ID = 460
    NAME = "Biome Tile Pattern #460"
    WALKABLE = True if 460 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.6000000000000005, 0.20000000000000107)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_460.TILE_ID, "walkable": TileBlueprint_460.WALKABLE, "cost": TileBlueprint_460.MOVEMENT_COST}


class TileBlueprint_461:
    TILE_ID = 461
    NAME = "Biome Tile Pattern #461"
    WALKABLE = True if 461 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.61, 0.22000000000000064)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_461.TILE_ID, "walkable": TileBlueprint_461.WALKABLE, "cost": TileBlueprint_461.MOVEMENT_COST}


class TileBlueprint_462:
    TILE_ID = 462
    NAME = "Biome Tile Pattern #462"
    WALKABLE = True if 462 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.62, 0.2400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_462.TILE_ID, "walkable": TileBlueprint_462.WALKABLE, "cost": TileBlueprint_462.MOVEMENT_COST}


class TileBlueprint_463:
    TILE_ID = 463
    NAME = "Biome Tile Pattern #463"
    WALKABLE = True if 463 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.63, 0.2599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_463.TILE_ID, "walkable": TileBlueprint_463.WALKABLE, "cost": TileBlueprint_463.MOVEMENT_COST}


class TileBlueprint_464:
    TILE_ID = 464
    NAME = "Biome Tile Pattern #464"
    WALKABLE = True if 464 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.64, 0.27999999999999936)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_464.TILE_ID, "walkable": TileBlueprint_464.WALKABLE, "cost": TileBlueprint_464.MOVEMENT_COST}


class TileBlueprint_465:
    TILE_ID = 465
    NAME = "Biome Tile Pattern #465"
    WALKABLE = True if 465 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.65, 0.3000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_465.TILE_ID, "walkable": TileBlueprint_465.WALKABLE, "cost": TileBlueprint_465.MOVEMENT_COST}


class TileBlueprint_466:
    TILE_ID = 466
    NAME = "Biome Tile Pattern #466"
    WALKABLE = True if 466 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.66, 0.3200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_466.TILE_ID, "walkable": TileBlueprint_466.WALKABLE, "cost": TileBlueprint_466.MOVEMENT_COST}


class TileBlueprint_467:
    TILE_ID = 467
    NAME = "Biome Tile Pattern #467"
    WALKABLE = True if 467 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.67, 0.33999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_467.TILE_ID, "walkable": TileBlueprint_467.WALKABLE, "cost": TileBlueprint_467.MOVEMENT_COST}


class TileBlueprint_468:
    TILE_ID = 468
    NAME = "Biome Tile Pattern #468"
    WALKABLE = True if 468 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.68, 0.35999999999999943)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_468.TILE_ID, "walkable": TileBlueprint_468.WALKABLE, "cost": TileBlueprint_468.MOVEMENT_COST}


class TileBlueprint_469:
    TILE_ID = 469
    NAME = "Biome Tile Pattern #469"
    WALKABLE = True if 469 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.69, 0.3800000000000008)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_469.TILE_ID, "walkable": TileBlueprint_469.WALKABLE, "cost": TileBlueprint_469.MOVEMENT_COST}


class TileBlueprint_470:
    TILE_ID = 470
    NAME = "Biome Tile Pattern #470"
    WALKABLE = True if 470 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.7, 0.40000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_470.TILE_ID, "walkable": TileBlueprint_470.WALKABLE, "cost": TileBlueprint_470.MOVEMENT_COST}


class TileBlueprint_471:
    TILE_ID = 471
    NAME = "Biome Tile Pattern #471"
    WALKABLE = True if 471 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.71, 0.41999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_471.TILE_ID, "walkable": TileBlueprint_471.WALKABLE, "cost": TileBlueprint_471.MOVEMENT_COST}


class TileBlueprint_472:
    TILE_ID = 472
    NAME = "Biome Tile Pattern #472"
    WALKABLE = True if 472 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.72, 0.4399999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_472.TILE_ID, "walkable": TileBlueprint_472.WALKABLE, "cost": TileBlueprint_472.MOVEMENT_COST}


class TileBlueprint_473:
    TILE_ID = 473
    NAME = "Biome Tile Pattern #473"
    WALKABLE = True if 473 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.73, 0.46000000000000085)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_473.TILE_ID, "walkable": TileBlueprint_473.WALKABLE, "cost": TileBlueprint_473.MOVEMENT_COST}


class TileBlueprint_474:
    TILE_ID = 474
    NAME = "Biome Tile Pattern #474"
    WALKABLE = True if 474 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.74, 0.4800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_474.TILE_ID, "walkable": TileBlueprint_474.WALKABLE, "cost": TileBlueprint_474.MOVEMENT_COST}


class TileBlueprint_475:
    TILE_ID = 475
    NAME = "Biome Tile Pattern #475"
    WALKABLE = True if 475 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.75, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_475.TILE_ID, "walkable": TileBlueprint_475.WALKABLE, "cost": TileBlueprint_475.MOVEMENT_COST}


class TileBlueprint_476:
    TILE_ID = 476
    NAME = "Biome Tile Pattern #476"
    WALKABLE = True if 476 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.76, 0.5199999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_476.TILE_ID, "walkable": TileBlueprint_476.WALKABLE, "cost": TileBlueprint_476.MOVEMENT_COST}


class TileBlueprint_477:
    TILE_ID = 477
    NAME = "Biome Tile Pattern #477"
    WALKABLE = True if 477 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.7700000000000005, 0.5400000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_477.TILE_ID, "walkable": TileBlueprint_477.WALKABLE, "cost": TileBlueprint_477.MOVEMENT_COST}


class TileBlueprint_478:
    TILE_ID = 478
    NAME = "Biome Tile Pattern #478"
    WALKABLE = True if 478 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.78, 0.5600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_478.TILE_ID, "walkable": TileBlueprint_478.WALKABLE, "cost": TileBlueprint_478.MOVEMENT_COST}


class TileBlueprint_479:
    TILE_ID = 479
    NAME = "Biome Tile Pattern #479"
    WALKABLE = True if 479 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.79, 0.5800000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_479.TILE_ID, "walkable": TileBlueprint_479.WALKABLE, "cost": TileBlueprint_479.MOVEMENT_COST}


class TileBlueprint_480:
    TILE_ID = 480
    NAME = "Biome Tile Pattern #480"
    WALKABLE = True if 480 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.8, 0.5999999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_480.TILE_ID, "walkable": TileBlueprint_480.WALKABLE, "cost": TileBlueprint_480.MOVEMENT_COST}


class TileBlueprint_481:
    TILE_ID = 481
    NAME = "Biome Tile Pattern #481"
    WALKABLE = True if 481 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.8100000000000005, 0.620000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_481.TILE_ID, "walkable": TileBlueprint_481.WALKABLE, "cost": TileBlueprint_481.MOVEMENT_COST}


class TileBlueprint_482:
    TILE_ID = 482
    NAME = "Biome Tile Pattern #482"
    WALKABLE = True if 482 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.82, 0.6400000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_482.TILE_ID, "walkable": TileBlueprint_482.WALKABLE, "cost": TileBlueprint_482.MOVEMENT_COST}


class TileBlueprint_483:
    TILE_ID = 483
    NAME = "Biome Tile Pattern #483"
    WALKABLE = True if 483 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.83, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_483.TILE_ID, "walkable": TileBlueprint_483.WALKABLE, "cost": TileBlueprint_483.MOVEMENT_COST}


class TileBlueprint_484:
    TILE_ID = 484
    NAME = "Biome Tile Pattern #484"
    WALKABLE = True if 484 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.84, 0.6799999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_484.TILE_ID, "walkable": TileBlueprint_484.WALKABLE, "cost": TileBlueprint_484.MOVEMENT_COST}


class TileBlueprint_485:
    TILE_ID = 485
    NAME = "Biome Tile Pattern #485"
    WALKABLE = True if 485 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.8500000000000005, 0.7000000000000011)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_485.TILE_ID, "walkable": TileBlueprint_485.WALKABLE, "cost": TileBlueprint_485.MOVEMENT_COST}


class TileBlueprint_486:
    TILE_ID = 486
    NAME = "Biome Tile Pattern #486"
    WALKABLE = True if 486 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.86, 0.7200000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_486.TILE_ID, "walkable": TileBlueprint_486.WALKABLE, "cost": TileBlueprint_486.MOVEMENT_COST}


class TileBlueprint_487:
    TILE_ID = 487
    NAME = "Biome Tile Pattern #487"
    WALKABLE = True if 487 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.87, 0.7400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_487.TILE_ID, "walkable": TileBlueprint_487.WALKABLE, "cost": TileBlueprint_487.MOVEMENT_COST}


class TileBlueprint_488:
    TILE_ID = 488
    NAME = "Biome Tile Pattern #488"
    WALKABLE = True if 488 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.88, 0.7599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_488.TILE_ID, "walkable": TileBlueprint_488.WALKABLE, "cost": TileBlueprint_488.MOVEMENT_COST}


class TileBlueprint_489:
    TILE_ID = 489
    NAME = "Biome Tile Pattern #489"
    WALKABLE = True if 489 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.89, 0.7799999999999994)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_489.TILE_ID, "walkable": TileBlueprint_489.WALKABLE, "cost": TileBlueprint_489.MOVEMENT_COST}


class TileBlueprint_490:
    TILE_ID = 490
    NAME = "Biome Tile Pattern #490"
    WALKABLE = True if 490 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.9, 0.8000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_490.TILE_ID, "walkable": TileBlueprint_490.WALKABLE, "cost": TileBlueprint_490.MOVEMENT_COST}


class TileBlueprint_491:
    TILE_ID = 491
    NAME = "Biome Tile Pattern #491"
    WALKABLE = True if 491 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.91, 0.8200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_491.TILE_ID, "walkable": TileBlueprint_491.WALKABLE, "cost": TileBlueprint_491.MOVEMENT_COST}


class TileBlueprint_492:
    TILE_ID = 492
    NAME = "Biome Tile Pattern #492"
    WALKABLE = True if 492 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.92, 0.8399999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_492.TILE_ID, "walkable": TileBlueprint_492.WALKABLE, "cost": TileBlueprint_492.MOVEMENT_COST}


class TileBlueprint_493:
    TILE_ID = 493
    NAME = "Biome Tile Pattern #493"
    WALKABLE = True if 493 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.93, 0.8599999999999994)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_493.TILE_ID, "walkable": TileBlueprint_493.WALKABLE, "cost": TileBlueprint_493.MOVEMENT_COST}


class TileBlueprint_494:
    TILE_ID = 494
    NAME = "Biome Tile Pattern #494"
    WALKABLE = True if 494 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.94, 0.8800000000000008)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_494.TILE_ID, "walkable": TileBlueprint_494.WALKABLE, "cost": TileBlueprint_494.MOVEMENT_COST}


class TileBlueprint_495:
    TILE_ID = 495
    NAME = "Biome Tile Pattern #495"
    WALKABLE = True if 495 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (4.95, 0.9000000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_495.TILE_ID, "walkable": TileBlueprint_495.WALKABLE, "cost": TileBlueprint_495.MOVEMENT_COST}


class TileBlueprint_496:
    TILE_ID = 496
    NAME = "Biome Tile Pattern #496"
    WALKABLE = True if 496 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (4.96, 0.9199999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_496.TILE_ID, "walkable": TileBlueprint_496.WALKABLE, "cost": TileBlueprint_496.MOVEMENT_COST}


class TileBlueprint_497:
    TILE_ID = 497
    NAME = "Biome Tile Pattern #497"
    WALKABLE = True if 497 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (4.97, 0.9399999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_497.TILE_ID, "walkable": TileBlueprint_497.WALKABLE, "cost": TileBlueprint_497.MOVEMENT_COST}


class TileBlueprint_498:
    TILE_ID = 498
    NAME = "Biome Tile Pattern #498"
    WALKABLE = True if 498 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (4.98, 0.9600000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_498.TILE_ID, "walkable": TileBlueprint_498.WALKABLE, "cost": TileBlueprint_498.MOVEMENT_COST}


class TileBlueprint_499:
    TILE_ID = 499
    NAME = "Biome Tile Pattern #499"
    WALKABLE = True if 499 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (4.99, 0.9800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_499.TILE_ID, "walkable": TileBlueprint_499.WALKABLE, "cost": TileBlueprint_499.MOVEMENT_COST}


class TileBlueprint_500:
    TILE_ID = 500
    NAME = "Biome Tile Pattern #500"
    WALKABLE = True if 500 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.0, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_500.TILE_ID, "walkable": TileBlueprint_500.WALKABLE, "cost": TileBlueprint_500.MOVEMENT_COST}


class TileBlueprint_501:
    TILE_ID = 501
    NAME = "Biome Tile Pattern #501"
    WALKABLE = True if 501 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.01, 0.019999999999999574)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_501.TILE_ID, "walkable": TileBlueprint_501.WALKABLE, "cost": TileBlueprint_501.MOVEMENT_COST}


class TileBlueprint_502:
    TILE_ID = 502
    NAME = "Biome Tile Pattern #502"
    WALKABLE = True if 502 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.0200000000000005, 0.040000000000000924)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_502.TILE_ID, "walkable": TileBlueprint_502.WALKABLE, "cost": TileBlueprint_502.MOVEMENT_COST}


class TileBlueprint_503:
    TILE_ID = 503
    NAME = "Biome Tile Pattern #503"
    WALKABLE = True if 503 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.03, 0.0600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_503.TILE_ID, "walkable": TileBlueprint_503.WALKABLE, "cost": TileBlueprint_503.MOVEMENT_COST}


class TileBlueprint_504:
    TILE_ID = 504
    NAME = "Biome Tile Pattern #504"
    WALKABLE = True if 504 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.04, 0.08000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_504.TILE_ID, "walkable": TileBlueprint_504.WALKABLE, "cost": TileBlueprint_504.MOVEMENT_COST}


class TileBlueprint_505:
    TILE_ID = 505
    NAME = "Biome Tile Pattern #505"
    WALKABLE = True if 505 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.05, 0.09999999999999964)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_505.TILE_ID, "walkable": TileBlueprint_505.WALKABLE, "cost": TileBlueprint_505.MOVEMENT_COST}


class TileBlueprint_506:
    TILE_ID = 506
    NAME = "Biome Tile Pattern #506"
    WALKABLE = True if 506 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.0600000000000005, 0.120000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_506.TILE_ID, "walkable": TileBlueprint_506.WALKABLE, "cost": TileBlueprint_506.MOVEMENT_COST}


class TileBlueprint_507:
    TILE_ID = 507
    NAME = "Biome Tile Pattern #507"
    WALKABLE = True if 507 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.07, 0.14000000000000057)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_507.TILE_ID, "walkable": TileBlueprint_507.WALKABLE, "cost": TileBlueprint_507.MOVEMENT_COST}


class TileBlueprint_508:
    TILE_ID = 508
    NAME = "Biome Tile Pattern #508"
    WALKABLE = True if 508 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.08, 0.16000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_508.TILE_ID, "walkable": TileBlueprint_508.WALKABLE, "cost": TileBlueprint_508.MOVEMENT_COST}


class TileBlueprint_509:
    TILE_ID = 509
    NAME = "Biome Tile Pattern #509"
    WALKABLE = True if 509 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.09, 0.17999999999999972)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_509.TILE_ID, "walkable": TileBlueprint_509.WALKABLE, "cost": TileBlueprint_509.MOVEMENT_COST}


class TileBlueprint_510:
    TILE_ID = 510
    NAME = "Biome Tile Pattern #510"
    WALKABLE = True if 510 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.1000000000000005, 0.20000000000000107)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_510.TILE_ID, "walkable": TileBlueprint_510.WALKABLE, "cost": TileBlueprint_510.MOVEMENT_COST}


class TileBlueprint_511:
    TILE_ID = 511
    NAME = "Biome Tile Pattern #511"
    WALKABLE = True if 511 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.11, 0.22000000000000064)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_511.TILE_ID, "walkable": TileBlueprint_511.WALKABLE, "cost": TileBlueprint_511.MOVEMENT_COST}


class TileBlueprint_512:
    TILE_ID = 512
    NAME = "Biome Tile Pattern #512"
    WALKABLE = True if 512 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.12, 0.2400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_512.TILE_ID, "walkable": TileBlueprint_512.WALKABLE, "cost": TileBlueprint_512.MOVEMENT_COST}


class TileBlueprint_513:
    TILE_ID = 513
    NAME = "Biome Tile Pattern #513"
    WALKABLE = True if 513 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.13, 0.2599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_513.TILE_ID, "walkable": TileBlueprint_513.WALKABLE, "cost": TileBlueprint_513.MOVEMENT_COST}


class TileBlueprint_514:
    TILE_ID = 514
    NAME = "Biome Tile Pattern #514"
    WALKABLE = True if 514 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.14, 0.27999999999999936)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_514.TILE_ID, "walkable": TileBlueprint_514.WALKABLE, "cost": TileBlueprint_514.MOVEMENT_COST}


class TileBlueprint_515:
    TILE_ID = 515
    NAME = "Biome Tile Pattern #515"
    WALKABLE = True if 515 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.15, 0.3000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_515.TILE_ID, "walkable": TileBlueprint_515.WALKABLE, "cost": TileBlueprint_515.MOVEMENT_COST}


class TileBlueprint_516:
    TILE_ID = 516
    NAME = "Biome Tile Pattern #516"
    WALKABLE = True if 516 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.16, 0.3200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_516.TILE_ID, "walkable": TileBlueprint_516.WALKABLE, "cost": TileBlueprint_516.MOVEMENT_COST}


class TileBlueprint_517:
    TILE_ID = 517
    NAME = "Biome Tile Pattern #517"
    WALKABLE = True if 517 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.17, 0.33999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_517.TILE_ID, "walkable": TileBlueprint_517.WALKABLE, "cost": TileBlueprint_517.MOVEMENT_COST}


class TileBlueprint_518:
    TILE_ID = 518
    NAME = "Biome Tile Pattern #518"
    WALKABLE = True if 518 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.18, 0.35999999999999943)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_518.TILE_ID, "walkable": TileBlueprint_518.WALKABLE, "cost": TileBlueprint_518.MOVEMENT_COST}


class TileBlueprint_519:
    TILE_ID = 519
    NAME = "Biome Tile Pattern #519"
    WALKABLE = True if 519 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.19, 0.3800000000000008)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_519.TILE_ID, "walkable": TileBlueprint_519.WALKABLE, "cost": TileBlueprint_519.MOVEMENT_COST}


class TileBlueprint_520:
    TILE_ID = 520
    NAME = "Biome Tile Pattern #520"
    WALKABLE = True if 520 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.2, 0.40000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_520.TILE_ID, "walkable": TileBlueprint_520.WALKABLE, "cost": TileBlueprint_520.MOVEMENT_COST}


class TileBlueprint_521:
    TILE_ID = 521
    NAME = "Biome Tile Pattern #521"
    WALKABLE = True if 521 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.21, 0.41999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_521.TILE_ID, "walkable": TileBlueprint_521.WALKABLE, "cost": TileBlueprint_521.MOVEMENT_COST}


class TileBlueprint_522:
    TILE_ID = 522
    NAME = "Biome Tile Pattern #522"
    WALKABLE = True if 522 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.22, 0.4399999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_522.TILE_ID, "walkable": TileBlueprint_522.WALKABLE, "cost": TileBlueprint_522.MOVEMENT_COST}


class TileBlueprint_523:
    TILE_ID = 523
    NAME = "Biome Tile Pattern #523"
    WALKABLE = True if 523 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.23, 0.46000000000000085)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_523.TILE_ID, "walkable": TileBlueprint_523.WALKABLE, "cost": TileBlueprint_523.MOVEMENT_COST}


class TileBlueprint_524:
    TILE_ID = 524
    NAME = "Biome Tile Pattern #524"
    WALKABLE = True if 524 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.24, 0.4800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_524.TILE_ID, "walkable": TileBlueprint_524.WALKABLE, "cost": TileBlueprint_524.MOVEMENT_COST}


class TileBlueprint_525:
    TILE_ID = 525
    NAME = "Biome Tile Pattern #525"
    WALKABLE = True if 525 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.25, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_525.TILE_ID, "walkable": TileBlueprint_525.WALKABLE, "cost": TileBlueprint_525.MOVEMENT_COST}


class TileBlueprint_526:
    TILE_ID = 526
    NAME = "Biome Tile Pattern #526"
    WALKABLE = True if 526 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.26, 0.5199999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_526.TILE_ID, "walkable": TileBlueprint_526.WALKABLE, "cost": TileBlueprint_526.MOVEMENT_COST}


class TileBlueprint_527:
    TILE_ID = 527
    NAME = "Biome Tile Pattern #527"
    WALKABLE = True if 527 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.2700000000000005, 0.5400000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_527.TILE_ID, "walkable": TileBlueprint_527.WALKABLE, "cost": TileBlueprint_527.MOVEMENT_COST}


class TileBlueprint_528:
    TILE_ID = 528
    NAME = "Biome Tile Pattern #528"
    WALKABLE = True if 528 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.28, 0.5600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_528.TILE_ID, "walkable": TileBlueprint_528.WALKABLE, "cost": TileBlueprint_528.MOVEMENT_COST}


class TileBlueprint_529:
    TILE_ID = 529
    NAME = "Biome Tile Pattern #529"
    WALKABLE = True if 529 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.29, 0.5800000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_529.TILE_ID, "walkable": TileBlueprint_529.WALKABLE, "cost": TileBlueprint_529.MOVEMENT_COST}


class TileBlueprint_530:
    TILE_ID = 530
    NAME = "Biome Tile Pattern #530"
    WALKABLE = True if 530 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.3, 0.5999999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_530.TILE_ID, "walkable": TileBlueprint_530.WALKABLE, "cost": TileBlueprint_530.MOVEMENT_COST}


class TileBlueprint_531:
    TILE_ID = 531
    NAME = "Biome Tile Pattern #531"
    WALKABLE = True if 531 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.3100000000000005, 0.620000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_531.TILE_ID, "walkable": TileBlueprint_531.WALKABLE, "cost": TileBlueprint_531.MOVEMENT_COST}


class TileBlueprint_532:
    TILE_ID = 532
    NAME = "Biome Tile Pattern #532"
    WALKABLE = True if 532 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.32, 0.6400000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_532.TILE_ID, "walkable": TileBlueprint_532.WALKABLE, "cost": TileBlueprint_532.MOVEMENT_COST}


class TileBlueprint_533:
    TILE_ID = 533
    NAME = "Biome Tile Pattern #533"
    WALKABLE = True if 533 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.33, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_533.TILE_ID, "walkable": TileBlueprint_533.WALKABLE, "cost": TileBlueprint_533.MOVEMENT_COST}


class TileBlueprint_534:
    TILE_ID = 534
    NAME = "Biome Tile Pattern #534"
    WALKABLE = True if 534 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.34, 0.6799999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_534.TILE_ID, "walkable": TileBlueprint_534.WALKABLE, "cost": TileBlueprint_534.MOVEMENT_COST}


class TileBlueprint_535:
    TILE_ID = 535
    NAME = "Biome Tile Pattern #535"
    WALKABLE = True if 535 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.3500000000000005, 0.7000000000000011)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_535.TILE_ID, "walkable": TileBlueprint_535.WALKABLE, "cost": TileBlueprint_535.MOVEMENT_COST}


class TileBlueprint_536:
    TILE_ID = 536
    NAME = "Biome Tile Pattern #536"
    WALKABLE = True if 536 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.36, 0.7200000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_536.TILE_ID, "walkable": TileBlueprint_536.WALKABLE, "cost": TileBlueprint_536.MOVEMENT_COST}


class TileBlueprint_537:
    TILE_ID = 537
    NAME = "Biome Tile Pattern #537"
    WALKABLE = True if 537 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.37, 0.7400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_537.TILE_ID, "walkable": TileBlueprint_537.WALKABLE, "cost": TileBlueprint_537.MOVEMENT_COST}


class TileBlueprint_538:
    TILE_ID = 538
    NAME = "Biome Tile Pattern #538"
    WALKABLE = True if 538 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.38, 0.7599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_538.TILE_ID, "walkable": TileBlueprint_538.WALKABLE, "cost": TileBlueprint_538.MOVEMENT_COST}


class TileBlueprint_539:
    TILE_ID = 539
    NAME = "Biome Tile Pattern #539"
    WALKABLE = True if 539 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.39, 0.7799999999999994)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_539.TILE_ID, "walkable": TileBlueprint_539.WALKABLE, "cost": TileBlueprint_539.MOVEMENT_COST}


class TileBlueprint_540:
    TILE_ID = 540
    NAME = "Biome Tile Pattern #540"
    WALKABLE = True if 540 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.4, 0.8000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_540.TILE_ID, "walkable": TileBlueprint_540.WALKABLE, "cost": TileBlueprint_540.MOVEMENT_COST}


class TileBlueprint_541:
    TILE_ID = 541
    NAME = "Biome Tile Pattern #541"
    WALKABLE = True if 541 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.41, 0.8200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_541.TILE_ID, "walkable": TileBlueprint_541.WALKABLE, "cost": TileBlueprint_541.MOVEMENT_COST}


class TileBlueprint_542:
    TILE_ID = 542
    NAME = "Biome Tile Pattern #542"
    WALKABLE = True if 542 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.42, 0.8399999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_542.TILE_ID, "walkable": TileBlueprint_542.WALKABLE, "cost": TileBlueprint_542.MOVEMENT_COST}


class TileBlueprint_543:
    TILE_ID = 543
    NAME = "Biome Tile Pattern #543"
    WALKABLE = True if 543 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.43, 0.8599999999999994)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_543.TILE_ID, "walkable": TileBlueprint_543.WALKABLE, "cost": TileBlueprint_543.MOVEMENT_COST}


class TileBlueprint_544:
    TILE_ID = 544
    NAME = "Biome Tile Pattern #544"
    WALKABLE = True if 544 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.44, 0.8800000000000008)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_544.TILE_ID, "walkable": TileBlueprint_544.WALKABLE, "cost": TileBlueprint_544.MOVEMENT_COST}


class TileBlueprint_545:
    TILE_ID = 545
    NAME = "Biome Tile Pattern #545"
    WALKABLE = True if 545 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.45, 0.9000000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_545.TILE_ID, "walkable": TileBlueprint_545.WALKABLE, "cost": TileBlueprint_545.MOVEMENT_COST}


class TileBlueprint_546:
    TILE_ID = 546
    NAME = "Biome Tile Pattern #546"
    WALKABLE = True if 546 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.46, 0.9199999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_546.TILE_ID, "walkable": TileBlueprint_546.WALKABLE, "cost": TileBlueprint_546.MOVEMENT_COST}


class TileBlueprint_547:
    TILE_ID = 547
    NAME = "Biome Tile Pattern #547"
    WALKABLE = True if 547 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.47, 0.9399999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_547.TILE_ID, "walkable": TileBlueprint_547.WALKABLE, "cost": TileBlueprint_547.MOVEMENT_COST}


class TileBlueprint_548:
    TILE_ID = 548
    NAME = "Biome Tile Pattern #548"
    WALKABLE = True if 548 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.48, 0.9600000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_548.TILE_ID, "walkable": TileBlueprint_548.WALKABLE, "cost": TileBlueprint_548.MOVEMENT_COST}


class TileBlueprint_549:
    TILE_ID = 549
    NAME = "Biome Tile Pattern #549"
    WALKABLE = True if 549 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.49, 0.9800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_549.TILE_ID, "walkable": TileBlueprint_549.WALKABLE, "cost": TileBlueprint_549.MOVEMENT_COST}


class TileBlueprint_550:
    TILE_ID = 550
    NAME = "Biome Tile Pattern #550"
    WALKABLE = True if 550 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.5, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_550.TILE_ID, "walkable": TileBlueprint_550.WALKABLE, "cost": TileBlueprint_550.MOVEMENT_COST}


class TileBlueprint_551:
    TILE_ID = 551
    NAME = "Biome Tile Pattern #551"
    WALKABLE = True if 551 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.51, 0.019999999999999574)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_551.TILE_ID, "walkable": TileBlueprint_551.WALKABLE, "cost": TileBlueprint_551.MOVEMENT_COST}


class TileBlueprint_552:
    TILE_ID = 552
    NAME = "Biome Tile Pattern #552"
    WALKABLE = True if 552 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.5200000000000005, 0.040000000000000924)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_552.TILE_ID, "walkable": TileBlueprint_552.WALKABLE, "cost": TileBlueprint_552.MOVEMENT_COST}


class TileBlueprint_553:
    TILE_ID = 553
    NAME = "Biome Tile Pattern #553"
    WALKABLE = True if 553 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.53, 0.0600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_553.TILE_ID, "walkable": TileBlueprint_553.WALKABLE, "cost": TileBlueprint_553.MOVEMENT_COST}


class TileBlueprint_554:
    TILE_ID = 554
    NAME = "Biome Tile Pattern #554"
    WALKABLE = True if 554 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.54, 0.08000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_554.TILE_ID, "walkable": TileBlueprint_554.WALKABLE, "cost": TileBlueprint_554.MOVEMENT_COST}


class TileBlueprint_555:
    TILE_ID = 555
    NAME = "Biome Tile Pattern #555"
    WALKABLE = True if 555 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.55, 0.09999999999999964)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_555.TILE_ID, "walkable": TileBlueprint_555.WALKABLE, "cost": TileBlueprint_555.MOVEMENT_COST}


class TileBlueprint_556:
    TILE_ID = 556
    NAME = "Biome Tile Pattern #556"
    WALKABLE = True if 556 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.5600000000000005, 0.120000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_556.TILE_ID, "walkable": TileBlueprint_556.WALKABLE, "cost": TileBlueprint_556.MOVEMENT_COST}


class TileBlueprint_557:
    TILE_ID = 557
    NAME = "Biome Tile Pattern #557"
    WALKABLE = True if 557 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.57, 0.14000000000000057)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_557.TILE_ID, "walkable": TileBlueprint_557.WALKABLE, "cost": TileBlueprint_557.MOVEMENT_COST}


class TileBlueprint_558:
    TILE_ID = 558
    NAME = "Biome Tile Pattern #558"
    WALKABLE = True if 558 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.58, 0.16000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_558.TILE_ID, "walkable": TileBlueprint_558.WALKABLE, "cost": TileBlueprint_558.MOVEMENT_COST}


class TileBlueprint_559:
    TILE_ID = 559
    NAME = "Biome Tile Pattern #559"
    WALKABLE = True if 559 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.59, 0.17999999999999972)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_559.TILE_ID, "walkable": TileBlueprint_559.WALKABLE, "cost": TileBlueprint_559.MOVEMENT_COST}


class TileBlueprint_560:
    TILE_ID = 560
    NAME = "Biome Tile Pattern #560"
    WALKABLE = True if 560 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.6000000000000005, 0.20000000000000107)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_560.TILE_ID, "walkable": TileBlueprint_560.WALKABLE, "cost": TileBlueprint_560.MOVEMENT_COST}


class TileBlueprint_561:
    TILE_ID = 561
    NAME = "Biome Tile Pattern #561"
    WALKABLE = True if 561 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.61, 0.22000000000000064)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_561.TILE_ID, "walkable": TileBlueprint_561.WALKABLE, "cost": TileBlueprint_561.MOVEMENT_COST}


class TileBlueprint_562:
    TILE_ID = 562
    NAME = "Biome Tile Pattern #562"
    WALKABLE = True if 562 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.62, 0.2400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_562.TILE_ID, "walkable": TileBlueprint_562.WALKABLE, "cost": TileBlueprint_562.MOVEMENT_COST}


class TileBlueprint_563:
    TILE_ID = 563
    NAME = "Biome Tile Pattern #563"
    WALKABLE = True if 563 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.63, 0.2599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_563.TILE_ID, "walkable": TileBlueprint_563.WALKABLE, "cost": TileBlueprint_563.MOVEMENT_COST}


class TileBlueprint_564:
    TILE_ID = 564
    NAME = "Biome Tile Pattern #564"
    WALKABLE = True if 564 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.64, 0.27999999999999936)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_564.TILE_ID, "walkable": TileBlueprint_564.WALKABLE, "cost": TileBlueprint_564.MOVEMENT_COST}


class TileBlueprint_565:
    TILE_ID = 565
    NAME = "Biome Tile Pattern #565"
    WALKABLE = True if 565 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.65, 0.3000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_565.TILE_ID, "walkable": TileBlueprint_565.WALKABLE, "cost": TileBlueprint_565.MOVEMENT_COST}


class TileBlueprint_566:
    TILE_ID = 566
    NAME = "Biome Tile Pattern #566"
    WALKABLE = True if 566 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.66, 0.3200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_566.TILE_ID, "walkable": TileBlueprint_566.WALKABLE, "cost": TileBlueprint_566.MOVEMENT_COST}


class TileBlueprint_567:
    TILE_ID = 567
    NAME = "Biome Tile Pattern #567"
    WALKABLE = True if 567 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.67, 0.33999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_567.TILE_ID, "walkable": TileBlueprint_567.WALKABLE, "cost": TileBlueprint_567.MOVEMENT_COST}


class TileBlueprint_568:
    TILE_ID = 568
    NAME = "Biome Tile Pattern #568"
    WALKABLE = True if 568 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.68, 0.35999999999999943)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_568.TILE_ID, "walkable": TileBlueprint_568.WALKABLE, "cost": TileBlueprint_568.MOVEMENT_COST}


class TileBlueprint_569:
    TILE_ID = 569
    NAME = "Biome Tile Pattern #569"
    WALKABLE = True if 569 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.69, 0.3800000000000008)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_569.TILE_ID, "walkable": TileBlueprint_569.WALKABLE, "cost": TileBlueprint_569.MOVEMENT_COST}


class TileBlueprint_570:
    TILE_ID = 570
    NAME = "Biome Tile Pattern #570"
    WALKABLE = True if 570 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.7, 0.40000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_570.TILE_ID, "walkable": TileBlueprint_570.WALKABLE, "cost": TileBlueprint_570.MOVEMENT_COST}


class TileBlueprint_571:
    TILE_ID = 571
    NAME = "Biome Tile Pattern #571"
    WALKABLE = True if 571 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.71, 0.41999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_571.TILE_ID, "walkable": TileBlueprint_571.WALKABLE, "cost": TileBlueprint_571.MOVEMENT_COST}


class TileBlueprint_572:
    TILE_ID = 572
    NAME = "Biome Tile Pattern #572"
    WALKABLE = True if 572 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.72, 0.4399999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_572.TILE_ID, "walkable": TileBlueprint_572.WALKABLE, "cost": TileBlueprint_572.MOVEMENT_COST}


class TileBlueprint_573:
    TILE_ID = 573
    NAME = "Biome Tile Pattern #573"
    WALKABLE = True if 573 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.73, 0.46000000000000085)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_573.TILE_ID, "walkable": TileBlueprint_573.WALKABLE, "cost": TileBlueprint_573.MOVEMENT_COST}


class TileBlueprint_574:
    TILE_ID = 574
    NAME = "Biome Tile Pattern #574"
    WALKABLE = True if 574 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.74, 0.4800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_574.TILE_ID, "walkable": TileBlueprint_574.WALKABLE, "cost": TileBlueprint_574.MOVEMENT_COST}


class TileBlueprint_575:
    TILE_ID = 575
    NAME = "Biome Tile Pattern #575"
    WALKABLE = True if 575 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.75, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_575.TILE_ID, "walkable": TileBlueprint_575.WALKABLE, "cost": TileBlueprint_575.MOVEMENT_COST}


class TileBlueprint_576:
    TILE_ID = 576
    NAME = "Biome Tile Pattern #576"
    WALKABLE = True if 576 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.76, 0.5199999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_576.TILE_ID, "walkable": TileBlueprint_576.WALKABLE, "cost": TileBlueprint_576.MOVEMENT_COST}


class TileBlueprint_577:
    TILE_ID = 577
    NAME = "Biome Tile Pattern #577"
    WALKABLE = True if 577 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.7700000000000005, 0.5400000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_577.TILE_ID, "walkable": TileBlueprint_577.WALKABLE, "cost": TileBlueprint_577.MOVEMENT_COST}


class TileBlueprint_578:
    TILE_ID = 578
    NAME = "Biome Tile Pattern #578"
    WALKABLE = True if 578 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.78, 0.5600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_578.TILE_ID, "walkable": TileBlueprint_578.WALKABLE, "cost": TileBlueprint_578.MOVEMENT_COST}


class TileBlueprint_579:
    TILE_ID = 579
    NAME = "Biome Tile Pattern #579"
    WALKABLE = True if 579 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.79, 0.5800000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_579.TILE_ID, "walkable": TileBlueprint_579.WALKABLE, "cost": TileBlueprint_579.MOVEMENT_COST}


class TileBlueprint_580:
    TILE_ID = 580
    NAME = "Biome Tile Pattern #580"
    WALKABLE = True if 580 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.8, 0.5999999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_580.TILE_ID, "walkable": TileBlueprint_580.WALKABLE, "cost": TileBlueprint_580.MOVEMENT_COST}


class TileBlueprint_581:
    TILE_ID = 581
    NAME = "Biome Tile Pattern #581"
    WALKABLE = True if 581 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.8100000000000005, 0.620000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_581.TILE_ID, "walkable": TileBlueprint_581.WALKABLE, "cost": TileBlueprint_581.MOVEMENT_COST}


class TileBlueprint_582:
    TILE_ID = 582
    NAME = "Biome Tile Pattern #582"
    WALKABLE = True if 582 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.82, 0.6400000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_582.TILE_ID, "walkable": TileBlueprint_582.WALKABLE, "cost": TileBlueprint_582.MOVEMENT_COST}


class TileBlueprint_583:
    TILE_ID = 583
    NAME = "Biome Tile Pattern #583"
    WALKABLE = True if 583 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.83, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_583.TILE_ID, "walkable": TileBlueprint_583.WALKABLE, "cost": TileBlueprint_583.MOVEMENT_COST}


class TileBlueprint_584:
    TILE_ID = 584
    NAME = "Biome Tile Pattern #584"
    WALKABLE = True if 584 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.84, 0.6799999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_584.TILE_ID, "walkable": TileBlueprint_584.WALKABLE, "cost": TileBlueprint_584.MOVEMENT_COST}


class TileBlueprint_585:
    TILE_ID = 585
    NAME = "Biome Tile Pattern #585"
    WALKABLE = True if 585 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.8500000000000005, 0.7000000000000011)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_585.TILE_ID, "walkable": TileBlueprint_585.WALKABLE, "cost": TileBlueprint_585.MOVEMENT_COST}


class TileBlueprint_586:
    TILE_ID = 586
    NAME = "Biome Tile Pattern #586"
    WALKABLE = True if 586 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.86, 0.7200000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_586.TILE_ID, "walkable": TileBlueprint_586.WALKABLE, "cost": TileBlueprint_586.MOVEMENT_COST}


class TileBlueprint_587:
    TILE_ID = 587
    NAME = "Biome Tile Pattern #587"
    WALKABLE = True if 587 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.87, 0.7400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_587.TILE_ID, "walkable": TileBlueprint_587.WALKABLE, "cost": TileBlueprint_587.MOVEMENT_COST}


class TileBlueprint_588:
    TILE_ID = 588
    NAME = "Biome Tile Pattern #588"
    WALKABLE = True if 588 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.88, 0.7599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_588.TILE_ID, "walkable": TileBlueprint_588.WALKABLE, "cost": TileBlueprint_588.MOVEMENT_COST}


class TileBlueprint_589:
    TILE_ID = 589
    NAME = "Biome Tile Pattern #589"
    WALKABLE = True if 589 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.89, 0.7799999999999994)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_589.TILE_ID, "walkable": TileBlueprint_589.WALKABLE, "cost": TileBlueprint_589.MOVEMENT_COST}


class TileBlueprint_590:
    TILE_ID = 590
    NAME = "Biome Tile Pattern #590"
    WALKABLE = True if 590 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.9, 0.8000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_590.TILE_ID, "walkable": TileBlueprint_590.WALKABLE, "cost": TileBlueprint_590.MOVEMENT_COST}


class TileBlueprint_591:
    TILE_ID = 591
    NAME = "Biome Tile Pattern #591"
    WALKABLE = True if 591 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.91, 0.8200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_591.TILE_ID, "walkable": TileBlueprint_591.WALKABLE, "cost": TileBlueprint_591.MOVEMENT_COST}


class TileBlueprint_592:
    TILE_ID = 592
    NAME = "Biome Tile Pattern #592"
    WALKABLE = True if 592 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.92, 0.8399999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_592.TILE_ID, "walkable": TileBlueprint_592.WALKABLE, "cost": TileBlueprint_592.MOVEMENT_COST}


class TileBlueprint_593:
    TILE_ID = 593
    NAME = "Biome Tile Pattern #593"
    WALKABLE = True if 593 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.93, 0.8599999999999994)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_593.TILE_ID, "walkable": TileBlueprint_593.WALKABLE, "cost": TileBlueprint_593.MOVEMENT_COST}


class TileBlueprint_594:
    TILE_ID = 594
    NAME = "Biome Tile Pattern #594"
    WALKABLE = True if 594 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.94, 0.8800000000000008)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_594.TILE_ID, "walkable": TileBlueprint_594.WALKABLE, "cost": TileBlueprint_594.MOVEMENT_COST}


class TileBlueprint_595:
    TILE_ID = 595
    NAME = "Biome Tile Pattern #595"
    WALKABLE = True if 595 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (5.95, 0.9000000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_595.TILE_ID, "walkable": TileBlueprint_595.WALKABLE, "cost": TileBlueprint_595.MOVEMENT_COST}


class TileBlueprint_596:
    TILE_ID = 596
    NAME = "Biome Tile Pattern #596"
    WALKABLE = True if 596 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (5.96, 0.9199999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_596.TILE_ID, "walkable": TileBlueprint_596.WALKABLE, "cost": TileBlueprint_596.MOVEMENT_COST}


class TileBlueprint_597:
    TILE_ID = 597
    NAME = "Biome Tile Pattern #597"
    WALKABLE = True if 597 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (5.97, 0.9399999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_597.TILE_ID, "walkable": TileBlueprint_597.WALKABLE, "cost": TileBlueprint_597.MOVEMENT_COST}


class TileBlueprint_598:
    TILE_ID = 598
    NAME = "Biome Tile Pattern #598"
    WALKABLE = True if 598 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (5.98, 0.9600000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_598.TILE_ID, "walkable": TileBlueprint_598.WALKABLE, "cost": TileBlueprint_598.MOVEMENT_COST}


class TileBlueprint_599:
    TILE_ID = 599
    NAME = "Biome Tile Pattern #599"
    WALKABLE = True if 599 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (5.99, 0.9800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_599.TILE_ID, "walkable": TileBlueprint_599.WALKABLE, "cost": TileBlueprint_599.MOVEMENT_COST}


class TileBlueprint_600:
    TILE_ID = 600
    NAME = "Biome Tile Pattern #600"
    WALKABLE = True if 600 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.0, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_600.TILE_ID, "walkable": TileBlueprint_600.WALKABLE, "cost": TileBlueprint_600.MOVEMENT_COST}


class TileBlueprint_601:
    TILE_ID = 601
    NAME = "Biome Tile Pattern #601"
    WALKABLE = True if 601 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.01, 0.019999999999999574)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_601.TILE_ID, "walkable": TileBlueprint_601.WALKABLE, "cost": TileBlueprint_601.MOVEMENT_COST}


class TileBlueprint_602:
    TILE_ID = 602
    NAME = "Biome Tile Pattern #602"
    WALKABLE = True if 602 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.0200000000000005, 0.040000000000000924)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_602.TILE_ID, "walkable": TileBlueprint_602.WALKABLE, "cost": TileBlueprint_602.MOVEMENT_COST}


class TileBlueprint_603:
    TILE_ID = 603
    NAME = "Biome Tile Pattern #603"
    WALKABLE = True if 603 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.03, 0.0600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_603.TILE_ID, "walkable": TileBlueprint_603.WALKABLE, "cost": TileBlueprint_603.MOVEMENT_COST}


class TileBlueprint_604:
    TILE_ID = 604
    NAME = "Biome Tile Pattern #604"
    WALKABLE = True if 604 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.04, 0.08000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_604.TILE_ID, "walkable": TileBlueprint_604.WALKABLE, "cost": TileBlueprint_604.MOVEMENT_COST}


class TileBlueprint_605:
    TILE_ID = 605
    NAME = "Biome Tile Pattern #605"
    WALKABLE = True if 605 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.05, 0.09999999999999964)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_605.TILE_ID, "walkable": TileBlueprint_605.WALKABLE, "cost": TileBlueprint_605.MOVEMENT_COST}


class TileBlueprint_606:
    TILE_ID = 606
    NAME = "Biome Tile Pattern #606"
    WALKABLE = True if 606 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.0600000000000005, 0.120000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_606.TILE_ID, "walkable": TileBlueprint_606.WALKABLE, "cost": TileBlueprint_606.MOVEMENT_COST}


class TileBlueprint_607:
    TILE_ID = 607
    NAME = "Biome Tile Pattern #607"
    WALKABLE = True if 607 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.07, 0.14000000000000057)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_607.TILE_ID, "walkable": TileBlueprint_607.WALKABLE, "cost": TileBlueprint_607.MOVEMENT_COST}


class TileBlueprint_608:
    TILE_ID = 608
    NAME = "Biome Tile Pattern #608"
    WALKABLE = True if 608 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.08, 0.16000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_608.TILE_ID, "walkable": TileBlueprint_608.WALKABLE, "cost": TileBlueprint_608.MOVEMENT_COST}


class TileBlueprint_609:
    TILE_ID = 609
    NAME = "Biome Tile Pattern #609"
    WALKABLE = True if 609 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.09, 0.17999999999999972)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_609.TILE_ID, "walkable": TileBlueprint_609.WALKABLE, "cost": TileBlueprint_609.MOVEMENT_COST}


class TileBlueprint_610:
    TILE_ID = 610
    NAME = "Biome Tile Pattern #610"
    WALKABLE = True if 610 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.1000000000000005, 0.20000000000000107)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_610.TILE_ID, "walkable": TileBlueprint_610.WALKABLE, "cost": TileBlueprint_610.MOVEMENT_COST}


class TileBlueprint_611:
    TILE_ID = 611
    NAME = "Biome Tile Pattern #611"
    WALKABLE = True if 611 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.11, 0.22000000000000064)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_611.TILE_ID, "walkable": TileBlueprint_611.WALKABLE, "cost": TileBlueprint_611.MOVEMENT_COST}


class TileBlueprint_612:
    TILE_ID = 612
    NAME = "Biome Tile Pattern #612"
    WALKABLE = True if 612 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.12, 0.2400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_612.TILE_ID, "walkable": TileBlueprint_612.WALKABLE, "cost": TileBlueprint_612.MOVEMENT_COST}


class TileBlueprint_613:
    TILE_ID = 613
    NAME = "Biome Tile Pattern #613"
    WALKABLE = True if 613 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.13, 0.2599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_613.TILE_ID, "walkable": TileBlueprint_613.WALKABLE, "cost": TileBlueprint_613.MOVEMENT_COST}


class TileBlueprint_614:
    TILE_ID = 614
    NAME = "Biome Tile Pattern #614"
    WALKABLE = True if 614 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.140000000000001, 0.28000000000000114)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_614.TILE_ID, "walkable": TileBlueprint_614.WALKABLE, "cost": TileBlueprint_614.MOVEMENT_COST}


class TileBlueprint_615:
    TILE_ID = 615
    NAME = "Biome Tile Pattern #615"
    WALKABLE = True if 615 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.15, 0.3000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_615.TILE_ID, "walkable": TileBlueprint_615.WALKABLE, "cost": TileBlueprint_615.MOVEMENT_COST}


class TileBlueprint_616:
    TILE_ID = 616
    NAME = "Biome Tile Pattern #616"
    WALKABLE = True if 616 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.16, 0.3200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_616.TILE_ID, "walkable": TileBlueprint_616.WALKABLE, "cost": TileBlueprint_616.MOVEMENT_COST}


class TileBlueprint_617:
    TILE_ID = 617
    NAME = "Biome Tile Pattern #617"
    WALKABLE = True if 617 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.17, 0.33999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_617.TILE_ID, "walkable": TileBlueprint_617.WALKABLE, "cost": TileBlueprint_617.MOVEMENT_COST}


class TileBlueprint_618:
    TILE_ID = 618
    NAME = "Biome Tile Pattern #618"
    WALKABLE = True if 618 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.18, 0.35999999999999943)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_618.TILE_ID, "walkable": TileBlueprint_618.WALKABLE, "cost": TileBlueprint_618.MOVEMENT_COST}


class TileBlueprint_619:
    TILE_ID = 619
    NAME = "Biome Tile Pattern #619"
    WALKABLE = True if 619 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.19, 0.3800000000000008)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_619.TILE_ID, "walkable": TileBlueprint_619.WALKABLE, "cost": TileBlueprint_619.MOVEMENT_COST}


class TileBlueprint_620:
    TILE_ID = 620
    NAME = "Biome Tile Pattern #620"
    WALKABLE = True if 620 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.2, 0.40000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_620.TILE_ID, "walkable": TileBlueprint_620.WALKABLE, "cost": TileBlueprint_620.MOVEMENT_COST}


class TileBlueprint_621:
    TILE_ID = 621
    NAME = "Biome Tile Pattern #621"
    WALKABLE = True if 621 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.21, 0.41999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_621.TILE_ID, "walkable": TileBlueprint_621.WALKABLE, "cost": TileBlueprint_621.MOVEMENT_COST}


class TileBlueprint_622:
    TILE_ID = 622
    NAME = "Biome Tile Pattern #622"
    WALKABLE = True if 622 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.22, 0.4399999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_622.TILE_ID, "walkable": TileBlueprint_622.WALKABLE, "cost": TileBlueprint_622.MOVEMENT_COST}


class TileBlueprint_623:
    TILE_ID = 623
    NAME = "Biome Tile Pattern #623"
    WALKABLE = True if 623 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.23, 0.46000000000000085)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_623.TILE_ID, "walkable": TileBlueprint_623.WALKABLE, "cost": TileBlueprint_623.MOVEMENT_COST}


class TileBlueprint_624:
    TILE_ID = 624
    NAME = "Biome Tile Pattern #624"
    WALKABLE = True if 624 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.24, 0.4800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_624.TILE_ID, "walkable": TileBlueprint_624.WALKABLE, "cost": TileBlueprint_624.MOVEMENT_COST}


class TileBlueprint_625:
    TILE_ID = 625
    NAME = "Biome Tile Pattern #625"
    WALKABLE = True if 625 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.25, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_625.TILE_ID, "walkable": TileBlueprint_625.WALKABLE, "cost": TileBlueprint_625.MOVEMENT_COST}


class TileBlueprint_626:
    TILE_ID = 626
    NAME = "Biome Tile Pattern #626"
    WALKABLE = True if 626 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.26, 0.5199999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_626.TILE_ID, "walkable": TileBlueprint_626.WALKABLE, "cost": TileBlueprint_626.MOVEMENT_COST}


class TileBlueprint_627:
    TILE_ID = 627
    NAME = "Biome Tile Pattern #627"
    WALKABLE = True if 627 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.2700000000000005, 0.5400000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_627.TILE_ID, "walkable": TileBlueprint_627.WALKABLE, "cost": TileBlueprint_627.MOVEMENT_COST}


class TileBlueprint_628:
    TILE_ID = 628
    NAME = "Biome Tile Pattern #628"
    WALKABLE = True if 628 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.28, 0.5600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_628.TILE_ID, "walkable": TileBlueprint_628.WALKABLE, "cost": TileBlueprint_628.MOVEMENT_COST}


class TileBlueprint_629:
    TILE_ID = 629
    NAME = "Biome Tile Pattern #629"
    WALKABLE = True if 629 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.29, 0.5800000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_629.TILE_ID, "walkable": TileBlueprint_629.WALKABLE, "cost": TileBlueprint_629.MOVEMENT_COST}


class TileBlueprint_630:
    TILE_ID = 630
    NAME = "Biome Tile Pattern #630"
    WALKABLE = True if 630 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.3, 0.5999999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_630.TILE_ID, "walkable": TileBlueprint_630.WALKABLE, "cost": TileBlueprint_630.MOVEMENT_COST}


class TileBlueprint_631:
    TILE_ID = 631
    NAME = "Biome Tile Pattern #631"
    WALKABLE = True if 631 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.3100000000000005, 0.620000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_631.TILE_ID, "walkable": TileBlueprint_631.WALKABLE, "cost": TileBlueprint_631.MOVEMENT_COST}


class TileBlueprint_632:
    TILE_ID = 632
    NAME = "Biome Tile Pattern #632"
    WALKABLE = True if 632 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.32, 0.6400000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_632.TILE_ID, "walkable": TileBlueprint_632.WALKABLE, "cost": TileBlueprint_632.MOVEMENT_COST}


class TileBlueprint_633:
    TILE_ID = 633
    NAME = "Biome Tile Pattern #633"
    WALKABLE = True if 633 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.33, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_633.TILE_ID, "walkable": TileBlueprint_633.WALKABLE, "cost": TileBlueprint_633.MOVEMENT_COST}


class TileBlueprint_634:
    TILE_ID = 634
    NAME = "Biome Tile Pattern #634"
    WALKABLE = True if 634 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.34, 0.6799999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_634.TILE_ID, "walkable": TileBlueprint_634.WALKABLE, "cost": TileBlueprint_634.MOVEMENT_COST}


class TileBlueprint_635:
    TILE_ID = 635
    NAME = "Biome Tile Pattern #635"
    WALKABLE = True if 635 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.3500000000000005, 0.7000000000000011)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_635.TILE_ID, "walkable": TileBlueprint_635.WALKABLE, "cost": TileBlueprint_635.MOVEMENT_COST}


class TileBlueprint_636:
    TILE_ID = 636
    NAME = "Biome Tile Pattern #636"
    WALKABLE = True if 636 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.36, 0.7200000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_636.TILE_ID, "walkable": TileBlueprint_636.WALKABLE, "cost": TileBlueprint_636.MOVEMENT_COST}


class TileBlueprint_637:
    TILE_ID = 637
    NAME = "Biome Tile Pattern #637"
    WALKABLE = True if 637 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.37, 0.7400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_637.TILE_ID, "walkable": TileBlueprint_637.WALKABLE, "cost": TileBlueprint_637.MOVEMENT_COST}


class TileBlueprint_638:
    TILE_ID = 638
    NAME = "Biome Tile Pattern #638"
    WALKABLE = True if 638 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.38, 0.7599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_638.TILE_ID, "walkable": TileBlueprint_638.WALKABLE, "cost": TileBlueprint_638.MOVEMENT_COST}


class TileBlueprint_639:
    TILE_ID = 639
    NAME = "Biome Tile Pattern #639"
    WALKABLE = True if 639 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.390000000000001, 0.7800000000000011)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_639.TILE_ID, "walkable": TileBlueprint_639.WALKABLE, "cost": TileBlueprint_639.MOVEMENT_COST}


class TileBlueprint_640:
    TILE_ID = 640
    NAME = "Biome Tile Pattern #640"
    WALKABLE = True if 640 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.4, 0.8000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_640.TILE_ID, "walkable": TileBlueprint_640.WALKABLE, "cost": TileBlueprint_640.MOVEMENT_COST}


class TileBlueprint_641:
    TILE_ID = 641
    NAME = "Biome Tile Pattern #641"
    WALKABLE = True if 641 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.41, 0.8200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_641.TILE_ID, "walkable": TileBlueprint_641.WALKABLE, "cost": TileBlueprint_641.MOVEMENT_COST}


class TileBlueprint_642:
    TILE_ID = 642
    NAME = "Biome Tile Pattern #642"
    WALKABLE = True if 642 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.42, 0.8399999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_642.TILE_ID, "walkable": TileBlueprint_642.WALKABLE, "cost": TileBlueprint_642.MOVEMENT_COST}


class TileBlueprint_643:
    TILE_ID = 643
    NAME = "Biome Tile Pattern #643"
    WALKABLE = True if 643 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.43, 0.8599999999999994)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_643.TILE_ID, "walkable": TileBlueprint_643.WALKABLE, "cost": TileBlueprint_643.MOVEMENT_COST}


class TileBlueprint_644:
    TILE_ID = 644
    NAME = "Biome Tile Pattern #644"
    WALKABLE = True if 644 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.44, 0.8800000000000008)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_644.TILE_ID, "walkable": TileBlueprint_644.WALKABLE, "cost": TileBlueprint_644.MOVEMENT_COST}


class TileBlueprint_645:
    TILE_ID = 645
    NAME = "Biome Tile Pattern #645"
    WALKABLE = True if 645 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.45, 0.9000000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_645.TILE_ID, "walkable": TileBlueprint_645.WALKABLE, "cost": TileBlueprint_645.MOVEMENT_COST}


class TileBlueprint_646:
    TILE_ID = 646
    NAME = "Biome Tile Pattern #646"
    WALKABLE = True if 646 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.46, 0.9199999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_646.TILE_ID, "walkable": TileBlueprint_646.WALKABLE, "cost": TileBlueprint_646.MOVEMENT_COST}


class TileBlueprint_647:
    TILE_ID = 647
    NAME = "Biome Tile Pattern #647"
    WALKABLE = True if 647 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.47, 0.9399999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_647.TILE_ID, "walkable": TileBlueprint_647.WALKABLE, "cost": TileBlueprint_647.MOVEMENT_COST}


class TileBlueprint_648:
    TILE_ID = 648
    NAME = "Biome Tile Pattern #648"
    WALKABLE = True if 648 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.48, 0.9600000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_648.TILE_ID, "walkable": TileBlueprint_648.WALKABLE, "cost": TileBlueprint_648.MOVEMENT_COST}


class TileBlueprint_649:
    TILE_ID = 649
    NAME = "Biome Tile Pattern #649"
    WALKABLE = True if 649 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.49, 0.9800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_649.TILE_ID, "walkable": TileBlueprint_649.WALKABLE, "cost": TileBlueprint_649.MOVEMENT_COST}


class TileBlueprint_650:
    TILE_ID = 650
    NAME = "Biome Tile Pattern #650"
    WALKABLE = True if 650 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.5, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_650.TILE_ID, "walkable": TileBlueprint_650.WALKABLE, "cost": TileBlueprint_650.MOVEMENT_COST}


class TileBlueprint_651:
    TILE_ID = 651
    NAME = "Biome Tile Pattern #651"
    WALKABLE = True if 651 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.51, 0.019999999999999574)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_651.TILE_ID, "walkable": TileBlueprint_651.WALKABLE, "cost": TileBlueprint_651.MOVEMENT_COST}


class TileBlueprint_652:
    TILE_ID = 652
    NAME = "Biome Tile Pattern #652"
    WALKABLE = True if 652 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.5200000000000005, 0.040000000000000924)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_652.TILE_ID, "walkable": TileBlueprint_652.WALKABLE, "cost": TileBlueprint_652.MOVEMENT_COST}


class TileBlueprint_653:
    TILE_ID = 653
    NAME = "Biome Tile Pattern #653"
    WALKABLE = True if 653 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.53, 0.0600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_653.TILE_ID, "walkable": TileBlueprint_653.WALKABLE, "cost": TileBlueprint_653.MOVEMENT_COST}


class TileBlueprint_654:
    TILE_ID = 654
    NAME = "Biome Tile Pattern #654"
    WALKABLE = True if 654 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.54, 0.08000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_654.TILE_ID, "walkable": TileBlueprint_654.WALKABLE, "cost": TileBlueprint_654.MOVEMENT_COST}


class TileBlueprint_655:
    TILE_ID = 655
    NAME = "Biome Tile Pattern #655"
    WALKABLE = True if 655 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.55, 0.09999999999999964)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_655.TILE_ID, "walkable": TileBlueprint_655.WALKABLE, "cost": TileBlueprint_655.MOVEMENT_COST}


class TileBlueprint_656:
    TILE_ID = 656
    NAME = "Biome Tile Pattern #656"
    WALKABLE = True if 656 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.5600000000000005, 0.120000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_656.TILE_ID, "walkable": TileBlueprint_656.WALKABLE, "cost": TileBlueprint_656.MOVEMENT_COST}


class TileBlueprint_657:
    TILE_ID = 657
    NAME = "Biome Tile Pattern #657"
    WALKABLE = True if 657 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.57, 0.14000000000000057)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_657.TILE_ID, "walkable": TileBlueprint_657.WALKABLE, "cost": TileBlueprint_657.MOVEMENT_COST}


class TileBlueprint_658:
    TILE_ID = 658
    NAME = "Biome Tile Pattern #658"
    WALKABLE = True if 658 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.58, 0.16000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_658.TILE_ID, "walkable": TileBlueprint_658.WALKABLE, "cost": TileBlueprint_658.MOVEMENT_COST}


class TileBlueprint_659:
    TILE_ID = 659
    NAME = "Biome Tile Pattern #659"
    WALKABLE = True if 659 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.59, 0.17999999999999972)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_659.TILE_ID, "walkable": TileBlueprint_659.WALKABLE, "cost": TileBlueprint_659.MOVEMENT_COST}


class TileBlueprint_660:
    TILE_ID = 660
    NAME = "Biome Tile Pattern #660"
    WALKABLE = True if 660 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.6000000000000005, 0.20000000000000107)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_660.TILE_ID, "walkable": TileBlueprint_660.WALKABLE, "cost": TileBlueprint_660.MOVEMENT_COST}


class TileBlueprint_661:
    TILE_ID = 661
    NAME = "Biome Tile Pattern #661"
    WALKABLE = True if 661 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.61, 0.22000000000000064)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_661.TILE_ID, "walkable": TileBlueprint_661.WALKABLE, "cost": TileBlueprint_661.MOVEMENT_COST}


class TileBlueprint_662:
    TILE_ID = 662
    NAME = "Biome Tile Pattern #662"
    WALKABLE = True if 662 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.62, 0.2400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_662.TILE_ID, "walkable": TileBlueprint_662.WALKABLE, "cost": TileBlueprint_662.MOVEMENT_COST}


class TileBlueprint_663:
    TILE_ID = 663
    NAME = "Biome Tile Pattern #663"
    WALKABLE = True if 663 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.63, 0.2599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_663.TILE_ID, "walkable": TileBlueprint_663.WALKABLE, "cost": TileBlueprint_663.MOVEMENT_COST}


class TileBlueprint_664:
    TILE_ID = 664
    NAME = "Biome Tile Pattern #664"
    WALKABLE = True if 664 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.640000000000001, 0.28000000000000114)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_664.TILE_ID, "walkable": TileBlueprint_664.WALKABLE, "cost": TileBlueprint_664.MOVEMENT_COST}


class TileBlueprint_665:
    TILE_ID = 665
    NAME = "Biome Tile Pattern #665"
    WALKABLE = True if 665 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.65, 0.3000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_665.TILE_ID, "walkable": TileBlueprint_665.WALKABLE, "cost": TileBlueprint_665.MOVEMENT_COST}


class TileBlueprint_666:
    TILE_ID = 666
    NAME = "Biome Tile Pattern #666"
    WALKABLE = True if 666 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.66, 0.3200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_666.TILE_ID, "walkable": TileBlueprint_666.WALKABLE, "cost": TileBlueprint_666.MOVEMENT_COST}


class TileBlueprint_667:
    TILE_ID = 667
    NAME = "Biome Tile Pattern #667"
    WALKABLE = True if 667 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.67, 0.33999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_667.TILE_ID, "walkable": TileBlueprint_667.WALKABLE, "cost": TileBlueprint_667.MOVEMENT_COST}


class TileBlueprint_668:
    TILE_ID = 668
    NAME = "Biome Tile Pattern #668"
    WALKABLE = True if 668 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.68, 0.35999999999999943)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_668.TILE_ID, "walkable": TileBlueprint_668.WALKABLE, "cost": TileBlueprint_668.MOVEMENT_COST}


class TileBlueprint_669:
    TILE_ID = 669
    NAME = "Biome Tile Pattern #669"
    WALKABLE = True if 669 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.69, 0.3800000000000008)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_669.TILE_ID, "walkable": TileBlueprint_669.WALKABLE, "cost": TileBlueprint_669.MOVEMENT_COST}


class TileBlueprint_670:
    TILE_ID = 670
    NAME = "Biome Tile Pattern #670"
    WALKABLE = True if 670 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.7, 0.40000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_670.TILE_ID, "walkable": TileBlueprint_670.WALKABLE, "cost": TileBlueprint_670.MOVEMENT_COST}


class TileBlueprint_671:
    TILE_ID = 671
    NAME = "Biome Tile Pattern #671"
    WALKABLE = True if 671 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.71, 0.41999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_671.TILE_ID, "walkable": TileBlueprint_671.WALKABLE, "cost": TileBlueprint_671.MOVEMENT_COST}


class TileBlueprint_672:
    TILE_ID = 672
    NAME = "Biome Tile Pattern #672"
    WALKABLE = True if 672 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.72, 0.4399999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_672.TILE_ID, "walkable": TileBlueprint_672.WALKABLE, "cost": TileBlueprint_672.MOVEMENT_COST}


class TileBlueprint_673:
    TILE_ID = 673
    NAME = "Biome Tile Pattern #673"
    WALKABLE = True if 673 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.73, 0.46000000000000085)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_673.TILE_ID, "walkable": TileBlueprint_673.WALKABLE, "cost": TileBlueprint_673.MOVEMENT_COST}


class TileBlueprint_674:
    TILE_ID = 674
    NAME = "Biome Tile Pattern #674"
    WALKABLE = True if 674 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.74, 0.4800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_674.TILE_ID, "walkable": TileBlueprint_674.WALKABLE, "cost": TileBlueprint_674.MOVEMENT_COST}


class TileBlueprint_675:
    TILE_ID = 675
    NAME = "Biome Tile Pattern #675"
    WALKABLE = True if 675 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.75, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_675.TILE_ID, "walkable": TileBlueprint_675.WALKABLE, "cost": TileBlueprint_675.MOVEMENT_COST}


class TileBlueprint_676:
    TILE_ID = 676
    NAME = "Biome Tile Pattern #676"
    WALKABLE = True if 676 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.76, 0.5199999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_676.TILE_ID, "walkable": TileBlueprint_676.WALKABLE, "cost": TileBlueprint_676.MOVEMENT_COST}


class TileBlueprint_677:
    TILE_ID = 677
    NAME = "Biome Tile Pattern #677"
    WALKABLE = True if 677 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.7700000000000005, 0.5400000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_677.TILE_ID, "walkable": TileBlueprint_677.WALKABLE, "cost": TileBlueprint_677.MOVEMENT_COST}


class TileBlueprint_678:
    TILE_ID = 678
    NAME = "Biome Tile Pattern #678"
    WALKABLE = True if 678 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.78, 0.5600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_678.TILE_ID, "walkable": TileBlueprint_678.WALKABLE, "cost": TileBlueprint_678.MOVEMENT_COST}


class TileBlueprint_679:
    TILE_ID = 679
    NAME = "Biome Tile Pattern #679"
    WALKABLE = True if 679 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.79, 0.5800000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_679.TILE_ID, "walkable": TileBlueprint_679.WALKABLE, "cost": TileBlueprint_679.MOVEMENT_COST}


class TileBlueprint_680:
    TILE_ID = 680
    NAME = "Biome Tile Pattern #680"
    WALKABLE = True if 680 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.8, 0.5999999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_680.TILE_ID, "walkable": TileBlueprint_680.WALKABLE, "cost": TileBlueprint_680.MOVEMENT_COST}


class TileBlueprint_681:
    TILE_ID = 681
    NAME = "Biome Tile Pattern #681"
    WALKABLE = True if 681 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.8100000000000005, 0.620000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_681.TILE_ID, "walkable": TileBlueprint_681.WALKABLE, "cost": TileBlueprint_681.MOVEMENT_COST}


class TileBlueprint_682:
    TILE_ID = 682
    NAME = "Biome Tile Pattern #682"
    WALKABLE = True if 682 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.82, 0.6400000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_682.TILE_ID, "walkable": TileBlueprint_682.WALKABLE, "cost": TileBlueprint_682.MOVEMENT_COST}


class TileBlueprint_683:
    TILE_ID = 683
    NAME = "Biome Tile Pattern #683"
    WALKABLE = True if 683 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.83, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_683.TILE_ID, "walkable": TileBlueprint_683.WALKABLE, "cost": TileBlueprint_683.MOVEMENT_COST}


class TileBlueprint_684:
    TILE_ID = 684
    NAME = "Biome Tile Pattern #684"
    WALKABLE = True if 684 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.84, 0.6799999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_684.TILE_ID, "walkable": TileBlueprint_684.WALKABLE, "cost": TileBlueprint_684.MOVEMENT_COST}


class TileBlueprint_685:
    TILE_ID = 685
    NAME = "Biome Tile Pattern #685"
    WALKABLE = True if 685 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.8500000000000005, 0.7000000000000011)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_685.TILE_ID, "walkable": TileBlueprint_685.WALKABLE, "cost": TileBlueprint_685.MOVEMENT_COST}


class TileBlueprint_686:
    TILE_ID = 686
    NAME = "Biome Tile Pattern #686"
    WALKABLE = True if 686 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.86, 0.7200000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_686.TILE_ID, "walkable": TileBlueprint_686.WALKABLE, "cost": TileBlueprint_686.MOVEMENT_COST}


class TileBlueprint_687:
    TILE_ID = 687
    NAME = "Biome Tile Pattern #687"
    WALKABLE = True if 687 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.87, 0.7400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_687.TILE_ID, "walkable": TileBlueprint_687.WALKABLE, "cost": TileBlueprint_687.MOVEMENT_COST}


class TileBlueprint_688:
    TILE_ID = 688
    NAME = "Biome Tile Pattern #688"
    WALKABLE = True if 688 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.88, 0.7599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_688.TILE_ID, "walkable": TileBlueprint_688.WALKABLE, "cost": TileBlueprint_688.MOVEMENT_COST}


class TileBlueprint_689:
    TILE_ID = 689
    NAME = "Biome Tile Pattern #689"
    WALKABLE = True if 689 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.890000000000001, 0.7800000000000011)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_689.TILE_ID, "walkable": TileBlueprint_689.WALKABLE, "cost": TileBlueprint_689.MOVEMENT_COST}


class TileBlueprint_690:
    TILE_ID = 690
    NAME = "Biome Tile Pattern #690"
    WALKABLE = True if 690 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.9, 0.8000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_690.TILE_ID, "walkable": TileBlueprint_690.WALKABLE, "cost": TileBlueprint_690.MOVEMENT_COST}


class TileBlueprint_691:
    TILE_ID = 691
    NAME = "Biome Tile Pattern #691"
    WALKABLE = True if 691 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.91, 0.8200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_691.TILE_ID, "walkable": TileBlueprint_691.WALKABLE, "cost": TileBlueprint_691.MOVEMENT_COST}


class TileBlueprint_692:
    TILE_ID = 692
    NAME = "Biome Tile Pattern #692"
    WALKABLE = True if 692 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.92, 0.8399999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_692.TILE_ID, "walkable": TileBlueprint_692.WALKABLE, "cost": TileBlueprint_692.MOVEMENT_COST}


class TileBlueprint_693:
    TILE_ID = 693
    NAME = "Biome Tile Pattern #693"
    WALKABLE = True if 693 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.93, 0.8599999999999994)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_693.TILE_ID, "walkable": TileBlueprint_693.WALKABLE, "cost": TileBlueprint_693.MOVEMENT_COST}


class TileBlueprint_694:
    TILE_ID = 694
    NAME = "Biome Tile Pattern #694"
    WALKABLE = True if 694 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.94, 0.8800000000000008)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_694.TILE_ID, "walkable": TileBlueprint_694.WALKABLE, "cost": TileBlueprint_694.MOVEMENT_COST}


class TileBlueprint_695:
    TILE_ID = 695
    NAME = "Biome Tile Pattern #695"
    WALKABLE = True if 695 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (6.95, 0.9000000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_695.TILE_ID, "walkable": TileBlueprint_695.WALKABLE, "cost": TileBlueprint_695.MOVEMENT_COST}


class TileBlueprint_696:
    TILE_ID = 696
    NAME = "Biome Tile Pattern #696"
    WALKABLE = True if 696 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (6.96, 0.9199999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_696.TILE_ID, "walkable": TileBlueprint_696.WALKABLE, "cost": TileBlueprint_696.MOVEMENT_COST}


class TileBlueprint_697:
    TILE_ID = 697
    NAME = "Biome Tile Pattern #697"
    WALKABLE = True if 697 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (6.97, 0.9399999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_697.TILE_ID, "walkable": TileBlueprint_697.WALKABLE, "cost": TileBlueprint_697.MOVEMENT_COST}


class TileBlueprint_698:
    TILE_ID = 698
    NAME = "Biome Tile Pattern #698"
    WALKABLE = True if 698 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (6.98, 0.9600000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_698.TILE_ID, "walkable": TileBlueprint_698.WALKABLE, "cost": TileBlueprint_698.MOVEMENT_COST}


class TileBlueprint_699:
    TILE_ID = 699
    NAME = "Biome Tile Pattern #699"
    WALKABLE = True if 699 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (6.99, 0.9800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_699.TILE_ID, "walkable": TileBlueprint_699.WALKABLE, "cost": TileBlueprint_699.MOVEMENT_COST}


class TileBlueprint_700:
    TILE_ID = 700
    NAME = "Biome Tile Pattern #700"
    WALKABLE = True if 700 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.0, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_700.TILE_ID, "walkable": TileBlueprint_700.WALKABLE, "cost": TileBlueprint_700.MOVEMENT_COST}


class TileBlueprint_701:
    TILE_ID = 701
    NAME = "Biome Tile Pattern #701"
    WALKABLE = True if 701 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.01, 0.019999999999999574)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_701.TILE_ID, "walkable": TileBlueprint_701.WALKABLE, "cost": TileBlueprint_701.MOVEMENT_COST}


class TileBlueprint_702:
    TILE_ID = 702
    NAME = "Biome Tile Pattern #702"
    WALKABLE = True if 702 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.0200000000000005, 0.040000000000000924)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_702.TILE_ID, "walkable": TileBlueprint_702.WALKABLE, "cost": TileBlueprint_702.MOVEMENT_COST}


class TileBlueprint_703:
    TILE_ID = 703
    NAME = "Biome Tile Pattern #703"
    WALKABLE = True if 703 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.03, 0.0600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_703.TILE_ID, "walkable": TileBlueprint_703.WALKABLE, "cost": TileBlueprint_703.MOVEMENT_COST}


class TileBlueprint_704:
    TILE_ID = 704
    NAME = "Biome Tile Pattern #704"
    WALKABLE = True if 704 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.04, 0.08000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_704.TILE_ID, "walkable": TileBlueprint_704.WALKABLE, "cost": TileBlueprint_704.MOVEMENT_COST}


class TileBlueprint_705:
    TILE_ID = 705
    NAME = "Biome Tile Pattern #705"
    WALKABLE = True if 705 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.05, 0.09999999999999964)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_705.TILE_ID, "walkable": TileBlueprint_705.WALKABLE, "cost": TileBlueprint_705.MOVEMENT_COST}


class TileBlueprint_706:
    TILE_ID = 706
    NAME = "Biome Tile Pattern #706"
    WALKABLE = True if 706 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.0600000000000005, 0.120000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_706.TILE_ID, "walkable": TileBlueprint_706.WALKABLE, "cost": TileBlueprint_706.MOVEMENT_COST}


class TileBlueprint_707:
    TILE_ID = 707
    NAME = "Biome Tile Pattern #707"
    WALKABLE = True if 707 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.07, 0.14000000000000057)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_707.TILE_ID, "walkable": TileBlueprint_707.WALKABLE, "cost": TileBlueprint_707.MOVEMENT_COST}


class TileBlueprint_708:
    TILE_ID = 708
    NAME = "Biome Tile Pattern #708"
    WALKABLE = True if 708 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.08, 0.16000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_708.TILE_ID, "walkable": TileBlueprint_708.WALKABLE, "cost": TileBlueprint_708.MOVEMENT_COST}


class TileBlueprint_709:
    TILE_ID = 709
    NAME = "Biome Tile Pattern #709"
    WALKABLE = True if 709 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.09, 0.17999999999999972)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_709.TILE_ID, "walkable": TileBlueprint_709.WALKABLE, "cost": TileBlueprint_709.MOVEMENT_COST}


class TileBlueprint_710:
    TILE_ID = 710
    NAME = "Biome Tile Pattern #710"
    WALKABLE = True if 710 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.1000000000000005, 0.20000000000000107)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_710.TILE_ID, "walkable": TileBlueprint_710.WALKABLE, "cost": TileBlueprint_710.MOVEMENT_COST}


class TileBlueprint_711:
    TILE_ID = 711
    NAME = "Biome Tile Pattern #711"
    WALKABLE = True if 711 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.11, 0.22000000000000064)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_711.TILE_ID, "walkable": TileBlueprint_711.WALKABLE, "cost": TileBlueprint_711.MOVEMENT_COST}


class TileBlueprint_712:
    TILE_ID = 712
    NAME = "Biome Tile Pattern #712"
    WALKABLE = True if 712 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.12, 0.2400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_712.TILE_ID, "walkable": TileBlueprint_712.WALKABLE, "cost": TileBlueprint_712.MOVEMENT_COST}


class TileBlueprint_713:
    TILE_ID = 713
    NAME = "Biome Tile Pattern #713"
    WALKABLE = True if 713 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.13, 0.2599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_713.TILE_ID, "walkable": TileBlueprint_713.WALKABLE, "cost": TileBlueprint_713.MOVEMENT_COST}


class TileBlueprint_714:
    TILE_ID = 714
    NAME = "Biome Tile Pattern #714"
    WALKABLE = True if 714 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.140000000000001, 0.28000000000000114)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_714.TILE_ID, "walkable": TileBlueprint_714.WALKABLE, "cost": TileBlueprint_714.MOVEMENT_COST}


class TileBlueprint_715:
    TILE_ID = 715
    NAME = "Biome Tile Pattern #715"
    WALKABLE = True if 715 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.15, 0.3000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_715.TILE_ID, "walkable": TileBlueprint_715.WALKABLE, "cost": TileBlueprint_715.MOVEMENT_COST}


class TileBlueprint_716:
    TILE_ID = 716
    NAME = "Biome Tile Pattern #716"
    WALKABLE = True if 716 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.16, 0.3200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_716.TILE_ID, "walkable": TileBlueprint_716.WALKABLE, "cost": TileBlueprint_716.MOVEMENT_COST}


class TileBlueprint_717:
    TILE_ID = 717
    NAME = "Biome Tile Pattern #717"
    WALKABLE = True if 717 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.17, 0.33999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_717.TILE_ID, "walkable": TileBlueprint_717.WALKABLE, "cost": TileBlueprint_717.MOVEMENT_COST}


class TileBlueprint_718:
    TILE_ID = 718
    NAME = "Biome Tile Pattern #718"
    WALKABLE = True if 718 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.18, 0.35999999999999943)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_718.TILE_ID, "walkable": TileBlueprint_718.WALKABLE, "cost": TileBlueprint_718.MOVEMENT_COST}


class TileBlueprint_719:
    TILE_ID = 719
    NAME = "Biome Tile Pattern #719"
    WALKABLE = True if 719 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.19, 0.3800000000000008)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_719.TILE_ID, "walkable": TileBlueprint_719.WALKABLE, "cost": TileBlueprint_719.MOVEMENT_COST}


class TileBlueprint_720:
    TILE_ID = 720
    NAME = "Biome Tile Pattern #720"
    WALKABLE = True if 720 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.2, 0.40000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_720.TILE_ID, "walkable": TileBlueprint_720.WALKABLE, "cost": TileBlueprint_720.MOVEMENT_COST}


class TileBlueprint_721:
    TILE_ID = 721
    NAME = "Biome Tile Pattern #721"
    WALKABLE = True if 721 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.21, 0.41999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_721.TILE_ID, "walkable": TileBlueprint_721.WALKABLE, "cost": TileBlueprint_721.MOVEMENT_COST}


class TileBlueprint_722:
    TILE_ID = 722
    NAME = "Biome Tile Pattern #722"
    WALKABLE = True if 722 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.22, 0.4399999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_722.TILE_ID, "walkable": TileBlueprint_722.WALKABLE, "cost": TileBlueprint_722.MOVEMENT_COST}


class TileBlueprint_723:
    TILE_ID = 723
    NAME = "Biome Tile Pattern #723"
    WALKABLE = True if 723 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.23, 0.46000000000000085)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_723.TILE_ID, "walkable": TileBlueprint_723.WALKABLE, "cost": TileBlueprint_723.MOVEMENT_COST}


class TileBlueprint_724:
    TILE_ID = 724
    NAME = "Biome Tile Pattern #724"
    WALKABLE = True if 724 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.24, 0.4800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_724.TILE_ID, "walkable": TileBlueprint_724.WALKABLE, "cost": TileBlueprint_724.MOVEMENT_COST}


class TileBlueprint_725:
    TILE_ID = 725
    NAME = "Biome Tile Pattern #725"
    WALKABLE = True if 725 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.25, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_725.TILE_ID, "walkable": TileBlueprint_725.WALKABLE, "cost": TileBlueprint_725.MOVEMENT_COST}


class TileBlueprint_726:
    TILE_ID = 726
    NAME = "Biome Tile Pattern #726"
    WALKABLE = True if 726 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.26, 0.5199999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_726.TILE_ID, "walkable": TileBlueprint_726.WALKABLE, "cost": TileBlueprint_726.MOVEMENT_COST}


class TileBlueprint_727:
    TILE_ID = 727
    NAME = "Biome Tile Pattern #727"
    WALKABLE = True if 727 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.2700000000000005, 0.5400000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_727.TILE_ID, "walkable": TileBlueprint_727.WALKABLE, "cost": TileBlueprint_727.MOVEMENT_COST}


class TileBlueprint_728:
    TILE_ID = 728
    NAME = "Biome Tile Pattern #728"
    WALKABLE = True if 728 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.28, 0.5600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_728.TILE_ID, "walkable": TileBlueprint_728.WALKABLE, "cost": TileBlueprint_728.MOVEMENT_COST}


class TileBlueprint_729:
    TILE_ID = 729
    NAME = "Biome Tile Pattern #729"
    WALKABLE = True if 729 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.29, 0.5800000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_729.TILE_ID, "walkable": TileBlueprint_729.WALKABLE, "cost": TileBlueprint_729.MOVEMENT_COST}


class TileBlueprint_730:
    TILE_ID = 730
    NAME = "Biome Tile Pattern #730"
    WALKABLE = True if 730 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.3, 0.5999999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_730.TILE_ID, "walkable": TileBlueprint_730.WALKABLE, "cost": TileBlueprint_730.MOVEMENT_COST}


class TileBlueprint_731:
    TILE_ID = 731
    NAME = "Biome Tile Pattern #731"
    WALKABLE = True if 731 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.3100000000000005, 0.620000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_731.TILE_ID, "walkable": TileBlueprint_731.WALKABLE, "cost": TileBlueprint_731.MOVEMENT_COST}


class TileBlueprint_732:
    TILE_ID = 732
    NAME = "Biome Tile Pattern #732"
    WALKABLE = True if 732 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.32, 0.6400000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_732.TILE_ID, "walkable": TileBlueprint_732.WALKABLE, "cost": TileBlueprint_732.MOVEMENT_COST}


class TileBlueprint_733:
    TILE_ID = 733
    NAME = "Biome Tile Pattern #733"
    WALKABLE = True if 733 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.33, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_733.TILE_ID, "walkable": TileBlueprint_733.WALKABLE, "cost": TileBlueprint_733.MOVEMENT_COST}


class TileBlueprint_734:
    TILE_ID = 734
    NAME = "Biome Tile Pattern #734"
    WALKABLE = True if 734 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.34, 0.6799999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_734.TILE_ID, "walkable": TileBlueprint_734.WALKABLE, "cost": TileBlueprint_734.MOVEMENT_COST}


class TileBlueprint_735:
    TILE_ID = 735
    NAME = "Biome Tile Pattern #735"
    WALKABLE = True if 735 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.3500000000000005, 0.7000000000000011)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_735.TILE_ID, "walkable": TileBlueprint_735.WALKABLE, "cost": TileBlueprint_735.MOVEMENT_COST}


class TileBlueprint_736:
    TILE_ID = 736
    NAME = "Biome Tile Pattern #736"
    WALKABLE = True if 736 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.36, 0.7200000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_736.TILE_ID, "walkable": TileBlueprint_736.WALKABLE, "cost": TileBlueprint_736.MOVEMENT_COST}


class TileBlueprint_737:
    TILE_ID = 737
    NAME = "Biome Tile Pattern #737"
    WALKABLE = True if 737 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.37, 0.7400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_737.TILE_ID, "walkable": TileBlueprint_737.WALKABLE, "cost": TileBlueprint_737.MOVEMENT_COST}


class TileBlueprint_738:
    TILE_ID = 738
    NAME = "Biome Tile Pattern #738"
    WALKABLE = True if 738 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.38, 0.7599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_738.TILE_ID, "walkable": TileBlueprint_738.WALKABLE, "cost": TileBlueprint_738.MOVEMENT_COST}


class TileBlueprint_739:
    TILE_ID = 739
    NAME = "Biome Tile Pattern #739"
    WALKABLE = True if 739 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.390000000000001, 0.7800000000000011)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_739.TILE_ID, "walkable": TileBlueprint_739.WALKABLE, "cost": TileBlueprint_739.MOVEMENT_COST}


class TileBlueprint_740:
    TILE_ID = 740
    NAME = "Biome Tile Pattern #740"
    WALKABLE = True if 740 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.4, 0.8000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_740.TILE_ID, "walkable": TileBlueprint_740.WALKABLE, "cost": TileBlueprint_740.MOVEMENT_COST}


class TileBlueprint_741:
    TILE_ID = 741
    NAME = "Biome Tile Pattern #741"
    WALKABLE = True if 741 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.41, 0.8200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_741.TILE_ID, "walkable": TileBlueprint_741.WALKABLE, "cost": TileBlueprint_741.MOVEMENT_COST}


class TileBlueprint_742:
    TILE_ID = 742
    NAME = "Biome Tile Pattern #742"
    WALKABLE = True if 742 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.42, 0.8399999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_742.TILE_ID, "walkable": TileBlueprint_742.WALKABLE, "cost": TileBlueprint_742.MOVEMENT_COST}


class TileBlueprint_743:
    TILE_ID = 743
    NAME = "Biome Tile Pattern #743"
    WALKABLE = True if 743 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.43, 0.8599999999999994)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_743.TILE_ID, "walkable": TileBlueprint_743.WALKABLE, "cost": TileBlueprint_743.MOVEMENT_COST}


class TileBlueprint_744:
    TILE_ID = 744
    NAME = "Biome Tile Pattern #744"
    WALKABLE = True if 744 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.44, 0.8800000000000008)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_744.TILE_ID, "walkable": TileBlueprint_744.WALKABLE, "cost": TileBlueprint_744.MOVEMENT_COST}


class TileBlueprint_745:
    TILE_ID = 745
    NAME = "Biome Tile Pattern #745"
    WALKABLE = True if 745 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.45, 0.9000000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_745.TILE_ID, "walkable": TileBlueprint_745.WALKABLE, "cost": TileBlueprint_745.MOVEMENT_COST}


class TileBlueprint_746:
    TILE_ID = 746
    NAME = "Biome Tile Pattern #746"
    WALKABLE = True if 746 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.46, 0.9199999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_746.TILE_ID, "walkable": TileBlueprint_746.WALKABLE, "cost": TileBlueprint_746.MOVEMENT_COST}


class TileBlueprint_747:
    TILE_ID = 747
    NAME = "Biome Tile Pattern #747"
    WALKABLE = True if 747 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.47, 0.9399999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_747.TILE_ID, "walkable": TileBlueprint_747.WALKABLE, "cost": TileBlueprint_747.MOVEMENT_COST}


class TileBlueprint_748:
    TILE_ID = 748
    NAME = "Biome Tile Pattern #748"
    WALKABLE = True if 748 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.48, 0.9600000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_748.TILE_ID, "walkable": TileBlueprint_748.WALKABLE, "cost": TileBlueprint_748.MOVEMENT_COST}


class TileBlueprint_749:
    TILE_ID = 749
    NAME = "Biome Tile Pattern #749"
    WALKABLE = True if 749 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.49, 0.9800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_749.TILE_ID, "walkable": TileBlueprint_749.WALKABLE, "cost": TileBlueprint_749.MOVEMENT_COST}


class TileBlueprint_750:
    TILE_ID = 750
    NAME = "Biome Tile Pattern #750"
    WALKABLE = True if 750 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.5, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_750.TILE_ID, "walkable": TileBlueprint_750.WALKABLE, "cost": TileBlueprint_750.MOVEMENT_COST}


class TileBlueprint_751:
    TILE_ID = 751
    NAME = "Biome Tile Pattern #751"
    WALKABLE = True if 751 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.51, 0.019999999999999574)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_751.TILE_ID, "walkable": TileBlueprint_751.WALKABLE, "cost": TileBlueprint_751.MOVEMENT_COST}


class TileBlueprint_752:
    TILE_ID = 752
    NAME = "Biome Tile Pattern #752"
    WALKABLE = True if 752 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.5200000000000005, 0.040000000000000924)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_752.TILE_ID, "walkable": TileBlueprint_752.WALKABLE, "cost": TileBlueprint_752.MOVEMENT_COST}


class TileBlueprint_753:
    TILE_ID = 753
    NAME = "Biome Tile Pattern #753"
    WALKABLE = True if 753 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.53, 0.0600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_753.TILE_ID, "walkable": TileBlueprint_753.WALKABLE, "cost": TileBlueprint_753.MOVEMENT_COST}


class TileBlueprint_754:
    TILE_ID = 754
    NAME = "Biome Tile Pattern #754"
    WALKABLE = True if 754 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.54, 0.08000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_754.TILE_ID, "walkable": TileBlueprint_754.WALKABLE, "cost": TileBlueprint_754.MOVEMENT_COST}


class TileBlueprint_755:
    TILE_ID = 755
    NAME = "Biome Tile Pattern #755"
    WALKABLE = True if 755 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.55, 0.09999999999999964)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_755.TILE_ID, "walkable": TileBlueprint_755.WALKABLE, "cost": TileBlueprint_755.MOVEMENT_COST}


class TileBlueprint_756:
    TILE_ID = 756
    NAME = "Biome Tile Pattern #756"
    WALKABLE = True if 756 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.5600000000000005, 0.120000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_756.TILE_ID, "walkable": TileBlueprint_756.WALKABLE, "cost": TileBlueprint_756.MOVEMENT_COST}


class TileBlueprint_757:
    TILE_ID = 757
    NAME = "Biome Tile Pattern #757"
    WALKABLE = True if 757 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.57, 0.14000000000000057)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_757.TILE_ID, "walkable": TileBlueprint_757.WALKABLE, "cost": TileBlueprint_757.MOVEMENT_COST}


class TileBlueprint_758:
    TILE_ID = 758
    NAME = "Biome Tile Pattern #758"
    WALKABLE = True if 758 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.58, 0.16000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_758.TILE_ID, "walkable": TileBlueprint_758.WALKABLE, "cost": TileBlueprint_758.MOVEMENT_COST}


class TileBlueprint_759:
    TILE_ID = 759
    NAME = "Biome Tile Pattern #759"
    WALKABLE = True if 759 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.59, 0.17999999999999972)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_759.TILE_ID, "walkable": TileBlueprint_759.WALKABLE, "cost": TileBlueprint_759.MOVEMENT_COST}


class TileBlueprint_760:
    TILE_ID = 760
    NAME = "Biome Tile Pattern #760"
    WALKABLE = True if 760 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.6000000000000005, 0.20000000000000107)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_760.TILE_ID, "walkable": TileBlueprint_760.WALKABLE, "cost": TileBlueprint_760.MOVEMENT_COST}


class TileBlueprint_761:
    TILE_ID = 761
    NAME = "Biome Tile Pattern #761"
    WALKABLE = True if 761 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.61, 0.22000000000000064)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_761.TILE_ID, "walkable": TileBlueprint_761.WALKABLE, "cost": TileBlueprint_761.MOVEMENT_COST}


class TileBlueprint_762:
    TILE_ID = 762
    NAME = "Biome Tile Pattern #762"
    WALKABLE = True if 762 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.62, 0.2400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_762.TILE_ID, "walkable": TileBlueprint_762.WALKABLE, "cost": TileBlueprint_762.MOVEMENT_COST}


class TileBlueprint_763:
    TILE_ID = 763
    NAME = "Biome Tile Pattern #763"
    WALKABLE = True if 763 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.63, 0.2599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_763.TILE_ID, "walkable": TileBlueprint_763.WALKABLE, "cost": TileBlueprint_763.MOVEMENT_COST}


class TileBlueprint_764:
    TILE_ID = 764
    NAME = "Biome Tile Pattern #764"
    WALKABLE = True if 764 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.640000000000001, 0.28000000000000114)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_764.TILE_ID, "walkable": TileBlueprint_764.WALKABLE, "cost": TileBlueprint_764.MOVEMENT_COST}


class TileBlueprint_765:
    TILE_ID = 765
    NAME = "Biome Tile Pattern #765"
    WALKABLE = True if 765 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.65, 0.3000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_765.TILE_ID, "walkable": TileBlueprint_765.WALKABLE, "cost": TileBlueprint_765.MOVEMENT_COST}


class TileBlueprint_766:
    TILE_ID = 766
    NAME = "Biome Tile Pattern #766"
    WALKABLE = True if 766 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.66, 0.3200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_766.TILE_ID, "walkable": TileBlueprint_766.WALKABLE, "cost": TileBlueprint_766.MOVEMENT_COST}


class TileBlueprint_767:
    TILE_ID = 767
    NAME = "Biome Tile Pattern #767"
    WALKABLE = True if 767 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.67, 0.33999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_767.TILE_ID, "walkable": TileBlueprint_767.WALKABLE, "cost": TileBlueprint_767.MOVEMENT_COST}


class TileBlueprint_768:
    TILE_ID = 768
    NAME = "Biome Tile Pattern #768"
    WALKABLE = True if 768 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.68, 0.35999999999999943)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_768.TILE_ID, "walkable": TileBlueprint_768.WALKABLE, "cost": TileBlueprint_768.MOVEMENT_COST}


class TileBlueprint_769:
    TILE_ID = 769
    NAME = "Biome Tile Pattern #769"
    WALKABLE = True if 769 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.69, 0.3800000000000008)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_769.TILE_ID, "walkable": TileBlueprint_769.WALKABLE, "cost": TileBlueprint_769.MOVEMENT_COST}


class TileBlueprint_770:
    TILE_ID = 770
    NAME = "Biome Tile Pattern #770"
    WALKABLE = True if 770 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.7, 0.40000000000000036)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_770.TILE_ID, "walkable": TileBlueprint_770.WALKABLE, "cost": TileBlueprint_770.MOVEMENT_COST}


class TileBlueprint_771:
    TILE_ID = 771
    NAME = "Biome Tile Pattern #771"
    WALKABLE = True if 771 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.71, 0.41999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_771.TILE_ID, "walkable": TileBlueprint_771.WALKABLE, "cost": TileBlueprint_771.MOVEMENT_COST}


class TileBlueprint_772:
    TILE_ID = 772
    NAME = "Biome Tile Pattern #772"
    WALKABLE = True if 772 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.72, 0.4399999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_772.TILE_ID, "walkable": TileBlueprint_772.WALKABLE, "cost": TileBlueprint_772.MOVEMENT_COST}


class TileBlueprint_773:
    TILE_ID = 773
    NAME = "Biome Tile Pattern #773"
    WALKABLE = True if 773 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.73, 0.46000000000000085)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_773.TILE_ID, "walkable": TileBlueprint_773.WALKABLE, "cost": TileBlueprint_773.MOVEMENT_COST}


class TileBlueprint_774:
    TILE_ID = 774
    NAME = "Biome Tile Pattern #774"
    WALKABLE = True if 774 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.74, 0.4800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_774.TILE_ID, "walkable": TileBlueprint_774.WALKABLE, "cost": TileBlueprint_774.MOVEMENT_COST}


class TileBlueprint_775:
    TILE_ID = 775
    NAME = "Biome Tile Pattern #775"
    WALKABLE = True if 775 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.75, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_775.TILE_ID, "walkable": TileBlueprint_775.WALKABLE, "cost": TileBlueprint_775.MOVEMENT_COST}


class TileBlueprint_776:
    TILE_ID = 776
    NAME = "Biome Tile Pattern #776"
    WALKABLE = True if 776 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.76, 0.5199999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_776.TILE_ID, "walkable": TileBlueprint_776.WALKABLE, "cost": TileBlueprint_776.MOVEMENT_COST}


class TileBlueprint_777:
    TILE_ID = 777
    NAME = "Biome Tile Pattern #777"
    WALKABLE = True if 777 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.7700000000000005, 0.5400000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_777.TILE_ID, "walkable": TileBlueprint_777.WALKABLE, "cost": TileBlueprint_777.MOVEMENT_COST}


class TileBlueprint_778:
    TILE_ID = 778
    NAME = "Biome Tile Pattern #778"
    WALKABLE = True if 778 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.78, 0.5600000000000005)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_778.TILE_ID, "walkable": TileBlueprint_778.WALKABLE, "cost": TileBlueprint_778.MOVEMENT_COST}


class TileBlueprint_779:
    TILE_ID = 779
    NAME = "Biome Tile Pattern #779"
    WALKABLE = True if 779 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.79, 0.5800000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_779.TILE_ID, "walkable": TileBlueprint_779.WALKABLE, "cost": TileBlueprint_779.MOVEMENT_COST}


class TileBlueprint_780:
    TILE_ID = 780
    NAME = "Biome Tile Pattern #780"
    WALKABLE = True if 780 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.8, 0.5999999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_780.TILE_ID, "walkable": TileBlueprint_780.WALKABLE, "cost": TileBlueprint_780.MOVEMENT_COST}


class TileBlueprint_781:
    TILE_ID = 781
    NAME = "Biome Tile Pattern #781"
    WALKABLE = True if 781 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.8100000000000005, 0.620000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_781.TILE_ID, "walkable": TileBlueprint_781.WALKABLE, "cost": TileBlueprint_781.MOVEMENT_COST}


class TileBlueprint_782:
    TILE_ID = 782
    NAME = "Biome Tile Pattern #782"
    WALKABLE = True if 782 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.82, 0.6400000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_782.TILE_ID, "walkable": TileBlueprint_782.WALKABLE, "cost": TileBlueprint_782.MOVEMENT_COST}


class TileBlueprint_783:
    TILE_ID = 783
    NAME = "Biome Tile Pattern #783"
    WALKABLE = True if 783 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.83, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_783.TILE_ID, "walkable": TileBlueprint_783.WALKABLE, "cost": TileBlueprint_783.MOVEMENT_COST}


class TileBlueprint_784:
    TILE_ID = 784
    NAME = "Biome Tile Pattern #784"
    WALKABLE = True if 784 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.84, 0.6799999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_784.TILE_ID, "walkable": TileBlueprint_784.WALKABLE, "cost": TileBlueprint_784.MOVEMENT_COST}


class TileBlueprint_785:
    TILE_ID = 785
    NAME = "Biome Tile Pattern #785"
    WALKABLE = True if 785 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.8500000000000005, 0.7000000000000011)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_785.TILE_ID, "walkable": TileBlueprint_785.WALKABLE, "cost": TileBlueprint_785.MOVEMENT_COST}


class TileBlueprint_786:
    TILE_ID = 786
    NAME = "Biome Tile Pattern #786"
    WALKABLE = True if 786 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.86, 0.7200000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_786.TILE_ID, "walkable": TileBlueprint_786.WALKABLE, "cost": TileBlueprint_786.MOVEMENT_COST}


class TileBlueprint_787:
    TILE_ID = 787
    NAME = "Biome Tile Pattern #787"
    WALKABLE = True if 787 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.87, 0.7400000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_787.TILE_ID, "walkable": TileBlueprint_787.WALKABLE, "cost": TileBlueprint_787.MOVEMENT_COST}


class TileBlueprint_788:
    TILE_ID = 788
    NAME = "Biome Tile Pattern #788"
    WALKABLE = True if 788 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.88, 0.7599999999999998)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_788.TILE_ID, "walkable": TileBlueprint_788.WALKABLE, "cost": TileBlueprint_788.MOVEMENT_COST}


class TileBlueprint_789:
    TILE_ID = 789
    NAME = "Biome Tile Pattern #789"
    WALKABLE = True if 789 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.890000000000001, 0.7800000000000011)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_789.TILE_ID, "walkable": TileBlueprint_789.WALKABLE, "cost": TileBlueprint_789.MOVEMENT_COST}


class TileBlueprint_790:
    TILE_ID = 790
    NAME = "Biome Tile Pattern #790"
    WALKABLE = True if 790 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.9, 0.8000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_790.TILE_ID, "walkable": TileBlueprint_790.WALKABLE, "cost": TileBlueprint_790.MOVEMENT_COST}


class TileBlueprint_791:
    TILE_ID = 791
    NAME = "Biome Tile Pattern #791"
    WALKABLE = True if 791 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.91, 0.8200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_791.TILE_ID, "walkable": TileBlueprint_791.WALKABLE, "cost": TileBlueprint_791.MOVEMENT_COST}


class TileBlueprint_792:
    TILE_ID = 792
    NAME = "Biome Tile Pattern #792"
    WALKABLE = True if 792 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.92, 0.8399999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_792.TILE_ID, "walkable": TileBlueprint_792.WALKABLE, "cost": TileBlueprint_792.MOVEMENT_COST}


class TileBlueprint_793:
    TILE_ID = 793
    NAME = "Biome Tile Pattern #793"
    WALKABLE = True if 793 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.930000000000001, 0.8600000000000012)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_793.TILE_ID, "walkable": TileBlueprint_793.WALKABLE, "cost": TileBlueprint_793.MOVEMENT_COST}


class TileBlueprint_794:
    TILE_ID = 794
    NAME = "Biome Tile Pattern #794"
    WALKABLE = True if 794 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.94, 0.8800000000000008)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_794.TILE_ID, "walkable": TileBlueprint_794.WALKABLE, "cost": TileBlueprint_794.MOVEMENT_COST}


class TileBlueprint_795:
    TILE_ID = 795
    NAME = "Biome Tile Pattern #795"
    WALKABLE = True if 795 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (7.95, 0.9000000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_795.TILE_ID, "walkable": TileBlueprint_795.WALKABLE, "cost": TileBlueprint_795.MOVEMENT_COST}


class TileBlueprint_796:
    TILE_ID = 796
    NAME = "Biome Tile Pattern #796"
    WALKABLE = True if 796 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (7.96, 0.9199999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_796.TILE_ID, "walkable": TileBlueprint_796.WALKABLE, "cost": TileBlueprint_796.MOVEMENT_COST}


class TileBlueprint_797:
    TILE_ID = 797
    NAME = "Biome Tile Pattern #797"
    WALKABLE = True if 797 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (7.97, 0.9399999999999995)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_797.TILE_ID, "walkable": TileBlueprint_797.WALKABLE, "cost": TileBlueprint_797.MOVEMENT_COST}


class TileBlueprint_798:
    TILE_ID = 798
    NAME = "Biome Tile Pattern #798"
    WALKABLE = True if 798 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (7.98, 0.9600000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_798.TILE_ID, "walkable": TileBlueprint_798.WALKABLE, "cost": TileBlueprint_798.MOVEMENT_COST}


class TileBlueprint_799:
    TILE_ID = 799
    NAME = "Biome Tile Pattern #799"
    WALKABLE = True if 799 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (7.99, 0.9800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_799.TILE_ID, "walkable": TileBlueprint_799.WALKABLE, "cost": TileBlueprint_799.MOVEMENT_COST}


class TileBlueprint_800:
    TILE_ID = 800
    NAME = "Biome Tile Pattern #800"
    WALKABLE = True if 800 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.0, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_800.TILE_ID, "walkable": TileBlueprint_800.WALKABLE, "cost": TileBlueprint_800.MOVEMENT_COST}


class TileBlueprint_801:
    TILE_ID = 801
    NAME = "Biome Tile Pattern #801"
    WALKABLE = True if 801 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.01, 0.019999999999999574)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_801.TILE_ID, "walkable": TileBlueprint_801.WALKABLE, "cost": TileBlueprint_801.MOVEMENT_COST}


class TileBlueprint_802:
    TILE_ID = 802
    NAME = "Biome Tile Pattern #802"
    WALKABLE = True if 802 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.02, 0.03999999999999915)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_802.TILE_ID, "walkable": TileBlueprint_802.WALKABLE, "cost": TileBlueprint_802.MOVEMENT_COST}


class TileBlueprint_803:
    TILE_ID = 803
    NAME = "Biome Tile Pattern #803"
    WALKABLE = True if 803 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.03, 0.05999999999999872)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_803.TILE_ID, "walkable": TileBlueprint_803.WALKABLE, "cost": TileBlueprint_803.MOVEMENT_COST}


class TileBlueprint_804:
    TILE_ID = 804
    NAME = "Biome Tile Pattern #804"
    WALKABLE = True if 804 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.040000000000001, 0.08000000000000185)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_804.TILE_ID, "walkable": TileBlueprint_804.WALKABLE, "cost": TileBlueprint_804.MOVEMENT_COST}


class TileBlueprint_805:
    TILE_ID = 805
    NAME = "Biome Tile Pattern #805"
    WALKABLE = True if 805 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.05, 0.10000000000000142)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_805.TILE_ID, "walkable": TileBlueprint_805.WALKABLE, "cost": TileBlueprint_805.MOVEMENT_COST}


class TileBlueprint_806:
    TILE_ID = 806
    NAME = "Biome Tile Pattern #806"
    WALKABLE = True if 806 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.06, 0.120000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_806.TILE_ID, "walkable": TileBlueprint_806.WALKABLE, "cost": TileBlueprint_806.MOVEMENT_COST}


class TileBlueprint_807:
    TILE_ID = 807
    NAME = "Biome Tile Pattern #807"
    WALKABLE = True if 807 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.07, 0.14000000000000057)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_807.TILE_ID, "walkable": TileBlueprint_807.WALKABLE, "cost": TileBlueprint_807.MOVEMENT_COST}


class TileBlueprint_808:
    TILE_ID = 808
    NAME = "Biome Tile Pattern #808"
    WALKABLE = True if 808 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.08, 0.16000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_808.TILE_ID, "walkable": TileBlueprint_808.WALKABLE, "cost": TileBlueprint_808.MOVEMENT_COST}


class TileBlueprint_809:
    TILE_ID = 809
    NAME = "Biome Tile Pattern #809"
    WALKABLE = True if 809 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.09, 0.17999999999999972)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_809.TILE_ID, "walkable": TileBlueprint_809.WALKABLE, "cost": TileBlueprint_809.MOVEMENT_COST}


class TileBlueprint_810:
    TILE_ID = 810
    NAME = "Biome Tile Pattern #810"
    WALKABLE = True if 810 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.1, 0.1999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_810.TILE_ID, "walkable": TileBlueprint_810.WALKABLE, "cost": TileBlueprint_810.MOVEMENT_COST}


class TileBlueprint_811:
    TILE_ID = 811
    NAME = "Biome Tile Pattern #811"
    WALKABLE = True if 811 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.11, 0.21999999999999886)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_811.TILE_ID, "walkable": TileBlueprint_811.WALKABLE, "cost": TileBlueprint_811.MOVEMENT_COST}


class TileBlueprint_812:
    TILE_ID = 812
    NAME = "Biome Tile Pattern #812"
    WALKABLE = True if 812 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.120000000000001, 0.240000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_812.TILE_ID, "walkable": TileBlueprint_812.WALKABLE, "cost": TileBlueprint_812.MOVEMENT_COST}


class TileBlueprint_813:
    TILE_ID = 813
    NAME = "Biome Tile Pattern #813"
    WALKABLE = True if 813 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.13, 0.26000000000000156)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_813.TILE_ID, "walkable": TileBlueprint_813.WALKABLE, "cost": TileBlueprint_813.MOVEMENT_COST}


class TileBlueprint_814:
    TILE_ID = 814
    NAME = "Biome Tile Pattern #814"
    WALKABLE = True if 814 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.14, 0.28000000000000114)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_814.TILE_ID, "walkable": TileBlueprint_814.WALKABLE, "cost": TileBlueprint_814.MOVEMENT_COST}


class TileBlueprint_815:
    TILE_ID = 815
    NAME = "Biome Tile Pattern #815"
    WALKABLE = True if 815 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.15, 0.3000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_815.TILE_ID, "walkable": TileBlueprint_815.WALKABLE, "cost": TileBlueprint_815.MOVEMENT_COST}


class TileBlueprint_816:
    TILE_ID = 816
    NAME = "Biome Tile Pattern #816"
    WALKABLE = True if 816 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.16, 0.3200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_816.TILE_ID, "walkable": TileBlueprint_816.WALKABLE, "cost": TileBlueprint_816.MOVEMENT_COST}


class TileBlueprint_817:
    TILE_ID = 817
    NAME = "Biome Tile Pattern #817"
    WALKABLE = True if 817 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.17, 0.33999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_817.TILE_ID, "walkable": TileBlueprint_817.WALKABLE, "cost": TileBlueprint_817.MOVEMENT_COST}


class TileBlueprint_818:
    TILE_ID = 818
    NAME = "Biome Tile Pattern #818"
    WALKABLE = True if 818 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.18, 0.35999999999999943)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_818.TILE_ID, "walkable": TileBlueprint_818.WALKABLE, "cost": TileBlueprint_818.MOVEMENT_COST}


class TileBlueprint_819:
    TILE_ID = 819
    NAME = "Biome Tile Pattern #819"
    WALKABLE = True if 819 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.19, 0.379999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_819.TILE_ID, "walkable": TileBlueprint_819.WALKABLE, "cost": TileBlueprint_819.MOVEMENT_COST}


class TileBlueprint_820:
    TILE_ID = 820
    NAME = "Biome Tile Pattern #820"
    WALKABLE = True if 820 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.2, 0.3999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_820.TILE_ID, "walkable": TileBlueprint_820.WALKABLE, "cost": TileBlueprint_820.MOVEMENT_COST}


class TileBlueprint_821:
    TILE_ID = 821
    NAME = "Biome Tile Pattern #821"
    WALKABLE = True if 821 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.21, 0.4200000000000017)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_821.TILE_ID, "walkable": TileBlueprint_821.WALKABLE, "cost": TileBlueprint_821.MOVEMENT_COST}


class TileBlueprint_822:
    TILE_ID = 822
    NAME = "Biome Tile Pattern #822"
    WALKABLE = True if 822 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.22, 0.4400000000000013)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_822.TILE_ID, "walkable": TileBlueprint_822.WALKABLE, "cost": TileBlueprint_822.MOVEMENT_COST}


class TileBlueprint_823:
    TILE_ID = 823
    NAME = "Biome Tile Pattern #823"
    WALKABLE = True if 823 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.23, 0.46000000000000085)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_823.TILE_ID, "walkable": TileBlueprint_823.WALKABLE, "cost": TileBlueprint_823.MOVEMENT_COST}


class TileBlueprint_824:
    TILE_ID = 824
    NAME = "Biome Tile Pattern #824"
    WALKABLE = True if 824 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.24, 0.4800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_824.TILE_ID, "walkable": TileBlueprint_824.WALKABLE, "cost": TileBlueprint_824.MOVEMENT_COST}


class TileBlueprint_825:
    TILE_ID = 825
    NAME = "Biome Tile Pattern #825"
    WALKABLE = True if 825 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.25, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_825.TILE_ID, "walkable": TileBlueprint_825.WALKABLE, "cost": TileBlueprint_825.MOVEMENT_COST}


class TileBlueprint_826:
    TILE_ID = 826
    NAME = "Biome Tile Pattern #826"
    WALKABLE = True if 826 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.26, 0.5199999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_826.TILE_ID, "walkable": TileBlueprint_826.WALKABLE, "cost": TileBlueprint_826.MOVEMENT_COST}


class TileBlueprint_827:
    TILE_ID = 827
    NAME = "Biome Tile Pattern #827"
    WALKABLE = True if 827 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.27, 0.5399999999999991)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_827.TILE_ID, "walkable": TileBlueprint_827.WALKABLE, "cost": TileBlueprint_827.MOVEMENT_COST}


class TileBlueprint_828:
    TILE_ID = 828
    NAME = "Biome Tile Pattern #828"
    WALKABLE = True if 828 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.28, 0.5599999999999987)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_828.TILE_ID, "walkable": TileBlueprint_828.WALKABLE, "cost": TileBlueprint_828.MOVEMENT_COST}


class TileBlueprint_829:
    TILE_ID = 829
    NAME = "Biome Tile Pattern #829"
    WALKABLE = True if 829 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.290000000000001, 0.5800000000000018)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_829.TILE_ID, "walkable": TileBlueprint_829.WALKABLE, "cost": TileBlueprint_829.MOVEMENT_COST}


class TileBlueprint_830:
    TILE_ID = 830
    NAME = "Biome Tile Pattern #830"
    WALKABLE = True if 830 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.3, 0.6000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_830.TILE_ID, "walkable": TileBlueprint_830.WALKABLE, "cost": TileBlueprint_830.MOVEMENT_COST}


class TileBlueprint_831:
    TILE_ID = 831
    NAME = "Biome Tile Pattern #831"
    WALKABLE = True if 831 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.31, 0.620000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_831.TILE_ID, "walkable": TileBlueprint_831.WALKABLE, "cost": TileBlueprint_831.MOVEMENT_COST}


class TileBlueprint_832:
    TILE_ID = 832
    NAME = "Biome Tile Pattern #832"
    WALKABLE = True if 832 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.32, 0.6400000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_832.TILE_ID, "walkable": TileBlueprint_832.WALKABLE, "cost": TileBlueprint_832.MOVEMENT_COST}


class TileBlueprint_833:
    TILE_ID = 833
    NAME = "Biome Tile Pattern #833"
    WALKABLE = True if 833 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.33, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_833.TILE_ID, "walkable": TileBlueprint_833.WALKABLE, "cost": TileBlueprint_833.MOVEMENT_COST}


class TileBlueprint_834:
    TILE_ID = 834
    NAME = "Biome Tile Pattern #834"
    WALKABLE = True if 834 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.34, 0.6799999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_834.TILE_ID, "walkable": TileBlueprint_834.WALKABLE, "cost": TileBlueprint_834.MOVEMENT_COST}


class TileBlueprint_835:
    TILE_ID = 835
    NAME = "Biome Tile Pattern #835"
    WALKABLE = True if 835 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.35, 0.6999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_835.TILE_ID, "walkable": TileBlueprint_835.WALKABLE, "cost": TileBlueprint_835.MOVEMENT_COST}


class TileBlueprint_836:
    TILE_ID = 836
    NAME = "Biome Tile Pattern #836"
    WALKABLE = True if 836 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.36, 0.7199999999999989)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_836.TILE_ID, "walkable": TileBlueprint_836.WALKABLE, "cost": TileBlueprint_836.MOVEMENT_COST}


class TileBlueprint_837:
    TILE_ID = 837
    NAME = "Biome Tile Pattern #837"
    WALKABLE = True if 837 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.370000000000001, 0.740000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_837.TILE_ID, "walkable": TileBlueprint_837.WALKABLE, "cost": TileBlueprint_837.MOVEMENT_COST}


class TileBlueprint_838:
    TILE_ID = 838
    NAME = "Biome Tile Pattern #838"
    WALKABLE = True if 838 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.38, 0.7600000000000016)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_838.TILE_ID, "walkable": TileBlueprint_838.WALKABLE, "cost": TileBlueprint_838.MOVEMENT_COST}


class TileBlueprint_839:
    TILE_ID = 839
    NAME = "Biome Tile Pattern #839"
    WALKABLE = True if 839 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.39, 0.7800000000000011)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_839.TILE_ID, "walkable": TileBlueprint_839.WALKABLE, "cost": TileBlueprint_839.MOVEMENT_COST}


class TileBlueprint_840:
    TILE_ID = 840
    NAME = "Biome Tile Pattern #840"
    WALKABLE = True if 840 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.4, 0.8000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_840.TILE_ID, "walkable": TileBlueprint_840.WALKABLE, "cost": TileBlueprint_840.MOVEMENT_COST}


class TileBlueprint_841:
    TILE_ID = 841
    NAME = "Biome Tile Pattern #841"
    WALKABLE = True if 841 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.41, 0.8200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_841.TILE_ID, "walkable": TileBlueprint_841.WALKABLE, "cost": TileBlueprint_841.MOVEMENT_COST}


class TileBlueprint_842:
    TILE_ID = 842
    NAME = "Biome Tile Pattern #842"
    WALKABLE = True if 842 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.42, 0.8399999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_842.TILE_ID, "walkable": TileBlueprint_842.WALKABLE, "cost": TileBlueprint_842.MOVEMENT_COST}


class TileBlueprint_843:
    TILE_ID = 843
    NAME = "Biome Tile Pattern #843"
    WALKABLE = True if 843 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.43, 0.8599999999999994)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_843.TILE_ID, "walkable": TileBlueprint_843.WALKABLE, "cost": TileBlueprint_843.MOVEMENT_COST}


class TileBlueprint_844:
    TILE_ID = 844
    NAME = "Biome Tile Pattern #844"
    WALKABLE = True if 844 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.44, 0.879999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_844.TILE_ID, "walkable": TileBlueprint_844.WALKABLE, "cost": TileBlueprint_844.MOVEMENT_COST}


class TileBlueprint_845:
    TILE_ID = 845
    NAME = "Biome Tile Pattern #845"
    WALKABLE = True if 845 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.45, 0.8999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_845.TILE_ID, "walkable": TileBlueprint_845.WALKABLE, "cost": TileBlueprint_845.MOVEMENT_COST}


class TileBlueprint_846:
    TILE_ID = 846
    NAME = "Biome Tile Pattern #846"
    WALKABLE = True if 846 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.46, 0.9200000000000017)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_846.TILE_ID, "walkable": TileBlueprint_846.WALKABLE, "cost": TileBlueprint_846.MOVEMENT_COST}


class TileBlueprint_847:
    TILE_ID = 847
    NAME = "Biome Tile Pattern #847"
    WALKABLE = True if 847 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.47, 0.9400000000000013)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_847.TILE_ID, "walkable": TileBlueprint_847.WALKABLE, "cost": TileBlueprint_847.MOVEMENT_COST}


class TileBlueprint_848:
    TILE_ID = 848
    NAME = "Biome Tile Pattern #848"
    WALKABLE = True if 848 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.48, 0.9600000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_848.TILE_ID, "walkable": TileBlueprint_848.WALKABLE, "cost": TileBlueprint_848.MOVEMENT_COST}


class TileBlueprint_849:
    TILE_ID = 849
    NAME = "Biome Tile Pattern #849"
    WALKABLE = True if 849 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.49, 0.9800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_849.TILE_ID, "walkable": TileBlueprint_849.WALKABLE, "cost": TileBlueprint_849.MOVEMENT_COST}


class TileBlueprint_850:
    TILE_ID = 850
    NAME = "Biome Tile Pattern #850"
    WALKABLE = True if 850 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.5, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_850.TILE_ID, "walkable": TileBlueprint_850.WALKABLE, "cost": TileBlueprint_850.MOVEMENT_COST}


class TileBlueprint_851:
    TILE_ID = 851
    NAME = "Biome Tile Pattern #851"
    WALKABLE = True if 851 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.51, 0.019999999999999574)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_851.TILE_ID, "walkable": TileBlueprint_851.WALKABLE, "cost": TileBlueprint_851.MOVEMENT_COST}


class TileBlueprint_852:
    TILE_ID = 852
    NAME = "Biome Tile Pattern #852"
    WALKABLE = True if 852 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.52, 0.03999999999999915)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_852.TILE_ID, "walkable": TileBlueprint_852.WALKABLE, "cost": TileBlueprint_852.MOVEMENT_COST}


class TileBlueprint_853:
    TILE_ID = 853
    NAME = "Biome Tile Pattern #853"
    WALKABLE = True if 853 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.53, 0.05999999999999872)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_853.TILE_ID, "walkable": TileBlueprint_853.WALKABLE, "cost": TileBlueprint_853.MOVEMENT_COST}


class TileBlueprint_854:
    TILE_ID = 854
    NAME = "Biome Tile Pattern #854"
    WALKABLE = True if 854 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.540000000000001, 0.08000000000000185)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_854.TILE_ID, "walkable": TileBlueprint_854.WALKABLE, "cost": TileBlueprint_854.MOVEMENT_COST}


class TileBlueprint_855:
    TILE_ID = 855
    NAME = "Biome Tile Pattern #855"
    WALKABLE = True if 855 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.55, 0.10000000000000142)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_855.TILE_ID, "walkable": TileBlueprint_855.WALKABLE, "cost": TileBlueprint_855.MOVEMENT_COST}


class TileBlueprint_856:
    TILE_ID = 856
    NAME = "Biome Tile Pattern #856"
    WALKABLE = True if 856 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.56, 0.120000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_856.TILE_ID, "walkable": TileBlueprint_856.WALKABLE, "cost": TileBlueprint_856.MOVEMENT_COST}


class TileBlueprint_857:
    TILE_ID = 857
    NAME = "Biome Tile Pattern #857"
    WALKABLE = True if 857 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.57, 0.14000000000000057)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_857.TILE_ID, "walkable": TileBlueprint_857.WALKABLE, "cost": TileBlueprint_857.MOVEMENT_COST}


class TileBlueprint_858:
    TILE_ID = 858
    NAME = "Biome Tile Pattern #858"
    WALKABLE = True if 858 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.58, 0.16000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_858.TILE_ID, "walkable": TileBlueprint_858.WALKABLE, "cost": TileBlueprint_858.MOVEMENT_COST}


class TileBlueprint_859:
    TILE_ID = 859
    NAME = "Biome Tile Pattern #859"
    WALKABLE = True if 859 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.59, 0.17999999999999972)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_859.TILE_ID, "walkable": TileBlueprint_859.WALKABLE, "cost": TileBlueprint_859.MOVEMENT_COST}


class TileBlueprint_860:
    TILE_ID = 860
    NAME = "Biome Tile Pattern #860"
    WALKABLE = True if 860 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.6, 0.1999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_860.TILE_ID, "walkable": TileBlueprint_860.WALKABLE, "cost": TileBlueprint_860.MOVEMENT_COST}


class TileBlueprint_861:
    TILE_ID = 861
    NAME = "Biome Tile Pattern #861"
    WALKABLE = True if 861 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.61, 0.21999999999999886)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_861.TILE_ID, "walkable": TileBlueprint_861.WALKABLE, "cost": TileBlueprint_861.MOVEMENT_COST}


class TileBlueprint_862:
    TILE_ID = 862
    NAME = "Biome Tile Pattern #862"
    WALKABLE = True if 862 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.620000000000001, 0.240000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_862.TILE_ID, "walkable": TileBlueprint_862.WALKABLE, "cost": TileBlueprint_862.MOVEMENT_COST}


class TileBlueprint_863:
    TILE_ID = 863
    NAME = "Biome Tile Pattern #863"
    WALKABLE = True if 863 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.63, 0.26000000000000156)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_863.TILE_ID, "walkable": TileBlueprint_863.WALKABLE, "cost": TileBlueprint_863.MOVEMENT_COST}


class TileBlueprint_864:
    TILE_ID = 864
    NAME = "Biome Tile Pattern #864"
    WALKABLE = True if 864 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.64, 0.28000000000000114)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_864.TILE_ID, "walkable": TileBlueprint_864.WALKABLE, "cost": TileBlueprint_864.MOVEMENT_COST}


class TileBlueprint_865:
    TILE_ID = 865
    NAME = "Biome Tile Pattern #865"
    WALKABLE = True if 865 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.65, 0.3000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_865.TILE_ID, "walkable": TileBlueprint_865.WALKABLE, "cost": TileBlueprint_865.MOVEMENT_COST}


class TileBlueprint_866:
    TILE_ID = 866
    NAME = "Biome Tile Pattern #866"
    WALKABLE = True if 866 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.66, 0.3200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_866.TILE_ID, "walkable": TileBlueprint_866.WALKABLE, "cost": TileBlueprint_866.MOVEMENT_COST}


class TileBlueprint_867:
    TILE_ID = 867
    NAME = "Biome Tile Pattern #867"
    WALKABLE = True if 867 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.67, 0.33999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_867.TILE_ID, "walkable": TileBlueprint_867.WALKABLE, "cost": TileBlueprint_867.MOVEMENT_COST}


class TileBlueprint_868:
    TILE_ID = 868
    NAME = "Biome Tile Pattern #868"
    WALKABLE = True if 868 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.68, 0.35999999999999943)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_868.TILE_ID, "walkable": TileBlueprint_868.WALKABLE, "cost": TileBlueprint_868.MOVEMENT_COST}


class TileBlueprint_869:
    TILE_ID = 869
    NAME = "Biome Tile Pattern #869"
    WALKABLE = True if 869 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.69, 0.379999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_869.TILE_ID, "walkable": TileBlueprint_869.WALKABLE, "cost": TileBlueprint_869.MOVEMENT_COST}


class TileBlueprint_870:
    TILE_ID = 870
    NAME = "Biome Tile Pattern #870"
    WALKABLE = True if 870 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.700000000000001, 0.40000000000000213)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_870.TILE_ID, "walkable": TileBlueprint_870.WALKABLE, "cost": TileBlueprint_870.MOVEMENT_COST}


class TileBlueprint_871:
    TILE_ID = 871
    NAME = "Biome Tile Pattern #871"
    WALKABLE = True if 871 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.71, 0.4200000000000017)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_871.TILE_ID, "walkable": TileBlueprint_871.WALKABLE, "cost": TileBlueprint_871.MOVEMENT_COST}


class TileBlueprint_872:
    TILE_ID = 872
    NAME = "Biome Tile Pattern #872"
    WALKABLE = True if 872 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.72, 0.4400000000000013)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_872.TILE_ID, "walkable": TileBlueprint_872.WALKABLE, "cost": TileBlueprint_872.MOVEMENT_COST}


class TileBlueprint_873:
    TILE_ID = 873
    NAME = "Biome Tile Pattern #873"
    WALKABLE = True if 873 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.73, 0.46000000000000085)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_873.TILE_ID, "walkable": TileBlueprint_873.WALKABLE, "cost": TileBlueprint_873.MOVEMENT_COST}


class TileBlueprint_874:
    TILE_ID = 874
    NAME = "Biome Tile Pattern #874"
    WALKABLE = True if 874 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.74, 0.4800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_874.TILE_ID, "walkable": TileBlueprint_874.WALKABLE, "cost": TileBlueprint_874.MOVEMENT_COST}


class TileBlueprint_875:
    TILE_ID = 875
    NAME = "Biome Tile Pattern #875"
    WALKABLE = True if 875 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.75, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_875.TILE_ID, "walkable": TileBlueprint_875.WALKABLE, "cost": TileBlueprint_875.MOVEMENT_COST}


class TileBlueprint_876:
    TILE_ID = 876
    NAME = "Biome Tile Pattern #876"
    WALKABLE = True if 876 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.76, 0.5199999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_876.TILE_ID, "walkable": TileBlueprint_876.WALKABLE, "cost": TileBlueprint_876.MOVEMENT_COST}


class TileBlueprint_877:
    TILE_ID = 877
    NAME = "Biome Tile Pattern #877"
    WALKABLE = True if 877 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.77, 0.5399999999999991)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_877.TILE_ID, "walkable": TileBlueprint_877.WALKABLE, "cost": TileBlueprint_877.MOVEMENT_COST}


class TileBlueprint_878:
    TILE_ID = 878
    NAME = "Biome Tile Pattern #878"
    WALKABLE = True if 878 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.78, 0.5599999999999987)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_878.TILE_ID, "walkable": TileBlueprint_878.WALKABLE, "cost": TileBlueprint_878.MOVEMENT_COST}


class TileBlueprint_879:
    TILE_ID = 879
    NAME = "Biome Tile Pattern #879"
    WALKABLE = True if 879 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.790000000000001, 0.5800000000000018)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_879.TILE_ID, "walkable": TileBlueprint_879.WALKABLE, "cost": TileBlueprint_879.MOVEMENT_COST}


class TileBlueprint_880:
    TILE_ID = 880
    NAME = "Biome Tile Pattern #880"
    WALKABLE = True if 880 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.8, 0.6000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_880.TILE_ID, "walkable": TileBlueprint_880.WALKABLE, "cost": TileBlueprint_880.MOVEMENT_COST}


class TileBlueprint_881:
    TILE_ID = 881
    NAME = "Biome Tile Pattern #881"
    WALKABLE = True if 881 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.81, 0.620000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_881.TILE_ID, "walkable": TileBlueprint_881.WALKABLE, "cost": TileBlueprint_881.MOVEMENT_COST}


class TileBlueprint_882:
    TILE_ID = 882
    NAME = "Biome Tile Pattern #882"
    WALKABLE = True if 882 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.82, 0.6400000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_882.TILE_ID, "walkable": TileBlueprint_882.WALKABLE, "cost": TileBlueprint_882.MOVEMENT_COST}


class TileBlueprint_883:
    TILE_ID = 883
    NAME = "Biome Tile Pattern #883"
    WALKABLE = True if 883 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.83, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_883.TILE_ID, "walkable": TileBlueprint_883.WALKABLE, "cost": TileBlueprint_883.MOVEMENT_COST}


class TileBlueprint_884:
    TILE_ID = 884
    NAME = "Biome Tile Pattern #884"
    WALKABLE = True if 884 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.84, 0.6799999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_884.TILE_ID, "walkable": TileBlueprint_884.WALKABLE, "cost": TileBlueprint_884.MOVEMENT_COST}


class TileBlueprint_885:
    TILE_ID = 885
    NAME = "Biome Tile Pattern #885"
    WALKABLE = True if 885 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.85, 0.6999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_885.TILE_ID, "walkable": TileBlueprint_885.WALKABLE, "cost": TileBlueprint_885.MOVEMENT_COST}


class TileBlueprint_886:
    TILE_ID = 886
    NAME = "Biome Tile Pattern #886"
    WALKABLE = True if 886 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.86, 0.7199999999999989)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_886.TILE_ID, "walkable": TileBlueprint_886.WALKABLE, "cost": TileBlueprint_886.MOVEMENT_COST}


class TileBlueprint_887:
    TILE_ID = 887
    NAME = "Biome Tile Pattern #887"
    WALKABLE = True if 887 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.870000000000001, 0.740000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_887.TILE_ID, "walkable": TileBlueprint_887.WALKABLE, "cost": TileBlueprint_887.MOVEMENT_COST}


class TileBlueprint_888:
    TILE_ID = 888
    NAME = "Biome Tile Pattern #888"
    WALKABLE = True if 888 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.88, 0.7600000000000016)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_888.TILE_ID, "walkable": TileBlueprint_888.WALKABLE, "cost": TileBlueprint_888.MOVEMENT_COST}


class TileBlueprint_889:
    TILE_ID = 889
    NAME = "Biome Tile Pattern #889"
    WALKABLE = True if 889 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.89, 0.7800000000000011)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_889.TILE_ID, "walkable": TileBlueprint_889.WALKABLE, "cost": TileBlueprint_889.MOVEMENT_COST}


class TileBlueprint_890:
    TILE_ID = 890
    NAME = "Biome Tile Pattern #890"
    WALKABLE = True if 890 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.9, 0.8000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_890.TILE_ID, "walkable": TileBlueprint_890.WALKABLE, "cost": TileBlueprint_890.MOVEMENT_COST}


class TileBlueprint_891:
    TILE_ID = 891
    NAME = "Biome Tile Pattern #891"
    WALKABLE = True if 891 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.91, 0.8200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_891.TILE_ID, "walkable": TileBlueprint_891.WALKABLE, "cost": TileBlueprint_891.MOVEMENT_COST}


class TileBlueprint_892:
    TILE_ID = 892
    NAME = "Biome Tile Pattern #892"
    WALKABLE = True if 892 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.92, 0.8399999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_892.TILE_ID, "walkable": TileBlueprint_892.WALKABLE, "cost": TileBlueprint_892.MOVEMENT_COST}


class TileBlueprint_893:
    TILE_ID = 893
    NAME = "Biome Tile Pattern #893"
    WALKABLE = True if 893 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.93, 0.8599999999999994)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_893.TILE_ID, "walkable": TileBlueprint_893.WALKABLE, "cost": TileBlueprint_893.MOVEMENT_COST}


class TileBlueprint_894:
    TILE_ID = 894
    NAME = "Biome Tile Pattern #894"
    WALKABLE = True if 894 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.94, 0.879999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_894.TILE_ID, "walkable": TileBlueprint_894.WALKABLE, "cost": TileBlueprint_894.MOVEMENT_COST}


class TileBlueprint_895:
    TILE_ID = 895
    NAME = "Biome Tile Pattern #895"
    WALKABLE = True if 895 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (8.950000000000001, 0.9000000000000021)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_895.TILE_ID, "walkable": TileBlueprint_895.WALKABLE, "cost": TileBlueprint_895.MOVEMENT_COST}


class TileBlueprint_896:
    TILE_ID = 896
    NAME = "Biome Tile Pattern #896"
    WALKABLE = True if 896 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (8.96, 0.9200000000000017)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_896.TILE_ID, "walkable": TileBlueprint_896.WALKABLE, "cost": TileBlueprint_896.MOVEMENT_COST}


class TileBlueprint_897:
    TILE_ID = 897
    NAME = "Biome Tile Pattern #897"
    WALKABLE = True if 897 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (8.97, 0.9400000000000013)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_897.TILE_ID, "walkable": TileBlueprint_897.WALKABLE, "cost": TileBlueprint_897.MOVEMENT_COST}


class TileBlueprint_898:
    TILE_ID = 898
    NAME = "Biome Tile Pattern #898"
    WALKABLE = True if 898 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (8.98, 0.9600000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_898.TILE_ID, "walkable": TileBlueprint_898.WALKABLE, "cost": TileBlueprint_898.MOVEMENT_COST}


class TileBlueprint_899:
    TILE_ID = 899
    NAME = "Biome Tile Pattern #899"
    WALKABLE = True if 899 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (8.99, 0.9800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_899.TILE_ID, "walkable": TileBlueprint_899.WALKABLE, "cost": TileBlueprint_899.MOVEMENT_COST}


class TileBlueprint_900:
    TILE_ID = 900
    NAME = "Biome Tile Pattern #900"
    WALKABLE = True if 900 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.0, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_900.TILE_ID, "walkable": TileBlueprint_900.WALKABLE, "cost": TileBlueprint_900.MOVEMENT_COST}


class TileBlueprint_901:
    TILE_ID = 901
    NAME = "Biome Tile Pattern #901"
    WALKABLE = True if 901 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.01, 0.019999999999999574)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_901.TILE_ID, "walkable": TileBlueprint_901.WALKABLE, "cost": TileBlueprint_901.MOVEMENT_COST}


class TileBlueprint_902:
    TILE_ID = 902
    NAME = "Biome Tile Pattern #902"
    WALKABLE = True if 902 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.02, 0.03999999999999915)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_902.TILE_ID, "walkable": TileBlueprint_902.WALKABLE, "cost": TileBlueprint_902.MOVEMENT_COST}


class TileBlueprint_903:
    TILE_ID = 903
    NAME = "Biome Tile Pattern #903"
    WALKABLE = True if 903 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.03, 0.05999999999999872)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_903.TILE_ID, "walkable": TileBlueprint_903.WALKABLE, "cost": TileBlueprint_903.MOVEMENT_COST}


class TileBlueprint_904:
    TILE_ID = 904
    NAME = "Biome Tile Pattern #904"
    WALKABLE = True if 904 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.040000000000001, 0.08000000000000185)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_904.TILE_ID, "walkable": TileBlueprint_904.WALKABLE, "cost": TileBlueprint_904.MOVEMENT_COST}


class TileBlueprint_905:
    TILE_ID = 905
    NAME = "Biome Tile Pattern #905"
    WALKABLE = True if 905 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.05, 0.10000000000000142)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_905.TILE_ID, "walkable": TileBlueprint_905.WALKABLE, "cost": TileBlueprint_905.MOVEMENT_COST}


class TileBlueprint_906:
    TILE_ID = 906
    NAME = "Biome Tile Pattern #906"
    WALKABLE = True if 906 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.06, 0.120000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_906.TILE_ID, "walkable": TileBlueprint_906.WALKABLE, "cost": TileBlueprint_906.MOVEMENT_COST}


class TileBlueprint_907:
    TILE_ID = 907
    NAME = "Biome Tile Pattern #907"
    WALKABLE = True if 907 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.07, 0.14000000000000057)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_907.TILE_ID, "walkable": TileBlueprint_907.WALKABLE, "cost": TileBlueprint_907.MOVEMENT_COST}


class TileBlueprint_908:
    TILE_ID = 908
    NAME = "Biome Tile Pattern #908"
    WALKABLE = True if 908 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.08, 0.16000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_908.TILE_ID, "walkable": TileBlueprint_908.WALKABLE, "cost": TileBlueprint_908.MOVEMENT_COST}


class TileBlueprint_909:
    TILE_ID = 909
    NAME = "Biome Tile Pattern #909"
    WALKABLE = True if 909 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.09, 0.17999999999999972)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_909.TILE_ID, "walkable": TileBlueprint_909.WALKABLE, "cost": TileBlueprint_909.MOVEMENT_COST}


class TileBlueprint_910:
    TILE_ID = 910
    NAME = "Biome Tile Pattern #910"
    WALKABLE = True if 910 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.1, 0.1999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_910.TILE_ID, "walkable": TileBlueprint_910.WALKABLE, "cost": TileBlueprint_910.MOVEMENT_COST}


class TileBlueprint_911:
    TILE_ID = 911
    NAME = "Biome Tile Pattern #911"
    WALKABLE = True if 911 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.11, 0.21999999999999886)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_911.TILE_ID, "walkable": TileBlueprint_911.WALKABLE, "cost": TileBlueprint_911.MOVEMENT_COST}


class TileBlueprint_912:
    TILE_ID = 912
    NAME = "Biome Tile Pattern #912"
    WALKABLE = True if 912 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.120000000000001, 0.240000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_912.TILE_ID, "walkable": TileBlueprint_912.WALKABLE, "cost": TileBlueprint_912.MOVEMENT_COST}


class TileBlueprint_913:
    TILE_ID = 913
    NAME = "Biome Tile Pattern #913"
    WALKABLE = True if 913 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.13, 0.26000000000000156)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_913.TILE_ID, "walkable": TileBlueprint_913.WALKABLE, "cost": TileBlueprint_913.MOVEMENT_COST}


class TileBlueprint_914:
    TILE_ID = 914
    NAME = "Biome Tile Pattern #914"
    WALKABLE = True if 914 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.14, 0.28000000000000114)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_914.TILE_ID, "walkable": TileBlueprint_914.WALKABLE, "cost": TileBlueprint_914.MOVEMENT_COST}


class TileBlueprint_915:
    TILE_ID = 915
    NAME = "Biome Tile Pattern #915"
    WALKABLE = True if 915 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.15, 0.3000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_915.TILE_ID, "walkable": TileBlueprint_915.WALKABLE, "cost": TileBlueprint_915.MOVEMENT_COST}


class TileBlueprint_916:
    TILE_ID = 916
    NAME = "Biome Tile Pattern #916"
    WALKABLE = True if 916 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.16, 0.3200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_916.TILE_ID, "walkable": TileBlueprint_916.WALKABLE, "cost": TileBlueprint_916.MOVEMENT_COST}


class TileBlueprint_917:
    TILE_ID = 917
    NAME = "Biome Tile Pattern #917"
    WALKABLE = True if 917 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.17, 0.33999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_917.TILE_ID, "walkable": TileBlueprint_917.WALKABLE, "cost": TileBlueprint_917.MOVEMENT_COST}


class TileBlueprint_918:
    TILE_ID = 918
    NAME = "Biome Tile Pattern #918"
    WALKABLE = True if 918 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.18, 0.35999999999999943)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_918.TILE_ID, "walkable": TileBlueprint_918.WALKABLE, "cost": TileBlueprint_918.MOVEMENT_COST}


class TileBlueprint_919:
    TILE_ID = 919
    NAME = "Biome Tile Pattern #919"
    WALKABLE = True if 919 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.19, 0.379999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_919.TILE_ID, "walkable": TileBlueprint_919.WALKABLE, "cost": TileBlueprint_919.MOVEMENT_COST}


class TileBlueprint_920:
    TILE_ID = 920
    NAME = "Biome Tile Pattern #920"
    WALKABLE = True if 920 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.200000000000001, 0.40000000000000213)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_920.TILE_ID, "walkable": TileBlueprint_920.WALKABLE, "cost": TileBlueprint_920.MOVEMENT_COST}


class TileBlueprint_921:
    TILE_ID = 921
    NAME = "Biome Tile Pattern #921"
    WALKABLE = True if 921 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.21, 0.4200000000000017)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_921.TILE_ID, "walkable": TileBlueprint_921.WALKABLE, "cost": TileBlueprint_921.MOVEMENT_COST}


class TileBlueprint_922:
    TILE_ID = 922
    NAME = "Biome Tile Pattern #922"
    WALKABLE = True if 922 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.22, 0.4400000000000013)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_922.TILE_ID, "walkable": TileBlueprint_922.WALKABLE, "cost": TileBlueprint_922.MOVEMENT_COST}


class TileBlueprint_923:
    TILE_ID = 923
    NAME = "Biome Tile Pattern #923"
    WALKABLE = True if 923 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.23, 0.46000000000000085)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_923.TILE_ID, "walkable": TileBlueprint_923.WALKABLE, "cost": TileBlueprint_923.MOVEMENT_COST}


class TileBlueprint_924:
    TILE_ID = 924
    NAME = "Biome Tile Pattern #924"
    WALKABLE = True if 924 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.24, 0.4800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_924.TILE_ID, "walkable": TileBlueprint_924.WALKABLE, "cost": TileBlueprint_924.MOVEMENT_COST}


class TileBlueprint_925:
    TILE_ID = 925
    NAME = "Biome Tile Pattern #925"
    WALKABLE = True if 925 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.25, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_925.TILE_ID, "walkable": TileBlueprint_925.WALKABLE, "cost": TileBlueprint_925.MOVEMENT_COST}


class TileBlueprint_926:
    TILE_ID = 926
    NAME = "Biome Tile Pattern #926"
    WALKABLE = True if 926 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.26, 0.5199999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_926.TILE_ID, "walkable": TileBlueprint_926.WALKABLE, "cost": TileBlueprint_926.MOVEMENT_COST}


class TileBlueprint_927:
    TILE_ID = 927
    NAME = "Biome Tile Pattern #927"
    WALKABLE = True if 927 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.27, 0.5399999999999991)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_927.TILE_ID, "walkable": TileBlueprint_927.WALKABLE, "cost": TileBlueprint_927.MOVEMENT_COST}


class TileBlueprint_928:
    TILE_ID = 928
    NAME = "Biome Tile Pattern #928"
    WALKABLE = True if 928 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.28, 0.5599999999999987)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_928.TILE_ID, "walkable": TileBlueprint_928.WALKABLE, "cost": TileBlueprint_928.MOVEMENT_COST}


class TileBlueprint_929:
    TILE_ID = 929
    NAME = "Biome Tile Pattern #929"
    WALKABLE = True if 929 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.290000000000001, 0.5800000000000018)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_929.TILE_ID, "walkable": TileBlueprint_929.WALKABLE, "cost": TileBlueprint_929.MOVEMENT_COST}


class TileBlueprint_930:
    TILE_ID = 930
    NAME = "Biome Tile Pattern #930"
    WALKABLE = True if 930 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.3, 0.6000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_930.TILE_ID, "walkable": TileBlueprint_930.WALKABLE, "cost": TileBlueprint_930.MOVEMENT_COST}


class TileBlueprint_931:
    TILE_ID = 931
    NAME = "Biome Tile Pattern #931"
    WALKABLE = True if 931 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.31, 0.620000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_931.TILE_ID, "walkable": TileBlueprint_931.WALKABLE, "cost": TileBlueprint_931.MOVEMENT_COST}


class TileBlueprint_932:
    TILE_ID = 932
    NAME = "Biome Tile Pattern #932"
    WALKABLE = True if 932 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.32, 0.6400000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_932.TILE_ID, "walkable": TileBlueprint_932.WALKABLE, "cost": TileBlueprint_932.MOVEMENT_COST}


class TileBlueprint_933:
    TILE_ID = 933
    NAME = "Biome Tile Pattern #933"
    WALKABLE = True if 933 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.33, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_933.TILE_ID, "walkable": TileBlueprint_933.WALKABLE, "cost": TileBlueprint_933.MOVEMENT_COST}


class TileBlueprint_934:
    TILE_ID = 934
    NAME = "Biome Tile Pattern #934"
    WALKABLE = True if 934 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.34, 0.6799999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_934.TILE_ID, "walkable": TileBlueprint_934.WALKABLE, "cost": TileBlueprint_934.MOVEMENT_COST}


class TileBlueprint_935:
    TILE_ID = 935
    NAME = "Biome Tile Pattern #935"
    WALKABLE = True if 935 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.35, 0.6999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_935.TILE_ID, "walkable": TileBlueprint_935.WALKABLE, "cost": TileBlueprint_935.MOVEMENT_COST}


class TileBlueprint_936:
    TILE_ID = 936
    NAME = "Biome Tile Pattern #936"
    WALKABLE = True if 936 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.36, 0.7199999999999989)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_936.TILE_ID, "walkable": TileBlueprint_936.WALKABLE, "cost": TileBlueprint_936.MOVEMENT_COST}


class TileBlueprint_937:
    TILE_ID = 937
    NAME = "Biome Tile Pattern #937"
    WALKABLE = True if 937 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.370000000000001, 0.740000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_937.TILE_ID, "walkable": TileBlueprint_937.WALKABLE, "cost": TileBlueprint_937.MOVEMENT_COST}


class TileBlueprint_938:
    TILE_ID = 938
    NAME = "Biome Tile Pattern #938"
    WALKABLE = True if 938 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.38, 0.7600000000000016)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_938.TILE_ID, "walkable": TileBlueprint_938.WALKABLE, "cost": TileBlueprint_938.MOVEMENT_COST}


class TileBlueprint_939:
    TILE_ID = 939
    NAME = "Biome Tile Pattern #939"
    WALKABLE = True if 939 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.39, 0.7800000000000011)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_939.TILE_ID, "walkable": TileBlueprint_939.WALKABLE, "cost": TileBlueprint_939.MOVEMENT_COST}


class TileBlueprint_940:
    TILE_ID = 940
    NAME = "Biome Tile Pattern #940"
    WALKABLE = True if 940 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.4, 0.8000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_940.TILE_ID, "walkable": TileBlueprint_940.WALKABLE, "cost": TileBlueprint_940.MOVEMENT_COST}


class TileBlueprint_941:
    TILE_ID = 941
    NAME = "Biome Tile Pattern #941"
    WALKABLE = True if 941 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.41, 0.8200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_941.TILE_ID, "walkable": TileBlueprint_941.WALKABLE, "cost": TileBlueprint_941.MOVEMENT_COST}


class TileBlueprint_942:
    TILE_ID = 942
    NAME = "Biome Tile Pattern #942"
    WALKABLE = True if 942 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.42, 0.8399999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_942.TILE_ID, "walkable": TileBlueprint_942.WALKABLE, "cost": TileBlueprint_942.MOVEMENT_COST}


class TileBlueprint_943:
    TILE_ID = 943
    NAME = "Biome Tile Pattern #943"
    WALKABLE = True if 943 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.43, 0.8599999999999994)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_943.TILE_ID, "walkable": TileBlueprint_943.WALKABLE, "cost": TileBlueprint_943.MOVEMENT_COST}


class TileBlueprint_944:
    TILE_ID = 944
    NAME = "Biome Tile Pattern #944"
    WALKABLE = True if 944 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.44, 0.879999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_944.TILE_ID, "walkable": TileBlueprint_944.WALKABLE, "cost": TileBlueprint_944.MOVEMENT_COST}


class TileBlueprint_945:
    TILE_ID = 945
    NAME = "Biome Tile Pattern #945"
    WALKABLE = True if 945 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.450000000000001, 0.9000000000000021)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_945.TILE_ID, "walkable": TileBlueprint_945.WALKABLE, "cost": TileBlueprint_945.MOVEMENT_COST}


class TileBlueprint_946:
    TILE_ID = 946
    NAME = "Biome Tile Pattern #946"
    WALKABLE = True if 946 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.46, 0.9200000000000017)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_946.TILE_ID, "walkable": TileBlueprint_946.WALKABLE, "cost": TileBlueprint_946.MOVEMENT_COST}


class TileBlueprint_947:
    TILE_ID = 947
    NAME = "Biome Tile Pattern #947"
    WALKABLE = True if 947 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.47, 0.9400000000000013)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_947.TILE_ID, "walkable": TileBlueprint_947.WALKABLE, "cost": TileBlueprint_947.MOVEMENT_COST}


class TileBlueprint_948:
    TILE_ID = 948
    NAME = "Biome Tile Pattern #948"
    WALKABLE = True if 948 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.48, 0.9600000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_948.TILE_ID, "walkable": TileBlueprint_948.WALKABLE, "cost": TileBlueprint_948.MOVEMENT_COST}


class TileBlueprint_949:
    TILE_ID = 949
    NAME = "Biome Tile Pattern #949"
    WALKABLE = True if 949 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.49, 0.9800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_949.TILE_ID, "walkable": TileBlueprint_949.WALKABLE, "cost": TileBlueprint_949.MOVEMENT_COST}


class TileBlueprint_950:
    TILE_ID = 950
    NAME = "Biome Tile Pattern #950"
    WALKABLE = True if 950 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.5, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_950.TILE_ID, "walkable": TileBlueprint_950.WALKABLE, "cost": TileBlueprint_950.MOVEMENT_COST}


class TileBlueprint_951:
    TILE_ID = 951
    NAME = "Biome Tile Pattern #951"
    WALKABLE = True if 951 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.51, 0.019999999999999574)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_951.TILE_ID, "walkable": TileBlueprint_951.WALKABLE, "cost": TileBlueprint_951.MOVEMENT_COST}


class TileBlueprint_952:
    TILE_ID = 952
    NAME = "Biome Tile Pattern #952"
    WALKABLE = True if 952 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.52, 0.03999999999999915)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_952.TILE_ID, "walkable": TileBlueprint_952.WALKABLE, "cost": TileBlueprint_952.MOVEMENT_COST}


class TileBlueprint_953:
    TILE_ID = 953
    NAME = "Biome Tile Pattern #953"
    WALKABLE = True if 953 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.53, 0.05999999999999872)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_953.TILE_ID, "walkable": TileBlueprint_953.WALKABLE, "cost": TileBlueprint_953.MOVEMENT_COST}


class TileBlueprint_954:
    TILE_ID = 954
    NAME = "Biome Tile Pattern #954"
    WALKABLE = True if 954 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.540000000000001, 0.08000000000000185)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_954.TILE_ID, "walkable": TileBlueprint_954.WALKABLE, "cost": TileBlueprint_954.MOVEMENT_COST}


class TileBlueprint_955:
    TILE_ID = 955
    NAME = "Biome Tile Pattern #955"
    WALKABLE = True if 955 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.55, 0.10000000000000142)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_955.TILE_ID, "walkable": TileBlueprint_955.WALKABLE, "cost": TileBlueprint_955.MOVEMENT_COST}


class TileBlueprint_956:
    TILE_ID = 956
    NAME = "Biome Tile Pattern #956"
    WALKABLE = True if 956 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.56, 0.120000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_956.TILE_ID, "walkable": TileBlueprint_956.WALKABLE, "cost": TileBlueprint_956.MOVEMENT_COST}


class TileBlueprint_957:
    TILE_ID = 957
    NAME = "Biome Tile Pattern #957"
    WALKABLE = True if 957 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.57, 0.14000000000000057)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_957.TILE_ID, "walkable": TileBlueprint_957.WALKABLE, "cost": TileBlueprint_957.MOVEMENT_COST}


class TileBlueprint_958:
    TILE_ID = 958
    NAME = "Biome Tile Pattern #958"
    WALKABLE = True if 958 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.58, 0.16000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_958.TILE_ID, "walkable": TileBlueprint_958.WALKABLE, "cost": TileBlueprint_958.MOVEMENT_COST}


class TileBlueprint_959:
    TILE_ID = 959
    NAME = "Biome Tile Pattern #959"
    WALKABLE = True if 959 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.59, 0.17999999999999972)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_959.TILE_ID, "walkable": TileBlueprint_959.WALKABLE, "cost": TileBlueprint_959.MOVEMENT_COST}


class TileBlueprint_960:
    TILE_ID = 960
    NAME = "Biome Tile Pattern #960"
    WALKABLE = True if 960 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.6, 0.1999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_960.TILE_ID, "walkable": TileBlueprint_960.WALKABLE, "cost": TileBlueprint_960.MOVEMENT_COST}


class TileBlueprint_961:
    TILE_ID = 961
    NAME = "Biome Tile Pattern #961"
    WALKABLE = True if 961 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.61, 0.21999999999999886)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_961.TILE_ID, "walkable": TileBlueprint_961.WALKABLE, "cost": TileBlueprint_961.MOVEMENT_COST}


class TileBlueprint_962:
    TILE_ID = 962
    NAME = "Biome Tile Pattern #962"
    WALKABLE = True if 962 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.620000000000001, 0.240000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_962.TILE_ID, "walkable": TileBlueprint_962.WALKABLE, "cost": TileBlueprint_962.MOVEMENT_COST}


class TileBlueprint_963:
    TILE_ID = 963
    NAME = "Biome Tile Pattern #963"
    WALKABLE = True if 963 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.63, 0.26000000000000156)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_963.TILE_ID, "walkable": TileBlueprint_963.WALKABLE, "cost": TileBlueprint_963.MOVEMENT_COST}


class TileBlueprint_964:
    TILE_ID = 964
    NAME = "Biome Tile Pattern #964"
    WALKABLE = True if 964 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.64, 0.28000000000000114)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_964.TILE_ID, "walkable": TileBlueprint_964.WALKABLE, "cost": TileBlueprint_964.MOVEMENT_COST}


class TileBlueprint_965:
    TILE_ID = 965
    NAME = "Biome Tile Pattern #965"
    WALKABLE = True if 965 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.65, 0.3000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_965.TILE_ID, "walkable": TileBlueprint_965.WALKABLE, "cost": TileBlueprint_965.MOVEMENT_COST}


class TileBlueprint_966:
    TILE_ID = 966
    NAME = "Biome Tile Pattern #966"
    WALKABLE = True if 966 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.66, 0.3200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_966.TILE_ID, "walkable": TileBlueprint_966.WALKABLE, "cost": TileBlueprint_966.MOVEMENT_COST}


class TileBlueprint_967:
    TILE_ID = 967
    NAME = "Biome Tile Pattern #967"
    WALKABLE = True if 967 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.67, 0.33999999999999986)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_967.TILE_ID, "walkable": TileBlueprint_967.WALKABLE, "cost": TileBlueprint_967.MOVEMENT_COST}


class TileBlueprint_968:
    TILE_ID = 968
    NAME = "Biome Tile Pattern #968"
    WALKABLE = True if 968 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.68, 0.35999999999999943)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_968.TILE_ID, "walkable": TileBlueprint_968.WALKABLE, "cost": TileBlueprint_968.MOVEMENT_COST}


class TileBlueprint_969:
    TILE_ID = 969
    NAME = "Biome Tile Pattern #969"
    WALKABLE = True if 969 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.69, 0.379999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_969.TILE_ID, "walkable": TileBlueprint_969.WALKABLE, "cost": TileBlueprint_969.MOVEMENT_COST}


class TileBlueprint_970:
    TILE_ID = 970
    NAME = "Biome Tile Pattern #970"
    WALKABLE = True if 970 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.700000000000001, 0.40000000000000213)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_970.TILE_ID, "walkable": TileBlueprint_970.WALKABLE, "cost": TileBlueprint_970.MOVEMENT_COST}


class TileBlueprint_971:
    TILE_ID = 971
    NAME = "Biome Tile Pattern #971"
    WALKABLE = True if 971 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.71, 0.4200000000000017)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_971.TILE_ID, "walkable": TileBlueprint_971.WALKABLE, "cost": TileBlueprint_971.MOVEMENT_COST}


class TileBlueprint_972:
    TILE_ID = 972
    NAME = "Biome Tile Pattern #972"
    WALKABLE = True if 972 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.72, 0.4400000000000013)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_972.TILE_ID, "walkable": TileBlueprint_972.WALKABLE, "cost": TileBlueprint_972.MOVEMENT_COST}


class TileBlueprint_973:
    TILE_ID = 973
    NAME = "Biome Tile Pattern #973"
    WALKABLE = True if 973 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.73, 0.46000000000000085)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_973.TILE_ID, "walkable": TileBlueprint_973.WALKABLE, "cost": TileBlueprint_973.MOVEMENT_COST}


class TileBlueprint_974:
    TILE_ID = 974
    NAME = "Biome Tile Pattern #974"
    WALKABLE = True if 974 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.74, 0.4800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_974.TILE_ID, "walkable": TileBlueprint_974.WALKABLE, "cost": TileBlueprint_974.MOVEMENT_COST}


class TileBlueprint_975:
    TILE_ID = 975
    NAME = "Biome Tile Pattern #975"
    WALKABLE = True if 975 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.75, 0.5)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_975.TILE_ID, "walkable": TileBlueprint_975.WALKABLE, "cost": TileBlueprint_975.MOVEMENT_COST}


class TileBlueprint_976:
    TILE_ID = 976
    NAME = "Biome Tile Pattern #976"
    WALKABLE = True if 976 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.76, 0.5199999999999996)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_976.TILE_ID, "walkable": TileBlueprint_976.WALKABLE, "cost": TileBlueprint_976.MOVEMENT_COST}


class TileBlueprint_977:
    TILE_ID = 977
    NAME = "Biome Tile Pattern #977"
    WALKABLE = True if 977 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.77, 0.5399999999999991)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_977.TILE_ID, "walkable": TileBlueprint_977.WALKABLE, "cost": TileBlueprint_977.MOVEMENT_COST}


class TileBlueprint_978:
    TILE_ID = 978
    NAME = "Biome Tile Pattern #978"
    WALKABLE = True if 978 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.78, 0.5599999999999987)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_978.TILE_ID, "walkable": TileBlueprint_978.WALKABLE, "cost": TileBlueprint_978.MOVEMENT_COST}


class TileBlueprint_979:
    TILE_ID = 979
    NAME = "Biome Tile Pattern #979"
    WALKABLE = True if 979 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.790000000000001, 0.5800000000000018)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_979.TILE_ID, "walkable": TileBlueprint_979.WALKABLE, "cost": TileBlueprint_979.MOVEMENT_COST}


class TileBlueprint_980:
    TILE_ID = 980
    NAME = "Biome Tile Pattern #980"
    WALKABLE = True if 980 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.8, 0.6000000000000014)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_980.TILE_ID, "walkable": TileBlueprint_980.WALKABLE, "cost": TileBlueprint_980.MOVEMENT_COST}


class TileBlueprint_981:
    TILE_ID = 981
    NAME = "Biome Tile Pattern #981"
    WALKABLE = True if 981 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.81, 0.620000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_981.TILE_ID, "walkable": TileBlueprint_981.WALKABLE, "cost": TileBlueprint_981.MOVEMENT_COST}


class TileBlueprint_982:
    TILE_ID = 982
    NAME = "Biome Tile Pattern #982"
    WALKABLE = True if 982 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.82, 0.6400000000000006)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_982.TILE_ID, "walkable": TileBlueprint_982.WALKABLE, "cost": TileBlueprint_982.MOVEMENT_COST}


class TileBlueprint_983:
    TILE_ID = 983
    NAME = "Biome Tile Pattern #983"
    WALKABLE = True if 983 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.83, 0.6600000000000001)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_983.TILE_ID, "walkable": TileBlueprint_983.WALKABLE, "cost": TileBlueprint_983.MOVEMENT_COST}


class TileBlueprint_984:
    TILE_ID = 984
    NAME = "Biome Tile Pattern #984"
    WALKABLE = True if 984 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.84, 0.6799999999999997)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_984.TILE_ID, "walkable": TileBlueprint_984.WALKABLE, "cost": TileBlueprint_984.MOVEMENT_COST}


class TileBlueprint_985:
    TILE_ID = 985
    NAME = "Biome Tile Pattern #985"
    WALKABLE = True if 985 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.85, 0.6999999999999993)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_985.TILE_ID, "walkable": TileBlueprint_985.WALKABLE, "cost": TileBlueprint_985.MOVEMENT_COST}


class TileBlueprint_986:
    TILE_ID = 986
    NAME = "Biome Tile Pattern #986"
    WALKABLE = True if 986 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.86, 0.7199999999999989)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_986.TILE_ID, "walkable": TileBlueprint_986.WALKABLE, "cost": TileBlueprint_986.MOVEMENT_COST}


class TileBlueprint_987:
    TILE_ID = 987
    NAME = "Biome Tile Pattern #987"
    WALKABLE = True if 987 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.870000000000001, 0.740000000000002)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_987.TILE_ID, "walkable": TileBlueprint_987.WALKABLE, "cost": TileBlueprint_987.MOVEMENT_COST}


class TileBlueprint_988:
    TILE_ID = 988
    NAME = "Biome Tile Pattern #988"
    WALKABLE = True if 988 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.88, 0.7600000000000016)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_988.TILE_ID, "walkable": TileBlueprint_988.WALKABLE, "cost": TileBlueprint_988.MOVEMENT_COST}


class TileBlueprint_989:
    TILE_ID = 989
    NAME = "Biome Tile Pattern #989"
    WALKABLE = True if 989 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.89, 0.7800000000000011)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_989.TILE_ID, "walkable": TileBlueprint_989.WALKABLE, "cost": TileBlueprint_989.MOVEMENT_COST}


class TileBlueprint_990:
    TILE_ID = 990
    NAME = "Biome Tile Pattern #990"
    WALKABLE = True if 990 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.9, 0.8000000000000007)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_990.TILE_ID, "walkable": TileBlueprint_990.WALKABLE, "cost": TileBlueprint_990.MOVEMENT_COST}


class TileBlueprint_991:
    TILE_ID = 991
    NAME = "Biome Tile Pattern #991"
    WALKABLE = True if 991 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.91, 0.8200000000000003)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_991.TILE_ID, "walkable": TileBlueprint_991.WALKABLE, "cost": TileBlueprint_991.MOVEMENT_COST}


class TileBlueprint_992:
    TILE_ID = 992
    NAME = "Biome Tile Pattern #992"
    WALKABLE = True if 992 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.92, 0.8399999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_992.TILE_ID, "walkable": TileBlueprint_992.WALKABLE, "cost": TileBlueprint_992.MOVEMENT_COST}


class TileBlueprint_993:
    TILE_ID = 993
    NAME = "Biome Tile Pattern #993"
    WALKABLE = True if 993 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.93, 0.8599999999999994)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_993.TILE_ID, "walkable": TileBlueprint_993.WALKABLE, "cost": TileBlueprint_993.MOVEMENT_COST}


class TileBlueprint_994:
    TILE_ID = 994
    NAME = "Biome Tile Pattern #994"
    WALKABLE = True if 994 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.94, 0.879999999999999)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_994.TILE_ID, "walkable": TileBlueprint_994.WALKABLE, "cost": TileBlueprint_994.MOVEMENT_COST}


class TileBlueprint_995:
    TILE_ID = 995
    NAME = "Biome Tile Pattern #995"
    WALKABLE = True if 995 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (9.950000000000001, 0.9000000000000021)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_995.TILE_ID, "walkable": TileBlueprint_995.WALKABLE, "cost": TileBlueprint_995.MOVEMENT_COST}


class TileBlueprint_996:
    TILE_ID = 996
    NAME = "Biome Tile Pattern #996"
    WALKABLE = True if 996 % 3 != 0 else False
    MOVEMENT_COST = 1.5
    TEXTURE_UV = (9.96, 0.9200000000000017)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_996.TILE_ID, "walkable": TileBlueprint_996.WALKABLE, "cost": TileBlueprint_996.MOVEMENT_COST}


class TileBlueprint_997:
    TILE_ID = 997
    NAME = "Biome Tile Pattern #997"
    WALKABLE = True if 997 % 3 != 0 else False
    MOVEMENT_COST = 2.0
    TEXTURE_UV = (9.97, 0.9400000000000013)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_997.TILE_ID, "walkable": TileBlueprint_997.WALKABLE, "cost": TileBlueprint_997.MOVEMENT_COST}


class TileBlueprint_998:
    TILE_ID = 998
    NAME = "Biome Tile Pattern #998"
    WALKABLE = True if 998 % 3 != 0 else False
    MOVEMENT_COST = 2.5
    TEXTURE_UV = (9.98, 0.9600000000000009)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_998.TILE_ID, "walkable": TileBlueprint_998.WALKABLE, "cost": TileBlueprint_998.MOVEMENT_COST}


class TileBlueprint_999:
    TILE_ID = 999
    NAME = "Biome Tile Pattern #999"
    WALKABLE = True if 999 % 3 != 0 else False
    MOVEMENT_COST = 3.0
    TEXTURE_UV = (9.99, 0.9800000000000004)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_999.TILE_ID, "walkable": TileBlueprint_999.WALKABLE, "cost": TileBlueprint_999.MOVEMENT_COST}


class TileBlueprint_1000:
    TILE_ID = 1000
    NAME = "Biome Tile Pattern #1000"
    WALKABLE = True if 1000 % 3 != 0 else False
    MOVEMENT_COST = 1.0
    TEXTURE_UV = (10.0, 0.0)

    @staticmethod
    def get_info():
        return {"id": TileBlueprint_1000.TILE_ID, "walkable": TileBlueprint_1000.WALKABLE, "cost": TileBlueprint_1000.MOVEMENT_COST}
