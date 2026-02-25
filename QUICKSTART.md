# ⚡ מדריך מהיר - 5 דקות להתחלה

## צ'ק-ליסט התקנה מהירה ✅

- [ ] Python 3.10+ מותקן
- [ ] uv מותקן
- [ ] API Key של Gemini מוכן
- [ ] VS Code פתוח

---

## 🚀 4 צעדים להרצה

### 1️⃣ הורדת הקבצים
צרי תיקייה חדשה והעתיקי את הקבצים:
```bash
mkdir windows-cli-generator
cd windows-cli-generator
```

העתיקי את הקבצים הבאים:
- ✅ `app.py`
- ✅ `pyproject.toml`
- ✅ `.env.example`

### 2️⃣ התקנת uv (אם עדיין לא)
```powershell
# הרצי ב-PowerShell כמנהל
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

בדקי שזה עובד:
```bash
uv --version
```

### 3️⃣ הגדרת API Key
```bash
# העתיקי את הקובץ
copy .env.example .env

# פתחי את .env ב-VS Code
code .env
```

הדביקי את המפתח שלך:
```
GEMINI_API_KEY=AIzaSy-xxxxx
```

💡 **איפה מקבלים API Key?**  
https://aistudio.google.com/app/apikey → Create API Key

### 4️⃣ הרצה!
```bash
# התקנת חבילות והרצה במכה אחת
uv sync
uv run python app.py
```

🎉 **זהו! האפליקציה רצה על:**  
http://127.0.0.1:7860

---

## 🧪 בדיקה ראשונה

1. פתחי את הדפדפן ב-http://127.0.0.1:7860
2. כתבי: **"צור תיקייה בשם test"**
3. לחצי "צור פקודה"
4. אם קיבלת `mkdir test` - מזל טוב! 🎊

---

## 🐛 בעיות נפוצות?

### ❌ "uv: command not found"
**פתרון:**
```bash
# סגרי וכפתחי את הטרמינל
# או הוסיפי ל-PATH ידנית
```

### ❌ "No module named 'gradio'"
**פתרון:**
```bash
uv sync --reinstall
```

### ❌ "GEMINI_API_KEY not found"
**פתרון:**
- וודאי שהקובץ `.env` קיים (לא `.env.example`)
- וודאי שהמפתח בפורמט הנכון (מתחיל ב-`AIzaSy`)

### ❌ "Port 7860 is already in use"
**פתרון:**
```bash
# שני ב-app.py את השורה:
server_port=7861  # במקום 7860
```

---

## 📊 השלב הבא - בדיקות

עכשיו שהאפליקציה רצה, עברי ל:
1. **קובץ `test_scenarios.md`** - 15 תרחישי בדיקה מוכנים
2. **צרי Google Sheet** עם התוצאות
3. **תעדי הכל** - גם הצלחות וגם כשלונות

---

## 💡 טיפים לעבודה

### הרצה מהירה בפעם הבאה:
```bash
cd windows-cli-generator
uv run python app.py
```

### עצירת האפליקציה:
לחצי `Ctrl+C` בטרמינל

### עריכת הקוד:
```bash
code app.py
```

### ניקוי והתקנה מחדש:
```bash
# מחיקת .venv והתקנה מחדש
rm -r .venv
uv sync
```

---

## 🎯 מה עכשיו?

1. ✅ האפליקציה רצה
2. ⏭️ צרי Google Sheet לתיעוד
3. ⏭️ העתיקי את 15 התרחישים מ-`test_scenarios.md`
4. ⏭️ הריצי כל תרחיש ותעדי את התוצאות
5. ⏭️ חשבי שיעור הצלחה

---

## 📞 עזרה נוספת

- **תיעוד Gradio:** https://gradio.app/docs/
- **תיעוד Gemini API:** https://ai.google.dev/gemini-api/docs
- **תיעוד uv:** https://docs.astral.sh/uv/

---

**בהצלחה! אם יש בעיה - תגידי לי! 💪**
