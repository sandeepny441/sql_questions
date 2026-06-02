const palette = {
  series: {
    control: {
      before: "#8cb5ff",
      during: "#244cff",
      label: "#244cff",
    },
    treatment: {
      before: "#f3a1aa",
      during: "#d94a57",
      label: "#b4313f",
    },
    unassigned: {
      before: "#c7d1df",
      during: "#4e607d",
      label: "#4e607d",
    },
  },
  ink: "#0d1526",
  muted: "#6f7788",
  line: "#e8ebf0",
  grid: "#edf0f4",
  neutral: "#bbc3cf",
  positive: "#22a55b",
  negative: "#d94a57",
};

const slides = [
  {
    metric: "Imports",
    chartType: "mirror-bars",
    beforeLabel: "Before Pilot",
    beforeDates: "Mar 27 - Apr 19",
    duringLabel: "During Pilot",
    duringDates: "Apr 20 - May 13",
    days: "24 days",
    rows: [
      { label: "Control", className: "control", before: 409, during: 423, deltaPct: 3 },
      { label: "Treatment", className: "treatment", before: 179, during: 161, deltaPct: -10 },
      { label: "Unassigned", className: "unassigned", before: 288, during: 321, deltaPct: 11 },
    ],
    insights: [
      {
        tone: "neutral",
        html:
          "<strong>Treatment is the only group down at the top of funnel.</strong> Control rose from 409 to 423 and Unassigned rose from 288 to 321, while Treatment fell from 179 to 161.",
      },
      {
        tone: "control",
        html:
          "<strong>Control: +3%</strong> from 409 to 423 imports. The baseline market was stable to slightly up entering the pilot period.",
      },
      {
        tone: "treatment",
        html:
          "<strong>Treatment: -10%</strong> from 179 to 161 imports. That early drop suggests loan officers were importing fewer loans they expected to price competitively.",
      },
      {
        tone: "unassigned",
        html:
          "<strong>Unassigned: +11%</strong> from 288 to 321 imports. Since the residual population also grew, the Treatment weakness looks behavioral rather than seasonal.",
      },
    ],
  },
  {
    metric: "Submissions",
    chartType: "mirror-bars",
    beforeLabel: "Before Pilot",
    beforeDates: "Mar 27 - Apr 19",
    duringLabel: "During Pilot",
    duringDates: "Apr 20 - May 13",
    days: "24 days",
    rows: [
      { label: "Control", className: "control", before: 185, during: 199, deltaPct: 8 },
      { label: "Treatment", className: "treatment", before: 96, during: 72, deltaPct: -25 },
      { label: "Unassigned", className: "unassigned", before: 124, during: 138, deltaPct: 11 },
    ],
    insights: [
      {
        tone: "neutral",
        html:
          "<strong>Treatment is the only group moving backward.</strong> Control grew from 185 to 199 and Unassigned grew from 124 to 138, while Treatment fell from 96 to 72 in the same matched 24-day window.",
      },
      {
        tone: "control",
        html:
          "<strong>Control: +8%</strong> from 185 to 199 submissions. That reads like normal market momentum rather than any drag from the pilot period.",
      },
      {
        tone: "treatment",
        html:
          "<strong>Treatment: -25%</strong> from 96 to 72 submissions. This is the sharpest deterioration across the four core production metrics.",
      },
      {
        tone: "unassigned",
        html:
          "<strong>Unassigned: +11%</strong> from 124 to 138 submissions. Broader growth makes the Treatment drop harder to dismiss as noise.",
      },
    ],
  },
  {
    metric: "Locks",
    chartType: "dumbbell",
    beforeLabel: "Before Pilot",
    beforeDates: "Mar 27 - Apr 19",
    duringLabel: "During Pilot",
    duringDates: "Apr 20 - May 13",
    days: "24 days",
    rows: [
      { label: "Control", className: "control", before: 209, during: 256, deltaPct: 22 },
      { label: "Treatment", className: "treatment", before: 89, during: 100, deltaPct: 12 },
      { label: "Unassigned", className: "unassigned", before: 174, during: 211, deltaPct: 21 },
    ],
    insights: [
      {
        tone: "neutral",
        html:
          "<strong>Lock volume grew everywhere, but Treatment lagged the market.</strong> Control and Unassigned both expanded above 21%, while Treatment rose only from 89 to 100.",
      },
      {
        tone: "control",
        html:
          "<strong>Control: +22%</strong> from 209 to 256 locks. The baseline market kept building downstream inventory during the pilot window.",
      },
      {
        tone: "treatment",
        html:
          "<strong>Treatment: +12%</strong> from 89 to 100 locks. Positive on the surface, but roughly half the Control growth rate, which points to weaker pull-through than the market benchmark.",
      },
      {
        tone: "unassigned",
        html:
          "<strong>Unassigned: +21%</strong> from 174 to 211 locks. This second benchmark reinforces that downstream demand was still healthy outside the pilot cohort.",
      },
    ],
  },
  {
    metric: "Wires",
    chartType: "slope",
    beforeLabel: "Before Pilot",
    beforeDates: "Mar 27 - Apr 19",
    duringLabel: "During Pilot",
    duringDates: "Apr 20 - May 13",
    days: "24 days",
    rows: [
      { label: "Control", className: "control", before: 171, during: 174, deltaPct: 2 },
      { label: "Treatment", className: "treatment", before: 77, during: 69, deltaPct: -10 },
      { label: "Unassigned", className: "unassigned", before: 108, during: 120, deltaPct: 11 },
    ],
    insights: [
      {
        tone: "neutral",
        html:
          "<strong>By the closing stage, Treatment is again the only group down.</strong> Control stayed essentially flat and Unassigned moved higher, while Treatment fell from 77 to 69 wires.",
      },
      {
        tone: "control",
        html:
          "<strong>Control: +2%</strong> from 171 to 174 wires. Closings held steady, which is what you would expect from loans already in process before the pilot.",
      },
      {
        tone: "treatment",
        html:
          "<strong>Treatment: -10%</strong> from 77 to 69 wires. The decline is smaller than Submissions because wires lag earlier funnel changes, but the direction still confirms weaker production flow.",
      },
      {
        tone: "unassigned",
        html:
          "<strong>Unassigned: +11%</strong> from 108 to 120 wires. Market-wide closing growth makes the Treatment decline more notable, not less.",
      },
    ],
  },
];

