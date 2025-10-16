from pathlib import Path
import subprocess
import sys

root_path = Path(__file__).parent.parent
module_path = Path(root_path / "v2.0_ratioinputinsulin/ratioinsulincalc.py")

# ratioinsulincalc = import_module(module_path)

def test_ratio_insulin_calc_if():

    dosage_ratio = 0.5
    carbs = 140
    bloodsugars = 10

    result = subprocess.run(
        [sys.executable, module_path],
        input=f"{dosage_ratio}\n{carbs}\n{bloodsugars}\n",
        text=True,
        capture_output=True
    )

    print(f"result.stdout: \n\n{result.stdout}")
    assert f"You Need 10 Units of Insulin"  in result.stdout

def test_ratio_insulin_calc_elif():

    dosage_ratio = 0.5
    carbs = 200
    bloodsugars = 0.2

    result = subprocess.run(
        [sys.executable, module_path],
        input=f"{dosage_ratio}\n{carbs}\n{bloodsugars}\n",
        text=True,
        capture_output=True
    )

    print(f"result.stdout: \n\n{result.stdout}")
    assert f"You Need 6 Units of Insulin"  in result.stdout