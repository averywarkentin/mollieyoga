import { chromium } from 'playwright';
const SCRAP = '/tmp/claude-0/-home-user-mollieyoga/37bd5502-3909-51e6-96f3-079409da18e9/scratchpad';
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const page = await browser.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1.2 });
await page.goto('file:///home/user/mollieyoga/index.html', { waitUntil: 'networkidle' });
await page.addStyleTag({ content: 'html{scroll-behavior:auto !important;}' });
await page.evaluate(async () => {
  await document.fonts.ready;
  for (const spec of ['900 40px "Archivo"','700 40px "Archivo"','400 16px "Space Grotesk"'])
    await document.fonts.load(spec).catch(()=>{});
});
await page.waitForTimeout(1500);

const shot = async (id, file, offsetY = 0) => {
  await page.evaluate(id => {
    const el = document.getElementById(id);
    if (el) window.scrollTo(0, el.getBoundingClientRect().top + window.scrollY - 60);
    else window.scrollTo(0, 0);
  }, id);
  await page.waitForTimeout(300);
  if (offsetY) await page.evaluate(y => window.scrollBy(0, y), offsetY);
  await page.waitForTimeout(200);
  await page.screenshot({ path: SCRAP + '/' + file, clip: { x:0, y:0, width:1440, height:900 } });
  console.log(file);
};

await shot('c1', 'c1-hero.png');
await shot('c1', 'c1-posts.png', 560);
await shot('c1', 'c1-stories.png', 1220);
await shot('c2', 'c2-hero.png');
await shot('c2', 'c2-posts.png', 560);
await shot('c2', 'c2-stories.png', 1220);
await shot('c3', 'c3-hero.png');
await shot('c3', 'c3-posts.png', 560);
await shot('c3', 'c3-stories.png', 1220);

await browser.close();
