import { chromium } from 'playwright';
import path from 'path';

const dir = path.resolve('deck');
const url = 'file://' + path.join(dir, 'index.html');
const mode = process.argv[2] || 'pdf';

const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 2 });
await page.goto(url, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(400);

if (mode === 'pdf') {
  await page.pdf({
    path: path.join(dir, 'MollieYoga-Brand-Concepts.pdf'),
    width: '1280px', height: '720px',
    printBackground: true, pageRanges: '', preferCSSPageSize: false,
  });
  console.log('PDF written');
} else {
  // screenshot specific pages: render.mjs shot 1,3,4
  const nums = (process.argv[3] || '1').split(',').map(n => parseInt(n) - 1);
  const sections = await page.$$('.page');
  for (const n of nums) {
    await sections[n].screenshot({ path: path.join(dir, `preview-${n + 1}.png`) });
    console.log('shot', n + 1);
  }
}
await browser.close();
