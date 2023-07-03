"""Author: Loris Jared Ndonga"""

from pytest import approx
from BAC import BAC_calculation, BAC_result
import pytest

def test_BAC_cal():
    """Test the function to see if it give the right calculation 
    """
    man = 0.73 
    woman = 0.66
    assert BAC_calculation(1, 65, man, 4) == approx(0.0788812, abs=1)
    assert BAC_calculation(4, 65, woman, 4) == approx(0.046425407, abs=1)

def test_message():

    """Test the function to see if it prints the right message """
    countries = {"South Africa": 0.05,
                     "Rep. Of Congo": 0.05,
                     "Cote D'Ivoire": 0.08,
                        "Ethiopia": 0.08, 
                        "Canada": 0.05,
                        "Japan": 0.03,
                        "Australia": 0.05,
                        "Ghana": 0.08,
                        "Brazil": 0.06}
        # Country's name, limit of BAC, BAC result
    assert BAC_result("Rep. Of Congo", 0.05, 0.06) == f'It is not legal for you to drive in Rep. Of Congo.'
    assert BAC_result("Ethiopia", 0.08, 0.07) == f"It's okay. You can drive."
    assert BAC_result("Japan", 0.03, 0.02) == f"It's okay. You can drive."
    assert BAC_result("Brazil", 0.06, 0.06) == f'It is not legal for you to drive in Brazil.'
    
pytest.main(["-v","--tb=line", "-rN", __file__])