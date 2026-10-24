from .schemas import CustomerProfile


def rank_customers(profiles, category, hour, radius, limit=12):
    """Only notification priority changes. This function never receives a price."""
    ranked=[]
    for raw in profiles:
        c=CustomerProfile.model_validate(raw)
        if not c.notifications_opt_in or c.distance_km>radius or category not in c.interests:
            continue
        if hour not in c.preferred_hours or c.reliability<.6:
            continue
        score=.35*(1-c.distance_km/max(radius,1))+.25*c.reliability+.25*c.engagement+.15
        ranked.append({"customer_id":c.id,"score":round(score,4),"distance_km":c.distance_km,
                       "reason":"Category and start-time preference match; opted in; ranked by distance, reliability and engagement."})
    return sorted(ranked,key=lambda x:(-x["score"],x["customer_id"]))[:limit]
