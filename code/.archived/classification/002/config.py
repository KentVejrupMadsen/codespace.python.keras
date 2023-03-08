from custom.configuration.tensorflow_settings \
    import \
    set_global_settings

from randomizer \
    import generate_seed


set_global_settings(
    {
        'dataset':
        {
            'path': '/mnt/c/DataSets/BigDataSet/dataset',
            'categories': 5
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

            'batch_size': 5,
            'epochs': 10,

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
                },
            },

        'images':
            {
                'width': 512,
                'height': 512,

                'keep_aspect_ratio': True,

                'color':
                {
                    'mode': 'rgb',
                    'channels': 3
                }
            }
    }
)
