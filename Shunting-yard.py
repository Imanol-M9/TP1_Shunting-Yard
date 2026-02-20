def tokenize(expression: str) -> list[str]:
    expression_list = list(expression)
    for element in expression_list:
        if element == " ":
            expression_list.remove(element)

    return expression_list


def infix_to_postfix(tokens: list[str]) -> list[str]:
    None


def evaluate_postfix(tokens: list[str]) -> float:
    None


print(tokenize("3 + 4.4 * 2 / ( 1 - 5 )"))
