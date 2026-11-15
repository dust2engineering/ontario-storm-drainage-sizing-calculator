#!/usr/bin/env python3
"""Ontario storm drainage sizing (OBC 7.4.10.9 / 7.4.10.11)."""
import argparse, json, os
D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "storm-data.json")))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--area", type=float, required=True, help="roof area served, m2")
    p.add_argument("--rain-mm", type=float, default=28, help="SB-1 maximum 15-minute rainfall, mm")
    p.add_argument("--slope", default="1:100", choices=D["storm_drain_table_7.4.10.9_max_load_L_by_slope"]["slopes"])
    a = p.parse_args()
    load = a.area * a.rain_mm
    print(f"Hydraulic load: {a.area:g} m2 x {a.rain_mm:g} mm = {load:,.0f} L")
    for size, cap in D["leader_table_7.4.10.11_max_load_L_circular"].items():
        if cap >= load:
            print(f"Leader (Table 7.4.10.11): minimum NPS {size} (capacity {cap:,} L)"); break
    else:
        print("Leader: exceeds NPS 8 table value - split the roof between more leaders")
    idx = D["storm_drain_table_7.4.10.9_max_load_L_by_slope"]["slopes"].index(a.slope)
    for size, caps in D["storm_drain_table_7.4.10.9_max_load_L_by_slope"]["rows"].items():
        cap = caps[idx]
        if cap is not None and cap >= load:
            print(f"Storm building drain at slope {a.slope} (Table 7.4.10.9): minimum NPS {size} (capacity {cap:,} L)"); break
    else:
        print(f"Storm building drain at slope {a.slope}: exceeds the table - increase slope or split the load")
    print("Preliminary only - verify against the OBC in force.")

if __name__ == "__main__":
    main()
