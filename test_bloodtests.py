import pytest


@pytest.mark.parametrize("input,expected_output", [
    (65, "Normal"),
    (50, "Borderline Low"),
    (20, "Low"),
])
def test_analyze_HDL_Normal(input, expected_output):
    from bloodtests import analyze_HDL
    result = analyze_HDL(input)

    assert result == expected_output
