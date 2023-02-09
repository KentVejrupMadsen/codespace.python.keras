from custom.domain \
    import Domain

from custom.configuration.Features \
    import set_setup_of_wandb

set_setup_of_wandb(True)


def main():
    domain = Domain()
    domain.initialise()
    domain.execute()
    domain.garbage_collection()


if __name__ == '__main__':
    main()
