import os
import sys

# --- CONFIGURATION ---
move_unmatched = True  # Set to True to move instead of delete
unmatched_folder_name = "_unmatched"


def main():
    # --- Determine target folder ---
    root_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    raw_dir = os.path.join(root_dir, "RAW")
    unmatched_dir = os.path.join(raw_dir, unmatched_folder_name)

    if not os.path.isdir(raw_dir):
        print(f"❌ RAW folder not found: {raw_dir}")
        return

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

    print(f"\n📁 Working folder: {root_dir}")
    print("📸 DRY RUN REPORT")
    print(f"Found {len(jpeg_basenames)} JPEGs")
    print(f"Found {len(raw_files)} RAWs")
    print(f"→ {len(matched)} will be kept")
    print(f"→ {len(unmatched)} will be {'moved' if move_unmatched else 'deleted'}")

    if not unmatched:
        print("✅ All RAWs have matching JPEGs. Nothing to do.")
        return

    confirm = input("\nProceed with changes? (y/N): ").strip().lower()
    if confirm != "y":
        print("❎ Aborted. No changes made.")
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

    print(f"\n✅ Done! {len(unmatched)} RAW files {'moved' if move_unmatched else 'deleted'}.")


if __name__ == "__main__":
    main()
