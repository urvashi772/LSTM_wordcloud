# ============================================
# PDF → LSTM → WordCloud
# Using TensorFlow (NO Transformer)
# ============================================

# ----------- Imports -----------
import numpy as np
import re
import matplotlib.pyplot as plt

from PyPDF2 import PdfReader
from wordcloud import WordCloud
from PIL import Image

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

from sklearn.model_selection import train_test_split

# ----------- 1. Read PDF -----------
pdf_path = "Narendra_Modi.pdf"   # <-- your PDF file

reader = PdfReader(pdf_path)
text = ""

for page in reader.pages:
    text += page.extract_text()

# ----------- 2. Clean text -----------
text = text.lower()
text = re.sub(r'[^a-z\s]', '', text)

# ----------- 3. Tokenization -----------
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])

total_words = len(tokenizer.word_index) + 1

# ----------- 4. Create sequences -----------
input_sequences = []
for line in text.split("\n"):
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        input_sequences.append(token_list[:i+1])

max_sequence_len = max(len(seq) for seq in input_sequences)

input_sequences = pad_sequences(
    input_sequences,
    maxlen=max_sequence_len,
    padding='pre'
)

X = input_sequences[:, :-1]
y = input_sequences[:, -1]

# One-hot encode labels
y = np.eye(total_words)[y]

# ----------- 5. Train-test split -----------
X_train, X_val, y_train, y_val = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# ----------- 6. Build LSTM model -----------
model = Sequential()
model.add(Embedding(
    input_dim=total_words,
    output_dim=64,
    input_length=max_sequence_len - 1
))
model.add(LSTM(100))
model.add(Dense(total_words, activation='softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# ----------- 7. Train model -----------
model.fit(
    X_train,
    y_train,
    epochs=50,
    validation_data=(X_val, y_val),
    verbose=1
)

# ----------- 8. Extract word importance -----------
embedding_weights = model.layers[0].get_weights()[0]

word_importance = {}
for word, idx in tokenizer.word_index.items():
    vector = embedding_weights[idx]
    word_importance[word] = np.linalg.norm(vector)

mask = np.array(Image.open("india_map.png"))
mask = np.where(mask > 0, 255, 0)

# ----------- 9. Generate WordCloud -----------
wordcloud = WordCloud(
    background_color="white",
    mask=mask,
    contour_width=2,
    contour_color="darkgreen",
    width=1000,
    height=1000
).generate(text)

plt.figure(figsize=(8,10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

wordcloud.to_file("India_Map_WordCloud.png")
print("✅ Word cloud created from full PDF!")