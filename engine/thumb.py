import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
D = Path(__file__).parent
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox', '--disable-gpu'])
    pg = b.new_page(viewport={'width': 1280, 'height': 720})
    for v in sys.argv[1:] or ['A', 'B']:
        pg.goto(f'file://{D}/thumb.html?v={v}'); pg.wait_for_function('window.done'); pg.evaluate('document.fonts.ready')
        pg.locator('#c').screenshot(path=str(D / f'001-thumb-{v}.png'))
    b.close()
