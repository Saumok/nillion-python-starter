from nada_dsl import *

def nada_main():
    # Define the parties involved
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")

    # Input secrets from party1 and party2
    u = SecretInteger(Input(name="U", party=party1))
    v = SecretInteger(Input(name="V", party=party2))

    # Perform comparison of the secret integers
    result = u < v

    # Output the result to party3
    return [Output(result, "comparison_output", party=party3)]
