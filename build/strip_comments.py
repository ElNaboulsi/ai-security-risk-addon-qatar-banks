import zipfile, shutil, re, sys
for src in sys.argv[1:]:
    tmp = src + ".tmp"
    with zipfile.ZipFile(src) as zi:
        c = zi.read("word/comments.xml").decode()
        assert "<w:comment " not in c, "real comments present"
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
            for it in zi.infolist():
                if it.filename in ("word/comments.xml", "word/_rels/comments.xml.rels"): continue
                d = zi.read(it.filename)
                if it.filename == "[Content_Types].xml":
                    d = re.sub(rb'<Override PartName="/word/comments.xml"[^>]*/>', b"", d)
                if it.filename == "word/_rels/document.xml.rels":
                    d = re.sub(rb'<Relationship [^>]*Target="comments.xml"[^>]*/>', b"", d)
                zo.writestr(it, d)
    shutil.move(tmp, src); print("stripped", src)
