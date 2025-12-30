All right, okay. I will give you some code snippets, please organize them properly. 



base_months = ['Mar', 'Apr', 'May', 'Jun']

# ───────────────────────────────────────────────────────────────
# 1. Split into Purchase and Refinance
# ───────────────────────────────────────────────────────────────
df_purchase = df[df['loanPurpose'].str.contains('Purchase', case=False)].copy()
df_refi     = df[df['loanPurpose'].str.contains('Refi|Refinance', case=False)].copy()

# ───────────────────────────────────────────────────────────────
# 2. Calculate trend factors
# ───────────────────────────────────────────────────────────────

# Purchase
purchase_uwm = df_purchase[df_purchase['loanPurpose'] == 'Purchase_uwm']
purchase_base_total   = purchase_uwm[base_months].sum().sum()
purchase_recent_total = purchase_uwm['Jul'].sum() + purchase_uwm['Aug'].sum()
purchase_base_avg     = purchase_base_total / 4
purchase_recent_avg   = purchase_recent_total / 2
purchase_trend_factor = purchase_recent_avg / purchase_base_avg if purchase_base_avg != 0 else 1.0

# Refinance
refi_uwm = df_refi[df_refi['loanPurpose'] == 'Refinance_uwm']
refi_base_total   = refi_uwm[base_months].sum().sum()
refi_recent_total = refi_uwm['Jul'].sum() + refi_uwm['Aug'].sum()
refi_base_avg     = refi_base_total / 4
refi_recent_avg   = refi_recent_total / 2
refi_trend_factor = refi_recent_avg / refi_base_avg if refi_base_avg != 0 else 1.0

# ───────────────────────────────────────────────────────────────
# 3. Add trend_factor column
# ───────────────────────────────────────────────────────────────
df_purchase['trend_factor'] = purchase_trend_factor
df_refi['trend_factor']     = refi_trend_factor

# ───────────────────────────────────────────────────────────────
# 4. Add base_avg_4m (4-month average) and forecasts only for *_all rows
# ───────────────────────────────────────────────────────────────

# Purchase
purchase_all_mask = df_purchase['loanPurpose'] == 'Purchase_all'
df_purchase.loc[purchase_all_mask, 'base_avg_4m'] = df_purchase.loc[purchase_all_mask, base_months].mean(axis=1)
df_purchase.loc[purchase_all_mask, 'Jul_fcst'] = (
    df_purchase.loc[purchase_all_mask, 'base_avg_4m'] * purchase_trend_factor
).round(0).astype(int)
df_purchase.loc[purchase_all_mask, 'Aug_fcst'] = df_purchase.loc[purchase_all_mask, 'Jul_fcst']

# Refinance
refi_all_mask = df_refi['loanPurpose'] == 'Refi_all'
df_refi.loc[refi_all_mask, 'base_avg_4m'] = df_refi.loc[refi_all_mask, base_months].mean(axis=1)
df_refi.loc[refi_all_mask, 'Jul_fcst'] = (
    df_refi.loc[refi_all_mask, 'base_avg_4m'] * refi_trend_factor
).round(0).astype(int)
df_refi.loc[refi_all_mask, 'Aug_fcst'] = df_refi.loc[refi_all_mask, 'Jul_fcst']

# Fill empty cells with empty string for non-_all rows
for df_seg in [df_purchase, df_refi]:
    for col in ['base_avg_4m', 'Jul_fcst', 'Aug_fcst']:
        df_seg[col] = df_seg[col].fillna('')


df_refi


df_purchase 

----------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Assuming df_purchase and df_refi are already defined from your previous code

# Months for plotting
months = ['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']

# ───────────────────────────────────────────────────────────────
# Prepare aggregated monthly UWM data
# ───────────────────────────────────────────────────────────────

# Refinance aggregated
refi_uwm = df_refi[df_refi['loanPurpose'] == 'Refinance_uwm']
refi_monthly = refi_uwm[months].sum().values

# Purchase aggregated
purchase_uwm = df_purchase[df_purchase['loanPurpose'] == 'Purchase_uwm']
purchase_monthly = purchase_uwm[months].sum().values

# ───────────────────────────────────────────────────────────────
# Plot 1: Refinance - Vertical Bars + Trend Lines
# ───────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))

# Colors: base period (Mar-Jun) vs recent (Jul-Aug)
colors = ['#a6cee3'] * 4 + ['#fdbf6f'] * 2  # light blue for Jan-Jun, light orange for Jul-Aug

bars = ax.bar(months, refi_monthly, color=colors, edgecolor='navy', width=0.7)

