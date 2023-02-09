from custom.configuration.tensorflow_settings \
    import \
    set_global_settings


def setup():
    set_global_settings(
        {
            'algorithm':
                {
                    'batch_size': 8,
                    'epochs': 5,
                    'seed': 4,
                    'class_mode': '',
                },

            'image':
                {
                    'width': 256,
                    'height': 256,

                    'color_mode': 'rgb',
                    'keep_aspect_ratio': True,
                }
        }
    )
