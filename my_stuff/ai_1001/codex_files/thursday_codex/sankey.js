const palette = {
  control: {
    accent: "#244cff",
    soft: "rgba(36, 76, 255, 0.18)",
    strongSoft: "rgba(36, 76, 255, 0.28)",
  },
  treatment: {
    accent: "#d94a57",
    soft: "rgba(217, 74, 87, 0.18)",
    strongSoft: "rgba(217, 74, 87, 0.3)",
  },
  unassigned: {
    accent: "#4e607d",
    soft: "rgba(78, 96, 125, 0.18)",
    strongSoft: "rgba(78, 96, 125, 0.28)",
  },
  total: {
    accent: "#6f54d8",
    soft: "rgba(111, 84, 216, 0.18)",
    strongSoft: "rgba(111, 84, 216, 0.28)",
  },
  sink: "rgba(117, 127, 147, 0.16)",
  sinkStroke: "rgba(117, 127, 147, 0.26)",
  support: "#d7a643",
  supportSoft: "rgba(215, 166, 67, 0.18)",
  ink: "#10192b",
  muted: "#6f7788",
  line: "rgba(16, 25, 43, 0.08)",
  success: "#17864d",
  danger: "#c53f4c",
};

const periodMeta = {
  before: {
    title: "Before Pilot",
    dates: "Mar 27 - Apr 19, 2026",
  },
  during: {
    title: "During Pilot",
    dates: "Apr 20 - May 13, 2026",
  },
};

const cohorts = {
  total: {
    key: "total",
    label: "Total Market",
    accentClass: "accent-total",
    tone: "total",
    before: { imports: 876, submissions: 405, locks: 472, wires: 356 },
    during: { imports: 905, submissions: 409, locks: 567, wires: 363 },
    summary:
      "The market imported a bit more volume during the pilot, but downstream output did not keep up. The biggest visual change is how much more lock volume depended on carryover pipeline rather than same-window submissions.",
  },
  control: {
    key: "control",
    label: "Control",
    accentClass: "accent-control",
    tone: "control",
    before: { imports: 409, submissions: 185, locks: 209, wires: 171 },
    during: { imports: 423, submissions: 199, locks: 256, wires: 174 },
    summary:
      "Control stays closest to a healthy baseline. Imports and submissions edge up, while a larger carryover branch at locks shows the market kept feeding inventory forward into closing stages.",
  },
  treatment: {
    key: "treatment",
    label: "Treatment",
    accentClass: "accent-treatment",
    tone: "treatment",
    before: { imports: 179, submissions: 96, locks: 89, wires: 77 },
    during: { imports: 161, submissions: 72, locks: 100, wires: 69 },
    summary:
      "Treatment is the only cohort where the top of funnel visibly narrows. Imports, submissions, and wires all shrink, and the lock stage leans more on carryover instead of fresh same-window submission flow.",
  },
  unassigned: {
    key: "unassigned",
    label: "Unassigned",
    accentClass: "accent-unassigned",
    tone: "unassigned",
    before: { imports: 288, submissions: 124, locks: 174, wires: 108 },
    during: { imports: 321, submissions: 138, locks: 211, wires: 120 },
    summary:
      "Unassigned behaves like the broader market expansion case. Volume rises at every major touchpoint, and the carryover branch grows, which reinforces that Treatment weakness is not just a seasonal slowdown.",
  },
};

const slides = ["total", "control", "treatment", "unassigned"].map((key) => {
  const cohort = cohorts[key];
  return {
    ...cohort,
    chips: buildSummaryChips(cohort),
    insightNote: buildInsightNote(cohort),
    cards: ["before", "during"].map((period) => ({
      period,
      title: periodMeta[period].title,
      dates: periodMeta[period].dates,
      data: cohort[period],
      flow: buildFlow(cohort[period]),
    })),
  };
});

let currentSlideIndex = 0;

function number(value) {
  return new Intl.NumberFormat("en-US").format(value);
}

function pct(value) {
  return `${Math.round(value * 100)}%`;
}

function signedPctFromCounts(before, during) {
  const delta = ((during - before) / before) * 100;
  const rounded = Math.round(delta);
  return `${rounded >= 0 ? "+" : ""}${rounded}%`;
}

function buildFlow(data) {
  const imports = data.imports;
  const submissions = data.submissions;
  const locks = data.locks;
  const wires = data.wires;
  const lockedFromSubmissions = Math.min(submissions, locks);
  const wiresFromLocks = Math.min(locks, wires);
  const carryover = Math.max(locks - submissions, 0);
  const noSubmission = Math.max(imports - submissions, 0);
  const noLock = Math.max(submissions - locks, 0);
  const noWire = Math.max(locks - wires, 0);
  const earlierLocksToWires = Math.max(wires - locks, 0);

  return {
    imports,
    submissions,
    locks,
    wires,
    lockedFromSubmissions,
    wiresFromLocks,
    carryover,
    noSubmission,
    noLock,
    noWire,
    earlierLocksToWires,
  };
}

