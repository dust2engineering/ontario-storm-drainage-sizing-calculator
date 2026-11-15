# Ontario Storm Drainage Sizing Calculator

Computes the storm hydraulic load in litres (roof area x SB-1 maximum 15-minute rainfall) and selects the minimum leader size (Table 7.4.10.11) and storm building drain size by slope (Table 7.4.10.9) from the 2024 Ontario Building Code, Part 7.

**Live web tool:** https://dust2engineering.github.io/ontario-storm-drainage-sizing-calculator/web/

## How it works

- Load (L) = roof area (m2) x 15-minute rainfall (mm); 1 mm on 1 m2 is 1 litre.
- Take the smallest pipe whose table capacity is not less than the load.

## Data in this repository

- storm-data.json — both tables and the load formula, machine-readable.

## Command line

```bash
python3 storm_drainage.py --area 600 --rain-mm 28 --slope 1:100
```

## Worked examples

- [plaza-roof-600m2.md](examples/plaza-roof-600m2.md)
- [restaurant-roof-250m2.md](examples/restaurant-roof-250m2.md)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Plumbing. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
