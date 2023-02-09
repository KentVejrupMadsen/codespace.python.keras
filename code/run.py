# https://www.analyticsvidhya.com/blog/2021/07/step-by-step-guide-for-image-classification-on-custom-datasets/
from tensorflow.python.framework.config \
    import \
    list_physical_devices, \
    set_memory_growth

from configuration.machine_state \
    import \
    get_epoch, \
    get_batch_size_value, \
    get_validation_split

from configuration.path_configuration \
    import set_dataset_path

import \
    setup, \
    classification, \
    model, \
    setupCallbacks


set_dataset_path(
    r'/mnt/c/DataSets/ScreenshotAsDataset/women_dataset/dataset'
)

gpus = list_physical_devices('GPU')

if gpus:
    for gpu in gpus:
        print('found: ', str(gpu))
        set_memory_growth(
            gpu,
            True
        )


def main():

    setup.start()

    data_sets = classification.classification()

    ai_model = model.create_model()

    history = ai_model.fit(
        data_sets['train_x'],
        data_sets['training'].classes,
        validation_data=(
            data_sets['validation_x'],
            data_sets['validation'].classes
        ),
        epochs=get_epoch(),
        callbacks=setupCallbacks.call_callbacks(),
        batch_size=get_batch_size_value(),
        shuffle=True,
        verbose=1,
        use_multiprocessing=False
    )

    print(history)

    ai_model.summary()

    setup.end()


if __name__ == '__main__':
    main()
