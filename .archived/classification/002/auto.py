from custom.configuration.wandb_variables \
    import \
    get_wandb_tags, \
    set_wandb_notes, \
    set_wandb_group


def setup_appendices():
    set_wandb_notes('Experimentation with classifying images')
    set_wandb_group('Experiment')


def setup_tags():
    get_wandb_tags().append('GPU')
    get_wandb_tags().append('GPU-CUDA')
    get_wandb_tags().append('test')
    get_wandb_tags().append('experiment')
    get_wandb_tags().append('vision')
    get_wandb_tags().append('classification')
    get_wandb_tags().append('medium')
    get_wandb_tags().append('images')
