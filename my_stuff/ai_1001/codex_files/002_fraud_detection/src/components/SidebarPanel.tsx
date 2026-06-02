import { formatCurrency, formatPercent } from '../lib/format';
import type { CaughtNote, LoanRecord, ReviewStatus } from '../types';

interface SidebarPanelProps {
  loans: LoanRecord[];
  caughtNotes: CaughtNote[];
  onReviewChange: (loanId: string, status: ReviewStatus) => void;
  onReset: () => void;
  onDipPull: () => void;
}

function statusClasses(status: ReviewStatus) {
  return status === 'fraud'
    ? 'bg-emerald-400/12 text-emerald-200 ring-1 ring-emerald-300/20'
    : 'bg-orange-400/12 text-orange-200 ring-1 ring-orange-300/20';
}

export function SidebarPanel({
  loans,
  caughtNotes,
  onReviewChange,
  onReset,
  onDipPull,
}: SidebarPanelProps) {
  const loanMap = new Map(loans.map((loan) => [loan.id, loan]));
  const fraudCount = caughtNotes.filter((note) => note.reviewStatus === 'fraud').length;
  const falsePositiveCount = caughtNotes.length - fraudCount;
  const estimatedSavings = caughtNotes.reduce((total, note) => {
    if (note.reviewStatus !== 'fraud') {
      return total;
    }

    return total + (loanMap.get(note.loanId)?.amount ?? 0) * 0.11;
  }, 0);

  return (
    <aside className="glass-panel flex min-h-[28rem] flex-col rounded-[32px] p-5 sm:p-6">
      <div className="flex flex-col gap-4 border-b border-white/10 pb-5">
        <div>
          <p className="text-xs uppercase tracking-[0.26em] text-finance/75">Captured by the magnet</p>
          <h2 className="mt-2 font-display text-2xl font-semibold text-white">
            Review the loans that stuck
          </h2>
          <p className="mt-2 text-sm leading-6 text-slate-300">
            Most of these should be shady matches. A few are close-enough loans that the model still
            pulled in.
          </p>
        </div>

        <div className="grid grid-cols-2 gap-3">
          <button
            type="button"
            onClick={onDipPull}
            className="rounded-2xl bg-gradient-to-r from-accent via-finance to-accent px-4 py-3 text-sm font-semibold text-slate-950 transition hover:scale-[1.01]"
          >
            Dip &amp; Pull
          </button>
          <button
            type="button"
            onClick={onReset}
            className="rounded-2xl border border-white/15 bg-white/5 px-4 py-3 text-sm font-semibold text-white transition hover:bg-white/10"
          >
            Reset Simulation
          </button>
        </div>
      </div>

      <div className="mt-5 grid grid-cols-2 gap-3">
        <div className="metric-card rounded-2xl p-4">
          <p className="text-xs uppercase tracking-[0.2em] text-slate-400">Confirmed Shady</p>
          <p className="mt-3 font-display text-3xl font-semibold text-success">{fraudCount}</p>
        </div>
        <div className="metric-card rounded-2xl p-4">
          <p className="text-xs uppercase tracking-[0.2em] text-slate-400">Probably Fine</p>
          <p className="mt-3 font-display text-3xl font-semibold text-warning">
            {falsePositiveCount}
          </p>
        </div>
        <div className="metric-card rounded-2xl p-4">
          <p className="text-xs uppercase tracking-[0.2em] text-slate-400">Total Stuck</p>
          <p className="mt-3 font-display text-3xl font-semibold text-white">{caughtNotes.length}</p>
        </div>
        <div className="metric-card rounded-2xl p-4">
          <p className="text-xs uppercase tracking-[0.2em] text-slate-400">Fraud Savings</p>
          <p className="mt-3 font-display text-2xl font-semibold text-finance">
            {formatCurrency(estimatedSavings)}
          </p>
        </div>
      </div>

      <div className="mt-5 rounded-2xl border border-white/10 bg-white/5 p-4">
        <p className="text-xs uppercase tracking-[0.2em] text-slate-400">What the ball represents</p>
        <p className="mt-2 text-sm text-white">One known bad mortgage file</p>
        <p className="mt-3 text-sm leading-6 text-slate-300">
          The system turns that one bad example into a magnetic signature and uses it to surface loans
          with the same suspicious traits.
        </p>
      </div>

      <div className="mt-5 flex-1 overflow-hidden">
        <div className="mb-3 flex items-center justify-between">
          <p className="text-sm font-semibold text-white">Sticky notes on the ball</p>
          <p className="text-xs uppercase tracking-[0.2em] text-slate-400">live review</p>
        </div>

        <div className="scroll-skin h-[24rem] space-y-3 overflow-y-auto pr-1">
          {caughtNotes.length === 0 ? (
            <div className="rounded-2xl border border-dashed border-white/12 bg-white/4 p-5 text-sm leading-6 text-slate-300">
              Drag the ball into the jar and lift it back out, or press Dip &amp; Pull to run the motion
              automatically.
            </div>
          ) : (
            caughtNotes.map((note) => {
              const loan = loanMap.get(note.loanId);

              if (!loan) {
                return null;
              }

              return (
                <article
                  key={note.loanId}
                  className="rounded-2xl border border-white/10 bg-slate-950/30 p-4"
                >
                  <div className="flex items-start justify-between gap-3">
                    <div>
                      <p className="font-display text-lg font-semibold text-white">{loan.id}</p>
                      <p className="text-sm text-slate-300">{loan.borrowerName}</p>
                    </div>
                    <span className={`rounded-full px-3 py-1 text-xs font-semibold ${statusClasses(note.reviewStatus)}`}>
                      {note.reviewStatus === 'fraud' ? 'Shady Match' : 'Likely Noise'}
                    </span>
                  </div>

                  <dl className="mt-4 grid grid-cols-2 gap-3 text-sm text-slate-300">
                    <div>
                      <dt className="text-xs uppercase tracking-[0.18em] text-slate-500">Officer</dt>
                      <dd className="mt-1">{loan.officerName}</dd>
                    </div>
                    <div>
                      <dt className="text-xs uppercase tracking-[0.18em] text-slate-500">Amount</dt>
                      <dd className="mt-1">{formatCurrency(loan.amount)}</dd>
                    </div>
                    <div>
                      <dt className="text-xs uppercase tracking-[0.18em] text-slate-500">County</dt>
                      <dd className="mt-1">{loan.county}</dd>
                    </div>
                    <div>
                      <dt className="text-xs uppercase tracking-[0.18em] text-slate-500">Similarity</dt>
                      <dd className="mt-1">{formatPercent(loan.matchScore)}</dd>
                    </div>
                  </dl>

                  <div className="mt-4 grid grid-cols-2 gap-2">
                    <button
                      type="button"
                      onClick={() => onReviewChange(loan.id, 'fraud')}
                      className={`rounded-xl px-3 py-2 text-sm font-semibold transition ${
                        note.reviewStatus === 'fraud'
                          ? 'bg-emerald-400 text-slate-950'
                          : 'bg-emerald-400/10 text-emerald-200 hover:bg-emerald-400/20'
                      }`}
                    >
                      Confirm Shady
                    </button>
                    <button
                      type="button"
                      onClick={() => onReviewChange(loan.id, 'falsePositive')}
                      className={`rounded-xl px-3 py-2 text-sm font-semibold transition ${
                        note.reviewStatus === 'falsePositive'
                          ? 'bg-orange-300 text-slate-950'
                          : 'bg-orange-300/10 text-orange-200 hover:bg-orange-300/20'
                      }`}
                    >
                      Mark as Fine
                    </button>
                  </div>
                </article>
              );
            })
          )}
        </div>
      </div>
    </aside>
  );
}
