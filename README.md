# JobHunter AI — MVP

منصة أولية للبحث وتجميع الوظائف من مصادر متعددة، مع FastAPI backend وNext.js frontend وTelegram bot.

## مهم
هذا الـMVP يستخدم مصدر Demo داخلي لتجربة النظام دون الاعتماد على scraping غير المصرح به.
طبقة `sources/` مصممة لإضافة APIs أو مصادر مسموح بها لاحقاً، ومنها LinkedIn حسب وسائل الوصول الرسمية/المسموح بها.

## المتطلبات
- Python 3.11+
- Node.js 20+
- PostgreSQL 15+ (أو Docker)
- Telegram Bot Token اختياري
- مفتاح مزود AI اختياري في المرحلة الأولى

## التشغيل السريع

### 1) Backend
```bash
cd backend
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env   # Windows
# أو cp .env.example .env
uvicorn app.main:app --reload
```

API: http://127.0.0.1:8000
Swagger: http://127.0.0.1:8000/docs

### 2) Frontend
```bash
cd frontend
npm install
npm run dev
```
ثم افتح http://localhost:3000

### 3) قاعدة البيانات
يمكن تشغيل PostgreSQL محلياً أو باستخدام:
```bash
docker compose up -d db
```
ثم عدّل DATABASE_URL في `.env`.

### 4) Telegram
```bash
cd telegram_bot
pip install -r requirements.txt
python bot.py
```

## الخطوة التالية
استبدال DemoSource بمصادر حقيقية تستخدم APIs/feeds/صفحات وظائف مسموح بها، ثم إضافة المصادقة وCV parsing وAI matching.