function buildSummaryChips(cohort) {
  return [
    {
      label: "Imports",
      value: `${number(cohort.before.imports)} -> ${number(cohort.during.imports)}`,
      tone: diffTone(cohort.before.imports, cohort.during.imports),
    },
    {
      label: "Submissions",
      value: `${number(cohort.before.submissions)} -> ${number(cohort.during.submissions)}`,
      tone: diffTone(cohort.before.submissions, cohort.during.submissions),
    },
    {
      label: "Locks",
      value: `${number(cohort.before.locks)} -> ${number(cohort.during.locks)}`,
      tone: diffTone(cohort.before.locks, cohort.during.locks),
    },
    {
      label: "Wires",
      value: `${number(cohort.before.wires)} -> ${number(cohort.during.wires)}`,
      tone: diffTone(cohort.before.wires, cohort.during.wires),
    },
  ];
}

function buildInsightNote(cohort) {
  const beforeSubmitRate = cohort.before.submissions / cohort.before.imports;
  const duringSubmitRate = cohort.during.submissions / cohort.during.imports;
  const beforeCarryoverShare = Math.max(cohort.before.locks - cohort.before.submissions, 0) / cohort.before.locks;
  const duringCarryoverShare = Math.max(cohort.during.locks - cohort.during.submissions, 0) / cohort.during.locks;

  return `
    Submission conversion moved from <strong>${pct(beforeSubmitRate)}</strong> to <strong>${pct(duringSubmitRate)}</strong>,
    while the share of locks coming from carryover pipeline changed from
    <strong>${pct(beforeCarryoverShare)}</strong> to <strong>${pct(duringCarryoverShare)}</strong>.
  `;
}

function diffTone(before, after) {
  if (after > before) return "positive";
  if (after < before) return "negative";
  return "";
}

function buildChartKpis(data, flow) {
  return [
    { label: "Import to Submit", value: pct(flow.submissions / flow.imports) },
    { label: "Submit to Lock", value: pct(flow.lockedFromSubmissions / flow.submissions) },
    { label: "Lock to Wire", value: pct(flow.wiresFromLocks / flow.locks) },
    { label: "Carryover in Locks", value: pct(flow.carryover / flow.locks) },
  ];
}

function buildCardNarrative(period, flow) {
  const carryoverText =
    flow.carryover > 0
      ? `${number(flow.carryover)} locks arrive from earlier pipeline.`
      : "Locks are fully supported by same-window submissions.";
  return `
    ${periodMeta[period].title} shows <strong>${number(flow.imports)}</strong> imports feeding
    <strong>${number(flow.submissions)}</strong> submissions, <strong>${number(flow.locks)}</strong> locks,
    and <strong>${number(flow.wires)}</strong> wires. ${carryoverText}
  `;
}

function renderSvgText(text, x, y, options = {}) {
  const {
    size = 12,
    weight = 700,
    fill = palette.ink,
    anchor = "start",
    letterSpacing = "0em",
  } = options;

  return `<text x="${x}" y="${y}" fill="${fill}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" letter-spacing="${letterSpacing}">${text}</text>`;
}

function nodeDefinitions(flow) {
  const defs = [
    { id: "imports", label: "Imports", kind: "main", lane: "source", value: flow.imports },
    { id: "noSubmission", label: "No submission", kind: "sink", lane: "top", value: flow.noSubmission },
    { id: "submitted", label: "Submitted", kind: "main", lane: "main", value: flow.submissions },
    { id: "carryover", label: "Carryover pipeline", kind: "support", lane: "support", value: flow.carryover },
    { id: "noLock", label: "Held pre-lock", kind: "sink", lane: "top", value: flow.noLock },
    { id: "locks", label: "Locks", kind: "main", lane: "main", value: flow.locks },
    { id: "earlierLocks", label: "Earlier locks", kind: "support", lane: "support", value: flow.earlierLocksToWires },
    { id: "noWire", label: "Still in pipeline", kind: "sink", lane: "top", value: flow.noWire },
    { id: "wires", label: "Wires", kind: "main", lane: "main", value: flow.wires },
  ];

  return defs.filter((node) => node.value > 0 || ["imports", "submitted", "locks", "wires"].includes(node.id));
}

