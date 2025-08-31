from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, trim, lower, split, slice, collect_list, flatten


def numClicksPerUser(user_interaction: DataFrame) -> DataFrame:
    clicks = user_interaction.filter(
                                    lower(
                                        trim(
                                            col("interaction")
                                        )
                                    ) == "click"
    )
    clicks_map = clicks.rdd.map(
                                lambda t: (t[0], 1)
    )
    num_clicks_per_user = clicks_map.reduceByKey(
                                lambda x, y: x + y
    )
    return num_clicks_per_user.toDF()

def numPurchasesPerUser(user_interaction: DataFrame) -> DataFrame:
    purchases = user_interaction.filter(
                                        lower(
                                            trim(
                                                col("interaction")
                                            )
                                        ) == "purchase"
    )
    purchases_map = purchases.rdd.map(
                                    lambda t: (t[0], 1)
    )
    num_purchases_per_user = purchases_map.reduceByKey(
                                    lambda x, y: x + y
    )
    return num_purchases_per_user.toDF()

def numInteractionsPerProduct(user_interaction: DataFrame) -> DataFrame:
    products_map = user_interaction.rdd.map(
                                            lambda row: (row[1], 1)
    )
    num_interactions_per_product = products_map.reduceByKey(
                                            lambda x, y: x + y
    )
    return num_interactions_per_product.toDF()

def users_products_price(user_interaction: DataFrame, product_catalog: DataFrame) -> DataFrame:
    joined_df = user_interaction.join(product_catalog, on="product_id", how="left")
    return joined_df

def averageRatingPerUser(user_review: DataFrame) -> DataFrame:
    user_review_grouped = user_review.groupby("user_id").avg("rating")
    user_review_grouped = user_review_grouped.withColumnRenamed("avg(rating)", "average_rating")
    return user_review_grouped

def keyword_frequency(user_review: DataFrame) -> DataFrame:
    top_3_words = user_review.withColumn(
                                        "Top_3_words",
                                        slice(split(col("review"), " "), 1, 3)
    )
    top_3_words = top_3_words.groupby("user_id").agg(collect_list("top_3_words").alias("top_3_words"))
    top_3_words = top_3_words.withColumn("top_3_words", flatten(col("top_3_words")))
    top_3_words = top_3_words.withColumn("word1", col("top_3_words")[0]) \
                         .withColumn("word2", col("top_3_words")[1]) \
                         .withColumn("word3", col("top_3_words")[2])
    top_3_words = top_3_words.select("user_id", "word1", "word2", "word3")
    return top_3_words