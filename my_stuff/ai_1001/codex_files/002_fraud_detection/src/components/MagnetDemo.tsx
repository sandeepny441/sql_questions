import { useMemo, useState } from 'react';
import { chooseCaughtNotes, createLoanPool, updateReviewStatus } from '../lib/demo-data';
import type { CaughtNote, LoanRecord, ReviewStatus } from '../types';
import { SidebarPanel } from './SidebarPanel';
import { FraudScene } from './scene/FraudScene';

export function MagnetDemo() {
  const [loans, setLoans] = useState<LoanRecord[]>(() => createLoanPool());
  const [caughtNotes, setCaughtNotes] = useState<CaughtNote[]>([]);
  const [pullSignal, setPullSignal] = useState(0);
  const [resetSignal, setResetSignal] = useState(0);

  const headlineStats = useMemo(() => {
    const suspicious = loans.filter((loan) => loan.actualFraud).length;
    return {
      suspicious,
      clean: loans.length - suspicious,
    };
  }, [loans]);

  const handleTriggerMagnet = () => {
    setCaughtNotes((current) => {
      const existingIds = new Set(current.map((note) => note.loanId));
      const additions = chooseCaughtNotes(loans, existingIds);
      return additions.length > 0 ? [...current, ...additions] : current;
    });
  };

  const handleReset = () => {
    setLoans(createLoanPool());
    setCaughtNotes([]);
    setResetSignal((signal) => signal + 1);
  };

  const handleDipPull = () => {
    setPullSignal((signal) => signal + 1);
  };

  const handleReviewChange = (loanId: string, status: ReviewStatus) => {
    setCaughtNotes((current) => updateReviewStatus(current, loanId, status));
  };

  return (
    <main className="min-h-screen px-4 py-5 sm:px-6 lg:px-8">
      <div className="mx-auto flex max-w-[1520px] flex-col gap-5">
        <header className="glass-panel rounded-[32px] px-6 py-6 sm:px-8">
          <div className="flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
            <div className="max-w-3xl">
              <p className="text-xs uppercase tracking-[0.34em] text-finance/80">Fraud Magnet</p>
              <h1 className="mt-3 font-display text-4xl font-bold tracking-tight text-white sm:text-[3.4rem]">
                Drop a magnet ball into a jar of mortgage loans and pull out the shady ones.
              </h1>
              <p className="mt-4 max-w-2xl text-base leading-7 text-slate-300">
                Each sticky note is a loan. Most are ordinary. A small cluster shares the same bad
                pattern, so when the magnet comes back out, those lookalike loans cling to it.
              </p>
            </div>

            <div className="grid gap-3 sm:grid-cols-3">
              <div className="metric-card rounded-2xl px-4 py-4">
                <p className="text-xs uppercase tracking-[0.18em] text-slate-400">Notes In Jar</p>
                <p className="mt-2 font-display text-3xl font-semibold text-white">{loans.length}</p>
              </div>
              <div className="metric-card rounded-2xl px-4 py-4">
                <p className="text-xs uppercase tracking-[0.18em] text-slate-400">Shady Cluster</p>
                <p className="mt-2 font-display text-3xl font-semibold text-warning">
                  {headlineStats.suspicious}
                </p>
              </div>
              <div className="metric-card rounded-2xl px-4 py-4">
                <p className="text-xs uppercase tracking-[0.18em] text-slate-400">Already Pulled</p>
                <p className="mt-2 font-display text-3xl font-semibold text-accent">
                  {caughtNotes.length}
                </p>
              </div>
            </div>
          </div>
        </header>

        <section className="grid gap-5 xl:grid-cols-[minmax(0,1fr)_25rem]">
          <div className="glass-panel scene-panel relative overflow-hidden rounded-[32px] p-3 sm:p-4">
            <div className="absolute left-5 top-5 z-10 max-w-md rounded-[24px] border border-white/10 bg-slate-950/42 p-4 backdrop-blur-md">
              <p className="text-xs uppercase tracking-[0.26em] text-finance/80">The story</p>
              <div className="mt-3 space-y-3 text-sm leading-6 text-slate-200">
                <p>
                  1. The jar holds a messy population of mortgage loans as sticky notes.
                </p>
                <p>
                  2. The ball represents a known bad pattern you dip into the system.
                </p>
                <p>
                  3. When you pull it out, related shady loans snap to the magnet.
                </p>
              </div>
            </div>

            <div className="absolute bottom-5 left-5 z-10 rounded-2xl border border-white/10 bg-slate-950/40 px-4 py-3 text-sm text-slate-200 backdrop-blur-md">
              Drag the ball into the jar, then lift it out.
            </div>

            <div className="h-[68vh] min-h-[560px] w-full overflow-hidden rounded-[28px]">
              <FraudScene
                loans={loans}
                caughtNotes={caughtNotes}
                pullSignal={pullSignal}
                resetSignal={resetSignal}
                onTriggerMagnet={handleTriggerMagnet}
              />
            </div>
          </div>

          <SidebarPanel
            loans={loans}
            caughtNotes={caughtNotes}
            onReviewChange={handleReviewChange}
            onReset={handleReset}
            onDipPull={handleDipPull}
          />
        </section>
      </div>
    </main>
  );
}
