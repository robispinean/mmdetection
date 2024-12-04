
import cv2
import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description='MMDetection video demo')
    parser.add_argument('--dry-run', action="store_true", help='dryrun')
    parser.add_argument('--text-file', type=Path, help='files')
    parser.add_argument('--username', type=Path, help='username')
    parser.add_argument('--password', type=Path, help='password')
    args = parser.parse_args()
    return args

def upload_data(args):
    
    if args.dry_run:
        print(args.files)
        return
    
    print("NOT DRY RUN")
    return 1

if __name__ == "__main__":
    args = parse_args()
    
    upload_data(args)
    
    