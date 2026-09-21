# Architecture

## Components
- Frontend: Next.js
- API: FastAPI
- Database: PostgreSQL
- Bot: python-telegram-bot
- AI layer: planned
- Job sources: isolated adapters in `backend/app/sources`

## Source policy
لا يتم افتراض أو تضمين تجاوز تسجيل الدخول أو الحماية أو القيود الخاصة بأي منصة. كل مصدر حقيقي يجب أن يستخدم API أو feed أو وسيلة وصول مسموح بها.
