from .base import JobSource, JobRecord


class DemoSource(JobSource):
    name = "demo"

    async def search(self, query: str, location: str = ""):
        return []