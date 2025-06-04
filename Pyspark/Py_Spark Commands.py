
# data Reading 
df_json = spark.read.format('json').option('inferSchema',True).option('header',True).option('multiLine',False).load('c:/suyash/filename.json')
df_json.display()

# data reading by utils 
dbutils.fs.ls('file path of db')

df =  spark.read.format('csv').option('inferschema',True).option('header')

# print schema
df.printSchema()

#DDL schema 
my_ddl_schema = '''
                column_name_1 STRING ,
                column_name_2 STRING ,
                column_name_3 DOUBLE ,
                column_name_4 INT , 
                column_name_5 STRING ,
                column_name_6 FLOAT
                '''
# here insted of inferschema using the defiend shema 
# inferschema means system generated scheam 
df = spark.read.format('csv').schema(my_ddl_schema).option('header',True).load('Path')

# structType() Schema 

from pyspark.sql.types import *
from pyspark.sql.functions import *

my_struct_schema = StructType([StructField('Column_name_1',StringType(),True),
                    StructField('Column_name_2',StringType(),True),
                    StructField('Column_name_3',StringType(),True),
                    StructField('Column_name_4',StringType(),True),
                    StructField('Column_name_5',StringType(),True)
                    ])

df.spark.read.format('csv').schema(my_struct_schema).option('header',True).load('FilePath')

df.printSchema()

# Transformation 
# Select 
df.select(col('Column_name_1'),col('Column_name_2'),col('Column_name_2')).display()

# ALIAS
df.select(col('Column_name_1').alias('Item_id')).display()

#Filter
# Example 1
df.filter(col('Column_name_2') == 'Regular').display()

#Example 2
df.filter(col('Column_name_3') == 'Soft Drinks') & (col('Item_Weight') < 10).display()

#Example 3
df,filter(col('Outlet_Size').isNull()) & (col('Outlet_Location_Type').isin('Tier 1' , 'Tier 2')).display()


# withColumnRenamed
df.withColumnRenamed('Item_weight','Item_Wt').display()

# withColumn
# example 1
df = df.withColumn('Flag',lit('new'))

# Example 2
df.withColumn('Multiply', col('Item_Weight')*col(Item_MRP)).display()

df = df.withColumn('Item_Fat_content', regexp_replace(col('Item_Fat_Content'),"Regular","Reg")).withColumn('Item_Fat_content',regexp_replace(col('Item_Fat_Content'),'Low Fat','Lf'))

# Type Casting
df = df.withColumn('Item_Weight', col('Item_Weight').cast(StringType()))
df.printSchema()

# sort 
df.sort(col('Item_Weight').desc()).display()

df.sort(col('Item_visibility').asc()).display()

df.sort(col['Item_Weight','Item_Visibility'],ascending = [0,0]).display()

df.sort(col['Item_Weight','Item_Visibility'],ascending = [0,1]).display()

# limit
df.limit(10).display()

#Drop
df.Drop('Item_Visibility').display()

df.drop('Item_Visibility','Item_Type').display()

# drop_Duplicates
df.drop_Duplicates().display()

df.drop_Duplicates(subset=['Item_Type']).display()

df.distinct().display()

# Union and Union By name 

data1 = [('1','kad'),
        ('2','sid')]
schame1 = 'id STRING , name STRING'
df1 = spark.createDataFrame(data1,schema1)

data2 = [('3','rahul'),
        ('4','jas')]
schema2 = 'id STRING , name STRING'
df2 = spark.createDataFrame(data2,schema2)
df1.display()
df2.display()

# union 
df1.union(df2).display()
#unionByName
df1.unionByName(df2).display()

#String Function
#Initcap()

df.select(upper('ItemType').alias('upper_Item_Type')).display()

# Date Function
#Current Date 
# showing the current date 
df.withColumn('curr_date',current_date())
df.display()

#Date_Add function 
# with the help we are adding the date 
df = df.withColumn('Week_after',date_add('curr_date',7))
df.display()

#date_sub function 
# with the help of that substract the date from current date or relevant column date column
df = df.withColumn('Week_before',date_sub('curr_date',7))
df.display()

# same thing we can do with the help of date_add function 
df = df.withColumn('Week_before',date_sub('curr_date',-7))
df.display()

#dateDiff() function 
# with the help of that we can find out the difference of two date column
df = df.withColumn('datediff',datediff('week_before','curr_date'))
df.display()

# date_format() function 
df = df.withColumn('week_before', date_format('week_before','dd-mm-yyyy'))
df.display()


# HAndling Nulls
# Dropping Nulls
# this is a dropping the column jaha all the column of table table have null
df = df.dropna('all').display()

# this will droping the any column whos having the null 
df = df.dropna('any').display()

# with the help of that we remove the null from specific column
df = df.dropna(subset=['Outlet_size']).display()

