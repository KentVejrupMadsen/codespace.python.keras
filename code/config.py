from custom.configuration.tensorflow_settings \
    import \
    set_global_settings

from randomizer \
    import generate_seed


def setup():
    set_global_settings(
        {
            'dataset':
                {
                    'path': '/mnt/c/DataSets/ScreenshotAsDataset/women_dataset/dataset'
                },
            'algorithm':
                {
                    'batch_size': 2,
                    'epochs': 5,
                    'seed': generate_seed(),
                    'validation':
                        {
                            'split': 0.2
                        },
                    'checkpoint':
                        {
                            'path': '/tmp/checkpoint',
                            'save':
                                {
                                    'only':
                                        {
                                            'weights': False,
                                            'best': True
                                        },

                                    'frequency': 4,
                                    'execution-steps': 50
                                },

                            'monitor':
                                {
                                    'monitor': 'accuracy',
                                    'threshold': 'max'
                                },

                            'output': True
                        }
                },

            'images':
                {
                    'width': 128,
                    'height': 128,

                    'keep_aspect_ratio': True,

                    'color':
                        {
                            'mode': 'rgb'
                        }
                }
        }
    )
