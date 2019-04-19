import glob


def detect_repository_type(path):
    languages = [
        {"java": [".java"]},
        {"python": [".py"]},
        {"terraform": [".tf", ".tfvars"]}
    ]
    file_type_count = {}
    for language in languages:
        for name, extensions in language.items():
            file_type_count[name] = 0
            for extension in extensions:
                file_type_count[name] = file_type_count[name] + len(glob.glob(path + '/**/*' + extension, recursive=True))
    return max(file_type_count, key=lambda key: file_type_count[key])
