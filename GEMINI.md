# 🔵 GEMINI.md - Tool Rules (For Gemini)

This document provides specific instructions for the Gemini AI Model when working on this repository.

## Environment Context
- **OS**: Windows (PowerShell)
- **Project Type**: Static Site (Firebase Hosting)
- **Hosting CLI**: `firebase-tools`

## Execution Rules
1. **Always use Local Server**: When testing, use `firebase serve` to simulate the production environment accurately.
2. **Terminal Handling**: When using PowerShell, separate multiple commands with `;` instead of `&&`.
3. **File Editing**: Use `replace_file_content` for surgical edits. Avoid replacing entire large files unless necessary.
4. **Image Processing**: If images need compression, use the `Pillow` library in Python as demonstrated in past workflows.

## SEO & Webmaster Protocols
- When creating a new page, immediately add it to `sitemap.xml`.
- Ensure `robots.txt` is updated if new directories are added.
- Always include `<link rel="canonical" href="...">` in the `<head>`.

## Design Consistency
- Refer to `style.css` for existing CSS variables.
- Don't create new color tokens; stick to the Blueprint palette.
- All new components must inherit the `.glass-panel` class for consistency.
