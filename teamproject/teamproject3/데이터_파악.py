{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "641cbc09",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# polls_user"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "aeacdf2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "polls_user = pd.read_csv('polls_usercandidate.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "77568736",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>created_at</th>\n",
       "      <th>question_piece_id</th>\n",
       "      <th>user_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3088872</td>\n",
       "      <td>2023-04-28 12:27:49</td>\n",
       "      <td>998458</td>\n",
       "      <td>849444</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3088873</td>\n",
       "      <td>2023-04-28 12:27:49</td>\n",
       "      <td>998458</td>\n",
       "      <td>849454</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3088874</td>\n",
       "      <td>2023-04-28 12:27:49</td>\n",
       "      <td>998458</td>\n",
       "      <td>849460</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3088875</td>\n",
       "      <td>2023-04-28 12:27:49</td>\n",
       "      <td>998458</td>\n",
       "      <td>849469</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3088964</td>\n",
       "      <td>2023-04-28 12:28:02</td>\n",
       "      <td>998459</td>\n",
       "      <td>849446</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4769604</th>\n",
       "      <td>646672580</td>\n",
       "      <td>2024-05-08 01:36:00</td>\n",
       "      <td>200139933</td>\n",
       "      <td>857296</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4769605</th>\n",
       "      <td>646672581</td>\n",
       "      <td>2024-05-08 01:36:18</td>\n",
       "      <td>200139934</td>\n",
       "      <td>850774</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4769606</th>\n",
       "      <td>646672582</td>\n",
       "      <td>2024-05-08 01:36:18</td>\n",
       "      <td>200139934</td>\n",
       "      <td>856446</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4769607</th>\n",
       "      <td>646672583</td>\n",
       "      <td>2024-05-08 01:36:18</td>\n",
       "      <td>200139934</td>\n",
       "      <td>857101</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4769608</th>\n",
       "      <td>646672584</td>\n",
       "      <td>2024-05-08 01:36:18</td>\n",
       "      <td>200139934</td>\n",
       "      <td>874566</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>4769609 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                id           created_at  question_piece_id  user_id\n",
       "0          3088872  2023-04-28 12:27:49             998458   849444\n",
       "1          3088873  2023-04-28 12:27:49             998458   849454\n",
       "2          3088874  2023-04-28 12:27:49             998458   849460\n",
       "3          3088875  2023-04-28 12:27:49             998458   849469\n",
       "4          3088964  2023-04-28 12:28:02             998459   849446\n",
       "...            ...                  ...                ...      ...\n",
       "4769604  646672580  2024-05-08 01:36:00          200139933   857296\n",
       "4769605  646672581  2024-05-08 01:36:18          200139934   850774\n",
       "4769606  646672582  2024-05-08 01:36:18          200139934   856446\n",
       "4769607  646672583  2024-05-08 01:36:18          200139934   857101\n",
       "4769608  646672584  2024-05-08 01:36:18          200139934   874566\n",
       "\n",
       "[4769609 rows x 4 columns]"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "polls_user"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "c6f1b81e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 4769609 entries, 0 to 4769608\n",
      "Data columns (total 4 columns):\n",
      " #   Column             Dtype \n",
      "---  ------             ----- \n",
      " 0   id                 int64 \n",
      " 1   created_at         object\n",
      " 2   question_piece_id  int64 \n",
      " 3   user_id            int64 \n",
      "dtypes: int64(3), object(1)\n",
      "memory usage: 145.6+ MB\n"
     ]
    }
   ],
   "source": [
    "polls_user.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "f688b6de",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id                   0\n",
       "created_at           0\n",
       "question_piece_id    0\n",
       "user_id              0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "polls_user.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "ffb40f71",
   "metadata": {},
   "outputs": [],
   "source": [
    "polls_user['created_at'] = pd.to_datetime(polls_user['created_at'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "460e5f15",
   "metadata": {},
   "outputs": [],
   "source": [
    "min = polls_user['created_at'].min()\n",
    "max = polls_user['created_at'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "4b4cb1be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2023-04-28 12:27:49 ~ 2024-05-08 01:36:18\n"
     ]
    }
   ],
   "source": [
    "print(f\"{min} ~ {max}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ebfc7f79",
   "metadata": {},
   "source": [
    "# polls_questionset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "df2c1a27",
   "metadata": {},
   "outputs": [],
   "source": [
    "polls_questionset = pd.read_csv('polls_questionset.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "753cef75",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 158384 entries, 0 to 158383\n",
      "Data columns (total 6 columns):\n",
      " #   Column                  Non-Null Count   Dtype \n",
      "---  ------                  --------------   ----- \n",
      " 0   id                      158384 non-null  int64 \n",
      " 1   question_piece_id_list  158384 non-null  object\n",
      " 2   opening_time            158384 non-null  object\n",
      " 3   status                  158384 non-null  object\n",
      " 4   created_at              158384 non-null  object\n",
      " 5   user_id                 158384 non-null  int64 \n",
      "dtypes: int64(2), object(4)\n",
      "memory usage: 7.3+ MB\n"
     ]
    }
   ],
   "source": [
    "polls_questionset.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "b510af09",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id                        0\n",
       "question_piece_id_list    0\n",
       "opening_time              0\n",
       "status                    0\n",
       "created_at                0\n",
       "user_id                   0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "polls_questionset.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "45e86bae",
   "metadata": {},
   "outputs": [],
   "source": [
    "polls_questionset['created_at'] = pd.to_datetime(polls_questionset['created_at'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "17f66399",
   "metadata": {},
   "outputs": [],
   "source": [
    "min = polls_questionset['created_at'].min()\n",
    "max = polls_questionset['created_at'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "fd4acd18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2023-04-28 12:27:23 ~ 2024-05-07 11:32:30\n"
     ]
    }
   ],
   "source": [
    "print(f\"{min} ~ {max}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "106c572f",
   "metadata": {},
   "source": [
    "# polls_questionreport"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "cf712bb7",
   "metadata": {},
   "outputs": [],
   "source": [
    "polls_questionreport = pd.read_csv('polls_questionreport.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "fe497bbd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 51424 entries, 0 to 51423\n",
      "Data columns (total 5 columns):\n",
      " #   Column       Non-Null Count  Dtype \n",
      "---  ------       --------------  ----- \n",
      " 0   id           51424 non-null  int64 \n",
      " 1   reason       51424 non-null  object\n",
      " 2   created_at   51424 non-null  object\n",
      " 3   question_id  51424 non-null  int64 \n",
      " 4   user_id      51424 non-null  int64 \n",
      "dtypes: int64(3), object(2)\n",
      "memory usage: 2.0+ MB\n"
     ]
    }
   ],
   "source": [
    "polls_questionreport.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e935de32",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id             0\n",
       "reason         0\n",
       "created_at     0\n",
       "question_id    0\n",
       "user_id        0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "polls_questionreport.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dea71c36",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "13e0e1d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "polls_questionreport['created_at'] = pd.to_datetime(polls_questionreport['created_at'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "be9728bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "min = polls_questionreport['created_at'].min()\n",
    "max = polls_questionreport['created_at'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "462bdc83",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2023-04-19 06:20:35 ~ 2024-05-05 14:56:25\n"
     ]
    }
   ],
   "source": [
    "print(f\"{min} ~ {max}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "96420cbf",
   "metadata": {},
   "source": [
    "# polls_questionpiece"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "270dea26",
   "metadata": {},
   "outputs": [],
   "source": [
    "polls_questionpiece = pd.read_csv('polls_questionpiece.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "4577d879",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1265476 entries, 0 to 1265475\n",
      "Data columns (total 5 columns):\n",
      " #   Column       Non-Null Count    Dtype \n",
      "---  ------       --------------    ----- \n",
      " 0   id           1265476 non-null  int64 \n",
      " 1   is_voted     1265476 non-null  int64 \n",
      " 2   created_at   1265476 non-null  object\n",
      " 3   question_id  1265476 non-null  int64 \n",
      " 4   is_skipped   1265476 non-null  int64 \n",
      "dtypes: int64(4), object(1)\n",
      "memory usage: 48.3+ MB\n"
     ]
    }
   ],
   "source": [
    "polls_questionpiece.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "45d4ed54",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id             0\n",
       "is_voted       0\n",
       "created_at     0\n",
       "question_id    0\n",
       "is_skipped     0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "polls_questionpiece.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e53c7014",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "3df83158",
   "metadata": {},
   "outputs": [],
   "source": [
    "polls_questionpiece['created_at'] = pd.to_datetime(polls_questionpiece['created_at'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "1413a423",
   "metadata": {},
   "outputs": [],
   "source": [
    "min = polls_questionpiece['created_at'].min()\n",
    "max = polls_questionpiece['created_at'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "eb290c62",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2023-04-28 12:27:22 ~ 2024-05-07 11:32:30\n"
     ]
    }
   ],
   "source": [
    "print(f\"{min} ~ {max}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7068028a",
   "metadata": {},
   "source": [
    "# polls_question"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "292898e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "polls_question = pd.read_csv('polls_question.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "2c62384c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 5025 entries, 0 to 5024\n",
      "Data columns (total 3 columns):\n",
      " #   Column         Non-Null Count  Dtype \n",
      "---  ------         --------------  ----- \n",
      " 0   id             5025 non-null   int64 \n",
      " 1   question_text  5025 non-null   object\n",
      " 2   created_at     5025 non-null   object\n",
      "dtypes: int64(1), object(2)\n",
      "memory usage: 117.9+ KB\n"
     ]
    }
   ],
   "source": [
    "polls_question.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c0b2a515",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id               0\n",
       "question_text    0\n",
       "created_at       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "polls_question.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a81fb691",
   "metadata": {},
   "source": [
    "------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "4f430ac6",
   "metadata": {},
   "outputs": [],
   "source": [
    "polls_question['created_at'] = pd.to_datetime(polls_question['created_at'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "d73a0b10",
   "metadata": {},
   "outputs": [],
   "source": [
    "min = polls_question['created_at'].min()\n",
    "max = polls_question['created_at'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "13e7b18c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2023-03-31 15:22:53 ~ 2023-06-06 06:15:52\n"
     ]
    }
   ],
   "source": [
    "print(f\"{min} ~ {max}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d3a8a733",
   "metadata": {},
   "source": [
    "# events"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "045137c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "events = pd.read_csv('events.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "259695f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 3 entries, 0 to 2\n",
      "Data columns (total 6 columns):\n",
      " #   Column      Non-Null Count  Dtype \n",
      "---  ------      --------------  ----- \n",
      " 0   id          3 non-null      int64 \n",
      " 1   title       3 non-null      object\n",
      " 2   plus_point  3 non-null      int64 \n",
      " 3   event_type  3 non-null      object\n",
      " 4   is_expired  3 non-null      int64 \n",
      " 5   created_at  3 non-null      object\n",
      "dtypes: int64(3), object(3)\n",
      "memory usage: 276.0+ bytes\n"
     ]
    }
   ],
   "source": [
    "events.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "3bddb3d0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id            0\n",
       "title         0\n",
       "plus_point    0\n",
       "event_type    0\n",
       "is_expired    0\n",
       "created_at    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "events.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6000b6e9",
   "metadata": {},
   "source": [
    "------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "b3353f48",
   "metadata": {},
   "outputs": [],
   "source": [
    "events['created_at'] = pd.to_datetime(events['created_at'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "8501dd48",
   "metadata": {},
   "outputs": [],
   "source": [
    "min = events['created_at'].min()\n",
    "max = events['created_at'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "9fb29cf4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2023-06-20 11:56:38 ~ 2023-09-24 17:05:59\n"
     ]
    }
   ],
   "source": [
    "print(f\"{min} ~ {max}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0652fd04",
   "metadata": {},
   "source": [
    "# event_receipts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "1fd2fad5",
   "metadata": {},
   "outputs": [],
   "source": [
    "event_receipts = pd.read_csv('event_receipts.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "bf673492",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 309 entries, 0 to 308\n",
      "Data columns (total 5 columns):\n",
      " #   Column      Non-Null Count  Dtype \n",
      "---  ------      --------------  ----- \n",
      " 0   id          309 non-null    int64 \n",
      " 1   created_at  309 non-null    object\n",
      " 2   event_id    309 non-null    int64 \n",
      " 3   user_id     309 non-null    int64 \n",
      " 4   plus_point  309 non-null    int64 \n",
      "dtypes: int64(4), object(1)\n",
      "memory usage: 12.2+ KB\n"
     ]
    }
   ],
   "source": [
    "event_receipts.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "121df9c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id            0\n",
       "created_at    0\n",
       "event_id      0\n",
       "user_id       0\n",
       "plus_point    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "event_receipts.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "605fff08",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>created_at</th>\n",
       "      <th>event_id</th>\n",
       "      <th>user_id</th>\n",
       "      <th>plus_point</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2</td>\n",
       "      <td>2023-06-22 09:25:16</td>\n",
       "      <td>1</td>\n",
       "      <td>1193618</td>\n",
       "      <td>500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3</td>\n",
       "      <td>2023-06-22 09:38:53</td>\n",
       "      <td>1</td>\n",
       "      <td>928351</td>\n",
       "      <td>500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4</td>\n",
       "      <td>2023-06-22 10:32:15</td>\n",
       "      <td>1</td>\n",
       "      <td>904872</td>\n",
       "      <td>500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>5</td>\n",
       "      <td>2023-06-22 13:03:06</td>\n",
       "      <td>1</td>\n",
       "      <td>974697</td>\n",
       "      <td>500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>6</td>\n",
       "      <td>2023-06-22 13:40:38</td>\n",
       "      <td>1</td>\n",
       "      <td>1168260</td>\n",
       "      <td>500</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id           created_at  event_id  user_id  plus_point\n",
       "0   2  2023-06-22 09:25:16         1  1193618         500\n",
       "1   3  2023-06-22 09:38:53         1   928351         500\n",
       "2   4  2023-06-22 10:32:15         1   904872         500\n",
       "3   5  2023-06-22 13:03:06         1   974697         500\n",
       "4   6  2023-06-22 13:40:38         1  1168260         500"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "event_receipts.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "20589d1b",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "95d31905",
   "metadata": {},
   "outputs": [],
   "source": [
    "event_receipts['created_at'] = pd.to_datetime(event_receipts['created_at'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "a7fdebfe",
   "metadata": {},
   "outputs": [],
   "source": [
    "min = event_receipts['created_at'].min()\n",
    "max = event_receipts['created_at'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "8478b6f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2023-06-22 09:25:16 ~ 2023-11-21 12:03:02\n"
     ]
    }
   ],
   "source": [
    "print(f\"{min} ~ {max}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3e40dcbb",
   "metadata": {},
   "source": [
    "# accounts_userwithdraw"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "c91e6484",
   "metadata": {},
   "outputs": [],
   "source": [
    "accounts_userwithdraw = pd.read_csv('accounts_userwithdraw.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "a25d94fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 70764 entries, 0 to 70763\n",
      "Data columns (total 3 columns):\n",
      " #   Column      Non-Null Count  Dtype \n",
      "---  ------      --------------  ----- \n",
      " 0   id          70764 non-null  int64 \n",
      " 1   reason      70764 non-null  object\n",
      " 2   created_at  70764 non-null  object\n",
      "dtypes: int64(1), object(2)\n",
      "memory usage: 1.6+ MB\n"
     ]
    }
   ],
   "source": [
    "accounts_userwithdraw.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "1427a46c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id            0\n",
       "reason        0\n",
       "created_at    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accounts_userwithdraw.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "48253f45",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "d798f971",
   "metadata": {},
   "outputs": [],
   "source": [
    "accounts_userwithdraw['created_at'] = pd.to_datetime(accounts_userwithdraw['created_at'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "c604dc65",
   "metadata": {},
   "outputs": [],
   "source": [
    "min = accounts_userwithdraw['created_at'].min()\n",
    "max = accounts_userwithdraw['created_at'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "2a810a67",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2023-03-29 13:22:12 ~ 2024-05-09 08:49:06\n"
     ]
    }
   ],
   "source": [
    "print(f\"{min} ~ {max}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "72fa8d41",
   "metadata": {},
   "source": [
    "# accounts_userquestionrecord"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "c5bd47ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "accounts_userquestionrecord = pd.read_csv('accounts_userquestionrecord.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "31f4e9cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1217558 entries, 0 to 1217557\n",
      "Data columns (total 12 columns):\n",
      " #   Column             Non-Null Count    Dtype \n",
      "---  ------             --------------    ----- \n",
      " 0   id                 1217558 non-null  int64 \n",
      " 1   status             1217558 non-null  object\n",
      " 2   created_at         1217558 non-null  object\n",
      " 3   chosen_user_id     1217558 non-null  int64 \n",
      " 4   question_id        1217558 non-null  int64 \n",
      " 5   user_id            1217558 non-null  int64 \n",
      " 6   question_piece_id  1217558 non-null  int64 \n",
      " 7   has_read           1217558 non-null  int64 \n",
      " 8   answer_status      1217558 non-null  object\n",
      " 9   answer_updated_at  1217558 non-null  object\n",
      " 10  report_count       1217558 non-null  int64 \n",
      " 11  opened_times       1217558 non-null  int64 \n",
      "dtypes: int64(8), object(4)\n",
      "memory usage: 111.5+ MB\n"
     ]
    }
   ],
   "source": [
    "accounts_userquestionrecord.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "58f56e2c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id                   0\n",
       "status               0\n",
       "created_at           0\n",
       "chosen_user_id       0\n",
       "question_id          0\n",
       "user_id              0\n",
       "question_piece_id    0\n",
       "has_read             0\n",
       "answer_status        0\n",
       "answer_updated_at    0\n",
       "report_count         0\n",
       "opened_times         0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accounts_userquestionrecord.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "156288b1",
   "metadata": {},
   "source": [
    "-----"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "9ddec85e",
   "metadata": {},
   "outputs": [],
   "source": [
    "accounts_userquestionrecord['created_at'] = pd.to_datetime(accounts_userquestionrecord['created_at'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "0dd6bb12",
   "metadata": {},
   "outputs": [],
   "source": [
    "min = accounts_userquestionrecord['created_at'].min()\n",
    "max = accounts_userquestionrecord['created_at'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "f56e7afa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2023-04-28 12:27:49 ~ 2024-05-08 01:36:18\n"
     ]
    }
   ],
   "source": [
    "print(f\"{min} ~ {max}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e50bcf47",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
