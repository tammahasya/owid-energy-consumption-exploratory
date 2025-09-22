#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers.schedules import ExponentialDecay


# In[2]:


df = pd.read_csv("/home/zellha/ML_Stuff/OWID_Energy/data/Fossil_vs_Renew_World.csv")

# Keep only World rows, sort by year
world = df[df["country"] == "World"].sort_values("year")
pct_data = world.loc[:, ["year", "fossil_pct", "renew_pct"]].copy()
years = pct_data["year"].values
energy_pct = pct_data[["fossil_pct", "renew_pct"]].values

# Scale only the energy columns (2 features)
scaler = MinMaxScaler(feature_range=(0, 1))
energy_scaled = scaler.fit_transform(energy_pct)

print("Scaled shape:", energy_scaled.shape)   # (n_years, 2)


# In[3]:


timesteps = 5
X_train, y_train = [], []
for i in range(timesteps, len(energy_scaled)):
    X_train.append(energy_scaled[i - timesteps:i, :])  # all features
    y_train.append(energy_scaled[i, :])                # next step

X_train = np.array(X_train)
y_train = np.array(y_train)

print("X_train:", X_train.shape)  # (samples, timesteps, 2)
print("y_train:", y_train.shape)  # (samples, 2)


# In[4]:


from keras.models import Sequential
from keras.layers import SimpleRNN, Dropout, Dense
from keras.optimizers import Adam

regressor = Sequential([
    SimpleRNN(32, activation='tanh', return_sequences=True, input_shape=(timesteps, 2)),
    Dropout(0.005),
    SimpleRNN(32, activation='tanh', return_sequences=True),
    Dropout(0.005),
    SimpleRNN(32, activation='tanh', return_sequences=True),
    Dropout(0.005),
    SimpleRNN(32, activation='tanh'),
    Dropout(0.005),
    Dense(2)   # two outputs: fossil_pct, renew_pct
])

regressor.compile(optimizer=Adam(0.001), loss='mse')
regressor.fit(X_train, y_train, epochs=200, batch_size=128)


# In[5]:


future_years = 13                     # how many years of forecasting
timesteps    = 5                     # same as training
current_seq  = energy_scaled[-timesteps:].copy()   # last 5 timesteps historical
future_scaled = []

for _ in range(future_years):
    # model expects shape (1, timesteps, 2)
    next_scaled = regressor.predict(current_seq[np.newaxis, ...], verbose=0)[0]
    future_scaled.append(next_scaled)

    # slide the window forward
    current_seq = np.vstack([current_seq[1:], next_scaled])

# Convert back to percentages
future_pct = scaler.inverse_transform(np.array(future_scaled))


# In[6]:


last_year = int(years[-1])
future_year_axis = np.arange(last_year + 1, last_year + 1 + future_years)


# In[7]:


pred_scaled = []
valid_years = []

for i in range(timesteps, len(energy_scaled)):
    window = energy_scaled[i - timesteps:i][np.newaxis, ...]
    pred = regressor.predict(window, verbose=0)[0]
    pred_scaled.append(pred)
    valid_years.append(years[i])

pred_scaled = np.array(pred_scaled)
pred_pct = scaler.inverse_transform(pred_scaled)


# In[8]:


plt.figure(figsize=(10,6))
plt.plot(years, pct_data["fossil_pct"],'k', label="Fossil actual (%)")
plt.plot(years, pct_data["renew_pct"], 'g', label="Renewables actual (%)")
plt.plot(valid_years, pred_pct[:,0], 'r--', label="Fossil predicted (%)")
plt.plot(valid_years, pred_pct[:,1], 'b--', label="Renewables predicted (%)")
plt.plot(future_year_axis, future_pct[:,0], 'r', label="Fossil forecast (%)")
plt.plot(future_year_axis, future_pct[:,1], 'b', label="Renewables forecast (%)")

plt.xlabel("Year")
plt.ylabel("Share of Total Energy (%)")
plt.legend()
plt.grid()
plt.savefig('forecast_rnn.png', bbox_inches='tight')
plt.show()


# In[9]:


from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense
from keras.optimizers import Adam

timesteps = 5

model = Sequential([
    LSTM(64, activation='tanh', return_sequences=True, input_shape=(timesteps, 2)),
    Dropout(0.1),
    LSTM(64, activation='tanh'),
    Dropout(0.1),
    Dense(2)  # Also 2 outputs: fossil_pct and renew_pct
])

model.compile(optimizer=Adam(0.001), loss='mse')
model.fit(X_train, y_train, epochs=200, batch_size=256, validation_split=0.1)


# In[10]:


future_steps = 13        # Years of forecasting
current_seq = energy_scaled[-timesteps:].copy()   # last 5 timesteps
future_scaled = []

for _ in range(future_steps):
    # shape = (1, timesteps, 2)
    next_pred = model.predict(current_seq[np.newaxis, ...], verbose=0)[0]
    future_scaled.append(next_pred)

    # slide window forward: drop oldest, append newest prediction
    current_seq = np.vstack([current_seq[1:], next_pred])

future_scaled = np.array(future_scaled)                  # (future_steps, 2)
future_pct    = scaler.inverse_transform(future_scaled)   # back to % scale


# In[11]:


last_year = int(years[-1])
future_years = np.arange(last_year + 1, last_year + 1 + future_steps)


# In[12]:


in_sample_preds = []
valid_years = []

for i in range(timesteps, len(energy_scaled)):
    seq = energy_scaled[i - timesteps:i][np.newaxis, ...]
    pred = model.predict(seq, verbose=0)[0]
    in_sample_preds.append(pred)
    valid_years.append(years[i])

in_sample_preds = scaler.inverse_transform(np.array(in_sample_preds))


# In[13]:


plt.figure(figsize=(10,6))

# Historical actuals
plt.plot(years, pct_data["fossil_pct"], 'k', label="Fossil actual (%)")
plt.plot(years, pct_data["renew_pct"], 'g', label="Renewables actual (%)")

# In-sample model fit
plt.plot(valid_years, in_sample_preds[:,0], 'r--', alpha=0.6, label="Fossil fit")
plt.plot(valid_years, in_sample_preds[:,1], 'b--', alpha=0.6, label="Renew fit")

# Future forecast
plt.plot(future_years, future_pct[:,0], 'r', label="Fossil forecast")
plt.plot(future_years, future_pct[:,1], 'b', label="Renew forecast")

plt.xlabel("Year")
plt.ylabel("Share of Total Energy (%)")
plt.title("Global Energy Mix: LSTM Forecast")
plt.legend()
plt.grid()
plt.savefig('forecast_lstm.png', bbox_inches='tight')
plt.show()


# In[ ]:




