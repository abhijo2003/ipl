# -*- coding: utf-8 -*-
"""Copy of Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N48hzL9SdKptQs8ZYspCQt_bWcYFndvX
"""

pip install streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
#

! wget -q -O - ipv4.icanhazip.com

!pip install --upgrade streamlit

! streamlit run app.py & npx localtunnel --port 8501