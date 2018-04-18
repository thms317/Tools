import matplotlib.pyplot as plt
import json

save = False

if save:
    # save figure
    plt.savefig('title.png')
    # save parameters
    with open('title.json', 'w') as f:
        f.write(json.dumps(parameters))

    # open parameters
    with open('title.json', 'r') as read_file:
        loaded_parameters = json.loads(read_file.read())
    print(loaded_parameters)

    l = loaded_parameters
    print(l['L1_bp'])  # extract L1_bp