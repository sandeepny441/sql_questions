<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UWM vs Cotality Delta Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-primary: #0a0e17;
            --bg-secondary: #111827;
            --bg-card: #1a2234;
            --bg-card-hover: #1f2a42;
            --accent-blue: #3b82f6;
            --accent-cyan: #06b6d4;
            --accent-emerald: #10b981;
            --accent-amber: #f59e0b;
            --accent-rose: #f43f5e;
            --accent-violet: #8b5cf6;
            --text-primary: #f1f5f9;
            --text-secondary: #94a3b8;
            --text-muted: #64748b;
            --border-color: #2d3a52;
            --gradient-1: linear-gradient(135deg, #3b82f6 0%, #06b6d4 100%);
            --gradient-2: linear-gradient(135deg, #8b5cf6 0%, #f43f5e 100%);
            --gradient-3: linear-gradient(135deg, #10b981 0%, #3b82f6 100%);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'DM Sans', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            overflow-x: hidden;
        }

        /* Animated background */
        .bg-pattern {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            pointer-events: none;
            opacity: 0.4;
            background: 
                radial-gradient(ellipse 80% 50% at 20% -10%, rgba(59, 130, 246, 0.15) 0%, transparent 50%),
                radial-gradient(ellipse 60% 40% at 80% 100%, rgba(6, 182, 212, 0.1) 0%, transparent 50%),
                radial-gradient(ellipse 50% 30% at 50% 50%, rgba(139, 92, 246, 0.05) 0%, transparent 50%);
        }

        .grid-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            pointer-events: none;
            background-image: 
                linear-gradient(rgba(59, 130, 246, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(59, 130, 246, 0.03) 1px, transparent 1px);
            background-size: 60px 60px;
        }

        .container {
            position: relative;
            z-index: 1;
            max-width: 1600px;
            margin: 0 auto;
            padding: 2rem;
        }

        /* Header */
        header {
            text-align: center;
            margin-bottom: 3rem;
            padding: 2rem 0;
        }

        .logo-container {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 1rem;
        }

        .logo-icon {
            width: 56px;
            height: 56px;
            background: var(--gradient-1);
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Space Mono', monospace;
            font-weight: 700;
            font-size: 1.5rem;
            box-shadow: 0 8px 32px rgba(59, 130, 246, 0.3);
        }

        h1 {
            font-size: 2.5rem;
            font-weight: 700;
            background: var(--gradient-1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -0.02em;
        }

        .subtitle {
            color: var(--text-secondary);
            font-size: 1.1rem;
            margin-top: 0.5rem;
        }

        /* Upload Section */
        .upload-section {
            background: var(--bg-card);
            border: 2px dashed var(--border-color);
            border-radius: 20px;
            padding: 3rem;
            text-align: center;
            margin-bottom: 2rem;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }

        .upload-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: var(--gradient-1);
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .upload-section:hover {
            border-color: var(--accent-blue);
            transform: translateY(-2px);
        }

        .upload-section:hover::before {
            opacity: 0.05;
        }

        .upload-section.dragover {
            border-color: var(--accent-cyan);
            background: rgba(6, 182, 212, 0.1);
        }

        .upload-section.has-file {
            border-style: solid;
            border-color: var(--accent-emerald);
        }

        .upload-icon {
            width: 80px;
            height: 80px;
            margin: 0 auto 1.5rem;
            background: var(--bg-secondary);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            z-index: 1;
        }

        .upload-icon svg {
            width: 36px;
            height: 36px;
            stroke: var(--accent-blue);
        }

        .upload-text {
            position: relative;
            z-index: 1;
        }

        .upload-text h3 {
            font-size: 1.25rem;
            margin-bottom: 0.5rem;
        }

        .upload-text p {
            color: var(--text-muted);
            font-size: 0.9rem;
        }

        .upload-text .file-name {
            color: var(--accent-emerald);
            font-family: 'Space Mono', monospace;
            font-size: 0.875rem;
            margin-top: 1rem;
            padding: 0.5rem 1rem;
            background: rgba(16, 185, 129, 0.1);
            border-radius: 8px;
            display: inline-block;
        }

        #fileInput {
            display: none;
        }

        /* Filters Section */
        .filters-section {
            display: none;
            background: var(--bg-card);
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 2rem;
            border: 1px solid var(--border-color);
            animation: slideDown 0.4s ease;
        }

        @keyframes slideDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .filters-section.active {
            display: block;
        }

        .filters-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
        }

        .filter-group {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }

        .filter-group label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: var(--text-muted);
            font-weight: 500;
        }

        .filter-group select {
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 0.875rem 1rem;
            color: var(--text-primary);
            font-family: 'DM Sans', sans-serif;
            font-size: 0.95rem;
            cursor: pointer;
            transition: all 0.2s ease;
            appearance: none;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%2394a3b8' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 0.75rem center;
            background-size: 18px;
            padding-right: 2.5rem;
        }

        .filter-group select:hover {
            border-color: var(--accent-blue);
        }

        .filter-group select:focus {
            outline: none;
            border-color: var(--accent-blue);
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
        }

        /* Dashboard Section */
        .dashboard-section {
            display: none;
            animation: fadeIn 0.5s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .dashboard-section.active {
            display: block;
        }

        /* Stats Cards */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }

        .stat-card {
            background: var(--bg-card);
            border-radius: 20px;
            padding: 1.75rem;
            border: 1px solid var(--border-color);
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }

        .stat-card:hover {
            transform: translateY(-4px);
            border-color: var(--accent-blue);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }

        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
        }

        .stat-card.uwm::before {
            background: var(--gradient-1);
        }

        .stat-card.cotality::before {
            background: var(--gradient-2);
        }

        .stat-card.delta::before {
            background: var(--gradient-3);
        }

        .stat-card.performance::before {
            background: linear-gradient(135deg, var(--accent-amber) 0%, var(--accent-rose) 100%);
        }

        .stat-header {
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            margin-bottom: 1rem;
        }

        .stat-label {
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--text-muted);
            font-weight: 500;
        }

        .stat-icon {
            width: 40px;
            height: 40px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .stat-card.uwm .stat-icon {
            background: rgba(59, 130, 246, 0.15);
            color: var(--accent-blue);
        }

        .stat-card.cotality .stat-icon {
            background: rgba(139, 92, 246, 0.15);
            color: var(--accent-violet);
        }

        .stat-card.delta .stat-icon {
            background: rgba(16, 185, 129, 0.15);
            color: var(--accent-emerald);
        }

        .stat-card.performance .stat-icon {
            background: rgba(245, 158, 11, 0.15);
            color: var(--accent-amber);
        }

        .stat-value {
            font-size: 2.25rem;
            font-weight: 700;
            font-family: 'Space Mono', monospace;
            margin-bottom: 0.25rem;
            line-height: 1.1;
        }

        .stat-card.uwm .stat-value {
            color: var(--accent-blue);
        }

        .stat-card.cotality .stat-value {
            color: var(--accent-violet);
        }

        .stat-card.delta .stat-value {
            color: var(--accent-emerald);
        }

        .stat-card.delta .stat-value.negative {
            color: var(--accent-rose);
        }

        .stat-card.performance .stat-value {
            color: var(--accent-amber);
        }

        .stat-sublabel {
            font-size: 0.85rem;
            color: var(--text-secondary);
        }

        /* Comparison Panel */
        .comparison-panel {
            background: var(--bg-card);
            border-radius: 20px;
            padding: 2rem;
            border: 1px solid var(--border-color);
            margin-bottom: 2rem;
        }

        .panel-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid var(--border-color);
        }

        .panel-title {
            font-size: 1.25rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .panel-title::before {
            content: '';
            width: 4px;
            height: 24px;
            background: var(--gradient-1);
            border-radius: 2px;
        }

        /* Comparison Table */
        .comparison-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
        }

        .comparison-table th {
            text-align: left;
            padding: 1rem;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--text-muted);
            font-weight: 500;
            background: var(--bg-secondary);
            border-bottom: 1px solid var(--border-color);
        }

        .comparison-table th:first-child {
            border-radius: 12px 0 0 0;
        }

        .comparison-table th:last-child {
            border-radius: 0 12px 0 0;
        }

        .comparison-table td {
            padding: 1rem;
            border-bottom: 1px solid var(--border-color);
            font-family: 'Space Mono', monospace;
            font-size: 0.95rem;
        }

        .comparison-table tr:last-child td {
            border-bottom: none;
        }

        .comparison-table tr:last-child td:first-child {
            border-radius: 0 0 0 12px;
        }

        .comparison-table tr:last-child td:last-child {
            border-radius: 0 0 12px 0;
        }

        .comparison-table tbody tr {
            transition: background 0.2s ease;
        }

        .comparison-table tbody tr:hover {
            background: var(--bg-card-hover);
        }

        .delta-positive {
            color: var(--accent-emerald);
        }

        .delta-negative {
            color: var(--accent-rose);
        }

        .delta-neutral {
            color: var(--text-muted);
        }

        /* Delta Bar */
        .delta-bar-container {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .delta-bar {
            flex: 1;
            height: 8px;
            background: var(--bg-secondary);
            border-radius: 4px;
            overflow: hidden;
            position: relative;
        }

        .delta-bar-fill {
            height: 100%;
            border-radius: 4px;
            transition: width 0.5s ease;
        }

        .delta-bar-fill.positive {
            background: var(--gradient-3);
        }

        .delta-bar-fill.negative {
            background: linear-gradient(135deg, var(--accent-rose) 0%, var(--accent-amber) 100%);
        }

        /* Chart Section */
        .chart-section {
            background: var(--bg-card);
            border-radius: 20px;
            padding: 2rem;
            border: 1px solid var(--border-color);
            margin-bottom: 2rem;
        }

        .chart-container {
            height: 300px;
            position: relative;
            margin-top: 1rem;
        }

        .bar-chart {
            display: flex;
            align-items: flex-end;
            justify-content: space-around;
            height: 100%;
            gap: 2rem;
            padding: 0 1rem;
        }

        .bar-group {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.75rem;
            flex: 1;
            max-width: 150px;
        }

        .bars-wrapper {
            display: flex;
            align-items: flex-end;
            gap: 8px;
            height: 220px;
        }

        .bar {
            width: 40px;
            border-radius: 8px 8px 0 0;
            transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            cursor: pointer;
        }

        .bar:hover {
            filter: brightness(1.2);
            transform: scaleY(1.02);
            transform-origin: bottom;
        }

        .bar.uwm {
            background: var(--gradient-1);
        }

        .bar.cotality {
            background: var(--gradient-2);
        }

        .bar-label {
            font-size: 0.8rem;
            color: var(--text-secondary);
            text-align: center;
            max-width: 100px;
            word-wrap: break-word;
        }

        .chart-legend {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 1.5rem;
            padding-top: 1rem;
            border-top: 1px solid var(--border-color);
        }

        .legend-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.875rem;
            color: var(--text-secondary);
        }

        .legend-color {
            width: 16px;
            height: 16px;
            border-radius: 4px;
        }

        .legend-color.uwm {
            background: var(--gradient-1);
        }

        .legend-color.cotality {
            background: var(--gradient-2);
        }

        /* Year Total & Performance Cards */
        .info-cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }

        .info-card {
            background: var(--bg-card);
            border-radius: 20px;
            padding: 2rem;
            border: 1px solid var(--border-color);
        }

        .info-card-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }

        .info-card-icon {
            width: 48px;
            height: 48px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
        }

        .info-card.year-total .info-card-icon {
            background: rgba(6, 182, 212, 0.15);
            color: var(--accent-cyan);
        }

        .info-card.performance .info-card-icon {
            background: rgba(245, 158, 11, 0.15);
            color: var(--accent-amber);
        }

        .info-card-title {
            font-size: 1rem;
            font-weight: 600;
        }

        .info-card-subtitle {
            font-size: 0.8rem;
            color: var(--text-muted);
        }

        .info-card-value {
            font-size: 3rem;
            font-weight: 700;
            font-family: 'Space Mono', monospace;
            margin-bottom: 0.5rem;
        }

        .info-card.year-total .info-card-value {
            background: linear-gradient(135deg, var(--accent-cyan) 0%, var(--accent-blue) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .performance-zone {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.75rem 1.25rem;
            border-radius: 12px;
            font-weight: 600;
            font-size: 1.1rem;
        }

        .performance-zone.green {
            background: rgba(16, 185, 129, 0.15);
            color: var(--accent-emerald);
        }

        .performance-zone.yellow {
            background: rgba(245, 158, 11, 0.15);
            color: var(--accent-amber);
        }

        .performance-zone.red {
            background: rgba(244, 63, 94, 0.15);
            color: var(--accent-rose);
        }

        /* No Data State */
        .no-data {
            text-align: center;
            padding: 4rem 2rem;
            color: var(--text-muted);
        }

        .no-data svg {
            width: 64px;
            height: 64px;
            margin-bottom: 1rem;
            opacity: 0.5;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .container {
                padding: 1rem;
            }

            h1 {
                font-size: 1.75rem;
            }

            .filters-grid {
                grid-template-columns: 1fr;
            }

            .stats-grid {
                grid-template-columns: 1fr;
            }

            .bar-chart {
                flex-wrap: wrap;
            }

            .info-cards-grid {
                grid-template-columns: 1fr;
            }
        }

        /* Tooltip */
        .tooltip {
            position: absolute;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 0.75rem 1rem;
            font-size: 0.85rem;
            pointer-events: none;
            z-index: 100;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
            opacity: 0;
            transition: opacity 0.2s ease;
        }

        .tooltip.visible {
            opacity: 1;
        }
    </style>
</head>
<body>
    <div class="bg-pattern"></div>
    <div class="grid-overlay"></div>

    <div class="container">
        <header>
            <div class="logo-container">
                <div class="logo-icon">Δ</div>
            </div>
            <h1>UWM vs Cotality</h1>
            <p class="subtitle">Data Variance Analysis Dashboard</p>
        </header>

        <!-- Upload Section -->
        <div class="upload-section" id="uploadSection">
            <input type="file" id="fileInput" accept=".csv">
            <div class="upload-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                    <polyline points="17 8 12 3 7 8"/>
                    <line x1="12" y1="3" x2="12" y2="15"/>
                </svg>
            </div>
            <div class="upload-text">
                <h3>Drop your CSV file here</h3>
                <p>or click to browse</p>
                <span class="file-name" id="fileName" style="display: none;"></span>
            </div>
        </div>

        <!-- Filters Section -->
        <div class="filters-section" id="filtersSection">
            <div class="filters-grid">
                <div class="filter-group">
                    <label>NMLS ID</label>
                    <select id="nmlsSelect">
                        <option value="">Select NMLS...</option>
                    </select>
                </div>
                <div class="filter-group">
                    <label>Month</label>
                    <select id="monthSelect">
                        <option value="">Select Month...</option>
                    </select>
                </div>
                <div class="filter-group">
                    <label>Metric Type</label>
                    <select id="metricSelect">
                        <option value="purchase">Purchase</option>
                        <option value="refi">Refinance</option>
                        <option value="total">Total</option>
                    </select>
                </div>
            </div>
        </div>

        <!-- Dashboard Section -->
        <div class="dashboard-section" id="dashboardSection">
            <!-- Stats Grid -->
            <div class="stats-grid" id="statsGrid">
                <div class="stat-card uwm">
                    <div class="stat-header">
                        <span class="stat-label">UWM Reported</span>
                        <div class="stat-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M12 20V10"/>
                                <path d="M18 20V4"/>
                                <path d="M6 20v-4"/>
                            </svg>
                        </div>
                    </div>
                    <div class="stat-value" id="uwmValue">--</div>
                    <div class="stat-sublabel" id="uwmLabel">Select filters to view</div>
                </div>
                <div class="stat-card cotality">
                    <div class="stat-header">
                        <span class="stat-label">Cotality Reported</span>
                        <div class="stat-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M3 3v18h18"/>
                                <path d="m19 9-5 5-4-4-3 3"/>
                            </svg>
                        </div>
                    </div>
                    <div class="stat-value" id="cotValue">--</div>
                    <div class="stat-sublabel" id="cotLabel">Select filters to view</div>
                </div>
                <div class="stat-card delta">
                    <div class="stat-header">
                        <span class="stat-label">Delta (UWM - Cotality)</span>
                        <div class="stat-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="m21 21-6-6m6 6v-4.8m0 4.8h-4.8"/>
                                <path d="M3 16.2V21m0 0h4.8M3 21l6-6"/>
                                <path d="M21 7.8V3m0 0h-4.8M21 3l-6 6"/>
                                <path d="M3 7.8V3m0 0h4.8M3 3l6 6"/>
                            </svg>
                        </div>
                    </div>
                    <div class="stat-value" id="deltaValue">--</div>
                    <div class="stat-sublabel" id="deltaLabel">Variance amount</div>
                </div>
                <div class="stat-card performance">
                    <div class="stat-header">
                        <span class="stat-label">Delta %</span>
                        <div class="stat-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <line x1="12" x2="12" y1="2" y2="22"/>
                                <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
                            </svg>
                        </div>
                    </div>
                    <div class="stat-value" id="deltaPercent">--</div>
                    <div class="stat-sublabel">Percentage difference</div>
                </div>
            </div>

            <!-- Comparison Chart -->
            <div class="chart-section">
                <div class="panel-header">
                    <span class="panel-title">Visual Comparison</span>
                </div>
                <div class="chart-container">
                    <div class="bar-chart" id="barChart"></div>
                </div>
                <div class="chart-legend">
                    <div class="legend-item">
                        <div class="legend-color uwm"></div>
                        <span>UWM Data</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-color cotality"></div>
                        <span>Cotality Data</span>
                    </div>
                </div>
            </div>

            <!-- Year Total & Performance Zone -->
            <div class="info-cards-grid">
                <div class="info-card year-total">
                    <div class="info-card-header">
                        <div class="info-card-icon">📊</div>
                        <div>
                            <div class="info-card-title">Year Total (UWM)</div>
                            <div class="info-card-subtitle">Cumulative yearly volume</div>
                        </div>
                    </div>
                    <div class="info-card-value" id="yearTotalValue">--</div>
                </div>
                <div class="info-card performance">
                    <div class="info-card-header">
                        <div class="info-card-icon">🎯</div>
                        <div>
                            <div class="info-card-title">Performance Zone</div>
                            <div class="info-card-subtitle">Current standing</div>
                        </div>
                    </div>
                    <div class="performance-zone" id="performanceZone">--</div>
                </div>
            </div>

            <!-- Detailed Comparison Table -->
            <div class="comparison-panel">
                <div class="panel-header">
                    <span class="panel-title">Detailed Breakdown</span>
                </div>
                <table class="comparison-table">
                    <thead>
                        <tr>
                            <th>Metric</th>
                            <th>UWM Value</th>
                            <th>Cotality Value</th>
                            <th>Delta</th>
                            <th>Variance</th>
                        </tr>
                    </thead>
                    <tbody id="comparisonTable">
                        <!-- Populated by JS -->
                    </tbody>
                </table>
            </div>

            <!-- Others from Cotality Section -->
            <div class="comparison-panel">
                <div class="panel-header">
                    <span class="panel-title">Others (Cotality Only)</span>
                </div>
                <table class="comparison-table">
                    <thead>
                        <tr>
                            <th>Metric</th>
                            <th>Value</th>
                        </tr>
                    </thead>
                    <tbody id="othersTable">
                        <!-- Populated by JS -->
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <div class="tooltip" id="tooltip"></div>

    <script>
        // Global state
        let csvData = [];
        let currentRow = null;

        // DOM Elements
        const uploadSection = document.getElementById('uploadSection');
        const fileInput = document.getElementById('fileInput');
        const fileName = document.getElementById('fileName');
        const filtersSection = document.getElementById('filtersSection');
        const dashboardSection = document.getElementById('dashboardSection');
        const nmlsSelect = document.getElementById('nmlsSelect');
        const monthSelect = document.getElementById('monthSelect');
        const metricSelect = document.getElementById('metricSelect');

        // Upload handlers
        uploadSection.addEventListener('click', () => fileInput.click());
        uploadSection.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadSection.classList.add('dragover');
        });
        uploadSection.addEventListener('dragleave', () => {
            uploadSection.classList.remove('dragover');
        });
        uploadSection.addEventListener('drop', (e) => {
            e.preventDefault();
            uploadSection.classList.remove('dragover');
            const file = e.dataTransfer.files[0];
            if (file && file.name.endsWith('.csv')) {
                processFile(file);
            }
        });
        fileInput.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (file) processFile(file);
        });

        function processFile(file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                const text = e.target.result;
                csvData = parseCSV(text);
                
                uploadSection.classList.add('has-file');
                fileName.textContent = `✓ ${file.name}`;
                fileName.style.display = 'inline-block';
                
                populateFilters();
                filtersSection.classList.add('active');
            };
            reader.readAsText(file);
        }

        function parseCSV(text) {
            const lines = text.trim().split('\n');
            const headers = lines[0].split(',').map(h => h.trim().toLowerCase().replace(/"/g, ''));
            const data = [];
            
            for (let i = 1; i < lines.length; i++) {
                const values = lines[i].split(',').map(v => v.trim().replace(/"/g, ''));
                const row = {};
                headers.forEach((header, index) => {
                    row[header] = values[index];
                });
                data.push(row);
            }
            return data;
        }

        function populateFilters() {
            // Get unique NMLS values
            const nmlsValues = [...new Set(csvData.map(row => row.nmls))].filter(Boolean).sort();
            nmlsSelect.innerHTML = '<option value="">All NMLS</option>';
            nmlsValues.forEach(nmls => {
                nmlsSelect.innerHTML += `<option value="${nmls}">${nmls}</option>`;
            });

            // Get unique months
            const months = [...new Set(csvData.map(row => row.month))].filter(Boolean).sort();
            monthSelect.innerHTML = '<option value="">All Months</option>';
            months.forEach(month => {
                monthSelect.innerHTML += `<option value="${month}">${month}</option>`;
            });
        }

        // Filter change handlers
        [nmlsSelect, monthSelect, metricSelect].forEach(select => {
            select.addEventListener('change', updateDashboard);
        });

        function updateDashboard() {
            const nmls = nmlsSelect.value;
            const month = monthSelect.value;
            const metric = metricSelect.value;

            if (!nmls && !month) {
                dashboardSection.classList.remove('active');
                return;
            }

            // Filter data
            let filteredData = csvData;
            if (nmls) {
                filteredData = filteredData.filter(row => row.nmls === nmls);
            }
            if (month) {
                filteredData = filteredData.filter(row => row.month === month);
            }

            if (filteredData.length === 0) {
                dashboardSection.classList.remove('active');
                return;
            }

            currentRow = filteredData[0];
            dashboardSection.classList.add('active');

            // Get column names based on metric
            const uwmCol = `${metric}_uwm_from_uwm`;
            const cotCol = `${metric}_uwm_from_cotality`;
            const othersCol = `${metric}_others_from_cotality`;

            const uwmVal = parseFloat(currentRow[uwmCol]) || 0;
            const cotVal = parseFloat(currentRow[cotCol]) || 0;
            const delta = uwmVal - cotVal;
            const deltaPercent = cotVal !== 0 ? ((delta / cotVal) * 100).toFixed(1) : 0;

            // Update stats cards
            document.getElementById('uwmValue').textContent = formatNumber(uwmVal);
            document.getElementById('uwmLabel').textContent = getMetricLabel(metric) + ' (UWM)';
            
            document.getElementById('cotValue').textContent = formatNumber(cotVal);
            document.getElementById('cotLabel').textContent = getMetricLabel(metric) + ' (Cotality)';
            
            const deltaEl = document.getElementById('deltaValue');
            deltaEl.textContent = (delta >= 0 ? '+' : '') + formatNumber(delta);
            deltaEl.className = 'stat-value ' + (delta >= 0 ? '' : 'negative');
            
            const deltaPercentEl = document.getElementById('deltaPercent');
            deltaPercentEl.textContent = (deltaPercent >= 0 ? '+' : '') + deltaPercent + '%';

            // Update year total
            const yearTotal = parseFloat(currentRow['year_total_uwm_from_uwm']) || 0;
            document.getElementById('yearTotalValue').textContent = formatNumber(yearTotal);

            // Update performance zone
            const perfZone = currentRow['performance_zone_from_uwm'] || '--';
            const perfEl = document.getElementById('performanceZone');
            perfEl.textContent = perfZone;
            perfEl.className = 'performance-zone ' + getZoneClass(perfZone);

            // Update bar chart
            updateBarChart(uwmVal, cotVal, metric);

            // Update comparison table
            updateComparisonTable();

            // Update others table
            updateOthersTable();
        }

        function updateBarChart(uwmVal, cotVal, metric) {
            const chart = document.getElementById('barChart');
            const maxVal = Math.max(uwmVal, cotVal, 1);
            
            chart.innerHTML = `
                <div class="bar-group">
                    <div class="bars-wrapper">
                        <div class="bar uwm" style="height: ${(uwmVal / maxVal) * 200}px" data-value="${formatNumber(uwmVal)}"></div>
                        <div class="bar cotality" style="height: ${(cotVal / maxVal) * 200}px" data-value="${formatNumber(cotVal)}"></div>
                    </div>
                    <div class="bar-label">${getMetricLabel(metric)}</div>
                </div>
            `;

            // Also show purchase, refi, total side by side
            const metrics = ['purchase', 'refi', 'total'];
            let allData = [];
            
            metrics.forEach(m => {
                const uwm = parseFloat(currentRow[`${m}_uwm_from_uwm`]) || 0;
                const cot = parseFloat(currentRow[`${m}_uwm_from_cotality`]) || 0;
                allData.push({ metric: m, uwm, cot });
            });

            const globalMax = Math.max(...allData.flatMap(d => [d.uwm, d.cot]), 1);
            
            chart.innerHTML = allData.map(d => `
                <div class="bar-group">
                    <div class="bars-wrapper">
                        <div class="bar uwm" style="height: ${(d.uwm / globalMax) * 200}px" 
                             onmouseenter="showTooltip(event, 'UWM: ${formatNumber(d.uwm)}')"
                             onmouseleave="hideTooltip()"></div>
                        <div class="bar cotality" style="height: ${(d.cot / globalMax) * 200}px"
                             onmouseenter="showTooltip(event, 'Cotality: ${formatNumber(d.cot)}')"
                             onmouseleave="hideTooltip()"></div>
                    </div>
                    <div class="bar-label">${getMetricLabel(d.metric)}</div>
                </div>
            `).join('');
        }

        function updateComparisonTable() {
            const table = document.getElementById('comparisonTable');
            const metrics = [
                { key: 'purchase', label: 'Purchase' },
                { key: 'refi', label: 'Refinance' },
                { key: 'total', label: 'Total' }
            ];

            table.innerHTML = metrics.map(m => {
                const uwm = parseFloat(currentRow[`${m.key}_uwm_from_uwm`]) || 0;
                const cot = parseFloat(currentRow[`${m.key}_uwm_from_cotality`]) || 0;
                const delta = uwm - cot;
                const pct = cot !== 0 ? ((delta / cot) * 100).toFixed(1) : 0;
                const deltaClass = delta > 0 ? 'delta-positive' : delta < 0 ? 'delta-negative' : 'delta-neutral';
                const barWidth = Math.min(Math.abs(pct), 100);
                const barClass = delta >= 0 ? 'positive' : 'negative';

                return `
                    <tr>
                        <td>${m.label}</td>
                        <td>${formatNumber(uwm)}</td>
                        <td>${formatNumber(cot)}</td>
                        <td class="${deltaClass}">${delta >= 0 ? '+' : ''}${formatNumber(delta)}</td>
                        <td>
                            <div class="delta-bar-container">
                                <div class="delta-bar">
                                    <div class="delta-bar-fill ${barClass}" style="width: ${barWidth}%"></div>
                                </div>
                                <span class="${deltaClass}">${pct >= 0 ? '+' : ''}${pct}%</span>
                            </div>
                        </td>
                    </tr>
                `;
            }).join('');
        }

        function updateOthersTable() {
            const table = document.getElementById('othersTable');
            const metrics = [
                { key: 'purchase_others_from_cotality', label: 'Purchase (Others)' },
                { key: 'refi_others_from_cotality', label: 'Refinance (Others)' },
                { key: 'total_others_from_cotality', label: 'Total (Others)' }
            ];

            table.innerHTML = metrics.map(m => {
                const val = parseFloat(currentRow[m.key]) || 0;
                return `
                    <tr>
                        <td>${m.label}</td>
                        <td>${formatNumber(val)}</td>
                    </tr>
                `;
            }).join('');
        }

        function formatNumber(num) {
            if (num >= 1000000) {
                return (num / 1000000).toFixed(2) + 'M';
            } else if (num >= 1000) {
                return (num / 1000).toFixed(1) + 'K';
            }
            return num.toLocaleString();
        }

        function getMetricLabel(metric) {
            const labels = {
                'purchase': 'Purchase',
                'refi': 'Refinance',
                'total': 'Total'
            };
            return labels[metric] || metric;
        }

        function getZoneClass(zone) {
            const z = zone.toLowerCase();
            if (z.includes('green') || z.includes('high') || z.includes('good')) return 'green';
            if (z.includes('red') || z.includes('low') || z.includes('poor')) return 'red';
            return 'yellow';
        }

        function showTooltip(event, text) {
            const tooltip = document.getElementById('tooltip');
            tooltip.textContent = text;
            tooltip.style.left = event.pageX + 10 + 'px';
            tooltip.style.top = event.pageY - 30 + 'px';
            tooltip.classList.add('visible');
        }

        function hideTooltip() {
            document.getElementById('tooltip').classList.remove('visible');
        }
    </script>
</body>
</html>
