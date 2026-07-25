import { JSDOM } from 'jsdom';
import fs from 'fs';
import path from 'path';

// Just simple heuristic: read Home.tsx and match the 7th div inside something?
// Actually JSDOM might need rendered react.
