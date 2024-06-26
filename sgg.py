import pandas as pd
from IPython.display import display
red_wine=pd.read_csv('red-wine.csv')
df_train=red_wine.sample(frac=0.7,random_state=0)
df_valid=red_wine.drop(df_train.index)
display(df_train.head(4))


#scale 0-1
max_=df_train.max(axis=0)
min_=df_train.min(axis=0)
df_train=(df_train-min_)/(max_-min_)
df_valid=(df_valid-min_)/(max_-min_)


#split f and t
X_train = df_train.drop('quality', axis=1)
#print(X_train)
X_valid = df_valid.drop('quality', axis=1)
#print(X_valid)
y_train = df_train['quality']
#print(y_train)
y_valid = df_valid['quality']
#print(y_valid)
print(X_train.shape)


from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Dense(512, activation='relu', input_shape=[11]),
    layers.Dense(512, activation='relu'),
    layers.Dense(512, activation='relu'),
    layers.Dense(1),
])


model.compile(
    optimizer='sgd',
    loss='mse',
)


history = model.fit(
    X_train, y_train,
    validation_data=(X_valid, y_valid),
    batch_size=256,
    epochs=100
)


history_df=pd.DataFrame(history.history)
history_df['loss'].plot()