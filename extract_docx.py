import docx, os
path = r"D:\writing\override_zone\2_0 The 'Hart' that shall beat.docx"
print(os.path.exists(path))
doc = docx.Document(path)
out=[]
for p in doc.paragraphs:
    if p.text.strip():
        out.append(p.style.name + '||' + p.text)
for t in doc.tables:
    out.append('---TABLE---')
    for row in t.rows:
        out.append(' | '.join(c.text for c in row.cells))
open(r"D:\develop\override-codex\extracted_2.txt",'w',encoding='utf-8').write('\n'.join(out))
print('paras', len(doc.paragraphs), 'tables', len(doc.tables))