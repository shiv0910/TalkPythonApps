def main():
    d = {
        "city": "Portland",
        "state": "ME",
        "details": ["cold", "snowy", "winter"]
    }

    print(d.get("country", "USA"))
    d["country"] = "AU"
    print(d.get("country", "USA"))
    print(d)


w = {
  "weather": {
    "description": "overcast clouds",
    "category": "Clouds"
  },
  "wind": {
    "speed": 1.01,
    "deg": 270
  },
  "units": "metric",
  "forecast": {
    "temp": 52.63,
    "feels_like": 51.67,
    "pressure": 1007,
    "humidity": 87,
    "low": 49,
    "high": 55
  },
  "location": {
    "city": "Portland",
    "state": "OR",
    "country": "US"
  },
  "rate_limiting": {
    "unique_lookups_remaining": 49,
    "lookup_reset_window": "1 hour"
  }
}

print(f'{w.get("forecast").get("temp")} C')

if __name__ == "__main__":
    main()

