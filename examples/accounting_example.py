"""Ví dụ minh họa công khai; KHÔNG phải bộ máy kế toán/backtest vận hành."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Account:
    cash_available: float
    cash_receivable: float
    etf_settled: int
    etf_receivable: int
    market_price: float

def account_nav(a: Account) -> float:
    """Ví dụ giả định tất cả ETF chờ nhận thuộc tài sản; không hạch toán nghĩa vụ mua chờ trả."""
    if min(a.cash_available, a.cash_receivable, a.etf_settled,
           a.etf_receivable, a.market_price) < 0:
        raise ValueError('Không chấp nhận tài sản âm trong ví dụ đơn giản')
    return a.cash_available + a.cash_receivable + (a.etf_settled + a.etf_receivable) * a.market_price

def executed_lot(requested: int, available: int, adv20: float,
                 lot: int = 100, limit_pct: float = .05) -> int:
    """Ví dụ tính giới hạn khối lượng; chưa tính tiền, thuế, độ sâu lệnh hoặc tín hiệu."""
    if requested < 0 or available < 0 or adv20 < 0 or lot <= 0:
        raise ValueError('Dữ liệu không hợp lệ')
    permitted = max(0, int(adv20 * limit_pct) // lot * lot)
    return (min(requested, available, permitted) // lot) * lot