df.display()

# fillings Nulls

df = df.fillna('NotAvailable').display()
df = df.fillna('NotAvailable',subset=['Outlet_Size']).display()

# split 
# here spilitting the value of the column (means in column we have 2 values trhat time )
df = df.withColumn('Outlet_Type',split('Outlet_Type','')).display()

# split and indexing
# here spliting the value of the column with index(means in ine colun we have list in this we have a value)
# so getting and spliting this using the this 
df = df.withColumn('Outlet_Type',split('Outlet_Type','')[1]).display()

# Explode Function
# with the help of this function we can explore the value 
# suppose we have 2 column first column we have 1 value and secondwe have list inside have 2 value then 
# then first value make the record 1 and also second so it will create a 2 record 

df_exp = df.withColumn('Outlet_Type',split('Outlet_type',''))
df_exp.display()

df_exp = df_exp.withColumn('Outlet_Type',explode('Outlet_Type'))
df_exp.display()

# Array_contains
# wuith the help of this we will return a yes and no value like a boolean 
# this will be applying the column which is having the list ind=suide column means struct column 

df_exp = df.exp.withColumn('Type1_flag',Array_contains('Outlet_Type','Type1')).display()

# Group_by Function 
# agg means aggrigation function 

df = df.groupBy('Item_Type').agg(sum('Item_MRP')).display()

df = df.groupBy('Item_Type').agg(AVG('Item_MRP')).display()

df = df.groupBy('Item_Type','Outlet_Size').agg(SUM('Item_MRP').alias('Total_MRP')).display()

df = df.groupBy('Item_Type','Outlet_Size').agg(SUM('Item_MRP'),AVG('Item_MRP')).display()

# collect_list Function 
# it is similar of SQL function of group_concat 

data = [('user1','book1'),
        ('user1','book2'),
        ('user2','book2'),
        ('user2','book4'),
        ('user3','book1')]

schema = 'user string, book string'

df_book = spark.createDataFrame(data,schema)
df_book.display()

# with the help of this we are combining the values and stores in one column as a list
df_book = df_book.groupBy('user').agg(collect_list('book')).display()

# PIVOT function 
# 
df.select('Item_Type','Outlet_Size','Item_MRP').display()

df = df.groupBy('Item_Type').pivot('Outlet_Size').agg(AVG('Item_MRP')).display()

# when-otherwise function 
# it is similar to the case when statemenet in SQL 

df = df.withColumn('veg_flag',when(col('Item_Type') == 'Meat','Non-Veg').otherwise('Veg'))
df.display()

df = df.withColumn('veg_exp_flag',when(((col('veg_flag')=='Veg') & (col('Item_MRP')<100)),'Veg_Inexpensive')\
                                .when((col('veg_flag')=='veg') & (col('Item_MRP')>100),'Veg Expensive')\
                                    .otherwise('Non_Veg')).display()


# Joins 
dataj1 = [('1','gaur','d01'),
          ('2','kit','d02'),
          ('3','sam','d03'),
          ('4','tim','d03'),
          ('5','aman','d05'),
          ('6','nad','d06')] 

schemaj1 = 'emp_id STRING, emp_name STRING, dept_id STRING' 
df1 = spark.createDataFrame(dataj1,schemaj1)

dataj2 = [('d01','HR'),
          ('d02','Marketing'),
          ('d03','Accounts'),
          ('d04','IT'),
          ('d05','Finance')]

schemaj2 = 'dept_id STRING, department STRING'

df2 = spark.createDataFrame(dataj2,schemaj2)

df1.display()
df2.display()

#Inner Join
df1.join(df2, df1['dept_id']==df2['dept_id'],'inner').display()

# Left Join 
df1.join(df2,df1['dept_id'] == df2['dept_id'],'left').display()

# Right Join
df1.join(df2,df1['dept_id'] == df2['dept_id'],'right').display()

#Anti Join 
df1.join(df2,df1['dept_id'] == df2['dept_id'],'anti').display()


# window Function

# Row_Number()

df.display()

from pyspark.sql.window import window 
df = df.withColumn('rowCol',row_number().over(window.orderBy('Item_Identifier'))).display()

#rank and dense_rank
df = df.withColumn('rank',rank().over(window.orderBy(col('Item_Identifier').desc())))\
    .withColumn('denserank',dense_rank().over(window.orderBy(col('Item_Identifier').desc()))).display()

# cumulative sum (sum of any column till partular length)

df = df.withColumn('cumsum',sum('Item_MRP').over(window.orderBy('Item_Type'))).display()

# unboundedPreceding means taking all previous row 
df = df.withColumn('cumsum',sum('Item_MRP').over(window.orderBy('Item_Type').rowsBetween(window.unboundedPreceding,window.currentRow))).display()