function renderSankeySvg(flow, tone, sharedMax) {
  const width = 640;
  const height = 360;
  const nodeWidth = 24;
  const maxNodeValue = sharedMax;
  const scale = 176 / maxNodeValue;
  const centers = {
    source: 182,
    main: 250,
    top: 86,
    support: 150,
  };
  const xMap = {
    imports: 56,
    noSubmission: 214,
    submitted: 214,
    carryover: 214,
    noLock: 378,
    locks: 378,
    earlierLocks: 378,
    noWire: 540,
    wires: 540,
  };
  const colors = palette[tone];
  const nodes = nodeDefinitions(flow).map((node) => {
    const heightPx = Math.max(node.value * scale, node.kind === "main" ? 22 : node.value > 0 ? 18 : 0);
    const centerY = centers[node.lane];
    return {
      ...node,
      x: xMap[node.id],
      y: centerY - heightPx / 2,
      width: nodeWidth,
      height: heightPx,
      incomingCursor: 0,
      outgoingCursor: 0,
    };
  });
  const nodeMap = Object.fromEntries(nodes.map((node) => [node.id, node]));
  const links = [
    { source: "imports", target: "noSubmission", value: flow.noSubmission, kind: "sink" },
    { source: "imports", target: "submitted", value: flow.submissions, kind: "primary" },
    { source: "submitted", target: "noLock", value: flow.noLock, kind: "sink" },
    { source: "submitted", target: "locks", value: flow.lockedFromSubmissions, kind: "primary" },
    { source: "carryover", target: "locks", value: flow.carryover, kind: "support" },
    { source: "earlierLocks", target: "wires", value: flow.earlierLocksToWires, kind: "support" },
    { source: "locks", target: "noWire", value: flow.noWire, kind: "sink" },
    { source: "locks", target: "wires", value: flow.wiresFromLocks, kind: "primary" },
  ].filter((link) => link.value > 0 && nodeMap[link.source] && nodeMap[link.target]);

  const pathMarkup = links
    .map((link) => {
      const source = nodeMap[link.source];
      const target = nodeMap[link.target];
      const thickness = Math.max(link.value * scale, 8);
      const sourceTop = source.y + source.outgoingCursor;
      const sourceBottom = sourceTop + thickness;
      source.outgoingCursor += thickness;
      const targetTop = target.y + target.incomingCursor;
      const targetBottom = targetTop + thickness;
      target.incomingCursor += thickness;
      const x0 = source.x + source.width;
      const x1 = target.x;
      const curve = Math.max((x1 - x0) * 0.44, 34);
      const fill =
        link.kind === "primary"
          ? colors.strongSoft
          : link.kind === "support"
            ? palette.supportSoft
            : palette.sink;
      const stroke =
        link.kind === "primary"
          ? colors.soft
          : link.kind === "support"
            ? "rgba(215, 166, 67, 0.24)"
            : palette.sinkStroke;
      const d = [
        `M ${x0} ${sourceTop}`,
        `C ${x0 + curve} ${sourceTop}, ${x1 - curve} ${targetTop}, ${x1} ${targetTop}`,
        `L ${x1} ${targetBottom}`,
        `C ${x1 - curve} ${targetBottom}, ${x0 + curve} ${sourceBottom}, ${x0} ${sourceBottom}`,
        "Z",
      ].join(" ");
      return `<path d="${d}" fill="${fill}" stroke="${stroke}" stroke-width="1" />`;
    })
    .join("");

  const gridMarkup = [138, 302, 466]
    .map(
      (x) =>
        `<line x1="${x}" y1="26" x2="${x}" y2="${height - 26}" stroke="${palette.line}" stroke-width="1.2" stroke-dasharray="4 7" />`,
    )
    .join("");

  const stageLabels = [
    renderSvgText("Imports", 68, 26, { size: 12, fill: palette.muted, letterSpacing: "0.08em" }),
    renderSvgText("Submissions", 226, 26, { size: 12, fill: palette.muted, letterSpacing: "0.08em" }),
    renderSvgText("Locks", 390, 26, { size: 12, fill: palette.muted, letterSpacing: "0.08em" }),
    renderSvgText("Wires", 552, 26, { size: 12, fill: palette.muted, letterSpacing: "0.08em" }),
  ].join("");

  const nodeMarkup = nodes
    .map((node) => {
      const fill =
        node.kind === "main"
          ? colors.soft
          : node.kind === "support"
            ? palette.supportSoft
            : palette.sink;
      const stroke =
        node.kind === "main"
          ? colors.accent
          : node.kind === "support"
            ? palette.support
            : palette.sinkStroke;
      const labelX = node.x + node.width / 2;
      const labelY = node.y - 12;
      const valueY = node.y + node.height + 18;
      const align = node.id === "imports" ? "start" : "middle";
      const textX = node.id === "imports" ? node.x - 2 : labelX;

      return `
        <rect x="${node.x}" y="${node.y}" width="${node.width}" height="${node.height}" rx="12" fill="${fill}" stroke="${stroke}" stroke-width="1.4" />
        ${renderSvgText(node.label, textX, labelY, {
          size: 12,
          fill: node.kind === "main" ? stroke : palette.muted,
          anchor: align,
          letterSpacing: "0.02em",
        })}
        ${renderSvgText(number(node.value), textX, valueY, {
          size: 14,
          fill: palette.ink,
          weight: 800,
          anchor: align,
        })}
      `;
    })
    .join("");

  return `
    <svg class="sankey-svg" viewBox="0 0 ${width} ${height}" aria-label="Sankey chart">
      ${gridMarkup}
      ${stageLabels}
      ${pathMarkup}
      ${nodeMarkup}
    </svg>
  `;
}

