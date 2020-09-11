{
 "metadata": {
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
   "version": "3.8.5-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python38532bitvenvvenvfa0948426e114792aa2b023009def919",
   "display_name": "Python 3.8.5 32-bit ('.venv': venv)"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "## downloading 4 libraries which we are going to work on\n",
    "%pip install pandas\n",
    "%pip install html5lib\n",
    "%pip install BeautifulSoup4\n",
    "%pip install lxml"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": "Hello Capstone Project Course!\n"
    }
   ],
   "source": [
    "## importing libraries\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "print (\"Hello Capstone Project Course!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": "  Postal Code         Community                                Neighbourhood\n0         M1A      Not assigned                                 Not assigned\n1         M2A      Not assigned                                 Not assigned\n2         M3A        North York                                    Parkwoods\n3         M4A        North York                             Victoria Village\n4         M5A  Downtown Toronto                    Regent Park, Harbourfront\n5         M6A        North York             Lawrence Manor, Lawrence Heights\n6         M7A  Downtown Toronto  Queen's Park, Ontario Provincial Government\n7         M8A      Not assigned                                 Not assigned\n8         M9A         Etobicoke      Islington Avenue, Humber Valley Village\n9         M1B       Scarborough                               Malvern, Rouge",
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Postal Code</th>\n      <th>Community</th>\n      <th>Neighbourhood</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>M1A</td>\n      <td>Not assigned</td>\n      <td>Not assigned</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>M2A</td>\n      <td>Not assigned</td>\n      <td>Not assigned</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>M3A</td>\n      <td>North York</td>\n      <td>Parkwoods</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>M4A</td>\n      <td>North York</td>\n      <td>Victoria Village</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>M5A</td>\n      <td>Downtown Toronto</td>\n      <td>Regent Park, Harbourfront</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>M6A</td>\n      <td>North York</td>\n      <td>Lawrence Manor, Lawrence Heights</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>M7A</td>\n      <td>Downtown Toronto</td>\n      <td>Queen's Park, Ontario Provincial Government</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>M8A</td>\n      <td>Not assigned</td>\n      <td>Not assigned</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>M9A</td>\n      <td>Etobicoke</td>\n      <td>Islington Avenue, Humber Valley Village</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>M1B</td>\n      <td>Scarborough</td>\n      <td>Malvern, Rouge</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 10
    }
   ],
   "source": [
    "## import library which knows how to convert html to pandas\n",
    "from pandas.io.html import read_html\n",
    "## define the wikipedia URL\n",
    "wiki_url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'\n",
    "## using read_html function in order to get list of dataframes by class that exist in the wiki_url\n",
    "wikitable = read_html(wiki_url, attrs={'class': 'wikitable'})\n",
    "## there is only 1 table we retrieve the first dataframe from the list\n",
    "df_postal = wikitable[0]\n",
    "df_postal.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": "  Postal Code         Community                                Neighbourhood\n0         M3A        North York                                    Parkwoods\n1         M4A        North York                             Victoria Village\n2         M5A  Downtown Toronto                    Regent Park, Harbourfront\n3         M6A        North York             Lawrence Manor, Lawrence Heights\n4         M7A  Downtown Toronto  Queen's Park, Ontario Provincial Government\n5         M9A         Etobicoke      Islington Avenue, Humber Valley Village\n6         M1B       Scarborough                               Malvern, Rouge\n7         M3B        North York                                    Don Mills\n8         M4B         East York              Parkview Hill, Woodbine Gardens\n9         M5B  Downtown Toronto                     Garden District, Ryerson",
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Postal Code</th>\n      <th>Community</th>\n      <th>Neighbourhood</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>M3A</td>\n      <td>North York</td>\n      <td>Parkwoods</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>M4A</td>\n      <td>North York</td>\n      <td>Victoria Village</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>M5A</td>\n      <td>Downtown Toronto</td>\n      <td>Regent Park, Harbourfront</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>M6A</td>\n      <td>North York</td>\n      <td>Lawrence Manor, Lawrence Heights</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>M7A</td>\n      <td>Downtown Toronto</td>\n      <td>Queen's Park, Ontario Provincial Government</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>M9A</td>\n      <td>Etobicoke</td>\n      <td>Islington Avenue, Humber Valley Village</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>M1B</td>\n      <td>Scarborough</td>\n      <td>Malvern, Rouge</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>M3B</td>\n      <td>North York</td>\n      <td>Don Mills</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>M4B</td>\n      <td>East York</td>\n      <td>Parkview Hill, Woodbine Gardens</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>M5B</td>\n      <td>Downtown Toronto</td>\n      <td>Garden District, Ryerson</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 11
    }
   ],
   "source": [
    "df_postal_filterd = df_postal[df_postal.Community != 'Not assigned'] ## Ignoring cells with a borough that is Not assigned.\n",
    "df_postal_filterd = df_postal_filterd[df_postal_filterd.Neighbourhood != 'Not assigned'] ## Checking If a cell has a borough but a Not assigned neighborhood (doesn't exist)\n",
    "df_postal_filterd.reset_index(inplace = True, drop = True) ## arrange the new df after cleaning\n",
    "df_postal_filterd.head(10)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": "(103, 3)"
     },
     "metadata": {},
     "execution_count": 12
    }
   ],
   "source": [
    "df_postal_filterd.shape ## get the df shape"
   ]
  }
 ]
}