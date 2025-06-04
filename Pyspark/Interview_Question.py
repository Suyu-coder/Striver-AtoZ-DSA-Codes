
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql.functions import current_date, date_add

# Initialize Spark session
spark = SparkSession.builder.appName("EmployeeQueries").getOrCreate()

# Sample DataFrame creation (replace with your actual data source)
employee_df = spark.createDataFrame([
 # Add your employee data here
])

salaries_df = spark.createDataFrame([
 # Add your salaries data here
])

# 1. Second Highest Salary
second_highest_salary = employee_df.filter(
  employee_df.salary < employee_df.select(F.max("salary")).collect()[0][0]
).agg(F.max("salary").alias("secondHighestSalary"))
second_highest_salary.show()

# 2. Second Highest Salary using DENSE_RANK
window_spec = Window.orderBy(employee_df.salary.desc())
ranked_df = employee_df.withColumn("rnk", F.dense_rank().over(window_spec))
second_highest_salary_dense_rank = ranked_df.filter(ranked_df.rnk == 2).select("salary")
second_highest_salary_dense_rank.show()

# 3. Second Highest Salary using OFFSET and LIMIT
second_highest_salary_offset = employee_df.select("salary").distinct().orderBy("salary", ascending=False).limit(2).collect()[1]
print(second_highest_salary_offset)

# 4. Top 3 Earners from Each Department
window_spec_dept = Window.partitionBy("department").orderBy(employee_df.salary.desc())
ranked_dept_df = employee_df.withColumn("rnk", F.dense_rank().over(window_spec_dept))
top_earners = ranked_dept_df.filter(ranked_dept_df.rnk <= 3)
top_earners.show()

# 5. Count Duplicates in the Table
duplicates = employee_df.groupBy("column_name").agg(F.count("*").alias("count")).filter("count > 1")
duplicates.show()

# 6. Convert Row Level Data into Column Level Data
pivot_df = salaries_df.groupBy("department").pivot("month").sum("salary")
pivot_df.show()

# 7. Find Employees Earning More Than Their Manager
employee_manager_df = employee_df.alias("e").join(employee_df.alias("m"), F.col("e.manager_id") == F.col("m.employee_id"))
higher_earning_employees = employee_manager_df.filter(F.col("e.salary") > F.col("m.salary")).select("e.employee_id", "e.salary")
higher_earning_employees.show()

# 8. Cumulative Sum of Column
window_spec_cumulative = Window.partitionBy("department").orderBy("employee_id").rowsBetween(Window.unboundedPreceding, Window.currentRow)
cumulative_salary_df = employee_df.withColumn("cumulative_salary", F.sum("salary").over(window_spec_cumulative))
cumulative_salary_df.show()

# 9. Nth Highest Salary
N = 3 # Replace with the desired rank
window_spec_nth = Window.orderBy(employee_df.salary.desc())
ranked_nth_df = employee_df.withColumn("rnk", F.dense_rank().over(window_spec_nth))
nth_highest_salary = ranked_nth_df.filter(ranked_nth_df.rnk == N).select("salary")
nth_highest_salary.show()

# 10. Employees Who Joined in Last 6 Months
recent_joiners = employee_df.filter(employee_df.joining_date >= date_add(current_date(), -6 * 30))
recent_joiners.show()

# 11. Department-wise Highest Salary
highest_salary_by_department = employee_df.groupBy("department").agg(F.max("salary").alias("max_salary"))
highest_salary_by_department.show()

# 12. Remove Duplicate Rows
distinct_employee_df = employee_df.dropDuplicates(["name", "salary", "department"])
distinct_employee_df.show()

# Stop the Spark session
spark.stop()
