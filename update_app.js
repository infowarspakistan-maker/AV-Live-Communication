const fs = require('fs');

let appContent = fs.readFileSync('src/App.tsx', 'utf8');

if (!appContent.includes("import { AnimatePresence, motion } from 'motion/react'")) {
  appContent = appContent.replace(
    "import { Routes, Route, Link, useNavigate } from 'react-router-dom';",
    "import { Routes, Route, Link, useNavigate, useLocation } from 'react-router-dom';\nimport { AnimatePresence, motion } from 'motion/react';\nimport { LoadingProvider } from './contexts/LoadingContext';"
  );
  
  // Wrap AuthProvider in LoadingProvider
  appContent = appContent.replace("<AuthProvider>", "<LoadingProvider>\n    <AuthProvider>");
  appContent = appContent.replace("</AuthProvider>", "</AuthProvider>\n    </LoadingProvider>");
  
  // Add location to Routes
  appContent = appContent.replace(
    "export default function App() {",
    "export default function App() {\n  const location = useLocation();"
  );
  
  // Wrap Routes in AnimatePresence and motion.div (which won't work perfectly inside Routes, wait)
  // We need to wrap each element in Route? Or wrap Routes in AnimatePresence and add location prop to Routes
  appContent = appContent.replace(
    "<Routes>",
    "<AnimatePresence mode=\"wait\">\n            <Routes location={location} key={location.pathname}>"
  );
  
  appContent = appContent.replace(
    "</Routes>",
    "</Routes>\n          </AnimatePresence>"
  );

  // For AnimatePresence to work, the children of AnimatePresence need to be components that have a key. We gave Routes a key, so it will unmount/remount the whole Routes tree.
  // Wait, if we unmount the whole Routes tree, we don't get page-level animations.
  // Instead, typically we can just add a PageWrapper that has motion.div, but wrapping Routes with location and key works because the new Routes instance mounts while the old one unmounts. But the exit animation must be inside the route element itself (e.g. motion.div).
  // Another simple approach is to wrap the Routes block in a motion.div:
  
  fs.writeFileSync('src/App.tsx', appContent);
}