# Add trend lines (averages)
ax.axhline(y=refi_base_avg,   color='darkgreen', linestyle='--', linewidth=1.5, 
           label=f'Base avg (Mar-Jun): {refi_base_avg:.1f}')
ax.axhline(y=refi_recent_avg, color='darkorange', linestyle='--', linewidth=1.5, 
           label=f'Recent avg (Jul-Aug): {refi_recent_avg:.1f}')

# Labels and formatting
ax.set_title('Aggregated UWM Refinance Volume by Month\nTrend Factor: {:.3f} ({:+.1f}%)'.format(
    refi_trend_factor, (refi_trend_factor-1)*100), fontsize=14)
ax.set_xlabel('Month')
ax.set_ylabel('Total UWM Refinance Closings')
ax.legend(loc='upper left')
ax.grid(axis='y', alpha=0.3)

# Annotate bar values
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 1, str(int(height)),
            ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

# ───────────────────────────────────────────────────────────────
# Plot 2: Purchase - Vertical Bars + Trend Lines
# ───────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(months, purchase_monthly, color=colors, edgecolor='darkgreen', width=0.7)

# Add trend lines
ax.axhline(y=purchase_base_avg,   color='darkgreen', linestyle='--', linewidth=1.5, 
           label=f'Base avg (Mar-Jun): {purchase_base_avg:.1f}')
ax.axhline(y=purchase_recent_avg, color='darkorange', linestyle='--', linewidth=1.5, 
           label=f'Recent avg (Jul-Aug): {purchase_recent_avg:.1f}')

# Labels and formatting
ax.set_title('Aggregated UWM Purchase Volume by Month\nTrend Factor: {:.3f} ({:+.1f}%)'.format(
    purchase_trend_factor, (purchase_trend_factor-1)*100), fontsize=14)
ax.set_xlabel('Month')
ax.set_ylabel('Total UWM Purchase Closings')
ax.legend(loc='upper left')
ax.grid(axis='y', alpha=0.3)

# Annotate bar values
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.1, str(int(height)),
            ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

=======================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Your DataFrame setup (copied from your code)
data = {
    'NMLS': ['7744887', '7744887', '7744887', '7744887',
             '1637367', '1637367', '1637367', '1637367'],
    'loanPurpose': ['Purchase_all', 'Purchase_uwm', 'Refi_all', 'Refinance_uwm',
                    'Purchase_all', 'Purchase_uwm', 'Refi_all', 'Refinance_uwm'],
    'Jan': [2, 1, 254, 145, 4, 1, 72, 39],
    'Feb': [6, 0, 234, 105, 6, 1, 64, 38],
    'Mar': [2, 1, 330, 152, 4, 4, 132, 49],
    'Apr': [4, 2, 268, 202, 4, 3, 146, 103],
    'May': [0, 2, 92, 89, 2, 1, 130, 61],
    'Jun': [8, 0, 54, 27, 2, 2, 98, 62],
    'Jul': [0, 1, 148, 40, 0, 1, 172, 65],
    'Aug': [0, 1, 144, 86, 2, 1, 198, 86]
}
df = pd.DataFrame(data)

base_months = ['Mar', 'Apr', 'May', 'Jun']
months_short = ['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']

# ───────────────────────────────────────────────────────────────
# Run your original calculations (necessary for forecasts & base_avg_4m)
# ───────────────────────────────────────────────────────────────
df_purchase = df[df['loanPurpose'].str.contains('Purchase', case=False)].copy()
df_refi = df[df['loanPurpose'].str.contains('Refi|Refinance', case=False)].copy()

purchase_uwm = df_purchase[df_purchase['loanPurpose'] == 'Purchase_uwm']
purchase_base_total = purchase_uwm[base_months].sum().sum()
purchase_recent_total = purchase_uwm['Jul'].sum() + purchase_uwm['Aug'].sum()
purchase_base_avg = purchase_base_total / 4
purchase_recent_avg = purchase_recent_total / 2
purchase_trend_factor = purchase_recent_avg / purchase_base_avg if purchase_base_avg != 0 else 1.0

refi_uwm = df_refi[df_refi['loanPurpose'] == 'Refinance_uwm']
refi_base_total = refi_uwm[base_months].sum().sum()
refi_recent_total = refi_uwm['Jul'].sum() + refi_uwm['Aug'].sum()
refi_base_avg = refi_base_total / 4
refi_recent_avg = refi_recent_total / 2
refi_trend_factor = refi_recent_avg / refi_base_avg if refi_base_avg != 0 else 1.0

