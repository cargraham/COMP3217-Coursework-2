Attribute VB_Name = "Module1"
Sub GraphMaker()
Attribute GraphMaker.VB_ProcData.VB_Invoke_Func = " \n14"
'
' GraphMaker Macro
'

'
    Columns("A:B").Select
    ActiveWorkbook.ActiveSheet.Sort.SortFields.Clear
    ActiveWorkbook.ActiveSheet.Sort.SortFields.Add2 Key:=Range( _
        "A1:A424"), SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:= _
        xlSortNormal
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
        TextQualifier:=xlDoubleQuote, ConsecutiveDelimiter:=False, Tab:=True, _
        Semicolon:=False, Comma:=False, Space:=False, Other:=True, OtherChar _
        :="_", FieldInfo:=Array(Array(1, 1), Array(2, 1)), TrailingMinusNumbers:=True
    Range("B1").Select
    ActiveCell.FormulaR1C1 = "1                            0"
    Range("F6").Select
    Cells.Find(What:="                            ", After:=ActiveCell, LookIn _
        :=xlFormulas2, LookAt:=xlPart, SearchOrder:=xlByRows, SearchDirection:= _
        xlNext, MatchCase:=False, SearchFormat:=False).Activate
    Cells.Replace What:="                            ", Replacement:=" ", _
        LookAt:=xlPart, SearchOrder:=xlByRows, MatchCase:=False, SearchFormat:= _
        False, ReplaceFormat:=False, FormulaVersion:=xlReplaceFormula2
    Range("B2").Select
    ActiveCell.FormulaR1C1 = "10                           0"
    Cells.Replace What:="                           ", Replacement:=" ", _
        LookAt:=xlPart, SearchOrder:=xlByRows, MatchCase:=False, SearchFormat:= _
        False, ReplaceFormat:=False, FormulaVersion:=xlReplaceFormula2
    Columns("B:B").Select
    Selection.TextToColumns Destination:=Range("B1"), DataType:=xlDelimited, _
        TextQualifier:=xlDoubleQuote, ConsecutiveDelimiter:=True, Tab:=True, _
        Semicolon:=False, Comma:=False, Space:=True, Other:=False, OtherChar _
        :="_", FieldInfo:=Array(Array(1, 1), Array(2, 1)), TrailingMinusNumbers:=True
    Range("E1").Select
    Application.CutCopyMode = False
    Selection.Consolidate Sources:= _
        "'https://sotonac-my.sharepoint.com/personal/cb6g19_soton_ac_uk/Documents/Year 3/Semester 2/COMP3217/Labs/Lab2/lp/lpcsv/[guideline-5.xlsm]guideline-5'!C2:C3" _
        , Function:=xlSum, TopRow:=True, LeftColumn:=True, CreateLinks:=False
    ActiveWorkbook.ActiveSheet.Sort.SortFields.Clear
    ActiveWorkbook.ActiveSheet.Sort.SortFields.Add2 Key:=Range( _
        "E1:E25"), SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:= _
        xlSortNormal
    With ActiveWorkbook.ActiveSheet.Sort
        .SetRange Range("E1:F25")
        .Header = xlNo
        .MatchCase = False
        .Orientation = xlTopToBottom
        .SortMethod = xlPinYin
        .Apply
    End With
    Range("E1:F24").Select
    ActiveSheet.Shapes.AddChart2(201, xlColumnClustered).Select
    ActiveChart.SetSourceData Source:=ActiveWorkbook.ActiveSheet.Range("$F$1:$F$24")
    Range("U25").Select
End Sub
