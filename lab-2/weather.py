import random

weather_conditions = ["Sunny", "Rainy", "Cloudy", "Windy", "Snowy"]

def get_player_prediction():
    print("\nPredict the weather for tomorrow:")
    for i, condition in enumerate(weather_conditions, 1):
        print(f"{i}. {condition}")
    
    while True:
        choice = input("Enter the number of your prediction: ")
        if choice.isdigit() and 1 <= int(choice) <= len(weather_conditions):
            return weather_conditions[int(choice) - 1]
        else:
            print("Invalid choice. Please enter a number between 1 and", len(weather_conditions))

def get_actual_weather():
    return random.choice(weather_conditions)

def calculate_score(prediction, actual):
    if prediction == actual:
        return 3
    elif (
        (prediction == "Sunny" and actual == "Cloudy") or
        (prediction == "Cloudy" and actual == "Rainy") or
        (prediction == "Rainy" and actual == "Windy") or
        (prediction == "Windy" and actual == "Snowy") or
        (prediction == "Snowy" and actual == "Sunny")
    ):
        return 1
    return 0

def play_game():
    print("Welcome to the Weather Prediction Game!")
    print("Predict tomorrow's weather and score points!")
    print("3 points for a correct prediction, 1 point for a close guess, 0 points otherwise.")
    
    total_score = 0
    rounds = 5

    for round in range(1, rounds + 1):
        print(f"\nRound {round} of {rounds}")
        prediction = get_player_prediction()
        actual = get_actual_weather()
        score = calculate_score(prediction, actual)
        
        print(f"You predicted: {prediction}")
        print(f"Actual weather: {actual}")
        print(f"You scored: {score} points")
        
        total_score += score

    print(f"\nGame over! Your total score is: {total_score} out of {rounds * 3}")

# Start the game
play_game()