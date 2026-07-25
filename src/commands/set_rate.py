from src.storage import load_rates, save_rates


def set_rate(currency: str, rate: float) -> None:
    rates = load_rates()

    rates[currency] = rate
    save_rates(rates)
    print("Exchange rate updated successfully")
