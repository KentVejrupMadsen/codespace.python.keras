from custom.domain \
    import Domain

from custom.configuration.wandb_variables \
    import \
    set_setup_of_wandb, \
    set_wandb_sync_tensorboard, \
    set_wandb_save_code, \
    set_wandb_name

import os
import time

import auto
import config

import log
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Setup of configuration
config.setup()

set_wandb_name(
    'Run-Experiment-'
    +
    str(time.time_ns())
)

# defaults
auto.setup_tags()
auto.setup_appendices()

# Setup wandb,
set_setup_of_wandb(
    True
)

# Enable additional features
set_wandb_save_code(
    False
)

set_wandb_sync_tensorboard(
    True
)


# Setup of application, execution and cleaning
def main():
    domain = Domain()
    domain.initialise()
    domain.debug()

    domain.execute()
    log.log_setup()

    domain.garbage_collection()


# entry function
if __name__ == '__main__':
    main()
