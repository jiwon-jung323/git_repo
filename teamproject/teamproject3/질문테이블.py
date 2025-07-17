{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "9acb8d5d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from datetime import datetime\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eedb2add",
   "metadata": {},
   "source": [
    "# 유입(회원가입 후) 1달 내 투표에 참여한 유저는, 횟수는?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c1322003",
   "metadata": {},
   "outputs": [],
   "source": [
    "user = pd.read_csv('accounts_user.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a9af7475",
   "metadata": {},
   "outputs": [],
   "source": [
    "userquestionrecord = pd.read_csv('accounts_userquestionrecord.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e938e817",
   "metadata": {},
   "outputs": [],
   "source": [
    "user = user.rename(columns = {'id' : 'user_id'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "73884931",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 677085 entries, 0 to 677084\n",
      "Data columns (total 16 columns):\n",
      " #   Column              Non-Null Count   Dtype  \n",
      "---  ------              --------------   -----  \n",
      " 0   user_id             677085 non-null  int64  \n",
      " 1   is_superuser        677085 non-null  int64  \n",
      " 2   is_staff            677085 non-null  int64  \n",
      " 3   gender              677083 non-null  object \n",
      " 4   point               677085 non-null  int64  \n",
      " 5   friend_id_list      677085 non-null  object \n",
      " 6   is_push_on          677085 non-null  int64  \n",
      " 7   created_at          677085 non-null  object \n",
      " 8   block_user_id_list  677085 non-null  object \n",
      " 9   hide_user_id_list   677085 non-null  object \n",
      " 10  ban_status          677085 non-null  object \n",
      " 11  report_count        677085 non-null  int64  \n",
      " 12  alarm_count         677085 non-null  int64  \n",
      " 13  pending_chat        677085 non-null  int64  \n",
      " 14  pending_votes       677085 non-null  int64  \n",
      " 15  group_id            677082 non-null  float64\n",
      "dtypes: float64(1), int64(9), object(6)\n",
      "memory usage: 82.7+ MB\n"
     ]
    }
   ],
   "source": [
    "user.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "063b6f09",
   "metadata": {},
   "outputs": [],
   "source": [
    "user['signup_date'] = pd.to_datetime(user['created_at'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d7aa33d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "userquestionrecord['vote_date'] = pd.to_datetime(userquestionrecord['created_at'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "09983d7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "merged = user.merge(userquestionrecord, on='user_id')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ca425074",
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
       "      <th>user_id</th>\n",
       "      <th>is_superuser</th>\n",
       "      <th>is_staff</th>\n",
       "      <th>gender</th>\n",
       "      <th>point</th>\n",
       "      <th>friend_id_list</th>\n",
       "      <th>is_push_on</th>\n",
       "      <th>created_at_x</th>\n",
       "      <th>block_user_id_list</th>\n",
       "      <th>hide_user_id_list</th>\n",
       "      <th>...</th>\n",
       "      <th>created_at_y</th>\n",
       "      <th>chosen_user_id</th>\n",
       "      <th>question_id</th>\n",
       "      <th>question_piece_id</th>\n",
       "      <th>has_read</th>\n",
       "      <th>answer_status</th>\n",
       "      <th>answer_updated_at</th>\n",
       "      <th>report_count_y</th>\n",
       "      <th>opened_times</th>\n",
       "      <th>vote_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>838023</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>F</td>\n",
       "      <td>2456</td>\n",
       "      <td>[855552, 861830, 859783, 850186, 868492, 85595...</td>\n",
       "      <td>1</td>\n",
       "      <td>2023-04-19 09:06:00.719792</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>...</td>\n",
       "      <td>2023-04-29 16:22:56</td>\n",
       "      <td>854596</td>\n",
       "      <td>121</td>\n",
       "      <td>1167335</td>\n",
       "      <td>0</td>\n",
       "      <td>N</td>\n",
       "      <td>2023-04-29 16:22:56</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2023-04-29 16:22:56</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>838023</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>F</td>\n",
       "      <td>2456</td>\n",
       "      <td>[855552, 861830, 859783, 850186, 868492, 85595...</td>\n",
       "      <td>1</td>\n",
       "      <td>2023-04-19 09:06:00.719792</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>...</td>\n",
       "      <td>2023-04-30 04:04:50</td>\n",
       "      <td>855117</td>\n",
       "      <td>224</td>\n",
       "      <td>1327698</td>\n",
       "      <td>1</td>\n",
       "      <td>N</td>\n",
       "      <td>2023-04-30 04:04:50</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2023-04-30 04:04:50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>838023</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>F</td>\n",
       "      <td>2456</td>\n",
       "      <td>[855552, 861830, 859783, 850186, 868492, 85595...</td>\n",
       "      <td>1</td>\n",
       "      <td>2023-04-19 09:06:00.719792</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>...</td>\n",
       "      <td>2023-04-30 04:05:01</td>\n",
       "      <td>855340</td>\n",
       "      <td>121</td>\n",
       "      <td>1327699</td>\n",
       "      <td>0</td>\n",
       "      <td>N</td>\n",
       "      <td>2023-04-30 04:05:01</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2023-04-30 04:05:01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>838023</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>F</td>\n",
       "      <td>2456</td>\n",
       "      <td>[855552, 861830, 859783, 850186, 868492, 85595...</td>\n",
       "      <td>1</td>\n",
       "      <td>2023-04-19 09:06:00.719792</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>...</td>\n",
       "      <td>2023-04-30 04:05:08</td>\n",
       "      <td>855953</td>\n",
       "      <td>310</td>\n",
       "      <td>1327700</td>\n",
       "      <td>0</td>\n",
       "      <td>N</td>\n",
       "      <td>2023-04-30 04:05:08</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2023-04-30 04:05:08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>838023</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>F</td>\n",
       "      <td>2456</td>\n",
       "      <td>[855552, 861830, 859783, 850186, 868492, 85595...</td>\n",
       "      <td>1</td>\n",
       "      <td>2023-04-19 09:06:00.719792</td>\n",
       "      <td>[]</td>\n",
       "      <td>[]</td>\n",
       "      <td>...</td>\n",
       "      <td>2023-04-30 04:05:22</td>\n",
       "      <td>854615</td>\n",
       "      <td>203</td>\n",
       "      <td>1327702</td>\n",
       "      <td>0</td>\n",
       "      <td>N</td>\n",
       "      <td>2023-04-30 04:05:22</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2023-04-30 04:05:22</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 29 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   user_id  is_superuser  is_staff gender  point  \\\n",
       "0   838023             0         0      F   2456   \n",
       "1   838023             0         0      F   2456   \n",
       "2   838023             0         0      F   2456   \n",
       "3   838023             0         0      F   2456   \n",
       "4   838023             0         0      F   2456   \n",
       "\n",
       "                                      friend_id_list  is_push_on  \\\n",
       "0  [855552, 861830, 859783, 850186, 868492, 85595...           1   \n",
       "1  [855552, 861830, 859783, 850186, 868492, 85595...           1   \n",
       "2  [855552, 861830, 859783, 850186, 868492, 85595...           1   \n",
       "3  [855552, 861830, 859783, 850186, 868492, 85595...           1   \n",
       "4  [855552, 861830, 859783, 850186, 868492, 85595...           1   \n",
       "\n",
       "                 created_at_x block_user_id_list hide_user_id_list  ...  \\\n",
       "0  2023-04-19 09:06:00.719792                 []                []  ...   \n",
       "1  2023-04-19 09:06:00.719792                 []                []  ...   \n",
       "2  2023-04-19 09:06:00.719792                 []                []  ...   \n",
       "3  2023-04-19 09:06:00.719792                 []                []  ...   \n",
       "4  2023-04-19 09:06:00.719792                 []                []  ...   \n",
       "\n",
       "          created_at_y  chosen_user_id  question_id  question_piece_id  \\\n",
       "0  2023-04-29 16:22:56          854596          121            1167335   \n",
       "1  2023-04-30 04:04:50          855117          224            1327698   \n",
       "2  2023-04-30 04:05:01          855340          121            1327699   \n",
       "3  2023-04-30 04:05:08          855953          310            1327700   \n",
       "4  2023-04-30 04:05:22          854615          203            1327702   \n",
       "\n",
       "   has_read  answer_status    answer_updated_at  report_count_y opened_times  \\\n",
       "0         0              N  2023-04-29 16:22:56               0            0   \n",
       "1         1              N  2023-04-30 04:04:50               0            0   \n",
       "2         0              N  2023-04-30 04:05:01               0            0   \n",
       "3         0              N  2023-04-30 04:05:08               0            0   \n",
       "4         0              N  2023-04-30 04:05:22               0            0   \n",
       "\n",
       "            vote_date  \n",
       "0 2023-04-29 16:22:56  \n",
       "1 2023-04-30 04:04:50  \n",
       "2 2023-04-30 04:05:01  \n",
       "3 2023-04-30 04:05:08  \n",
       "4 2023-04-30 04:05:22  \n",
       "\n",
       "[5 rows x 29 columns]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merged.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d7a01e8c",
   "metadata": {},
   "outputs": [],
   "source": [
    "merged['days_since_signup'] = (merged['vote_date'] - merged['signup_date']).dt.days"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "217e4948",
   "metadata": {},
   "outputs": [],
   "source": [
    "valid_votes = merged[(merged['days_since_signup'] >= 0) & (merged['days_since_signup'] <= 30)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "8794b871",
   "metadata": {},
   "outputs": [],
   "source": [
    "vote_signup = valid_votes.groupby('days_since_signup').count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "681ffe38",
   "metadata": {},
   "outputs": [],
   "source": [
    "vote_signup_count = vote_signup['user_id']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "03dad307",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "days_since_signup\n",
       "0    210684\n",
       "1    169863\n",
       "2    144695\n",
       "3    116593\n",
       "4     93538\n",
       "Name: user_id, dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vote_signup_count.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "29c1d6fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "vote_counts = valid_votes.groupby('user_id').size().reset_index(name='vote_count_within_1_month')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "f6e2a277",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAxYAAAHqCAYAAACZcdjsAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAABohElEQVR4nO3de1hU5fr/8c+IMCDKpCIgHtDaSRpqpqVohZaC5DErKwwljWprmqkd3B087NQyD+2v7k5mWmrZ3t+0nWmEmof8Kp5JSVN3SWiCmCGoKSA+vz+6nJ8jchgWJOT7dV1zXcxa99xzr5FnmNtnPWtsxhgjAAAAALCg2pUuAAAAAEDVR2MBAAAAwDIaCwAAAACW0VgAAAAAsIzGAgAAAIBlNBYAAAAALKOxAAAAAGAZjQUAAAAAy2gsAAAAAFhGYwHgT2v+/Pmy2WzOm7e3t4KCgtSlSxdNmTJFmZmZV7rEYm3evFn33HOPGjduLLvdrsDAQIWHh2v06NEucZ07d1bnzp2vTJGlcPr0ab322mtq3bq1/Pz8VKtWLV133XXq37+/1q1b54xbu3atbDab1q5de+WK/ZNJTU11GQPVqlVT7dq1dddddykxMfFKl1cm/J4AlVf1K10AAFS0efPm6YYbblB+fr4yMzO1YcMGvfbaa5o2bZo++eQTde3a9UqXWMjy5cvVu3dvde7cWVOnTlX9+vWVnp6ubdu2afHixZo+fboz9s0337yClRavoKBAkZGR2r17t5555hndeuutkqQDBw5o2bJl+uabbxQRESFJuvnmm7Vp0ya1aNHiSpb8pzR8+HDFxMSooKBA33//vSZMmKC7775bX3/9te64444rXR6APwmbMcZc6SIAoCLMnz9fjzzyiLZu3ap27dq57EtLS9Ntt92mEydO6MCBAwoMDLxCVV5eRESEfv75Z33//feqXt31/4DOnz+vatWqxoTzmjVrdOedd+r999/XI488Umh/VTqWyurMmTPy9vaWzWYrtC81NVVNmzbV66+/rjFjxji3r1+/XhERERo4cKA++OCDP7LcUjlz5ox8fHwuu2/t2rXq0qWL1qxZU6ln6oCrEe/mAK5KjRs31vTp03Xy5Em98847zu3btm3Tgw8+qCZNmsjHx0dNmjTRQw89pJ9++skZk5qaqurVq2vKlCmF8q5fv142m03//ve/JUnHjh3TY489pkaNGslut6tevXrq1KmTVq1aVWx9x48fl7+/f6GmQlKhD+KXngp14fSXadOmacaMGWratKlq1qyp8PBwJSUlFcq3efNm9erVS3Xr1pW3t7euu+46jRw50iXmwIEDiomJUUBAgOx2u5o3b65//vOfxR7DheOQpPr16192/8XHUtQpLnPmzFGzZs1kt9vVokULffTRR4qLi1OTJk3KdMxFnTpWVM6pU6dq0qRJaty4sby9vdWuXTutXr26xGO/cDwLFy7UqFGjFBQUJB8fH0VERGjnzp2F4rdt26bevXurTp068vb2Vps2bfSvf/3LJebC6X2JiYkaPHiw6tWrpxo1aig3N7fEei52odE+evSoy/aMjAw9/vjjatiwoby8vNS0aVNNmDBB586dc4nLzc3VxIkT1bx5c3l7e6tu3brq0qWLNm7c6Iw5e/asxo4dq6ZNm8rLy0sNGjTQsGHDdOLECZdcTZo0Uc+ePbVkyRK1adNG3t7emjBhgiTp+++/V/fu3VWjRg35+/vriSee0MmTJ906VgB/HE6FAnDVuvvuu+Xh4aH169c7t6Wmpio0NFQPPvig6tSpo/T0dL311lu65ZZbtGfPHvn7+6tJkybq3bu33n77bT377LPy8PBwPn727NkKDg7WPffcI0mKjY3Vjh07NGnSJDVr1kwnTpzQjh07nB+4ixIeHq733ntPI0aM0IABA3TzzTfL09PTreP75z//qRtuuEFvvPGGJOmll17S3XffrYMHD8rhcEiSvvrqK/Xq1UvNmzfXjBkz1LhxY6Wmprqcf79nzx517NjR2YwFBQXpq6++0ogRI/TLL79o3LhxRdbQrl07eXp66qmnntLLL7+sO++8s8gm43LeffddPf7447r33ns1c+ZMZWdna8KECUV+kC7NMbtr9uzZCgkJ0RtvvKHz589r6tSpio6O1rp16xQeHl7i4//2t7/p5ptv1nvvvafs7GyNHz9enTt31s6dO3XttddK+n1mp3v37mrfvr3efvttORwOLV68WA888IB+++03xcXFueQcPHiwevTooQULFuj06dNu/24cPHhQktSsWTPntoyMDN16662qVq2aXn75ZV133XXatGmTXnnlFaWmpmrevHmSpHPnzik6OlrffPONRo4cqTvvvFPnzp1TUlKS0tLS1LFjRxlj1LdvX61evVpjx47V7bffrl27dmncuHHatGmTNm3aJLvd7nzuHTt2aO/evXrxxRfVtGlT+fr66ujRo4qIiJCnp6fefPNNBQYGatGiRXryySfdOlYAfyADAH9S8+bNM5LM1q1bi4wJDAw0zZs3L3L/uXPnzKlTp4yvr6/5xz/+4dy+Zs0aI8ksXbrUue3nn3821atXNxMmTHBuq1mzphk5cqTbtf/yyy/mtttuM5KMJOPp6Wk6duxopkyZYk6ePOkSGxERYSIiIpz3Dx48aCSZli1bmnPnzjm3b9myxUgyH3/8sXPbddddZ6677jpz5syZImuJiooyDRs2NNnZ2S7bn3zySePt7W1+/fXXYo9l7ty5pmbNms5jqV+/vhk4cKBZv369S9yF13TNmjXGGGMKCgpMUFCQad++vUvcTz/9ZDw9PU1ISEiZjvnS1+uCQYMGXTZncHCwy+uTk5Nj6tSpY7p27VrscV84nptvvtmcP3/euT01NdV4enqaRx991LnthhtuMG3atDH5+fkuOXr27Gnq169vCgoKjDH//3d64MCBxT73pcfw2muvmfz8fHP27FmTnJxswsPDTf369c3BgwedsY8//ripWbOm+emnn1xyTJs2zUgy3333nTHGmA8//NBIMnPmzCnyeRMSEowkM3XqVJftn3zyiZFk3n33Xee2kJAQ4+HhYfbt2+cS+9xzzxmbzWaSk5Ndtnfr1s3l9wRA5cGpUACuauaSZWanTp3Sc889p7/85S+qXr26qlevrpo1a+r06dPau3evM65z585q3bq1y+lAb7/9tmw2mx577DHntltvvVXz58/XK6+8oqSkJOXn55eqrrp16+qbb77R1q1b9eqrr6pPnz7av3+/xo4dq5YtW+qXX34pMUePHj1cZlNatWolSc7Tuvbv368ffvhBQ4YMkbe392VznD17VqtXr9Y999yjGjVq6Ny5c87b3XffrbNnz1729KqLDR48WIcPH9ZHH32kESNGqFGjRlq4cKEiIiL0+uuvF/m4ffv2KSMjQ/3793fZ3rhxY3Xq1KlMx1wW/fr1c3l9atWqpV69emn9+vUqKCgo8fExMTEu6x9CQkLUsWNHrVmzRpL03//+V99//70GDBggSYVe4/T0dO3bt88l57333uvWMTz33HPy9PSUt7e3brrpJqWkpGjZsmUup3598cUX6tKli4KDg11qiI6OliTnFby+/PJLeXt7a/DgwUU+39dffy1JhWZa7r//fvn6+hY6laxVq1YusyfS77M4N954o1q3bu2yPSYmxq1jB/DHobEAcNU6ffq0jh8/ruDgYOe2mJgYzZ49W48++qi++uorbdmyRVu3blW9evV05swZl8ePGDFCq1ev1r59+5Sfn685c+bovvvuU1BQkDPmk08+0aBBg/Tee+8pPDxcderU0cCBA5WRkVGqGtu1a6fnnntO//73v3XkyBE9/fTTSk1N1dSpU0t8bN26dV3uXzj15MJxHDt2TJLUsGHDInMcP35c586d06xZs+Tp6elyu/vuuyWpVE2Ow+HQQw89pH/84x/avHmzdu3apcDAQL3wwguFzrm/+LklXXZhfVGL7Us65rK4+N/z4m15eXk6depUmR9/4fgurHMYM2ZModd46NChkgq/xu6cTiZJTz31lLZu3aoNGzZo2rRpys/PV58+fVxOyTt69KiWLVtWqIYbb7zRpYZjx44pODi42EX3x48fV/Xq1VWvXj2X7TabzeXYizue48ePF/naAaicWGMB4Kq1fPlyFRQUOBfyZmdn64svvtC4ceP0/PPPO+Nyc3P166+/Fnp8TEyMnnvuOf3zn/9Uhw4dlJGRoWHDhrnE+Pv764033tAbb7yhtLQ0ff7553r++eeVmZmphIQEt+r19PTUuHHjNHPmTKWkpLh/wJe48KHv8OHDRcbUrl1bHh4eio2NLXRsFzRt2tTt577xxhv14IMP6o033tD+/fudl6G92IUm4dIFxpJK3Zhdjre3t7KzswttL6pButxzZWRkyMvLSzVr1izx+Yp6/IXj8/f3lySNHTtW/fr1u2yO0NBQl/uXuwJUcRo2bOhcsN2pUycFBQXp4Ycf1rhx4zR79mxnHa1atdKkSZMum+NCA16vXj1t2LCh2Ct61a1bV+fOndOxY8dcmgtjjDIyMnTLLbeUeDx169Yt8rUDUDkxYwHgqpSWlqYxY8bI4XDo8ccfl/T7hxtjjMuiUkl67733LnvKi7e3tx577DF98MEHmjFjhm666aYiT9GRfj+F58knn1S3bt20Y8eOYutLT0+/7PYLp2NdPMtSVs2aNdN1112n999/v8jF0DVq1FCXLl20c+dOtWrVSu3atSt0u3SW4GLHjx9XXl7eZfd9//33xR5LaGiogoKCCl0ZKS0tzeXqQ+5q0qSJ9u/f73LMx48fLzLnkiVLdPbsWef9kydPatmyZbr99ttdTrsqyscff+xyyt1PP/2kjRs3Ohva0NBQXX/99fr2228v+/q2a9dOtWrVKuPRXt6AAQPUuXNnzZkzx3maWM+ePZWSkqLrrrvusjVc+HeKjo7W2bNnNX/+/CLz33XXXZKkhQsXumz/9NNPdfr0aef+4nTp0kXfffedvv32W5ftH330kTuHCuAPxIwFgD+9lJQU5/nimZmZ+uabbzRv3jx5eHho6dKlzv9R9fPz0x133KHXX3/defWndevWae7cubrmmmsum3vo0KGaOnWqtm/frvfee89lX3Z2trp06aKYmBjdcMMNqlWrlrZu3aqEhIQi/2f6gqioKDVs2FC9evXSDTfcoPPnzys5OVnTp09XzZo19dRTT5XLa/PPf/5TvXr1UocOHfT000+rcePGSktL01dffaVFixZJkv7xj3/otttu0+23366//vWvatKkiU6ePKn//ve/WrZsmfN8+stZs2aNnnrqKQ0YMEAdO3ZU3bp1lZmZqY8//lgJCQkaOHBgkadiVatWTRMmTNDjjz+u++67T4MHD9aJEyc0YcIE1a9fv8zffxEbG6t33nlHDz/8sOLj43X8+HFNnTpVfn5+l4338PBQt27dNGrUKJ0/f16vvfaacnJynJdELUlmZqbuuecexcfHKzs7W+PGjZO3t7fGjh3rjHnnnXcUHR2tqKgoxcXFqUGDBvr111+1d+9e7dixw3n54vL02muvqX379vr73/+u9957TxMnTtTKlSvVsWNHjRgxQqGhoTp79qxSU1O1YsUKvf3222rYsKEeeughzZs3T0888YT27dunLl266Pz589q8ebOaN2+uBx98UN26dVNUVJSee+455eTkqFOnTs6rQrVp00axsbEl1jdy5Ei9//776tGjh1555RXnVaEuNKQAKqEru3YcACrOhSvoXLh5eXmZgIAAExERYSZPnmwyMzMLPebw4cPm3nvvNbVr1za1atUy3bt3NykpKSYkJMQMGjToss/TuXNnU6dOHfPbb7+5bD979qx54oknTKtWrYyfn5/x8fExoaGhZty4ceb06dPF1v7JJ5+YmJgYc/3115uaNWsaT09P07hxYxMbG2v27NnjElvUVaFef/31QnklmXHjxrls27Rpk4mOjjYOh8PY7XZz3XXXmaefftol5uDBg2bw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n5+v/v376+DBg1q5cqXLbMXl3HzzzfL09NSBAwckSUFBQTp69GihuGPHjjlnHIKCgpwzExdkZWUpPz+/2JjMzExJKvbSuna7XX5+fi43AAAA4M+m1I3F5s2b9eWXX7ps+/DDD9W0aVMFBATosccec1lLUB4uNBUHDhzQqlWrVLdu3RIf89133yk/P1/169eXJIWHhys7O1tbtmxxOZbs7Gx17NjRGZOSkuLypX6JiYmy2+1q27atM2b9+vUul6BNTExUcHBwoVOkAAAAgKtNqRuL8ePHa9euXc77u3fv1pAhQ9S1a1c9//zzWrZsmaZMmeLWk586dUrJyclKTk6WJB08eFDJyclKS0vTuXPndN9992nbtm1atGiRCgoKlJGRoYyMDOeH+x9++EETJ07Utm3blJqaqhUrVuj+++9XmzZt1KlTJ0lS8+bN1b17d8XHxyspKUlJSUmKj49Xz549FRoaKkmKjIxUixYtFBsbq507d2r16tUaM2aM4uPjnTMMMTExstvtiouLU0pKipYuXarJkydzRSgAAABAbjQWycnJuuuuu5z3Fy9erPbt22vOnDkaNWqU/ud//kf/+te/3Hrybdu2qU2bNmrTpo0kadSoUWrTpo1efvllHT58WJ9//rkOHz6sm266SfXr13feNm7cKEny8vLS6tWrFRUVpdDQUI0YMUKRkZFatWqVPDw8nM+zaNEitWzZUpGRkYqMjFSrVq20YMEC534PDw8tX75c3t7e6tSpk/r376++fftq2rRpzpgLl789fPiw2rVrp6FDh2rUqFEu6ycAAACAq1Wpv8ciKyvLZS3BunXr1L17d+f9W265RYcOHXLryTt37lzsN1eX9K3WjRo10rp160p8njp16mjhwoXFxjRu3FhffPFFsTEtW7bU+vXrS3w+AAAA4GpT6hmLwMBAHTx4UJKUl5enHTt2KDw83Ln/5MmT8vT0LP8KAQAAAFR6pW4sunfvrueff17ffPONxo4dqxo1auj222937t+1a5euu+66CikSAAAAQOVW6lOhXnnlFfXr108RERGqWbOmPvjgA3l5eTn3v//++4qMjKyQIgEAAABUbqVuLOrVq6dvvvlG2dnZqlmzpsviaEn697//rZo1a5Z7gQAAAAAqv1I3Fhc4HI7Lbq9Tp47lYgAAAABUTZX+m7cBAAAAVH40FgAAAAAso7EA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0vbt28ucr0mTJoVqtNlsGjZsWJnynTt3Ti+++KKaNm0qHx8fXXvttZo4caLOnz9f5hpPnjypkSNHKiQkRD4+PurYsaO2bt1aqseW9HtsjNH48eMVHBwsHx8fde7cWd99952lnEuWLFFUVJT8/f1ls9mUnJxc5nz5+fl67rnn1LJlS/n6+io4OFgDBw7UkSNHylzf+PHjdcMNN8jX11e1a9dW165dtXnzZkvHfLHHH39cNptNb7zxRpnzxcXFFfqd7NChg6X69u7dq969e8vhcKhWrVrq0KGD0tLSypzzcuPGZrPp9ddfL1O+U6dO6cknn1TDhg3l4+Oj5s2b66233ipzfUePHlVcXJyCg4NVo0YNde/eXQcOHCgyX2neo90ZL6XJ585YKSlfWcZKaWp0Z7y4+3eupLFSmnzujpXS1lja8VKafO6MldLkc2eslCafu2OlpM8fZfm7UtnQWECffPKJRo4cqRdeeEE7d+7U7bffrujo6GL/cBbn9OnTat26tWbPnl0u9a1bt07Dhg1TUlKSVq5cqXPnzikyMlKnT58uU76GDRvq1Vdf1bZt27Rt2zbdeeed6tOnT7kM3q1bt+rdd99Vq1atLOe68cYblZ6e7rzt3r27zLmysrLUqVMneXp66ssvv9SePXs0ffp0S1/WuHXrVpf6Vq5cKUm6//77y5Tvtdde09tvv63Zs2dr7969mjp1ql5//XXNmjWrzDU++uijWrlypRYsWKDdu3crMjJSXbt21c8//1ziY0v6PZ46dapmzJih2bNna+vWrQoKClK3bt108uTJMuc8ffq0OnXqpFdffbVUx1dcvt9++007duzQSy+9pB07dmjJkiXav3+/evfuXeb6mjVrptmzZ2v37t3asGGDmjRposjISB07dqzMOS/47LPPtHnz5hK/2bU0+bp37+7yu7lixYoy5/vhhx9022236YYbbtDatWv17bff6qWXXpK3t3eZc15cW3p6ut5//33ZbDbde++9Zcr39NNPKyEhQQsXLtTevXv19NNPa/jw4frPf/7jdj5jjPr27asff/xR//nPf7Rz506FhISoa9euRb7nluY92p3xUpp87oyVkvKVZayUpkZ3xos7f+dKM1ZKm8+dsVKanO6Ml9Lkc2eslCafO2OlpHxlGSslff4oy9+VSsfgqnfrrbeaJ554wmXbDTfcYJ5//nnLuSWZpUuXWs5zsczMTCPJrFu3rtxy1q5d27z33nuWcpw8edJcf/31ZuXKlSYiIsI89dRTZc41btw407p1a0v1XOy5554zt912W7nlu5ynnnrKXHfddeb8+fNlenyPHj3M4MGDXbb169fPPPzww2XK99tvvxkPDw/zxRdfuGxv3bq1eeGFF9zKdenv8fnz501QUJB59dVXndvOnj1rHA6Hefvtt8uU82IHDx40kszOnTvLXOPlbNmyxUgyP/30U7nky87ONpLMqlWrLNV4+PBh06BBA5OSkmJCQkLMzJkzy5xv0KBBpk+fPqV6fGnyPfDAA2X+HSwq56X69Olj7rzzzjLnu/HGG83EiRNdtt18883mxRdfdDvfvn37jCSTkpLi3Hbu3DlTp04dM2fOnFLVeOl7tNXxUtx7flnGSmn+hrgzVkqb053xUlS+so6Vy+WzMlaKymllvJTmNXRnrFwun5Wxcmm+8hgrxvz/zx/l8XelMmDG4iqXl5en7du3KzIy0mV7ZGSkNm7ceIWqKl52drYkqU6dOpZzFRQUaPHixTp9+rTCw8Mt5Ro2bJh69Oihrl27Wq5Lkg4cOKDg4GA1bdpUDz74oH788ccy5/r888/Vrl073X///QoICFCbNm00Z86ccqlT+v33aOHChRo8eLBsNluZctx2221avXq19u/fL0n69ttvtWHDBt19991lynfu3DkVFBQU+p8yHx8fbdiwoUw5Lzh48KAyMjJcxo3dbldERESlHTfS72PHZrNZmqm6IC8vT++++64cDodat25d5jznz59XbGysnnnmGd14442W65KktWvXKiAgQM2aNVN8fLwyMzPLXNvy5cvVrFkzRUVFKSAgQO3bt7d8eufFjh49quXLl2vIkCFlznHbbbfp888/188//yxjjNasWaP9+/crKirK7Vy5ubmS5DJuPDw85OXlVepxc+l7tNXxUp7v+aXN5+5YKSmnu+PlcvmsjJWi6rMyVi7NaXW8lPQaujtWLpfPyli5NJ/VsXLp54+q+nelkCvd2eDK+vnnn40k83//938u2ydNmmSaNWtmOb/Kecbi/PnzplevXpb/933Xrl3G19fXeHh4GIfDYZYvX24p38cff2zCwsLMmTNnjDHG8ozFihUrzP/+7/+aXbt2OWdAAgMDzS+//FKmfHa73djtdjN27FizY8cO8/bbbxtvb2/zwQcflLnGi33yySfGw8PD/Pzzz2XOcf78efP8888bm81mqlevbmw2m5k8ebKlusLDw01ERIT5+eefzblz58yCBQuMzWZz+3f70t/j//u//zOSCh1vfHy8iYyMLFPOi1XEjMWZM2dM27ZtzYABAyzlW7ZsmfH19TU2m80EBwebLVu2WKpx8uTJplu3bs6ZLqszFosXLzZffPGF2b17t/n8889N69atzY033mjOnj3rdr709HQjydSoUcPMmDHD7Ny500yZMsXYbDazdu3aMtd4sddee83Url3b+d5Rlny5ublm4MCBRpKpXr268fLyMh9++GGZ8uXl5ZmQkBBz//33m19//dXk5uaaKVOmGEml+t2+3Hu0lfFS0nu+u2OlNH9D3B0rxeUsy3gpKl9Zx0pR+ayMlcvltDJeSvPv4s5YKSpfWcfK5fKVdawU9fmjPP6uVAY0Fle5C43Fxo0bXba/8sorJjQ01HL+8m4shg4dakJCQsyhQ4cs5cnNzTUHDhwwW7duNc8//7zx9/c33333XZlypaWlmYCAAJOcnOzcZrWxuNSpU6dMYGCgmT59epke7+npacLDw122DR8+3HTo0KE8yjORkZGmZ8+elnJ8/PHHpmHDhubjjz82u3btMh9++KGpU6eOmT9/fplz/ve//zV33HGHkWQ8PDzMLbfcYgYMGGCaN2/uVp6iGosjR464xD366KMmKiqqTDkvVt6NRV5enunTp49p06aNyc7OtpTv1KlT5sCBA2bTpk1m8ODBpkmTJubo0aNlyrlt2zYTGBjo8ofUamNxqSNHjhhPT0/z6aefup3vwvvjQw895BLXq1cv8+CDD5ZLjaGhoebJJ58sVa6i8r3++uumWbNm5vPPPzfffvutmTVrlqlZs6ZZuXJlmfJt27bNtG7d2jluoqKiTHR0tImOji4x3+Xeo62Ml5Le890dKyXlK8tYKS5nWcbL5fJZGSul/bvpzli5XE4r46U0NbozVorKV9axUlS+soyVoj5/lMfflcqAxuIql5ubazw8PMySJUtcto8YMcLccccdlvOXZ2Px5JNPmoYNG5off/yxXPJd7K677jKPPfZYmR67dOlS55vKhZskY7PZjIeHhzl37ly51Ni1a9dCa2FKq3HjxmbIkCEu2958800THBxsua7U1FRTrVo189lnn1nK07BhQzN79myXbX//+9/LpcE9deqU8826f//+5u6773br8Zf+Hv/www9GktmxY4dLXO/evc3AgQPLlPNi5dlY5OXlmb59+5pWrVq5NeNV2rH7l7/8pdQzS5fmnDlzpnOcXDx2qlWrZkJCQsq1xovPWy5tvtzcXFO9enXz97//3SXu2WefNR07diwxX0k1rl+/3khy+U8Jd/P99ttvxtPTs9BaoiFDhpTqw0hx9Z04ccJkZmYaY35fizd06NBicxX1Hl3W8VKa93x3xkpJ+coyVtz9u1TSeCkqX1nHSlnqK2msFJWzrOOlNDW6M1aKylfWsVKa+twdKxe78PmjPP6uVAassbjKeXl5qW3bts4r+lywcuVKdezY8QpV5coYoyeffFJLlizR119/raZNm1bIc1w4X9Jdd911l3bv3q3k5GTnrV27dhowYICSk5Pl4eFhub7c3Fzt3btX9evXL9PjO3XqVOgyefv371dISIjl2ubNm6eAgAD16NHDUp7ffvtN1aq5viV5eHhYutzsBb6+vqpfv76ysrL01VdfqU+fPpbyNW3aVEFBQS7jJi8vT+vWras040b6/TKa/fv314EDB7Rq1SrVrVu33J/DytiJjY3Vrl27XMZOcHCwnnnmGX311VflUt/x48d16NChMo0dLy8v3XLLLRU2dubOnau2bdtaWqOSn5+v/Pz8Chk7DodD9erV04EDB7Rt27Yix01J79Hujpfyfs8vTT53x0pZayxqvJSUz92xUpb6ShorJeV0d7y4U2NpxkpJ+dwdK+7UV9qxUlTdubm5VebvSomuQDODSmbx4sXG09PTzJ071+zZs8eMHDnS+Pr6mtTU1DLlO3nypNm5c6fZuXOnkeQ817K0V9e41F//+lfjcDjM2rVrTXp6uvP222+/lSnf2LFjzfr1683BgwfNrl27zN/+9jdTrVo1k5iYWKZ8l2P1VKjRo0ebtWvXmh9//NEkJSWZnj17mlq1apX532TLli2mevXqZtKkSebAgQNm0aJFpkaNGmbhwoVlrtEYYwoKCkzjxo3Nc889ZymPMb9foaRBgwbmiy++MAcPHjRLliwx/v7+5tlnny1zzoSEBPPll1+aH3/80SQmJprWrVubW2+91eTl5ZX42JJ+j1999VXjcDjMkiVLzO7du81DDz1k6tevb3Jycsqc8/jx42bnzp1m+fLlRpJZvHix2blzp0lPT3c7X35+vundu7dp2LChSU5Odhk7ubm5buc7deqUGTt2rNm0aZNJTU0127dvN0OGDDF2u93lqijuHvOlSjq9o7h8J0+eNKNHjzYbN240Bw8eNGvWrDHh4eGmQYMGRf67lFTfkiVLjKenp3n33XfNgQMHzKxZs4yHh4f55ptvLB1zdna2qVGjhnnrrbeKzFPafBEREebGG280a9asMT/++KOZN2+e8fb2Nm+++WaZ8v3rX/8ya9asMT/88IP57LPPTEhIiOnXr1+R9ZXmPdqd8VKafO6MlZLylWWslJTT3fFSlr9zxY2VkvKVZayUpkZ3xktpj7m0Y6U0+dwZK6XJ5+5YKenzR1n+rlQ2NBYwxhjzz3/+04SEhBgvLy9z8803W7qU65o1a4ykQrdBgwaVKd/lckky8+bNK1O+wYMHO4+1Xr165q677irXpsIY643FAw88YOrXr288PT1NcHCw6devX5nXgFywbNkyExYWZux2u7nhhhvMu+++aymfMcZ89dVXRpLZt2+f5Vw5OTnmqaeeMo0bNzbe3t7m2muvNS+88EKRf9hL45NPPjHXXnut8fLyMkFBQWbYsGHmxIkTpXpsSb/H58+fN+PGjTNBQUHGbrebO+64w+zevdtSznnz5l12/7hx49zOd+EUkcvd1qxZ43a+M2fOmHvuuccEBwcbLy8vU79+fdO7d+8SF6O6+35QUmNRXL7ffvvNREZGmnr16hlPT0/TuHFjM2jQIJOWlmapvrlz55q//OUvxtvb27Ru3brE0/5Kk/Odd94xPj4+pfp9LClfenq6iYuLM8HBwcbb29uEhoaa6dOnF3np55Ly/eMf/zANGzZ0voYvvvhiseOwNO/R7oyX0uRzZ6yUlK8sY6WknO6Ol7L8nSturJSUryxjpbQ1lna8lDZfacdKafK5M1ZKk8/dsVLS54+y/F2pbGzGGCMAAAAAsIA1FgAAAAAso7EAAAAAYBmNBQAAAADLaCwAAAAAWEZjAQAAAMAyGgsAAAAAltFYAAAAALCMxgIAAACAZTQWAIA/BZvNps8+++xKlwEAVy0aCwDAFRcXF6e+ffte6TIAABbQWAAAAACwjMYCAFCpdO7cWSNGjNCzzz6rOnXqKCgoSOPHj3eJOXDggO644w55e3urRYsWWrlyZaE8P//8sx544AHVrl1bdevWVZ8+fZSamipJ+v7771WjRg199NFHzvglS5bI29tbu3fvrsjDA4A/LRoLAECl88EHH8jX11ebN2/W1KlTNXHiRGfzcP78efXr108eHh5KSkrS22+/reeee87l8b/99pu6dOmimjVrav369dqwYYNq1qyp7t27Ky8vTzfccIOmTZumoUOH6qefftKRI0cUHx+vV199VS1btrwShwwAVZ7NGGOudBEAgKtbXFycTpw4oc8++0ydO3dWQUGBvvnmG+f+W2+9VXfeeadeffVVJSYm6u6771ZqaqoaNmwoSUpISFB0dLSWLl2qvn376v3339fUqVO1d+9e2Ww2SVJeXp6uueYaffbZZ4qMjJQk9ezZUzk5OfLy8lK1atX01VdfOeMBAO6pfqULAADgUq1atXK5X79+fWVmZkqS9u7dq8aNGzubCkkKDw93id++fbv++9//qlatWi7bz549qx9++MF5//3331ezZs1UrVo1paSk0FQAgAU0FgCASsfT09Plvs1m0/nz5yVJl5tov7QhOH/+vNq2batFixYViq1Xr57z52+//VanT59WtWrVlJGRoeDg4PIoHwCuSjQWAIAqpUWLFkpLS9ORI0ecjcCmTZtcYm6++WZ98sknCggIkJ+f32Xz/Prrr4qLi9MLL7ygjIwMDRgwQDt27JCPj0+FHwMA/BmxeBsAUKV07dpVoaGhGjhwoL799lt98803euGFF1xiBgwYIH9/f/Xp00fffPONDh48qHXr1umpp57S4cOHJUlPPPGEGjVqpBdffFEzZsyQMUZjxoy5EocEAH8KNBYAgCqlWrVqWrp0qXJzc3Xrrbfq0Ucf1aRJk1xiatSoofXr16tx48bq16+fmjdvrsGDB+vMmTPy8/PThx9+qBUrVmjBggWqXr26atSooUWLFum9997TihUrrtCRAUDVxlWhAAAAAFjGjAUAAAAAy2gsAAAAAFhGYwEAAADAMhoLAAAAAJbRWAAAAACwjMYCAAAAgGU0FgAAAAAso7EAAAAAYBmNBQAAAADLaCwAAAAAWEZjAQAAAMAyGgsAAAAAlv0/8Pw+3rI1sTYAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 800x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(8, 5))\n",
    "plt.bar(vote_signup_count.index.astype(str), vote_signup_count.values, color='salmon')\n",
    "plt.xlabel('Index')\n",
    "plt.ylabel('Days Since Signup')\n",
    "plt.title('Days Since Signup per Record')\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d008a6dc",
   "metadata": {},
   "source": [
    "# 유저 테이블과 연결하여 탈퇴 이유 묶어보기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "24977cb6",
   "metadata": {},
   "outputs": [],
   "source": [
    "userwithdraw = pd.read_csv('accounts_userwithdraw.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "fc8e82c9",
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
       "    </tr>\n",
       "    <tr>\n",
       "      <th>reason</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>admin</th>\n",
       "      <td>61</td>\n",
       "      <td>61</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>test</th>\n",
       "      <td>53</td>\n",
       "      <td>53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>구독료가 너무 비싸서</th>\n",
       "      <td>730</td>\n",
       "      <td>730</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>기타</th>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>기타 이유</th>\n",
       "      <td>40301</td>\n",
       "      <td>40301</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>버그가 너무 많아서</th>\n",
       "      <td>2031</td>\n",
       "      <td>2031</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>재밌는 질문이 없어서</th>\n",
       "      <td>13133</td>\n",
       "      <td>13133</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>함께 할 친구가 없어서</th>\n",
       "      <td>14450</td>\n",
       "      <td>14450</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 id  created_at\n",
       "reason                         \n",
       "admin            61          61\n",
       "test             53          53\n",
       "구독료가 너무 비싸서     730         730\n",
       "기타                5           5\n",
       "기타 이유         40301       40301\n",
       "버그가 너무 많아서     2031        2031\n",
       "재밌는 질문이 없어서   13133       13133\n",
       "함께 할 친구가 없어서  14450       14450"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "userwithdraw.groupby('reason').count()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5054ff90",
   "metadata": {},
   "source": [
    "# 질문테이블을 이용한 질문 중복 확인"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "dbead7a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "question = pd.read_csv('polls_question.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c514bc97",
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
       "      <th>question_text</th>\n",
       "      <th>created_at</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>99</td>\n",
       "      <td>가장 신비한 매력이 있는 사람은?</td>\n",
       "      <td>2023-03-31 15:22:53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>100</td>\n",
       "      <td>\"이 사람으로 한 번 살아보고 싶다\" 하는 사람은?</td>\n",
       "      <td>2023-03-31 15:22:53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>101</td>\n",
       "      <td>미래의 틱톡커는?</td>\n",
       "      <td>2023-03-31 15:22:54</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>102</td>\n",
       "      <td>여기서 제일 특이한 친구는?</td>\n",
       "      <td>2023-03-31 15:22:54</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>103</td>\n",
       "      <td>가장 지켜주고 싶은 사람은?</td>\n",
       "      <td>2023-03-31 15:22:55</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5020</th>\n",
       "      <td>5129</td>\n",
       "      <td>나에게 가장 중요한 사람은?</td>\n",
       "      <td>2023-06-06 06:15:52</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5021</th>\n",
       "      <td>5130</td>\n",
       "      <td>오목을 제일 잘 할 것 같은 사람은?</td>\n",
       "      <td>2023-06-06 06:15:52</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5022</th>\n",
       "      <td>5131</td>\n",
       "      <td>가방에서 쓰레기가 안 나올 것 같은 사람은?</td>\n",
       "      <td>2023-06-06 06:15:52</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5023</th>\n",
       "      <td>5132</td>\n",
       "      <td>아무리 많은 숙제도 30분만에 다 끝내버릴 수 있을 것 같은 친구는?</td>\n",
       "      <td>2023-06-06 06:15:52</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5024</th>\n",
       "      <td>5133</td>\n",
       "      <td>러브레터를 가장 잘 쓸 것 같은 사람은?</td>\n",
       "      <td>2023-06-06 06:15:52</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5025 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        id                           question_text           created_at\n",
       "0       99                      가장 신비한 매력이 있는 사람은?  2023-03-31 15:22:53\n",
       "1      100            \"이 사람으로 한 번 살아보고 싶다\" 하는 사람은?  2023-03-31 15:22:53\n",
       "2      101                               미래의 틱톡커는?  2023-03-31 15:22:54\n",
       "3      102                         여기서 제일 특이한 친구는?  2023-03-31 15:22:54\n",
       "4      103                         가장 지켜주고 싶은 사람은?  2023-03-31 15:22:55\n",
       "...    ...                                     ...                  ...\n",
       "5020  5129                         나에게 가장 중요한 사람은?  2023-06-06 06:15:52\n",
       "5021  5130                    오목을 제일 잘 할 것 같은 사람은?  2023-06-06 06:15:52\n",
       "5022  5131                가방에서 쓰레기가 안 나올 것 같은 사람은?  2023-06-06 06:15:52\n",
       "5023  5132  아무리 많은 숙제도 30분만에 다 끝내버릴 수 있을 것 같은 친구는?  2023-06-06 06:15:52\n",
       "5024  5133                  러브레터를 가장 잘 쓸 것 같은 사람은?  2023-06-06 06:15:52\n",
       "\n",
       "[5025 rows x 3 columns]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "question"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "0554a289",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "중복된 질문 목록:\n",
      "        id                         question_text\n",
      "4305  4414  1000만원 주고 365일 학교 오라고 하면 올 것 같은 사람은?\n",
      "3322  3431  1000만원 주고 365일 학교 오라고 하면 올 것 같은 사람은?\n",
      "3670  3779                  10년 후에 건물주일 것  같은 사람\n",
      "4653  4762                  10년 후에 건물주일 것  같은 사람\n",
      "3458  3567            20년 뒤 돈 많은 백수가 될 것 같은 사람은?\n",
      "...    ...                                   ...\n",
      "3358  3467       힌트 없이도 내가 누군지 맞출 수 있을 것 같은 친구는?\n",
      "4434  4543                   힘을 숨기고 있을 것 같은 사람은?\n",
      "3451  3560                   힘을 숨기고 있을 것 같은 사람은?\n",
      "4490  4599          힙합 남친을 두면 가장 잘 어울릴 것 같은 사람은?\n",
      "3507  3616          힙합 남친을 두면 가장 잘 어울릴 것 같은 사람은?\n",
      "\n",
      "[2185 rows x 2 columns]\n"
     ]
    }
   ],
   "source": [
    "duplicates = question[question.duplicated('question_text', keep=False)]\n",
    "\n",
    "# 중복된 질문 출력\n",
    "print(\"중복된 질문 목록:\")\n",
    "print(duplicates[['id', 'question_text']].sort_values('question_text'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "7f1b0029",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "중복 질문과 간격:\n",
      "        id                         question_text          created_at  \\\n",
      "3322  3431  1000만원 주고 365일 학교 오라고 하면 올 것 같은 사람은? 2023-06-06 06:10:08   \n",
      "4305  4414  1000만원 주고 365일 학교 오라고 하면 올 것 같은 사람은? 2023-06-06 06:15:42   \n",
      "3670  3779                  10년 후에 건물주일 것  같은 사람 2023-06-06 06:10:12   \n",
      "4653  4762                  10년 후에 건물주일 것  같은 사람 2023-06-06 06:15:47   \n",
      "3458  3567            20년 뒤 돈 많은 백수가 될 것 같은 사람은? 2023-06-06 06:10:10   \n",
      "...    ...                                   ...                 ...   \n",
      "4341  4450       힌트 없이도 내가 누군지 맞출 수 있을 것 같은 친구는? 2023-06-06 06:15:42   \n",
      "3451  3560                   힘을 숨기고 있을 것 같은 사람은? 2023-06-06 06:10:09   \n",
      "4434  4543                   힘을 숨기고 있을 것 같은 사람은? 2023-06-06 06:15:44   \n",
      "3507  3616          힙합 남친을 두면 가장 잘 어울릴 것 같은 사람은? 2023-06-06 06:10:10   \n",
      "4490  4599          힙합 남친을 두면 가장 잘 어울릴 것 같은 사람은? 2023-06-06 06:15:44   \n",
      "\n",
      "           time_diff  \n",
      "3322             NaT  \n",
      "4305 0 days 00:05:34  \n",
      "3670             NaT  \n",
      "4653 0 days 00:05:35  \n",
      "3458             NaT  \n",
      "...              ...  \n",
      "4341 0 days 00:05:34  \n",
      "3451             NaT  \n",
      "4434 0 days 00:05:35  \n",
      "3507             NaT  \n",
      "4490 0 days 00:05:34  \n",
      "\n",
      "[2185 rows x 4 columns]\n"
     ]
    }
   ],
   "source": [
    "# created_at 컬럼을 datetime으로 변환\n",
    "question['created_at'] = pd.to_datetime(question['created_at'])\n",
    "\n",
    "# 중복 질문만 추출\n",
    "duplicates = question[question.duplicated('question_text', keep=False)]\n",
    "\n",
    "# 중복 질문을 question_text로 묶고, 생성일 기준 정렬\n",
    "duplicates = duplicates.sort_values(['question_text', 'created_at'])\n",
    "\n",
    "# 각 중복 그룹에서 시간 간격 계산\n",
    "duplicates['time_diff'] = duplicates.groupby('question_text')['created_at'].diff()\n",
    "\n",
    "print(\"중복 질문과 간격:\")\n",
    "print(duplicates[['id', 'question_text', 'created_at', 'time_diff']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "39ed9f22",
   "metadata": {},
   "outputs": [],
   "source": [
    "duplicates_time = duplicates['time_diff']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "83a85f68",
   "metadata": {},
   "outputs": [],
   "source": [
    "duplicates_time = duplicates_time.dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "38a6b5e4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4305    0 days 00:05:34\n",
       "4653    0 days 00:05:35\n",
       "4441    0 days 00:05:34\n",
       "4596    0 days 00:05:34\n",
       "3054   17 days 18:08:08\n",
       "             ...       \n",
       "4809    0 days 00:05:35\n",
       "4871    0 days 00:05:35\n",
       "4341    0 days 00:05:34\n",
       "4434    0 days 00:05:35\n",
       "4490    0 days 00:05:34\n",
       "Name: time_diff, Length: 1122, dtype: timedelta64[ns]"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "duplicates_time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "a9ce80e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Timedelta('1 days 09:29:39.139928698')"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "duplicates_time.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "f2642b0e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1122"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "duplicates_time.count()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e9626a6b",
   "metadata": {},
   "source": [
    "# 스킵을 많이 당한 질문 id"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "6fd65cbe",
   "metadata": {},
   "outputs": [],
   "source": [
    "questionpiece = pd.read_csv('polls_questionpiece.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "adfe3cdb",
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
       "      <th>is_voted</th>\n",
       "      <th>created_at</th>\n",
       "      <th>question_id</th>\n",
       "      <th>is_skipped</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>998458</td>\n",
       "      <td>1</td>\n",
       "      <td>2023-04-28 12:27:22</td>\n",
       "      <td>252</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>998459</td>\n",
       "      <td>1</td>\n",
       "      <td>2023-04-28 12:27:22</td>\n",
       "      <td>244</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>998460</td>\n",
       "      <td>1</td>\n",
       "      <td>2023-04-28 12:27:22</td>\n",
       "      <td>183</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>998461</td>\n",
       "      <td>1</td>\n",
       "      <td>2023-04-28 12:27:22</td>\n",
       "      <td>101</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>998462</td>\n",
       "      <td>1</td>\n",
       "      <td>2023-04-28 12:27:22</td>\n",
       "      <td>209</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1265471</th>\n",
       "      <td>208385226</td>\n",
       "      <td>0</td>\n",
       "      <td>2024-05-07 11:32:30</td>\n",
       "      <td>960</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1265472</th>\n",
       "      <td>208385227</td>\n",
       "      <td>0</td>\n",
       "      <td>2024-05-07 11:32:30</td>\n",
       "      <td>1402</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1265473</th>\n",
       "      <td>208385228</td>\n",
       "      <td>0</td>\n",
       "      <td>2024-05-07 11:32:30</td>\n",
       "      <td>1676</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1265474</th>\n",
       "      <td>208385229</td>\n",
       "      <td>0</td>\n",
       "      <td>2024-05-07 11:32:30</td>\n",
       "      <td>3115</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1265475</th>\n",
       "      <td>208385230</td>\n",
       "      <td>0</td>\n",
       "      <td>2024-05-07 11:32:30</td>\n",
       "      <td>1461</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1265476 rows × 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                id  is_voted           created_at  question_id  is_skipped\n",
       "0           998458         1  2023-04-28 12:27:22          252           0\n",
       "1           998459         1  2023-04-28 12:27:22          244           0\n",
       "2           998460         1  2023-04-28 12:27:22          183           0\n",
       "3           998461         1  2023-04-28 12:27:22          101           0\n",
       "4           998462         1  2023-04-28 12:27:22          209           0\n",
       "...            ...       ...                  ...          ...         ...\n",
       "1265471  208385226         0  2024-05-07 11:32:30          960           0\n",
       "1265472  208385227         0  2024-05-07 11:32:30         1402           0\n",
       "1265473  208385228         0  2024-05-07 11:32:30         1676           0\n",
       "1265474  208385229         0  2024-05-07 11:32:30         3115           0\n",
       "1265475  208385230         0  2024-05-07 11:32:30         1461           0\n",
       "\n",
       "[1265476 rows x 5 columns]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "questionpiece"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "5e849b4c",
   "metadata": {},
   "outputs": [],
   "source": [
    "questionpiece_skip = questionpiece[['question_id', 'is_voted', 'is_skipped']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "288241e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "questionpiece_vote_skip = questionpiece_skip.groupby('question_id').sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "6ccac23a",
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
       "      <th>is_voted</th>\n",
       "      <th>is_skipped</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>question_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>99</th>\n",
       "      <td>1696</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>100</th>\n",
       "      <td>1701</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101</th>\n",
       "      <td>1817</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>102</th>\n",
       "      <td>1946</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>103</th>\n",
       "      <td>1632</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5129</th>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5130</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5131</th>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5132</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5133</th>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>4944 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             is_voted  is_skipped\n",
       "question_id                      \n",
       "99               1696           0\n",
       "100              1701           0\n",
       "101              1817           0\n",
       "102              1946           0\n",
       "103              1632           1\n",
       "...               ...         ...\n",
       "5129                3           0\n",
       "5130                1           0\n",
       "5131                2           0\n",
       "5132                1           0\n",
       "5133                3           0\n",
       "\n",
       "[4944 rows x 2 columns]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "questionpiece_vote_skip"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "7325c8ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "최대 투표수 질문 ID: 170, 투표수: 1998\n"
     ]
    }
   ],
   "source": [
    "max_voted = questionpiece_vote_skip['is_voted'].idxmax()\n",
    "max_voted_count = questionpiece_vote_skip.loc[max_voted, 'is_voted']\n",
    "\n",
    "print(f\"최대 투표수 질문 ID: {max_voted}, 투표수: {max_voted_count}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "7875a458",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "최대 투표수 질문 ID: 4157, 투표수: 0\n"
     ]
    }
   ],
   "source": [
    "min_voted = questionpiece_vote_skip['is_voted'].idxmin()\n",
    "min_voted_count = questionpiece_vote_skip.loc[min_voted, 'is_voted']\n",
    "\n",
    "print(f\"최대 투표수 질문 ID: {min_voted}, 투표수: {min_voted_count}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "8794f749",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "최대 스킵수 질문 ID: 362, 스킵수: 5\n"
     ]
    }
   ],
   "source": [
    "max_skipped = questionpiece_vote_skip['is_skipped'].idxmax()\n",
    "max_skipped_count = questionpiece_vote_skip.loc[max_skipped, 'is_skipped']\n",
    "\n",
    "print(f\"최대 스킵수 질문 ID: {max_skipped}, 스킵수: {max_skipped_count}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a392c43",
   "metadata": {},
   "source": [
    "# 유지 관련 확인 필요: 질문으로 인해 신고받은 유저 top 10과 이유 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "8f429eb4",
   "metadata": {},
   "outputs": [],
   "source": [
    "questionreport = pd.read_csv('polls_questionreport.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "003ddf16",
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
       "      <th>reason</th>\n",
       "      <th>created_at</th>\n",
       "      <th>question_id</th>\n",
       "      <th>user_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>이 질문은 재미없어요</td>\n",
       "      <td>2023-04-19 06:20:35</td>\n",
       "      <td>250</td>\n",
       "      <td>837556</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>이 질문은 재미없어요</td>\n",
       "      <td>2023-04-19 06:58:09</td>\n",
       "      <td>113</td>\n",
       "      <td>837672</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>불쾌한 내용이 포함되어 있음</td>\n",
       "      <td>2023-04-19 06:58:17</td>\n",
       "      <td>113</td>\n",
       "      <td>837672</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>어떻게 이런 생각을? 이 질문 최고!</td>\n",
       "      <td>2023-04-19 08:12:42</td>\n",
       "      <td>119</td>\n",
       "      <td>837922</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>어떻게 이런 생각을? 이 질문 최고!</td>\n",
       "      <td>2023-04-19 08:12:50</td>\n",
       "      <td>119</td>\n",
       "      <td>837922</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id                reason           created_at  question_id  user_id\n",
       "0   1           이 질문은 재미없어요  2023-04-19 06:20:35          250   837556\n",
       "1   2           이 질문은 재미없어요  2023-04-19 06:58:09          113   837672\n",
       "2   3       불쾌한 내용이 포함되어 있음  2023-04-19 06:58:17          113   837672\n",
       "3   4  어떻게 이런 생각을? 이 질문 최고!  2023-04-19 08:12:42          119   837922\n",
       "4   5  어떻게 이런 생각을? 이 질문 최고!  2023-04-19 08:12:50          119   837922"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "questionreport.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "aa638a29",
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
       "      <th>question_id</th>\n",
       "      <th>user_id</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>reason</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>그냥 싫어</th>\n",
       "      <td>28446</td>\n",
       "      <td>28446</td>\n",
       "      <td>28446</td>\n",
       "      <td>28446</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>기타</th>\n",
       "      <td>480</td>\n",
       "      <td>480</td>\n",
       "      <td>480</td>\n",
       "      <td>480</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>나랑 맞지 않는 질문인 것 같음</th>\n",
       "      <td>9541</td>\n",
       "      <td>9541</td>\n",
       "      <td>9541</td>\n",
       "      <td>9541</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>불쾌한 내용이 포함되어 있음</th>\n",
       "      <td>250</td>\n",
       "      <td>250</td>\n",
       "      <td>250</td>\n",
       "      <td>250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>불쾌한 질문 내용</th>\n",
       "      <td>5386</td>\n",
       "      <td>5386</td>\n",
       "      <td>5386</td>\n",
       "      <td>5386</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>선정적이거나 자극적인 질문</th>\n",
       "      <td>58</td>\n",
       "      <td>58</td>\n",
       "      <td>58</td>\n",
       "      <td>58</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>어떻게 이런 생각을? 이 질문 최고!</th>\n",
       "      <td>1821</td>\n",
       "      <td>1821</td>\n",
       "      <td>1821</td>\n",
       "      <td>1821</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>오타가 있음</th>\n",
       "      <td>68</td>\n",
       "      <td>68</td>\n",
       "      <td>68</td>\n",
       "      <td>68</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>이 질문은 재미없어요</th>\n",
       "      <td>471</td>\n",
       "      <td>471</td>\n",
       "      <td>471</td>\n",
       "      <td>471</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>자꾸 같은 내용의 질문 반복</th>\n",
       "      <td>3202</td>\n",
       "      <td>3202</td>\n",
       "      <td>3202</td>\n",
       "      <td>3202</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>한 친구가 질문을 반복적으로 보냄</th>\n",
       "      <td>1701</td>\n",
       "      <td>1701</td>\n",
       "      <td>1701</td>\n",
       "      <td>1701</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                         id  created_at  question_id  user_id\n",
       "reason                                                       \n",
       "그냥 싫어                 28446       28446        28446    28446\n",
       "기타                      480         480          480      480\n",
       "나랑 맞지 않는 질문인 것 같음      9541        9541         9541     9541\n",
       "불쾌한 내용이 포함되어 있음         250         250          250      250\n",
       "불쾌한 질문 내용              5386        5386         5386     5386\n",
       "선정적이거나 자극적인 질문           58          58           58       58\n",
       "어떻게 이런 생각을? 이 질문 최고!   1821        1821         1821     1821\n",
       "오타가 있음                   68          68           68       68\n",
       "이 질문은 재미없어요             471         471          471      471\n",
       "자꾸 같은 내용의 질문 반복        3202        3202         3202     3202\n",
       "한 친구가 질문을 반복적으로 보냄     1701        1701         1701     1701"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "questionreport.groupby('reason').count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "b9105ac0",
   "metadata": {},
   "outputs": [],
   "source": [
    "questionreport_user = questionreport.groupby('user_id').count().sort_values('question_id' ,ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "aea07c0f",
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
       "      <th>reason</th>\n",
       "      <th>created_at</th>\n",
       "      <th>question_id</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>user_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1441146</th>\n",
       "      <td>865</td>\n",
       "      <td>865</td>\n",
       "      <td>865</td>\n",
       "      <td>865</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1330073</th>\n",
       "      <td>271</td>\n",
       "      <td>271</td>\n",
       "      <td>271</td>\n",
       "      <td>271</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>892516</th>\n",
       "      <td>254</td>\n",
       "      <td>254</td>\n",
       "      <td>254</td>\n",
       "      <td>254</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1518143</th>\n",
       "      <td>167</td>\n",
       "      <td>167</td>\n",
       "      <td>167</td>\n",
       "      <td>167</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1035498</th>\n",
       "      <td>159</td>\n",
       "      <td>159</td>\n",
       "      <td>159</td>\n",
       "      <td>159</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1316535</th>\n",
       "      <td>152</td>\n",
       "      <td>152</td>\n",
       "      <td>152</td>\n",
       "      <td>152</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1006953</th>\n",
       "      <td>151</td>\n",
       "      <td>151</td>\n",
       "      <td>151</td>\n",
       "      <td>151</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1377605</th>\n",
       "      <td>140</td>\n",
       "      <td>140</td>\n",
       "      <td>140</td>\n",
       "      <td>140</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1382117</th>\n",
       "      <td>129</td>\n",
       "      <td>129</td>\n",
       "      <td>129</td>\n",
       "      <td>129</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>962059</th>\n",
       "      <td>118</td>\n",
       "      <td>118</td>\n",
       "      <td>118</td>\n",
       "      <td>118</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          id  reason  created_at  question_id\n",
       "user_id                                      \n",
       "1441146  865     865         865          865\n",
       "1330073  271     271         271          271\n",
       "892516   254     254         254          254\n",
       "1518143  167     167         167          167\n",
       "1035498  159     159         159          159\n",
       "1316535  152     152         152          152\n",
       "1006953  151     151         151          151\n",
       "1377605  140     140         140          140\n",
       "1382117  129     129         129          129\n",
       "962059   118     118         118          118"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "questionreport_user.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "9751e354",
   "metadata": {},
   "outputs": [],
   "source": [
    "questionreport_1441146 = questionreport[questionreport['user_id'] == 1441146]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "161e21ae",
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
       "      <th>question_id</th>\n",
       "      <th>user_id</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>reason</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>그냥 싫어</th>\n",
       "      <td>865</td>\n",
       "      <td>865</td>\n",
       "      <td>865</td>\n",
       "      <td>865</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         id  created_at  question_id  user_id\n",
       "reason                                       \n",
       "그냥 싫어   865         865          865      865"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "questionreport_1441146.groupby('reason').count()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0baeface",
   "metadata": {},
   "source": [
    "# 유입 후 한달간 opening_time 질문이 가장 오래 오픈되는 요일, 시간대"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "4a7ced15",
   "metadata": {},
   "outputs": [],
   "source": [
    "questionset = pd.read_csv('polls_questionset.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "90ebcb80",
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
       "      <th>question_piece_id_list</th>\n",
       "      <th>opening_time</th>\n",
       "      <th>status</th>\n",
       "      <th>created_at</th>\n",
       "      <th>user_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>99817</td>\n",
       "      <td>[998458, 998459, 998460, 998461, 998462, 99846...</td>\n",
       "      <td>2023-04-28 12:27:22</td>\n",
       "      <td>F</td>\n",
       "      <td>2023-04-28 12:27:23</td>\n",
       "      <td>849436</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>99830</td>\n",
       "      <td>[998588, 998589, 998590, 998591, 998592, 99859...</td>\n",
       "      <td>2023-04-28 12:28:07</td>\n",
       "      <td>F</td>\n",
       "      <td>2023-04-28 12:28:07</td>\n",
       "      <td>849438</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>99840</td>\n",
       "      <td>[998689, 998691, 998693, 998695, 998697, 99869...</td>\n",
       "      <td>2023-04-28 12:28:38</td>\n",
       "      <td>F</td>\n",
       "      <td>2023-04-28 12:28:38</td>\n",
       "      <td>847375</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>99841</td>\n",
       "      <td>[998688, 998690, 998692, 998694, 998696, 99869...</td>\n",
       "      <td>2023-04-28 12:28:38</td>\n",
       "      <td>F</td>\n",
       "      <td>2023-04-28 12:28:38</td>\n",
       "      <td>849446</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>99848</td>\n",
       "      <td>[998768, 998769, 998770, 998771, 998772, 99877...</td>\n",
       "      <td>2023-04-28 12:28:57</td>\n",
       "      <td>F</td>\n",
       "      <td>2023-04-28 12:28:57</td>\n",
       "      <td>849477</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      id                             question_piece_id_list  \\\n",
       "0  99817  [998458, 998459, 998460, 998461, 998462, 99846...   \n",
       "1  99830  [998588, 998589, 998590, 998591, 998592, 99859...   \n",
       "2  99840  [998689, 998691, 998693, 998695, 998697, 99869...   \n",
       "3  99841  [998688, 998690, 998692, 998694, 998696, 99869...   \n",
       "4  99848  [998768, 998769, 998770, 998771, 998772, 99877...   \n",
       "\n",
       "          opening_time status           created_at  user_id  \n",
       "0  2023-04-28 12:27:22      F  2023-04-28 12:27:23   849436  \n",
       "1  2023-04-28 12:28:07      F  2023-04-28 12:28:07   849438  \n",
       "2  2023-04-28 12:28:38      F  2023-04-28 12:28:38   847375  \n",
       "3  2023-04-28 12:28:38      F  2023-04-28 12:28:38   849446  \n",
       "4  2023-04-28 12:28:57      F  2023-04-28 12:28:57   849477  "
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "questionset.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "0ad76e60",
   "metadata": {},
   "outputs": [],
   "source": [
    "questionset['created_questionset'] = pd.to_datetime(questionset['created_at'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "259c3011",
   "metadata": {},
   "outputs": [],
   "source": [
    "questionset['weekday'] = questionset['created_questionset'].dt.dayofweek  # Monday=0, Sunday=6\n",
    "questionset['weekday_name'] = questionset['created_questionset'].dt.day_name()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "b441c75c",
   "metadata": {},
   "outputs": [],
   "source": [
    "questionset['hour'] = questionset['created_questionset'].dt.hour\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "e78b216e",
   "metadata": {},
   "outputs": [],
   "source": [
    "weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "9f16f6b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "pivot_table = questionset.groupby(['weekday_name', 'hour']).size().reset_index(name='count')\n",
    "pivot_table = pivot_table.pivot(index='weekday_name', columns='hour', values='count').fillna(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "3b5634ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "pivot_table = pivot_table.reindex(weekday_order)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "c83b4780",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 1200x600 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(12, 6))\n",
    "sns.heatmap(pivot_table, cmap='YlGnBu', linewidths=.5, annot=True, fmt=\".0f\")\n",
    "plt.title('Heatmap: Count by Weekday and Hour')\n",
    "plt.xlabel('Hour')\n",
    "plt.ylabel('Weekday')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "d8b4dbf9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def time_period(hour):\n",
    "    if 0 <= hour < 6:\n",
    "        return '새벽'\n",
    "    elif 6 <= hour < 12:\n",
    "        return '아침'\n",
    "    elif 12 <= hour < 18:\n",
    "        return '점심'\n",
    "    else:\n",
    "        return '저녁'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "c35d183f",
   "metadata": {},
   "outputs": [],
   "source": [
    "questionset['time_period'] = questionset['hour'].apply(time_period)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "f35b5b5d",
   "metadata": {},
   "outputs": [],
   "source": [
    "time_period_order = ['새벽', '아침', '점심', '저녁']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c6870dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "pivot_table = questionset.groupby(['weekday_name', 'time_period']).size().reset_index(name='count')\n",
    "pivot_table = pivot_table.pivot(index='weekday_name', columns='time_period', values='count').fillna(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "09c03d28",
   "metadata": {},
   "outputs": [],
   "source": [
    "pivot_table = pivot_table.reindex(weekday_order)[time_period_order]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "d6aa251f",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\Users\\jewji\\anaconda3\\Lib\\site-packages\\seaborn\\utils.py:61: UserWarning: Glyph 49352 (\\N{HANGUL SYLLABLE SAE}) missing from font(s) DejaVu Sans.\n",
      "  fig.canvas.draw()\n",
      "c:\\Users\\jewji\\anaconda3\\Lib\\site-packages\\seaborn\\utils.py:61: UserWarning: Glyph 48317 (\\N{HANGUL SYLLABLE BYEOG}) missing from font(s) DejaVu Sans.\n",
      "  fig.canvas.draw()\n",
      "c:\\Users\\jewji\\anaconda3\\Lib\\site-packages\\seaborn\\utils.py:61: UserWarning: Glyph 50500 (\\N{HANGUL SYLLABLE A}) missing from font(s) DejaVu Sans.\n",
      "  fig.canvas.draw()\n",
      "c:\\Users\\jewji\\anaconda3\\Lib\\site-packages\\seaborn\\utils.py:61: UserWarning: Glyph 52840 (\\N{HANGUL SYLLABLE CIM}) missing from font(s) DejaVu Sans.\n",
      "  fig.canvas.draw()\n",
      "c:\\Users\\jewji\\anaconda3\\Lib\\site-packages\\seaborn\\utils.py:61: UserWarning: Glyph 51216 (\\N{HANGUL SYLLABLE JEOM}) missing from font(s) DejaVu Sans.\n",
      "  fig.canvas.draw()\n",
      "c:\\Users\\jewji\\anaconda3\\Lib\\site-packages\\seaborn\\utils.py:61: UserWarning: Glyph 49900 (\\N{HANGUL SYLLABLE SIM}) missing from font(s) DejaVu Sans.\n",
      "  fig.canvas.draw()\n",
      "c:\\Users\\jewji\\anaconda3\\Lib\\site-packages\\seaborn\\utils.py:61: UserWarning: Glyph 51200 (\\N{HANGUL SYLLABLE JEO}) missing from font(s) DejaVu Sans.\n",
      "  fig.canvas.draw()\n",
      "c:\\Users\\jewji\\anaconda3\\Lib\\site-packages\\seaborn\\utils.py:61: UserWarning: Glyph 45377 (\\N{HANGUL SYLLABLE NYEOG}) missing from font(s) DejaVu Sans.\n",
      "  fig.canvas.draw()\n",
      "c:\\Users\\jewji\\anaconda3\\Lib\\site-packages\\IPython\\core\\pylabtools.py:170: UserWarning: Glyph 49352 (\\N{HANGUL SYLLABLE SAE}) missing from font(s) DejaVu Sans.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "c:\\Users\\jewji\\anaconda3\\Lib\\site-packages\\IPython\\core\\pylabtools.py:170: UserWarning: Glyph 48317 (\\N{HANGUL SYLLABLE BYEOG}) missing from font(s) DejaVu Sans.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "c:\\Users\\jewji\\anaconda3\\Lib\\site-packages\\IPython\\core\\pylabtools.py:170: UserWarning: Glyph 50500 (\\N{HANGUL SYLLABLE A}) missing from font(s) DejaVu Sans.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "c:\\Users\\jewji\\anaconda3\\Lib\\site-packages\\IPython\\core\\pylabtools.py:170: UserWarning: Glyph 52840 (\\N{HANGUL SYLLABLE CIM}) missing from font(s) DejaVu Sans.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "c:\\Users\\jewji\\anaconda3\\Lib\\site-packages\\IPython\\core\\pylabtools.py:170: UserWarning: Glyph 51216 (\\N{HANGUL SYLLABLE JEOM}) missing from font(s) DejaVu Sans.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "c:\\Users\\jewji\\anaconda3\\Lib\\site-packages\\IPython\\core\\pylabtools.py:170: UserWarning: Glyph 49900 (\\N{HANGUL SYLLABLE SIM}) missing from font(s) DejaVu Sans.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "c:\\Users\\jewji\\anaconda3\\Lib\\site-packages\\IPython\\core\\pylabtools.py:170: UserWarning: Glyph 51200 (\\N{HANGUL SYLLABLE JEO}) missing from font(s) DejaVu Sans.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "c:\\Users\\jewji\\anaconda3\\Lib\\site-packages\\IPython\\core\\pylabtools.py:170: UserWarning: Glyph 45377 (\\N{HANGUL SYLLABLE NYEOG}) missing from font(s) DejaVu Sans.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n"
     ]
    },
    {
     "data": {
      "image/png": "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A1+tjJODDWcuRTH2k52s3HQm+w5K7srVxYFxw9rg7+tORGQsq34+xAfTVpCcnEqh/J40b1gRgB2rx1ps1+KV6ezYm/b/yOgJ35KSksr8j3tib2/Ltt2/81LvBaqJfwilne+2aec7KpZV637l/WkrSE5OoVB+T55vVAmAnT+9Y7Hd850+ZMfeP6hUrjDVK6clKEI2T7BoU772KC7+eYP4+CRaNanM6EEtcXS042p4FBu2HaXboLn/mvmUB2fFst0AvNH9C4vlo9/rQPPW1bHKY+LCuXDWrjpAVGQMru5OlClbgE+D+1GsRNqNi3a21vz26zmWLdrO7Vtx5PV0pmLVYnzxVX88PNNu0nf3cGLaZz2Y88k6BvWcTXJyCkWL+zDpo66ULP3k/O2U3PNEzUP9KIqNjcXf35+goCDatm37n/p41Oehlvv3KM5DLf/dozgPtfx3j8M81HL/cnMe6viU3dnWt32ex/Op1E9UhvpRkpqaSlhYGNOmTcPNzY1WrXLvB0tERERE7k4B9UPq4sWLFC1alAIFCjB//nysrXWqREREJCeohjqzFKU9pIoUKaI7k0VERCTHmTQJXKbpExMRERERyQJlqEVERETkb1TykVnKUIuIiIiIZIEy1CIiIiJi+OuponL/lKEWEREREckCZahFRERE5G+Uoc4sZahFRERERLJAGWoRERERMWge6sxTQC0iIiIif6OSj8zSVxARERERkSxQhlpEREREDCZlqDNNGWoRERERkSxQhlpEREREDHqwS+YpQy0iIiIikgXKUIuIiIjI3yjfmln6xEREREREskAZahERERExaJaPzFOGWkREREQkC5ShFhEREZG/UYY6sxRQi4iIiIhB0+Zlnko+RERERESyQBlqEREREfkb5VszS5+YiIiIiEgWKEMtIiIiIgZNm5d5ylCLiIiIiGSByWw2m3N7ECIPUkJCApMmTWLUqFHY2dnl9nAkm+l8P1l0vp8sOt/yqFBALY+dW7du4ebmRlRUFK6urrk9HMlmOt9PFp3vJ4vOtzwqVPIhIiIiIpIFCqhFRERERLJAAbWIiIiISBYooJbHjp2dHePGjdMNLE8Ine8ni873k0XnWx4VuilRRERERCQLlKEWEREREckCBdQiIiIiIlmggFpEREREJAsUUIuIiIiIZIF1bg9A5L/YtWsX/fr1y3Bd06ZNOXDg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",
      "text/plain": [
       "<Figure size 800x600 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(8, 6))\n",
    "sns.heatmap(pivot_table, cmap='YlGnBu', linewidths=.5, annot=True, fmt=\".0f\")\n",
    "plt.title('Heatmap: Count by Weekday and Time Period')\n",
    "plt.xlabel('Time Period')\n",
    "plt.ylabel('Weekday')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "4d20e6fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "weekday_counts = questionset['weekday_name'].value_counts().reindex(weekday_order).fillna(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "08bca67c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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FSokpqam0qNHD9myZcsbzW5x5swZad26tRQtWlSKFSsmX375pURGRmb7mgMHDggAmTZt2ku3nZ369esLAPH398+ybsiQIQJAGjdunGXd48eP5ZtvvhF7e3sxMjISrVYr1atXl6FDh0pERIRO2eXLl0uDBg3ExMREChcuLB999JF07txZ5/+e+v+siMjFixfFyspK6tSpo/zff/TokXTv3l1KlCghRYoUkZYtW8rVq1ezHDNiY2OlR48eYmFhIUWKFJEmTZrI4cOHxdnZ+YUztnTt2lUMDAzk7t27r9t8RO+URiQHbldFRET0gRg+fDgWLVqEsLCwLBe10etJSUlB+fLl0aRJkxydkYcoJ3G4BRER0Ws4fvw4rl+/joULF6JPnz4MyG8hOjoa165dw4oVKxAZGYlRo0bldZWIXoghmYiI6DU0atQIRYoUgbe3N7777ru8rk6BtH37dnTr1g2lS5fGwoULOe0b5WscbkFEREREpMIp4IiIiIiIVPI0JC9atAg1atRA8eLFUbx4cTRq1Ag7d+5U1osIJkyYAGtraxQuXBguLi64dOmSzjaSk5MxcOBAmJubw8TEBG3atMHdu3d1ysTGxsLPzw9arRZarRZ+fn549OiRTpk7d+6gdevWMDExgbm5OQYNGoSUlJRc++xERERElH/laUguW7Yspk2bhtOnT+P06dNo3rw52rZtqwTh6dOnY/bs2Zg/fz5OnToFKysrtGzZUueuTUOGDMGmTZsQFBSEI0eO4PHjx/D29kZaWppSxtfXF6GhoQgODkZwcDBCQ0Ph5+enrE9LS4OXlxcSExNx5MgRBAUFYcOGDRg+fPi7awwiIiIiyjfy3ZhkU1NTzJgxA927d4e1tTWGDBmCkSNHAnjea2xpaYkffvgBffr0QVxcHEqVKoWAgAB8/vnnAJ7fctbGxgY7duyAh4cHrly5gqpVq+L48eNo0KABgOdXKDdq1AhXr16Fvb09du7cCW9vb4SFhcHa2hrA81vJdu3aFVFRUShevPhr1T09PR33799HsWLFXvvWr0RERET07ogIEhISYG1tDT29l/QX590UzbqePXsma9asESMjI7l06ZL8/fffAkD++usvnXJt2rSRzp07i4jI3r17BYA8fPhQp0yNGjXk22+/FRGRZcuWiVarzfJ+Wq1Wli9fLiIi48aNkxo1auisf/jwoQCQ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IiJSYUgmIiIiIlJhSCYiIiIiUuHsFkRERK+BswwRfVjYk0xEREREpMKQTERERESkwpBMRERERKTCkExEREREpMKQTERERESkwpBMRERERKTCkExEREREpMKQTERERESkwpBMRERERKTCkExEREREpMKQTERERESkwpBMRERERKTCkExEREREpMKQTERERESkwpBMRERERKTCkExEREREpGKQl28+depUbNy4EVevXkXhwoXh5OSEH374Afb29koZEcHEiRPxyy+/IDY2Fg0aNMCCBQtQrVo1pUxycjL8/f2xZs0aJCUloUWLFli4cCHKli2rlImNjcWgQYOwdetWAECbNm0wb948lChRQilz584d9O/fH/v27UPhwoXh6+uLmTNnwsjIKPcbg+g9N+3sg7yuwhsZVds8r6tARER5KE97kg8ePIj+/fvj+PHj2L17N549ewZ3d3ckJiYqZaZPn47Zs2dj/vz5OHXqFKysrNCyZUskJCQoZYYMGYJNmzYhKCgIR44cwePHj+Ht7Y20tDSljK+vL0JDQxEcHIzg4GCEhobCz89PWZ+WlgYvLy8kJibiyJEjCAoKwoYNGzB8+PB30xhERERElG/kaU9ycHCwzvMVK1bAwsICZ86cQbNmzSAi+PHHHzF27Fh06NABAPDrr7/C0tISq1evRp8+fRAXF4dly5YhICAAbm5uAIDAwEDY2Nhgz5498PDwwJUrVxAcHIzjx4+jQYMGAIAlS5agUaNGuHbtGuzt7RESEoLLly8jLCwM1tbWAIBZs2aha9eu+P7771G8ePF32DL0rhW0Xk6APZ1ERES5KV+NSY6LiwMAmJqaAgBu3bqFiIgIuLu7K2WMjY3h7OyMo0ePAgDOnDmD1NRUnTLW1tZwdHRUyhw7dgxarVYJyADQsGFDaLVanTKOjo5KQAYADw8PJCcn48yZM9nWNzk5GfHx8ToPIiIiIir48k1IFhEMGzYMTZo0gaOjIwAgIiICAGBpaalT1tLSUlkXEREBIyMjlCxZ8qVlLCwssrynhYWFThn1+5QsWRJGRkZKGbWpU6dCq9UqDxsbmzf92ERERESUD+WbkDxgwACcP38ea9asybJOo9HoPBeRLMvU1GWyK/82ZTIbPXo04uLilEdYWNhL60REREREBUO+CMkDBw7E1q1bsX//fp0ZKaysrAAgS09uVFSU0utr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oEGD8PHHH6NatWo4fPhwrlSUiIiIiOhdeaOQ/OOPP77wBhtarRZ9+vTB7Nmzc6xyRERERER54Y1C8rlz5+Dp6fnC9e7u7jhz5sx/rhQRERERUV56o5AcGRmZ7dRvGQwMDBAdHf2fK0VERERElJfeKCSXKVMGFy5ceOH68+fPo3Tp0v+5UkREREREeemNQvInn3yCb7/9Fk+fPs2yLikpCePHj4e3t3eOVY6IiIiIKC+80RRw33zzDTZu3IjKlStjwIABsLe3h0ajwZUrV7BgwQKkpaVh7NixuVVXIiIiIqJ34o1CsqWlJY4ePYqvvvoKo0ePhogAADQaDTw8PLBw4UJYWlrmSkWJiIiIiN6VN76ZiK2tLXbs2IHY2FjcvHkTIoJKlSqhZMmSuVE/IiIiIqJ37q3uuAcAJUuWxMcff5yTdSEiIiIiyhfe6MI9IiIiIqIPAUMyEREREZEKQzIRERERkQpDMhERERGRCkMyEREREZEKQzIRERERkQpDMhERERGRCkMyEREREZEKQzIRERERkQpDMhERERGRCkMyEREREZEKQzIRERERkQpDMhERERGRCkMyEREREZEKQzIRERERkQpDMhERERGRCkMyEREREZEKQzIRERERkQpDMhERERGRCkMyEREREZEKQzIRERERkQpDMhERERGRCkMyEREREZEKQzIRERERkQpDMhERERGRCkMyEREREZEKQzIRERERkQpDMhERERGRCkMyEREREZEKQzIRERERkQpDMhERERGRCkMyEREREZEKQzIRERERkQpDMhERERGRCkMyEREREZEKQzIRERERkQpDMhERERGRCkMyEREREZFKnobkQ4cOoXXr1rC2toZGo8HmzZt11osIJkyYAGtraxQuXBguLi64dOmSTpnk5GQMHDgQ5ubmMDExQZs2bXD37l2dMrGxsfDz84NWq4VWq4Wfnx8ePXqkU+bOnTto3bo1TExMYG5ujkGDBiElJSU3PjYRERER5XN5GpITExNRs2ZNzJ8/P9v106dPx+zZszF//nycOnUKVlZWaNmyJRISEpQyQ4YMwaZNmxAUFIQjR47g8ePH8Pb2RlpamlLG19cXoaGhCA4ORnBwMEJDQ+Hn56esT0tLg5eXFxITE3HkyBEEBQVhw4YNGD58eO59eCIiIiLKtwzy8s1btWqFVq1aZbtORPDjjz9i7Nix6NChAwDg119/haWlJVavXo0+ffogLi4Oy5YtQ0BAANzc3AAAgYGBsLGxwZ49e+Dh4YErV64gODgYx48fR4MGDQAAS5YsQaNGjXDt2jXY29sjJCQEly9fRlhYGKytrQEAs2bNQteuXfH999+jePHi76A1iIiIiCi/yLdjkm/duoWIiAi4u7sry4yNjeHs7IyjR48CAM6cOYPU1FSdMtbW1nB0dFTKHDt2DFqtVgnIANCwYUNotVqdMo6OjkpABgAPDw8kJyfjzJkzL6xjcnIy4uPjdR5EREREVPDl25AcEREBALC0tNRZbmlpqayLiIiAkZERSpYs+dIyFhYWWbZvYWGhU0b9PiVLloSRkZFSJjtTp05VxjlrtVrY2Ni84ackIiIiovwo34bkDBqNRue5iGRZpqYuk135tymjNnr0aMTFxSmPsLCwl9aLiIiIiAqGfBuSraysACBLT25UVJTS62tlZYWUlBTExsa+tExkZGSW7UdHR+uUUb9PbGwsUlNTs/QwZ2ZsbIzixYvrPIiIiIio4Mu3IdnOzg5WVlbYvXu3siwlJQUHDx6Ek5MTAKBu3bowNDTUKRMeHo6LFy8qZRo1aoS4uDicPHlSKXPixAnExcXplLl48SLCw8OVMiEhITA2NkbdunVz9XMSERERUf6Tp7NbPH78GDdv3lSe37p1C6GhoTA1NUW5cuUwZMgQTJkyBZUqVUKlSpUwZcoUFClSBL6+vgAArVaLHj16YPjw4TAzM4OpqSn8/f1RvXp1ZbYLBwcHeHp6olevXvj5558BAL1794a3tzfs7e0BAO7u7qhatSr8/PwwY8YMPHz4EP7+/ujVqxd7h4mIiIg+QHkakk+fPg1XV1fl+bBhwwAAXbp0wcqVKzFixAgkJSWhX79+iI2NRYMGDRASEoJixYopr5kzZw4MDAzg4+ODpKQktGjRAitXroS+vr5SZtWqVRg0aJAyC0abNm105mbW19fH9u3b0a9fPzRu3BiFCxeGr68vZs6cmdtNQERERET5UJ6GZBcXF4jIC9drNBpMmDABEyZMeGGZQoUKYd68eZg3b94Ly5iamiIwMPCldSlXrhy2bdv2yjoTERER0fsv345JJiIiIiLKKwzJREREREQqDMlERERERCoMyUREREREKgzJREREREQqDMlERERERCoMyUREREREKgzJREREREQqDMlERERERCoMyUREREREKgzJREREREQqDMlERERERCoMyUREREREKgzJREREREQqDMlERERERCoMyUREREREKgzJREREREQqDMlERERERCoMyUREREREKgzJREREREQqDMlERERERCoMyUREREREKgzJREREREQqDMlERERERCoMyUREREREKgzJREREREQqDMlERERERCoMyUREREREKgzJREREREQqDMlERERERCoMyUREREREKgzJREREREQqDMlERERERCoMyUREREREKgzJREREREQqDMlERERERCoMyUREREREKgzJREREREQqDMlERERERCoMyUREREREKgzJREREREQqDMlERERERCoMyUREREREKgzJREREREQqDMlERERERCoMyUREREREKgzJREREREQqDMlERERERCoMyUREREREKgzJREREREQqDMlERERERCoMyUREREREKgzJREREREQq+TokT5gwARqNRudhZWWlrBcRTJgwAdbW1ihcuDBcXFxw6dIlnW0kJydj4MCBMDc3h4mJCdq0aYO7d+/qlImNjYWfnx+0Wi20Wi38/Pzw6NGjd/ERiYiIiCgfytchGQCqVauG8PBw5XHhwgVl3fTp0zF79mzMnz8fp06dgpWVFVq2bImEhASlzJAhQ7Bp0yYEBQXhyJEjePz4Mby9vZGWlqaU8fX1RWhoKIKDgxEcHIzQ0FD4+fm9089JRERERPmHQV5X4FUMDAx0eo8ziAh+/PFHjB07Fh06dAAA/Prrr7C0tMTq1avRp08fxMXFYdmyZQgICICbmxsAIDAwEDY2NtizZw88PDxw5coVBAcH4/jx42jQoAEAYMmSJWjUqBGuXbsGe3v7d/dhiYiIiChfyPc9yTdu3IC1tTXs7OzwxRdf4J9//gEA3Lp1CxEREXB3d1fKGhsbw9nZGUePHgUAnDlzBqmpqTplrK2t4ejoqJQ5duwYtFqtEpABoGHDhtBqtUqZF0lOTkZ8fLzOg4iIiIgKvnwdkhs0aIDffvsNu3btwpIlSxAREQEnJyfExMQgIiICAGBpaanzGktLS2VdREQEjIyMULJkyZeWsbCwyPLeFhYWSpkXmTp1qjKOWavVwsbG5q0/KxERERHlH/k6JLdq1QqffvopqlevDjc3N2zfvh3A82EVGTQajc5rRCTLMjV1mezKv852Ro8e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",
      "text/plain": [
       "<Figure size 800x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(8, 5))\n",
    "weekday_counts.plot(kind='bar', color='skyblue')\n",
    "plt.title('Number of Data Created by Weekday')\n",
    "plt.xlabel('Weekday')\n",
    "plt.ylabel('Count')\n",
    "plt.xticks(rotation=45)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "831f0728",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "04a2034b",
   "metadata": {},
   "source": [
    "# 질문 등장 횟수 유저 top 10과 그 유저군의 행동 탐색"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "fd511d24",
   "metadata": {},
   "outputs": [],
   "source": [
    "usercandidate = pd.read_csv('polls_usercandidate.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "1ec8e61f",
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
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        id           created_at  question_piece_id  user_id\n",
       "0  3088872  2023-04-28 12:27:49             998458   849444\n",
       "1  3088873  2023-04-28 12:27:49             998458   849454\n",
       "2  3088874  2023-04-28 12:27:49             998458   849460\n",
       "3  3088875  2023-04-28 12:27:49             998458   849469\n",
       "4  3088964  2023-04-28 12:28:02             998459   849446"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "usercandidate.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "f20e98be",
   "metadata": {},
   "outputs": [],
   "source": [
    "usercandidate_user = usercandidate.groupby('user_id').count().sort_values('question_piece_id', ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "d4e63a25",
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
       "    </tr>\n",
       "    <tr>\n",
       "      <th>user_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>860304</th>\n",
       "      <td>4226</td>\n",
       "      <td>4226</td>\n",
       "      <td>4226</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>940572</th>\n",
       "      <td>4070</td>\n",
       "      <td>4070</td>\n",
       "      <td>4070</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1137034</th>\n",
       "      <td>3948</td>\n",
       "      <td>3948</td>\n",
       "      <td>3948</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1207066</th>\n",
       "      <td>3920</td>\n",
       "      <td>3920</td>\n",
       "      <td>3920</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>994573</th>\n",
       "      <td>3674</td>\n",
       "      <td>3674</td>\n",
       "      <td>3674</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1019558</th>\n",
       "      <td>3664</td>\n",
       "      <td>3664</td>\n",
       "      <td>3664</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1206668</th>\n",
       "      <td>3648</td>\n",
       "      <td>3648</td>\n",
       "      <td>3648</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1017272</th>\n",
       "      <td>3584</td>\n",
       "      <td>3584</td>\n",
       "      <td>3584</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1085141</th>\n",
       "      <td>3562</td>\n",
       "      <td>3562</td>\n",
       "      <td>3562</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>915833</th>\n",
       "      <td>3544</td>\n",
       "      <td>3544</td>\n",
       "      <td>3544</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           id  created_at  question_piece_id\n",
       "user_id                                     \n",
       "860304   4226        4226               4226\n",
       "940572   4070        4070               4070\n",
       "1137034  3948        3948               3948\n",
       "1207066  3920        3920               3920\n",
       "994573   3674        3674               3674\n",
       "1019558  3664        3664               3664\n",
       "1206668  3648        3648               3648\n",
       "1017272  3584        3584               3584\n",
       "1085141  3562        3562               3562\n",
       "915833   3544        3544               3544"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "usercandidate_user.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "4905e651",
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
       "    </tr>\n",
       "    <tr>\n",
       "      <th>user_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>927190</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>927447</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1157929</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1157754</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1157658</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1459327</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1379533</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1157406</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>928162</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1580629</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         id  created_at  question_piece_id\n",
       "user_id                                   \n",
       "927190    1           1                  1\n",
       "927447    1           1                  1\n",
       "1157929   1           1                  1\n",
       "1157754   1           1                  1\n",
       "1157658   1           1                  1\n",
       "1459327   1           1                  1\n",
       "1379533   1           1                  1\n",
       "1157406   1           1                  1\n",
       "928162    1           1                  1\n",
       "1580629   1           1                  1"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "usercandidate_user.tail(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "419f2e10",
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
