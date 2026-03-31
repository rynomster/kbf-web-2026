/**
 * build.js - Static Site Generator for KBF
 * Injects shared header and footer into all HTML files.
 * Usage: node build.js
 */
const fs = require('fs');
const path = require('path');

const templatesDir = path.join(__dirname, 'templates');
const header = fs.readFileSync(path.join(templatesDir, 'header.html'), 'utf8');
const footer = fs.readFileSync(path.join(templatesDir, 'footer.html'), 'utf8');

const files = fs.readdirSync(__dirname).filter(f => f.endsWith('.html') && !f.includes('shared-'));

files.forEach(file => {
    let content = fs.readFileSync(path.join(__dirname, file), 'utf8');
    
    // Replace <header>...</header> block
    content = content.replace(/<header[^>]*>([\s\S]*?)<\/header>/i, header);
    
    // Replace <footer[^>]*>...</footer> block
    content = content.replace(/<footer[^>]*>([\s\S]*?)<\/footer>/i, footer);
    
    fs.writeFileSync(path.join(__dirname, file), content);
    console.log(`✓ Processed ${file}`);
});

console.log('Build complete: All headers and footers standardized.');
