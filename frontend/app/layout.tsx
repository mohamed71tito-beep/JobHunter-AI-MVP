import "./globals.css";

export const metadata = {
  title: "JobHunter AI",
  description: "Search jobs from multiple sources",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body>{children}</body></html>;
}
