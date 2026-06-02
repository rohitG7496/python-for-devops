import argparse

parser = argparse.ArgumentParser(description="Cloud Deployment Script")
parser.add_argument("--env", required=True, help="Environment (prod/dev)")
parser.add_argument("--count", type=int, default=1, help="Number of instances")

args = parser.parse_args()
print(f"Deploying {args.count} instances to {args.env}")