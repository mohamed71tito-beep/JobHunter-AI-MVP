from .base import JobSource, JobRecord


class JobOpportunitiesSource(JobSource):
    name = "jobopportunities"

    async def search(
        self,
        query: str,
        location: str = ""
    ) -> list[JobRecord]:
        """
        Job Opportunities source placeholder.

        سيتم إضافة طريقة جلب البيانات الفعلية
        لهذا المصدر بعد تحديد الـ API أو الصفحة
        المسموح باستخدامها.
        """

        return []