# Task 1

def total_salary(path: str) -> tuple:
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = [el.strip().split(",")[1] for el in file.readlines()]

            if not salaries:
                raise ValueError(f"Please make sure file {path} contains expected data")

            total_salary = 0

            for salary in salaries:
                try:
                    total_salary += int(salary)
                except ValueError:
                    raise ValueError(f"Incorrect salary value detected in file {path}")

            average_salary = total_salary / len(salaries)

        return total_salary, average_salary

    except FileNotFoundError as err:
        print(f"Ooops! File {path} could not be found")
        return 0, 0

    except Exception as err:
        print(f"Error occurred: {err}")
        return 0, 0


total, average = total_salary("salaries.txt")
print(f"Total salary amount: {total}$, Average salary: {average}$")
