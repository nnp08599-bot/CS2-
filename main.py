import json
import sys
from pathlib import Path

from demoparser2 import DemoParser


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 main.py data/demos/match.dem")

    demo_path = Path(sys.argv[1])
    if not demo_path.exists() or demo_path.suffix.lower() != ".dem":
        raise SystemExit(f"Invalid demo file: {demo_path}")

    parser = DemoParser(str(demo_path))
    events_df = parser.parse_event("player_death")

    result = []
    for event in events_df.to_dict(orient="records"):
        result.append(
            {
                "time": float(event.get("time", event.get("tick", 0) / 128.0)),
                "attacker": str(event.get("attacker_name", event.get("attacker", ""))),
                "victim": str(
                    event.get("user_name", event.get("victim_name", event.get("victim", "")))
                ),
                "weapon": str(event.get("weapon", "")),
                "headshot": bool(event.get("headshot", False)),
            }
        )

    out_path = Path("data/out/match.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    print("done")


if __name__ == "__main__":
    main()


