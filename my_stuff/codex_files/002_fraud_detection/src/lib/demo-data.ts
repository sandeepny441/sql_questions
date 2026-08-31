import * as THREE from 'three';
import type { CaughtNote, LoanRecord, ReviewStatus } from '../types';

const borrowers = [
  'Avery Mitchell',
  'Maya Patel',
  'Julian Brooks',
  'Sofia Ramirez',
  'Miles Carter',
  'Nora Kim',
  'Elijah Turner',
  'Chloe Bennett',
  'Hudson Flores',
  'Leah Collins',
  'Noah Price',
  'Camila Diaz',
  'Gavin Ross',
  'Zoe Fisher',
  'Ethan Murphy',
  'Layla Cooper',
];

const officers = [
  'Jordan Hale',
  'Priya Desai',
  'Marcus Lee',
  'Olivia Grant',
  'Daniel Moss',
  'Bianca Shaw',
  'Adrian West',
  'Naomi Ford',
];

const counties = [
  'Wayne County',
  'Cook County',
  'Broward County',
  'Maricopa County',
  'Travis County',
  'Fulton County',
  'Clark County',
  'King County',
];

const employers = [
  'Northgate Logistics',
  'Summit Dental Group',
  'Silverline Consulting',
  'Harbor Peak Staffing',
  'Blue Arch Holdings',
  'Crownlight Medical',
  'Verity Freight',
  'Pioneer Claims',
];

const channels = ['Broker', 'Retail', 'Correspondent', 'Wholesale'];
const occupancies: LoanRecord['occupancy'][] = [
  'Owner Occupied',
  'Investment',
  'Second Home',
];

