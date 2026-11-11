import docx, json, re, os, shutil

BASE = r"D:\writing\override_zone"
OUT  = r"D:\develop\override-codex"
ILL  = os.path.join(BASE, "illust5rations")

# ---------- 1. Characters from character_lines.txt ----------
text = open(os.path.join(BASE, "character_lines.txt"), encoding="utf-8").read()

# faction + image filename overrides (best-effort)
FACTION = {
 "Niro Hart":"Hart Family","Victor Hart":"Hart Family","Elena Hart (Mother)":"Hart Family",
 "Seraphine Hart":"Hart Family","Thaddeus Hart / Thad":"Hart Family","Edward Hart":"Hart Family",
 "Nigel Hart":"Hart Family",
 "Naobito Yagami":"Yagami","Yurei Himura (Dark Maiden)":"Dark Maiden",
 "Lucien Moreau":"Weavers","Leon Cross":"Independent","Proxy / PRX-04":"Independent",
 "Nemimoth (Key of Hunger)":"Keys","Asha Nkosi":"Rankers","Viktor Drago":"Rankers",
 "Hana Yagami":"Yagami","Isolde Aster":"Rankers","Mireille Vale":"Weavers",
 "Kenshi Kashimo":"Rankers","Master Kael Voss":"Weavers","Lady Elara Vane":"Weavers",
 "High Weaver Selene Arkwright":"Weavers","Reno":"Independent","Saya Kurogane":"Kurogane",
 "Amara Khalil":"Weavers","Mei Ling Zhao (Weaver of Silence)":"Weavers",
 "Isabella Cortez":"Weavers","Omar al-Sayed":"Independent","Dr. Elias Thorn":"Independent",
 "Freya Haldorsdottir":"Rankers","Soren Blackwood":"Independent","Kiritaka Yagami":"Yagami",
 "Sylvara Kane":"Independent","The King (Ivory Board)":"Ivory Board",
 "VeilNet Anchor":"Ivory Board","The Maid":"Independent",
}

# build image index: lowercase name -> relative asset path
img_index = {}
for root,_,files in os.walk(ILL):
    for fn in files:
        if fn.lower().endswith((".png",".jpg",".jpeg",".webp")):
            stem = os.path.splitext(fn)[0].lower().replace(" ","").replace("_","")
            rel = os.path.relpath(os.path.join(root,fn), ILL).replace("\\","/")
            img_index[stem] = "assets/illustrations/" + rel

def find_image(name):
    # normalize name tokens
    clean = name.lower().replace("(","").replace(")","").replace("/"," ").replace("-"," ")
    tokens = [t for t in clean.split() if t not in ("the","high","master","lady","dr.","dr","weaver","key","board","of","a")]
    # build candidate stems
    cands = []
    if len(tokens) >= 2:
        cands.append(tokens[-1])   # last name
        cands.append(tokens[0])    # first name
    else:
        cands.append(tokens[0])
    # also full joined
    cands.append("".join(tokens))
    # skip collages
    pool = {k:v for k,v in img_index.items() if "collage" not in k}
    for cand in cands:
        cn = cand.replace(" ","")
        for k,v in pool.items():
            if k == cn:
                return v
    for cand in cands:
        cn = cand.replace(" ","")
        for k,v in pool.items():
            if k.startswith(cn) and len(cn) >= 3:
                return v
    for cand in cands:
        cn = cand.replace(" ","")
        for k,v in pool.items():
            if cn in k:
                return v
    return None

# parse sections
chars = []
current = None
for raw in text.splitlines():
    line = raw.strip()
    if not line:
        continue
    if set(line) <= set("=") and len(line) >= 5:
        continue
    m = re.match(r"^\d+\.\s*(.+)$", line)
    if m and current is not None:
        current["quotes"].append(m.group(1).strip().strip('"'))
        continue
    if current is not None and current["quotes"]:
        chars.append(current)
    current = {"name": line, "faction": FACTION.get(line, "Other"),
               "quotes": [], "image": find_image(line)}
if current is not None and current["quotes"]:
    chars.append(current)

with open(os.path.join(OUT,"data","characters.json"),"w",encoding="utf-8") as f:
    json.dump(chars, f, ensure_ascii=False, indent=2)
print("characters:", len(chars))
for c in chars[:5]:
    print(c["name"], c["faction"], c["image"])

