ent2idx = {}
idx2ent = {}
with open('data/rawdata/MetaQA/entities.dict', 'r') as f, open('data/MetaQA/entities.dict', 'w') as f2, open('data/MetaQA/entities_desc.dict', 'w') as f3:
    lines = f.readlines()
    for line in lines:
        ent, idx = line.strip().split('\t')
        ent2idx[ent] = idx
        idx2ent[idx] = ent
    new_lines = ""
    for idx, ent in idx2ent.items():
        new_line = idx + '\t' + ent + '\n'
        new_lines += new_line
    f2.write(new_lines)
    f3.write(new_lines)


rel2idx = {}
idx2rel = {}
with open('data/rawdata/MetaQA/relations.dict', 'r') as f, open('data/MetaQA/relations.dict', 'w') as f2:
    lines = f.readlines()
    for line in lines:
        rel, idx = line.strip().split('\t')
        rel2idx[rel] = idx
        idx2rel[idx] = rel
    new_lines = ""
    for idx, rel in idx2rel.items():
        new_line = idx + '\t' + rel + '\n'
        new_lines += new_line
    f2.write(new_lines)

def translate_dataset(mode='train'):
    with open('data/rawdata/MetaQA/' + mode + '.txt', 'r') as f, open('data/MetaQA/' + mode +'.txt', 'w') as f2:
        lines = f.readlines()
        new_lines = ""
        for line in lines:
            h, r, t = line.strip().split('\t')
            new_line = ent2idx[h] + '\t' + rel2idx[r] + '\t' + ent2idx[t] + '\n'
            new_lines += new_line
        f2.write(new_lines)

translate_dataset('train')
translate_dataset('valid')
translate_dataset('test')