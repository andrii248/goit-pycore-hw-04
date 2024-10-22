# Task 1


def get_cats_info(path: str) -> list:
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = [el.strip().split(",") for el in file.readlines()]

            if not lines:
                raise ValueError(f"Please make sure file {path} contains expected data")

            results = []

            for el in lines:
                if len(el) != 3:
                    raise ValueError(
                        f"Please make sure info about the cat at line: {lines.index(el) + 1} is correct. Each line should contain id, name and age of the cat."
                    )

                cat_id, cat_name, cat_age = el[0], el[1], el[2]

                if not cat_id.isalnum():
                    raise ValueError(f"Invalid cat Id at line: {lines.index(el) + 1}.")
                if not cat_name.isalpha():
                    raise ValueError(
                        f"Invalid cat name at line: {lines.index(el) + 1}."
                    )

                try:
                    age = int(cat_age)
                    if age < 0:
                        raise ValueError

                except ValueError:
                    raise ValueError(
                        f"Age at line:  {lines.index(el) + 1} should be a positive integer "
                    )

                cat = {"id": cat_id, "name": cat_name, "age": cat_age}
                results.append(cat)

            return results

    except FileNotFoundError as err:
        print(f"Error occurred: {err}")
        return []

    except Exception as err:
        print(f"Error occurred: {err}")
        return []


cats_info = get_cats_info("cats.txt")
print(cats_info)
