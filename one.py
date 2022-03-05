{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7154d09b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0cd79e1c",
   "metadata": {},
   "outputs": [],
   "source": [
    "data1 = pd.read_csv(\"archive/FastFoodRestaurants.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "6e05bf03",
   "metadata": {},
   "outputs": [],
   "source": [
    "data1=data1.drop([\"address\",\"country\",\"keys\",\"name\",\"postalCode\",\"province\",\"websites\"], axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "d86df280",
   "metadata": {},
   "outputs": [],
   "source": [
    "Columbus=data1.loc[data1[\"city\"]==\"Columbus\"]\n",
    "Cincinnati=data1.loc[data1[\"city\"]==\"Cincinnati\"]\n",
    "Cleveland =data1.loc[data1[\"city\"]==\"Cleveland\"]\n",
    "Las=data1.loc[data1[\"city\"]==\"Las Vegas\"]\n",
    "Miami=data1.loc[data1[\"city\"]==\"Miami\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "0c682e7c",
   "metadata": {},
   "outputs": [],
   "source": [
    "data2 = pd.read_csv(\"archive/Datafiniti_Fast_Food_Restaurants_May19.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "488ccb1e",
   "metadata": {},
   "outputs": [],
   "source": [
    "data2=data2[[\"city\",\"latitude\",\"longitude\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "aaf67047",
   "metadata": {},
   "outputs": [],
   "source": [
    "Columbus=pd.concat([Columbus, data2.loc[data2[\"city\"]==\"Columbus\"]], ignore_index=True)\n",
    "Cincinnati=pd.concat([Cincinnati, data2.loc[data2[\"city\"]==\"Cincinnati\"]], ignore_index=True)\n",
    "Cleveland=pd.concat([Cleveland, data2.loc[data2[\"city\"]==\"Cleveland\"]], ignore_index=True)\n",
    "Las=pd.concat([Las, data2.loc[data2[\"city\"]==\"Las\"]], ignore_index=True)\n",
    "Miami=pd.concat([Miami, data2.loc[data2[\"city\"]==\"Miami\"]], ignore_index=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "937e8037",
   "metadata": {},
   "outputs": [],
   "source": [
    "data3 = pd.read_csv(\"archive/Datafiniti_Fast_Food_Restaurants.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "d4c50b5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "data3=data3[[\"city\",\"latitude\",\"longitude\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "d83f415a",
   "metadata": {},
   "outputs": [],
   "source": [
    "Columbus=pd.concat([Columbus, data3.loc[data3[\"city\"]==\"Columbus\"]], ignore_index=True)\n",
    "Cincinnati=pd.concat([Cincinnati, data3.loc[data3[\"city\"]==\"Cincinnati\"]], ignore_index=True)\n",
    "Cleveland=pd.concat([Cleveland, data3.loc[data3[\"city\"]==\"Cleveland\"]], ignore_index=True)\n",
    "Las=pd.concat([Las, data3.loc[data3[\"city\"]==\"Las\"]], ignore_index=True)\n",
    "Miami=pd.concat([Miami, data3.loc[data3[\"city\"]==\"Miami\"]], ignore_index=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "d922c5c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "Columbus=Columbus.drop_duplicates()\n",
    "Cincinnati=Cincinnati.drop_duplicates()\n",
    "Cleveland=Cleveland.drop_duplicates()\n",
    "Las=Las.drop_duplicates()\n",
    "Miami=Miami.drop_duplicates()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "21a82225",
   "metadata": {},
   "outputs": [],
   "source": [
    "Columbus=Columbus[[\"latitude\",\"longitude\"]]\n",
    "Cincinnati=Cincinnati[[\"latitude\",\"longitude\"]]\n",
    "Cleveland=Cleveland[[\"latitude\",\"longitude\"]]\n",
    "Las=Las[[\"latitude\",\"longitude\"]]\n",
    "Miami=Miami[[\"latitude\",\"longitude\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "200cf14e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
