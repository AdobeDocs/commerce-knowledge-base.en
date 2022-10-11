# Add a new line to the end of all files in the ./help directory

import os

for root, dir_names, file_names in os.walk('./help'):
        for file_name in file_names:
            # if filename ends in .md
            if file_name[-3:] == '.md':
                # open file
                with open(os.path.join(root, file_name), 'a') as f:
                    # add new line
                    f.write(' ')