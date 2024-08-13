import argparse
from dealer import Dealer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dealer Mobil")
    parser.add_argument("command", choices=["show_all", "show_models", "show_details"], help="Command to execute")
    parser.add_argument("--brand", help="Brand of the car")
    parser.add_argument("--model", help="Model of the car")

    args = parser.parse_args()

    if args.command == "show_all":
        Dealer.show_all_cars()
        
    elif args.command == "show_models":
        if not args.brand:
            parser.error("The --brand argument is required for the 'show_models' command")
        Dealer.show_all_car_models(args.brand)

    elif args.command == "show_details":
        if not args.brand or not args.model:
            parser.error("Both --brand and --model arguments are required for the 'show_details' command")
        Dealer.show_model_details(args.brand, args.model)