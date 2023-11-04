import os
from octanry_hexanary import *

data_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(data_path, 'data', 'random.txt')
# filename = os.path.join(data_path, 'data', 'enwik8.txt')
# filename = os.path.join(data_path, 'data', 'Canterbury.txt')

data, file_type, size = f_read_data_from_file(filename_in_data=filename)

# Шифрование -- шифрование восьмеричным методом Хаффмана
octanry_huffman =Octanry_Hexanary_huffman(data=data, file_type=file_type)
[encode_initial, symbol_composition, seat] = octanry_huffman.codegenerate()

# Шифрование -- шифрование шестнадцатеричным методом Хаффмана
hexanary_huffman = Octanry_Hexanary_huffman(data=data, file_type=file_type)
[encode_initial_hex, symbol_composition_hex, seat_hex] = hexanary_huffman.codegenerate()


# Шифрование -- добавление таблицы кодов для восьмеричного представления
code_table = Code_table_addition(symbol_composition=symbol_composition, seat=seat, file_type=file_type)
encode_table_add = code_table.f_huffman_table() + encode_initial

# Шифрование -- добавление таблицы кодов для шестнадцатеричного представления
code_table_hex = Code_table_addition(symbol_composition=symbol_composition_hex, seat=seat_hex, file_type=file_type)
encode_table_add_hex = code_table.f_huffman_table() + encode_initial_hex


extension_mapping = Extension_mapping(code_initial=encode_table_add)
encode_final = extension_mapping.f_extension_mapping_twice()


extension_mapping_hex = Extension_mapping(code_initial=encode_table_add_hex)
encode_final_hex = extension_mapping_hex.f_extension_mapping_twice()


segmentation_index = Segmentation_index(sequences_initial=encode_final, n_bases_payload=994)
dna_sequences = segmentation_index.f_index_and_num2base()

segmentation_index_hex = Segmentation_index(sequences_initial=encode_final_hex, n_bases_payload=994)
dna_sequences_hex = segmentation_index_hex.f_index_and_num2base()

# Расшифрование подготовка восьмеричного метода
mapping_inverse = Extension_mapping_inverse(sequences_silicon=encode_final)
decode_initial = mapping_inverse.mapping_inverse_twice()

# Расшифрование подготовка шестнадцатиричного метода
mapping_inverse_hex = Extension_mapping_inverse(sequences_silicon=encode_final_hex)
decode_initial_hex = mapping_inverse_hex.mapping_inverse_twice()

# Расшифровка -- восстановление соответствия между кодовыми словами и символами для восьмеричного метода
code_table_reading = Code_table_reading(data=decode_initial, file_type=file_type)
[decode_payloads, decode_codewords, decode_symbol_composition] = code_table_reading.f_code_table_reading()

# Расшифровка -- восстановление соответствия между кодовыми словами и символами для шестнадцатеричного метода метода
code_table_reading_hex = Code_table_reading(data=decode_initial, file_type=file_type)
[decode_payloads_hex, decode_codewords_hex, decode_symbol_composition_hex] = code_table_reading_hex.f_code_table_reading()

# Decoding -- decode into original text or picture data
decode_result = decode_txt_pic(sequences=decode_payloads, codewords=decode_codewords,
                               symbol_composition=decode_symbol_composition, file_type=file_type, size=size)
# Decoding -- decode into original text or picture data
decode_result_hex = decode_txt_pic(sequences=decode_payloads_hex, codewords=decode_codewords_hex,
                               symbol_composition=decode_symbol_composition_hex, file_type=file_type, size=size)