let currentSlideIndex = 0;

function tonesFor(className) {
  return palette.series[className];
}

function number(value) {
  return new Intl.NumberFormat("en-US").format(value);
}

function deltaText(value) {
  return `${value >= 0 ? "+" : ""}${value}%`;
}

function renderPeriodHeader(slide) {
  return `
    <div class="chart-top">
      <div class="period-pair">
        <div class="period-header">
          <span class="period-title before">${slide.beforeLabel}</span>
          <span class="period-dates">${slide.beforeDates}</span>
          <span class="period-days">${slide.days}</span>
        </div>
        <div class="period-header">
          <span class="period-title during">${slide.duringLabel}</span>
          <span class="period-dates">${slide.duringDates}</span>
          <span class="period-days">${slide.days}</span>
        </div>
      </div>
    </div>
  `;
}

function renderMirrorRows(slide) {
  const maxValue = Math.max(...slide.rows.flatMap((row) => [row.before, row.during]));

  return `
    <div class="rows">
      ${slide.rows
        .map((row) => {
          const tones = tonesFor(row.className);
          const beforeWidth = (row.before / maxValue) * 100;
          const duringWidth = (row.during / maxValue) * 100;
          const deltaClass = row.deltaPct >= 0 ? "positive" : "negative";

          return `
            <div class="row">
              <div class="metric-value">${number(row.before)}</div>
              <div class="bars" aria-label="${row.label} ${slide.metric.toLowerCase()} comparison">
                <div class="bars-label ${row.className}">${row.label}</div>
                <div class="bars-track">
                  <div class="half before">
                    <div class="bar" style="width: ${beforeWidth}%; background: ${tones.before};"></div>
                  </div>
                  <div class="half during">
                    <div class="bar" style="width: ${duringWidth}%; background: ${tones.during};"></div>
                  </div>
                </div>
              </div>
              <div class="metric-during">${number(row.during)}</div>
              <div class="delta ${deltaClass}">${deltaText(row.deltaPct)}</div>
            </div>
          `;
        })
        .join("")}
    </div>
  `;
}

