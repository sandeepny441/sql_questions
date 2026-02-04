import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Page config
st.set_page_config(
    page_title="UWM vs Cotality Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for light theme
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: white;
        border-right: 1px solid #e2e8f0;
    }
    
    [data-testid="stSidebar"] .stMarkdown h1 {
        color: #1e293b;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #1e293b !important;
    }
    
    /* Metric cards */
    [data-testid="stMetric"] {
        background: white;
        padding: 1rem 1.25rem;
        border-radius: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08), 0 4px 12px rgba(0,0,0,0.04);
        border: 1px solid #e2e8f0;
    }
    
    [data-testid="stMetric"] label {
        color: #64748b !important;
        font-weight: 500;
    }
    
    [data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #1e293b !important;
        font-weight: 700;
    }
    
    /* Cards/containers */
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08), 0 4px 12px rgba(0,0,0,0.04);
        border: 1px solid #e2e8f0;
        margin-bottom: 1rem;
    }
    
    .card-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 1rem;
        padding-bottom: 0.75rem;
        border-bottom: 2px solid #e2e8f0;
    }
    
    /* Delta indicators */
    .delta-positive {
        color: #059669 !important;
        font-weight: 600;
    }
    
    .delta-negative {
        color: #dc2626 !important;
        font-weight: 600;
    }
    
    /* Performance zones */
    .zone-green {
        background: #dcfce7;
        color: #166534;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: 600;
        display: inline-block;
    }
    
    .zone-yellow {
        background: #fef3c7;
        color: #92400e;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: 600;
        display: inline-block;
    }
    
    .zone-red {
        background: #fee2e2;
        color: #991b1b;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: 600;
        display: inline-block;
    }
    
    /* Upload section */
    [data-testid="stFileUploader"] {
        background: white;
        padding: 1.5rem;
        border-radius: 16px;
        border: 2px dashed #cbd5e1;
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: #3b82f6;
    }
    
    /* Input fields */
    .stTextInput > div > div > input {
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        background: white;
    }
    
    .stSelectbox > div > div {
        border-radius: 8px;
        background: white;
    }
    
    /* Tables */
    .dataframe {
        border: none !important;
    }
    
    .dataframe th {
        background: #f1f5f9 !important;
        color: #475569 !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        font-size: 0.75rem;
        letter-spacing: 0.05em;
    }
    
    .dataframe td {
        color: #1e293b !important;
    }
    
    /* Divider */
    hr {
        border-color: #e2e8f0;
    }
    
    /* Info boxes */
    .stAlert {
        border-radius: 12px;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Header styling */
    .main-header {
        text-align: center;
        padding: 1rem 0 2rem 0;
    }
    
    .main-header h1 {
        font-size: 2.25rem;
        background: linear-gradient(135deg, #3b82f6 0%, #06b6d4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    
    .main-header p {
        color: #64748b;
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)


def format_number(num):
    """Format large numbers with K/M suffix"""
    if pd.isna(num):
        return "--"
    num = float(num)
    if abs(num) >= 1_000_000:
        return f"{num/1_000_000:,.2f}M"
    elif abs(num) >= 1_000:
        return f"{num/1_000:,.1f}K"
    return f"{num:,.0f}"


def get_zone_class(zone):
    """Get CSS class for performance zone"""
    if pd.isna(zone):
        return "zone-yellow"
    z = str(zone).lower()
    if any(x in z for x in ['green', 'high', 'good', 'excellent']):
        return "zone-green"
    elif any(x in z for x in ['red', 'low', 'poor', 'bad']):
        return "zone-red"
    return "zone-yellow"


def create_comparison_chart(row):
    """Create a bar chart comparing UWM vs Cotality"""
    metrics = ['Purchase', 'Refinance', 'Total']
    uwm_values = [
        float(row.get('purchase_uwm_from_uwm', 0) or 0),
        float(row.get('refi_uwm_from_uwm', 0) or 0),
        float(row.get('total_uwm_from_uwm', 0) or 0)
    ]
    cotality_values = [
        float(row.get('purchase_uwm_from_cotality', 0) or 0),
        float(row.get('refi_uwm_from_cotality', 0) or 0),
        float(row.get('total_uwm_from_cotality', 0) or 0)
    ]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='UWM',
        x=metrics,
        y=uwm_values,
        marker_color='#3b82f6',
        text=[format_number(v) for v in uwm_values],
        textposition='outside',
        textfont=dict(size=12, color='#1e293b')
    ))
    
    fig.add_trace(go.Bar(
        name='Cotality',
        x=metrics,
        y=cotality_values,
        marker_color='#8b5cf6',
        text=[format_number(v) for v in cotality_values],
        textposition='outside',
        textfont=dict(size=12, color='#1e293b')
    ))
    
    fig.update_layout(
        barmode='group',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family="DM Sans, sans-serif", color='#1e293b'),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            bgcolor='rgba(255,255,255,0.8)'
        ),
        margin=dict(l=40, r=40, t=60, b=40),
        yaxis=dict(
            gridcolor='#e2e8f0',
            tickformat=',',
        ),
        xaxis=dict(
            tickfont=dict(size=14)
        ),
        height=400
    )
    
    return fig