# ---------- 2. Novels ----------
novels_meta = [
 ("1_0override zone-the dark maiden.docx", "Override Zone: The Dark Maiden", "novel_1.json"),
 ("2_0 The 'Hart' that shall beat.docx", "The Hart That Shall Beat", "novel_2.json"),
 ("3_0Override Zone the blood tournament.docx", "Override Zone: The Blood Tournament", "novel_3.json"),
 ("4_0Override Zone Cobalt Knight.docx", "Override Zone: Cobalt Knight", "novel_4.json"),
]
novels_list = []
for fn,title,outfn in novels_meta:
    d = docx.Document(os.path.join(BASE, fn))
    paras = [p.text for p in d.paragraphs]
    # drop trailing empties, keep internal blanks as scene breaks marker
    # collapse multiple blanks into one empty string marker
    cleaned = []
    prev_blank = False
    for p in paras:
        t = p.strip()
        if t == "":
            if not prev_blank and cleaned:
                cleaned.append("")  # scene break
            prev_blank = True
        else:
            cleaned.append(t)
            prev_blank = False
    # remove leading/trailing blanks
    while cleaned and cleaned[0]=="": cleaned.pop(0)
    while cleaned and cleaned[-1]=="": cleaned.pop()
    with open(os.path.join(OUT,"data",outfn),"w",encoding="utf-8") as f:
        json.dump({"title":title,"paragraphs":cleaned}, f, ensure_ascii=False)
    novels_list.append({"id":outfn.replace(".json",""),"title":title,"file":outfn,"paragraphs":len(cleaned)})
    print(title, len(cleaned), "paras")

with open(os.path.join(OUT,"data","novels.json"),"w",encoding="utf-8") as f:
    json.dump(novels_list, f, ensure_ascii=False, indent=2)

# ---------- 3. Lore ----------
disclaimer = open(os.path.join(BASE,"disclaimer.txt"),encoding="utf-8").read().strip()
lore = {
  "disclaimer": disclaimer,
  "factions": [
    {"name":"Hart Family","desc":"The central family. Power, cruelty, and inheritance define them."},
    {"name":"Yagami","desc":"Naobito and Hana's line. Analytical, survival-driven."},
    {"name":"Weavers","desc":"Those who pull threads of reality — Elara, Selene, Lucien, Kael, Mireille, Amara, Isabella, Mei Ling."},
    {"name":"Rankers","desc":"Combatants who climb the lists — Asha, Viktor, Kenshi, Freya, Isolde."},
    {"name":"Keys","desc":"Nemimoth and the Keys of Hunger."},
    {"name":"Ivory Board","desc":"The governing body — The King, VeilNet Anchor."},
    {"name":"Kurogane","desc":"Saya Kurogane and allies."},
    {"name":"Independent","desc":"Rogue actors: Leon, Proxy, Reno, Omar, Soren, Elias Thorn, Sylvara, The Maid."},
    {"name":"Dark Maiden","desc":"Yurei Himura — the entity behind the puzzle."},
  ]
}
with open(os.path.join(OUT,"data","lore.json"),"w",encoding="utf-8") as f:
    json.dump(lore, f, ensure_ascii=False, indent=2)

# ---------- 4. Copy illustrations ----------
dst_root = os.path.join(OUT,"assets","illustrations")
count=0
for root,_,files in os.walk(ILL):
    for fn in files:
        if fn.lower().endswith((".png",".jpg",".jpeg",".webp")):
            src = os.path.join(root,fn)
            rel = os.path.relpath(src, ILL)
            dst = os.path.join(dst_root, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            count+=1
# ---------- 5. Gallery index ----------
gallery = []
for root,_,files in os.walk(ILL):
    for fn in files:
        if fn.lower().endswith((".png",".jpg",".jpeg",".webp")):
            rel = os.path.relpath(os.path.join(root,fn), ILL).replace("\\","/")
            folder = rel.split("/")[0] if "/" in rel else "root"
            gallery.append({"path":"assets/illustrations/"+rel,"name":fn,"folder":folder})
with open(os.path.join(OUT,"data","gallery.json"),"w",encoding="utf-8") as f:
    json.dump(gallery, f, ensure_ascii=False, indent=2)
print("gallery entries:", len(gallery))
print("images copied:", count)
print("DONE")
