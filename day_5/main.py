from logic import Resolver
from utils import load_rules_and_sequences



if __name__ == '__main__':
    rules, sequences = load_rules_and_sequences('inputs/input.txt')
    resolver = Resolver(rules, sequences)
    print(resolver.resolve(part=2))