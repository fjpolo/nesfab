
Add-Type -AssemblyName System.Drawing

$sourcePath = "c:\Workspace\NES\nesfab\examples\LuciYFer\assets\bg1.png"
$destPath = "c:\Workspace\NES\nesfab\examples\LuciYFer\assets\bg1_fixed.png"
$backupPath = "c:\Workspace\NES\nesfab\examples\LuciYFer\assets\bg1.png.bak"

try {
    Write-Host "Loading image from $sourcePath..."
    $img = [System.Drawing.Image]::FromFile($sourcePath)
    Write-Host "Image loaded. Format: " $img.RawFormat.Guid
    Write-Host "Size:Width=" $img.Width " Height=" $img.Height
    
    # Check dimensions against backup if possible
    if (Test-Path $backupPath) {
        $imgBackup = [System.Drawing.Image]::FromFile($backupPath)
        Write-Host "Original Size:Width=" $imgBackup.Width " Height=" $imgBackup.Height
        
        if ($img.Width -ne $imgBackup.Width -or $img.Height -ne $imgBackup.Height) {
            Write-Host "Resize needed!"
            # Resize
            $newImg = new-object System.Drawing.Bitmap $imgBackup.Width, $imgBackup.Height
            $graph = [System.Drawing.Graphics]::FromImage($newImg)
            $graph.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::NearestNeighbor
            $graph.DrawImage($img, 0, 0, $imgBackup.Width, $imgBackup.Height)
            $img.Dispose()
            $img = $newImg
        }
        $imgBackup.Dispose()
    }

    Write-Host "Saving as PNG..."
    $img.Save($destPath, [System.Drawing.Imaging.ImageFormat]::Png)
    Write-Host "Done."
    $img.Dispose()
}
catch {
    Write-Error $_
}
