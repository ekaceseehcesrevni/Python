def build_reinforced_wall():
    for position in range(1,21):
        if position % 4 == 0:
            block_type = "COBBLESTONE"
        else:
            block_type = "PLANK"
        print(f"{block_type} at position {position}")
        if position % 5 == 0:
            print("Defense checkpoint reached!")