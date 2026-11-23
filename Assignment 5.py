
from collections import defaultdict
import statistics

def create_basic_charts(rows):
    """Create charts supported by (station, date, pm25) daily data."""

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Charts skipped: install matplotlib using pip install matplotlib")
        return

    by_day = defaultdict(list)
    by_station = defaultdict(list)

    for station, day, value in rows:
        by_day[day].append(value)
        by_station[station].append(value)

    # Daily PM2.5 trend
    days = sorted(by_day)
    daily_means = [statistics.mean(by_day[d]) for d in days]

    plt.figure()
    plt.plot(days, daily_means, marker="o")
    plt.title("Daily Mean PM2.5 Trend")
    plt.xlabel("Date")
    plt.ylabel("PM2.5 (µg/m³)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("daily_pm25_trend.png", dpi=150)
    plt.close()

    # Station comparison
    stations = sorted(by_station)
    station_means = [statistics.mean(by_station[s]) for s in stations]

    plt.figure()
    plt.bar(stations, station_means)
    plt.title("Mean PM2.5 by Monitoring Station")
    plt.xlabel("Station")
    plt.ylabel("Mean PM2.5 (µg/m³)")
    plt.tight_layout()
    plt.savefig("station_pm25_comparison.png", dpi=150)
    plt.close()

    print("Charts created successfully!")
    print("1. daily_pm25_trend.png")
    print("2. station_pm25_comparison.png")


# Main program
if __name__ == "__main__":

    clean = [
        ("Chennai", "2026-11-20", 45),
        ("Chennai", "2026-11-21", 50),
        ("Chennai", "2026-11-22", 55),
        ("Coimbatore", "2026-11-20", 30),
        ("Coimbatore", "2026-11-21", 35),
        ("Coimbatore", "2026-11-22", 40),
        ("Madurai", "2026-11-20", 25),
        ("Madurai", "2026-11-21", 30),
        ("Madurai", "2026-11-22", 35)
    ]

    create_basic_charts(clean)
  