function mulberry32(seed: number) {
  return function random() {
    let t = (seed += 0x6d2b79f5);
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function pick<T>(items: T[], random: () => number) {
  return items[Math.floor(random() * items.length)];
}

function clamp(value: number, min: number, max: number) {
  return Math.min(max, Math.max(min, value));
}

function createAttachmentSlots(count: number): [number, number, number][] {
  const slots: [number, number, number][] = [];
  const radius = 1.12;

  for (let index = 0; index < count; index += 1) {
    const offset = 2 / count;
    const y = index * offset - 1 + offset / 2;
    const r = Math.sqrt(1 - y * y);
    const phi = index * Math.PI * (3 - Math.sqrt(5));
    slots.push([
      Math.cos(phi) * r * radius,
      y * radius,
      Math.sin(phi) * r * radius,
    ]);
  }

  return slots;
}

export function createLoanPool(total = 220) {
  const random = mulberry32(1087);
  const loans: LoanRecord[] = [];

  for (let index = 0; index < total; index += 1) {
    const clusterBias = index % 9 === 0 || index % 13 === 0;
    const amount = Math.round((180000 + random() * 720000) / 1000) * 1000;
    const fico = Math.round(560 + random() * 210);
    const ltv = Math.round(58 + random() * 39);
    const occupancy = clusterBias && random() > 0.4 ? 'Investment' : pick(occupancies, random);
    const employer = clusterBias ? 'Blue Arch Holdings' : pick(employers, random);
    const officerName = clusterBias && random() > 0.25 ? 'Jordan Hale' : pick(officers, random);
    const county = clusterBias && random() > 0.35 ? 'Broward County' : pick(counties, random);
    const channel = clusterBias ? 'Broker' : pick(channels, random);

    const score =
      (clusterBias ? 0.38 : 0.12) +
      (occupancy === 'Investment' ? 0.14 : 0.03) +
      (fico < 620 ? 0.14 : fico < 680 ? 0.07 : 0.02) +
      (ltv > 90 ? 0.18 : ltv > 82 ? 0.08 : 0.03) +
      (channel === 'Broker' ? 0.08 : 0.02) +
      (employer === 'Blue Arch Holdings' ? 0.14 : 0.02) +
      random() * 0.2;

    const matchScore = clamp(score, 0.04, 0.98);
    const actualFraud =
      matchScore > 0.76 ? random() > 0.12 : matchScore > 0.64 ? random() > 0.55 : false;

    loans.push({
      id: `LN-${String(4200 + index).padStart(5, '0')}`,
      borrowerName: pick(borrowers, random),
      officerName,
      amount,
      county,
      fico,
      ltv,
      channel,
      employer,
      occupancy,
      tone: actualFraud ? 'risk' : matchScore < 0.28 ? 'clean' : 'neutral',
      actualFraud,
      matchScore,
      atlasIndex: index % 64,
    });
  }

  return loans.sort((left, right) => right.matchScore - left.matchScore);
}

export function chooseCaughtNotes(loans: LoanRecord[], existingIds: Set<string>) {
  const freshLoans = loans.filter((loan) => !existingIds.has(loan.id));
  const clearlyShady = freshLoans.filter(
    (loan) => loan.actualFraud || loan.matchScore > 0.76,
  );
  const nearMatches = freshLoans.filter(
    (loan) => !clearlyShady.includes(loan) && loan.matchScore > 0.64,
  );
  const candidates = [...clearlyShady.slice(0, 18), ...nearMatches.slice(0, 6)];
  const slots = createAttachmentSlots(candidates.length);

  return candidates.map<CaughtNote>((loan, index) => ({
    loanId: loan.id,
    reviewStatus: loan.actualFraud ? 'fraud' : 'falsePositive',
    attachedAt: performance.now(),
    slot: slots[index],
  }));
}

export function updateReviewStatus(
  notes: CaughtNote[],
  loanId: string,
  status: ReviewStatus,
) {
  return notes.map((note) =>
    note.loanId === loanId
      ? {
          ...note,
          reviewStatus: status,
        }
      : note,
  );
}

export function estimateSavings(loans: LoanRecord[], caughtNotes: CaughtNote[]) {
  const loanMap = new Map(loans.map((loan) => [loan.id, loan]));
  return caughtNotes.reduce((total, note) => {
    if (note.reviewStatus !== 'fraud') {
      return total;
    }

    const amount = loanMap.get(note.loanId)?.amount ?? 0;
    return total + amount * 0.11;
  }, 0);
}

export function buildLoanAtlas(loans: LoanRecord[]) {
  const cols = 8;
  const rows = 8;
  const cell = 256;
  const canvas = document.createElement('canvas');
  canvas.width = cols * cell;
  canvas.height = rows * cell;
  const context = canvas.getContext('2d');

  if (!context) {
    throw new Error('Canvas 2D context not available');
  }

  context.fillStyle = '#f8fbff';
  context.fillRect(0, 0, canvas.width, canvas.height);

  loans.slice(0, cols * rows).forEach((loan, index) => {
    const col = index % cols;
    const row = Math.floor(index / cols);
    const x = col * cell;
    const y = row * cell;
    const tone = loan.tone === 'risk' ? '#ffd2b0' : loan.tone === 'clean' ? '#eefcf6' : '#fff6b8';
    const fold = loan.tone === 'risk' ? '#ffc197' : loan.tone === 'clean' ? '#def3ea' : '#f4df7d';

    context.fillStyle = tone;
    context.fillRect(x + 10, y + 10, cell - 20, cell - 20);
    context.strokeStyle = 'rgba(18, 39, 57, 0.18)';
    context.lineWidth = 3;
    context.strokeRect(x + 10, y + 10, cell - 20, cell - 20);

    context.fillStyle = fold;
    context.beginPath();
    context.moveTo(x + cell - 54, y + 10);
    context.lineTo(x + cell - 10, y + 10);
    context.lineTo(x + cell - 10, y + 54);
    context.closePath();
    context.fill();

    context.fillStyle = '#0d2333';
    context.font = 'bold 22px "IBM Plex Sans"';
    context.fillText(loan.id, x + 22, y + 40);
    context.font = '15px "IBM Plex Sans"';
    context.fillStyle = '#183042';
    context.fillText(`Officer: ${loan.officerName}`, x + 22, y + 74);
    context.fillText(`Borrower: ${loan.borrowerName}`, x + 22, y + 102);
    context.fillText(`Amount: $${Math.round(loan.amount / 1000)}k`, x + 22, y + 130);
    context.fillText(`County: ${loan.county.replace(' County', '')}`, x + 22, y + 158);
    context.fillText(`FICO ${loan.fico}  |  LTV ${loan.ltv}%`, x + 22, y + 186);
    context.fillText(loan.channel.toUpperCase(), x + 22, y + 214);
    context.strokeStyle = 'rgba(13, 35, 51, 0.12)';
    context.beginPath();
    context.moveTo(x + 22, y + 58);
    context.lineTo(x + cell - 22, y + 58);
    context.stroke();

    context.fillStyle = 'rgba(13, 35, 51, 0.6)';
    context.beginPath();
    context.arc(x + 128, y + 18, 4.5, 0, Math.PI * 2);
    context.fill();
  });

  const texture = new THREE.CanvasTexture(canvas);
  texture.anisotropy = 8;
  texture.colorSpace = THREE.SRGBColorSpace;
  texture.needsUpdate = true;

  return { texture, cols, rows };
}
