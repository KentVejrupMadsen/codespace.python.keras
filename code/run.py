from custom.domain \
    import Domain

from custom.configuration.wandb_variables \
    import \
    set_setup_of_wandb, \
    set_wandb_sync_tensorboard, \
    set_wandb_save_code

import auto

import config
# Setup of configuration
config.setup()

# defaults
auto.setup_tags()
auto.setup_appendices()

# Setup wandb,
set_setup_of_wandb(True)

# Enable additional features
set_wandb_save_code(True)
set_wandb_sync_tensorboard(True)


# Setup of application, execution and cleaning
def main():
    domain = Domain()
    domain.initialise()
    domain.execute()
    domain.garbage_collection()


# entry function
if __name__ == '__main__':
    main()
