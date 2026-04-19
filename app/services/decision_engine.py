def decide_mastering(analysis: dict, mode: str = "human_master") -> dict:
    low = float(analysis.get("low", 0.0))
    low_mid = float(analysis.get("low_mid", 0.0))
    mid = float(analysis.get("mid", 0.0))
    high = float(analysis.get("high", 0.0))
    air = float(analysis.get("air", 0.0))
    crest = float(analysis.get("crest", 0.0))
    issues = list(analysis.get("issues", []))

    decision = {
        "preset_name": "Human Master",
        "target_lufs": -10.5,
        "tighten_low_end": False,
        "tighten_low_end_strength": "medium",
        "mud_cut_db": 0.0,
        "mud_center_hz": 280,
        "low_mid_cut_db": 0.0,
        "low_mid_center_hz": 450,
        "presence_boost_db": 0.0,
        "presence_center_hz": 3200,
        "air_shelf_db": 0.0,
        "air_start_hz": 10000,
        "use_exciter": False,
        "exciter_band": "off",
        "boost_transients": False,
        "transient_focus": "off",
        "widen_stereo": True,
        "widen_stereo_band": "high_only",
        "widen_amount": 0.10,
        "use_deharsh": False,
        "deharsh_db": 0.0,
        "deharsh_center_hz": 3500,
        "multiband_drive": "medium",
        "limiter_ceiling_dbtp": -1.0,
        "actions": [],
        "notes": [],
        "genre": "general",
    }

    low_vs_mid = low / max(mid, 1e-6)
    lowmid_vs_mid = low_mid / max(mid, 1e-6)
    high_vs_mid = high / max(mid, 1e-6)

    if low_vs_mid > 5.0:
        decision["genre"] = "club_or_dark_mix"
    elif air > high * 0.35 and crest > 5.5:
        decision["genre"] = "open_or_hifi"

    if "mud" in issues:
        decision["tighten_low_end"] = True
        decision["tighten_low_end_strength"] = "high" if low_vs_mid > 6.0 else "medium"
        decision["mud_cut_db"] = 2.4 if lowmid_vs_mid > 4.0 else 1.8
        decision["low_mid_cut_db"] = 1.2
        decision["actions"].append("Limpiar barro y ordenar low-mids")
        decision["notes"].append("Se detectó acumulación en graves/medios bajos.")

    if "lack_of_air" in issues:
        decision["air_shelf_db"] = 2.0
        decision["presence_boost_db"] = 1.0 if high_vs_mid < 0.6 else 0.6
        decision["use_exciter"] = True
        decision["exciter_band"] = "high_only"
        decision["actions"].append("Recuperar aire y presencia")
        decision["notes"].append("La mezcla está oscura y cerrada arriba.")

    if "harsh" in issues:
        decision["use_deharsh"] = True
        decision["deharsh_db"] = 1.5
        decision["actions"].append("Suavizar zona agresiva")
        decision["notes"].append("Hay dureza en presencia alta.")

    if "weak_transients" in issues or low_vs_mid > 4.0:
        decision["boost_transients"] = True
        decision["transient_focus"] = "mid_high"
        decision["actions"].append("Recuperar pegada")
        decision["notes"].append("Se reforzó ataque percibido.")

    if decision["genre"] == "club_or_dark_mix":
        decision["target_lufs"] = -9.8
        decision["multiband_drive"] = "high"
    elif decision["genre"] == "open_or_hifi":
        decision["target_lufs"] = -10.8
        decision["multiband_drive"] = "low"

    if not decision["actions"]:
        decision["actions"].append("Glue sutil y control final")
        decision["notes"].append("La mezcla llegó bastante equilibrada.")

    return decision
