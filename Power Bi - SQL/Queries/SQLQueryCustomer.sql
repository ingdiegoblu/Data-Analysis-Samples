/****** Script for SelectTopNRows command from SSMS  ******/
--Cleaning data for Customer Table--
SELECT [CustomerKey],
	  --[GeographyKey]
      --,[CustomerAlternateKey]
      --,[Title]
       [FirstName],
      --,[MiddleName]
       [LastName],
      --,[NameStyle]
      -- [BirthDate],
      --,[MaritalStatus]
      --,[Suffix]
       [Gender],
      --,[EmailAddress]
      --,[YearlyIncome]
      --,[TotalChildren]
      --,[NumberChildrenAtHome]
      --,[EnglishEducation]
      --,[SpanishEducation]
      --,[FrenchEducation]
      --,[EnglishOccupation]
      --,[SpanishOccupation]
      --,[FrenchOccupation]
      --,[HouseOwnerFlag]
      --,[NumberCarsOwned]
      --,[AddressLine1]
      --,[AddressLine2]
      --,[Phone]
      [DateFirstPurchase],
	  g.City AS [Customer City],
	  g.EnglishCountryRegionName AS [Customer Country]
      --,[CommuteDistance]
  FROM [AdventureWorksDW2019].[dbo].[DimCustomer]
		LEFT JOIN [AdventureWorksDW2019].[dbo].[DimGeography] AS g ON g.GeographyKey =[AdventureWorksDW2019].[dbo].[DimCustomer].[GeographyKey]
  ORDER BY
		CustomerKey ASC
