def tokenize(expression: str) -> list[str]:
    expression_list = list(expression)
    for element in expression_list:
        if element == " ":
            expression_list.remove(element)

    return expression_list


# Need to fin a solution for . and , in nomber
def infix_to_postfix(tokens: list[str]) -> list[str]:
    print(tokens)
    precedence_of_operator = {
        "(": 0,
        ")": 0,
        "^": 4,
        "*": 3,
        "×": 3,
        "/": 3,
        "÷": 3,
        "+": 2,
        "−": 2,
        "-": 2,
    }
    output = []
    operators = []

    for token in tokens:
        if (
            42 <= ord(token) <= 47
            or token == "×"
            or token == "÷"
            or token == "−"
            or token == "^"
            and ord(token) != 46
        ):
            # le code acsii de 46 est le . il faut donc le garder dans les nombres
            try:
                valeur_dernier_operatation = precedence_of_operator[operators[-1]]
            except IndexError:
                valeur_dernier_operatation = 0
            if (
                valeur_dernier_operatation < precedence_of_operator[token]
                or token == "^"
            ):
                print("ajout directe")
                operators.append(token)
            elif valeur_dernier_operatation >= precedence_of_operator[token]:
                print(f"vidage besoin de mettre {token}")
                valeur_dernier_operatation = 0
                for element in operators[::-1]:
                    if precedence_of_operator[token] <= precedence_of_operator[element]:
                        output.append(operators[::-1].pop(0))
                        del operators[-1]
                operators.append(token)

        elif token == "(":
            operators.append(token)

        elif token == ")":
            print("----- fin de braket -----")
            operators_bracket = []
            print("operators", operators)
            while operators[-1] != "(":
                operators_bracket_temp = operators.pop(-1)
                operators_bracket.append(operators_bracket_temp)
            del operators[-1]
            print("opertaor apres", operators)
            print("element a mettre", operators_bracket)
            for element in operators_bracket:
                output.append(element)
            # print(f"operateur apres supresion (){operators}")

        else:
            output.append(token)
        print(f"output {output}, operators{operators}")
    for element in operators[::-1]:
        output.append(element)
    print(f"ouput final {output}")


def evaluate_postfix(tokens: list[str]) -> float:
    None


print(infix_to_postfix(tokenize("3 + 4 * 2 / ( 1 - 5 )")))