df_purchase['trend_factor'] = purchase_trend_factor
df_refi['trend_factor'] = refi_trend_factor

purchase_all_mask = df_purchase['loanPurpose'] == 'Purchase_all'
df_purchase.loc[purchase_all_mask, 'base_avg_4m'] = df_purchase.loc[purchase_all_mask, base_months].mean(axis=1)
df_purchase.loc[purchase_all_mask, 'Jul_fcst'] = (df_purchase.loc[purchase_all_mask, 'base_avg_4m'] * purchase_trend_factor).round(0).astype(int)
df_purchase.loc[purchase_all_mask, 'Aug_fcst'] = df_purchase.loc[purchase_all_mask, 'Jul_fcst']

refi_all_mask = df_refi['loanPurpose'] == 'Refi_all'
df_refi.loc[refi_all_mask, 'base_avg_4m'] = df_refi.loc[refi_all_mask, base_months].mean(axis=1)
df_refi.loc[refi_all_mask, 'Jul_fcst'] = (df_refi.loc[refi_all_mask, 'base_avg_4m'] * refi_trend_factor).round(0).astype(int)
df_refi.loc[refi_all_mask, 'Aug_fcst'] = df_refi.loc[refi_all_mask, 'Jul_fcst']

# ───────────────────────────────────────────────────────────────
# Plot function for one NMLS ID and one segment
# ───────────────────────────────────────────────────────────────
def plot_nmls_actual_vs_forecast(nmls_id, loan_purpose, df_segment, title):
    row = df_segment[(df_segment['NMLS'] == nmls_id) & (df_segment['loanPurpose'] == loan_purpose)].iloc[0]
    
    actual_values = row[months_short].astype(float).values
    base_avg = row['base_avg_4m']
    jul_fcst = row['Jul_fcst'] if pd.notna(row['Jul_fcst']) and row['Jul_fcst'] != '' else 0
    aug_fcst = row['Aug_fcst'] if pd.notna(row['Aug_fcst']) and row['Aug_fcst'] != '' else 0
    
    x = np.arange(len(months_short))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Actual bars
    ax.bar(x[:4], actual_values[:4], width, color='#a6cee3', edgecolor='navy', label='Mar–Jun')
    ax.bar(x[4], actual_values[4], width, color='#fdbf6f', edgecolor='darkorange', label='Jul actual')
    ax.bar(x[5], actual_values[5], width, color='#fb9a99', edgecolor='darkred', label='Aug actual')
    
    # Forecast bars right next to actuals
    ax.bar(x[4] + width, [jul_fcst], width, color='teal', edgecolor='darkcyan', label='Forecast')
    ax.bar(x[5] + width, [aug_fcst], width, color='teal', edgecolor='darkcyan')
    
    # Only the 4-month base average line
    ax.axhline(y=base_avg, color='darkgreen', linestyle='--', linewidth=1.5,
               label=f'4-month avg (Mar–Jun): {base_avg:.1f}')
    
    # Formatting
    ax.set_xticks(x + width/2)
    ax.set_xticklabels(months_short)
    ax.set_title(title, fontsize=14)
    ax.set_ylabel('Closings')
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1))
    ax.grid(axis='y', alpha=0.3)
    
    # Annotate actual values
    for i, v in enumerate(actual_values):
        ax.text(i, v + max(1, v*0.05), str(int(v)), ha='center', va='bottom')
    # Annotate forecasts
    ax.text(x[4] + width, jul_fcst + max(1, jul_fcst*0.05), str(int(jul_fcst)), 
            ha='center', va='bottom', color='teal')
    ax.text(x[5] + width, aug_fcst + max(1, aug_fcst*0.05), str(int(aug_fcst)), 
            ha='center', va='bottom', color='teal')
    
    plt.tight_layout()
    plt.show()

# ───────────────────────────────────────────────────────────────
# Generate all four plots
# ───────────────────────────────────────────────────────────────
plot_nmls_actual_vs_forecast('7744887', 'Refi_all', df_refi, 'Refi_all - NMLS 7744887: Actual vs Forecast')
plot_nmls_actual_vs_forecast('1637367', 'Refi_all', df_refi, 'Refi_all - NMLS 1637367: Actual vs Forecast')
plot_nmls_actual_vs_forecast('7744887', 'Purchase_all', df_purchase, 'Purchase_all - NMLS 7744887: Actual vs Forecast')
plot_nmls_actual_vs_forecast('1637367', 'Purchase_all', df_purchase, 'Purchase_all - NMLS 1637367: Actual vs Forecast')
