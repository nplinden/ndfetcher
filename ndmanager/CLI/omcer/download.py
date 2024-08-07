import shutil
import subprocess as sp
import tempfile
from contextlib import chdir
from pathlib import Path

from ndmanager.API.data import (OPENMC_LANL_LIBS, OPENMC_NUCLEAR_DATA,
                                OPENMC_OFFICIAL_LIBS)


def download(libname):
    with tempfile.TemporaryDirectory() as tmpdir:
        with chdir(tmpdir):
            if libname[:9] == "official:":
                name = libname[9:]
                dico = OPENMC_OFFICIAL_LIBS[name]
                sp.run(["wget", "-q", "--show-progress", dico["source"]])
                sp.run(["tar", "xf", dico["tarname"]])

                source = Path(dico["extractedname"])
                target = OPENMC_NUCLEAR_DATA / "official" / name
                target.parent.mkdir(exist_ok=True, parents=True)
                shutil.rmtree(target, ignore_errors=True)
                shutil.move(source, target)
            elif libname[:5] == "lanl:":
                name = libname[5:]
                dico = OPENMC_LANL_LIBS[name]
                sp.run(["wget", "-q", "--show-progress", dico["source"]])
                sp.run(["tar", "xf", dico["tarname"]])

                source = Path(dico["extractedname"])
                target = OPENMC_NUCLEAR_DATA / "lanl" / name
                target.parent.mkdir(exist_ok=True, parents=True)
                shutil.rmtree(target, ignore_errors=True)
                shutil.move(source, target)
