# Add a new line to the end of all files in the ./help directory

import os

for root, dir_names, file_names in os.walk('./help'):
        for file_name in file_names:
            # if filename ends in .md and is inside troubleshooting
            # if file_name.endswith('.md') and 'troubleshooting' in root:
            if file_name.endswith('.md'):
                # open file
                with open(os.path.join(root, file_name), 'a') as f:
                    # add a new line
                    f.write('\n')