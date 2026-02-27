import interface


def tokenize(expression: str) -> list[str]:
    def add_list_finale(nombre):
        try:
            print(f"le nombre {nombre} va {float(nombre)}")
            list_finale.append(float(nombre))
        except ValueError as e:
            print(ValueError)
            interface.execute_erreur_(f"ValueError: {e}")

    expression_list = list(expression)
    list_finale = []
    nombre_vergule = str()
    for element in expression_list:
        print("element", element)
        if (
            element in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            or element == "."
        ):
            nombre_vergule += element
        elif (
            element in ["(", ")", "*", "×", "/", "÷", "+", "−", "-"] and element != " "
        ):
            if nombre_vergule != "":
                print(f"nombre_vergule {nombre_vergule}")
                add_list_finale(nombre_vergule)
            list_finale.append(element)
            nombre_vergule = str()
    if len(nombre_vergule) != 0:
        add_list_finale(nombre_vergule)
    return list_finale


def infix_to_postfix(tokens: list[str]) -> list[str]:
    precedence_of_operator = {
        "(": 0,
        ")": 0,
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
        if type(token) is type(str()) and token != "(" and token != ")":
            try:
                valeur_dernier_operatation = precedence_of_operator[operators[-1]]
            except IndexError:
                valeur_dernier_operatation = 0
            if (
                valeur_dernier_operatation < precedence_of_operator[token]
                or token == "^"
            ):
                operators.append(token)
            elif valeur_dernier_operatation >= precedence_of_operator[token]:
                valeur_dernier_operatation = 0
                for element in operators[::-1]:
                    if precedence_of_operator[token] <= precedence_of_operator[element]:
                        output.append(operators[::-1].pop(0))
                        del operators[-1]
                operators.append(token)

        elif token == "(":
            operators.append(token)

        elif token == ")":
            operators_bracket = []
            while operators[-1] != "(":
                operators_bracket_temp = operators.pop(-1)
                operators_bracket.append(operators_bracket_temp)
            del operators[-1]
            for element in operators_bracket:
                output.append(element)

        else:
            output.append(token)
    for element in operators[::-1]:
        output.append(element)
    return output


def evaluate_postfix(tokens: list[str]) -> float:
    list_nombre = list()
    precedence_of_operator = {
        "(": 0,
        ")": 0,
        "*": 3,
        "×": 3,
        "/": 3,
        "÷": 3,
        "+": 2,
        "−": 2,
        "-": 2,
    }
    for token_index in range(len(tokens)):
        if type(tokens[token_index]) is type(float()):
            list_nombre.append(tokens[token_index])
        if type(tokens[token_index]) is type(str()):
            try:
                match precedence_of_operator[tokens[token_index]]:
                    case 2:
                        if tokens[token_index] == "+":
                            list_nombre.append(list_nombre[-2] + list_nombre[-1])
                        elif tokens[token_index] == "-" or tokens[token_index] == "−":
                            list_nombre.append(list_nombre[-2] - list_nombre[-1])
                        del list_nombre[-2], list_nombre[-2]
                    case 3:
                        if tokens[token_index] == "*" or tokens[token_index] == "×":
                            list_nombre.append(list_nombre[-2] * list_nombre[-1])
                        elif tokens[token_index] == "/" or tokens[token_index] == "÷":
                            list_nombre.append(list_nombre[-2] / list_nombre[-1])
                        del list_nombre[-2], list_nombre[-2]
            except IndexError as e:
                interface.execute_erreur_(f"IndexError : {e}")
            except ZeroDivisionError as e:
                print("diviser 0 ")
                interface.execute_erreur_(f"ZeroDivisionError : {e}")
                return "impossible"
    return list_nombre[0]


# print(infix_to_postfix(tokenize("3 + 2.45 * 2 / ( 1 - 5 )")))
