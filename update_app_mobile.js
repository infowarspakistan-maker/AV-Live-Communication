const fs = require('fs');

let appContent = fs.readFileSync('src/App.tsx', 'utf8');

if (!appContent.includes("import { MobileBottomNav }")) {
  appContent = appContent.replace(
    "import { Footer } from './components/Footer';",
    "import { Footer } from './components/Footer';\nimport { MobileBottomNav } from './components/MobileBottomNav';"
  );
  
  appContent = appContent.replace(
    "<CookieConsent />\n      </div>",
    "<CookieConsent />\n      <MobileBottomNav />\n      </div>"
  );
  
  fs.writeFileSync('src/App.tsx', appContent);
}
