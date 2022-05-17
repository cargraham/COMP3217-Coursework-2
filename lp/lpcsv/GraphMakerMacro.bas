Attribute VB_Name = "Module1"
Sub GraphMaker2()
Attribute GraphMaker2.VB_ProcData.VB_Invoke_Func = " \n14"
'
' GraphMaker2 Macro
'

'
    Columns("A:A").Select
    Application.CutCopyMode = False
    ActiveWorkbook.ActiveSheet.Sort.SortFields.Clear
    ActiveWorkbook.ActiveSheet.Sort.SortFields.Add2 Key:=Range("A1:A424" _
        ), SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:=xlSortNormal
    With ActiveWorkbook.ActiveSheet.Sort
        .SetRange Range("A2:A424")
        .Header = xlNo
        .MatchCase = False
        .Orientation = xlTopToBottom
        .SortMethod = xlPinYin
        .Apply
    End With
    Rows("1:17").Select
    Selection.Delete Shift:=xlUp
    Columns("A:A").Select
    Selection.TextToColumns Destination:=Range("A1"), DataType:=xlDelimited, _
        TextQualifier:=xlDoubleQuote, ConsecutiveDelimiter:=True, Tab:=True, _
        Semicolon:=False, Comma:=False, Space:=True, Other:=True, OtherChar:= _
        "_", FieldInfo:=Array(Array(1, 1), Array(2, 1), Array(3, 1)), _
        TrailingMinusNumbers:=True
    Range("E1").Select
    Application.CutCopyMode = False
    Application.CutCopyMode = False
    Application.CutCopyMode = False
    
    Dim sheetname As String
    sheetname = ActiveWorkbook.ActiveSheet.Name
    Selection.Consolidate Sources:= _
        sheetname & "!C2:C3" _
        , Function:=xlSum, TopRow:=True, LeftColumn:=True, CreateLinks:=False
    ActiveWorkbook.ActiveSheet.Sort.SortFields.Clear
    ActiveWorkbook.ActiveSheet.Sort.SortFields.Add2 Key:=Range("E1:E25") _
        , SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:=xlSortNormal
    With ActiveWorkbook.ActiveSheet.Sort
        .SetRange Range("E1:F25")
        .Header = xlNo
        .MatchCase = False
        .Orientation = xlTopToBottom
        .SortMethod = xlPinYin
        .Apply
    End With
    ActiveSheet.Shapes.AddChart2(201, xlColumnClustered).Select
    Dim sourceRange As String
    sourceRange = "'" & sheetname & "'!$E$1:$F$25"
    ActiveChart.SetSourceData source:=Range(sourceRange)
    Application.CutCopyMode = False
    Application.CutCopyMode = False
    ActiveChart.FullSeriesCollection(1).Delete
    ActiveChart.FullSeriesCollection(1).XValues = "='" & sheetname & "'!$E$1:$E$24"
    ActiveChart.Legend.Select
    Selection.Delete
End Sub
