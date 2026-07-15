S

# Power BI Interview Crash Course (5 Hours, Zero to Ready)

## Before You Start

Quick reality check: in 5 hours you won't become a Power BI expert, and that's fine — most entry-level interviews know you're new to the tool. What they're testing is whether you understand the core *concepts* and can talk through your reasoning. Follow the schedule below, don't skip the DAX hours (that's where most interviews focus), and try saying the definitions out loud once — explaining out loud is what makes them stick.

## Your 5-Hour Schedule

| Time   | Topic                            |
| ------ | -------------------------------- |
| Hour 1 | Power BI basics + Data modelingS |
| Hour 2 | Power Query (data prep)          |
| Hour 3 | DAX fundamentals                 |
| Hour 4 | DAX functions + practice         |
| Hour 5 | Interview Q&A + behavioral prep  |

---

## HOUR 1: Power BI Basics + Data Modeling

### What Power BI actually is (have this answer ready)

Power BI is Microsoft's business intelligence tool. It connects to data sources, lets you clean/transform that data, builds a data model with relationships, and turns it into interactive visual reports.

Three parts:

- **Power BI Desktop** – free authoring app where you build reports
- **Power BI Service** (app.powerbi.com) – cloud platform where reports get published, shared, and refreshed
- **Power BI Mobile** – view reports on your phone

Three views inside Desktop (left-hand icons):

- **Report view** – build charts/visuals
- **Data view** – see raw data in tables
- **Model view** – see and edit relationships between tables

### Star Schema (this WILL come up)

Good data models organize tables into two types:

- **Fact table** – transactional data with numbers you measure (Sales, Orders). Many rows, mostly foreign keys + numeric values.
- **Dimension table** – descriptive lookup data (Date, Product, Customer, Region). Fewer rows, used to filter/group/slice the facts.

**Classic interview question: "Why not just use one big flat table?"**
Your answer: a single flat table duplicates dimension data across every row (bad for performance and storage), makes relationships/filtering messier, and DAX is optimized to work with star schemas. Separate fact/dimension tables also keep the model smaller and easier to maintain.

### Relationships

- **Cardinality**: one-to-many (most common — one Customer, many Orders), one-to-one, many-to-many
- **Cross-filter direction**: single (filters flow one way) or both (filters flow both ways — use carefully, can cause ambiguity)
- Only **one relationship can be "active"** between two tables at a time. Inactive ones can still be used in DAX via `USERELATIONSHIP()`.

### 60-second self-test before moving on

Say out loud, no notes: what's a fact table, what's a dimension table, why does star schema beat one flat table? If you can't, reread this section — everything else builds on it.

---

## HOUR 2: Power Query (Data Prep)

### What it is

Power Query is Power BI's ETL (Extract, Transform, Load) tool, opened via **Transform Data**. Every click (remove a column, change a type, filter rows) gets recorded as a step in the **Applied Steps** panel, and generates code in a language called **M** behind the scenes. You rarely need to write M by hand as a beginner, but know it's there.

### Transformations you should be able to name and explain

- **Remove/keep columns, remove duplicates, remove errors**
- **Change data type** (text, whole number, decimal, date, etc.)
- **Split column** – by delimiter or number of characters
- **Merge queries** – joins two tables side-by-side, like a SQL JOIN. Types: Inner, Left Outer, Right Outer, Full Outer, Left Anti, Right Anti
- **Append queries** – stacks rows from multiple tables, like a SQL UNION
- **Group By** – aggregate data (sum, count, average) by a category
- **Pivot / Unpivot columns** – Unpivot comes up a lot: it turns "wide" data (a column per month) into "long" data (one Month column, one Value column), usually a required step before proper visuals or time-based DAX
- **Custom/Conditional column** – add a new column with a formula or if/then logic

### Classic interview question: "Merge vs Append — what's the difference?"

Your answer: **Merge** combines tables side-by-side by matching a key column (adds columns) — it's a join. **Append** stacks tables on top of each other (adds rows) — it's a union. Merge when you need columns from two related tables; Append when you have the same structure from different sources (e.g., 2024 sales + 2025 sales).

### Bonus concept: Query Folding

When possible, Power Query pushes your transformation steps back to the source system (e.g., SQL Server) to run there, instead of pulling raw data down and transforming it locally. This is much faster. Mentioning query folding if asked about performance is a strong signal you understand what's happening under the hood.

---

## HOUR 3: DAX Fundamentals

This is the section interviewers lean on hardest. Slow down here.

### Calculated Column vs Measure vs Calculated Table

Close to a guaranteed question. Know it cold:

|                 | Calculated Column                             | Measure                           |
| --------------- | --------------------------------------------- | --------------------------------- |
| When calculated | Row-by-row, on data refresh                   | On the fly, when a visual renders |
| Stored?         | Yes, takes up memory                          | No                                |
| Context used    | Row context                                   | Filter context                    |
| Used for        | A new row-level value to filter/sort/group by | Aggregations, KPIs, ratios        |

Rule of thumb to say in interview: **default to measures for any aggregation** — better performance, no wasted storage. Only use a calculated column when you need a new row-level value to group, filter, or sort by.

