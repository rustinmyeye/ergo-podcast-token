const puppeteer = require('puppeteer');
const path = require('path');

async function takeScreenshot(url, screenshotPath) {
    const browser = await puppeteer.launch({
        args: ['--no-sandbox', '--disable-setuid-sandbox'],
        userDataDir: path.join(__dirname, 'user_data') // Use user data directory
    });
    const page = await browser.newPage();

    await page.goto(url);
    await page.setViewport({ width: 1080, height: 1920 });

    // Introduce a simple sleep for 15 seconds to let the page load completely
    await new Promise(resolve => setTimeout(resolve, 15000)); // Wait for 15 seconds

    await page.evaluate(() => window.scrollBy(0, window.innerHeight / 6));

    const clip = {
        x: 95,
        y: 570,
        width: 600,
        height: 850
    };

    await page.screenshot({ path: screenshotPath, clip });
    await browser.close();
}

async function main() {
    const url = 'https://twitter.com/ergo_platform'; // change this to the twitter page you'd like to capture
    const screenshotPath = path.join(__dirname, 'screenshot', 'screenshot.png');

    await takeScreenshot(url, screenshotPath);
    console.log('Screenshot saved to:', screenshotPath);
}

main().catch(console.error);