function renderGroupedBarsChart(slide) {
  const width = 920;
  const height = 520;
  const baseline = 404;
  const barMaxHeight = 238;
  const maxValue = Math.max(...slide.rows.flatMap((row) => [row.before, row.during]));
  const centers = [182, 460, 738];
  const barWidth = 82;
  const gap = 22;

  const gridLines = [0.25, 0.5, 0.75, 1]
    .map((fraction) => {
      const y = baseline - barMaxHeight * fraction;
      return `<line x1="56" y1="${y}" x2="864" y2="${y}" stroke="${palette.grid}" stroke-width="2" />`;
    })
    .join("");

  const groups = slide.rows
    .map((row, index) => {
      const tones = tonesFor(row.className);
      const center = centers[index];
      const beforeHeight = (row.before / maxValue) * barMaxHeight;
      const duringHeight = (row.during / maxValue) * barMaxHeight;
      const beforeX = center - gap / 2 - barWidth;
      const duringX = center + gap / 2;
      const beforeY = baseline - beforeHeight;
      const duringY = baseline - duringHeight;

      return `
        <text x="${beforeX + barWidth / 2}" y="${beforeY - 16}" text-anchor="middle" fill="${palette.ink}" font-size="22" font-weight="800">${number(row.before)}</text>
        <rect x="${beforeX}" y="${beforeY}" width="${barWidth}" height="${beforeHeight}" rx="12" fill="${tones.before}" />
        <text x="${duringX + barWidth / 2}" y="${duringY - 16}" text-anchor="middle" fill="${palette.ink}" font-size="22" font-weight="800">${number(row.during)}</text>
        <rect x="${duringX}" y="${duringY}" width="${barWidth}" height="${duringHeight}" rx="12" fill="${tones.during}" />
        <text x="${center}" y="${baseline + 48}" text-anchor="middle" fill="${tones.label}" font-size="24" font-weight="800">${row.label}</text>
        <text x="${center}" y="${baseline + 82}" text-anchor="middle" fill="${row.deltaPct >= 0 ? palette.positive : palette.negative}" font-size="22" font-weight="800">${deltaText(row.deltaPct)}</text>
      `;
    })
    .join("");

  return `
    <svg class="chart-svg" viewBox="0 0 ${width} ${height}" aria-label="${slide.metric} grouped bar chart">
      ${gridLines}
      <line x1="56" y1="${baseline}" x2="864" y2="${baseline}" stroke="${palette.line}" stroke-width="2" />
      ${groups}
    </svg>
  `;
}

function renderDumbbellChart(slide) {
  const width = 920;
  const height = 520;
  const yPositions = [126, 264, 402];
  const plotStart = 116;
  const plotEnd = 804;
  const allValues = slide.rows.flatMap((row) => [row.before, row.during]);
  const minValue = Math.min(...allValues);
  const maxValue = Math.max(...allValues);
  const domainMin = Math.max(0, minValue - (maxValue - minValue) * 0.2);
  const domainMax = maxValue + (maxValue - minValue) * 0.1;
  const scale = (value) =>
    plotStart + ((value - domainMin) / (domainMax - domainMin)) * (plotEnd - plotStart);

  const guides = [0, 0.25, 0.5, 0.75, 1]
    .map((fraction) => {
      const x = plotStart + (plotEnd - plotStart) * fraction;
      return `<line x1="${x}" y1="70" x2="${x}" y2="450" stroke="${palette.grid}" stroke-width="2" />`;
    })
    .join("");

  const rows = slide.rows
    .map((row, index) => {
      const tones = tonesFor(row.className);
      const y = yPositions[index];
      const beforeX = scale(row.before);
      const duringX = scale(row.during);
      const labelsTight = Math.abs(duringX - beforeX) < 60;
      const beforeLabel = labelsTight
        ? `<text x="${beforeX - 12}" y="${y - 26}" text-anchor="end" fill="${palette.ink}" font-size="19" font-weight="800">${number(row.before)}</text>`
        : `<text x="${beforeX}" y="${y - 26}" text-anchor="middle" fill="${palette.ink}" font-size="19" font-weight="800">${number(row.before)}</text>`;
      const duringLabel = labelsTight
        ? `<text x="${duringX + 12}" y="${y - 26}" text-anchor="start" fill="${palette.ink}" font-size="19" font-weight="800">${number(row.during)}</text>`
        : `<text x="${duringX}" y="${y - 26}" text-anchor="middle" fill="${palette.ink}" font-size="19" font-weight="800">${number(row.during)}</text>`;
      const labelX = (beforeX + duringX) / 2;
      return `
        <text x="${labelX}" y="${y - 52}" text-anchor="middle" fill="${tones.label}" font-size="21" font-weight="800">${row.label}</text>
        <line x1="${plotStart}" y1="${y}" x2="${plotEnd}" y2="${y}" stroke="${palette.line}" stroke-width="6" stroke-linecap="round" />
        <line x1="${beforeX}" y1="${y}" x2="${duringX}" y2="${y}" stroke="${tones.during}" stroke-width="8" stroke-linecap="round" />
        <circle cx="${beforeX}" cy="${y}" r="14" fill="${tones.before}" stroke="#ffffff" stroke-width="4" />
        <circle cx="${duringX}" cy="${y}" r="14" fill="${tones.during}" stroke="#ffffff" stroke-width="4" />
        ${beforeLabel}
        ${duringLabel}
        <text x="884" y="${y + 8}" text-anchor="end" fill="${row.deltaPct >= 0 ? palette.positive : palette.negative}" font-size="22" font-weight="800">${deltaText(row.deltaPct)}</text>
      `;
    })
    .join("");

  return `
    <svg class="chart-svg" viewBox="0 0 ${width} ${height}" aria-label="${slide.metric} dumbbell comparison chart">
      ${guides}
      ${rows}
    </svg>
  `;
}

