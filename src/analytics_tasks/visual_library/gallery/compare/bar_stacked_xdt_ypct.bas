Sub bar_stacked_xdt_ypct()
    Dim ws As Worksheet
    Dim chartObj As ChartObject
    Dim chart As chart
    Dim lastRow As Long
    Dim i As Long, j As Long
    Dim uniqueMonths As Object
    Dim uniqueCategories As Object
    Dim monthCategories As Object
    Dim outputCol As Long
    Dim outputRow As Long
    Dim colorMap As Object
    Dim totalValue As Double
    
    ' Chart styling variables
    Dim chartFontFamily As String
    Dim chartElementsColor As Long
    Dim gridlineColor As Long
    Dim chart_title_font_size As String
    Dim xtitle_font_size As Integer
    Dim xtick_label_font_size As Integer
    Dim ytitle_font_size As Integer
    Dim ytick_label_font_size As Integer
    Dim series_label_font_size As Integer
    Dim legend_font_size As Integer
    Dim y_axis_unit As Integer
    
    ' Title variables
    Dim chartTitle As String
    Dim xAxisTitle As String
    Dim yAxisTitle As String
    
    ' Percentage data location variables
    Dim percentCol As Long
    Dim percentRow As Long
    
    ' Sorting array
    Dim sort_array As Variant
    
    ' Set the font family, size, and colors
    chartFontFamily = "Calibri"
    chartElementsColor = RGB(0, 22, 94)
    gridlineColor = RGB(242, 242, 242)
    chart_title_font_size = 14
    xtitle_font_size = 9
    xtick_label_font_size = 10
    ytitle_font_size = 9
    ytick_label_font_size = 10
    series_label_font_size = 8
    legend_font_size = 9
    y_axis_unit = 100 ' Adjusted for percentage scale
    
    ' Set chart and axis titles
    chartTitle = ""
    xAxisTitle = "Date"
    yAxisTitle = "Percentage (%)"
    
    ' Define the sorting array (can be "" for default sorting)
    sort_array = Array(" ") ' Comment this out or set to "" for default sorting
    
    ' Set active sheet
    Set ws = ActiveSheet
    
    ' Find last row of data
    lastRow = ws.Cells(Rows.Count, 1).End(xlUp).row
    
    ' Create dictionaries for unique months, categories, and color mapping
    Set uniqueMonths = CreateObject("Scripting.Dictionary")
    Set uniqueCategories = CreateObject("Scripting.Dictionary")
    Set colorMap = CreateObject("Scripting.Dictionary")
    Set monthCategories = CreateObject("Scripting.Dictionary")
    
    ' Collect unique months and categories, and store color mappings
    For i = 2 To lastRow
        Dim monthKey As Variant
        Dim categoryKey As Variant
        monthKey = Format(CDate(ws.Cells(i, 1).value), "mmm-yy")
        categoryKey = ws.Cells(i, 2).value ' Category in Column B
        
        If Not uniqueMonths.Exists(monthKey) Then uniqueMonths.Add monthKey, 0
        If Not uniqueCategories.Exists(categoryKey) Then uniqueCategories.Add categoryKey, 0
        
        Dim rgbText As String
        Dim rgbValues As Variant
        Dim rgbColor As Long
        rgbText = ws.Cells(i, 5).value
        rgbText = Replace(rgbText, "(", "")
        rgbText = Replace(rgbText, ")", "")
        rgbValues = Split(rgbText, ", ")
        
        If UBound(rgbValues) >= 2 Then
            rgbColor = RGB(CInt(rgbValues(0)), CInt(rgbValues(1)), CInt(rgbValues(2)))
            If Not colorMap.Exists(categoryKey) Then colorMap.Add categoryKey, rgbColor
        Else
            If Not colorMap.Exists(categoryKey) Then colorMap.Add categoryKey, RGB(0, 0, 0)
        End If
        
        Dim monthCategoryKey As String
        monthCategoryKey = monthKey & "|" & categoryKey
        If Not monthCategories.Exists(monthCategoryKey) Then
            monthCategories.Add monthCategoryKey, ws.Cells(i, 3).value
        Else
            monthCategories(monthCategoryKey) = monthCategories(monthCategoryKey) + ws.Cells(i, 3).value
        End If
    Next i
    
    ' Transpose data to wide format starting from column O (15)
    outputCol = 15 ' Start at column O
    outputRow = 1  ' Header row for categories
    
    ' Write month headers (dates) starting from column P (outputCol + 1)
    ws.Cells(outputRow, outputCol).value = "Date"
    j = 0
    For Each monthKey In uniqueMonths.Keys
        j = j + 1
        Dim properDate As Date
        properDate = DateSerial(20 & Right(monthKey, 2), month(DateValue("01-" & Left(monthKey, 3) & "-2022")), 1)
        ws.Cells(outputRow, outputCol + j).value = properDate
        ws.Cells(outputRow, outputCol + j).NumberFormat = "mmm-yy"
    Next monthKey
        
    ' Sort categories based on sort_array or ascending order
    Dim sortedCategories As Variant
    If IsMissingOrEmpty(sort_array) Or (IsArray(sort_array) And ArrayLength(sort_array) = 0) Then
        ' Default sorting: ascending order of category names
        sortedCategories = uniqueCategories.Keys
        Dim temp As Variant, k As Long, l As Long
        For k = LBound(sortedCategories) To UBound(sortedCategories) - 1
            For l = k + 1 To UBound(sortedCategories)
                If sortedCategories(k) > sortedCategories(l) Then
                    temp = sortedCategories(k)
                    sortedCategories(k) = sortedCategories(l)
                    sortedCategories(l) = temp
                End If
            Next l
        Next k
    Else
        ' Custom sorting based on sort_array
        sortedCategories = sort_array
        ' Ensure all categories are included
        For Each categoryKey In uniqueCategories.Keys
            If Not IsInArray(categoryKey, sortedCategories) Then
                ReDim Preserve sortedCategories(UBound(sortedCategories) + 1)
                sortedCategories(UBound(sortedCategories)) = categoryKey
            End If
        Next categoryKey
    End If
    
    ' Write category headers and values based on sorted order
    outputRow = 2
    For Each categoryKey In sortedCategories
        If uniqueCategories.Exists(categoryKey) Then ' Ensure category exists in data
            ws.Cells(outputRow, outputCol).value = categoryKey
            j = 0
            For Each monthKey In uniqueMonths.Keys
                j = j + 1
                Dim fullKey As String
                fullKey = monthKey & "|" & categoryKey
                If monthCategories.Exists(fullKey) Then
                    ws.Cells(outputRow, outputCol + j).value = monthCategories(fullKey)
                Else
                    ws.Cells(outputRow, outputCol + j).value = 0
                End If
            Next monthKey
            outputRow = outputRow + 1
        End If
    Next categoryKey
    
    ' Add a row for totals below the categories
    ws.Cells(outputRow, outputCol).value = "Total"
    For j = 1 To uniqueMonths.Count
        totalValue = 0
        For i = 2 To outputRow - 1
            totalValue = totalValue + ws.Cells(i, outputCol + j).value
        Next i
        ws.Cells(outputRow, outputCol + j).value = totalValue
    Next j
    
    ' Define percentage table location (5 rows below transposed data, same column O)
    percentCol = outputCol ' Same starting column (O)
    percentRow = outputRow + 5 ' 5 rows below the total row
    
    ' Write headers for percentage table
    ws.Cells(percentRow, percentCol).value = "Date"
    ws.Range(ws.Cells(percentRow, percentCol + 1), ws.Cells(percentRow, percentCol + uniqueMonths.Count)).value = _
        ws.Range(ws.Cells(1, outputCol + 1), ws.Cells(1, outputCol + uniqueMonths.Count)).value
    
    ' Copy category names
    ws.Range(ws.Cells(percentRow + 1, percentCol), ws.Cells(percentRow + uniqueCategories.Count, percentCol)).value = _
        ws.Range(ws.Cells(2, outputCol), ws.Cells(outputRow - 1, outputCol)).value
    
    ' Write percentage formulas
    For i = percentRow + 1 To percentRow + uniqueCategories.Count
        For j = 1 To uniqueMonths.Count
            Dim valueCell As String
            Dim totalCell As String
            valueCell = ws.Cells(i - percentRow + 1, outputCol + j).Address(False, False) ' e.g., "P2"
            totalCell = ws.Cells(outputRow, outputCol + j).Address(False, False) ' e.g., "P5"
            ws.Cells(i, percentCol + j).Formula = "=IF(" & totalCell & "=0,0," & valueCell & "/" & totalCell & ")"
            ws.Cells(i, percentCol + j).NumberFormat = "0.0%" ' Format as percentage with 1 decimal
        Next j
    Next i
    
    ' Remove any existing charts
    For Each chartObj In ws.ChartObjects
        chartObj.Delete
    Next chartObj
    
    ' Create chart object
    Set chartObj = ws.ChartObjects.Add(Left:=200, Width:=700, Top:=50, Height:=400)
    Set chart = chartObj.chart
    
    chart.ChartType = xlColumnStacked
    chart.ChartArea.Font.Name = chartFontFamily
    chart.ChartArea.Font.Color = chartElementsColor
    chart.ChartArea.Border.LineStyle = msoLineNone
    
    If chartTitle <> "" Then
        chart.HasTitle = True
        chart.chartTitle.Text = chartTitle
        chart.chartTitle.Font.Size = chart_title_font_size
        chart.chartTitle.Font.Name = chartFontFamily
        chart.chartTitle.Font.Color = chartElementsColor
    Else
        chart.HasTitle = False
    End If
    
    ' Set data range to percentage values
    Dim percentageDataRange As Range
    Set percentageDataRange = ws.Range(ws.Cells(percentRow + 1, percentCol), ws.Cells(percentRow + uniqueCategories.Count, percentCol + uniqueMonths.Count))
    chart.SetSourceData Source:=percentageDataRange
    
    With chart.Axes(xlCategory)
        .HasTitle = True
        .AxisTitle.Text = xAxisTitle
        .AxisTitle.Font.Size = xtitle_font_size
        .TickLabels.Font.Size = xtick_label_font_size
        .TickLabels.Font.Name = chartFontFamily
        .TickLabelPosition = xlTickLabelPositionLow
        .MajorTickMark = xlTickMarkNone
        .TickLabels.NumberFormat = "mmm-yy"
        Dim categoryLabels As Range
        Set categoryLabels = ws.Range(ws.Cells(percentRow, percentCol + 1), ws.Cells(percentRow, percentCol + uniqueMonths.Count))
        chart.SeriesCollection(1).XValues = categoryLabels
    End With
    
    With chart.Axes(xlValue)
        .HasTitle = False
        '.AxisTitle.Text = yAxisTitle
        '.AxisTitle.Font.Size = ytitle_font_size
        '.TickLabels.Font.Size = ytick_label_font_size
        '.TickLabels.Font.Name = chartFontFamily
        .TickLabels.Font.Size = ytick_label_font_size
        .TickLabels.Font.Name = chartFontFamily
        .MinimumScale = 0
        .MaximumScale = 1
        .MajorUnit = 0.2 ' 20% intervals
        .HasMajorGridlines = False
        .MajorGridlines.Format.line.ForeColor.RGB = gridlineColor
        .MajorTickMark = xlTickMarkNone
        .Border.LineStyle = xlNone
        .TickLabels.NumberFormat = "0%"
        .TickLabelPosition = xlNone ' Hides the labels
        .Border.LineStyle = xlNone ' Hides the axis line
    End With
    
    ' Apply colors and data labels to series
    Dim seriesIndex As Long
    For seriesIndex = 1 To chart.SeriesCollection.Count
        Dim seriesName As String
        seriesName = chart.SeriesCollection(seriesIndex).Name
        With chart.SeriesCollection(seriesIndex)
            If colorMap.Exists(seriesName) Then
                .Format.Fill.ForeColor.RGB = colorMap(seriesName)
            Else
                .Format.Fill.ForeColor.RGB = RGB(0, 0, 0)
            End If
            
            ' Series data labels as percentages
            .HasDataLabels = True
            With .dataLabels
                .ShowValue = True
                .Position = xlLabelPositionCenter
                .Font.Name = chartFontFamily
                .Font.Size = series_label_font_size
                .Font.Color = RGB(255, 255, 255)
                .NumberFormat = "0.0%" ' Format as percentages
            End With
        End With
    Next seriesIndex
    
    On Error Resume Next
    For seriesIndex = 1 To chart.SeriesCollection.Count - 1
        Dim categoryName As String
        categoryName = ws.Cells(percentRow + 1 + seriesIndex - 1, percentCol).value
        If Len(Trim(categoryName)) > 0 Then
            chart.SeriesCollection(seriesIndex).Name = categoryName
        End If
    Next seriesIndex
    On Error GoTo 0
    
    ' Add total series with labels
    Dim totalSeries As series
    Set totalSeries = chart.SeriesCollection.NewSeries
    With totalSeries
        .Name = "Total"
        .Values = ws.Range(ws.Cells(outputRow, outputCol + 1), ws.Cells(outputRow, outputCol + uniqueMonths.Count))
        .ChartType = xlLine
        .Format.line.Visible = msoFalse
        .HasDataLabels = True
        With .dataLabels
            .ShowValue = True
            .Position = xlLabelPositionAbove
            .Font.Name = chartFontFamily
            .Font.Size = series_label_font_size
            .Font.Color = RGB(0, 0, 0)
            .NumberFormat = "#,##0" ' Format as whole numbers
        End With
    End With
    
    chart.legend.LegendEntries(chart.SeriesCollection.Count).Delete
    
    ' Format legend
    chart.HasLegend = True
    Set legend = chart.legend
    
    With legend
        .Position = xlLegendPositionTop
        .Left = 0
        FontSize = 10 ' Your font size
        .Font.Size = FontSize
        .Font.Name = chartFontFamily
        .Font.Color = chartElementsColor
    End With
    
    Set ws = Nothing
    Set chartObj = Nothing
    Set chart = Nothing
    Set uniqueMonths = Nothing
    Set uniqueCategories = Nothing
    Set colorMap = Nothing
    Set monthCategories = Nothing
End Sub

Private Function IsMissingOrEmpty(v As Variant) As Boolean
    Select Case VarType(v)
        Case vbEmpty
            IsMissingOrEmpty = True
        Case vbString
            IsMissingOrEmpty = (v = "")
        Case Else
            IsMissingOrEmpty = False
    End Select
End Function

Private Function ArrayLength(arr As Variant) As Long
    On Error Resume Next
    ArrayLength = UBound(arr) - LBound(arr) + 1
    If Err.Number <> 0 Then ArrayLength = 0
    On Error GoTo 0
End Function

Private Function IsInArray(val As Variant, arr As Variant) As Boolean
    Dim i As Long
    For i = LBound(arr) To UBound(arr)
        If arr(i) = val Then
            IsInArray = True
            Exit Function
        End If
    Next i
    IsInArray = False
End Function