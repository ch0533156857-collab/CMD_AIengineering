# 🖥️ Windows CLI Command Generator
🌐 **Live Demo:** https://cmd-aiengineering.onrender.com

אפליקציית ווב שמתרגמת הוראות בשפה טבעית (עברית / אנגלית) לפקודות Windows CLI, באמצעות Gemini.

---

## ✨ תכונות

- קבלת הוראות בעברית או אנגלית
- תרגום אוטומטי לפקודות CMD / PowerShell תקניות
- ממשק גרפי נוח עם Gradio
- כפתור העתקה מובנה לפקודה שנוצרה
- 15 תרחישי בדיקה מוכנים

---

## 🚀 התקנה והרצה

### דרישות מקדימות
- Python 3.10+
- [uv](https://docs.astral.sh/uv/) מותקן
- Gemini API Key מ: https://aistudio.google.com/app/apikey

### שלבים

```bash
# 1. כניסה לתיקייה
cd windows-cli-generator

# 2. הגדרת API Key בקובץ .env
# GEMINI_API_KEY=AIzaSy...

# 3. התקנה והרצה
uv sync
uv run python app.py
```

האפליקציה תהיה זמינה בכתובת: http://127.0.0.1:7860

---

## 📁 מבנה הפרויקט

```
windows-cli-generator/
├── app.py              # קוד האפליקציה הראשי
├── pyproject.toml      # הגדרות פרויקט ותלויות
├── .env                # API Key (לא מועלה ל-Git!)
├── .env.example        # תבנית לקובץ .env
├── .gitignore
├── test_scenarios.md   # 15 תרחישי בדיקה
└── README.md
```

---

## 🐛 בעיות נפוצות

**"uv: command not found"**
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
# סגרי וכפתחי את הטרמינל אחרי ההתקנה
```

**"No module named 'gradio'"**
```bash
uv sync --reinstall
```

**"GEMINI_API_KEY not found"**
- וודאי שקובץ `.env` קיים (לא `.env.example`)
- וודאי שהמפתח מתחיל ב-`AIzaSy`

**"Port 7860 is already in use"**
```bash
# שני ב-app.py את השורה:
server_port=7861  # במקום 7860
```

---

## 🧪 בדיקות

15 תרחישי בדיקה מוכנים בקובץ `test_scenarios.md`, המכסים יצירה ומחיקה, הצגת מידע, העתקה והעברה, חיפוש, ופקודות רשת.

---

## 🔒 אבטחה

- לעולם אל תעלי את `.env` ל-GitHub
- בדקי כל פקודה לפני הרצה
- שמרי גיבוי לפני פקודות מחיקה

---

## 📚 תיעוד

- [Gradio Docs](https://gradio.app/docs/)
- [Gemini API Docs](https://ai.google.dev/gemini-api/docs)
- [uv Docs](https://docs.astral.sh/uv/)
