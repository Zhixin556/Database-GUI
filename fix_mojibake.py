from pathlib import Path

file_path = Path(r'C:\BZX\Python\3_GUI_EMVELOPE\Database-GUI\Database-GUI\index.html')
text = file_path.read_text(encoding='utf-8')
replacements = {
    'ðŸ“–': '📘',
    'Ã—': '×',
    'â˜…': '★',
    'âš ï¸': '⚠️',
    'ðŸš€': '🚀',
    'ðŸ”': '📖',
    'ðŸ’¡': '💡',
    'ðŸ“‚': '📊',
    'ðŸ”§': '🛠️',
    'âŒ¨ï¸': '✨',
    'ðŸ“ž': '📞',
    'âŒ': '✗',
    'âœ…': '✓',
    'ðŸ”„': '📦',
    'ðŸ’¾': '💾',
    'ðŸ“„': '📄',
    'ðŸŽ¯': '🔍',
    'ðŸŽ¨': '💡',
    'Â±': '±',
    'â„ƒ': '°C',
    'â€™': "'",
    'â€œ': '“',
    'â€': '”',
    'â€“': '–',
    'â€”': '—',
    'ï¼š': ':',
    'ï¼Ž': '...',
    'â€¢': '•',
    'Ã¢': '¢',
    'ã€': '}',
    'ã€': '{',
    'ã€': '"',
    'ã€': '"',
    'ã€': '"',
    'Â': ' ',
    'Ã': 'A',
}

orig = text
for old, new in replacements.items():
    text = text.replace(old, new)

# Fix the most visible placeholder corruption known in the document.
text = text.replace('23Â±5â„ƒ ;20%RH~80%RH(ESD20%~40%)', '23±5°C ;20%RH~80%RH(ESD20%~40%)')
text = text.replace('13.0Â±0.5V', '13.0±0.5V')
text = text.replace('â˜… Yellow highlighted fields are mandatory', '★ Yellow highlighted fields are mandatory')
text = text.replace('â˜…', '★')
text = text.replace('âŒ', '✗')
text = text.replace('âœ…', '✓')

# Write back only if content changed.
if text != orig:
    file_path.write_text(text, encoding='utf-8')
    print('Updated mojibake text in index.html')
else:
    print('No mojibake replacements needed')
