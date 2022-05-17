Dim file, WB

With CreateObject("Excel.Application")
	On Error Resume Next
	For Each file in WScript.Arguments
		Set WB = .Workbooks.Open(file)
		WB.SaveAs Replace(WB.FullName, ".csv", ".xlsm"),52
		WB.Close False
	Next
	.Quit
End With