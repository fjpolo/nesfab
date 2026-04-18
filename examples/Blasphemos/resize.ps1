Add-Type -AssemblyName System.Drawing
$imagePath = "C:\Users\franc\.gemini\antigravity\brain\03fec54e-79e3-4151-a162-b7c2f2662ee1\penitent_climbing_ladder_32x32_1776476342986.png"
$img = [System.Drawing.Image]::FromFile($imagePath)

$out32 = New-Object System.Drawing.Bitmap 32, 32
$g32 = [System.Drawing.Graphics]::FromImage($out32)
$g32.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g32.DrawImage($img, 0, 0, 32, 32)
$g32.Dispose()

$out128 = New-Object System.Drawing.Bitmap 128, 128
$g128 = [System.Drawing.Graphics]::FromImage($out128)
$g128.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::NearestNeighbor
$g128.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::Half

# Upscale the downscaled image to 128x128
$g128.DrawImage($out32, 0, 0, 128, 128)

# Add a grid every 32 pixels for max visualization (32x32 per 8x8 block mapped)
$pen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(100, 255, 0, 0), 1)
for ($i = 0; $i -le 128; $i += 32) {
    if ($i -eq 128) { $x = 127 } else { $x = $i }
    $g128.DrawLine($pen, $x, 0, $x, 128)
    $g128.DrawLine($pen, 0, $x, 128, $x)
}
$pen.Dispose()

$out128.Save("c:\Workspace\NESFab\nesfab\examples\Blasphemos\assets\ladder_tiles.png", [System.Drawing.Imaging.ImageFormat]::Png)
$out32.Save("c:\Workspace\NESFab\nesfab\examples\Blasphemos\assets\ladder_32x32.png", [System.Drawing.Imaging.ImageFormat]::Png)

$g128.Dispose()
$out32.Dispose()
$out128.Dispose()
$img.Dispose()
Write-Host "Done"