# unboundedFollowing means taking all the value of this particular column
df = df.withColumn('TotalSum',sum('Item_MRP').over(window.orderBy('Item_Type').rowsBetween(window.unboundedPreceding , window.unboundedFollowing))).display()


# USER DEFINED FUNCTIONS (UDF)

def my_func(x):
    return x*x 

my_udf = udf(my_func)

df.withColumn('mynewcol',my_udf('Item_MRP')).display()

# data Writting

# CSV File 
df.write.format('CSV').save('path')

# append
df.write.format('CSV').mode('append').save('path')
df.write.format('CSV').mode('append').option('path','path/path').save()

#Overwrite
df.write.format('csv').mode('overwrite').option('path','path/path').save()

#Error
df.write.format('CSV').mode('error').option('path','path/path').save()

#Ignore
df.write.format('CSV').mode('ignore').option('path','path/path').save()

#PARQUET
df.write.format('parquet').mode('overwrite').option('path','path/path').save()


# TABLE
df.write.format('parquet').mode('overwrite').saveAsTable('my_table')

# Window Functions 

from pyspark.sql import window 
import pyspark 
from pyspark.sql import sparkSession
spark = sparkSession.builder.appName("pyspark_window").getOrCreate()

sampleData = (('bob',42),('lisa',59))
column_name = ['firstName','age']

df = spark.createDataFrame(data = sampleData,schema = column_name)
windowpartations = window.partitionBy('department').orderBy('Age')
df.printSchema()
df.show()
display(df)


#cumeDist()  This window function is used to get the cmulative distribution within a partation 

from pyspark.sql.functions import cume_dist
df.withColumn('cume_dist',cume_dist().over(windowpartations)).display()

# using lag() this window function is used to access previous row data as par the defied offsert value 

from pyspark.sql.functions import lag 
df.withColumn("Lag",lag("salary",2).over(windowpartations)).display()

# lead() this window function is used to access next rows data as par the defined offset value In the funcytion 

from pyspark.sql.functions import lead 

df.withColumn('Lead',lead('salary',2).over(windowpartations)).display()

#---------------------------------------------------------------------------------------------------------------------------------------
# Ranking Functions

# syntax for window function 

dataFrame.withColumn('Col_name',window_functions().over(window_partiton))

from pyspark.sql.window import window
import pyspark 
from pyspark.sql import SparkSession

spark = sparkSession.builder.appName("Pyspark_Window").gerOrCreate()

sampleData = (('bob',42),('lisa',59))
column = ['firstName','age']

df2 = spark.createDataFrame(data = sampleData , schema = column)
window_partation = window.partitionBy('Subject').orderBy('Marks')
df2.printSchema()
df2.diaplay()

# row_number() 

from pyspark.sql.functions import row_number
df2.withColumn('roe_number',row_number().over(windowpartations)).display()

# Rank()

from pyspark.sql.functions import rank

df2.withColumn('Rank',rank().over(windowpartations)).display()

# percent_rank() this function is similar to rank() , it is also provide a rank but in percentage manner 

from pyspark.sql.functions import percent_rank 
df2.withColumn('percent_rank',percent_rank().over(windowpartations)).display()

# dense rank()

from pyspark.sql.sql.functions import dense_rank
df2.withColumn('dense_rank',dense_rank().over(windowpartation)).display()

#---------------------------------------------------------------------------------------------------------------------------------------

#Aggereate Function 

sampleData = (('bob',42),('lisa',59),('maria',20),('camilo',31))
column = ['firstName','age']

df3 = spark.createDataFrame(data = sampleData , schema = column)
df3.printSchema()
df3.display()

from pyspark.sql.window import window 
from pyspark.sql.functions import col,avg,sum,min,max,row_number 
windowPartationAgg = window.partitionBy('firstName')

df3.withColumn('Avg',avg(col('age')).over(windowPartationAgg)).show()

df3.withColumn('sum',sum(col('age')).over(windowPartationAgg)).show()

df3.withColumn('min',min(col('age')).over(windowPartationAgg)).show()

df3.withColumn('max',max(col('age')).over(windowPartationAgg)).show()

#---------------------------------------------------------------------------------------------------------------------------------------

# Pyspark Joins

Inner
outer
left/leftouter
right/rightouter
leftsemi
leftanti

#---------------------------------------------------------------------------------------------------------------------------------------

df1 = spark.createDataFrame(data1,column)
df2 = spark.createDataFrame(data2,column)

# creating a view for dataframe 
df1.createOrReplaceTempView('student')
df2.createOrReplaceTempView('department')

spark.sql('select 8 from student , department where student.id == depart.id').display()

#---------------------------------------------------------------------------------------------------------------------------------------

# filtering the row based on column values 
df.where(dataframe.ID == '1').show()
df.filter(df1.id > '3').show()

#---------------------------------------------------------------------------------------------------------------------------------------
