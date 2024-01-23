# Databricks notebook source
print("Hello World!")

# COMMAND ----------

# MAGIC %sql
# MAGIC Select "Hello world from SQL!"

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # title1
# MAGIC

# COMMAND ----------

# MAGIC %run ./Includes/setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets/')

# COMMAND ----------

display(files)

# COMMAND ----------


