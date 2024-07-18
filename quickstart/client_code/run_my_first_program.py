from nada_dsl import *
def nada_main():

    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")

    u = SecretInteger(Input(name="U", party=party1))
    v = SecretInteger(Input(name="V", party=party2))

    result = u < v
    return [Output(result, "comparison_output", party=party3)]
