"use client";

import { useState } from "react";

type Job = {
  id: number;
  title: string;
  company: string;
  location: string;
  work_type: string;
  experience_level: string;
  salary: string;
  source: string;
  source_url: string;
  description: string;
};

export default function Home() {
  const [query, setQuery] = useState("Data Analyst");
  const [location, setLocation] = useState("Egypt");
  const [jobs, setJobs] = useState<Job[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function searchJobs() {
    if (!query.trim()) return;

    setLoading(true);
    setError("");

    try {
      const params = new URLSearchParams({
        q: query,
        location,
        refresh: "true",
      });

      const response = await fetch(
        `http://127.0.0.1:8000/api/jobs/search?${params}`
      );

      if (!response.ok) {
        throw new Error("Failed to fetch jobs");
      }

      const data = await response.json();

      setJobs(data.jobs || []);
    } catch (err) {
      console.error(err);
      setError(
        "حدث خطأ أثناء جلب الوظائف. تأكد أن الـBackend يعمل."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-6xl px-6 py-10">

        {/* Header */}
        <header className="mb-10">
          <h1 className="text-4xl font-bold tracking-tight">
            JobHunter AI
          </h1>

          <p className="mt-2 text-slate-400">
            ابحث عن الوظائف من مصادر متعددة في مكان واحد
          </p>
        </header>

        {/* Search */}
        <section className="rounded-2xl border border-slate-800 bg-slate-900 p-5 shadow-xl">

          <div className="grid gap-4 md:grid-cols-[1fr_1fr_auto]">

            <input
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  searchJobs();
                }
              }}
              placeholder="مثال: Data Analyst"
              className="rounded-xl border border-slate-700 bg-slate-950 px-4 py-3 outline-none focus:border-blue-500"
            />

            <input
              value={location}
              onChange={(e) => setLocation(e.target.value)}
              placeholder="الموقع: Egypt / Cairo"
              className="rounded-xl border border-slate-700 bg-slate-950 px-4 py-3 outline-none focus:border-blue-500"
            />

            <button
              onClick={searchJobs}
              disabled={loading}
              className="rounded-xl bg-blue-600 px-7 py-3 font-semibold transition hover:bg-blue-500 disabled:cursor-not-allowed disabled:opacity-50"
            >
              {loading ? "جاري البحث..." : "بحث عن وظائف"}
            </button>

          </div>
        </section>

        {/* Error */}
        {error && (
          <div className="mt-5 rounded-xl border border-red-800 bg-red-950/40 p-4 text-red-300">
            {error}
          </div>
        )}

        {/* Results header */}
        {jobs.length > 0 && (
          <div className="mt-8 flex items-center justify-between">
            <h2 className="text-xl font-semibold">
              نتائج البحث
            </h2>

            <span className="rounded-full bg-slate-800 px-4 py-2 text-sm text-slate-300">
              {jobs.length} وظيفة
            </span>
          </div>
        )}

        {/* Jobs */}
        <section className="mt-5 grid gap-5">

          {jobs.map((job) => (
            <article
              key={job.id}
              className="rounded-2xl border border-slate-800 bg-slate-900 p-6 transition hover:border-blue-600"
            >

              <div className="flex flex-col gap-5 md:flex-row md:items-start md:justify-between">

                <div className="flex-1">

                  <div className="mb-3 flex flex-wrap gap-2">

                    <span className="rounded-full bg-blue-500/10 px-3 py-1 text-xs text-blue-400">
                      {job.source}
                    </span>

                    {job.work_type &&
                      job.work_type !== "Not specified" && (
                        <span className="rounded-full bg-emerald-500/10 px-3 py-1 text-xs text-emerald-400">
                          {job.work_type}
                        </span>
                      )}

                  </div>

                  <h3 className="text-2xl font-semibold">
                    {job.title}
                  </h3>

                  <p className="mt-2 text-lg text-slate-300">
                    {job.company}
                  </p>

                  <div className="mt-4 flex flex-wrap gap-3 text-sm text-slate-400">

                    <span>
                      📍 {job.location}
                    </span>

                    {job.experience_level &&
                      job.experience_level !== "Not specified" && (
                        <span>
                          🎓 {job.experience_level}
                        </span>
                      )}

                    {job.salary &&
                      job.salary !== "Not specified" && (
                        <span>
                          💰 {job.salary}
                        </span>
                      )}

                  </div>

                  {job.description && (
                    <p className="mt-5 line-clamp-3 text-sm leading-6 text-slate-400">
                      {job.description}
                    </p>
                  )}

                </div>

                <div className="shrink-0">

                  {job.source_url && (
                    <a
                      href={job.source_url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="inline-flex rounded-xl bg-blue-600 px-6 py-3 font-semibold transition hover:bg-blue-500"
                    >
                      Apply Now →
                    </a>
                  )}

                </div>

              </div>

            </article>
          ))}

        </section>

        {/* Empty state */}
        {!loading && jobs.length === 0 && !error && (
          <div className="mt-12 rounded-2xl border border-dashed border-slate-700 p-10 text-center text-slate-500">
            اكتب الوظيفة والموقع ثم اضغط "بحث عن وظائف"
          </div>
        )}

      </div>
    </main>
  );
}
