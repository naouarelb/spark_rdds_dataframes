from pyspark.sql import SparkSession, DataFrame
from transformation.analysis import numClicksPerUser, \
                    numPurchasesPerUser, \
                    numInteractionsPerProduct, \
                    users_products_price, \
                    averageRatingPerUser, \
                    keyword_frequency


def log_summary(log_dir: str, user_interaction: DataFrame, product_catalog: DataFrame, user_review: DataFrame):
    numClicksPerUser(user_interaction).write.csv(f"{log_dir}/num_clicks_per_user", header=True, mode="overwrite")
    numPurchasesPerUser(user_interaction).write.csv(f"{log_dir}/num_purchases_per_user", header=True, mode="overwrite")
    numInteractionsPerProduct(user_interaction).write.csv(f"{log_dir}/num_interactions_per_product", header=True, mode="overwrite")
    users_products_price(user_interaction, product_catalog).write.csv(f"{log_dir}/users_products_price", header=True, mode="overwrite")
    averageRatingPerUser(user_review).write.csv(f"{log_dir}/average_rating_per_user", header=True, mode="overwrite")
    keyword_frequency(user_review).write.csv(f"{log_dir}/keyword_frequency_per_user", header=True, mode="overwrite")

