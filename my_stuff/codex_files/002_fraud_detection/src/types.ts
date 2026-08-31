export type LoanTone = 'neutral' | 'risk' | 'clean';
export type ReviewStatus = 'fraud' | 'falsePositive';

export interface LoanRecord {
  id: string;
  borrowerName: string;
  officerName: string;
  amount: number;
  county: string;
  fico: number;
  ltv: number;
  channel: string;
  employer: string;
  occupancy: 'Owner Occupied' | 'Investment' | 'Second Home';
  tone: LoanTone;
  actualFraud: boolean;
  matchScore: number;
  atlasIndex: number;
}

export interface CaughtNote {
  loanId: string;
  reviewStatus: ReviewStatus;
  attachedAt: number;
  slot: [number, number, number];
}