def create_delta_chart(row):
    """Create a waterfall-style delta chart"""
    metrics = ['Purchase', 'Refinance', 'Total']
    deltas = []
    
    for metric in ['purchase', 'refi', 'total']:
        uwm = float(row.get(f'{metric}_uwm_from_uwm', 0) or 0)
        cot = float(row.get(f'{metric}_uwm_from_cotality', 0) or 0)
        deltas.append(uwm - cot)
    
    colors = ['#059669' if d >= 0 else '#dc2626' for d in deltas]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=metrics,
        y=deltas,
        marker_color=colors,
        text=[f"{'+' if d >= 0 else ''}{format_number(d)}" for d in deltas],
        textposition='outside',
        textfont=dict(size=12, color='#1e293b')
    ))
    
    fig.add_hline(y=0, line_dash="dash", line_color="#94a3b8", line_width=1)
    
    fig.update_layout(
        title=dict(text="Delta (UWM - Cotality)", font=dict(size=16, color='#1e293b')),
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family="DM Sans, sans-serif", color='#1e293b'),
        margin=dict(l=40, r=40, t=60, b=40),
        yaxis=dict(
            gridcolor='#e2e8f0',
            tickformat=',',
            zeroline=False
        ),
        xaxis=dict(
            tickfont=dict(size=14)
        ),
        height=350
    )
    
    return fig


