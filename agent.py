"""Summarize supplied comparable-sale evidence for professional review."""
from __future__ import annotations
from statistics import median


def summarize_comparables(subject: dict, comparables: list[dict]) -> dict:
    usable = []
    for item in comparables:
        price, area = item.get("sale_price"), item.get("area_sqft")
        if price is not None and area and float(area) > 0:
            usable.append({"id": item.get("id"), "price_per_sqft": round(float(price) / float(area), 2), "sale_date": item.get("sale_date"), "distance_km": item.get("distance_km")})
    subject_area = subject.get("area_sqft")
    if not usable or not subject_area:
        return {"status": "insufficient-evidence", "usable_comparables": usable, "formal_valuation": None, "professional_review_required": True}
    rates = [item["price_per_sqft"] for item in usable]
    midpoint = median(rates)
    estimate = round(midpoint * float(subject_area), 2)
    return {"status": "evidence-summary", "median_price_per_sqft": midpoint, "indicative_range": [round(estimate * 0.9, 2), round(estimate * 1.1, 2)], "usable_comparables": usable, "limitations": ["No adjustment for condition, title, micro-location, financing, or market change."], "formal_valuation": None, "professional_review_required": True}
