meerkats_pieces_list = []

for _ in range(3):
    meerkat_piece = input()
    meerkats_pieces_list.append(meerkat_piece)

meerkats_pieces_list[0], meerkats_pieces_list[2] = meerkats_pieces_list[2], meerkats_pieces_list[0]
print(meerkats_pieces_list)