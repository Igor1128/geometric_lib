import circle
import square
import triangle

figs = ["circle", "square", "triangle"]
funcs = ["perimeter", "area"]
sizes = {}


def calc(fig, func, size):
    if fig not in figs:
        return f"Invalid figure: {fig}. Available figures: {figs}"
    if func not in funcs:
        return f"Invalid function: {func}. Available functions: {funcs}"

    try:
        if fig == "circle":
            result = getattr(circle, func)(*size)
        elif fig == "square":
            result = getattr(square, func)(*size)
        elif fig == "triangle":
            result = getattr(triangle, func)(*size)
        return result
    except ValueError as e:
        if fig == "triangle" and func == "area":
            return f"Error calculating {func} of {fig}: math domain error"
        elif (
            fig == "square"
            and func == "area"
            or fig == "square"
            and func == "perimeter"
        ):
            return f"Error calculating {func} of {fig}: negative side"
        elif (
            fig == "circle"
            and func == "area"
            or fig == "circle"
            and func == "perimeter"
        ):
            return f"Error calculating {func} of {fig}: negative radius"
        else:
            return f"Error calculating {func} of {fig}: {e}"
    except Exception as e:
        return f"Error calculating {func} of {fig}: {e}"


if __name__ == "__main__":
    func = ""
    fig = ""
    size = list()

    while fig not in ["circle", "square", "triangle"]:
        fig = input(
            "Enter figure name, available are ['circle', 'square'," "'triangle']:\n"
        )

    while func not in ["perimeter", "area"]:
        func = input("Enter function name, available are ['perimeter', 'area']:\n")

        while len(size) != {
            "circle-perimeter": 1,
            "circle-area": 1,
            "square-perimeter": 1,
            "square-area": 1,
            "triangle-perimeter": 3,
            "triangle-area": 3,
        }.get(f"{func}-{fig}", 1):
            size = list(
                map(
                    int,
                    input(
                        "Input figure sizes separated by space\n"
                        "1 for circle and square\n"
                    ).split(),
                )
            )
    result = calc(fig, func, size)
    print(f"{func} of {fig} is {result}")
