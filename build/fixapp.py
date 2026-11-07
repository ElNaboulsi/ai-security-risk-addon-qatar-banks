"""Blank the Application/AppVersion fields in docProps/app.xml of an OOXML file."""
import sys, zipfile, shutil, re, os

for fn in sys.argv[1:]:
    tmp = fn + ".tmp"
    with zipfile.ZipFile(fn) as zi, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
        for it in zi.infolist():
            data = zi.read(it.filename)
            if it.filename == "docProps/app.xml":
                t = data.decode("utf-8")
                t = re.sub(r"<Application>.*?</Application>", "<Application></Application>", t)
                t = re.sub(r"<AppVersion>.*?</AppVersion>", "", t)
                data = t.encode("utf-8")
            zo.writestr(it, data)
    shutil.move(tmp, fn)
    print("app.xml cleaned:", os.path.basename(fn))
