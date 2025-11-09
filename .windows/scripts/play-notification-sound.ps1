# Play random "notification" sound
$soundDir = Join-Path $env:USERPROFILE '.claude\sounds\notification'
$sounds = Get-ChildItem -Path "$soundDir\*" -Include *.wav,*.mp3 -File -ErrorAction SilentlyContinue

if ($sounds.Count -gt 0) {
    $randomSound = $sounds | Get-Random
    (New-Object Media.SoundPlayer $randomSound.FullName).PlaySync()
}