function renderChartCard(slide, card) {
  const sharedMax = Math.max(
    ...slide.cards.flatMap((item) => [item.data.imports, item.data.submissions, item.data.locks, item.data.wires]),
  );
  const flow = card.flow;
  const kpis = buildChartKpis(card.data, flow);

  return `
    <article class="chart-card">
      <div class="chart-topline">
        <h2 class="chart-title">${card.title}</h2>
        <span class="chart-dates">${card.dates}</span>
      </div>

      <div class="kpi-row">
        ${kpis
          .map(
            (kpi) => `
              <div class="kpi">
                <span class="kpi-label">${kpi.label}</span>
                <span class="kpi-value">${kpi.value}</span>
              </div>
            `,
          )
          .join("")}
      </div>

      <div class="sankey-wrap">
        ${renderSankeySvg(flow, slide.tone, sharedMax)}
      </div>

      <p class="chart-caption">${buildCardNarrative(card.period, flow)}</p>
    </article>
  `;
}

function renderProgress() {
  const root = document.getElementById("deck-progress");
  root.innerHTML = slides
    .map(
      (_, index) =>
        `<span class="progress-dot${index === currentSlideIndex ? " active" : ""}" aria-hidden="true"></span>`,
    )
    .join("");
}

function updateNav() {
  const prev = document.getElementById("prev-slide");
  const next = document.getElementById("next-slide");
  prev.disabled = currentSlideIndex === 0;
  next.disabled = currentSlideIndex === slides.length - 1;
}

function renderSlide() {
  const slide = slides[currentSlideIndex];
  const root = document.getElementById("sankey-root");
  const totalBefore = slide.before.imports + slide.before.submissions + slide.before.locks + slide.before.wires;
  const totalDuring = slide.during.imports + slide.during.submissions + slide.during.locks + slide.during.wires;
  const totalDelta = signedPctFromCounts(totalBefore, totalDuring);

  root.innerHTML = `
    <section class="slide">
      <header class="slide-header">
        <div>
          <p class="eyebrow">Pilot Funnel Sankeys</p>
          <h1 class="slide-title">${slide.label}</h1>
          <p class="slide-copy">
            ${slide.summary}
          </p>
        </div>

        <div class="summary-strip">
          ${slide.chips
            .map(
              (chip) => `
                <div class="summary-chip">
                  <span class="summary-chip-label">${chip.label}</span>
                  <span class="summary-chip-value ${chip.tone}">${chip.value}</span>
                </div>
              `,
            )
            .join("")}
        </div>
      </header>

      <div class="meta-row">
        <p class="meta-note">
          ${slide.insightNote}
          <br />
          <span class="${slide.accentClass}">Carryover pipeline</span> captures lock volume that likely originated before the observed 24-day submission window, which is why some lock stages exceed same-window submissions.
        </p>
        <div class="meta-pill">Before vs During total stage volume: ${totalDelta}</div>
      </div>

      <div class="chart-grid">
        ${slide.cards.map((card) => renderChartCard(slide, card)).join("")}
      </div>

      <p class="chart-caption">
        Source: <strong>AB_Test_Summary.xlsx</strong>, matched 24-day windows from Mar 27-Apr 19, 2026 and Apr 20-May 13, 2026.
      </p>
    </section>
  `;

  renderProgress();
  updateNav();
}

function changeSlide(direction) {
  const nextIndex = currentSlideIndex + direction;
  if (nextIndex < 0 || nextIndex >= slides.length) return;
  currentSlideIndex = nextIndex;
  renderSlide();
}

function boot() {
  document.getElementById("prev-slide").addEventListener("click", () => changeSlide(-1));
  document.getElementById("next-slide").addEventListener("click", () => changeSlide(1));
  document.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft") changeSlide(-1);
    if (event.key === "ArrowRight") changeSlide(1);
  });
  renderSlide();
}

window.addEventListener("DOMContentLoaded", boot);
