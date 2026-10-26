"""Stable launcher: update app/studio.py without rebuilding the EXE."""
import os,sys,runpy
from pathlib import Path
base=Path(sys.executable).resolve().parent if getattr(sys,'frozen',False) else Path(__file__).resolve().parent
os.environ['MRGEE_HOME']=str(base)
app_dir=base/'app'
if str(app_dir) not in sys.path: sys.path.insert(0,str(app_dir))
script=app_dir/'studio.py'
if not script.is_file():raise SystemExit('app/studio.py fehlt. Bitte vollständiges ZIP entpacken.')
runpy.run_path(str(script),run_name='__main__')
