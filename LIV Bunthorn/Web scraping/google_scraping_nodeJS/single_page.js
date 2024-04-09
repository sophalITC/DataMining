const puppeteer = require("puppeteer");

async function parsePlaces(page) {
  let places = [];
  const elements = await page.$$(".NrDZNb span");
  if (elements && elements.length) {
    for (const el of elements) {
      const name = await el.evaluate((span) => span.textContent);

      places.push({ name });
    }
  }
  return places;
}

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();
  await page.goto(
    "https://www.google.com/maps/search/tourist+place+near+Krong+Kampot/@10.620694,104.0731434,12z"
  );

  const places = await parsePlaces(page);
  console.log(places);
})();
