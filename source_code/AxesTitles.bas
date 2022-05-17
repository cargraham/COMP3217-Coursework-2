Attribute VB_Name = "Module1"
Sub AxesTitles()
Attribute AxesTitles.VB_ProcData.VB_Invoke_Func = " \n14"
'
' AxesTitles Macro
'

'
    ActiveSheet.ChartObjects("Chart 1").Activate
    ActiveChart.SetElement (msoElementPrimaryCategoryAxisTitleAdjacentToAxis)
    ActiveChart.Axes(xlCategory, xlPrimary).AxisTitle.Text = "Hour"
    Selection.Format.TextFrame2.TextRange.Characters.Text = "Hour"
    With Selection.Format.TextFrame2.TextRange.Characters(1, 4).ParagraphFormat
        .TextDirection = msoTextDirectionLeftToRight
        .Alignment = msoAlignCenter
    End With
    With Selection.Format.TextFrame2.TextRange.Characters(1, 4).Font
        .BaselineOffset = 0
        .Bold = msoFalse
        .NameComplexScript = "+mn-cs"
        .NameFarEast = "+mn-ea"
        .Fill.Visible = msoTrue
        .Fill.ForeColor.RGB = RGB(89, 89, 89)
        .Fill.Transparency = 0
        .Fill.Solid
        .Size = 10
        .Italic = msoFalse
        .Kerning = 12
        .Name = "+mn-lt"
        .UnderlineStyle = msoNoUnderline
        .Strike = msoNoStrike
    End With
    ActiveChart.Axes(xlCategory).Select
    ActiveChart.ChartArea.Select
    ActiveChart.SetElement (307)
    ActiveChart.Axes(xlValue, xlPrimary).AxisTitle.Text = "Total Energy Usage"
    Selection.Format.TextFrame2.TextRange.Characters.Text = "Total Energy Usage"
    With Selection.Format.TextFrame2.TextRange.Characters(1, 18).ParagraphFormat
        .TextDirection = msoTextDirectionLeftToRight
        .Alignment = msoAlignCenter
    End With
    With Selection.Format.TextFrame2.TextRange.Characters(1, 5).Font
        .BaselineOffset = 0
        .Bold = msoFalse
        .NameComplexScript = "+mn-cs"
        .NameFarEast = "+mn-ea"
        .Fill.Visible = msoTrue
        .Fill.ForeColor.RGB = RGB(89, 89, 89)
        .Fill.Transparency = 0
        .Fill.Solid
        .Size = 10
        .Italic = msoFalse
        .Kerning = 12
        .Name = "+mn-lt"
        .UnderlineStyle = msoNoUnderline
        .Strike = msoNoStrike
    End With
    With Selection.Format.TextFrame2.TextRange.Characters(6, 13).Font
        .BaselineOffset = 0
        .Bold = msoFalse
        .NameComplexScript = "+mn-cs"
        .NameFarEast = "+mn-ea"
        .Fill.Visible = msoTrue
        .Fill.ForeColor.RGB = RGB(89, 89, 89)
        .Fill.Transparency = 0
        .Fill.Solid
        .Size = 10
        .Italic = msoFalse
        .Kerning = 12
        .Name = "+mn-lt"
        .UnderlineStyle = msoNoUnderline
        .Strike = msoNoStrike
    End With
    ActiveChart.ChartArea.Select
End Sub
