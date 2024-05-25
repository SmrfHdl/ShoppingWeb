import pandas as pd
from pandas import isnull, notnull
from sklearn.metrics.pairwise import linear_kernel , cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def tfidf_matrix(df_new):
    """
        Dùng hàm "TfidfVectorizer" để chuẩn hóa "genres" với:
        + analyzer='word': chọn đơn vị trích xuất là word
        + ngram_range=(1, 1): mỗi lần trích xuất 1 word
        + min_df=0: tỉ lệ word không đọc được là 0
        Lúc này ma trận trả về với số dòng tương ứng với số lượng film và số cột tương ứng với số từ được tách ra từ "genres"
    """
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0.0)
    new_tfidf_matrix = tf.fit_transform(df_new['combined_features'])
    return new_tfidf_matrix

def cosine_sim(matrix):
    """
            Dùng hàm "linear_kernel" để tạo thành ma trận hình vuông với số hàng và số cột là số lượng film
             để tính toán điểm tương đồng giữa từng bộ phim với nhau
    """
    new_cosine_sim = linear_kernel(matrix, matrix)
    return new_cosine_sim

def preprocess_text(text):
    if not isinstance(text, str):
        text = str(text)
    # Chuyển thành chữ thường
    text = text.lower()
    
    # Loại bỏ dấu câu và các ký tự đặc biệt, chỉ giữ lại chữ cái và khoảng trắng
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Tokenization
    words = word_tokenize(text)
    
    # Loại bỏ các từ dừng
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    
    # Stemming
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    
    res ="".join(word + " " for word in words)
    
    return res

def dict_to_string(detail_dict):
    return "".join(c for c in detail_dict if c.isalpha() or c == " ")

def get_CB_data(text):
    data = pd.read_csv(text)
    df_new = data[['ID', 'Title','Detail','Description', 'Department']].copy()

    df_new['Detail'] = df_new['Detail'].apply(dict_to_string)
    df_new['Description'] = df_new['Description'].apply(preprocess_text)

    df_new['combined_features'] = df_new['Department'] + " " + df_new['Detail'] + " " + df_new['Description']

    return df_new

def get_CF_data(text):
   """
   đọc file base của movilens, lưu thành dataframe với 3 cột user id, item id, rating
   """
   ratings = pd.read_csv(text, sep ='\t',encoding='latin-1')
   data = ratings.values
   return data

def get_data(text):
    data = pd.read_csv(text)
    return data

