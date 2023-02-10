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
                    'path': '/mnt/c/DataSets/ScreenshotAsDataset/women_dataset/dataset',
                    'categories': 4
                },

            'log':
                {
                    'path': '/tmp/logs/'
                },

            'algorithm':
                {
                    'model':
                        {
                            'name': 'Horus'
                        },
                    'path': '/home/madsen/models',

                    'batch_size': 2,
                    'epochs': 1,

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
                    'width': 256,
                    'height': 256,

                    'keep_aspect_ratio': True,

                    'color':
                        {
                            'mode': 'rgb'
                        }
                }
        }
    )
