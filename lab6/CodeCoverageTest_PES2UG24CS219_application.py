
import pytest
from coupon_validator import coupon_discount, best_discount, is_expired


def test_empty_cart_raises_error():
    with pytest.raises(ValueError, match="empty cart"):
        coupon_discount("WELCOME10", 0, True, "mon")


def test_welcome_new_user():
    assert coupon_discount("WELCOME10", 200, True, "mon") == 20


def test_welcome_existing_user():
    assert coupon_discount("WELCOME10", 200, False, "mon") == 0


def test_weekend20_large_cart():
    assert coupon_discount("WEEKEND20", 500, False, "sat") == 100


def test_weekend20_small_cart():
    assert coupon_discount("WEEKEND20", 200, False, "sun") == 50


def test_weekend20_weekday():
    assert coupon_discount("WEEKEND20", 500, False, "mon") == 0


def test_flat100_large_cart():
    assert coupon_discount("FLAT100", 400, False, "mon") == 100


def test_flat100_small_cart():
    assert coupon_discount("FLAT100", 300, False, "mon") == 0


def test_unknown_coupon():
    assert coupon_discount("INVALID", 200, False, "mon") == 0


def test_best_discount_selects_largest():
    assert best_discount(
        ["WELCOME10", "FLAT100"], 400, True, "mon"
    ) == 100


def test_best_discount_cap():
    assert best_discount(["FLAT100"], 200, False, "mon") == 0


def test_best_discount_empty_codes():
    assert best_discount([], 200, False, "mon") == 0


def test_expiry_at_validity_boundary():
    assert is_expired(15, 10, 5) is False


def test_expiry_after_validity():
    assert is_expired(16, 10, 5) is True


def test_nonpositive_validity():
    assert is_expired(10, 5, 0) is True

def test_best_discount_below_cap():
    assert best_discount(["WELCOME10"], 200, True, "mon") == 20