# Main app
def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>📊 UWM vs Cotality Dashboard</h1>
        <p>Data Variance Analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("## 📁 Data Upload")
        uploaded_file = st.file_uploader(
            "Upload your CSV file",
            type=['csv'],
            help="Upload the CSV file containing UWM and Cotality data"
        )
        
        st.markdown("---")
        st.markdown("## 🔍 Filters")
    
    if uploaded_file is None:
        # Show upload prompt
        st.markdown("""
        <div class="card" style="text-align: center; padding: 4rem 2rem;">
            <h2 style="color: #64748b; margin-bottom: 1rem;">👆 Upload your CSV to get started</h2>
            <p style="color: #94a3b8;">Use the sidebar to upload your data file</p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Load data
    @st.cache_data
    def load_data(file):
        df = pd.read_csv(file)
        df.columns = df.columns.str.strip().str.lower()
        return df
    
    try:
        df = load_data(uploaded_file)
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return
    
    # Sidebar filters
    with st.sidebar:
        # NMLS input with autocomplete-like behavior
        all_nmls = df['nmls'].dropna().astype(str).unique().tolist()
        
        nmls_input = st.text_input(
            "🔎 Search NMLS",
            placeholder="Type NMLS ID...",
            help="Start typing to search for an NMLS ID"
        )
        
        # Filter NMLS options based on input
        if nmls_input:
            filtered_nmls = [n for n in all_nmls if nmls_input.lower() in n.lower()]
            if filtered_nmls:
                selected_nmls = st.selectbox(
                    "Matching NMLS IDs",
                    options=[""] + filtered_nmls[:50],  # Limit to 50 matches
                    format_func=lambda x: "Select..." if x == "" else x
                )
            else:
                st.warning("No matching NMLS found")
                selected_nmls = ""
        else:
            selected_nmls = st.selectbox(
                "Or select from list",
                options=[""] + sorted(all_nmls)[:100],  # Show first 100
                format_func=lambda x: "Select NMLS..." if x == "" else x
            )
        
        st.markdown("---")
        
        # Month filter
        all_months = df['month'].dropna().astype(str).unique().tolist()
        selected_month = st.selectbox(
            "📅 Month",
            options=[""] + sorted(all_months),
            format_func=lambda x: "All Months" if x == "" else x
        )
        
        st.markdown("---")
        
        # Metric type
        metric_type = st.radio(
            "📈 Primary Metric",
            options=['purchase', 'refi', 'total'],
            format_func=lambda x: {'purchase': 'Purchase', 'refi': 'Refinance', 'total': 'Total'}[x],
            horizontal=True
        )
    
    # Filter data
    filtered_df = df.copy()
    
    if selected_nmls:
        filtered_df = filtered_df[filtered_df['nmls'].astype(str) == selected_nmls]
    
    if selected_month:
        filtered_df = filtered_df[filtered_df['month'].astype(str) == selected_month]
    
    if filtered_df.empty:
        st.warning("No data matches the selected filters. Please adjust your selection.")
        return
    
    # Get the first matching row for display
    row = filtered_df.iloc[0].to_dict()
    
    # Calculate values
    uwm_col = f'{metric_type}_uwm_from_uwm'
    cot_col = f'{metric_type}_uwm_from_cotality'
    
    uwm_val = float(row.get(uwm_col, 0) or 0)
    cot_val = float(row.get(cot_col, 0) or 0)
    delta = uwm_val - cot_val
    delta_pct = ((delta / cot_val) * 100) if cot_val != 0 else 0
    
    # Key Metrics Row
    st.markdown("### 📊 Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label=f"UWM ({metric_type.title()})",
            value=format_number(uwm_val)
        )
    
    with col2:
        st.metric(
            label=f"Cotality ({metric_type.title()})",
            value=format_number(cot_val)
        )
    
    with col3:
        st.metric(
            label="Delta",
            value=format_number(delta),
            delta=f"{delta_pct:+.1f}%"
        )
    
    with col4:
        year_total = float(row.get('year_total_uwm_from_uwm', 0) or 0)
        st.metric(
            label="Year Total (UWM)",
            value=format_number(year_total)
        )
    
    st.markdown("---")
    
    # Performance Zone
    perf_zone = row.get('performance_zone_from_uwm', '--')
    zone_class = get_zone_class(perf_zone)
    
    col_perf, col_info = st.columns([1, 3])
    with col_perf:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">🎯 Performance Zone</div>
            <div class="{zone_class}" style="font-size: 1.25rem;">
                {perf_zone if pd.notna(perf_zone) else '--'}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_info:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">ℹ️ Current Selection</div>
            <p><strong>NMLS:</strong> {selected_nmls or 'All'}</p>
            <p><strong>Month:</strong> {selected_month or 'All'}</p>
            <p><strong>Records:</strong> {len(filtered_df):,}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Charts Row
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.markdown('<div class="card"><div class="card-title">📊 UWM vs Cotality Comparison</div></div>', unsafe_allow_html=True)
        fig1 = create_comparison_chart(row)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col_chart2:
        st.markdown('<div class="card"><div class="card-title">📉 Delta Analysis</div></div>', unsafe_allow_html=True)
        fig2 = create_delta_chart(row)
        st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("---")
    
    # Detailed Comparison Table
    st.markdown("### 📋 Detailed Comparison")
    
    comparison_data = []
    for metric_name, metric_key in [('Purchase', 'purchase'), ('Refinance', 'refi'), ('Total', 'total')]:
        uwm = float(row.get(f'{metric_key}_uwm_from_uwm', 0) or 0)
        cot = float(row.get(f'{metric_key}_uwm_from_cotality', 0) or 0)
        d = uwm - cot
        d_pct = ((d / cot) * 100) if cot != 0 else 0
        
        comparison_data.append({
            'Metric': metric_name,
            'UWM Value': format_number(uwm),
            'Cotality Value': format_number(cot),
            'Delta': f"{'+' if d >= 0 else ''}{format_number(d)}",
            'Delta %': f"{d_pct:+.1f}%"
        })
    
    comparison_df = pd.DataFrame(comparison_data)
    st.dataframe(comparison_df, use_container_width=True, hide_index=True)
    
    # Others from Cotality
    st.markdown("### 📊 Others (Cotality Only)")
    
    others_data = []
    for metric_name, metric_key in [('Purchase', 'purchase'), ('Refinance', 'refi'), ('Total', 'total')]:
        val = float(row.get(f'{metric_key}_others_from_cotality', 0) or 0)
        others_data.append({
            'Metric': f"{metric_name} (Others)",
            'Value': format_number(val)
        })
    
    others_df = pd.DataFrame(others_data)
    st.dataframe(others_df, use_container_width=True, hide_index=True)
    
    # Show raw data option
    with st.expander("📄 View Raw Data"):
        st.dataframe(filtered_df, use_container_width=True)


if __name__ == "__main__":
    main()
