from kondo.get_repositories import get_repositories


def main():
    organizations = ["TradeRev"]
    users = []
    get_repositories(organizations, users)


if __name__ == '__main__':
    main()
