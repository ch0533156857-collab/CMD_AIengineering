import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from dotenv import load_dotenv
load_dotenv()

# חייב להיות לפני import של google.genai
import certifi
os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = certifi.where()
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

from google import genai
from google.genai import types
import gradio as gr

# ------------------------------
# אתחול מודל
# ------------------------------
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ------------------------------
# פרומפט מערכת
# ------------------------------
SYSTEM_PROMPT = """אתה מומחה בפקודות Windows CLI. תפקידך לתרגם הוראות בשפה טבעית (עברית או אנגלית) לפקודות Windows תקניות.
החזר רק את הפקודה עצמה, ללא הסברים או טקסט נוסף.
אם ההוראה לא ברורה או לא ניתן לתרגמה לפקודה, החזר: ERROR: לא ניתן לתרגם הוראה זו.
"""

# ------------------------------
# פונקציה להמרת הוראה לפקודה
# ------------------------------
def natural_to_cli(user_input: str) -> str:
    if not user_input.strip():
        return "אנא הכניסי הוראה."

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
            ),
            contents=f"הוראה: {user_input}",
        )
        command = response.text.strip()
        # מחזיר שורה ראשונה בלבד
        return command.split("\n")[0].strip()
    except Exception as e:
        return f"❌ שגיאה: {str(e)}"

# ------------------------------
# פונקציה ליצירת ממשק Gradio
# ------------------------------
def create_gradio_interface():
    custom_css = """
    .gradio-container { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .main-header { text-align: center; color: white; padding: 2rem; background: rgba(255, 255, 255, 0.1); border-radius: 15px; margin-bottom: 2rem; backdrop-filter: blur(10px); }
    #component-0 { background: white; border-radius: 15px; padding: 2rem; box-shadow: 0 10px 40px rgba(0,0,0,0.2); }
    .input-box textarea { border: 2px solid #667eea !important; border-radius: 10px !important; font-size: 16px !important; }
    .output-box { background: #f8f9fa !important; border: 2px solid #28a745 !important; border-radius: 10px !important; padding: 1rem !important; font-family: 'Courier New', monospace !important; font-size: 16px !important; direction: ltr !important; }
    .submit-btn { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important; border: none !important; color: white !important; font-size: 18px !important; padding: 12px 30px !important; border-radius: 10px !important; font-weight: bold !important; }
    """

    with gr.Blocks(css=custom_css, title="Windows CLI Generator", theme=gr.themes.Soft()) as demo:
        gr.HTML("""
            <div class="main-header">
                <h1>🖥️ Windows CLI Command Generator</h1>
                <p style="font-size: 18px; margin-top: 10px;">תרגום הוראות לפקודות Windows | Powered by Gemini</p>
            </div>
        """)
        
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("""
                ### 📋 איך להשתמש:
                1. כתבי הוראה בשפה טבעית (עברית/אנגלית)
                2. לחצי על "צור פקודה"
                3. העתיקי והריצי את הפקודה ב-CMD
                
                ### 💡 דוגמאות:
                - "צור תיקייה בשם test"
                - "מחק קבצים ישנים"
                - "הצג את כל התהליכים"
                - "העתק קובץ מתיקייה אחת לאחרת"
                """)
        
        with gr.Row():
            with gr.Column():
                user_input = gr.Textbox(
                    label="🎯 ההוראה שלך",
                    placeholder="לדוגמה: צור תיקייה בשם projects בדיסק C",
                    lines=3,
                    elem_classes="input-box"
                )
                
                submit_btn = gr.Button("✨ צור פקודה", variant="primary", elem_classes="submit-btn")
                
                output = gr.Textbox(
                    label="⚡ הפקודה שנוצרה",
                    placeholder="הפקודה תופיע כאן...",
                    lines=5,
                    elem_classes="output-box",
                    show_copy_button=True
                )
        
        gr.Markdown("""
        ---
        ### ⚠️ הערות חשובות:
        - בדקי את הפקודה לפני הרצה!
        - פקודות מסוימות דורשות הרשאות מנהל (Run as Administrator)
        - שמרי גיבוי לפני פקודות מחיקה
        """)
        
        submit_btn.click(
            fn=natural_to_cli,
            inputs=[user_input],
            outputs=output
        )
        
        gr.Examples(
            examples=[
                ["צור תיקייה בשם projects בדיסק C"],
                ["הצג את כל הקבצים בתיקייה הנוכחית"],
                ["מחק את כל הקבצים עם סיומת tmp"],
                ["העתק את כל התמונות לתיקיית backup"],
                ["הצג את כל התהליכים הפועלים"],
                ["בדוק את גרסת Windows"],
                ["נקה את המסך"],
                ["הצג את תוכן הקובץ config.txt"],
            ],
            inputs=user_input,
        )

    return demo

# ------------------------------
# הרצת הממשק
# ------------------------------
if __name__ == "__main__":
    if not os.getenv("GEMINI_API_KEY"):
        print("❌ שגיאה: GEMINI_API_KEY לא נמצא בקובץ .env")
        exit(1)
    
    print("🚀 מתחיל את האפליקציה...")
    print("📍 פתחי את הדפדפן בכתובת שתופיע למטה")
    demo = create_gradio_interface()
    demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)), show_error=True)