function renderSlopeChart(slide) {
  const width = 920;
  const height = 520;
  const xBefore = 176;
  const xDuring = 774;
  const top = 88;
  const bottom = 430;
  const allValues = slide.rows.flatMap((row) => [row.before, row.during]);
  const minValue = Math.min(...allValues);
  const maxValue = Math.max(...allValues);
  const domainMin = Math.max(0, minValue - 14);
  const domainMax = maxValue + 14;
  const scaleY = (value) => bottom - ((value - domainMin) / (domainMax - domainMin)) * (bottom - top);

  const guides = [0, 0.25, 0.5, 0.75, 1]
    .map((fraction) => {
      const y = top + (bottom - top) * fraction;
      return `<line x1="112" y1="${y}" x2="806" y2="${y}" stroke="${palette.grid}" stroke-width="2" />`;
    })
    .join("");

  const columns = `
    <text x="${xBefore}" y="${top - 40}" text-anchor="middle" fill="${palette.muted}" font-size="18" font-weight="800">Before Pilot</text>
    <text x="${xDuring}" y="${top - 40}" text-anchor="middle" fill="${palette.muted}" font-size="18" font-weight="800">During Pilot</text>
    <line x1="${xBefore}" y1="${top - 22}" x2="${xBefore}" y2="${bottom + 26}" stroke="${palette.line}" stroke-width="3" />
    <line x1="${xDuring}" y1="${top - 22}" x2="${xDuring}" y2="${bottom + 26}" stroke="${palette.line}" stroke-width="3" />
  `;

  const series = slide.rows
    .map((row) => {
      const tones = tonesFor(row.className);
      const beforeY = scaleY(row.before);
      const duringY = scaleY(row.during);
      const labelX = (xBefore + xDuring) / 2;
      const labelY = Math.min(beforeY, duringY) - 28;
      return `
        <line x1="${xBefore}" y1="${beforeY}" x2="${xDuring}" y2="${duringY}" stroke="${tones.during}" stroke-width="8" stroke-linecap="round" />
        <circle cx="${xBefore}" cy="${beforeY}" r="12" fill="${tones.before}" stroke="#ffffff" stroke-width="4" />
        <circle cx="${xDuring}" cy="${duringY}" r="12" fill="${tones.during}" stroke="#ffffff" stroke-width="4" />
        <text x="${labelX}" y="${labelY}" text-anchor="middle" fill="${tones.label}" font-size="19" font-weight="800">${row.label}</text>
        <text x="${xBefore - 24}" y="${beforeY + 18}" text-anchor="end" fill="${palette.ink}" font-size="18" font-weight="800">${number(row.before)}</text>
        <text x="${xDuring + 20}" y="${duringY + 4}" text-anchor="start" fill="${palette.ink}" font-size="19" font-weight="800">${number(row.during)}</text>
        <text x="882" y="${duringY + 4}" text-anchor="end" fill="${row.deltaPct >= 0 ? palette.positive : palette.negative}" font-size="19" font-weight="800">${deltaText(row.deltaPct)}</text>
      `;
    })
    .join("");

  return `
    <svg class="chart-svg" viewBox="0 0 ${width} ${height}" aria-label="${slide.metric} slope comparison chart">
      ${guides}
      ${columns}
      ${series}
    </svg>
  `;
}

function renderChart(slide) {
  switch (slide.chartType) {
    case "grouped-bars":
      return renderGroupedBarsChart(slide);
    case "mirror-bars":
      return renderMirrorRows(slide);
    case "dumbbell":
      return renderDumbbellChart(slide);
    case "slope":
      return renderSlopeChart(slide);
    default:
      return renderMirrorRows(slide);
  }
}

function renderInsights(insights) {
  return insights
    .map(
      (insight) => `
        <div class="insight">
          <div class="insight-line ${insight.tone}"></div>
          <p class="insight-copy">${insight.html}</p>
        </div>
      `,
    )
    .join("");
}

function renderProgress() {
  const root = document.getElementById("deck-progress");
  root.innerHTML = slides
    .map(
      (_, index) =>
        `<span class="progress-dot${index === currentSlideIndex ? " active" : ""}"></span>`,
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
  const root = document.getElementById("slide-root");

  root.innerHTML = `
    <section class="slide-layout">
      <div class="slide-main">
        <h1 class="slide-title">${slide.metric}</h1>
        <div class="chart-stage">
          ${renderPeriodHeader(slide)}
          <div class="chart-view chart-view-${slide.chartType}">
            ${renderChart(slide)}
          </div>
        </div>
      </div>

      <aside class="slide-aside">
        <p class="aside-label">Key Insights</p>
        <div class="insights">
          ${renderInsights(slide.insights)}
        </div>
      </aside>
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
