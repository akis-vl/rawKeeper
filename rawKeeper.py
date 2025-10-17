import os
import sys

# --- CONFIGURATION ---
move_unmatched = False  # Set True to move instead of delete
unmatched_folder_name = "_unmatched"  # Destination folder for moved RAWs


def find_raw_folder(root_dir):
    """Find a subfolder whose name contains 'raw' (case-insensitive)."""
    for name in os.listdir(root_dir):
        if os.path.isdir(os.path.join(root_dir, name)) and "raw" in name.lower():
            return os.path.join(root_dir, name)
    return None


def main():
    # --- Determine target folder ---
    root_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    raw_dir = find_raw_folder(root_dir)

    if not raw_dir:
        print(f"No folder containing 'raw' found in: {root_dir}")
        return

    unmatched_dir = os.path.join(raw_dir, unmatched_folder_name)

    print(f"Working folder: {root_dir}")
    print(f"RAW folder detected: {raw_dir}")

    # Collect JPEG base names
    jpeg_basenames = {
        os.path.splitext(f)[0]
        for f in os.listdir(root_dir)
        if f.lower().endswith((".jpg", ".jpeg"))
    }

    # Collect RAWs
    raw_files = [f for f in os.listdir(raw_dir) if not f.startswith(".")]
    unmatched = [f for f in raw_files if os.path.splitext(f)[0] not in jpeg_basenames]
    matched = [f for f in raw_files if os.path.splitext(f)[0] in jpeg_basenames]

    print("\nDRY RUN REPORT")
    print(f"Found {len(jpeg_basenames)} JPEGs")
    print(f"Found {len(raw_files)} RAWs in '{os.path.basename(raw_dir)}'")
    print(f"→ {len(matched)} will be kept")
    print(f"→ {len(unmatched)} will be {'moved' if move_unmatched else 'deleted'}")

    if not unmatched:
        print("All RAWs have matching JPEGs. Nothing to do.")
        return

    confirm = input("\nProceed with changes? (y/N): ").strip().lower()
    if confirm != "y":
        print("Aborted. No changes made.")
        return

    if move_unmatched:
        os.makedirs(unmatched_dir, exist_ok=True)

    for raw_file in unmatched:
        src = os.path.join(raw_dir, raw_file)
        if move_unmatched:
            dst = os.path.join(unmatched_dir, raw_file)
            os.rename(src, dst)
        else:
            os.remove(src)

    print(f"\nDone! {len(unmatched)} RAW files {'moved' if move_unmatched else 'deleted'}.")


if __name__ == "__main__":
    main()
