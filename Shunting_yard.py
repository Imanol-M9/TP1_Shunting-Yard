def tokenize(expression: str) -> list[str]:
    def add_list_finale(nombre):
        try:
            list_finale.append(float(nombre))

        except ValueError:
            list_finale.append((ValueError, "Nombre mal formé"))

    expression_list = list(expression)
    list_finale = []
    nombre_vergule = str()
    for element in expression_list:
        if (
            element in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            or element == "."
        ):
            nombre_vergule += element

        elif (
            element in ["(", ")", "*", "×", "/", "÷", "+", "−", "-"] and element != " "
        ):
            if nombre_vergule != "":
                add_list_finale(nombre_vergule)
            list_finale.append(element)
            nombre_vergule = str()
        elif type(element) is not type(int()) and element not in [
            "(",
            ")",
            "*",
            "×",
            "/",
            "÷",
            "+",
            "−",
            "-",
            " ",
        ]:
            return ValueError, "Opérateur inconnu"

    if len(nombre_vergule) != 0:
        add_list_finale(nombre_vergule)
    if (ValueError, "Opérateur inconnu") in list_finale:
        return ValueError, "Opérateur inconnu"
    else:
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
    try:
        if type(tokens[0]) is type(BaseException):
            return tokens
    except IndexError:
        pass
    else:
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
                        if (
                            precedence_of_operator[token]
                            <= precedence_of_operator[element]
                        ):
                            output.append(operators[::-1].pop(0))
                            del operators[-1]
                    operators.append(token)

            elif token == "(":
                operators.append(token)

            elif token == ")":
                operators_bracket = []
                try:
                    while operators[-1] != "(":
                        operators_bracket_temp = operators.pop(-1)
                        operators_bracket.append(operators_bracket_temp)
                    del operators[-1]
                    for element in operators_bracket:
                        output.append(element)
                except IndexError:
                    return IndexError, "Parenthèse ouverte manquente"
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
    if type(tokens[0]) is type(BaseException):
        return tokens
    else:
        for token_index in range(len(tokens)):
            if type(tokens[token_index]) is type(float()):
                list_nombre.append(tokens[token_index])
            if type(tokens[token_index]) is type(str()):
                try:
                    match precedence_of_operator[tokens[token_index]]:
                        case 2:
                            if tokens[token_index] == "+":
                                list_nombre.append(list_nombre[-2] + list_nombre[-1])
                            elif (
                                tokens[token_index] == "-" or tokens[token_index] == "−"
                            ):
                                list_nombre.append(list_nombre[-2] - list_nombre[-1])
                            del list_nombre[-2], list_nombre[-2]
                        case 3:
                            if tokens[token_index] == "*" or tokens[token_index] == "×":
                                list_nombre.append(list_nombre[-2] * list_nombre[-1])
                            elif (
                                tokens[token_index] == "/" or tokens[token_index] == "÷"
                            ):
                                list_nombre.append(list_nombre[-2] / list_nombre[-1])
                            del list_nombre[-2], list_nombre[-2]
                        case 0:
                            return IndexError, "Parenthèse fermante manquente"

                except IndexError:
                    return IndexError, "Un ou plusieur opérateur est de trop"

                except ZeroDivisionError:
                    return ZeroDivisionError, "Division par zéro imposible"
    if len(list_nombre) != 1:
        return IndexError, "Il manque d'opérateur"
    else:
        return list_nombre[0]