A **Calculated Table** is an entire new table generated by a DAX formula — less common, but good to know it exists.

### Row Context vs Filter Context (the concept that trips up everyone)

- **Row context** = "which row am I currently looking at?" Exists automatically in calculated columns, and inside iterator functions like `SUMX`.
- **Filter context** = "which subset of data is currently visible?" Set by slicers, visual rows/columns, report/page filters, and anything inside `CALCULATE()`.

**The one sentence to memorize**: `CALCULATE()` is the only function that can turn row context into filter context — called **context transition**. You don't need to master this deeply as a beginner, but saying that sentence confidently puts you ahead of most candidates.

### Quick self-test

Explain the calculated column vs measure table above, out loud, in your own words, before moving to Hour 4.

---

## HOUR 4: DAX Functions + Practice

### Aggregations (the basics)

`SUM()`, `AVERAGE()`, `COUNT()`, `COUNTROWS()`, `DISTINCTCOUNT()`

### CALCULATE — the most important function in DAX

```
CALCULATE(<expression>, <filter1>, <filter2>...)
```

Evaluates an expression under a modified filter context.

```
Sales Last Year = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))
```

### FILTER — returns a filtered table, usually used inside CALCULATE

```
High Value Sales = CALCULATE([Total Sales], FILTER(Sales, Sales[Amount] > 1000))
```

### ALL / ALLEXCEPT — remove filters (classic for % of total)

```
% of Total Sales = DIVIDE([Total Sales], CALCULATE([Total Sales], ALL(Sales)))
```

### RELATED / RELATEDTABLE — pull data across a relationship

`RELATED()` pulls a single value from the "one" side into a row on the "many" side.

### SUMX / AVERAGEX — iterators (row-by-row, then aggregate)

```
Profit = SUMX(Sales, Sales[Quantity] * (Sales[Price] - Sales[Cost]))
```

Use these when the calculation must happen per row before summing.

### DIVIDE — safe division

```
DIVIDE(<numerator>, <denominator>, [alternate result if error])
```

Use instead of `/` because it handles divide-by-zero gracefully instead of throwing an error.

### Time intelligence (needs a proper Date table)

`TOTALYTD()`, `SAMEPERIODLASTYEAR()`, `DATEADD()`

### Practice: say these answers out loud

1. **"What does CALCULATE do?"** → Evaluates an expression in a modified filter context based on the filter arguments you give it.
2. **"Difference between FILTER and CALCULATE?"** → FILTER returns a table of rows meeting a condition; CALCULATE changes the filter context an expression is evaluated in. FILTER is often used as an argument inside CALCULATE.
3. **"Why use DIVIDE instead of /?"** → Handles division by zero cleanly, no error thrown.
4. **"When do I need a calculated column instead of a measure?"** → When I need row-level detail to filter, sort, or group by.

---

## HOUR 5: Interview Q&A + Behavioral Prep

### Conceptual questions to have answers ready for

- **"Walk me through building a report from scratch."** → Connect to source → clean/shape in Power Query → build relationships in the model → write DAX measures → build visuals in Report view → publish to the Service.
- **"Import mode vs DirectQuery?"** → Import loads data into Power BI's in-memory engine (fast, needs scheduled refreshes to stay current). DirectQuery queries the live source every time (always current, but slower, with some DAX/modeling limits).
- **"Slicer vs filter?"** → A slicer is a visible on-report control users interact with directly; a filter (in the Filters pane) restricts a visual, page, or report but isn't necessarily shown as an interactive object.
- **"How would you handle a slow report?"** → Reduce columns/rows loaded, prefer Import over DirectQuery where possible, watch for excessive calculated columns, check query folding is happening, consider aggregation tables.
- **"Power BI vs Excel — why use it?"** → Handles much larger data volumes, built for repeatable/refreshable reporting rather than one-off analysis, better for sharing interactive dashboards across a team, proper data modeling instead of scattered spreadsheets.

### Behavioral prep (STAR method)

Structure any "tell me about a time..." answer as:

- **S**ituation – brief context
- **T**ask – what you needed to do
- **A**ction – what you specifically did
- **R**esult – the outcome, ideally with a number

Since you're new to Power BI, expect general data/analytical behavioral questions rather than Power BI–specific ones: "tell me about a time you worked with messy data," "tell me about a time you had to learn a new tool quickly," "tell me about a time you caught an error in your own work." Prep 2–3 stories (they don't have to be from a BI job) and frame them with STAR before the interview, not during it.

### Questions to ask your interviewer

- "What does the data source landscape look like — mostly one database, or lots of different systems to pull from?"
- "What does the report review/approval process look like on this team?"
- "What's the biggest data challenge the team is dealing with right now?"

---

## Final 10-Minute Review (do this right before your interview)

Run through these five out loud, no notes:

1. Fact table vs dimension table
2. Calculated column vs measure
3. What CALCULATE does
4. Merge vs Append in Power Query
5. Import vs DirectQuery

If you can say all five clearly, you're in good shape.
