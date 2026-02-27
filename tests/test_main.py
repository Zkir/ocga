import filecmp
from pathlib import Path
import sys

# Add project root to path to allow 'from ocga import ...' when running as a script
sys.path.insert(0, str(Path(__file__).parent.parent))

from ocga import ocga_process2

# --- Path Setup ---
# Make paths robust by anchoring them to this file's location, not the CWD
ROOT_DIR = Path(__file__).parent.parent
SAMPLES_DIR = ROOT_DIR / "docs" / "ocga_samples"
OUTPUT_DIR = ROOT_DIR / "docs" / "ocga_output"


def run_single_test(rules_file: str, input_file: str) -> bool:
    """Helper function to run one test case and compare the output."""
    input_path = SAMPLES_DIR / input_file
    output_path = OUTPUT_DIR / f"{input_path.stem}-rewrite.osm"
    reference_path = SAMPLES_DIR / f"{input_path.stem}-rewrite.osm"
    rules_path = SAMPLES_DIR / rules_file
    compiled_rules_path = OUTPUT_DIR / f"{rules_path.stem}_ocga.py"

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(exist_ok=True)

    print(f"\nProcessing {input_file}...")
    ocga_process2(str(input_path), str(output_path), str(rules_path), compiled_rules_file=str(compiled_rules_path))

    return filecmp.cmp(output_path, reference_path, shallow=False)

# --- Pytest-compatible test functions ---

def test_gorky_park_entrance():
    assert run_single_test("gorky_park_entrance.ocga", "gorky_park_entrance.osm")

def test_church_of_st_louis():
    assert run_single_test("church_of_st_louis.ocga", "church_of_st_louis.osm")

def test_gorky_park_rotunda():
    assert run_single_test("gorky_park_rotunda.ocga", "gorky_park_rotunda.osm")

def test_tsaritsino_rotunda():
    assert run_single_test("tsaritsino_rotunda.ocga", "tsaritsino_rotunda.osm")

def test_main_cathedral_of_russian_army():
    assert run_single_test("main_cathedral_of_russian_army.ocga", "main_cathedral_of_russian_army.osm")

def test_alexander_column():
    assert run_single_test("alexander_column.ocga", "alexander_column.osm")

def test_moscow_manege():
    assert run_single_test("moscow_manege.ocga", "moscow_manege.osm")

def test_komsomolskaya_station():
    assert run_single_test("komsomolskaya_station.ocga", "komsomolskaya_station.osm")

def test_novokuznetskaya():
    assert run_single_test("novokuznetskaya.ocga", "novokuznetskaya.osm")

# --- Block for direct execution (`python tests/test_main.py`) ---

if __name__ == "__main__":
    print("--- Running tests as a standalone script ---")
    
    # Run all test functions defined in this file
    all_tests = [v for k, v in locals().items() if k.startswith("test_")]
    
    passed = 0
    failed = 0
    
    for test_func in all_tests:
        try:
            test_func()
            print(f"  [PASS] {test_func.__name__}")
            passed += 1
        except AssertionError:
            print(f"  [FAIL] {test_func.__name__}")
            failed += 1

    print("\n--- Test run finished ---")
    print(f"Result: {passed} passed, {failed} failed.")
    
    if failed > 0:
        sys.exit(1)
