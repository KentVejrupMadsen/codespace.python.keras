from custom.domain \
    import Domain


def main():
    domain = Domain()
    domain.initialise()
    domain.execute()
    domain.garbage_collection()


if __name__ == '__main__':
    main()
