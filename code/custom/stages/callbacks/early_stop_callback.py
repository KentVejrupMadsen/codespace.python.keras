from tensorflow.python.keras.callbacks \
    import                              \
    EarlyStopping


def add_early_stopper(
        callbacks: list
):
    early_stopping = EarlyStopping(
        monitor="loss",
        mode="min",
        verbose=1,
        patience=5
    )

    callbacks.append(
        early_stopping
    )
