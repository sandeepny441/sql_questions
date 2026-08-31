# United Wholesale Mortgage — HMDA action-taken breakdown, 2007–2025

This table counts every UWM HMDA LAR record by year and action taken. The available rebuilt dataset covers **19 years (2007–2025)**; a 20th year is not present in the supplied files.

| Year | Total records | Originated (1) | Approved, not accepted (2) | Denied (3) | Withdrawn (4) | Incomplete (5) | Purchased (6) | Preapproval denied (7) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2007 | 12,714 | 5,379 | 37 | 2,678 | 4,510 | 42 | 0 | 68 |
| 2008 | 23,593 | 11,341 | 73 | 4,532 | 7,587 | 0 | 0 | 60 |
| 2009 | 32,662 | 16,886 | 132 | 6,255 | 9,326 | 0 | 0 | 63 |
| 2010 | 19,490 | 10,504 | 44 | 3,565 | 5,371 | 0 | 0 | 6 |
| 2011 | 17,288 | 9,972 | 93 | 2,219 | 5,004 | 0 | 0 | 0 |
| 2012 | 47,572 | 35,127 | 1,968 | 5,013 | 886 | 4,578 | 0 | 0 |
| 2013 | 68,143 | 46,414 | 1,278 | 10,654 | 887 | 8,910 | 0 | 0 |
| 2014 | 52,808 | 37,720 | 1,200 | 8,448 | 276 | 5,164 | 0 | 0 |
| 2015 | 65,165 | 49,988 | 622 | 8,431 | 27 | 6,097 | 0 | 0 |
| 2016 | 102,234 | 82,643 | 856 | 9,963 | 90 | 8,682 | 0 | 0 |
| 2017 | 132,912 | 104,548 | 1,127 | 11,654 | 144 | 15,439 | 0 | 0 |
| 2018 | 182,654 | 145,888 | 1,606 | 14,311 | 40 | 20,809 | 0 | 0 |
| 2019 | 410,835 | 339,144 | 4,824 | 23,920 | 7 | 42,940 | 0 | 0 |
| 2020 | 689,666 | 560,798 | 8,838 | 40,317 | 45,580 | 33,954 | 179 | 0 |
| 2021 | 803,496 | 654,191 | 11,126 | 56,924 | 58,610 | 22,268 | 377 | 0 |
| 2022 | 462,351 | 348,415 | 5,682 | 47,895 | 43,897 | 12,815 | 3,647 | 0 |
| 2023 | 394,401 | 294,387 | 4,301 | 45,275 | 41,649 | 7,504 | 1,285 | 0 |
| 2024 | 493,978 | 366,078 | 7,692 | 57,760 | 46,939 | 13,176 | 2,333 | 0 |
| 2025 | 578,838 | 422,120 | 10,283 | 69,523 | 54,820 | 19,964 | 2,128 | 0 |

## Interpretation

- **Originated (code 1)** is UWM-reported production: the institution made the credit decision and the decision resulted in an extension of credit.
- **Purchased (code 6)** is separate acquisition/repurchase activity after closing; it is not additional originated production and should not be added to code 1 when measuring loans closed by UWM.
- Codes 2–5 are applications that did not become an originated loan. Code 7 is a denied preapproval request and appears in the older years.

UWM identifiers used: respondent ID `7184500000` (2007–2010), respondent ID `38-2750395` (2011–2017), and LEI `549300HW662MN1WU8550` (2018–2025). Source: rebuilt yearly HMDA Parquet files in `hmda_yearly_analysis_2007_to_2025`.

HMDA action-code definitions: [FFIEC 2024 HMDA Guide](https://www.ffiec.gov/sites/default/files/data/hmda/2024Guide.pdf).
