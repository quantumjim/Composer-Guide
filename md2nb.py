import os
import json
import nbconvert

empty_notebook = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "replace"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

for path, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file[-3:]=='.md':
            with open(path+'/'+file) as md_file:  
                md = md_file.read()
                
                md = md.replace(' $$',' $')
                md = md.replace('$$ ','$ ')
                md = md.replace('$$.','$.')
                md = md.replace('$$,','$,')
                
                md = md.replace('\n','\nsplit_here')
                md_list = md.split('split_here')
                
                notebook = empty_notebook
                notebook['cells'][0]['source'] = md_list
                
                new_file = file.replace('.md','.ipynb')
                print(path+'/'+new_file)
                with open(path+'/'+new_file,'w') as nb_file:
                    json.dump(empty_notebook,nb_file)