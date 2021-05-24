/****** Script for SelectTopNRows command from SSMS  ******/
SELECT [ProductKey],
      [ProductAlternateKey] AS [ProductItemCode],
      --[ProductSubcategoryKey],
      --,[WeightUnitMeasureCode]
      --,[SizeUnitMeasureCode]
      [EnglishProductName] AS [Product Name],
	  pc.[EnglishProductCategoryName] AS [Product Category],
	  ps.[EnglishProductSubcategoryName] AS [Product Subcategory],
      --,[SpanishProductName]
      --,[FrenchProductName]
      [StandardCost],
      --,[FinishedGoodsFlag]
      [Color] AS [Product Color],
      --,[SafetyStockLevel]
      --,[ReorderPoint]
      --,[ListPrice]
      [Size] AS [Product Size],
      --,[SizeRange]
      --,[Weight]
      --,[DaysToManufacture]
      [ProductLine],
      --,[DealerPrice]
      --,[Class]
      --,[Style]
      [ModelName] AS [Product Model Name],
      --,[LargePhoto]
      [EnglishDescription] AS [Product Description],
      --,[FrenchDescription]
      --,[ChineseDescription]
      --,[ArabicDescription]
      --,[HebrewDescription]
      --,[ThaiDescription]
      --,[GermanDescription]
      --,[JapaneseDescription]
      --,[TurkishDescription]
      --,[StartDate]
      --,[EndDate]
      ISNULL([Status],'Outdated') AS [Product Status]
  FROM [AdventureWorksDW2019].[dbo].[DimProduct]
		LEFT JOIN [AdventureWorksDW2019].[dbo].[DimProductSubcategory] AS ps ON ps.[ProductSubcategoryKey]=[AdventureWorksDW2019].[dbo].[DimProduct].[ProductSubcategoryKey]
		LEFT JOIN [AdventureWorksDW2019].[dbo].[DimProductCategory] AS pc ON pc.[ProductCategoryKey]=ps.[ProductSubcategoryKey]
  ORDER BY
		[ProductKey] ASC