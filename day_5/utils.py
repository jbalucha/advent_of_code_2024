from collections import defaultdict


def load_rules_and_sequences(file_name):
    rules = []
    sequences = []

    with open(file_name, 'r') as file:
        current_part = rules

        for line in file:
            if line.strip() == '':
                current_part = sequences
                continue
            current_part.append(line.strip())

    return parse_rules(rules), parse_sequences(sequences)

def parse_rules(raw_rules):
    must_before = defaultdict(set)

    for rule in raw_rules:
        first, second = rule.split('|')
        must_before[int(second.strip())].add(int(first.strip()))

    return must_before

def parse_sequences(raw_sequences):
    result = []
    for response in raw_sequences:
        result.append([int(number) for number in response.split(',')])

    return result