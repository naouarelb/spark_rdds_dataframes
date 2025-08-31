from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, trim, lower, collect_list, split, slice, regexp_replace


def cleaning(user_interaction: str, product_catalog: str, user_review: str) -> tuple[DataFrame, DataFrame, DataFrame]:

    # 0. Trim string columns to remove spaces
    user_interaction = user_interaction.select(
                                                *[trim(
                                                    col(c)
                                                ).alias(c) \
                                                if c != 'timestamp' else col(c) for c in user_interaction.columns
                                                ]
    )
    product_catalog = product_catalog.select(
                                            *[trim(
                                                col(c)
                                                ).alias(c) \
                                                for c in product_catalog.columns
                                            ]
    )
    user_review = user_review.select(
                                    *[trim(
                                        col(c)
                                        ).alias(c) \
                                        for c in user_review.columns
                                    ]
    )

    # 1. fix data types
    user_review = user_review.select(
                                    col("rating").cast("int").alias("rating"),
                                    col("review").cast("string").alias("review"),
                                    col("user_id").cast("string").alias("user_id"),
                                    col("product_id").cast("string").alias("product_id")
    )

    user_review = user_review.withColumn(
                                        "review",
                                        regexp_replace(col("review"), ",", "")
    )

    product_catalog = product_catalog.select(
                                            col("product_id").cast("string").alias("product_id"),
                                            col("category").cast("string").alias("category"),
                                            col("price").cast("float").alias("price")
    )

    user_interaction = user_interaction.select(
                                                col("user_id").cast("string").alias("user_id"),
                                                col("product_id").cast("string").alias("product_id"),
                                                col("interaction").cast("string").alias("interaction"),
                                                col("timestamp").cast("string").alias("timestamp")
    )

    # 2. Normalization
    product_catalog = product_catalog.withColumn(
                                                "category",
                                                lower(
                                                    col("category")
                                                )
    )

    # 3. Filter out any interactions that are not relevant (keep purchase, click)
    user_interaction = user_interaction.filter(
                                                lower(
                                                    trim(
                                                        col("interaction")
                                                    )
                                                ).isin(["click", "purchase"])
    )
    # Map each interaction to a user_id, product_id pair
    user_interaction_map = user_interaction.groupby(
                                                col("user_id"), 
                                                col("product_id")
                                                ).agg(
                                                    collect_list(
                                                                col("interaction")
                                                                ).alias("interaction")
    )
    return user_interaction, product_catalog, user_review