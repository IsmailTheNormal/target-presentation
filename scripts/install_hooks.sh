#!/bin/bash
# Target International School — Git Hooks Installer
# Installs localization pre-commit hook

HOOK_DIR="$(git rev-parse --show-toplevel)/.git/hooks"

if [ ! -d "$HOOK_DIR" ]; then
  echo "Error: .git/hooks directory not found."
  exit 1
fi

cat << 'EOF' > "$HOOK_DIR/pre-commit"
#!/bin/bash
# Target International School — i18n Pre-Commit Hook
# Guarantees 100% trilingual coverage (UZ, RU, EN)

echo "🔍 Tekshirilmoqda: i18n lokalizatsiya standarti (UZ, RU, EN)..."
python3 scripts/verify_i18n.py --staged

EXIT_CODE=$?
if [ $EXIT_CODE -ne 0 ]; then
  echo ""
  echo "❌ XATOLIK: Commit to'xtatildi! Staged fayllarda i18n tarjima xatolari bor."
  echo "💡 Yuqoridagi ko'rsatilgan fayl va qatorlardagi 'data-ru' / 'data-en' atributlarini to'ldiring."
  exit 1
fi

echo "✅ i18n tekshiruvi muvaffaqiyatli yakunlandi!"
exit 0
EOF

chmod +x "$HOOK_DIR/pre-commit"
echo "✅ Pre-commit hook successfully installed to $HOOK_DIR/pre-commit"
