export function AppHeader() {
  return (
    <header className="border-b border-border bg-card px-4 sm:px-6 py-3 sm:py-4">
      <div className="max-w-7xl mx-auto flex items-center justify-between gap-3">
        <div className="min-w-0">
          <h1 className="text-lg sm:text-xl font-semibold text-foreground tracking-tight truncate">
            OSPF Ayurveda Knowledge Graph
          </h1>
          <p className="text-xs sm:text-sm text-muted-foreground">
            Drug Discovery Analysis for Oral Mucositis
          </p>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-xs text-muted-foreground bg-muted px-2 py-1 rounded-md font-mono">
            Prototype
          </span>
        </div>
      </div>
    </header>
  );
}
