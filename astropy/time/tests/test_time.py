import astropy.units as u
from astropy.coordinates import EarthLocation
from astropy.time import Time


def test_time_isclose_self_with_location():
    # Test with identical locations
    t = Time(
        "2024-01-01T00:00:00",
        scale="utc",
        location=EarthLocation(0 * u.m, 0 * u.m, 0 * u.m),
    )
    assert t.isclose(t)

    # Test with different locations within tolerance
    t1 = Time(
        "2024-01-01T00:00:00",
        scale="utc",
        location=EarthLocation(1 * u.m, 0 * u.m, 0 * u.m),
    )
    t2 = Time(
        "2024-01-01T00:00:00",
        scale="utc",
        location=EarthLocation(2 * u.m, 0 * u.m, 0 * u.m),
    )

    # Compute actual time difference
    time_difference = abs(t1 - t2)

    assert time_difference < 1.1 * u.s  # Ensure difference is within tolerance
