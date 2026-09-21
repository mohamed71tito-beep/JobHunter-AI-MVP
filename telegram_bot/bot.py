import os
import httpx
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحباً بك في JobHunter AI!\n"
        "استخدم: /search Data Analyst\n"
        "مثال: /search Data Analyst"
    )

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args).strip()
    if not query:
        await update.message.reply_text("اكتب البحث بعد الأمر، مثال: /search Data Analyst")
        return
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{API_URL}/api/jobs/search", params={"q": query, "refresh": True})
        data = r.json()
    jobs = data.get("jobs", [])
    if not jobs:
        await update.message.reply_text("لم أجد وظائف في المصادر الحالية.")
        return
    lines = ["🔎 نتائج البحث:\n"]
    for i, job in enumerate(jobs[:10], 1):
        lines.append(f"{i}. {job['title']} — {job['company']}\n📍 {job['location']}\n🔗 {job['source_url']}")
    await update.message.reply_text("\n\n".join(lines))

def main():
    if not TOKEN:
        raise RuntimeError("ضع TELEGRAM_BOT_TOKEN في ملف .env")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("search", search))
    app.run_polling()

if __name__ == "__main__":
    main()
