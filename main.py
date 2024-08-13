import argparse
import json
from dealer import Dealer

dealer = Dealer()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dealer Mobil")
    parser.add_argument("command", choices=["show_all", "show_models", "show_details"], help="Command to execute")
    parser.add_argument("--brand", type=str, help="Brand of the car")
    parser.add_argument("--model", type=str, help="Model of the car")
    args = parser.parse_args()

    if args.command == "show_all":
        dealer.show_all_cars()

    elif args.command == "show_models":
        if not args.brand:
            parser.error("The --brand argument is required for the 'show_models' command")
        for car in dealer.show_all_car_models(args.brand):
            print(f"Model: {car}")

    elif args.command == "show_details":
        if not args.brand or not args.model:
            parser.error("Both --brand and --model arguments are required for the 'show_details' command")
        print(json.dumps(dealer.show_car_model_detail(args.brand, args.model), indent=4))
