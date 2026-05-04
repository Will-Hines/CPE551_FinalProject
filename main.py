from appliance import Appliance
from dataset_loader import load_data
from display import plot_power, suggest_reduction

def main():
    # Load example datasets
    try:
        ac_data = load_data("data/air_conditioner.csv")
        fridge_data = load_data("data/fridge.csv")
    except Exception as e:
        print("Error loading data:", e)
        return

    # Create Appliance objects
    ac = Appliance("Air Conditioner", ac_data)
    fridge = Appliance("Fridge", fridge_data)

    appliances = [ac, fridge]

    # Display appliance stats
    for appliance in appliances:
        print(appliance)
        print("Peak Usage:", appliance.peak_usage)
        print("Average Usage:", appliance.average_usage)
        print("Total Energy:", appliance.get_total_energy(), "J\n")

    # Plot one appliance
    plot_power(ac)

    # Suggestions
    suggest_reduction(appliances)

    # Loop + enumerate requirement
    print("\nFirst 5 power values:")
    for i, val in enumerate(ac.energy["power"]):
        if i >= 5:
            break
        print(val)

if __name__ == "__main__":
    main()
