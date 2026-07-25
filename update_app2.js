const fs = require('fs');

let appContent = fs.readFileSync('src/App.tsx', 'utf8');

// Undo the previous wrapping of <Routes> directly inside <AnimatePresence>
appContent = appContent.replace(
  /<AnimatePresence mode="wait">\s*<Routes location=\{location\} key=\{location\.pathname\}>/,
  "<AnimatePresence mode=\"wait\">\n            <motion.div\n              key={location.pathname}\n              initial={{ opacity: 0, y: 15 }}\n              animate={{ opacity: 1, y: 0 }}\n              exit={{ opacity: 0, y: -15 }}\n              transition={{ duration: 0.3 }}\n              className=\"flex-grow flex flex-col\"\n            >\n              <Routes location={location}>"
);

appContent = appContent.replace(
  /<\/Routes>\s*<\/AnimatePresence>/,
  "</Routes>\n            </motion.div>\n          </AnimatePresence>"
);

fs.writeFileSync('src/App.tsx', appContent);
