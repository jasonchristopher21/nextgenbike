classes = ['asphalt', 'pavement', 'gravel', 'grass']
learning_rate = 1e-3
momentum = 0.9
num_training_epochs = 10
batch_size = 25
n_training_cols = 8
n_hidden_layers = 256

surfacemodel_path = "surfacemodel"


def map_to_int(c):
    for i, e in enumerate(classes):
        if c == e:
            return i


def map_to_string(i):
    return classes[i]
