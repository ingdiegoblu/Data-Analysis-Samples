/****** Script for SelectTopNRows command from SSMS  ******/
SELECT [ProductKey],
       [OrderDateKey],
      --,[DueDateKey]
      --,[ShipDateKey]
       [CustomerKey],
      --,[PromotionKey]
      --,[CurrencyKey]
      --,[SalesTerritoryKey]
      [SalesOrderNumber],
      --,[SalesOrderLineNumber]
      --,[RevisionNumber]
      [OrderQuantity],
      --,[UnitPrice]
      --,[ExtendedAmount]
      --,[UnitPriceDiscountPct]
      --,[DiscountAmount]
      [ProductStandardCost] AS [StandardCost],
      [TotalProductCost],
      [SalesAmount],
      --,[TaxAmt]
      --,[Freight]
      --,[CarrierTrackingNumber]
      --,[CustomerPONumber]
      [OrderDate],
      [DueDate],
      [ShipDate]
  FROM [AdventureWorksDW2019].[dbo].[FactInternetSales]
  WHERE [AdventureWorksDW2019].[dbo].[FactInternetSales].[OrderDate] >='2018'
  ORDER BY OrderDate ASC