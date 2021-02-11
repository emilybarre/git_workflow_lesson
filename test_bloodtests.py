def test_analyze_HDL_Normal():
    from bloodtests import analyze_HDL
    
    result = analyze_HDL(65)
    expected = "Normal"

    assert result == expected 
    
def test_analyze_HDL_B_Low():
    from bloodtests import analyze_HDL
    
    result = analyze_HDL(50)
    expected = "Borderline Low"
    
    assert result == expected 
    
def test_analyze_HDL_Low():
    from bloodtests import analyze_HDL
        
    result = analyze_HDL(20)
    expected = "Low"
    
    assert result == expected    

    
    
    