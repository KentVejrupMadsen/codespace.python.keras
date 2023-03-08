from custom.stages.callbacks.checkpoint_callback \
    import add_checkpoint_callback

from custom.stages.callbacks.early_stop_callback \
    import add_early_stopper

from custom.stages.callbacks.tensorboard_callback \
    import add_tensorboard_callback


def callback_setup(
        callbacks: list
):
    add_checkpoint_callback(
        callbacks
    )

    add_early_stopper(
        callbacks
    )
