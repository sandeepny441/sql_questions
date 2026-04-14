<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Twin Pair Dashboard</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
  <style>
    :root {
      --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      --text-xs: 0.75rem;
      --text-sm: 0.8125rem;
      --text-base: 0.875rem;
      --text-lg: 1rem;
      --text-xl: 1.25rem;
      --text-2xl: 1.5rem;

      --space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px;
      --space-5: 20px; --space-6: 24px; --space-8: 32px;

      --bg: #f8f9fa;
      --surface: #ffffff;
      --border: #e5e7eb;
      --border-light: #f0f1f3;
      --text-primary: #111827;
      --text-secondary: #6b7280;
      --text-tertiary: #9ca3af;

      --green: #059669;
      --green-light: #ecfdf5;
      --blue: #2563eb;
      --blue-light: #eff6ff;
      --red: #dc2626;
      --red-light: #fef2f2;

      --radius-sm: 6px; --radius-md: 8px; --radius-lg: 12px;
      --shadow-sm: 0 1px 2px rgba(0,0,0,0.04);
      --shadow-md: 0 4px 16px rgba(0,0,0,0.08);
      --shadow-lg: 0 8px 30px rgba(0,0,0,0.12);
    }

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: var(--font-body);
      font-size: var(--text-base);
      color: var(--text-primary);
      background: var(--bg);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      min-height: 100vh;
    }

    .page {
      max-width: 1400px;
      margin: 0 auto;
      padding: var(--space-5) var(--space-6);
    }

    /* ───── Upload Zone ───── */
    .upload-zone {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 60vh;
      text-align: center;
    }
    .upload-box {
      border: 2.5px dashed var(--border);
      border-radius: 20px;
      padding: 56px 64px;
      max-width: 520px;
      width: 100%;
      transition: border-color 200ms ease, background 200ms ease;
      cursor: pointer;
      position: relative;
    }
    .upload-box.dragover {
      border-color: var(--blue);
      background: var(--blue-light);
    }
    .upload-box svg { color: var(--text-tertiary); margin-bottom: var(--space-4); }
    .upload-title {
      font-size: var(--text-lg);
      font-weight: 700;
      margin-bottom: var(--space-1);
    }
    .upload-sub {
      font-size: var(--text-sm);
      color: var(--text-secondary);
      margin-bottom: var(--space-4);
    }
    .upload-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-body);
      font-size: var(--text-sm);
      font-weight: 600;
      color: var(--surface);
      background: var(--blue);
      border: none;
      border-radius: 10px;
      padding: 10px 24px;
      cursor: pointer;
      transition: background 150ms ease;
    }
    .upload-btn:hover { background: #1d4ed8; }
    .upload-box input[type="file"] {
      position: absolute;
      inset: 0;
      opacity: 0;
      cursor: pointer;
    }
    .upload-error {
      color: var(--red);
      font-size: var(--text-sm);
      font-weight: 600;
      margin-top: var(--space-3);
      min-height: 1.5em;
    }
    /* File badge after load */
    .file-badge {
      display: none;
      align-items: center;
      gap: 8px;
      margin-bottom: var(--space-5);
      justify-content: center;
    }
    .file-badge.visible { display: flex; }
    .file-badge-inner {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: var(--text-sm);
      font-weight: 600;
      color: var(--text-secondary);
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 999px;
      padding: 6px 16px;
    }
    .file-badge-inner svg { flex-shrink: 0; }
    .file-badge-reload {
      font-family: var(--font-body);
      font-size: var(--text-xs);
      font-weight: 600;
      color: var(--blue);
      background: none;
      border: none;
      cursor: pointer;
      text-decoration: underline;
      text-underline-offset: 2px;
    }
    .file-badge-reload:hover { color: #1d4ed8; }

    /* ───── Dashboard (hidden until CSV loads) ───── */
    .dashboard { display: none; }
    .dashboard.visible { display: block; }

    /* ───── Header ───── */
    .header {
      text-align: center;
      margin-bottom: var(--space-6);
    }
    .header h1 {
      font-size: var(--text-2xl);
      font-weight: 700;
      letter-spacing: -0.025em;
    }

    /* ───── Summary Cards ───── */
    .summary-row {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: var(--space-3);
      margin-bottom: var(--space-6);
    }
    .stat-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: var(--space-4) var(--space-5);
      box-shadow: var(--shadow-sm);
    }
    .stat-label {
      font-size: var(--text-xs);
      font-weight: 500;
      color: var(--text-tertiary);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: var(--space-1);
    }
    .stat-value {
      font-size: var(--text-xl);
      font-weight: 700;
      font-variant-numeric: tabular-nums;
    }

    /* ───── NMLS Selector ───── */
    .selector-section {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-bottom: var(--space-5);
    }
    .selector-label {
      font-size: var(--text-xs);
      font-weight: 600;
      color: var(--text-tertiary);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: var(--space-2);
    }
    .selector-row {
      display: flex;
      align-items: center;
      gap: var(--space-3);
      flex-wrap: wrap;
      justify-content: center;
    }
    .nmls-input-wrap {
      position: relative;
      display: inline-flex;
      align-items: center;
    }
    .nmls-input-wrap .icon {
      position: absolute;
      left: 16px;
      pointer-events: none;
      color: var(--text-tertiary);
      display: flex;
      align-items: center;
    }
    input#nmlsInput {
      font-family: var(--font-body);
      font-size: var(--text-base);
      font-weight: 600;
      color: var(--text-primary);
      border: 2px solid var(--border);
      border-radius: 14px;
      padding: 12px 20px 12px 44px;
      background: var(--surface);
      outline: none;
      cursor: text;
      width: 240px;
      box-shadow: var(--shadow-md);
      transition: border-color 180ms ease, box-shadow 180ms ease;
      font-variant-numeric: tabular-nums;
    }
    input#nmlsInput::placeholder {
      color: var(--text-tertiary);
      font-weight: 500;
    }
    input#nmlsInput:hover { border-color: var(--blue); }
    input#nmlsInput:focus {
      border-color: var(--blue);
      box-shadow: var(--shadow-md), 0 0 0 3px rgba(37, 99, 235, 0.12);
    }

    /* Custom dropdown panel */
    .nmls-dropdown-wrap {
      position: relative;
      display: inline-flex;
      flex-direction: column;
    }
    .nmls-dropdown {
      position: absolute;
      top: 100%;
      left: 0;
      right: 0;
      margin-top: 4px;
      background: var(--surface);
      border: 1.5px solid var(--border);
      border-radius: 12px;
      box-shadow: var(--shadow-lg);
      max-height: 260px;
      overflow-y: auto;
      z-index: 20;
      display: none;
    }
    .nmls-dropdown.open { display: block; }
    .nmls-dropdown-item {
      padding: 10px 16px;
      font-size: var(--text-sm);
      font-weight: 500;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-variant-numeric: tabular-nums;
      transition: background 80ms ease;
    }
    .nmls-dropdown-item:first-child { border-radius: 10px 10px 0 0; }
    .nmls-dropdown-item:last-child { border-radius: 0 0 10px 10px; }
    .nmls-dropdown-item:hover { background: var(--blue-light); }
    .nmls-dropdown-item.active { background: var(--blue-light); font-weight: 700; }
    .nmls-dropdown-item .dd-nmls { color: var(--text-primary); font-weight: 600; }
    .nmls-dropdown-item .dd-pair { color: var(--text-tertiary); font-size: var(--text-xs); font-weight: 600; }

    /* ───── Badges ───── */
    .match-badge {
      display: inline-flex;
      align-items: center;
      padding: 6px 14px;
      border-radius: 999px;
      font-size: var(--text-base);
      font-weight: 700;
      font-variant-numeric: tabular-nums;
      background: var(--green-light);
      color: var(--green);
      white-space: nowrap;
      opacity: 0;
      transition: opacity 180ms ease;
    }
    .match-badge.visible { opacity: 1; }

    .nmls-pair-info {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 999px;
      font-size: var(--text-sm);
      font-weight: 600;
      font-variant-numeric: tabular-nums;
      background: #f3f4f6;
      color: var(--text-secondary);
      white-space: nowrap;
      opacity: 0;
      transition: opacity 180ms ease;
    }
    .nmls-pair-info.visible { opacity: 1; }
    .nmls-pair-info .pi-pair { font-weight: 700; color: var(--text-primary); }
    .nmls-pair-info .pi-ctrl { color: var(--green); font-weight: 700; }
    .nmls-pair-info .pi-treat { color: var(--blue); font-weight: 700; }

    /* ───── Panels & Grid ───── */
    .main-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: var(--space-4);
    }
    .panel {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }
    .panel-head {
      padding: var(--space-3) var(--space-4);
      border-bottom: 1px solid var(--border-light);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .panel-title {
      font-size: var(--text-sm);
      font-weight: 600;
      color: var(--text-secondary);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .panel-body {
      padding: var(--space-3) var(--space-4);
      flex: 1;
      min-height: 0;
    }

    /* ───── Map Panel ───── */
    .map-panel { grid-column: 1 / -1; }
    .map-panel .panel-body { padding: var(--space-2); position: relative; }
    .map-wrap {
      position: relative;
      background: #0d1117;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
      overflow: hidden;
      height: 520px;
    }
    .map-legend {
      position: absolute;
      top: 12px;
      right: 14px;
      display: flex;
      gap: 14px;
      z-index: 2;
      background: rgba(255,255,255,0.92);
      backdrop-filter: blur(6px);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 8px 14px;
      box-shadow: var(--shadow-sm);
    }
    .map-legend-item {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-secondary);
    }
    .map-legend-dot {
      width: 9px;
      height: 9px;
      border-radius: 50%;
      flex-shrink: 0;
    }

    /* View mode toggle */
    .view-toggle {
      position: absolute;
      top: 12px;
      left: 14px;
      display: flex;
      z-index: 2;
      background: rgba(255,255,255,0.92);
      backdrop-filter: blur(6px);
      border: 1px solid var(--border);
      border-radius: 10px;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
    }
    .view-toggle-btn {
      font-family: var(--font-body);
      font-size: 11px;
      font-weight: 600;
      padding: 7px 14px;
      border: none;
      background: transparent;
      color: var(--text-secondary);
      cursor: pointer;
      transition: background 120ms ease, color 120ms ease;
    }
    .view-toggle-btn.active {
      background: var(--blue);
      color: white;
    }
    .view-toggle-btn:not(:last-child) { border-right: 1px solid var(--border); }

    /* Map hint */
    .map-hint {
      position: absolute;
      bottom: 12px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 2;
      font-size: 11px;
      font-weight: 500;
      color: rgba(255,255,255,0.5);
      pointer-events: none;
      text-align: center;
    }

    #mapCanvas {
      width: 100%;
      height: 100%;
      display: block;
      cursor: grab;
    }
    #mapCanvas:active { cursor: grabbing; }

    /* 2D canvas (hidden by default) */
    #map2dCanvas {
      width: 100%;
      height: 100%;
      display: none;
      cursor: grab;
    }
    #map2dCanvas:active { cursor: grabbing; }

    /* ───── Blended 5-Column Table ───── */
    .compare-panel { grid-column: 1 / -1; }
    .blend-table { width: 100%; max-width: 820px; margin: 0 auto; border-collapse: collapse; }
    .blend-table th { font-size: var(--text-xs); font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; padding: var(--space-2) var(--space-3); border-bottom: 1.5px solid var(--border); white-space: nowrap; }
    .blend-table th.col-metric { color: var(--text-tertiary); text-align: left; }
    .blend-table th.col-ctrl-val { color: var(--green); text-align: right; }
    .blend-table th.col-ctrl-bar { color: var(--green); text-align: center; padding-right: 0; }
    .blend-table th.col-treat-bar { color: var(--blue); text-align: center; padding-left: 0; }
    .blend-table th.col-treat-val { color: var(--blue); text-align: left; }
    .blend-table td { padding: 6px var(--space-3); font-size: var(--text-sm); border-bottom: 1px solid var(--border-light); vertical-align: middle; }
    .blend-table tr:last-child td { border-bottom: none; }
    .blend-table .td-metric { font-weight: 500; color: var(--text-secondary); white-space: nowrap; width: 110px; }
    .blend-table .td-ctrl-val { font-weight: 700; color: var(--green); text-align: right; font-variant-numeric: tabular-nums; width: 70px; }
    .blend-table .td-treat-val { font-weight: 700; color: var(--blue); text-align: left; font-variant-numeric: tabular-nums; width: 70px; }
    .blend-table .td-bar { padding-top: 6px; padding-bottom: 6px; }
    .blend-table .td-ctrl-bar { padding-right: 0; }
    .blend-table .td-treat-bar { padding-left: 0; }
    .bar-track { height: 20px; background: var(--bg); position: relative; overflow: hidden; }
    .td-ctrl-bar .bar-track { border-radius: 4px 0 0 4px; }
    .td-treat-bar .bar-track { border-radius: 0 4px 4px 0; }
    .bar-fill { position: absolute; top: 0; height: 100%; transition: width 300ms ease; }
    .td-ctrl-bar .bar-fill { right: 0; background: var(--green); opacity: 0.72; border-radius: 4px 0 0 4px; }
    .td-treat-bar .bar-fill { left: 0; background: var(--blue); opacity: 0.72; border-radius: 0 4px 4px 0; }

    /* ───── Tooltip ───── */
    .map-tooltip { position: fixed; pointer-events: none; z-index: 100; background: rgba(255,255,255,0.97); backdrop-filter: blur(10px); border: 1px solid var(--border); border-radius: 12px; padding: 14px 18px 12px; box-shadow: var(--shadow-lg); font-size: 13px; line-height: 1.5; color: var(--text-primary); opacity: 0; transition: opacity 120ms ease; transform: translate(-50%, -100%); margin-top: -14px; white-space: nowrap; }
    .map-tooltip.visible { opacity: 1; }
    .tt-pair-grid { display: grid; grid-template-columns: auto 1fr 1fr; gap: 3px 16px; font-variant-numeric: tabular-nums; }
    .tt-col-header { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; padding-bottom: 4px; border-bottom: 1.5px solid var(--border-light); }
    .tt-col-header.control { color: var(--green); }
    .tt-col-header.treatment { color: var(--blue); }
    .tt-col-header.metric { color: var(--text-tertiary); }
    .tt-metric { font-size: 13px; color: var(--text-secondary); padding: 2px 0; }
    .tt-val { font-size: 13px; font-weight: 600; color: var(--text-primary); text-align: right; padding: 2px 0; }
    .tt-outlier-header { font-size: 15px; font-weight: 700; margin-bottom: 6px; font-variant-numeric: tabular-nums; }
    .tt-outlier-badge { display: inline-block; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; padding: 2px 7px; border-radius: 4px; margin-left: 6px; background: var(--red-light); color: var(--red); }
    .tt-outlier-row { display: flex; justify-content: space-between; gap: 16px; color: var(--text-secondary); font-size: 13px; padding: 2px 0; }
    .tt-outlier-row span:last-child { font-weight: 600; color: var(--text-primary); font-variant-numeric: tabular-nums; }

    /* ───── Raw Data Table ───── */
    .data-panel { grid-column: 1 / -1; margin-top: var(--space-4); }
    .data-table-wrap {
      max-height: 480px;
      overflow: auto;
      border: 1px solid var(--border-light);
      border-radius: var(--radius-md);
    }
    .raw-table { width: 100%; border-collapse: collapse; font-size: var(--text-xs); }
    .raw-table th {
      position: sticky;
      top: 0;
      background: var(--surface);
      z-index: 1;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--text-tertiary);
      padding: 8px 10px;
      border-bottom: 1.5px solid var(--border);
      white-space: nowrap;
      text-align: left;
    }
    .raw-table td {
      padding: 6px 10px;
      border-bottom: 1px solid var(--border-light);
      white-space: nowrap;
      font-variant-numeric: tabular-nums;
      color: var(--text-secondary);
    }
    .raw-table tr:hover td { background: #f9fafb; }
    .raw-table tr:last-child td { border-bottom: none; }
    /* Selected pair row highlights */
    .raw-table tr.row-ctrl td { background: #d1fae5; }
    .raw-table tr.row-treat td { background: #dbeafe; }
    .raw-table tr.row-ctrl:hover td { background: #a7f3d0; }
    .raw-table tr.row-treat:hover td { background: #bfdbfe; }
    /* Color-code assignment column */
    .raw-table td.asgn-control { color: var(--green); font-weight: 600; }
    .raw-table td.asgn-treatment { color: var(--blue); font-weight: 600; }
    .raw-table td.asgn-outlier { color: var(--red); font-weight: 600; }

    /* ───── Responsive ───── */
    @media (max-width: 960px) {
      .summary-row { grid-template-columns: repeat(2, 1fr); }
      .main-grid { grid-template-columns: 1fr; }
      .map-panel, .compare-panel, .data-panel { grid-column: 1; }
      input#nmlsInput { width: 100%; }
      .selector-row { flex-direction: column; }
    }
  </style>
</head>
<body>
  <div class="page">

    <!-- Header -->
    <div class="header">
      <h1>Twin Pair Dashboard</h1>
    </div>

    <!-- Upload Zone -->
    <div class="upload-zone" id="uploadZone">
      <div class="upload-box" id="uploadBox">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
        <div class="upload-title">Upload Twin Pair CSV</div>
        <div class="upload-sub">Drag and drop or click to browse</div>
        <button class="upload-btn">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
          Choose File
        </button>
        <input type="file" id="fileInput" accept=".csv" />
      </div>
      <div class="upload-error" id="uploadError"></div>
    </div>

    <!-- File badge (shown after load) -->
    <div class="file-badge" id="fileBadge">
      <div class="file-badge-inner">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
        <span id="fileName"></span>
      </div>
      <button class="file-badge-reload" id="reloadBtn">Upload new file</button>
    </div>

    <!-- ═══════════ Dashboard (hidden until CSV loaded) ═══════════ -->
    <div class="dashboard" id="dashboard">

      <!-- Summary -->
      <div class="summary-row" id="summaryRow"></div>

      <!-- NMLS Selector -->
      <div class="selector-section">
        <div class="selector-label">Search Treatment NMLS</div>
        <div class="selector-row">
          <div class="nmls-dropdown-wrap">
            <div class="nmls-input-wrap">
              <span class="icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
              </span>
              <input id="nmlsInput" type="text" placeholder="Type or select NMLS…" autocomplete="off" />
            </div>
            <div class="nmls-dropdown" id="nmlsDropdown"></div>
          </div>
          <span class="nmls-pair-info" id="nmlsPairInfo"></span>
          <span class="match-badge" id="matchBadge"></span>
        </div>
      </div>

      <!-- Grid -->
      <div class="main-grid">

        <!-- Map -->
        <div class="panel map-panel">
          <div class="panel-head"><span class="panel-title">Overview Map</span></div>
          <div class="panel-body">
            <div class="map-wrap" id="mapWrap">
              <div class="view-toggle">
                <button class="view-toggle-btn active" id="btn3d" onclick="setView('3d')">3D Scatter</button>
                <button class="view-toggle-btn" id="btn2d" onclick="setView('2d')">2D Density</button>
              </div>
              <div class="map-legend">
                <div class="map-legend-item"><span class="map-legend-dot" style="background:var(--green)"></span>Control</div>
                <div class="map-legend-item"><span class="map-legend-dot" style="background:var(--blue)"></span>Treatment</div>
                <div class="map-legend-item"><span class="map-legend-dot" style="background:var(--red)"></span>Outlier</div>
              </div>
              <canvas id="mapCanvas"></canvas>
              <canvas id="map2dCanvas"></canvas>
              <div class="map-hint" id="mapHint">Drag to rotate · Scroll to zoom · Click a point to select</div>
            </div>
          </div>
        </div>

        <!-- Blended Comparison -->
        <div class="panel compare-panel">
          <div class="panel-head"><span class="panel-title">Profile Comparison</span></div>
          <div class="panel-body">
            <table class="blend-table">
              <thead><tr>
                <th class="col-metric">Metric</th>
                <th class="col-ctrl-val" id="controlHeader">Control</th>
                <th class="col-ctrl-bar">Control</th>
                <th class="col-treat-bar">Treatment</th>
                <th class="col-treat-val" id="treatmentHeader">Treatment</th>
              </tr></thead>
              <tbody id="compareBody"></tbody>
            </table>
          </div>
        </div>

        <!-- Raw Data Table -->
        <div class="panel data-panel">
          <div class="panel-head"><span class="panel-title">Raw Data</span></div>
          <div class="panel-body" style="padding:0">
            <div class="data-table-wrap">
              <table class="raw-table" id="rawTable"></table>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
  <div class="map-tooltip" id="mapTooltip"></div>

  <script>
    /* ═══════════════════════════════════════════════════════════
       GLOBALS
    ═══════════════════════════════════════════════════════════ */
    let D = null;
    let state = {};
    let nmlsToPair = {};
    let nmlsToMember = {};
    let treatNmlsToPair = {};
    let csvRows = [];
    let csvHeaders = [];
    let currentView = '3d';  // '3d' or '2d'

    const $ = id => document.getElementById(id);
    const el = {
      uploadZone:   $("uploadZone"),
      uploadBox:    $("uploadBox"),
      fileInput:    $("fileInput"),
      uploadError:  $("uploadError"),
      fileBadge:    $("fileBadge"),
      fileName:     $("fileName"),
      reloadBtn:    $("reloadBtn"),
      dashboard:    $("dashboard"),
      summaryRow:   $("summaryRow"),
      nmlsInput:    $("nmlsInput"),
      nmlsDropdown: $("nmlsDropdown"),
      nmlsPairInfo: $("nmlsPairInfo"),
      matchBadge:   $("matchBadge"),
      controlHeader:$("controlHeader"),
      treatmentHeader:$("treatmentHeader"),
      compareBody:  $("compareBody"),
      mapTooltip:   $("mapTooltip"),
      rawTable:     $("rawTable"),
      mapWrap:      $("mapWrap"),
      mapCanvas:    $("mapCanvas"),
      map2dCanvas:  $("map2dCanvas"),
      mapHint:      $("mapHint")
    };

    function fmt(v, d = 0) {
      return Number(v).toLocaleString(undefined, { minimumFractionDigits: d, maximumFractionDigits: d });
    }

    const METRIC_NAMES = {
      pro_score: 'PRO Score', uwm_production: 'UWM Prod.', overall_production: 'Overall Prod.',
      conv_mix: 'Conv Mix', fha_mix: 'FHA Mix', va_mix: 'VA Mix',
      purchase_pct: 'Purchase %', total_ytd_closings: 'YTD Closings'
    };
    function prettyMetric(m) {
      return METRIC_NAMES[m] || m.replace(/_pct/g, " %").replace(/_mix/g, " Mix").replace(/_/g, " ").replace(/\b\w/g, c => c.toUpperCase());
    }
    function getPair(id) { return D.pairs.find(p => p.pair_id === Number(id)); }

    /* ═══════════════════════════════════════════════════════════
       CSV PARSING → D object
    ═══════════════════════════════════════════════════════════ */
    function parseCSV(text) {
      const lines = text.trim().split(/\r?\n/);
      const headers = lines[0].split(',').map(h => h.trim().toLowerCase());
      csvHeaders = headers;
      const rows = lines.slice(1).map(line => {
        const vals = line.split(',');
        const obj = {};
        headers.forEach((h, i) => { obj[h] = vals[i] ? vals[i].trim() : ''; });
        return obj;
      });
      csvRows = rows;
      return { headers, rows };
    }

    function num(v) { const n = parseFloat(v); return isNaN(n) ? 0 : n; }

    function buildDataFromCSV({ headers, rows }) {
      const KNOWN_FEATURES = ['pro_score','uwm_production','overall_production','conv_mix','fha_mix','va_mix','purchase_pct','total_ytd_closings'];
      const match_features = KNOWN_FEATURES.filter(f => headers.includes(f));

      const pairMap = {};
      const unmatched = [];

      rows.forEach(r => {
        const pid = parseInt(r.pair_id);
        if (!pid || isNaN(pid)) {
          unmatched.push(buildMember(r, 'outlier'));
          return;
        }
        if (!pairMap[pid]) pairMap[pid] = [];
        pairMap[pid].push(r);
      });

      const pairs = Object.keys(pairMap).sort((a, b) => +a - +b).map(pid => {
        const members = pairMap[pid].map(r => buildMember(r, r.assignment || 'unknown'));
        const ctrl = members.find(m => m.assignment === 'control') || members[0];
        const treat = members.find(m => m.assignment === 'treatment') || members[1];
        return {
          pair_id: +pid,
          pair_distance: num(pairMap[pid][0].pair_distance),
          match_score: num(pairMap[pid][0].match_score),
          rank_bucket: pairMap[pid][0].pro_ranking || '',
          control_nmls: ctrl ? ctrl.nmls : 0,
          treatment_nmls: treat ? treat.nmls : 0,
          members
        };
      });

      const feature_ranges = {};
      match_features.forEach(f => {
        const vals = rows.map(r => num(r[f]));
        feature_ranges[f] = { min: Math.min(...vals), max: Math.max(...vals) };
      });

      const allDistances = pairs.map(p => p.pair_distance).filter(d => d > 0);
      const summary = {
        matched_records: pairs.reduce((s, p) => s + p.members.length, 0),
        pair_count: pairs.length,
        unmatched_records: unmatched.length,
        avg_pair_distance: allDistances.length ? +(allDistances.reduce((a, b) => a + b, 0) / allDistances.length).toFixed(4) : 0
      };

      return { summary, pairs, unmatched, match_features, feature_ranges };
    }

    function buildMember(r, fallbackAssignment) {
      return {
        nmls: parseInt(r.nmls) || 0,
        assignment: (r.assignment || fallbackAssignment).toLowerCase(),
        pro_ranking: r.pro_ranking || '',
        pro_score: num(r.pro_score),
        uwm_production: num(r.uwm_production),
        overall_production: num(r.overall_production),
        conv_mix: num(r.conv_mix),
        fha_mix: num(r.fha_mix),
        va_mix: num(r.va_mix),
        purchase_pct: num(r.purchase_pct),
        refi_pct: num(r.refi_pct),
        total_ytd_closings: num(r.total_ytd_closings),
        jan_closings: num(r.jan_closings),
        feb_closings: num(r.feb_closings),
        march_closings: num(r.march_closings),
        pair_distance: num(r.pair_distance),
        twin_nmls: parseInt(r.twin_nmls) || 0,
        plot_x: num(r.plot_x),
        plot_y: num(r.plot_y)
      };
    }

    /* ═══════════════════════════════════════════════════════════
       FILE UPLOAD HANDLING
    ═══════════════════════════════════════════════════════════ */
    function handleFile(file) {
      el.uploadError.textContent = '';
      if (!file || !file.name.endsWith('.csv')) {
        el.uploadError.textContent = 'Please upload a .csv file';
        return;
      }
      const reader = new FileReader();
      reader.onload = e => {
        try {
          const parsed = parseCSV(e.target.result);
          if (!parsed.headers.includes('nmls')) throw new Error('Missing "nmls" column');
          if (!parsed.headers.includes('assignment')) throw new Error('Missing "assignment" column');
          D = buildDataFromCSV(parsed);
          if (D.pairs.length === 0) throw new Error('No pairs found (need "pair_id" column)');
          showDashboard(file.name);
        } catch (err) {
          el.uploadError.textContent = 'Error: ' + err.message;
        }
      };
      reader.readAsText(file);
    }

    el.uploadBox.addEventListener('dragover', e => { e.preventDefault(); el.uploadBox.classList.add('dragover'); });
    el.uploadBox.addEventListener('dragleave', () => { el.uploadBox.classList.remove('dragover'); });
    el.uploadBox.addEventListener('drop', e => { e.preventDefault(); el.uploadBox.classList.remove('dragover'); handleFile(e.dataTransfer.files[0]); });
    el.fileInput.addEventListener('change', e => { handleFile(e.target.files[0]); });

    el.reloadBtn.addEventListener('click', () => {
      el.dashboard.classList.remove('visible');
      el.fileBadge.classList.remove('visible');
      el.uploadZone.style.display = '';
      el.fileInput.value = '';
      if (threeScene) { threeScene.dispose && threeScene.dispose(); threeScene = null; }
    });

    /* ═══════════════════════════════════════════════════════════
       SHOW DASHBOARD
    ═══════════════════════════════════════════════════════════ */
    function showDashboard(name) {
      nmlsToPair = {};
      nmlsToMember = {};
      treatNmlsToPair = {};
      D.pairs.forEach(p => {
        p.members.forEach(m => {
          nmlsToPair[m.nmls] = p.pair_id;
          nmlsToMember[m.nmls] = { ...m, pair: p };
        });
        const t = p.members.find(m => m.assignment === 'treatment');
        if (t) treatNmlsToPair[t.nmls] = p;
      });
      D.unmatched.forEach(u => {
        nmlsToMember[u.nmls] = { ...u, pair: null };
      });

      state = { activePairId: D.pairs[0].pair_id };

      el.uploadZone.style.display = 'none';
      el.fileName.textContent = name;
      el.fileBadge.classList.add('visible');
      el.dashboard.classList.add('visible');

      buildSummary();
      buildNmlsInput();
      buildRawTable();

      const initPair = D.pairs[0];
      const initTreat = initPair.members.find(m => m.assignment === 'treatment');
      if (initTreat) el.nmlsInput.value = initTreat.nmls;
      updateNmlsPairInfo(initPair);

      // Init 3D and 2D
      setTimeout(() => {
        init3DMap();
        init2DMap();
        render();
      }, 100);
    }

    /* ═══════════════════════════════════════════════════════════
       SUMMARY
    ═══════════════════════════════════════════════════════════ */
    function buildSummary() {
      const items = [
        ["Matched Records", D.summary.matched_records],
        ["Twin Pairs", D.summary.pair_count],
        ["Outliers", D.summary.unmatched_records],
        ["Avg Pair Distance", D.summary.avg_pair_distance]
      ];
      el.summaryRow.innerHTML = items.map(([l, v]) =>
        `<div class="stat-card"><div class="stat-label">${l}</div><div class="stat-value">${v}</div></div>`
      ).join("");
    }

    /* ═══════════════════════════════════════════════════════════
       NMLS INPUT
    ═══════════════════════════════════════════════════════════ */
    let ddItems = [];

    function buildNmlsInput() {
      const sorted = D.pairs.slice().sort((a, b) => a.pair_id - b.pair_id);
      ddItems = sorted.map(p => {
        const t = p.members.find(m => m.assignment === 'treatment');
        const c = p.members.find(m => m.assignment === 'control');
        if (!t) return null;
        return { nmls: t.nmls, pair: p, label: `Pair ${p.pair_id}  (C: ${c ? c.nmls : '\u2014'}, T: ${t.nmls})` };
      }).filter(Boolean);

      populateDropdown(ddItems);

      const fresh = el.nmlsInput.cloneNode(true);
      el.nmlsInput.parentNode.replaceChild(fresh, el.nmlsInput);
      el.nmlsInput = fresh;

      el.nmlsInput.addEventListener('focus', () => openDropdown());
      el.nmlsInput.addEventListener('input', () => {
        const q = el.nmlsInput.value.trim().toLowerCase();
        if (!q) { populateDropdown(ddItems); openDropdown(); return; }
        const filtered = ddItems.filter(it => String(it.nmls).includes(q) || it.label.toLowerCase().includes(q));
        populateDropdown(filtered);
        openDropdown();
      });

      document.addEventListener('click', e => {
        if (!el.nmlsInput.contains(e.target) && !el.nmlsDropdown.contains(e.target)) {
          closeDropdown();
        }
      });
    }

    function populateDropdown(items) {
      el.nmlsDropdown.innerHTML = items.map((it, i) =>
        `<div class="nmls-dropdown-item" data-index="${i}" data-nmls="${it.nmls}">` +
        `<span class="dd-nmls">${it.label}</span>` +
        `</div>`
      ).join('');
      el.nmlsDropdown.querySelectorAll('.nmls-dropdown-item').forEach(div => {
        div.addEventListener('click', () => {
          const nmls = Number(div.dataset.nmls);
          pickNmls(nmls);
        });
      });
    }

    function openDropdown() { el.nmlsDropdown.classList.add('open'); }
    function closeDropdown() { el.nmlsDropdown.classList.remove('open'); }

    function pickNmls(nmls) {
      const pair = treatNmlsToPair[nmls];
      if (!pair) return;
      el.nmlsInput.value = nmls;
      closeDropdown();
      state.activePairId = pair.pair_id;
      updateNmlsPairInfo(pair);
      highlightRawRows(pair);
      render();
    }

    function updateNmlsPairInfo(pair) {
      const ctrl = pair.members.find(m => m.assignment === 'control');
      const treat = pair.members.find(m => m.assignment === 'treatment');
      el.nmlsPairInfo.innerHTML =
        `<span class="pi-pair">Pair ${pair.pair_id}</span>` +
        `<span>\u00b7</span>` +
        `<span class="pi-ctrl">C: ${ctrl ? ctrl.nmls : '\u2014'}</span>` +
        `<span class="pi-treat">T: ${treat ? treat.nmls : '\u2014'}</span>`;
      el.nmlsPairInfo.classList.add('visible');
      el.matchBadge.textContent = `${fmt(pair.match_score, 1)}% match`;
      el.matchBadge.classList.add('visible');
    }

    /* ═══════════════════════════════════════════════════════════
       TOOLTIP
    ═══════════════════════════════════════════════════════════ */
    function showTooltipAt(x, y, nmls) {
      const info = nmlsToMember[nmls];
      if (!info) return;
      const tt = el.mapTooltip;
      const isOutlier = info.assignment === 'outlier';
      if (!isOutlier) {
        const pair = info.pair;
        const ctrl = pair.members.find(m => m.assignment === 'control');
        const treat = pair.members.find(m => m.assignment === 'treatment');
        const metrics = [
          ['Rank', ctrl.pro_ranking, treat.pro_ranking],
          ['PRO Score', ctrl.pro_score, treat.pro_score],
          ['UWM Prod.', fmt(ctrl.uwm_production, 0), fmt(treat.uwm_production, 0)],
          ['Overall Prod.', fmt(ctrl.overall_production, 0), fmt(treat.overall_production, 0)],
          ['Conv Mix', fmt(ctrl.conv_mix, 1), fmt(treat.conv_mix, 1)],
          ['Purchase %', fmt(ctrl.purchase_pct, 1), fmt(treat.purchase_pct, 1)],
          ['YTD Closings', ctrl.total_ytd_closings, treat.total_ytd_closings]
        ];
        const rows = metrics.map(([label, cv, tv]) =>
          `<span class="tt-metric">${label}</span><span class="tt-val">${cv}</span><span class="tt-val">${tv}</span>`
        ).join('');
        tt.innerHTML = `<div class="tt-pair-grid">
          <span class="tt-col-header metric"></span>
          <span class="tt-col-header control">C: ${ctrl.nmls}</span>
          <span class="tt-col-header treatment">T: ${treat.nmls}</span>
          ${rows}</div>`;
      } else {
        tt.innerHTML = `<div class="tt-outlier-header">${nmls}<span class="tt-outlier-badge">Outlier</span></div>
          <div class="tt-outlier-row"><span>Rank</span><span>${info.pro_ranking}</span></div>
          <div class="tt-outlier-row"><span>PRO Score</span><span>${info.pro_score}</span></div>
          <div class="tt-outlier-row"><span>UWM Production</span><span>${fmt(info.uwm_production, 0)}</span></div>
          <div class="tt-outlier-row"><span>YTD Closings</span><span>${info.total_ytd_closings}</span></div>`;
      }
      tt.style.left = x + 'px';
      tt.style.top = y + 'px';
      tt.classList.add('visible');
    }
    function hideTooltip() { el.mapTooltip.classList.remove('visible'); }

    /* ═══════════════════════════════════════════════════════════
       VIEW MODE TOGGLE
    ═══════════════════════════════════════════════════════════ */
    function setView(mode) {
      currentView = mode;
      $('btn3d').classList.toggle('active', mode === '3d');
      $('btn2d').classList.toggle('active', mode === '2d');
      el.mapCanvas.style.display = mode === '3d' ? 'block' : 'none';
      el.map2dCanvas.style.display = mode === '2d' ? 'block' : 'none';
      el.mapHint.textContent = mode === '3d'
        ? 'Drag to rotate \u00b7 Scroll to zoom \u00b7 Click a point to select'
        : 'Drag to pan \u00b7 Scroll to zoom \u00b7 Click a point to select';
      if (mode === '3d') update3DMap();
      if (mode === '2d') render2DMap();
    }

    /* ═══════════════════════════════════════════════════════════
       3D MAP (Three.js)
    ═══════════════════════════════════════════════════════════ */
    let threeScene = null;
    let threeRenderer, threeCamera, threeControls;
    let pointMeshes = [];  // { mesh, nmls, pairId, assignment, x, y, z }
    let lineMeshes = [];   // { line, pairId }
    let labelSprites = []; // { sprite, pairId }
    let ringMesh = null;
    let raycaster, mouse;

    function computeZCoord(member) {
      // Use match_score as Z for paired members, or a hash for outliers
      const pid = nmlsToPair[member.nmls];
      if (pid) {
        const pair = getPair(pid);
        return pair ? pair.match_score : 50;
      }
      return 10 + (member.pro_score || 0) * 0.5;
    }

    function init3DMap() {
      const container = el.mapWrap;
      const W = container.clientWidth;
      const H = container.clientHeight;

      // Clean up previous
      if (threeRenderer) {
        threeRenderer.dispose();
        threeRenderer.domElement.remove();
      }

      // Setup renderer
      threeRenderer = new THREE.WebGLRenderer({ canvas: el.mapCanvas, antialias: true, alpha: false });
      threeRenderer.setSize(W, H);
      threeRenderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      threeRenderer.setClearColor(0x0d1117, 1);

      // Camera
      threeCamera = new THREE.PerspectiveCamera(50, W / H, 0.1, 2000);
      threeCamera.position.set(0, 0, 200);

      // Scene
      threeScene = new THREE.Scene();

      // Ambient light
      threeScene.add(new THREE.AmbientLight(0xffffff, 0.8));
      const dirLight = new THREE.DirectionalLight(0xffffff, 0.6);
      dirLight.position.set(50, 80, 100);
      threeScene.add(dirLight);

      // Orbit controls
      threeControls = new THREE.OrbitControls(threeCamera, threeRenderer.domElement);
      threeControls.enableDamping = true;
      threeControls.dampingFactor = 0.08;
      threeControls.minDistance = 30;
      threeControls.maxDistance = 600;

      // Grid helper
      const gridSize = 200;
      const gridDivs = 20;
      const grid = new THREE.GridHelper(gridSize, gridDivs, 0x1a2332, 0x151d2a);
      grid.rotation.x = Math.PI / 2;
      grid.position.z = -5;
      threeScene.add(grid);

      // Raycaster for click/hover
      raycaster = new THREE.Raycaster();
      raycaster.params.Points = { threshold: 3 };
      mouse = new THREE.Vector2();

      // Build points
      buildPoints3D();

      // Animate
      function animate() {
        requestAnimationFrame(animate);
        threeControls.update();
        threeRenderer.render(threeScene, threeCamera);
      }
      animate();

      // Event handlers
      el.mapCanvas.addEventListener('mousemove', onMapMouseMove);
      el.mapCanvas.addEventListener('click', onMapClick);
      el.mapCanvas.addEventListener('mouseleave', hideTooltip);

      // Resize
      window.addEventListener('resize', () => {
        const w = container.clientWidth;
        const h = container.clientHeight;
        threeCamera.aspect = w / h;
        threeCamera.updateProjectionMatrix();
        threeRenderer.setSize(w, h);
      });
    }

    function buildPoints3D() {
      if (!threeScene) return;

      // Clear old
      pointMeshes.forEach(p => threeScene.remove(p.mesh));
      lineMeshes.forEach(l => threeScene.remove(l.line));
      labelSprites.forEach(l => threeScene.remove(l.sprite));
      if (ringMesh) { threeScene.remove(ringMesh); ringMesh = null; }
      pointMeshes = [];
      lineMeshes = [];
      labelSprites = [];

      // Compute coordinate ranges for normalization
      const allMembers = [];
      D.pairs.forEach(p => p.members.forEach(m => allMembers.push(m)));
      D.unmatched.forEach(u => allMembers.push(u));

      const xs = allMembers.map(m => m.plot_x);
      const ys = allMembers.map(m => m.plot_y);
      const minX = Math.min(...xs), maxX = Math.max(...xs);
      const minY = Math.min(...ys), maxY = Math.max(...ys);
      const rangeX = maxX - minX || 1;
      const rangeY = maxY - minY || 1;

      function norm(m) {
        const nx = ((m.plot_x - minX) / rangeX - 0.5) * 160;
        const ny = ((m.plot_y - minY) / rangeY - 0.5) * -160;
        const z = computeZCoord(m);
        const nz = (z / 100 - 0.5) * 80;
        return { x: nx, y: ny, z: nz };
      }

      const isLarge = D.pairs.length > 50;
      const baseR = isLarge ? (D.pairs.length > 200 ? 1.2 : 1.8) : 2.5;
      const activeR = baseR * 2.2;

      // Create a shared geometry for performance
      const sphereGeo = new THREE.SphereGeometry(1, 12, 8);

      // Colors
      const COL_GREEN = new THREE.Color(0x059669);
      const COL_BLUE = new THREE.Color(0x2563eb);
      const COL_RED = new THREE.Color(0xdc2626);
      const COL_ACTIVE_GREEN = new THREE.Color(0x34d399);
      const COL_ACTIVE_BLUE = new THREE.Color(0x60a5fa);

      // Outliers
      D.unmatched.forEach(u => {
        const { x, y, z } = norm(u);
        const mat = new THREE.MeshPhongMaterial({ color: COL_RED, transparent: true, opacity: 0.6 });
        const mesh = new THREE.Mesh(sphereGeo, mat);
        mesh.position.set(x, y, z);
        mesh.scale.setScalar(baseR);
        mesh.userData = { nmls: u.nmls, assignment: 'outlier', pairId: null };
        threeScene.add(mesh);
        pointMeshes.push({ mesh, nmls: u.nmls, pairId: null, assignment: 'outlier' });
      });

      // Pairs
      D.pairs.forEach(pair => {
        const active = pair.pair_id === state.activePairId;
        const ctrl = pair.members.find(m => m.assignment === 'control');
        const treat = pair.members.find(m => m.assignment === 'treatment');

        const ctrlPos = ctrl ? norm(ctrl) : null;
        const treatPos = treat ? norm(treat) : null;

        // Connection line
        if (ctrlPos && treatPos) {
          const lineGeo = new THREE.BufferGeometry().setFromPoints([
            new THREE.Vector3(ctrlPos.x, ctrlPos.y, ctrlPos.z),
            new THREE.Vector3(treatPos.x, treatPos.y, treatPos.z)
          ]);
          const lineMat = new THREE.LineBasicMaterial({
            color: active ? 0xffffff : 0x3b4a5c,
            transparent: true,
            opacity: active ? 0.8 : 0.15,
            linewidth: 1
          });
          const line = new THREE.Line(lineGeo, lineMat);
          threeScene.add(line);
          lineMeshes.push({ line, pairId: pair.pair_id });
        }

        // Nodes
        [ctrl, treat].forEach(m => {
          if (!m) return;
          const isCtrl = m.assignment === 'control';
          const { x, y, z } = norm(m);
          const col = active
            ? (isCtrl ? COL_ACTIVE_GREEN : COL_ACTIVE_BLUE)
            : (isCtrl ? COL_GREEN : COL_BLUE);
          const mat = new THREE.MeshPhongMaterial({
            color: col,
            transparent: true,
            opacity: active ? 1.0 : (isLarge ? 0.5 : 0.6),
            emissive: active ? col.clone().multiplyScalar(0.3) : new THREE.Color(0x000000)
          });
          const mesh = new THREE.Mesh(sphereGeo, mat);
          mesh.position.set(x, y, z);
          mesh.scale.setScalar(active ? activeR : baseR);
          mesh.userData = { nmls: m.nmls, assignment: m.assignment, pairId: pair.pair_id };
          threeScene.add(mesh);
          pointMeshes.push({ mesh, nmls: m.nmls, pairId: pair.pair_id, assignment: m.assignment });
        });

        // Active pair ring + labels
        if (active && ctrlPos && treatPos) {
          const mx = (ctrlPos.x + treatPos.x) / 2;
          const my = (ctrlPos.y + treatPos.y) / 2;
          const mz = (ctrlPos.z + treatPos.z) / 2;
          const dist = Math.sqrt(
            (ctrlPos.x - treatPos.x) ** 2 +
            (ctrlPos.y - treatPos.y) ** 2 +
            (ctrlPos.z - treatPos.z) ** 2
          );
          const ringGeo = new THREE.RingGeometry(dist / 2 + 8, dist / 2 + 9, 48);
          const ringMat = new THREE.MeshBasicMaterial({
            color: 0xffffff,
            transparent: true,
            opacity: 0.15,
            side: THREE.DoubleSide
          });
          ringMesh = new THREE.Mesh(ringGeo, ringMat);
          ringMesh.position.set(mx, my, mz);
          threeScene.add(ringMesh);

          // Label sprites
          [ctrl, treat].forEach(m => {
            if (!m) return;
            const pos = norm(m);
            const canvas = document.createElement('canvas');
            canvas.width = 256; canvas.height = 64;
            const ctx = canvas.getContext('2d');
            ctx.font = 'bold 32px Inter, sans-serif';
            ctx.fillStyle = m.assignment === 'control' ? '#34d399' : '#60a5fa';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(String(m.nmls), 128, 32);
            const tex = new THREE.CanvasTexture(canvas);
            const spriteMat = new THREE.SpriteMaterial({ map: tex, transparent: true });
            const sprite = new THREE.Sprite(spriteMat);
            sprite.position.set(pos.x, pos.y + activeR + 5, pos.z);
            sprite.scale.set(24, 6, 1);
            threeScene.add(sprite);
            labelSprites.push({ sprite, pairId: pair.pair_id });
          });

          // Pair ID label
          const pCanvas = document.createElement('canvas');
          pCanvas.width = 128; pCanvas.height = 48;
          const pCtx = pCanvas.getContext('2d');
          pCtx.font = 'bold 28px Inter, sans-serif';
          pCtx.fillStyle = 'rgba(255,255,255,0.7)';
          pCtx.textAlign = 'center';
          pCtx.textBaseline = 'middle';
          pCtx.fillText(`P${pair.pair_id}`, 64, 24);
          const pTex = new THREE.CanvasTexture(pCanvas);
          const pSprite = new THREE.Sprite(new THREE.SpriteMaterial({ map: pTex, transparent: true }));
          pSprite.position.set(mx, my + dist / 2 + 12, mz);
          pSprite.scale.set(14, 5, 1);
          threeScene.add(pSprite);
          labelSprites.push({ sprite: pSprite, pairId: pair.pair_id });
        }
      });
    }

    function update3DMap() {
      if (!threeScene) return;
      buildPoints3D();
    }

    function onMapMouseMove(event) {
      if (currentView !== '3d' || !threeScene) return;
      const rect = el.mapCanvas.getBoundingClientRect();
      mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
      mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
      raycaster.setFromCamera(mouse, threeCamera);
      const meshes = pointMeshes.map(p => p.mesh);
      const intersects = raycaster.intersectObjects(meshes);
      if (intersects.length > 0) {
        const hit = intersects[0].object;
        el.mapCanvas.style.cursor = 'pointer';
        showTooltipAt(event.clientX, event.clientY, hit.userData.nmls);
      } else {
        el.mapCanvas.style.cursor = 'grab';
        hideTooltip();
      }
    }

    function onMapClick(event) {
      if (currentView !== '3d' || !threeScene) return;
      const rect = el.mapCanvas.getBoundingClientRect();
      mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
      mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
      raycaster.setFromCamera(mouse, threeCamera);
      const meshes = pointMeshes.map(p => p.mesh);
      const intersects = raycaster.intersectObjects(meshes);
      if (intersects.length > 0) {
        const hit = intersects[0].object;
        const ud = hit.userData;
        if (ud.pairId) {
          selectPair(ud.pairId);
        }
      }
    }

    /* ═══════════════════════════════════════════════════════════
       2D DENSITY MAP (Canvas)
    ═══════════════════════════════════════════════════════════ */
    let map2dState = { offsetX: 0, offsetY: 0, zoom: 1, dragging: false, lastX: 0, lastY: 0 };
    let allPoints2D = [];  // { x, y, nmls, pairId, assignment, color }

    function init2DMap() {
      const canvas = el.map2dCanvas;
      canvas.addEventListener('mousedown', e => {
        map2dState.dragging = true;
        map2dState.lastX = e.clientX;
        map2dState.lastY = e.clientY;
      });
      canvas.addEventListener('mousemove', e => {
        if (map2dState.dragging) {
          map2dState.offsetX += e.clientX - map2dState.lastX;
          map2dState.offsetY += e.clientY - map2dState.lastY;
          map2dState.lastX = e.clientX;
          map2dState.lastY = e.clientY;
          render2DMap();
        } else {
          on2DMouseMove(e);
        }
      });
      canvas.addEventListener('mouseup', () => { map2dState.dragging = false; });
      canvas.addEventListener('mouseleave', () => { map2dState.dragging = false; hideTooltip(); });
      canvas.addEventListener('wheel', e => {
        e.preventDefault();
        const zoomFactor = e.deltaY > 0 ? 0.9 : 1.1;
        const rect = canvas.getBoundingClientRect();
        const mx = e.clientX - rect.left;
        const my = e.clientY - rect.top;
        map2dState.offsetX = mx - (mx - map2dState.offsetX) * zoomFactor;
        map2dState.offsetY = my - (my - map2dState.offsetY) * zoomFactor;
        map2dState.zoom *= zoomFactor;
        render2DMap();
      }, { passive: false });
      canvas.addEventListener('click', on2DClick);
    }

    function render2DMap() {
      const canvas = el.map2dCanvas;
      const rect = el.mapWrap.getBoundingClientRect();
      const W = rect.width;
      const H = rect.height;
      canvas.width = W * window.devicePixelRatio;
      canvas.height = H * window.devicePixelRatio;
      canvas.style.width = W + 'px';
      canvas.style.height = H + 'px';
      const ctx = canvas.getContext('2d');
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);

      // Dark background
      ctx.fillStyle = '#0d1117';
      ctx.fillRect(0, 0, W, H);

      if (!D) return;

      // Compute all points
      allPoints2D = [];
      const allMembers = [];
      D.pairs.forEach(p => p.members.forEach(m => allMembers.push(m)));
      D.unmatched.forEach(u => allMembers.push(u));

      const xs = allMembers.map(m => m.plot_x);
      const ys = allMembers.map(m => m.plot_y);
      const minX = Math.min(...xs), maxX = Math.max(...xs);
      const minY = Math.min(...ys), maxY = Math.max(...ys);
      const rangeX = maxX - minX || 1;
      const rangeY = maxY - minY || 1;
      const pad = 60;

      function toScreen(px, py) {
        const sx = pad + ((px - minX) / rangeX) * (W - 2 * pad);
        const sy = pad + ((py - minY) / rangeY) * (H - 2 * pad);
        return {
          x: sx * map2dState.zoom + map2dState.offsetX,
          y: sy * map2dState.zoom + map2dState.offsetY
        };
      }

      // Density heatmap: bin points and draw radial gradients
      const isLarge = allMembers.length > 100;
      if (isLarge) {
        const heatCanvas = document.createElement('canvas');
        heatCanvas.width = W;
        heatCanvas.height = H;
        const hCtx = heatCanvas.getContext('2d');
        const heatR = 40 * map2dState.zoom;
        allMembers.forEach(m => {
          const { x, y } = toScreen(m.plot_x, m.plot_y);
          const grad = hCtx.createRadialGradient(x, y, 0, x, y, heatR);
          grad.addColorStop(0, 'rgba(37, 99, 235, 0.08)');
          grad.addColorStop(1, 'rgba(37, 99, 235, 0)');
          hCtx.fillStyle = grad;
          hCtx.fillRect(x - heatR, y - heatR, heatR * 2, heatR * 2);
        });
        ctx.drawImage(heatCanvas, 0, 0);
      }

      const baseR = isLarge ? Math.max(2, 4 * map2dState.zoom) : Math.max(4, 8 * map2dState.zoom);
      const activeR = baseR * 2;

      // Draw pair lines
      D.pairs.forEach(pair => {
        const ctrl = pair.members.find(m => m.assignment === 'control');
        const treat = pair.members.find(m => m.assignment === 'treatment');
        if (!ctrl || !treat) return;
        const active = pair.pair_id === state.activePairId;
        const p1 = toScreen(ctrl.plot_x, ctrl.plot_y);
        const p2 = toScreen(treat.plot_x, treat.plot_y);
        ctx.beginPath();
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
        ctx.strokeStyle = active ? 'rgba(255,255,255,0.6)' : 'rgba(80,100,130,0.12)';
        ctx.lineWidth = active ? 2 : 0.5;
        ctx.stroke();
      });

      // Draw outlier points
      D.unmatched.forEach(u => {
        const { x, y } = toScreen(u.plot_x, u.plot_y);
        ctx.beginPath();
        ctx.arc(x, y, baseR, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(220, 38, 38, 0.6)';
        ctx.fill();
        ctx.strokeStyle = 'rgba(220, 38, 38, 0.3)';
        ctx.lineWidth = 1;
        ctx.stroke();
        allPoints2D.push({ x, y, nmls: u.nmls, pairId: null, assignment: 'outlier', r: baseR });
      });

      // Draw pair points
      D.pairs.forEach(pair => {
        const active = pair.pair_id === state.activePairId;
        pair.members.forEach(m => {
          const { x, y } = toScreen(m.plot_x, m.plot_y);
          const isCtrl = m.assignment === 'control';
          const r = active ? activeR : baseR;
          ctx.beginPath();
          ctx.arc(x, y, r, 0, Math.PI * 2);
          if (active) {
            ctx.fillStyle = isCtrl ? '#34d399' : '#60a5fa';
            ctx.fill();
            ctx.strokeStyle = '#fff';
            ctx.lineWidth = 2;
            ctx.stroke();
          } else {
            ctx.fillStyle = isCtrl ? 'rgba(5, 150, 105, 0.45)' : 'rgba(37, 99, 235, 0.45)';
            ctx.fill();
          }
          allPoints2D.push({ x, y, nmls: m.nmls, pairId: pair.pair_id, assignment: m.assignment, r });
        });

        // Active pair labels
        if (active) {
          const ctrl = pair.members.find(m => m.assignment === 'control');
          const treat = pair.members.find(m => m.assignment === 'treatment');
          if (ctrl && treat) {
            const p1 = toScreen(ctrl.plot_x, ctrl.plot_y);
            const p2 = toScreen(treat.plot_x, treat.plot_y);
            // Pair label
            ctx.font = 'bold 12px Inter, sans-serif';
            ctx.fillStyle = 'rgba(255,255,255,0.7)';
            ctx.textAlign = 'center';
            ctx.fillText(`P${pair.pair_id}`, (p1.x + p2.x) / 2, (p1.y + p2.y) / 2 - activeR - 8);
            // NMLS labels
            ctx.font = 'bold 11px Inter, sans-serif';
            ctx.fillStyle = '#34d399';
            ctx.fillText(String(ctrl.nmls), p1.x, p1.y - activeR - 4);
            ctx.fillStyle = '#60a5fa';
            ctx.fillText(String(treat.nmls), p2.x, p2.y - activeR - 4);

            // Dashed ring
            const mx = (p1.x + p2.x) / 2;
            const my = (p1.y + p2.y) / 2;
            const dx = p2.x - p1.x;
            const dy = p2.y - p1.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            ctx.beginPath();
            ctx.ellipse(mx, my, dist / 2 + 16, dist / 2 + 16, 0, 0, Math.PI * 2);
            ctx.setLineDash([5, 4]);
            ctx.strokeStyle = 'rgba(255,255,255,0.15)';
            ctx.lineWidth = 1.5;
            ctx.stroke();
            ctx.setLineDash([]);
          }
        }
      });
    }

    function findNearest2D(mx, my) {
      let best = null, bestDist = Infinity;
      for (const p of allPoints2D) {
        const d = Math.sqrt((p.x - mx) ** 2 + (p.y - my) ** 2);
        if (d < p.r + 6 && d < bestDist) {
          best = p;
          bestDist = d;
        }
      }
      return best;
    }

    function on2DMouseMove(e) {
      if (currentView !== '2d') return;
      const rect = el.map2dCanvas.getBoundingClientRect();
      const mx = e.clientX - rect.left;
      const my = e.clientY - rect.top;
      const hit = findNearest2D(mx, my);
      if (hit) {
        el.map2dCanvas.style.cursor = 'pointer';
        showTooltipAt(e.clientX, e.clientY, hit.nmls);
      } else {
        el.map2dCanvas.style.cursor = 'grab';
        hideTooltip();
      }
    }

    function on2DClick(e) {
      if (currentView !== '2d') return;
      const rect = el.map2dCanvas.getBoundingClientRect();
      const mx = e.clientX - rect.left;
      const my = e.clientY - rect.top;
      const hit = findNearest2D(mx, my);
      if (hit && hit.pairId) {
        selectPair(hit.pairId);
      }
    }

    /* ═══════════════════════════════════════════════════════════
       SELECT PAIR / RENDER
    ═══════════════════════════════════════════════════════════ */
    function selectPair(pairId) {
      state.activePairId = pairId;
      const pair = getPair(pairId);
      const treat = pair.members.find(m => m.assignment === 'treatment');
      if (treat) el.nmlsInput.value = treat.nmls;
      updateNmlsPairInfo(pair);
      highlightRawRows(pair);
      render();
    }

    /* ═══════════════════════════════════════════════════════════
       DETAILS (5-column table)
    ═══════════════════════════════════════════════════════════ */
    function renderDetails() {
      const pair = getPair(state.activePairId);
      const ctrl = pair.members.find(m => m.assignment === "control");
      const treat = pair.members.find(m => m.assignment === "treatment");
      el.controlHeader.textContent = ctrl ? ctrl.nmls : 'Control';
      el.treatmentHeader.textContent = treat ? treat.nmls : 'Treatment';

      el.compareBody.innerHTML = D.match_features.map(metric => {
        const cv = Math.abs(Number(ctrl[metric]));
        const tv = Math.abs(Number(treat[metric]));
        const range = D.feature_ranges[metric];
        const rangeMax = Math.max(Math.abs(range.max), Math.abs(range.min), 1);
        const cPct = ((cv / rangeMax) * 100).toFixed(1);
        const tPct = ((tv / rangeMax) * 100).toFixed(1);
        const d = metric.includes("pct") || metric.includes("mix") ? 2 : metric.includes("production") ? 1 : 0;
        return `<tr>
          <td class="td-metric">${prettyMetric(metric)}</td>
          <td class="td-ctrl-val">${fmt(cv, d)}</td>
          <td class="td-bar td-ctrl-bar"><div class="bar-track"><div class="bar-fill" style="width:${cPct}%"></div></div></td>
          <td class="td-bar td-treat-bar"><div class="bar-track"><div class="bar-fill" style="width:${tPct}%"></div></div></td>
          <td class="td-treat-val">${fmt(tv, d)}</td>
        </tr>`;
      }).join("");
    }

    /* ═══════════════════════════════════════════════════════════
       RAW DATA TABLE
    ═══════════════════════════════════════════════════════════ */
    function buildRawTable() {
      if (!csvRows.length) return;
      const priority = ['nmls', 'assignment', 'pair_id', 'match_score', 'rank_bucket'];
      const rest = csvHeaders.filter(h => !priority.includes(h));
      const orderedCols = priority.filter(h => csvHeaders.includes(h)).concat(rest);

      const ths = orderedCols.map(h => `<th>${h}</th>`).join('');
      const trs = csvRows.map((row, ri) => {
        const nmls = row['nmls'] || '';
        const cells = orderedCols.map(h => {
          const v = row[h] || '';
          let cls = '';
          if (h === 'assignment') {
            const lv = v.toLowerCase();
            if (lv === 'control') cls = ' class="asgn-control"';
            else if (lv === 'treatment') cls = ' class="asgn-treatment"';
            else if (lv === 'outlier') cls = ' class="asgn-outlier"';
          }
          return `<td${cls}>${v}</td>`;
        }).join('');
        return `<tr data-nmls="${nmls}" data-row="${ri}" style="cursor:pointer">${cells}</tr>`;
      }).join('');
      el.rawTable.innerHTML = `<thead><tr>${ths}</tr></thead><tbody>${trs}</tbody>`;

      el.rawTable.querySelectorAll('tbody tr').forEach(tr => {
        tr.addEventListener('click', () => {
          const nmls = Number(tr.dataset.nmls);
          if (!nmls) return;
          if (treatNmlsToPair[nmls]) {
            pickNmls(nmls);
            return;
          }
          const pairId = nmlsToPair[nmls];
          if (pairId) {
            selectPair(pairId);
          }
        });
      });

      const initPair = getPair(state.activePairId);
      if (initPair) highlightRawRows(initPair);
    }

    function highlightRawRows(pair) {
      clearRawHighlights();
      if (!pair) return;
      const ctrlNmls = String(pair.control_nmls);
      const treatNmls = String(pair.treatment_nmls);
      el.rawTable.querySelectorAll('tbody tr').forEach(tr => {
        const n = tr.dataset.nmls;
        if (n === ctrlNmls) tr.classList.add('row-ctrl');
        else if (n === treatNmls) tr.classList.add('row-treat');
      });
    }

    function clearRawHighlights() {
      el.rawTable.querySelectorAll('tr.row-ctrl, tr.row-treat').forEach(tr => {
        tr.classList.remove('row-ctrl', 'row-treat');
      });
    }

    /* ═══════════════════════════════════════════════════════════
       RENDER
    ═══════════════════════════════════════════════════════════ */
    function render() {
      if (currentView === '3d') update3DMap();
      if (currentView === '2d') render2DMap();
      renderDetails();
    }
  </script>
</body>
</html>
