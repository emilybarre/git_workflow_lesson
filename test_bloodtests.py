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

@pytest.mark.parametrize("input,expected_output", [
    (120, "Normal"),
    (135, "Borderline High"),
    (165, "High"),
    (195, "Very High"),
])
def test_analyze_LDL_Normal(input, expected_output):
    from bloodtests import analyze_LDL
    result = analyze_LDL(input)

    assert result == expected_output
