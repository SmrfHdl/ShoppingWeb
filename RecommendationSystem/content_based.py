import pandas as pd
import RecommendationSystem.CBCF_function

class CB(object):
    """
        Khởi tại dataframe "movies" với hàm "get_dataframe_movies_csv"
    """
    def __init__(self):
        self.products = RecommendationSystem.CBCF_function.get_CB_data('instance\database.db')
        self.tfidf_matrix = None
        self.cosine_sim = None

    def fit(self):
        """
           tính TF-IDF và ma trận tương đồng
        """
        self.tfidf_matrix = RecommendationSystem.CBCF_function.tfidf_matrix(self.products)
        self.cosine_sim = RecommendationSystem.CBCF_function.cosine_sim(self.tfidf_matrix)

    # Hàm này ở trong class CB
    def genre_recommendations(self, title, top_x):
            """
                Xây dựng hàm trả về danh sách top film tương đồng theo tên film truyền vào:
                + Tham số truyền vào gồm "title" là tên film và "topX" là top film tương đồng cần lấy
                + Tạo ra list "sim_score" là danh sách điểm tương đồng với film truyền vào
                + Sắp xếp điểm tương đồng từ cao đến thấp
                + Trả về top danh sách tương đồng cao nhất theo giá trị "topX" truyền vào
            """
            titles = self.products['name']
            indices = pd.Series(self.products.index, index=self.products['name'])
            idx = indices[title]
            sim_scores = list(enumerate(self.cosine_sim[idx]))
    
    # Sắp xếp sim_scores dựa trên giá trị đơn lẻ có thể so sánh được
            sim_scores = sorted(sim_scores, key=lambda x: x[0], reverse=True)
            sim_scores = sim_scores[1:top_x + 1]
            product_indices = [i[0] for i in sim_scores]
            return titles.iloc[product_indices].values

    def CB_get_Rcm_Product(self, text, top_x):
        """
            In ra top film tương đồng với film truyền vào
        """
        recommended_items= self.genre_recommendations(text, top_x)
        res = pd.DataFrame(recommended_items, columns = ['name'])

        products =RecommendationSystem.CBCF_function.get_data('instance\database.db')
        rcm_res = res.merge(products, on='name', how='inner')
        return rcm_res

#test
#name = "Under Armour Men's UA Tech™ Graphic Shorts"
#test = CB()
#test.fit()
#rcm_prodcut = test.CB_get_Rcm_Product(name,10)
#print(rcm_prodcut)

def get_recommendations(name,number_of_product):
    test = CB()
    test.fit()
    rcm_product = test.CB_get_Rcm_Product(name,number_of_product)
    rcm_product = rcm_product.values.tolist()
    return rcm_product

res = get_recommendations("Under Armour Men's UA Tech™ Graphic Shorts",4)
print(res)