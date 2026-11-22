#!/usr/bin/env python3
"""Render aset channel dari kode (maskot v4): logo, banner, thumbnail.
Pakai: python3 engine/aset.py logo|banner|thumb-a|thumb-b KELUAR.png"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
jenis, out = sys.argv[1], Path(sys.argv[2])
here = Path(__file__).resolve().parent
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox', '--disable-gpu'])
    pg = b.new_page()
    pg.goto(f'file://{here / "aset.html"}#{jenis}')
    pg.evaluate('window.ready')
    out.parent.mkdir(parents=True, exist_ok=True)
    pg.locator('#c').screenshot(path=str(out))
    b.close()
print('selesai:', out)
