with open('preproinsulin-seq.txt', 'r') as file:
    content=file.read()
content=content.replace('ORIGIN', '')
content=''.join(char for char in content if not char.isdigit())
content=content.replace('//', '')
content=content.replace(' ', '').replace('\n', '').replace('\r', '')
print(content)
print(len(content))
print(content.islower())

amino_acids_1_24=content[:24]
with open('lsinsulin_seq_clean.txt', 'w') as output_file:
    output_file.write(amino_acids_1_24)
print(f'Are noul fisier 24 de caractere?', len(amino_acids_1_24))

amino_acids_24_54=content[24:54]
with open('binsulin_seq_clean.txt', 'w') as output_file:
    output_file.write(amino_acids_24_54)
print(f'Are noul fisier 30 de caractere?', len(amino_acids_24_54))

amino_acids_54_89=content[54:89]
with open('cinsulin_seq_clean.txt', 'w') as output_file:
    output_file.write(amino_acids_54_89)
print(f'Are noul fisier 35 caractere?', len(amino_acids_54_89))

amino_acids_89_110=content[89:110]
with open('ainsulin_seq_clean.txt', 'w') as output_file:
    output_file.write(amino_acids_89_110)
print(f'Are noul fisier 21 de caractere?', len(amino_acids_89_110))

